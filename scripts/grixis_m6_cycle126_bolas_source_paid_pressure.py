#!/usr/bin/env python3
"""Cycle126: physical-source Bolas/Mox Diamond versus Amplifier *opportunities*.

No real opponents, stack, combat, triggered discards, tutors, counterspells,
loyalty abilities or wins. "Cast", "transform" and "double" below mean bounded,
uncontested physically paid outcomes after the listed costs and tap checks.
"""
from __future__ import annotations
import argparse,copy,hashlib,itertools,json,random,sys
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
import grixis_m6_cycle122_nonbasic_source_casts as c122
import grixis_m6_nonbasic_land_access_62 as c103
from grixis_m6_priority_nonbasic import PriorityNonbasic,LANDS,colors
from grixis_m6_state_kernel import BASIC_MANA,BlockedAction

PLAN=ROOT/"data/grixis/m6/phase_b_plans/cycle126_bolas_source_paid_pressure_preregistered_01.json"
SOURCE=ROOT/"data/grixis/registry.json"
PARENT=ROOT/"data/grixis/m6/phase_b_plans/cycle121_source_paid_cast_prereg_01.json"
OUT=ROOT/"data/grixis/m6/phase_b_bounded/cycle126_bolas_source_paid_pressure_01.json"
AMP="Aetheric Amplifier"
MOX="Mox Diamond"
BOLAS="Nicol Bolas, the Ravager // Nicol Bolas, the Arisen"
COSTS={"commander":(1,("U","B","R")),
       "transform":(4,("U","B","R")),
       "amplifier_cast":(3,()),
       "amplifier_double":(4,())}
POLICIES=("baseline_mox_commander_first","candidate_amplifier_early","candidate_amplifier_commander_first")
AUTH={"apply_swap":False,"change_canonical_list":False,"accept_m6":False,"certify_pass_c":False,"certify_phase_b":False}

def read(p):return json.loads(Path(p).read_text(encoding="utf-8"))
def sha(p):return "sha256:"+hashlib.sha256(Path(p).read_bytes()).hexdigest()
def enc(x):return json.dumps(x,sort_keys=True,ensure_ascii=False,indent=2)+"\n"

def frozen_card_gates(R):
  card_m=R.get(MOX)[0]
  card_a=R.get(AMP)[0]
  card_b=R.get(BOLAS)[0]
  text_m=card_m.get("oracle_text") or ""
  text_a=card_a.get("oracle_text") or ""
  faces=card_b.get("card_faces") or []
  if (len(faces)!=2 or [x["name"] for x in faces]!=["Nicol Bolas, the Ravager","Nicol Bolas, the Arisen"]
       or "discard a land card" not in text_m.lower()
       or "Add one mana of any color" not in text_m
       or card_a.get("mana_cost")!="{3}"
       or "{T}: Add one mana of any color" not in text_a
       or "{4}, {T}" not in text_a
       or "Activate only as a sorcery" not in text_a
       or "Double the number of each kind of counter on target permanent" not in text_a
       or faces[0].get("mana_cost")!="{1}{U}{B}{R}"
       or "{4}{U}{B}{R}" not in faces[0].get("oracle_text","")
       or faces[1].get("loyalty")!="7"):
    raise ValueError("Frozen authoritative Mox/Amp/Bolas cost, tap or transformation text drift")
  return {name:"sha256:"+hashlib.sha256(text.encode()).hexdigest()
    for name,text in [(MOX,text_m),(AMP,text_a),(BOLAS,"\n".join(f["oracle_text"] for f in faces))]}

