#!/usr/bin/env python3
"""Cycle104: strict fetch search/stack, Ancient Tomb mana, City of Brass trigger.

A small versioned extension of Cycle103 physical-ID state; not the full MTG
rules engine. Player decisions use registered deterministic policies, and
unsupported card effects, lethal payments and opponent spells fail closed.
"""
from __future__ import annotations
import copy,itertools,random,hashlib
from contextlib import contextmanager
import grixis_sim
from grixis_m6_priority_nonbasic import PriorityNonbasic,LANDS,TYPED,colors
from grixis_m6_state_kernel import BASIC_MANA,BlockedAction
from grixis_m6_transactional_stack import TransactionalLedger

FETCHES={
 "Bloodstained Mire":("Swamp","Mountain"),
 "Polluted Delta":("Island","Swamp"),
 "Scalding Tarn":("Island","Mountain"),
 "Marsh Flats":("Plains","Swamp"),
 "Flooded Strand":("Plains","Island"),
 "Misty Rainforest":("Forest","Island"),
 "Verdant Catacombs":("Swamp","Forest"),
 "Wooded Foothills":("Mountain","Forest"),
 "Arid Mesa":("Mountain","Plains"),
 "Windswept Heath":("Forest","Plains")
}
SPECIALS=("Ancient Tomb","City of Brass")
MODEL_LANDS=set(LANDS)|set(BASIC_MANA)|set(FETCHES)|set(SPECIALS)

