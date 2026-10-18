#!/usr/bin/env python3
"""Cycle106 narrow Commander-first physical casting *opportunities*, not win rates.

Three paired 100-card source lists with the same one physical slot replaced.
Effect resolution is allowed only for the two creature-slot abilities under
explicit scripted response profiles; Bituminous Blast always has an UNKNOWN
opponent-creature target and UNKNOWN printed cascade/removal value.
"""
from __future__ import annotations
import argparse,copy,hashlib,itertools,json,sys
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import evaluate_decklist as ev
import grixis_sim as sim
from grixis_m6_fetch_city_tomb import PriorityFetchCityTomb,MODEL_LANDS,FETCHES
from grixis_m6_priority_nonbasic import colors
from grixis_m6_state_kernel import BlockedAction
from grixis_m6_transactional_stack import TransactionalLedger

PLAN=ROOT/"data/grixis/m6/phase_b_plans/abaddon_physical_slot_01.json"
OUT=ROOT/"data/grixis/m6/phase_b_bounded/abaddon_physical_slot_01.json"
REG=ROOT/"data/grixis/registry.json"
SOURCE=ROOT/"exports/grixis-archidekt/source-baseline/abaddon-the-despoiler.txt"
PREV=ROOT/"data/grixis/m6/phase_b_bounded/abaddon_decision_readiness_01.json"
SLOTS={
 "Bituminous Blast":("{3}{B}{R}","instant",5),
 "Heartless Hidetsugu":("{3}{R}{R}","creature",5),
 "Tree of Perdition":("{3}{B}","creature",4)
}
AUTH={"can_change_decklists":False,"can_approve_or_lock":False,
      "can_decide":False,"can_certify_M6":False}
def read(p):return json.loads(p.read_text(encoding="utf-8"))
def digest(p):return "sha256:"+hashlib.sha256(p.read_bytes()).hexdigest()
def fmt(a):return json.dumps(a,indent=2,sort_keys=True,ensure_ascii=False)+"\n"

def oracle_check(res):
 checks={}
 for name in ["Abaddon the Despoiler"]+list(SLOTS):
  c=res.get(name)[0];txt=c.get("oracle_text") or "";ty=c.get("type_line","")
  if c.get("name")!=name:raise ValueError("Oracle card name mismatch "+name)
  if name=="Abaddon the Despoiler":
   if ("spells you cast from your hand" not in txt.casefold() or
       "have cascade" not in txt.casefold() or int(c["cmc"])!=5):
    raise ValueError("Commander Oracle changed")
  else:
   cost,kind,mv=SLOTS[name]
   if (sim.parse_cost(c["mana_cost"])!=sim.parse_cost(cost) or
       kind not in ty.lower() or int(c["cmc"])!=mv):
    raise ValueError("Slot mana or type changed "+name)
   if name=="Bituminous Blast" and (
       "cascade" not in txt.casefold() or "target creature" not in txt.casefold()
       or "4 damage" not in txt):
    raise ValueError("Printed cascade, creature target or damage changed")
   if name=="Heartless Hidetsugu" and (
       "{T}:" not in txt or "half that player's life total" not in txt.casefold()
       or "each player" not in txt.casefold()):
    raise ValueError("Heartless tap/damage ability changed")
   if name=="Tree of Perdition" and (
       "{T}:" not in txt or "exchange" not in txt.casefold()
       or "target opponent" not in txt.casefold()):
    raise ValueError("Tree target/exchange changed")
  checks[name]={"oracle_sha256":"sha256:"+hashlib.sha256(txt.encode()).hexdigest(),
                "mana_cost":c.get("mana_cost"),"type_line":ty}
 return checks

