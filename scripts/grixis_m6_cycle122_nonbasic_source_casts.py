#!/usr/bin/env python3
"""Cycle122 Oracle-checked 19 named nonbasic mana and conditional entries over paired physical decks.

Uses the EXISTING bounded PriorityNonbasic land rules, not a new land rules
engine. Counts source-paid, uncontested main-phase permanent placements under
supported lands only. Unsupported lands, fetches, abilities, actual opponent
spells, Mox Diamond mana, win rates and real Phase B remain unmodeled.
"""
from __future__ import annotations
import argparse,hashlib,itertools,json,random,sys
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import evaluate_decklist as ev
import grixis_authority as ga
import grixis_sim as sim
import grixis_paired as paired
import grixis_m6_cycle120_physical_access as c120
import grixis_m6_cycle121_basic_paid_casts as c121
import grixis_m6_nonbasic_land_access_62 as c103
from grixis_m6_priority_nonbasic import PriorityNonbasic,LANDS,colors
from grixis_m6_state_kernel import BASIC_MANA,BlockedAction

PLAN=ROOT/"data/grixis/m6/phase_b_plans/cycle122_nonbasic_source_casts_prereg_01.json"
REG=ROOT/"data/grixis/registry.json"
PRIOR=ROOT/"data/grixis/m6/phase_b_plans/cycle121_source_paid_cast_prereg_01.json"
LAND_PLAN=ROOT/"data/grixis/m6/phase_b_plans/nonbasic_land_access_62_01.json"
OUT=ROOT/"data/grixis/m6/phase_b_bounded/cycle122_nonbasic_source_casts_01.json"
AUTH={"can_modify_canonical_decks":False,"can_approve_swaps":False,
      "can_certify_M6":False,"can_certify_Pass_C":False,"can_promote_phase_B":False}
def read(p):return json.loads(Path(p).read_text(encoding="utf-8"))
def sha(p):return "sha256:"+hashlib.sha256(Path(p).read_bytes()).hexdigest()
def fmt(d):return json.dumps(d,sort_keys=True,ensure_ascii=False,indent=2)+"\n"
def is_supported_land(t,u):
 return (t.cards[u].get("land") and
         t.cards[u]["name"] in set(LANDS)|set(BASIC_MANA))
def choose_land(t,target):
 choices=[]
 wanted=set(c121.COST.get(target,(0,{}))[1])
 others=[u for u in t.zones["battlefield"] if t.cards[u].get("land")]
 for uid in t.zones["hand"]:
  if not is_supported_land(t,uid):continue
  name=t.cards[uid]["name"]
  shock=name in LANDS and LANDS[name][1]=="shock"
  choice=(t.pilot>2) if shock else None
  tapped=t._enter_tapped(uid,others,choice)
  # A single agreed deterministic play priority, NOT perfect future sequencing.
  score=(0 if any(c in wanted for c in colors(name)) else 1,
         int(tapped),name,uid)
  choices.append((score,uid,choice))
 if not choices:return None
 _,uid,payshock=min(choices,key=lambda item:item[0])
 t.play_supported_land(uid,pay_shock=payshock)
 return {"name":t.cards[uid]["name"],"uid":uid,
         "entered_tapped":uid in t.tapped,"shock_paid":bool(payshock)}
def source_payment(t,target):
 """Pure preflight; no land or mana mutation until full exact payment is found."""
 cost=c121.COST.get(target)
 if cost is None:raise BlockedAction("Unregistered selected spell")
 generic,pips=cost
 needed=generic+sum(pips.values())
 eligible=sorted(uid for uid in t.zones["battlefield"]
    if is_supported_land(t,uid) and uid not in t.tapped)
 if len(eligible)<needed:return None
 plans=[]
 for combo in itertools.combinations(eligible,needed):
  for opts in itertools.product(*(colors(t.cards[u]["name"]) for u in combo)):
   payable=sim.can_pay(sim.parse_cost(
      "{"+str(generic)+"}" if generic else "") if False else
      {"generic":generic,"pips":[frozenset([c]) for c,n in pips.items() for _ in range(n)],"life":0},
      [frozenset([color]) for color in opts])
   if payable is None:continue
   life=sum(t.cards[u]["name"]=="Mana Confluence" for u in combo)
   if t.pilot<=life:continue
   plans.append(((life,combo,opts),combo,opts))
 if not plans:return None
 _,uids,choices=min(plans,key=lambda rec:rec[0])
 return list(zip(uids,choices))
