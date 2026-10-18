#!/usr/bin/env python3
"""Cycle 107: legal physical Bituminous Blast target and cascade offer receipts.

This tests a FIXED external 3/3 opposing creature, not a full opposing deck.
Cascade spells are offered and explicitly DECLINED; their possible effects are
UNKNOWN, never treated as zero-value. No true opponent game or deck advantage.
"""
from __future__ import annotations
import argparse,copy,hashlib,json,random,sys
from collections import Counter
from contextlib import contextmanager
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import evaluate_decklist as ev
import grixis_sim as sim
from grixis_m6_abaddon_physical_slot import SlotProbe,sources_can_pay,slot_in_hand
from grixis_m6_state_kernel import BlockedAction
from grixis_m6_transactional_stack import TransactionalLedger
from grixis_m6_fetch_city_tomb import MODEL_LANDS,FETCHES

PLAN=ROOT/"data/grixis/m6/phase_b_plans/abaddon_blast_target_cascade_01.json"
PREV=ROOT/"data/grixis/m6/phase_b_bounded/abaddon_physical_slot_01.json"
SOURCE=ROOT/"exports/grixis-archidekt/source-baseline/abaddon-the-despoiler.txt"
REG=ROOT/"data/grixis/registry.json"
OUT=ROOT/"data/grixis/m6/phase_b_bounded/abaddon_blast_target_cascade_01.json"
AUTH={"can_change_decklists":False,"can_approve_or_lock":False,
      "can_decide":False,"can_certify_M6":False}
def read(p):return json.loads(p.read_text(encoding="utf-8"))
def sha(p):return "sha256:"+hashlib.sha256(p.read_bytes()).hexdigest()
def encode(v):return json.dumps(v,sort_keys=True,indent=2,ensure_ascii=False)+"\n"

class BlastCascade(SlotProbe):
 def __init__(self,*args,**kwargs):
  super().__init__(*args,slot="Bituminous Blast",**kwargs)
  self.target_alive=True            # externally scripted opponent 3/3
  self.target_damage=0
  self.cascade_triggers=0
  self.cascade_resolved=0
  self.cascade_offers=[]
  self.blast_cast=False
  self.blast_resolution=None
  self.outside_response_events=[]

 @contextmanager
 def atomic(self):
  keys=("target_alive","target_damage","cascade_triggers","cascade_resolved",
        "cascade_offers","blast_cast","blast_resolution","outside_response_events")
  save={x:copy.deepcopy(getattr(self,x)) for x in keys}
  try:
   with super().atomic():yield
  except Exception:
   for x,y in save.items():setattr(self,x,y)
   raise

 def cast(self,uid,origin="hand"):
  if uid not in self.cards or self.cards[uid]["name"]!="Bituminous Blast":
   return super().cast(uid,origin=origin)
  if origin!="hand" or self.zone_of(uid)!="hand":
   raise BlockedAction("Bituminous Blast must be held in actual hand")
  if self.blast_cast or not self.target_alive:
   raise BlockedAction("No unmodeled legal creature target or Blast already cast")
  if not self.own_turn or self.priority_seat!=0 or self.pass_count or self.frames:
   raise BlockedAction("Outside bounded first-main-controller casting window")
  name,spec,cost=self._registered(uid)
  after=self._payment(cost)
  threshold=self.opponents_lost_this_turn
  commander_on_board=any(self.cards[x]["name"]=="Abaddon the Despoiler"
                       for x in self.zones["battlefield"])
  granted=int(commander_on_board and threshold>=self.cards[uid]["mv"])
  with self.atomic():
   self.mana=after
   self.transfer(uid,"hand","stack")
   self.frames.append({"kind":"spell","name":"Bituminous Blast",
                       "uid":uid,"origin":"hand"})
   # Fixed AP controller ordering: one printed trigger then (if eligible)
   # one Abaddon-granted cascade trigger, above the physical instant spell.
   for why in (["printed"]+["Abaddon_granted"]*granted):
    self.frames.append({"kind":"trigger","name":"Bituminous Blast cascade",
                        "source_uid":uid,"why":why,"mv":5})
   self.cascade_triggers=1+granted
   self.blast_cast=True
   self.slot_cast_turn=self.turn
   self.slot_events.append({"event":"Bituminous Blast cast","turn":self.turn,
      "cascade_triggers":self.cascade_triggers,
      "threshold_at_CAST":threshold,"printed_cascade":1,
      "granted_from_hand":granted,"real_mana_paid":True,
      "target":"external 3/3 opposing creature fixture"})
  return name

 def externally_remove_target(self):
  if not self.blast_cast or not self.target_alive or self.blast_resolution is not None:
   raise BlockedAction("No pending opponent target to remove")
  if self.priority_seat not in (1,2,3):
   raise BlockedAction("Scripted target removal requires opponent priority")
  with self.atomic():
   self.target_alive=False
   self.outside_response_events.append({"event":"scripted_opposing_target_removed",
     "seat":self.priority_seat,"no_actual_counterspell_or_mana_model":True})
   self.priority_seat=0;self.pass_count=0

 def _cascade_offer(self,frame):
  revealed=[]
  eligible=None
  while self.zones["library"]:
   uid=self.zones["library"][0]
   c=self.cards[uid]
   self.transfer(uid,"library","exile")
   revealed.append(uid)
   if not c.get("land",False) and int(c["mv"])<int(frame["mv"]):
    eligible=uid
    break
  if eligible is not None:
   # Cascade permits NOT casting the discovered card. We choose to decline
   # specifically because its full cost/target/strategic effect is unknown.
   self.cascade_offers.append({"trigger":frame["why"],
      "revealed_physical_ids":list(revealed),
      "eligible_uid":eligible,"eligible_name":self.cards[eligible]["name"],
      "eligible_mv":int(self.cards[eligible]["mv"]),
      "controller_choice":"decline_optional_cast",
      "possible_effect_value":"UNKNOWN_NOT_ZERO",
      "legality_if_chosen":"NOT_VERIFIED",
      "number_of_revealed":len(revealed)})
  else:
   self.cascade_offers.append({"trigger":frame["why"],
     "revealed_physical_ids":list(revealed),"eligible_uid":None,
     "eligible_name":None,"eligible_mv":None,
     "controller_choice":"no_eligible_hit_found",
     "possible_effect_value":"NONE_OFFERED","legality_if_chosen":"NOT_APPLICABLE",
     "number_of_revealed":len(revealed)})
  self.cascade_resolved+=1
  rng=random.Random(self.seed ^ (self.cascade_resolved*0x9e3779b1))
  rng.shuffle(revealed)
  for uid in revealed:self.transfer(uid,"exile","library")
  return self.cascade_offers[-1]

 def pass_priority(self):
  if not self.frames or not (
     self.frames[-1].get("name") in ("Bituminous Blast cascade","Bituminous Blast")):
   return super().pass_priority()
  with self.atomic():
   seat=self.priority_seat
   self.pass_count+=1;self.priority_seat=(seat+1)%4
   self.priority_events.append({"event":"priority_pass",
     "seat":seat,"consecutive":self.pass_count})
   if self.pass_count==4:
    frame=self.frames.pop()
    if frame["kind"]=="trigger":
     self._cascade_offer(frame)
    else:
     if frame["kind"]!="spell" or self.zone_of(frame["uid"])!="stack":
      raise AssertionError("Blast physical ID not on stack")
     if self.target_alive:
      self.target_damage=4
      self.target_alive=False
      self.blast_resolution="REMOVED_EXTERNAL_3_3_BY_FOUR_DAMAGE"
     else:
      self.blast_resolution="FAILED_TO_RESOLVE_TARGET_ILLEGAL"
     self.transfer(frame["uid"],"stack","graveyard")
    self.priority_events.append({"event":"four_passes_resolve_top",
      "name":frame["name"],"kind":frame["kind"]})
    self.pass_count=0;self.priority_seat=0
   self.validate_stack()
  return self.priority_seat

