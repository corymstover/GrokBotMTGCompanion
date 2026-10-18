#!/usr/bin/env python3
"""Cycle 103: limited Oracle-gated nonbasic land state and real mana sourcing.

Strict subset; all other nonbasic lands fail closed. No land effects beyond named
mana/ETB are modeled. No gameplay, opponents' actions or deck-strength estimates.
"""
from __future__ import annotations
import itertools
from grixis_m6_priority_basics import PriorityBasics,BlockedAction
from grixis_m6_state_kernel import BASIC_MANA
import grixis_sim

LANDS={
 "Command Tower":("UBR","always"),"Crumbling Necropolis":("UBR","tapped"),
 "Xander's Lounge":("UBR","tapped"),
 "Underground Sea":("UB","always"),"Volcanic Island":("UR","always"),
 "Badlands":("BR","always"),
 "Watery Grave":("UB","shock"),"Steam Vents":("UR","shock"),"Blood Crypt":("BR","shock"),
 "Drowned Catacomb":("UB","typed"),"Sulfur Falls":("UR","typed"),
 "Dragonskull Summit":("BR","typed"),
 "Spirebluff Canal":("UR","fast"),"Darkslick Shores":("UB","fast"),
 "Blackcleave Cliffs":("BR","fast"),
 "Morphic Pool":("UB","bond"),"Training Center":("UR","bond"),
 "Luxury Suite":("BR","bond"),"Mana Confluence":("UBR","life_mana")
}
# Land subtype effects are NOT emulated from names outside this exact Oracle
# verified group. Basic type presence can count even if the typed land is tapped.
TYPED={
 "Underground Sea":"Island Swamp","Volcanic Island":"Island Mountain",
 "Badlands":"Swamp Mountain","Watery Grave":"Island Swamp",
 "Steam Vents":"Island Mountain","Blood Crypt":"Swamp Mountain",
 "Xander's Lounge":"Island Swamp Mountain"
}
REQUIRES={
 "Drowned Catacomb":("Island","Swamp"),
 "Sulfur Falls":("Island","Mountain"),
 "Dragonskull Summit":("Swamp","Mountain")
}
def colors(name):
 if name in BASIC_MANA:return (BASIC_MANA[name],)
 if name in LANDS:return tuple(LANDS[name][0])
 raise BlockedAction("Unmodeled land mana: "+name)

