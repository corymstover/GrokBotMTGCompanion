#!/usr/bin/env python3
"""Cycle 102: bounded four-seat priority-pass + actual basic-source mana kernel.

No opponents are simulated. Four consecutive passes resolve the top stack frame
under the registered Cycle101 effect subset. Nonbasic land effects, extra costs,
cascade and actual opponent spell legality remain strictly unsupported.
"""
from __future__ import annotations
from contextlib import contextmanager
from grixis_m6_transactional_stack import TransactionalLedger,BlockedAction
from grixis_m6_state_kernel import BASIC_MANA
import grixis_sim

class PriorityBasics(TransactionalLedger):
 def __init__(self,*args,**kwargs):
  super().__init__(*args,**kwargs)
  self.priority_seat=0
  self.pass_count=0
  self.priority_events=[]

 @contextmanager
 def atomic(self):
  # Transactionally restore the new priority state as well as all inherited
  # physical zones, mana, life, stack and event fields on a blocked action.
  old=(self.priority_seat,self.pass_count,list(self.priority_events))
  try:
   with super().atomic():
    yield
  except Exception:
   self.priority_seat,self.pass_count,self.priority_events=old
   raise

 def cast(self,uid,origin="hand"):
  if self.priority_seat!=0:
   raise BlockedAction("Only the active modeled controller may cast in Cycle102")
  name=super().cast(uid,origin=origin)
  self.pass_count=0
  self.priority_seat=0
  self.priority_events.append({"event":"active_player_cast","card":name,
                               "priority_to":0})
  return name

 def play_basic(self,uid,own_turn=True,main_phase=True,stack_empty=True):
  if (self.priority_seat!=0 or self.pass_count!=0
      or self.frames or self.zones["stack"]):
   raise BlockedAction("Basic land play requires active main-phase priority and empty stack")
  if not self.own_turn or not self.main_phase:
   raise BlockedAction("Basic land play requires own main phase")
  with self.atomic():
   return super().play_basic(uid,own_turn=own_turn,main_phase=main_phase,
                             stack_empty=stack_empty)

 def pass_priority(self):
  """Pass once in seats 0->1->2->3. Four passes resolve one stack frame.

  The engine makes no claim about opponents' strategic choices. Opponents in
  the default policy simply pass; scripted counter is a labeled external outcome.
  """
  with self.atomic():
   passed=self.priority_seat
   self.pass_count+=1
   self.priority_seat=(self.priority_seat+1)%4
   self.priority_events.append({"event":"priority_pass","seat":passed,
                                "consecutive":self.pass_count})
   if self.pass_count==4:
    if self.frames:
     top=super().resolve_top()
     self.priority_events.append({"event":"four_passes_resolve_top",
                                   "frame_kind":top["kind"],
                                   "uid":top.get("uid")})
    else:
     self.priority_events.append({"event":"four_passes_empty_stack",
                                   "no_phase_transition_modeled":True})
    self.pass_count=0
    self.priority_seat=0
   self.validate_stack()
  return self.priority_seat

 def resolve_by_passes(self,limit=48):
  if not isinstance(limit,int) or limit<=0:
   raise BlockedAction("Invalid priority pass cap")
  n=0
  while self.frames:
   if n+4>limit:raise BlockedAction("Priority pass cap hit")
   for _ in range(4):self.pass_priority();n+=1
  return n

 def resolve_top(self):
  raise BlockedAction("Cannot resolve stack frame without four successive priority passes")

 def scripted_counter_spell(self,uid):
  if self.priority_seat not in (1,2,3):
   raise BlockedAction("Scripted opponent response requires opponent priority")
  with self.atomic():
   opponent=self.priority_seat
   result=super().scripted_counter_spell(uid)
   self.priority_seat=0
   self.pass_count=0
   self.priority_events.append({"event":"scripted_counter_at_opponent_priority",
        "seat":opponent,"target_uid":uid,
        "actual_counterspell_and_mana_NOT_modeled":True})
   return result

 def scripted_remove_permanent(self,uid):
  if self.priority_seat not in (1,2,3):
   raise BlockedAction("Scripted removal outcome requires opponent priority")
  with self.atomic():
   opponent=self.priority_seat
   super().scripted_remove_permanent(uid)
   self.priority_seat=0
   self.pass_count=0
   self.priority_events.append({"event":"scripted_removal_at_opponent_priority",
        "seat":opponent,"target_uid":uid,
        "actual_removal_spell_and_targets_NOT_modeled":True})

 def next_turn(self):
  if self.priority_seat!=0 or self.pass_count:
   raise BlockedAction("Unfinished priority round cannot advance turn")
  with self.atomic():
   super().next_turn()
   self.priority_events.append({"event":"start_next_sampled_controller_turn",
       "turn":self.turn,"not_full_turn_structure":True})

 def cast_with_basic_sources(self,uid,origin="hand"):
  """Source-backed *registered* cast, no injected/floating mana.

  Preselect tapped mana sources with exact pip matching and roll back all
  tapped-state, mana and hand changes if any underlying cast fails. This
  preflight intentionally does not model Signet as a mana source.
  """
  if any(self.mana.values()):
   raise BlockedAction("Basic-only source planner requires empty floating pool")
  if self.priority_seat!=0 or self.frames:
   raise BlockedAction("Basic-only planner requires uncontested controller priority")
  name,spec,cost=self._registered(uid)
  if self.zone_of(uid)!=origin:raise BlockedAction("Card unavailable")
  tax=2*self.command_casts.get(uid,0) if origin=="command" else 0
  sources=[i for i in self.zones["battlefield"]
           if self.cards[i]["name"] in BASIC_MANA
           and self.cards[i].get("land") and i not in self.tapped]
  sources.sort()
  units=[frozenset((BASIC_MANA[self.cards[i]["name"]],)) for i in sources]
  payment=grixis_sim.can_pay(cost,units,tax=tax)
  if payment is None:raise BlockedAction("Not enough physically available untapped basic sources")
  chosen=[sources[i] for i in payment]
  with self.atomic():
   for src in chosen:self.tap_basic(src)
   self.cast(uid,origin=origin)
   self.priority_events.append({"event":"actual_basic_source_payment",
     "name":name,"source_ids":chosen,"not_injected_mana":True})
  return chosen