def simulate_one(library,commander,target,permutation):
 t=PriorityNonbasic(library,commander,seed=120026,opponent_count=3)
 t.zones["library"]=[f"m{i:03d}" for i in permutation]
 t.check()
 t.draw(7)
 seen=False;first_paid=None;first_payable=None;first_source=None
 unsupported_seen=set();land_events=[];entries=Counter();used_colors=Counter()
 mox_discard=False;recorded=[]
 for turn in range(1,9):
  if turn>1:t.next_turn()
  t.draw(1)
  uid=next((u for u in t.zones["hand"] if t.cards[u]["name"]==target),None)
  if uid is not None:seen=True
  unsupported_seen|={t.cards[u]["name"] for u in t.zones["hand"] if t.cards[u].get("land")
                 and not is_supported_land(t,u)}
  if target=="Mox Diamond" and uid is not None and first_paid is None:
   others=sorted((u for u in t.zones["hand"] if u!=uid and t.cards[u].get("land")),
          key=lambda u:(t.cards[u]["name"],u))
   if others:
    with t.atomic():
     t.transfer(others[0],"hand","graveyard")
     t.transfer(uid,"hand","battlefield")
     t.priority_events.append({"event":"mox_physical_land_discard_entry_no_mox_mana",
         "turn":t.turn,"source_land_uid":others[0]})
    mox_discard=True;first_paid=turn
  played=choose_land(t,target)
  if played is not None:
   land_events.append({"turn":turn,**played})
   entries["tapped" if played["entered_tapped"] else "untapped"]+=1
  # The model can show instant-cost affordance, but cannot invent an opponent's stack.
  if target=="An Offer You Can't Refuse":
   uid=next((u for u in t.zones["hand"] if t.cards[u]["name"]==target),None)
   if uid is not None and first_payable is None and source_payment(t,target):
    first_payable=turn
  elif target!="Mox Diamond" and first_paid is None:
   uid=next((u for u in t.zones["hand"] if t.cards[u]["name"]==target),None)
   payment=source_payment(t,target) if uid is not None else None
   if payment:
    with t.atomic():
     for land,color in payment:
      t.tap_land(land,color)
      used_colors[color]+=1
     # Uncontested, bounded source-paid PERMANENT placement: actual stack
     # and opponent responses are not modeled; it is not a certified game.
     t.transfer(uid,"hand","battlefield")
     if target.startswith("The Enigma Jewel"):
      t.tapped.add(uid)    # Oracle: Jewel enters tapped.
     t.priority_events.append({"event":"bounded_uncontested_source_paid_permanent",
       "turn":turn,"name":target,"uids":[a for a,b in payment],
       "colors":[b for a,b in payment],"actual_opponent_priority_simulated":False})
    first_paid=turn
    first_source=[{"uid":u,"name":t.cards[u]["name"],"color":c} for u,c in payment]
  # Mana floating in this analysis empties at own-turn boundary; no effects from it.
  t.check()
 if not (first_paid is None or seen):raise AssertionError("Cast without card seen")
 return {"seen":int(seen),"paid":int(first_paid is not None),
         "first_paid_turn":first_paid,"payable_in_absence_of_opponent_spell":int(first_payable is not None),
         "mox_physical_land_discard":int(mox_discard),
         "entry_counts":dict(entries),"selected_colors":dict(used_colors),
         "unsupported_lands_seen":sorted(unsupported_seen),"land_play_events":land_events,
         "witness_source_payment":first_source,"physical_card_count":t.receipt()["count"],
         "last_pilot_life":t.pilot}

def verify(p,reg,prior,R):
 if (p["schema_version"]!=1 or p["cycle"]!=122 or p["status"]!="preregistered_before_engineering_or_results"
  or p["authority"]!=AUTH or p["model"]["seed"]!=120026 or
   p["model"]["samples_per_deck"]!=1024 or p["model"]["turns"]!=8 or
   len(p["studies"])!=3 or reg["program"]["milestones"]["M6"]["status"]!="in_progress"
   or reg["program"]["milestones"]["M7"]["status"]!="not_started"
   or len(reg["decks"])!=62 or prior["cycle"]!=121):
  raise ValueError("Cycle122 prereg or milestone drift")
 expected={x["deck_id"]:x for x in prior["studies"]}
 if set(expected)!={x["deck_id"] for x in p["studies"]}:raise ValueError("Named source roster drift")
 for x in p["studies"]:
  orig=expected[x["deck_id"]]
  if x!=orig:raise ValueError("Approved source/swap mutation in Cycle122 plan")
  authoritative=reg["decks"][x["deck_id"]]
  if (authoritative["current_canonical_hash"]!=x["approved_logical_hash"] or
      authoritative["source"]["recorded_sha256"]!=x["approved_raw_sha256"]):
   raise ValueError("Approved list hash mismatch")
  if ga.text_hash(ga.deck_block_text(x["slug"]),R)!=x["approved_logical_hash"]:
   raise ValueError("Actual engineering approved source changed")
 if (c121.COST["The Enigma Jewel // Locus of Enlightenment"]!=(0,{"U":1}) or
     set(LANDS)!=set(c103.read(LAND_PLAN)["supported_nonbasic_mana_colors"])):
  raise ValueError("Jewel blue cost or named land set not authoritative")
 land_oracle=c103.oracle_checks(R,c103.read(LAND_PLAN))
 if len(land_oracle)!=19:raise ValueError("Expected nineteen Oracle-verified named lands")
 return land_oracle