class PriorityNonbasic(PriorityBasics):
 def __init__(self,*args,opponent_count=3,**kwargs):
  super().__init__(*args,**kwargs)
  if opponent_count not in (0,1,2,3):raise BlockedAction("Unmodeled opponent count")
  self.opponent_count=opponent_count

 def _land_subtypes(self,uid):
  n=self.cards[uid]["name"]
  return set((TYPED.get(n,n if n in BASIC_MANA else "")).split())

 def _enter_tapped(self,uid,other_lands,pay_shock):
  name=self.cards[uid]["name"]
  if name in BASIC_MANA:return False
  tag=LANDS[name][1]
  if tag in ("always","life_mana"):return False
  if tag=="tapped":return True
  if tag=="shock":return not pay_shock
  if tag=="fast":return len(other_lands)>2
  if tag=="bond":return self.opponent_count<2
  if tag=="typed":
   want=set(REQUIRES[name])
   return not any(self._land_subtypes(i)&want for i in other_lands)
  raise BlockedAction("Unsupported land entry condition")

 def play_supported_land(self,uid,pay_shock=None):
  if uid not in self.cards:raise BlockedAction("Unknown physical card")
  card=self.cards[uid];name=card["name"]
  if not card.get("land",False) or name not in LANDS and name not in BASIC_MANA:
   raise BlockedAction("Land is unsupported or not an actual land")
  if self.zone_of(uid)!="hand" or self.land_played or not self.own_turn or not self.main_phase:
   raise BlockedAction("Land drop unavailable")
  if self.priority_seat!=0 or self.pass_count or self.frames or self.zones["stack"]:
   raise BlockedAction("Land plays require own main-phase priority, empty stack")
  other=[i for i in self.zones["battlefield"] if self.cards[i].get("land",False)]
  tag=LANDS[name][1] if name in LANDS else "basic"
  if tag=="shock":
   if pay_shock is None:pay_shock=self.pilot>2
   if not isinstance(pay_shock,bool):raise BlockedAction("Shock-land life choice required")
   if pay_shock and self.pilot<2:raise BlockedAction("Cannot pay 2 life")
  elif pay_shock is not None:raise BlockedAction("Only shocklands accept 2-life entry choice")
  tapped=self._enter_tapped(uid,other,pay_shock)
  with self.atomic():
   self.transfer(uid,"hand","battlefield")
   if tapped:self.tapped.add(uid)
   if tag=="shock" and pay_shock:self.pilot-=2
   self.land_played=True
   self.priority_events.append({"event":"supported_land_play","name":name,"id":uid,
     "entered_tapped":tapped,"shock_paid_two_life":bool(tag=="shock" and pay_shock),
     "life":self.pilot,"other_lands_before_entry":len(other),"turn":self.turn})
  return not tapped

 def tap_land(self,uid,color):
  if uid not in self.cards:raise BlockedAction("Unknown card ID")
  if self.zone_of(uid)!="battlefield" or uid in self.tapped:
   raise BlockedAction("Land is absent or tapped")
  name=self.cards[uid]["name"]
  if name not in LANDS and name not in BASIC_MANA or not self.cards[uid].get("land",False):
   raise BlockedAction("Unsupported land activation")
  if color not in colors(name):raise BlockedAction("Land cannot produce that mana color")
  if name=="Mana Confluence" and self.pilot<=1:
   raise BlockedAction("Life payment would need game-ending state modeling")
  with self.atomic():
   self.tapped.add(uid)
   if name=="Mana Confluence":self.pilot-=1
   self.mana[color]+=1
   self.priority_events.append({"event":"supported_land_mana","name":name,
     "id":uid,"color":color,"pilot_life":self.pilot,
     "activation_life_paid":int(name=="Mana Confluence"),
     "opponents_lost_this_turn":self.opponents_lost_this_turn})
  return color

 def cast_with_land_sources(self,uid,origin="hand"):
  if any(self.mana.values()):raise BlockedAction("Planner expects empty floating mana")
  if self.priority_seat!=0 or self.pass_count or self.frames:
   raise BlockedAction("Planner requires active controller priority and empty stack")
  name,spec,cost=self._registered(uid)
  if self.zone_of(uid)!=origin:raise BlockedAction("Spell not in source zone")
  tax=2*self.command_casts.get(uid,0) if origin=="command" else 0
  needed=len(cost["pips"])+cost["generic"]+tax
  if needed<=0:raise BlockedAction("Zero-cost casting handled separately")
  sources=sorted(i for i in self.zones["battlefield"] if self.cards[i].get("land",False)
     and i not in self.tapped and (self.cards[i]["name"] in LANDS or self.cards[i]["name"] in BASIC_MANA))
  if len(sources)<needed:raise BlockedAction("Insufficient untapped modeled land sources")
  plans=[]
  for combo in itertools.combinations(sources,needed):
   opts=[colors(self.cards[i]["name"]) for i in combo]
   life=sum(self.cards[i]["name"]=="Mana Confluence" for i in combo)
   if life and self.pilot<=life:continue
   for chosen in itertools.product(*opts):
    if grixis_sim.can_pay(cost,[frozenset((c,)) for c in chosen],tax=tax) is None:
     continue
    score=(life,sum(len(x) for x in opts),combo,chosen)
    plans.append((score,combo,chosen))
  if not plans:raise BlockedAction("Available modeled lands cannot satisfy printed colors")
  _,srcs,choice=min(plans,key=lambda p:p[0])
  with self.atomic():
   for i,c in zip(srcs,choice):self.tap_land(i,c)
   self.cast(uid,origin=origin)
   self.priority_events.append({"event":"source_backed_land_payment","name":name,
     "source_ids":list(srcs),"colors":list(choice),
     "life_payment":sum(self.cards[i]["name"]=="Mana Confluence" for i in srcs)})
  return list(srcs)