def verify(p,registry,old,R):
 if (p["cycle"]!=126 or p["schema_version"]!=1 or
     p["status"]!="preregistered_before_code_or_results" or p["authority"]!=AUTH or
     p["base_head"]!="aa3a18821b908b62b5dc7e80a5a77ae5ab896429" or
     p["simulation"]["paired_shuffles"]!=1024 or p["simulation"]["seed"]!=120026 or
     p["simulation"]["turns"]!=8 or p["simulation"]["opening"]!=7 or
     p["simulation"]["draw_per_turn"]!=1 or p["simulation"]["mulligans"] is not False or
     p["simulation"]["policies"]!=list(POLICIES) or
     registry["program"]["milestones"]["M6"]["status"]!="in_progress" or
     registry["program"]["milestones"]["M7"]["status"]!="not_started" or len(registry["decks"])!=62):
  raise ValueError("Cycle126 prereg/authority status drift")
 st=p["study"];source=next(x for x in old["studies"] if x["deck_id"]=="Nicol_Bolas__the_Ravager")
 r=registry["decks"]["Nicol_Bolas__the_Ravager"]
 if (st!=source or st["cut"]!=MOX or st["add"]!=AMP or st["commander"]!=BOLAS or
     r["current_canonical_hash"]!=st["approved_logical_hash"] or
     r["source"]["recorded_sha256"]!=st["approved_raw_sha256"] or
     r["source"]["recorded_matches_raw"] is not True or
     ga.text_hash(ga.deck_block_text(st["slug"]),R)!=st["approved_logical_hash"]):
   raise ValueError("Exact approved Bolas M5 swap or source hash mismatch")
 names=frozen_card_gates(R)
 if len(c103.oracle_checks(R,c103.read(c122.LAND_PLAN)))!=19:
   raise ValueError("Existing 19 named-land Oracle gate drift")
 return names

def supported_sources(t,exclude_amp=False):
  a=[]
  for uid in t.zones["battlefield"]:
   if uid in t.tapped:continue
   name=t.cards[uid]["name"]
   if t.cards[uid].get("land") and c122.is_supported_land(t,uid):
    a.append((uid,colors(name)))
   elif name in (MOX,AMP) and not(name==AMP and exclude_amp):
    a.append((uid,tuple("UBR")))
  return sorted(a)

def planned_payment(t,cost,exclude_amp=False):
 """Pure payment preflight; colored-pip matching plus ordinary generic sources.
 Search avoids imaginary mana and matches at most 7 physical source taps.
 """
 generic,pips=cost
 available=supported_sources(t,exclude_amp)
 need=generic+len(pips)
 if len(available)<need:return None
 opts=dict(available)
 bypip=[sorted(uid for uid,cs in available if pip in cs) for pip in pips]
 if any(not row for row in bypip):return None
 best=None
 for colored_uids in itertools.product(*bypip):
  if len(set(colored_uids))!=len(colored_uids):continue
  left=[uid for uid,_ in available if uid not in colored_uids]
  if len(left)<generic:continue
  for extra in itertools.combinations(left,generic):
   # Use a color from each generic source as actual physically generated mana.
   assignment=list(zip(colored_uids,pips))+[(uid,opts[uid][0]) for uid in extra]
   life=sum(t.cards[uid]["name"]=="Mana Confluence" for uid,_ in assignment)
   if t.pilot<=life:continue
   ordered=sorted(assignment)
   score=(life,tuple(ordered))
   if best is None or score<best[0]:best=(score,ordered)
 return None if best is None else best[1]

def pay_physical(t,assignment,event):
 if assignment is None:raise BlockedAction("No physically payable source assignment")
 before=t.pilot
 with t.atomic():
  for uid,color in assignment:
   name=t.cards[uid]["name"]
   if t.cards[uid].get("land"):
    t.tap_land(uid,color)
   else:
    if name not in (MOX,AMP) or uid in t.tapped or t.zone_of(uid)!="battlefield" or color not in "UBR":
     raise BlockedAction("Tapped/absent/unmodeled artifact mana source")
    t.tapped.add(uid)
    t.mana[color]+=1
   if t.mana[color]<=0:raise AssertionError("No actual mana produced")
   t.mana[color]-=1  # immediately pay printed cost; no floating mana.
  t.priority_events.append({"event":event,"payment":list(assignment),
                            "life_paid":before-t.pilot,"no_opponent_response_simulated":True})
 t.check()
 return [{"id":uid,"name":t.cards[uid]["name"],"color":color} for uid,color in assignment]