def simulate(library,commanders,seed,turns,removal=False):
 t=BlastCascade(library,commanders,seed=seed,opponents=(40,39,31),pilot=40)
 opening=t.drawn_names(t.draw(7));draws=[];held_affordable=False
 for turn in range(1,turns+1):
  if turn>1:t.next_turn()
  uid=t.draw(1)[0];draws.append(t.cards[uid]["name"])
  land=next((u for u in t.zones["hand"] if
      t.cards[u].get("land") and t.cards[u]["name"] in MODEL_LANDS),None)
  if land is not None:
   n=t.cards[land]["name"];t.play_supported_land(land)
   if n in FETCHES and t.pilot>1:
    t.activate_fetch(land);t.resolve_by_passes()
  blast=slot_in_hand(t)
  if blast is not None and sources_can_pay(t,blast):
   held_affordable=True
  if t.command_casts.get("c000",0)==0:
   try:t.cast_with_land_sources("c000","command")
   except BlockedAction:pass
   else:t.resolve_by_passes()
  if not t.blast_cast and blast is not None:
   try:t.cast_with_land_sources(blast)
   except BlockedAction:pass
   else:
    if removal:
     t.pass_priority()
     t.externally_remove_target()
    t.resolve_by_passes()
  t.check();t.validate_stack()
 if not (t.initial_card_count==100 and sum(t.receipt()["zone_counts"].values())==100):
  raise AssertionError("100 physical ID conservation failed")
 return {"seed":seed,"opening":opening,"draws":draws,
  "held_and_source_payable":held_affordable,"blast_cast":t.blast_cast,
  "resolution":t.blast_resolution,"trigger_count":t.cascade_triggers,
  "resolved_trigger_count":t.cascade_resolved,
  "offers":t.cascade_offers,
  "fetch_shuffles":t.fetch_resolutions,
  "opposing_target_removed_by_script":removal and t.blast_cast,
  "zone_counts":t.receipt()["zone_counts"],"initial_inventory":t.initial_inventory_hash}

