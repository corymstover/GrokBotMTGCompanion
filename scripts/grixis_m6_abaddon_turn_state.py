#!/usr/bin/env python3
"""Cycle 96: finite Abaddon stack and mana micro-engine.

Not a generic Magic rules engine, 99-card simulator, opponent-policy model,
win-rate estimator, or improvement certificate. Unsupported cards fail closed.
"""
from __future__ import annotations
import argparse,hashlib,json,random
from pathlib import Path
from grixis_m6_abaddon_followthrough import legal_payments
ROOT=Path(__file__).resolve().parents[1]
PLAN=ROOT/"data/grixis/m6/phase_b_plans/abaddon_turn_state_01.json"
SOURCE=ROOT/"exports/grixis-archidekt/source-baseline/abaddon-the-despoiler.txt"
PREV=ROOT/"data/grixis/m6/phase_b_bounded/abaddon_deckwide_access_01.json"
OUT=ROOT/"data/grixis/m6/phase_b_bounded/abaddon_turn_state_01.json"
AUTH={"can_decide":False,"can_apply_swap":False,"can_change_canonical_list":False,"can_approve_or_lock":False}
def sha(p): return "sha256:"+hashlib.sha256(p.read_bytes()).hexdigest()
def enc(o): return json.dumps(o,sort_keys=True,indent=2,ensure_ascii=False)+"\n"
def load(p): return json.loads(p.read_text(encoding="utf-8"))

# Exactly supported effects only. Test Spark/Echo are SYNTHETIC and never real deck inclusions.
CARDS={
 "Abaddon the Despoiler": {"mv":5,"cost":{"U":1,"B":1,"R":1,"generic":2},"type":"creature"},
 "Kessig Flamebreather": {"mv":2,"cost":{"R":1,"generic":1},"type":"creature"},
 "Birgi, God of Storytelling": {"mv":3,"cost":{"R":1,"generic":2},"type":"creature"},
 "Heartless Hidetsugu": {"mv":5,"cost":{"R":2,"generic":3},"type":"creature"},
 "Tree of Perdition": {"mv":4,"cost":{"B":1,"generic":3},"type":"creature"},
 "Solphim, Mayhem Dominus": {"mv":4,"cost":{"R":2,"generic":2},"type":"creature"},
 "Bloodletter of Aclazotz": {"mv":4,"cost":{"B":2,"generic":2},"type":"creature"},
 "Bituminous Blast": {"mv":5,"cost":{"B":1,"R":1,"generic":3},"type":"instant","printed_cascade":1},
 "Boltwave": {"mv":1,"cost":{"R":1,"generic":0},"type":"sorcery"},
 "Flame Rift": {"mv":2,"cost":{"R":1,"generic":1},"type":"sorcery"},
 "Test Spark": {"mv":1,"cost":{"generic":1},"type":"sorcery","synthetic":True},
 "Test Echo": {"mv":0,"cost":{"generic":0},"type":"sorcery","synthetic":True},
 "Test Land": {"mv":0,"cost":{},"type":"land","synthetic":True}
}
class Unsupported(Exception): pass