def physical_mox_entry(t):
 """After land drop, require a *different actual land card still in hand*."""
 uid=next((u for u in t.zones["hand"] if t.cards[u]["name"]==MOX),None)
 if uid is None:return None
 lands=[u for u in t.zones["hand"] if u!=uid and t.cards[u].get("land",False)]
 if not lands:return None
 # Rational fixed discarding policy: discard an unsupported land first, then name/UID.
 lands.sort(key=lambda u:(c122.is_supported_land(t,u),t.cards[u]["name"],u))
 discard=lands[0]
 with t.atomic():
  t.transfer(discard,"hand","graveyard")
  t.transfer(uid,"hand","battlefield")
  t.priority_events.append({"event":"physical_mox_entry_with_land_replacement",
      "mox_uid":uid,"discard_uid":discard,"discard_name":t.cards[discard]["name"],
      "not_an_additional_land_drop":True,"opponents_pass_assumed":True})
 return {"mox_uid":uid,"discard_uid":discard,"discard_name":t.cards[discard]["name"],
         "entry_turn":t.turn}

def paid_amplifier_cast(t):
 uid=next((u for u in t.zones["hand"] if t.cards[u]["name"]==AMP),None)
 if uid is None:return None
 sources=planned_payment(t,COSTS["amplifier_cast"])
 if sources is None:return None
 paid=pay_physical(t,sources,"amplifier_artifact_printed_cost_paid")
 with t.atomic():
  t.transfer(uid,"hand","battlefield")
  t.priority_events.append({"event":"amplifier_placed_uncontested_after_paid_cast",
                             "uid":uid,"can_tap_for_mana_same_turn":True})
 return {"turn":t.turn,"sources":paid}

def pay_and_place_commander(t):
 if "c000" not in t.zones["command"]:return None
 srcs=planned_payment(t,COSTS["commander"])
 if srcs is None:return None
 paid=pay_physical(t,srcs,"ravager_printed_four_mana_paid")
 with t.atomic():
  t.transfer("c000","command","battlefield")
  t.priority_events.append({"event":"uncontested_commander_placement",
       "not_modeling_three_opponent_ETB_discards":True})
 return {"turn":t.turn,"sources":paid}

def source_transform(t):
 if "c000" not in t.zones["battlefield"]:return None
 srcs=planned_payment(t,COSTS["transform"])
 if srcs is None:return None
 paid=pay_physical(t,srcs,"ravager_seven_mana_transform_activation_paid")
 with t.atomic():
  t.transfer("c000","battlefield","exile")
  t.transfer("c000","exile","battlefield")
  t.priority_events.append({"event":"uncontested_transform_to_Arisen",
       "starting_loyalty":7,"no_activated_loyalty_abilities_simulated":True})
 return {"turn":t.turn,"sources":paid,"initial_loyalty":7}

def source_double(t,loyalty=7,own_main=True,stack_empty=True):
 if not own_main or not stack_empty or t.priority_seat!=0 or t.frames or t.zones["stack"]:
  return None
 amplifier=next((u for u in t.zones["battlefield"] if t.cards[u]["name"]==AMP),None)
 if amplifier is None or amplifier in t.tapped:return None
 assignment=planned_payment(t,COSTS["amplifier_double"],exclude_amp=True)
 if assignment is None:return None
 paid=pay_physical(t,assignment,"amplifier_four_mana_sorcery_ability")
 with t.atomic():
  if amplifier in t.tapped:raise BlockedAction("Amplifier tap used for other ability already")
  t.tapped.add(amplifier)
  t.priority_events.append({"event":"bounded_uncontested_loyalty_counters_doubled",
                             "before":loyalty,"after":loyalty*2,"extra_loyalty_activations":0})
 return {"turn":t.turn,"before":loyalty,"after":loyalty*2,"sources":paid}

def pressure_thresholds(loyalty):
 """Pure hypothetical loyalty reduction, not sampled combat or opponents."""
 if loyalty is None:return None
 return {str(d):{"remaining":max(0,loyalty-d),"survives":loyalty>d}
        for d in (3,8,13)}