def run():
 plan=read(PLAN);old=read(PREV);r=read(REG)
 if (plan["cycle"]!=107 or plan["status"]!="preregistered_before_implementation"
    or plan["seed"]!=106017 or plan["trials"]!=240 or plan["turns"]!=8
    or plan["authority"]!=AUTH or len(r["decks"])!=62
    or r["program"]["milestones"]["M6"]["status"]!="in_progress"
    or sha(SOURCE)!="sha256:"+plan["source_sha256"]
    or old["approved_raw_sha256"]!=plan["approved_sha256"]
    or old["comparison_verdict"]!="CANNOT_EVALUATE_RELATIVE_DECK_STRENGTH"):
  raise ValueError("Cycle107 prereg or approved source drift")
 resolver=ev.Resolver()
 blast=resolver.get("Bituminous Blast")[0]
 txt=blast.get("oracle_text","").casefold()
 if not ("cascade" in txt and "4 damage to target creature" in txt
         and int(blast["cmc"])==5 and blast["mana_cost"]=="{3}{B}{R}"):
  raise ValueError("Frozen Oracle Bituminous target/printed cascade drift")
 d=sim.load_deck("abaddon-the-despoiler",resolver)
 if len(d.library)!=99 or len(d.commanders)!=1:
  raise ValueError("Not canonical 99+1 physical deck")
 prev=old["variants"]["Bituminous Blast"]["trials"]
 results={}
 for policy in ("no_removal","target_removed_after_cast"):
  receipts=[];s=Counter()
  for idx,prior in enumerate(prev):
   seed=sim.seed_for(plan["seed"],idx)
   x=simulate(d.library,d.commanders,seed,plan["turns"],
              removal=policy=="target_removed_after_cast")
   if x["seed"]!=prior["seed"] or x["opening"]!=prior["opening"]:
    raise AssertionError("Cycle106 paired opening or initial seed drift")
   s["observations"]+=1
   s["held_and_source_payable"]+=int(x["held_and_source_payable"])
   s["blast_cast"]+=int(x["blast_cast"])
   s["printed_cascades"]+=x["trigger_count"]
   s["cascade_resolved"]+=x["resolved_trigger_count"]
   s["eligible_offers"]+=sum(y["eligible_uid"] is not None for y in x["offers"])
   s["unknown_effect_offers"]+=sum(y["possible_effect_value"]=="UNKNOWN_NOT_ZERO" for y in x["offers"])
   s["creatures_removed_in_fixture"]+=int(x["resolution"]=="REMOVED_EXTERNAL_3_3_BY_FOUR_DAMAGE")
   s["spell_failed_illegal_target"]+=int(x["resolution"]=="FAILED_TO_RESOLVE_TARGET_ILLEGAL")
   receipts.append(x)
  results[policy]={"counts":dict(sorted(s.items())),"trials":receipts}
  print("Cycle107",policy,dict(s),flush=True)
 return {"schema_version":1,"cycle":107,"plan_sha256":sha(PLAN),
    "prior_cycle106_sha256":sha(PREV),"approved_sha256":plan["approved_sha256"],
    "frozen_bituminous_oracle_sha256":"sha256:"+hashlib.sha256(blast["oracle_text"].encode()).hexdigest(),
    "sample_count":plan["trials"],"policies":results,
    "scripted_board_target":"opponent_3_3_creature_without_abilities",
    "all_cascade_hits_declined_when_offered":True,
    "potential_value_of_offered_hits":"UNKNOWN_NOT_ZERO",
    "relative_deck_strength":"CANNOT_EVALUATE",
    "full_phase_b_complete":False,"independent_pass_c_complete":False,
    "supports_improvement_claim":False,"zero_improvement_certified":False,
    "M6_accepted":False,"authority":AUTH}

def compact(x):
 return {"cycle":107,"sample_count":x["sample_count"],
  "counts":{k:v["counts"] for k,v in x["policies"].items()},
  "relative_deck_strength":x["relative_deck_strength"],
  "candidate_approved":False,"M6_accepted":False,
  "potential_value_of_offered_hits":x["potential_value_of_offered_hits"]}
def main():
 a=argparse.ArgumentParser()
 a.add_argument("--build",action="store_true");a.add_argument("--check",action="store_true")
 z=a.parse_args()
 if not(z.build or z.check):a.error("require --build/--check")
 obj=run();big=encode(obj);small=encode(compact(obj))
 short=OUT.with_name("abaddon_blast_target_cascade_summary_01.json")
 if z.build:
  OUT.parent.mkdir(parents=True,exist_ok=True)
  OUT.write_text(big,encoding="utf-8");short.write_text(small,encoding="utf-8")
 if z.check and (not OUT.is_file() or OUT.read_text(encoding="utf-8")!=big
     or not short.is_file() or short.read_text(encoding="utf-8")!=small):
  raise ValueError("Cycle107 source-backed replay diverged")
 print("Cycle107 Blast physical legal target, printed cascade offers; UNKNOWN comparative value.")
if __name__=="__main__":main()
