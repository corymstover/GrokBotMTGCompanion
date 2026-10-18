#!/usr/bin/env python3
"""Cycle 101: transactional, bounded *real-card* spell casting over Cycle 100 IDs.

Six registered spells/permanents only. A real Magic Comprehensive Rules engine,
multiplayer opponent policy, cascade executor or optimization metric is NOT provided.
All other effects and active Abaddon-granted cascade fail closed before changing
cards, mana, life or the stack. Scripted counter/removal are external response
*outcomes*, not modeled spells or probabilistic gameplay.
"""
from __future__ import annotations
import copy
from contextlib import contextmanager
import grixis_sim
from grixis_m6_state_kernel import Ledger,BlockedAction,MANA

SUPPORTED={
 "Abaddon the Despoiler":{"kind":"creature","cost":"{2}{U}{B}{R}"},
 "Kessig Flamebreather":{"kind":"creature","cost":"{1}{R}"},
 "Dark Ritual":{"kind":"instant","cost":"{B}"},
 "Boltwave":{"kind":"sorcery","cost":"{R}"},
 "Flame Rift":{"kind":"sorcery","cost":"{1}{R}"},
 "Arcane Signet":{"kind":"artifact","cost":"{2}"}
}
class TransactionalLedger(Ledger):
 def __init__(self,main_cards,commanders,seed=1,opponents=(40,39,31),pilot=40):
  super().__init__(main_cards,commanders,seed)
  self.frames=[]                         # virtual triggered abilities plus physical spells
  self.opponents=list(opponents)
  self.pilot=int(pilot)
  self.opponents_lost_this_turn=0
  self.command_casts={}
  self.own_turn=True
  self.main_phase=True
  self.priority=True
  self.outcome_events=[]

 @contextmanager
 def atomic(self):
  keys=("zones","mana","tapped","events","frames","opponents","pilot",
        "opponents_lost_this_turn","command_casts","outcome_events","land_played","turn")
  snap={k:copy.deepcopy(getattr(self,k)) for k in keys}
  try:
   yield
   self.check()
   self.validate_stack()
  except Exception:
   for k,v in snap.items():setattr(self,k,v)
   raise

 def validate_stack(self):
  stack_cards=[f["uid"] for f in self.frames if f["kind"]=="spell"]
  if len(stack_cards)!=len(set(stack_cards)) or set(stack_cards)!=set(self.zones["stack"]):
   raise AssertionError("Pending spell frames and physical stack card IDs diverge")
  if any(f["kind"] not in ("spell","trigger") for f in self.frames):
   raise AssertionError("Unrecognized virtual stack frame")
  if self.pilot<=0:
   # No state-based action / game-end handling beyond explicit pilot-lives report.
   pass
  return True

 def inject_mana(self,units):
  """TEST SETUP ONLY, not tapped-land mana development or a real game."""
  if set(units)-set(MANA) or any(not isinstance(n,int) or n<0 for n in units.values()):
   raise BlockedAction("Invalid scripted mana")
  with self.atomic():
   for c,n in units.items():self.mana[c]+=n
   self.outcome_events.append({"event":"scripted_injected_mana","units":dict(units),
        "not_gameplay":True})

 def _registered(self,uid):
  if uid not in self.cards:raise BlockedAction("Unknown card ID")
  name=self.cards[uid]["name"]
  spec=SUPPORTED.get(name)
  if spec is None:raise BlockedAction("Unregistered card effect: "+name)
  card=self.cards[uid]
  if card.get("land",False):raise BlockedAction("Land is not a spell")
  printed=card.get("cost")
  if not isinstance(printed,dict) or printed.get("life",0):
   raise BlockedAction("Additional/Phyrexian/unknown cost is unsupported")
  if printed!=grixis_sim.parse_cost(spec["cost"]):
   raise BlockedAction("Oracle printed cost mismatch: "+name)
  return name,spec,printed

 def _payment(self,cost,tax=0):
  units=[frozenset((col,)) for col in MANA for _ in range(self.mana[col])]
  indexes=grixis_sim.can_pay(cost,units,tax=tax)
  if indexes is None:raise BlockedAction("Cannot pay exact colored/generic printed mana and commander tax")
  after=dict(self.mana)
  for i in indexes:
   col=next(iter(units[i]))
   after[col]-=1
  if any(v<0 for v in after.values()):raise AssertionError("Negative mana in payment")
  return after

 def cast(self,uid,origin="hand"):
  """Cast exactly one registered card; spell and triggered ability are stack frames.

  No default legal priority inference. The caller supplies priority/main phase;
  unsupported effects stop before mana/zone movement.
  """
  name,spec,cost=self._registered(uid)
  if origin not in ("hand","command"):raise BlockedAction("Origin not supported")
  if self.zone_of(uid)!=origin:raise BlockedAction("Card not available in stated origin")
  if not self.priority:raise BlockedAction("No modeled player priority")
  if origin=="command" and (uid[0]!="c" or name!="Abaddon the Despoiler"):
   raise BlockedAction("Command cast permitted only for Abaddon in this adapter")
  if origin=="hand" and uid.startswith("c"):
   raise BlockedAction("Commander physical ID not in hand")
  if spec["kind"]!="instant" and (not self.own_turn or not self.main_phase or self.frames):
   raise BlockedAction("Normal permanent/sorcery requires own main phase and empty stack")
  # Abaddon grants cascade to hand-cast spells; don't silently ignore that effect.
  commander_present=any(self.cards[x]["name"]=="Abaddon the Despoiler" for x in self.zones["battlefield"])
  card_mv=int(self.cards[uid].get("mv",-1))
  if card_mv<0:raise BlockedAction("Missing Oracle mana value")
  if (origin=="hand" and self.own_turn and commander_present
      and self.opponents_lost_this_turn>=card_mv):
   raise BlockedAction("Abaddon-granted cascade unsupported by Cycle101 adapter")
  tax=2*self.command_casts.get(uid,0) if origin=="command" else 0
  mana_after=self._payment(cost,tax)
  with self.atomic():
   self.mana=mana_after
   self.transfer(uid,origin,"stack")
   self.frames.append({"kind":"spell","uid":uid,"name":name,"origin":origin})
   if origin=="command":self.command_casts[uid]=self.command_casts.get(uid,0)+1
   # Kessig trigger is created ON CAST, not when its initiating spell resolves.
   if spec["kind"] not in ("creature",) and any(
       self.cards[x]["name"]=="Kessig Flamebreather" for x in self.zones["battlefield"]):
    source=next(x for x in self.zones["battlefield"]
                if self.cards[x]["name"]=="Kessig Flamebreather")
    self.frames.append({"kind":"trigger","source_uid":source,"name":"Kessig Flamebreather",
                        "triggered_by":uid})
   self.outcome_events.append({"event":"supported_cast","name":name,"id":uid,
           "origin":origin,"paid_tax":tax,"pending_frames":len(self.frames),
           "remaining_mana":dict(self.mana),"no_cascade_eligible":True})
  return name

 def _opponent_damage(self,n):
  self.opponents=[life-n for life in self.opponents]
  self.opponents_lost_this_turn+=n*len(self.opponents)

 def resolve_top(self):
  if not self.frames:raise BlockedAction("No modeled stack frame")
  top=self.frames[-1]
  with self.atomic():
   self.frames.pop()
   if top["kind"]=="trigger":
    if top["name"]!="Kessig Flamebreather":
     raise BlockedAction("Unsupported trigger")
    self._opponent_damage(1)
    self.outcome_events.append({"event":"kessig_trigger_resolved",
        "source_uid":top["source_uid"],"triggered_by":top["triggered_by"],
        "opponent_lost":3,"trigger_survives_source_or_spell_removal":True})
   else:
    uid=top["uid"];name=top["name"]
    if self.zone_of(uid)!="stack":raise BlockedAction("Stack zone missing spell")
    if name in ("Abaddon the Despoiler","Kessig Flamebreather","Arcane Signet"):
     destination="battlefield"
    elif name=="Dark Ritual":
     self.mana["B"]+=3
     destination="graveyard"
    elif name=="Boltwave":
     self._opponent_damage(3)
     destination="graveyard"
    elif name=="Flame Rift":
     self._opponent_damage(4)
     self.pilot-=4
     destination="graveyard"
    else:raise BlockedAction("Unsupported resolving effect")
    self.transfer(uid,"stack",destination)
    self.outcome_events.append({"event":"supported_resolution","id":uid,"name":name,
       "destination":destination,"opponents":list(self.opponents),
       "pilot":self.pilot,"opponents_lost_this_turn":self.opponents_lost_this_turn})
  return top

 def resolve_all(self):
  steps=0
  while self.frames:
   if steps>=25:raise BlockedAction("Resolution cap exceeded")
   self.resolve_top();steps+=1
  return steps

 def scripted_counter_spell(self,uid):
  """Recorded *outcome* of an opponent counter. No legal counter spell or mana."""
  idx=next((i for i,f in enumerate(self.frames)
            if f["kind"]=="spell" and f["uid"]==uid),None)
  if idx is None or self.zone_of(uid)!="stack":
   raise BlockedAction("No pending physical spell with that ID")
  if uid.startswith("c"):
   raise BlockedAction("Commander counter replacement choice not modeled")
  with self.atomic():
   del self.frames[idx]
   self.transfer(uid,"stack","graveyard")
   self.outcome_events.append({"event":"scripted_counter_outcome","id":uid,
      "no_opponent_spell_cast_or_priority_simulated":True})
  return uid

 def scripted_remove_permanent(self,uid):
  """Recorded removal *outcome*, not legal targeted removal stack sequence."""
  if self.zone_of(uid)!="battlefield" or uid.startswith("c"):
   raise BlockedAction("Only supported noncommander battlefield removal outcome")
  with self.atomic():
   self.transfer(uid,"battlefield","graveyard")
   self.outcome_events.append({"event":"scripted_remove_permanent","id":uid,
           "no_opponent_spell_cast_or_priority_simulated":True})

 def commander_to_command(self,uid):
  """Explicit user/fixture choice of command-zone replacement after removal.

  NOT a default model of death/exile rules or replacement timing.
  """
  if uid not in self.zones["battlefield"] or not uid.startswith("c"):
   raise BlockedAction("Commander not on battlefield")
  with self.atomic():
   self.transfer(uid,"battlefield","command")
   self.outcome_events.append({"event":"scripted_command_zone_choice","id":uid,
         "replacement_rules_not_modeled":True})

 def tap_signet(self,uid,color):
  if color not in ("U","B","R") or self.zone_of(uid)!="battlefield" or uid in self.tapped:
   raise BlockedAction("Arcane Signet Grixis mana ability unavailable")
  if self.cards[uid]["name"]!="Arcane Signet":
   raise BlockedAction("Wrong artifact")
  with self.atomic():
   self.tapped.add(uid)
   self.mana[color]+=1
   self.outcome_events.append({"event":"arcane_signet_tapped","id":uid,"mana_color":color})
  return color

 def next_turn(self):
  if self.frames or self.zones["stack"]:raise BlockedAction("Pending spell or trigger at turn boundary")
  with self.atomic():
   super().next_turn()
   self.opponents_lost_this_turn=0
   self.outcome_events.append({"event":"turn_reset","turn":self.turn})