def simulate_one(library,commanders,permutation,policy):
 if policy not in POLICIES:raise ValueError("Unknown preregistered pilot policy")
 t=PriorityNonbasic(library,commanders,seed=120026,opponent_count=3)
 t.zones["library"]=[f"m{i:03d}" for i in permutation];t.check()
 t.draw(7)
 result={"policy":policy,"mox_entry":None,"amp_cast":None,
         "ravager_cast":None,"transform":None,"double":None,"unsupported_land_seen":set()}
 for turn in range(1,9):
  if turn>1:t.next_turn()
  t.draw(1)
  for uid in t.zones["hand"]:
   if t.cards[uid].get("land") and not c122.is_supported_land(t,uid):
    result["unsupported_land_seen"].add(t.cards[uid]["name"])
  c122.choose_land(t,"")   # Cycle122 *color-neutral* deterministic land policy
  if policy=="baseline_mox_commander_first" and result["mox_entry"] is None:
   result["mox_entry"]=physical_mox_entry(t)
  if policy=="candidate_amplifier_early" and result["amp_cast"] is None:
   result["amp_cast"]=paid_amplifier_cast(t)
  if result["ravager_cast"] is None:
   result["ravager_cast"]=pay_and_place_commander(t)
  # Sorcery-speed transform cannot be attempted in model during its cast turn.
  if (result["ravager_cast"] is not None and
      t.turn>result["ravager_cast"]["turn"] and result["transform"] is None):
   result["transform"]=source_transform(t)
  if policy=="candidate_amplifier_commander_first" and result["ravager_cast"] is not None and result["amp_cast"] is None:
   result["amp_cast"]=paid_amplifier_cast(t)
  if result["transform"] and result["amp_cast"] and result["double"] is None:
   result["double"]=source_double(t,7)
  t.check()
  if any(t.mana.values()):raise AssertionError("Generated/spent mana is not zero at step end")
  if t.receipt()["count"]!=100:raise AssertionError("Lost a physical approved card")
 result["unsupported_land_seen"]=sorted(result["unsupported_land_seen"])
 result["pressure"]=pressure_thresholds(
   14 if result["double"] is not None else 7 if result["transform"] is not None else None)
 result["physical_card_count"]=t.receipt()["count"]
 result["virtual_opponents_actually_simulated"]=0
 result["loyalty_ability_resolutions"]=0
 return result