def run():
 p,reg,prior=map(read,(PLAN,REG,PRIOR))
 R=ev.Resolver()
 oracle=verify(p,reg,prior,R)
 result=[]
 for x in p["studies"]:
  txt=ga.deck_block_text(x["slug"])
  alt=c120.c118.replace_exact_slot(txt,x["cut"],x["add"])
  deck=sim.load_deck(x["slug"],R,text=txt)
  challenger=sim.load_deck(x["slug"],R,text=alt)
  a,b,pairs=paired.align(deck,challenger,[(x["cut"],x["add"])])
  if pairs!=[(x["cut"],x["add"])] or a.N!=99 or b.N!=99:raise AssertionError("Source physical pair not 99/one slot")
  d={}
  for arm,name,source in [("baseline",x["cut"],a),("candidate",x["add"],b)]:
   d[arm]={"name":name,"seen":0,"supported_paid_or_entry":0,
           "payable_without_opponent_event":0,"first_turn_counts":Counter(),
           "mox_real_land_discard":0,"sampled_unsupported_land_names":Counter(),
           "land_entry_types":Counter(),"land_colors_paid":Counter(),"witnesses":[]}
  for i in range(p["model"]["samples_per_deck"]):
   permutation=random.Random(sim.seed_for(120026,i)^0x5EED).sample(range(99),99)
   for arm,name,source in [("baseline",x["cut"],a),("candidate",x["add"],b)]:
    z=simulate_one(source.library,source.commanders,name,permutation)
    item=d[arm]
    item["seen"]+=z["seen"]
    item["supported_paid_or_entry"]+=z["paid"]
    item["payable_without_opponent_event"]+=z["payable_in_absence_of_opponent_spell"]
    item["mox_real_land_discard"]+=z["mox_physical_land_discard"]
    if z["first_paid_turn"] is not None:
     item["first_turn_counts"][str(z["first_paid_turn"])]+=1
     if len(item["witnesses"])<2:
      item["witnesses"].append({"sample_index":i,"turn":z["first_paid_turn"],
                               "source_payment":z["witness_source_payment"],
                               "selected_land_entries":z["land_play_events"],
                               "opponents_modeled":False})
    for land in z["unsupported_lands_seen"]:
     item["sampled_unsupported_land_names"][land]+=1
    for group,n in z["entry_counts"].items():item["land_entry_types"][group]+=n
    for color,n in z["selected_colors"].items():item["land_colors_paid"][color]+=n
    if z["physical_card_count"]!=100:raise AssertionError("Lost commander/physical cards")
  records=[]
  for arm in ("baseline","candidate"):
   r=d[arm]
   for key in ("first_turn_counts","sampled_unsupported_land_names","land_entry_types","land_colors_paid"):
    r[key]=dict(sorted(r[key].items()))
   records.append({"arm":arm,**r})
  if records[0]["seen"]!=records[1]["seen"]:
   raise AssertionError("Paired changed-slot seen mismatch")
  result.append({"deck_id":x["deck_id"],"commander":x["commander"],
                 "approved_raw_sha256_recorded":x["approved_raw_sha256"],
                 "approved_source_logical_hash":x["approved_logical_hash"],
                 "registered_swap":[x["cut"],x["add"]],
                 "source_main_cards":99,"commander_count":1,"samples":1024,"arm_results":records})
 return {"schema_version":1,"cycle":122,
     "stage":"M6_PHYSICAL_NAMED_NONBASIC_SOURCE_PAYMENTS_NOT_PHASE_B",
     "plan_sha256":sha(PLAN),"registry_sha256":sha(REG),
     "prior_cycle121_plan_sha256":sha(PRIOR),"frozen_named_land_count":len(oracle),
     "oracle_named_land_text_hashes":oracle,
     "modeled_untapped_tapped_shock_typed_fast_bond":True,
     "paired_samples":3072,"arm_views":6144,"results":result,
     "current_canonical_decks_modified":0,"applied_swaps":0,
     "independent_pass_c":0,"complete_phase_b_certifications":0,
     "M6_accepted":False,"M7_started":False,
     "limits":["All fetch lands, City of Brass, Ancient Tomb, pathways, channel and utility lands unsupported in this adapter despite other engineering kernels covering some.",
       "Only registered printed simple-cost spell access and bounded uncontested permanent placement. No opponents, priority responses, actual stack adjudication or tactical AI.",
       "An Offer requires a real opponent noncreature stack event; report affordability only, never countered spell/win.",
       "Mox Diamond can discard a real land but its mana production is excluded; reported mana performance is incomplete.",
       "Nonbasic mana source omission makes these lower coverage examples, not actual deck optimality or win probabilities."]}
def main():
 ap=argparse.ArgumentParser();ap.add_argument("--build",action="store_true");ap.add_argument("--check",action="store_true")
 args=ap.parse_args()
 if not(args.build or args.check):ap.error("Use --build or --check")
 txt=fmt(run())
 if args.build:OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(txt,encoding="utf-8")
 if args.check and (not OUT.exists() or OUT.read_text(encoding="utf-8")!=txt):
  raise ValueError("Cycle122 exact reproducible receipt failed")
 print("Cycle122: 3072 physical nonbasic-supported source samples, nineteen gated named lands; no Phase B or Pass C.")
if __name__=="__main__":main()