class SlotProbe(PriorityFetchCityTomb):
 def __init__(self,*args,slot,**kwargs):
  if slot not in SLOTS:raise ValueError("Wrong focus slot")
  super().__init__(*args,**kwargs)
  self.slot=slot
  self.slot_cast_turn=None
  self.slot_uid=None
  self.slot_activated=False
  self.slot_events=[]

 def _registered(self,uid):
  if uid in self.cards and self.cards[uid]["name"]==self.slot:
   cost,kind,mv=SLOTS[self.slot]
   c=self.cards[uid]
   if c["land"] or c["mv"]!=mv or c["cost"]!=sim.parse_cost(cost):
    raise BlockedAction("Oracle slot cost mismatch")
   return self.slot,{"kind":kind,"cost":cost},c["cost"]
  return super()._registered(uid)

 def cast(self,uid,origin="hand"):
  if uid not in self.cards or self.cards[uid]["name"]!=self.slot:
   return super().cast(uid,origin=origin)
  if self.slot=="Bituminous Blast":
   raise BlockedAction("Blast creature target and printed cascade are unmodeled")
  if origin!="hand" or self.zone_of(uid)!="hand" or self.frames or self.priority_seat!=0:
   raise BlockedAction("Creature slot requires held card and active clear priority")
  if not self.own_turn or not self.main_phase:raise BlockedAction("Not own main phase")
  if self.slot_uid is not None:raise BlockedAction("Creature slot already cast")
  if self.opponents_lost_this_turn>=self.cards[uid]["mv"] and any(
       self.cards[u]["name"]=="Abaddon the Despoiler" for u in self.zones["battlefield"]):
   raise BlockedAction("Abaddon granted cascade unresolved")
  _,_,cost=self._registered(uid)
  after=self._payment(cost)
  with self.atomic():
   self.mana=after
   self.transfer(uid,"hand","stack")
   self.frames.append({"kind":"spell","uid":uid,"name":self.slot,"origin":"hand"})
   self.slot_uid=uid;self.slot_cast_turn=self.turn
   self.slot_events.append({"event":"slot_cast_with_actual_mana","name":self.slot,
                           "uid":uid,"turn":self.turn})
  return self.slot

 def pass_priority(self):
  if not (self.frames and self.frames[-1].get("name")==self.slot and
          self.frames[-1]["kind"]=="spell"):
   return super().pass_priority()
  with self.atomic():
   seat=self.priority_seat
   self.pass_count+=1;self.priority_seat=(seat+1)%4
   self.priority_events.append({"event":"priority_pass","seat":seat,
                                 "consecutive":self.pass_count})
   if self.pass_count==4:
    frame=self.frames.pop()
    self.transfer(frame["uid"],"stack","battlefield")
    self.slot_events.append({"event":"creature_spell_resolved",
                             "name":self.slot,"uid":frame["uid"],"turn":self.turn})
    self.priority_events.append({"event":"four_passes_resolve_top",
      "frame_kind":"spell","name":self.slot})
    self.pass_count=0;self.priority_seat=0
   self.validate_stack()
  return self.priority_seat

 def activate_slot(self,profile):
  if self.slot not in ("Heartless Hidetsugu","Tree of Perdition"):
   raise BlockedAction("Baseline has no supported activated source")
  if profile not in ("no_interference","remove_source_before_first_activation",
                     "remove_source_after_ability_on_stack"):
   raise BlockedAction("Unsupported response profile")
  uid=self.slot_uid
  if uid is None or self.slot_activated or self.turn<=self.slot_cast_turn or (
     self.zone_of(uid)!="battlefield" or uid in self.tapped or self.frames):
   raise BlockedAction("Tap source not yet legally available under no-haste policy")
  with self.atomic():
   if profile=="remove_source_before_first_activation":
    self.transfer(uid,"battlefield","graveyard")
    rec={"profile":profile,"activated":False,"resolved":False,
         "opponents_lost":0,"pilot_damage":0,"source_removed":True}
   else:
    self.tapped.add(uid)
    # This is a SCRIPTED opposing response outcome, not a modeled opponent
    # spell, target, cost, or probability. Heartless ability persists using
    # source last-known characteristics; Tree exchange fails if absent.
    if profile=="remove_source_after_ability_on_stack":
     self.transfer(uid,"battlefield","graveyard")
    if self.slot=="Tree of Perdition" and self.zone_of(uid)!="battlefield":
     rec={"profile":profile,"activated":True,"resolved":False,
          "opponents_lost":0,"pilot_damage":0,"source_removed":True}
    elif self.slot=="Heartless Hidetsugu":
     original=list(self.opponents)
     damage=[x//2 for x in original]
     self.opponents=[x-d for x,d in zip(original,damage)]
     pilot_damage=self.pilot//2
     self.pilot-=pilot_damage
     lost=sum(damage)
     self.opponents_lost_this_turn+=lost
     rec={"profile":profile,"activated":True,"resolved":True,
          "opponents_lost":lost,"pilot_damage":pilot_damage,
          "source_removed":profile=="remove_source_after_ability_on_stack"}
    else:
     # 0/13 Tree: one opponent's life becomes 13; only a loss, not
     # damage. It is not modified by Solphim in this bounded fixture.
     before=self.opponents[0]
     self.opponents[0]=13
     lost=max(0,before-13)
     self.opponents_lost_this_turn+=lost
     rec={"profile":profile,"activated":True,"resolved":True,
          "opponents_lost":lost,"pilot_damage":0,
          "source_removed":False,"target_life_before":before,
          "target_life_after":13}
   rec.update({"source_uid":uid,"turn":self.turn,"pilot_life_after":self.pilot,
               "opponent_life_after":list(self.opponents),
               "abaddon_present":any(self.cards[u]["name"]=="Abaddon the Despoiler"
                                   for u in self.zones["battlefield"])})
   self.slot_events.append({"event":"bounded_tap_ability_branch",**rec})
   self.slot_activated=True
  return rec

def slot_in_hand(t):
 return next((u for u in t.zones["hand"] if t.cards[u]["name"]==t.slot),None)

def sources_can_pay(t,uid):
 # Explicit source-accurate, held-card-cost preflight. This is not proof that
 # Bituminous Blast has a legal target or grants a valuable cascade hit.
 if t.zone_of(uid)!="hand":return False
 _,_,cost=t._registered(uid)
 need=len(cost["pips"])+cost["generic"]
 source=[u for u in t.zones["battlefield"] if t.cards[u].get("land")
         and u not in t.tapped and t.cards[u]["name"] in MODEL_LANDS
         and t.cards[u]["name"] not in FETCHES]
 for n in range(1,min(need,len(source))+1):
  for comb in itertools.combinations(source,n):
   choices=[]
   life=0
   for v in comb:
    name=t.cards[v]["name"]
    choices.append(("C",) if name=="Ancient Tomb" else
                   ("U","B","R") if name=="City of Brass" else colors(name))
    if name=="Ancient Tomb":life+=2
    elif name in ("City of Brass","Mana Confluence"):life+=1
   if t.pilot<=life:continue
   for selected in itertools.product(*choices):
    units=[frozenset((c,)) for u,c in zip(comb,selected)
       for _ in range(2 if t.cards[u]["name"]=="Ancient Tomb" else 1)]
    if sim.can_pay(cost,units) is not None:return True
 return False

def slot_libraries(deck,resolver):
 # Exactly one physical main-library card changes and only at the frozen slot.
 base=list(deck.library)
 b=[i for i,c in enumerate(base) if c["name"]=="Bituminous Blast"]
 if len(b)!=1:raise ValueError("Baseline slot cardinality wrong")
 idx=b[0];variants={}
 for name in SLOTS:
  lib=list(base)
  if name!="Bituminous Blast":
   lib[idx]=sim.card_model(resolver.get(name)[0],deck.ci)
  if len(lib)!=99 or lib[idx]["name"]!=name:
   raise ValueError("Physical library is not a 99-card one-slot challenger")
  originals=Counter(c["name"] for c in lib)
  expect=Counter(c["name"] for c in base)
  expect["Bituminous Blast"]-=1
  if expect["Bituminous Blast"]==0:del expect["Bituminous Blast"]
  expect[name]+=1
  if originals!=expect:raise ValueError("Non-slot change in challenger library")
  variants[name]=lib
 return variants,idx

def run_trial(library,commanders,slot,seed,turns):
 t=SlotProbe(library,commanders,slot=slot,seed=seed,opponents=(40,39,31),pilot=40)
 initial=t.initial_inventory_hash
 opening=t.draw(7);initial_names=t.drawn_names(opening)
 drawn=[];summary={"slot_seen":False,"slot_held_and_mana_affordable":False,
   "slot_cast":False,"slot_cast_turn":None,"commander_cast_turn":None,
   "slot_activation_turn":None,"first_activation_profiles":None,
   "blast_target_and_printed_cascade_unknown":slot=="Bituminous Blast",
   "followup_held_with_actual_untapped_mana":False,
   "post_fetch_shuffles":0,"unregistered_lands_held":0}
 for turn in range(1,turns+1):
  if turn>1:t.next_turn()
  card=t.draw(1)[0]
  drawn.append(t.cards[card]["name"])
  summary["unregistered_lands_held"]+=sum(
   bool(t.cards[u].get("land")) and t.cards[u]["name"] not in MODEL_LANDS
   for u in t.zones["hand"])
  options=[u for u in t.zones["hand"] if t.cards[u].get("land") and
           t.cards[u]["name"] in MODEL_LANDS]
  if options:
   land=options[0];name=t.cards[land]["name"]
   t.play_supported_land(land)
   if name in FETCHES and t.pilot>1:
    t.activate_fetch(land);t.resolve_by_passes()
  found=slot_in_hand(t)
  if found is not None:summary["slot_seen"]=True
  if found is not None and not summary["slot_held_and_mana_affordable"]:
   summary["slot_held_and_mana_affordable"]=sources_can_pay(t,found)
  # Dedicated policy: Abaddon is attempted before a candidate creature each
  # turn if real land sources can pay; do not model extra mana rocks/rituals.
  if summary["commander_cast_turn"] is None:
   try:
    t.cast_with_land_sources(t.zones["command"][0],"command")
   except BlockedAction:pass
   else:
    t.resolve_by_passes()
    summary["commander_cast_turn"]=turn
  if summary["slot_cast_turn"] is None and found is not None and slot!="Bituminous Blast":
   try:t.cast_with_land_sources(found)
   except BlockedAction:pass
   else:
    t.resolve_by_passes()
    summary["slot_cast_turn"]=turn
    summary["slot_cast"]=True
  if (slot!="Bituminous Blast" and summary["slot_cast_turn"] is not None
      and turn>summary["slot_cast_turn"] and summary["slot_activation_turn"] is None):
   snapshots=[]
   for profile in ("no_interference","remove_source_before_first_activation",
                   "remove_source_after_ability_on_stack"):
    cp=copy.deepcopy(t)
    branch=cp.activate_slot(profile)
    followup=False
    if branch["resolved"] and branch["abaddon_present"]:
     for n in ("Boltwave","Flame Rift"):
      u=next((u for u in cp.zones["hand"] if cp.cards[u]["name"]==n),None)
      if u is not None and sources_can_pay(cp,u):
       followup=True
       break
    branch["followup_held_source_payable"]="YES_but_granted_cascade_unknown" if followup else "NO"
    if followup:summary["followup_held_with_actual_untapped_mana"]=True
    snapshots.append(branch)
   summary["first_activation_profiles"]=snapshots
   summary["slot_activation_turn"]=turn
  t.check();t.validate_stack()
 if t.initial_inventory_hash!=initial or t.initial_card_count!=100 or len(drawn)!=turns:
  raise AssertionError("Physical card/draw conservation failed")
 if summary["slot_cast"] and summary["slot_cast_turn"] is None:
  raise AssertionError("Contradictory cast status")
 summary["post_fetch_shuffles"]=t.fetch_resolutions
 return {"seed":seed,"opening":initial_names,"draws":drawn,
         "physical_inventory":initial,"observations":summary,
         "physical_conservation":True,"no_mulligans_or_opponent_gameplay":True,
         "no_injected_mana":True}

def verify():
 p=read(PLAN);reg=read(REG);prev=read(PREV)
 if (p["cycle"]!=106 or p["status"]!="preregistered_before_implementation"
     or p["authority"]!=AUTH or len(reg["decks"])!=62
     or reg["program"]["milestones"]["M6"]["status"]!="in_progress"
     or p["seed"]!=106017 or p["samples_per_variant"]!=240 or p["turns"]!=8
     or p["variants"]!=list(SLOTS)
     or digest(SOURCE)!="sha256:"+p["source_export_sha256"]
     or prev["source_approved_list_sha256"]!=p["approved_raw_sha256"]
     or prev["ready_for_any_card_swap"]
     or len(prev["deep_focus_comparisons"])!=6):
  raise ValueError("Frozen source authority, preregistration, or Cycle105 drift")
 resolver=ev.Resolver()
 checks=oracle_check(resolver)
 baseline=sim.load_deck("abaddon-the-despoiler",resolver)
 libs,slot_index=slot_libraries(baseline,resolver)
 all_results={};seqs=[]
 for slot,lib in libs.items():
  rows=[];stats=Counter();first_opens=[]
  for k in range(p["samples_per_variant"]):
   sd=sim.seed_for(p["seed"],k)
   rec=run_trial(lib,baseline.commanders,slot,sd,p["turns"])
   rows.append(rec)
   o=rec["observations"]
   for metric in ("slot_seen","slot_held_and_mana_affordable","slot_cast",
                  "followup_held_with_actual_untapped_mana"):
    stats[metric]+=int(o[metric])
   stats["commander_cast"]+=int(o["commander_cast_turn"] is not None)
   stats["activation_ready"]+=int(o["slot_activation_turn"] is not None)
   stats["real_fetch_shuffles"]+=o["post_fetch_shuffles"]
   stats["unsupported_land_held_occurrences"]+=o["unregistered_lands_held"]
   first_opens.append(rec["opening"])
  seqs.append(first_opens)
  all_results[slot]={"samples":len(rows),"observed":dict(sorted(stats.items())),
                      "trials":rows}
  print("Cycle106",slot,"cast",stats["slot_cast"],"activation",stats["activation_ready"],
        "commander",stats["commander_cast"],flush=True)
 slotnames=set(SLOTS)
 for idx in range(p["samples_per_variant"]):
  opener=[seq[idx] for seq in seqs]
  if any([n for n in arr if n not in slotnames]!=
         [n for n in opener[0] if n not in slotnames] for arr in opener[1:]):
   raise ValueError("Paired opening hand drift beyond one registered slot")
  if not all(len(a)==7 for a in opener):raise ValueError("Missing opening seven")
 # If scripted zero known values dominate, comparative deck verdict impossible.
 cannot_eval_reasons=[
  "Baseline Bituminous Blast cannot be legally cast without an opponent creature target; targets not modeled",
  "Baseline Bituminous Blast printed cascade and possible Abaddon-granted cascade have unknown value and targets",
  "Candidate activation trials use no real opponent creature removal probabilities; response outcomes are scripted",
  "Mana model omits rocks, rituals, conditional utility lands, mana reductions, alternative spell costs and other spell sequencing",
  "Unmodeled hand-cast Abaddon-triggered cascade prevents a complete advantage or win calculation",
  "Only eight simplified pilot turns; no mulligan, full opponent game states, cards played outside commander and tested slot, or completed win conditions"
 ]
 return {"schema_version":1,"cycle":106,"stage":"M6_Abaddon_physical_held_cast_and_activation_opportunity",
   "plan_sha256":digest(PLAN),"prior_cycle105_sha256":digest(PREV),
   "approved_raw_sha256":p["approved_raw_sha256"],"baseline_source_sha256":digest(SOURCE),
   "oracle_checks":checks,"paired_physical_slot_index":slot_index,
   "samples_per_variant":p["samples_per_variant"],
   "total_samples":p["samples_per_variant"]*len(SLOTS),
   "exact_paired_initial_7_verified":True,
   "no_forced_card_or_mana_access":True,
   "variants":all_results,
   "comparison_verdict":"CANNOT_EVALUATE_RELATIVE_DECK_STRENGTH",
   "reasons":cannot_eval_reasons,
   "effect_value_of_unmodeled_actions":None,
   "real_opponent_response_frequency":None,
   "actual_game_win_rate":None,
   "supports_any_swap":False,"zero_improvement_certified":False,
   "phase_b_complete":False,"independent_pass_c_complete":False,
   "M6_accepted":False,"authority":AUTH}

def compact(j):
 return {"cycle":106,"approved_raw_sha256":j["approved_raw_sha256"],
  "samples_per_variant":j["samples_per_variant"],"total_samples":j["total_samples"],
  "exact_paired_initial_7_verified":True,
  "result_by_variant":{name:x["observed"] for name,x in j["variants"].items()},
  "oracle_checks":j["oracle_checks"],
  "comparison_verdict":j["comparison_verdict"],"reasons":j["reasons"],
  "actual_game_win_rate":None,"new_card_approved":False,"M6_accepted":False}
def main():
 a=argparse.ArgumentParser();a.add_argument("--build",action="store_true");a.add_argument("--check",action="store_true")
 args=a.parse_args()
 if not(args.build or args.check):a.error("require --build or --check")
 x=verify();txt=fmt(x);short=fmt(compact(x))
 small=OUT.with_name("abaddon_physical_slot_summary_01.json")
 if args.build:
  OUT.parent.mkdir(parents=True,exist_ok=True)
  OUT.write_text(txt,encoding="utf-8");small.write_text(short,encoding="utf-8")
 if args.check and (not OUT.exists() or OUT.read_text(encoding="utf-8")!=txt
                    or not small.exists() or small.read_text(encoding="utf-8")!=short):
  raise ValueError("Cycle106 paired source physical cast replay diverged")
 print("Cycle106: paired physical access only; UNKNOWN blast target/cascade value; CANNOT EVALUATE a swap.")
if __name__=="__main__":main()