class PriorityFetchCityTomb(PriorityNonbasic):
 def __init__(self,*args,**kwargs):
  super().__init__(*args,**kwargs)
  self._defer_city=False
  self._pending_city=[]
  self.fetch_resolutions=0
  self.fetch_search_events=[]
  self.utility_events=[]

 @contextmanager
 def atomic(self):
  extras=("_defer_city","_pending_city","fetch_resolutions","fetch_search_events","utility_events")
  prior={k:copy.deepcopy(getattr(self,k)) for k in extras}
  try:
   with super().atomic():
    yield
  except Exception:
   for k,v in prior.items():setattr(self,k,v)
   raise

 def play_supported_land(self,uid,pay_shock=None):
  if uid not in self.cards:raise BlockedAction("Unknown land")
  name=self.cards[uid]["name"]
  if name not in FETCHES and name not in SPECIALS:
   return super().play_supported_land(uid,pay_shock=pay_shock)
  if pay_shock is not None:raise BlockedAction("Shock choice only applies to shock ETB")
  if not self.cards[uid].get("land",False) or self.zone_of(uid)!="hand":
   raise BlockedAction("Special land must actually be in hand")
  if (self.land_played or not self.own_turn or not self.main_phase or self.priority_seat!=0
      or self.pass_count or self.frames or self.zones["stack"]):
   raise BlockedAction("Land play unavailable in modeled main phase")
  with self.atomic():
   self.transfer(uid,"hand","battlefield")
   self.land_played=True
   self.utility_events.append({"event":"supported_special_land_play","name":name,"id":uid})
  return True

 def activate_fetch(self,uid):
  if uid not in self.cards or self.cards[uid]["name"] not in FETCHES:
   raise BlockedAction("Not an implemented fetchland")
  name=self.cards[uid]["name"]
  if (self.zone_of(uid)!="battlefield" or uid in self.tapped or self.pilot<=1
      or self.priority_seat!=0 or not self.priority
      or self.pass_count or self.frames):
   raise BlockedAction("Fetch cost unavailable or priority/response window unsupported")
  with self.atomic():
   self.tapped.add(uid)
   self.pilot-=1  # activation cost, not damage; never counts toward Abaddon
   self.transfer(uid,"battlefield","graveyard") # sacrifice is a COST
   self.frames.append({"kind":"trigger","name":"fetchland_search","source_uid":uid,
                       "subtypes":list(FETCHES[name])})
   self.priority_seat=0;self.pass_count=0
   self.utility_events.append({"event":"fetch_activated_costs_paid","name":name,
       "source_uid":uid,"pilot_life":self.pilot,"sacrificed_before_resolution":True,
       "target_not_chosen_yet":True,"opponent_loss":self.opponents_lost_this_turn})
  return name

 def _subtypes(self,uid):
  name=self.cards[uid]["name"]
  if name in BASIC_MANA:return {name}
  return set(TYPED.get(name,"").split())

 def _resolve_fetch(self,obj):
  desired=set(obj["subtypes"])
  battlefield_lands=[u for u in self.zones["battlefield"] if self.cards[u].get("land",False)]
  candidates=[]
  possible_unmodeled=0
  for uid in self.zones["library"]:
   n=self.cards[uid]["name"]
   if not self.cards[uid].get("land",False):continue
   if n not in set(LANDS)|set(BASIC_MANA):
    possible_unmodeled+=1
    continue
   if not self._subtypes(uid)&desired:continue
   shock=(n in LANDS and LANDS[n][1]=="shock")
   pay_shock=shock and self.pilot>2
   tapped=self._enter_tapped(uid,battlefield_lands,pay_shock)
   options=colors(n)
   # Policy is declared and fixed: untapped first, then more color options,
   # then alphabetical name and physical ID, NOT a rational tutor optimizer.
   candidates.append(((int(tapped),-len(options),n,uid),uid,pay_shock,tapped))
  candidates.sort(key=lambda z:z[0])
  selected=candidates[0] if candidates else None
  selected_name=None;entered_tapped=None;shock_paid=False
  if selected is not None:
   _,uid,pay_shock,tapped=selected
   selected_name=self.cards[uid]["name"]
   self.transfer(uid,"library","battlefield")
   if tapped:self.tapped.add(uid)
   if pay_shock:
    self.pilot-=2
    shock_paid=True
   entered_tapped=tapped
  # The search finishes by shuffling ALL remaining library physical IDs,
  # whether a target was found or intentionally failed to find.
  self.fetch_resolutions+=1
  rng=random.Random(self.seed ^ (self.fetch_resolutions*0x9e3779b1))
  rng.shuffle(self.zones["library"])
  rec={"event":"fetch_search_resolved","fetch_source":obj["source_uid"],
       "selected":selected_name,"selected_uid":selected[1] if selected else None,
       "entered_tapped":entered_tapped,"shock_paid_2_life":shock_paid,
       "unmodeled_land_names_in_library_before_search":possible_unmodeled,
       "library_shuffled":True,"pilot_life":self.pilot,
       "eligible_modeled_targets":len(candidates),
       "opponent_loss":self.opponents_lost_this_turn}
  self.fetch_search_events.append(rec)
  self.utility_events.append(rec)
  return rec

 def tap_land(self,uid,color):
  if uid not in self.cards:raise BlockedAction("Unknown physical land")
  name=self.cards[uid]["name"]
  if name not in SPECIALS:return super().tap_land(uid,color)
  if (self.zone_of(uid)!="battlefield" or uid in self.tapped
      or self.priority_seat!=0 or not self.priority):
   raise BlockedAction("Special land is tapped/absent or cannot be activated")
  if name=="Ancient Tomb" and color!="C":raise BlockedAction("Ancient Tomb only produces C C")
  if name=="City of Brass" and color not in ("U","B","R"):
   raise BlockedAction("City of Brass color outside registered Grixis identity")
  if name=="Ancient Tomb" and self.pilot<=2:
   raise BlockedAction("Potentially lethal Ancient Tomb damage not modeled")
  if name=="City of Brass" and self.pilot<=1:
   raise BlockedAction("Potentially lethal City trigger not modeled")
  with self.atomic():
   self.tapped.add(uid)
   self.mana[color]+=2 if name=="Ancient Tomb" else 1
   if name=="Ancient Tomb":
    self.pilot-=2 # damage DURING mana-ability resolution, not stack.
    self.utility_events.append({"event":"ancient_tomb_mana_and_damage",
       "source_uid":uid,"colorless_added":2,"immediate_pilot_damage":2,
       "pilot_life":self.pilot,"opponent_loss":self.opponents_lost_this_turn,
       "no_damage_trigger_created":True})
   else:
    frame={"kind":"trigger","name":"City of Brass","source_uid":uid}
    if self._defer_city:self._pending_city.append(frame)
    else:self.frames.append(frame)
    self.utility_events.append({"event":"city_mana_tapped_trigger_pending",
       "source_uid":uid,"mana_color":color,
       "deferred_until_after_cast":self._defer_city,
       "pilot_life":self.pilot})
  return color

 def pass_priority(self):
  # Cycle102 dispatch explicitly calls TransactionalLedger.resolve_top, not
  # virtual subclass resolution. Override only to support two new named stack
  # frames, keeping identical four-consecutive-pass semantics.
  with self.atomic():
   passed=self.priority_seat
   self.pass_count+=1;self.priority_seat=(self.priority_seat+1)%4
   self.priority_events.append({"event":"priority_pass","seat":passed,
        "consecutive":self.pass_count})
   if self.pass_count==4:
    if self.frames:
     obj=self.frames[-1]
     if obj["kind"]=="trigger" and obj["name"] in ("fetchland_search","City of Brass"):
      top=self.frames.pop()
      if top["name"]=="fetchland_search":self._resolve_fetch(top)
      else:
       # City damage uses the stack. It persists even if the tapped land left play.
       if self.pilot<=1:raise BlockedAction("City lethal damage response not modeled")
       self.pilot-=1
       self.utility_events.append({"event":"city_of_brass_damage_resolves",
          "source_uid":top["source_uid"],"pilot_life":self.pilot,
          "opponent_loss":self.opponents_lost_this_turn})
     else:top=TransactionalLedger.resolve_top(self)
     self.priority_events.append({"event":"four_passes_resolve_top",
                                  "frame_kind":top["kind"],"name":top.get("name")})
    else:self.priority_events.append({"event":"four_passes_empty_stack","phase_not_modeled":True})
    self.pass_count=0;self.priority_seat=0
   self.validate_stack()
  return self.priority_seat

 def cast_with_land_sources(self,uid,origin="hand"):
  if any(self.mana.values()) or self.frames or self.pass_count or self.priority_seat!=0:
   raise BlockedAction("Planner requires empty floating mana and clear active priority")
  name,spec,cost=self._registered(uid)
  if self.zone_of(uid)!=origin:raise BlockedAction("Spell not available")
  tax=2*self.command_casts.get(uid,0) if origin=="command" else 0
  needed=len(cost["pips"])+cost["generic"]+tax
  if needed<1:raise BlockedAction("Zero cost unmodeled by this planner")
  sources=sorted(i for i in self.zones["battlefield"] if self.cards[i].get("land")
    and i not in self.tapped and self.cards[i]["name"] in MODEL_LANDS
    and self.cards[i]["name"] not in FETCHES)
  if not sources:raise BlockedAction("No modeled untapped land sources")
  solutions=[]
  # Enumerate candidate subsets up to printed mana unit count; Ancient Tomb
  # contributes TWO units, unlike ordinary land. Avoid greedy colored errors.
  for size in range(1,min(len(sources),needed)+1):
   for subset in itertools.combinations(sources,size):
    generated=[]
    for src in subset:
     n=self.cards[src]["name"]
     generated.append(("C",) if n=="Ancient Tomb" else
                      ("U","B","R") if n=="City of Brass" else colors(n))
    life_damage=sum(2 if self.cards[src]["name"]=="Ancient Tomb" else
                    1 if self.cards[src]["name"] in ("City of Brass","Mana Confluence")
                    else 0 for src in subset)
    if self.pilot<=life_damage:continue
    for assignment in itertools.product(*generated):
     units=[frozenset((c,)) for u,c in zip(subset,assignment)
            for _ in range(2 if self.cards[u]["name"]=="Ancient Tomb" else 1)]
     if grixis_sim.can_pay(cost,units,tax=tax) is None:continue
     score=(life_damage,len(subset),subset,assignment)
     solutions.append((score,subset,assignment))
  if not solutions:raise BlockedAction("Unsupported or insufficient physically available mana colors")
  _,selected,assignment=min(solutions,key=lambda q:q[0])
  with self.atomic():
   self._defer_city=True
   for src,color in zip(selected,assignment):self.tap_land(src,color)
   self.cast(uid,origin=origin)
   # Controller-selected fixed stack order: City triggers above cast/other
   # triggers; none of the mana ability or their triggered abilities is a spell.
   self.frames.extend(self._pending_city)
   self._pending_city=[]
   self._defer_city=False
   self.utility_events.append({"event":"real_source_spell_payment","spell":name,
      "source_ids":list(selected),"colors":list(assignment),
      "ancient_tomb_used":any(self.cards[x]["name"]=="Ancient Tomb" for x in selected),
      "city_triggers_on_stack":sum(self.cards[x]["name"]=="City of Brass" for x in selected),
      "not_injected_mana":True})
  return list(selected)