def run():
 plan,registry,previous=map(read,(PLAN,SOURCE,PARENT))
 R=ev.Resolver();oracle=verify(plan,registry,previous,R)
 st=plan["study"]
 a,b,changed,text,flags=c120.verify_exact_pair(
   {"slug":st["slug"],"cut":st["cut"],"add":st["add"],
    "commander":st["commander"],"approved_logical_hash":st["approved_logical_hash"],
    "opportunities":[]},R)
 src=sim.load_deck(st["slug"],R,text=text)
 alternative=sim.load_deck(st["slug"],R,text=c120.c118.replace_exact_slot(text,MOX,AMP))
 base,alt,pairs=paired.align(src,alternative,[(MOX,AMP)])
 if pairs!=[(MOX,AMP)] or base.N!=99 or alt.N!=99 or changed<0:
  raise ValueError("Unpaired approved 99-card physical source")
 records={p:{"policy":p,"n":1024,
       "mox_entries":0,"amp_casts":0,"commander_casts":0,"transformations":0,
       "paid_loyalty_doubles":0,"first_commander_by_turn":Counter(),
       "first_transform_by_turn":Counter(),"first_double_by_turn":Counter(),
       "pressure_3_survivals":0,"pressure_8_survivals":0,"pressure_13_survivals":0,
       "unsupported_land_source_sample_count":Counter(),"physical_examples":[]} for p in POLICIES}
 for i in range(1024):
  perm=random.Random(sim.seed_for(120026,i)^0x5EED).sample(range(99),99)
  for policy in POLICIES:
   model=base if policy==POLICIES[0] else alt
   z=simulate_one(model.library,model.commanders,perm,policy)
   d=records[policy]
   d["mox_entries"]+=int(z["mox_entry"] is not None)
   d["amp_casts"]+=int(z["amp_cast"] is not None)
   d["commander_casts"]+=int(z["ravager_cast"] is not None)
   d["transformations"]+=int(z["transform"] is not None)
   d["paid_loyalty_doubles"]+=int(z["double"] is not None)
   for name,key in (("ravager_cast","first_commander_by_turn"),("transform","first_transform_by_turn"),("double","first_double_by_turn")):
    if z[name] is not None:d[key][str(z[name]["turn"])]+=1
   if z["pressure"]:
    for damage in (3,8,13):
     d[f"pressure_{damage}_survivals"]+=int(z["pressure"][str(damage)]["survives"])
   for name in z["unsupported_land_seen"]:d["unsupported_land_source_sample_count"][name]+=1
   if (z["ravager_cast"] or z["double"]) and len(d["physical_examples"])<2:
    d["physical_examples"].append({"sample_index":i,"cast_turn":z["ravager_cast"]["turn"] if z["ravager_cast"] else None,
        "transform_turn":z["transform"]["turn"] if z["transform"] else None,
        "paid_double_turn":z["double"]["turn"] if z["double"] else None,
        "mox_discard":z["mox_entry"],"amplifier_paid":z["amp_cast"],
        "physical_source_payments":z["ravager_cast"]["sources"] if z["ravager_cast"] else []})
 rows=[]
 for p in POLICIES:
  d=records[p]
  for key in ("first_commander_by_turn","first_transform_by_turn","first_double_by_turn","unsupported_land_source_sample_count"):
   d[key]=dict(sorted(d[key].items()))
  rows.append(d)
 return {"schema_version":1,"cycle":126,
      "stage":"M6_PAIRED_PHYSICAL_MANA_AND_HYPOTHETICAL_LOYALTY_NOT_GAMEPLAY",
      "preregistered_plan_sha256":sha(PLAN),"registry_sha256":sha(SOURCE),
      "frozen_oracle_card_text_sha256":oracle,
      "physical_approved_main_count":99,"commanders":1,"one_changed_physical_slot_index":changed,
      "approved_raw_sha256_recorded":st["approved_raw_sha256"],
      "approved_logical_hash":st["approved_logical_hash"],
      "paired_physical_shuffles":1024,"arm_policy_views":3072,
      "policies":rows,"opponents_actually_simulated":0,
      "conditional_commander_ETB_discard_events_resolved":0,"actual_planeswalker_combat_damage_observed":0,
      "actual_multiplayer_game_wins":0,"independent_Pass_C_certified":False,"phase_B_certified":False,
      "candidate_deck_approved":False,"m6_accepted":False,"m7_started":False,
      "canonical_decks_modified":0,
      "limitations":["Only 19 named nonbasic mana sources plus printed basics; many source lands, tutors, treasures, rituals and other ramp unmodeled.",
       "Color-neutral deterministic land selection and two contrasting Amplifier casting priorities are fixed test policies, not competent/optimal player choices.",
       "Commander, Amp, and transform resolution assumed uncontested; no real opponents, stack interaction or ETB discard outcomes.",
       "Planeswalker starting loyalty 7, and any doubling requires physically source-paid {4} plus unused Amplifier tap in own main phase. No actual loyalty ability uses.",
       "Pressure amounts 3,8,13 are hypothetical loyalty thresholds, never observed opponent damage or game outcomes.",
       "Results are source-payable bounded opportunity comparisons, not deck win rates, statistical commander optimization or permission for approved swaps."]}

def main():
 ap=argparse.ArgumentParser()
 ap.add_argument("--build",action="store_true");ap.add_argument("--check",action="store_true")
 args=ap.parse_args()
 if not(args.build or args.check):ap.error("Use --build or --check")
 output=enc(run())
 if args.build:OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(output,encoding="utf-8")
 if args.check and (not OUT.exists() or OUT.read_text(encoding="utf-8")!=output):
  raise ValueError("Cycle126 Bolas source/loyalty results are not reproducible")
 print("Cycle126: 1024 exact Bolas source-paired shuffles x 3 bounded source policies; no opponent games, recommendations or certifications.")
if __name__=="__main__":main()