class TurnState:
 def __init__(self,hand=(),mana=None,library=(),opponents=(40,39,31),pilot=40,turn=1,target_creature=True):
  self.hand=list(hand);self.mana={c:int((mana or {}).get(c,0)) for c in "UBRC"}
  self.library=list(library);self.exile=[];self.graveyard=[]
  self.board={};self.stack=[];self.events=[]
  self.opponents=list(opponents);self.pilot=pilot;self.turn=turn
  self.lost=0;self.own_turn=True;self.command_casts=0
  self.target_creature=target_creature;self.prevent=set()
  self.rng=random.Random(9617)
  self.over=False;self._cascade_offer=None;self.command_ready=True
  for n in self.hand+self.library:
   if n not in CARDS:raise Unsupported("Unknown model card: "+n)

 def place(self,name,entered=0):
  if name not in CARDS or CARDS[name]["type"] in ("instant","sorcery","land"):
   raise Unsupported("Not a supported permanent: "+name)
  if name in self.board:raise ValueError("Duplicate battlefield permanent in singleton model")
  self.board[name]={"entered":entered,"tapped":False}
  if name=="Abaddon the Despoiler":self.command_ready=False
  self.events.append({"event":"setup_battlefield","name":name,"turn":self.turn})

 def remove(self,name):
  if name not in self.board:raise ValueError("Removal target not present")
  del self.board[name]
  if name=="Abaddon the Despoiler":self.command_ready=True
  else:self.graveyard.append(name)
  self.events.append({"event":"remove","name":name,"turn":self.turn})

 def _damage(self,opponent_amounts,self_amount=0):
  # Apply current replacement effects, THEN prevention, THEN life loss.
  for i,n in enumerate(opponent_amounts):
   n*=2 if "Solphim, Mayhem Dominus" in self.board else 1
   n=0 if i in self.prevent else n
   lost=n*(2 if self.own_turn and "Bloodletter of Aclazotz" in self.board else 1)
   self.opponents[i]-=lost;self.lost+=lost
  self.pilot-=self_amount
  self.over=(self.pilot<=0 or all(v<=0 for v in self.opponents))
  self.events.append({"event":"damage_resolved","opponents":list(self.opponents),"pilot":self.pilot,"lost_this_turn":self.lost})

 def cast(self,name,origin="hand",free=False):
  if self.over:raise ValueError("Game already ended")
  if name not in CARDS:raise Unsupported("Unmodeled card cast: "+name)
  card=CARDS[name]
  if card["type"]=="land":raise ValueError("Land cannot be cast")
  if origin=="hand":
   if name not in self.hand:raise ValueError("Spell not in hand")
   if free:raise ValueError("Free cast requires cascade resolver")
  elif origin=="command":
   if name!="Abaddon the Despoiler" or name in self.board or free or not self.command_ready:
    raise ValueError("Illegal command-zone cast")
  elif origin=="cascade_exile":
   if not free or self._cascade_offer!=name:raise ValueError("Only a resolving cascade may offer free exile cast")
  else:raise ValueError("Unsupported origin")
  if name=="Bituminous Blast" and not self.target_creature:raise ValueError("No legal creature target")
  if not free:
   cost=dict(card["cost"])
   cost["generic"]=cost.get("generic",0)+(2*self.command_casts if origin=="command" else 0)
   options=legal_payments(self.mana,cost)
   if not options:raise ValueError("Insufficient colored or generic mana")
   self.mana=max(options,key=lambda p:(p["U"]+p["B"]+p["R"],p["C"],p["R"]))
  if origin=="hand":self.hand.remove(name)
  if origin=="command":self.command_casts+=1;self.command_ready=False
  threshold=self.lost
  granted=int(bool(self.own_turn and origin=="hand" and "Abaddon the Despoiler" in self.board
                    and threshold>=card["mv"]))
  printed=card.get("printed_cascade",0)
  self.stack.append({"kind":"spell","name":name,"origin":origin})
  # Fixed controller stack order: printed, granted, Kessig, Birgi (last resolves first).
  for _ in range(printed):self.stack.append({"kind":"cascade","name":name,"why":"printed","mv":card["mv"]})
  for _ in range(granted):self.stack.append({"kind":"cascade","name":name,"why":"abaddon","mv":card["mv"]})
  if card["type"]!="creature" and "Kessig Flamebreather" in self.board:
   self.stack.append({"kind":"trigger","name":"Kessig Flamebreather"})
  if "Birgi, God of Storytelling" in self.board:
   self.stack.append({"kind":"trigger","name":"Birgi, God of Storytelling"})
  self.events.append({"event":"cast","name":name,"origin":origin,"turn":self.turn,
       "threshold_at_cast":threshold,"granted_cascade":granted,"printed_cascade":printed,
       "mana_remaining":dict(self.mana)})
  return granted+printed

 def tap_activate(self,name,target=0):
  if self.over:raise ValueError("Game already ended")
  if name not in ("Heartless Hidetsugu","Tree of Perdition"):
   raise Unsupported("Tap activation not implemented: "+name)
  b=self.board.get(name)
  if b is None or b["tapped"] or b["entered"]>=self.turn:
   raise ValueError("Tap ability unavailable or source summoning sick")
  if name=="Tree of Perdition" and not 0<=target<len(self.opponents):
   raise ValueError("Illegal opponent target")
  b["tapped"]=True
  self.stack.append({"kind":"activated","name":name,"target":target})
  self.events.append({"event":"activate","name":name,"turn":self.turn,"target":target})

 def resolve_top(self):
  if not self.stack:raise ValueError("No stack object")
  obj=self.stack.pop()
  k,n=obj["kind"],obj["name"]
  if k=="trigger":
   if n=="Birgi, God of Storytelling":
    self.mana["R"]+=1
    self.events.append({"event":"birgi_trigger_resolves","mana":dict(self.mana)})
   elif n=="Kessig Flamebreather":
    self._damage([1]*len(self.opponents))
   else:raise Unsupported("Unknown trigger "+n)
  elif k=="activated":
   if n=="Heartless Hidetsugu":
    self._damage([max(0,x//2) for x in self.opponents],max(0,self.pilot//2))
   elif n=="Tree of Perdition":
    if n not in self.board:
     self.events.append({"event":"tree_exchange_failed_source_absent"})
    else:
     i=obj["target"];before=self.opponents[i]
     if before>13:
      amount=(before-13)*(2 if self.own_turn and "Bloodletter of Aclazotz" in self.board else 1)
      self.opponents[i]-=amount;self.lost+=amount
     else:self.opponents[i]=13
     self.over=(self.pilot<=0 or all(x<=0 for x in self.opponents))
     self.events.append({"event":"tree_exchange","target":i,"opponents":list(self.opponents),
                         "lost_this_turn":self.lost})
  elif k=="spell":
   if CARDS[n]["type"]=="creature":
    self.place(n,entered=self.turn)
   elif n=="Boltwave":self._damage([3]*len(self.opponents))
   elif n=="Flame Rift":self._damage([4]*len(self.opponents),4)
   elif n=="Bituminous Blast":
    self.events.append({"event":"bituminous_blast_resolves","creature_damage":4,
                         "creature_damage_result_not_modeled":True})
   elif not CARDS[n].get("synthetic"):raise Unsupported("Unmodeled spell effect "+n)
   self.graveyard.append(n) if CARDS[n]["type"]!="creature" else None
   self.events.append({"event":"spell_resolves","name":n})
  elif k=="cascade":
   revealed=[];hit=None
   while self.library:
    c=self.library.pop(0)
    revealed.append(c)
    if CARDS[c]["type"]!="land" and CARDS[c]["mv"]<obj["mv"]:
     hit=c;break
   if hit is not None and hit=="Bituminous Blast" and not self.target_creature:hit=None
   if hit is not None:
    revealed.remove(hit)
    self.events.append({"event":"cascade_hit","from":n,"trigger_source":obj["why"],"hit":hit})
    self._cascade_offer=hit
    try:self.cast(hit,origin="cascade_exile",free=True)
    finally:self._cascade_offer=None
   else:self.events.append({"event":"cascade_no_cast","from":n,"trigger_source":obj["why"]})
   self.rng.shuffle(revealed);self.library+=revealed
  else:raise Unsupported("Unknown stack object "+k)
  return obj

 def resolve_all(self,max_steps=100):
  steps=0
  while self.stack:
   steps+=1
   if steps>max_steps:raise ValueError("Stack resolution limit")
   self.resolve_top()
   if self.over:
    self.events.append({"event":"game_ended_stack_abandoned","remaining_stack_objects":len(self.stack)})
    self.stack.clear();break
  return steps

 def next_turn(self):
  if self.stack:raise ValueError("Cannot skip an unresolved stack")
  self.turn+=1;self.lost=0;self.mana={c:0 for c in "UBRC"}
  for b in self.board.values():b["tapped"]=False
  self.events.append({"event":"new_controller_turn","turn":self.turn,"threshold":0})

def scenarios():
 # First spell's Kessig trigger cannot retroactively grant cascade, second can.
 a=TurnState(hand=["Test Spark","Test Spark"],mana={"C":2})
 a.place("Abaddon the Despoiler");a.place("Kessig Flamebreather")
 a.cast("Test Spark");a.resolve_all()
 a.cast("Test Spark");a.resolve_all()
 casts=[e for e in a.events if e["event"]=="cast"]
 assert [c["granted_cascade"] for c in casts]==[0,1] and a.lost==6
 # Birgi doesn't fund the triggering spell; red mana arrives afterward.
 b=TurnState(hand=["Boltwave","Boltwave"],mana={"R":1})
 b.place("Birgi, God of Storytelling");b.cast("Boltwave")
 assert b.mana["R"]==0
 b.resolve_all();assert b.mana["R"]==1
 b.cast("Boltwave");b.resolve_all();assert b.lost==18
 # Ability independence from source after tap: Heartless yes, Tree no.
 h=TurnState(turn=6);h.place("Heartless Hidetsugu",entered=5)
 h.tap_activate("Heartless Hidetsugu");h.remove("Heartless Hidetsugu");h.resolve_all()
 assert h.lost==54 and h.pilot==20
 t=TurnState(turn=6);t.place("Tree of Perdition",entered=5)
 t.tap_activate("Tree of Perdition");t.remove("Tree of Perdition");t.resolve_all()
 assert t.lost==0 and t.opponents[0]==40
 # Printed and granted cascade instances, with legal target.
 x=TurnState(hand=["Bituminous Blast"],mana={"B":1,"R":1,"C":3},library=["Test Echo"])
 x.place("Abaddon the Despoiler");x.lost=5
 assert x.cast("Bituminous Blast")==2
 x.resolve_all()
 assert len([e for e in x.events if e["event"]=="cascade_hit"])==1
 # Without commander, printed cascade still works.
 y=TurnState(hand=["Bituminous Blast"],mana={"B":1,"R":1,"C":3},library=["Test Echo"])
 assert y.cast("Bituminous Blast")==1;y.resolve_all()
 # Cascade from exile DOES trigger Kessig, but not Abaddon.
 z=TurnState(hand=["Test Spark"],mana={"C":1},library=["Test Echo"])
 z.place("Abaddon the Despoiler");z.place("Kessig Flamebreather");z.lost=3
 z.cast("Test Spark");z.resolve_all()
 c=[e for e in z.events if e["event"]=="cast"]
 assert len(c)==2 and c[1]["origin"]=="cascade_exile" and c[1]["granted_cascade"]==0
 # Return compact receipts (not outcomes / win rates).
 ret=[]
 for label,st in [("kessig_order",a),("birgi_order",b),("heartless_removed",h),
                  ("tree_removed",t),("bituminous_double",x),
                  ("bituminous_printed_only",y),("cascade_exile_cast",z)]:
  ret.append({"id":label,"events":st.events,"final":{"opponents":st.opponents,
    "pilot":st.pilot,"lost_this_turn":st.lost,"mana":st.mana,
    "stack_empty":not st.stack,"game_ended":st.over}})
 return ret

def build():
 plan=load(PLAN);prev=load(PREV)
 if (plan["cycle"]!=96 or plan["preregistration_status"]!="locked_before_tests"
     or plan["authority"]!=AUTH or prev["supports_improvement_claim"]
     or prev["full_phase_b_complete"] or sha(SOURCE)!="sha256:"+plan["baseline_export_sha256"]):
  raise ValueError("Approved source / prereg / prior evidence drift")
 if len(plan["scenarios"])!=7:raise ValueError("Unexpected preregistered scenarios")
 receipts=scenarios()
 if [v["id"] for v in receipts]!=[v["id"] for v in plan["scenarios"]]:
  raise ValueError("Receipt/scenario mismatch")
 return {"schema_version":1,"stage":"M6_Abaddon_deterministic_turn_state_microengine",
   "deck_id":plan["deck_id"],"canonical_hash":plan["canonical_hash"],
   "approved_raw_sha256":plan["approved_raw_sha256"],
   "baseline_export_sha256":sha(SOURCE),"plan_sha256":sha(PLAN),
   "prior_cycle_95_sha256":sha(PREV),"scenario_count":len(receipts),
   "scenarios":receipts,"supported_cards":sorted(CARDS),"limitations":plan["limits"],
   "actual_turn_state_effects_supported":True,"full_deck_paired_effect_simulator":False,
   "full_phase_b_complete":False,"supports_improvement_claim":False,"authority":AUTH}

def main():
 p=argparse.ArgumentParser();p.add_argument("--build",action="store_true");p.add_argument("--check",action="store_true")
 args=p.parse_args()
 if not (args.build or args.check):p.error("require --build or --check")
 text=enc(build())
 if args.build:OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(text,encoding="utf-8")
 if args.check and (not OUT.is_file() or OUT.read_text(encoding="utf-8")!=text):
  raise ValueError("Cycle 96 reproducibility drift")
 print("Cycle 96: seven real stack/mana effect microtraces; no full-deck or approval claim")
if __name__=="__main__":main()
