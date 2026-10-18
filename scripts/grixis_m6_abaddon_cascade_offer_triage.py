#!/usr/bin/env python3
"""Cycle108 deterministic audit of *offered*, uncast real cascade card effects.

A Cascade offer is NOT a proven legal/beneficial card cast. We explicitly leave
card value UNKNOWN, even for a hypothetical self-contained known effect, because
Cycle107 declined every offer. This is a decision-readiness inspection only.
"""
from __future__ import annotations
import argparse,hashlib,json,sys
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import evaluate_decklist as ev
import grixis_sim as sim

PLAN=ROOT/"data/grixis/m6/phase_b_plans/abaddon_cascade_offer_triage_01.json"
PREV=ROOT/"data/grixis/m6/phase_b_bounded/abaddon_blast_target_cascade_01.json"
C106=ROOT/"data/grixis/m6/phase_b_bounded/abaddon_physical_slot_summary_01.json"
SOURCE=ROOT/"exports/grixis-archidekt/source-baseline/abaddon-the-despoiler.txt"
REG=ROOT/"data/grixis/registry.json"
OUT=ROOT/"data/grixis/m6/phase_b_bounded/abaddon_cascade_offer_triage_01.json"
AUTH={"can_change_decklists":False,"can_approve_or_lock":False,
      "can_decide":False,"can_certify_M6":False}

def read(p):return json.loads(p.read_text(encoding="utf-8"))
def sha(p):return "sha256:"+hashlib.sha256(p.read_bytes()).hexdigest()
def enc(o):return json.dumps(o,sort_keys=True,indent=2,ensure_ascii=False)+"\n"

def oracle_classification(off,source,permitted):
 """Conservatively triage prerequisites; do not assert full effect legality."""
 name=off["eligible_name"]
 if not name or name not in permitted:
  raise ValueError("Oracle offered name not in approved deck main library: "+str(name))
 if source.get("name")!=name:
  raise ValueError("Scryfall name does not match actual offered card "+name)
 typ=source.get("type_line") or ""
 txt=source.get("oracle_text") or ""
 cost=source.get("mana_cost") or ""
 mv=int(source.get("cmc",-1))
 if not typ or not txt or mv!=off["eligible_mv"] or not 0<=mv<5:
  raise ValueError("Cascade hit Oracle type/cost/eligibility diverged for "+name)
 if source.get("layout") in ("transform","modal_dfc","adventure","split","aftermath"):
  complex_layout=True
 else:complex_layout=False
 if typ.lower().startswith("land") or "land" in [x.strip().lower() for x in typ.split("—")[0].split()]:
  raise ValueError("Land offered as printed-cascade nonland")
 lower=txt.casefold()
 reasons=[]
 if "target" in lower:reasons.append("LEGAL_TARGET_REQUIRES_STACK_OR_BOARD_CONTEXT")
 if "choose" in lower:reasons.append("MODE_OR_CHOICE_NEEDS_CONTEXT")
 if "additional cost" in lower or "as an additional cost" in lower:
  reasons.append("ADDITIONAL_COST_NOT_MODELED")
 if "{x}" in cost.casefold():reasons.append("X_ZERO_FREE_CAST_AND_RELEVANT_EFFECT_UNMODELED")
 if any(t in lower for t in ("graveyard","where x","equal to the number","for each","unless")):
  reasons.append("DEPENDENT_ON_GAME_STATE_OR_CARD_COUNTS")
 if complex_layout:reasons.append("ALTERNATE_CARD_FACE_OR_COMPLEX_LAYOUT")
 if "counter target" in lower:reasons.append("COUNTER_TARGET_ON_STACK_UNKNOWN")
 if "suspend" in lower:reasons.append("SUSPEND_ALTERNATE_TIMING_UNMODELED")
 kind="instant" if "instant" in typ.casefold() else "sorcery" if "sorcery" in typ.casefold() else "permanent" if any(t in typ.casefold() for t in ("creature","artifact","enchantment","planeswalker","battle")) else "unknown"
 if kind=="unknown":reasons.append("UNREGISTERED_SPELL_TYPE")
 # Prior microengines support these four *effects*, but they were NOT cast
 # here. Any projection is therefore a textual property, not a measured benefit.
 known_conditional={
  "Boltwave":"printed nonprevented 3 damage to each opponent if cast and resolved",
  "Flame Rift":"printed nonprevented 4 damage to each player if cast and resolved",
  "Dark Ritual":"printed addition of BBB on resolution if cast",
  "Arcane Signet":"printed permanent enters battlefield and can tap for color-identity mana"
 }.get(name)
 result={
   "name":name,"real_physical_uid":off["eligible_uid"],
   "oracle_sha256":"sha256:"+hashlib.sha256(txt.encode()).hexdigest(),
   "type_line":typ,"printed_mana_cost":cost,"printed_mana_value":mv,
   "cascade_eligible_verified":True,
   "controller_chose_cast":False,
   "spell_legality_if_chosen":"UNVERIFIED_MAY_REQUIRE_CONTEXT",
   "priority_and_effect_resolution":"NOT_EXECUTED",
   "effect_outcome":"UNKNOWN_NOT_ZERO",
   "comparative_deck_value":"UNKNOWN_NOT_ZERO",
   "relevant_target_or_choice_flags":sorted(set(reasons)),
   "effect_text_known_but_NOT_observed":known_conditional,
   "no_numerical_value_assigned":True}
 return result

def offer_rows(data,policy,source_cards,library_names):
 trials=data["policies"][policy]["trials"]
 rows=[]
 for t in trials:
  offers=t["offers"]
  if t["blast_cast"]!=bool(offers) or t["trigger_count"]!=len(offers):
   raise ValueError("Cast/offered-count mismatch at seed "+str(t["seed"]))
  for offer in offers:
   if offer["trigger"]!="printed" or offer["eligible_uid"] is None:
    raise ValueError("Expected one real eligible printed cascade offer per cast")
   if offer["controller_choice"]!="decline_optional_cast" or offer["possible_effect_value"]!="UNKNOWN_NOT_ZERO":
    raise ValueError("Cycle107's unmodeled effect was not explicitly declined+unknown")
   if offer["eligible_name"] not in library_names:
    raise ValueError("Offered card not in approved main library")
   classified=oracle_classification(offer,source_cards[offer["eligible_name"]],library_names)
   classified["seed"]=t["seed"]
   classified["policy"]=policy
   classified["reveal_count"]=offer["number_of_revealed"]
   classified["real_candidate_preceded_by_exiled_cards"]=len(offer["revealed_physical_ids"])>1
   classified["source_blast_target_resolution"]=t["resolution"]
   rows.append(classified)
 return rows

def run():
 p=read(PLAN);old=read(PREV);c106=read(C106);reg=read(REG)
 if (p["cycle"]!=108 or p["status"]!="preregistered_before_implementation"
     or p["authority"]!=AUTH or len(reg["decks"])!=62
     or reg["program"]["milestones"]["M6"]["status"]!="in_progress"
     or p["sample_count"]!=240 or old["sample_count"]!=240
     or sha(SOURCE)!="sha256:"+p["source_export_sha256"]
     or old["approved_sha256"]!=p["approved_raw_sha256"]
     or old["relative_deck_strength"]!="CANNOT_EVALUATE"
     or not old["all_cascade_hits_declined_when_offered"]
     or c106["total_samples"]!=720
     or set(old["policies"])!=set(p["scenarios"])):
  raise ValueError("Cycle108 prereg/approved source/rules authority drift")
 resolver=ev.Resolver()
 deck=sim.load_deck("abaddon-the-despoiler",resolver)
 names={c["name"] for c in deck.library}
 if len(deck.library)!=99 or len(deck.commanders)!=1:
  raise ValueError("Approved physical 99+1 source changed")
 name_offers=set()
 for policy in p["scenarios"]:
  for trial in old["policies"][policy]["trials"]:
   for offer in trial["offers"]:
    if offer["eligible_name"] is not None:name_offers.add(offer["eligible_name"])
 sources={n:resolver.get(n)[0] for n in sorted(name_offers)}
 a=offer_rows(old,p["scenarios"][0],sources,names)
 b=offer_rows(old,p["scenarios"][1],sources,names)
 if len(a)!=7 or len(b)!=7:
  raise ValueError("Expected exactly seven paired real eligible offers per policy")
 for i,(x,y) in enumerate(zip(a,b)):
  for field in ("seed","name","real_physical_uid","printed_mana_value","reveal_count","oracle_sha256"):
   if x[field]!=y[field]:raise ValueError("Paired target-removal policy altered card offer at index "+str(i)+": "+field)
  if x["source_blast_target_resolution"]!="REMOVED_EXTERNAL_3_3_BY_FOUR_DAMAGE":
   raise ValueError("No-removal target fixture did not resolve Blast")
  if y["source_blast_target_resolution"]!="FAILED_TO_RESOLVE_TARGET_ILLEGAL":
   raise ValueError("Removal policy did not invalidate Blast")
 flags=Counter(f for x in a for f in x["relevant_target_or_choice_flags"])
 names_seen=Counter(x["name"] for x in a)
 if c106["result_by_variant"]["Bituminous Blast"]["slot_held_and_mana_affordable"]!=8:
  raise ValueError("Baseline Cycle106 opportunity drift")
 result={"schema_version":1,"cycle":108,"source_sha256":sha(SOURCE),
   "plan_sha256":sha(PLAN),"cycle107_sha256":sha(PREV),"cycle106_sha256":sha(C106),
   "paired_seeds":p["sample_count"],"offers_per_policy":len(a),
   "paired_oracle_verified_real_card_names":dict(sorted(names_seen.items())),
   "source_oracle_gated_cards":{n:{"oracle_sha256":"sha256:"+hashlib.sha256((sources[n].get("oracle_text") or "").encode()).hexdigest(),
     "type_line":sources[n].get("type_line"),"mv":int(sources[n].get("cmc",-1))}
      for n in sorted(name_offers)},
   "relevance_and_cast_condition_flags":dict(sorted(flags.items())),
   "first_policy_offers":a,"second_policy_offers":b,
   "baseline_blast_observations":{"held_and_model_mana_affordable":8,
     "actual_cast_with_scripted_3_3":7,
     "fixture_3_3_removed_if_target_survives":7,
     "blast_failed_if_target_removed_after_cast":7,
     "printed_cascade_eligible_offers":7},
   "challenger_role_context":{
     "Heartless Hidetsugu":{"physically_cast_cycle106":c106["result_by_variant"]["Heartless Hidetsugu"]["slot_cast"],
        "eligible_later_tap_cycle106":c106["result_by_variant"]["Heartless Hidetsugu"]["activation_ready"],
        "does_not_damage_fixture_creature":"TAP_HITS_PLAYERS_ONLY"},
     "Tree of Perdition":{"physically_cast_cycle106":c106["result_by_variant"]["Tree of Perdition"]["slot_cast"],
        "eligible_later_tap_cycle106":c106["result_by_variant"]["Tree of Perdition"]["activation_ready"],
        "does_not_damage_fixture_creature":"TAP_EXCHANGES_TARGET_OPPONENT_LIFE"}},
   "candidate_effects_not_run_against_same_opponent_board":True,
   "offers_declined_in_original_cycle107":True,
   "cascade_cast_legality_resolved":False,
   "cascade_value_range":"UNKNOWN_NOT_ZERO",
   "balanced_three_variant_board_test_complete":False,
   "relative_value":"CANNOT_EVALUATE",
   "supports_improvement_claim":False,"zero_improvement_certified":False,
   "full_phase_b_complete":False,"independent_pass_c_complete":False,
   "M6_accepted":False,"authority":AUTH,
   "next_experiment":{"priority":"choose highest-information offered spells for *actual* source-gated cascade-exile cast+resolution, with equal opponent-board and commander state across three card-slot variants",
                      "decision_gate":"Do not assign a positive/negative comparative value before hit resolution and balanced opponent policy are available",
                      "unknown_event_budget":"Seven of seven offered spell outcomes were not actually executed; prohibit promotion while any of these unresolved effects is decision-relevant."}}
 return result

def main():
 ap=argparse.ArgumentParser()
 ap.add_argument("--build",action="store_true")
 ap.add_argument("--check",action="store_true")
 args=ap.parse_args()
 if not (args.build or args.check):ap.error("require --build/--check")
 obj=run();s=enc(obj)
 if args.build:
  OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(s,encoding="utf-8")
 if args.check and (not OUT.exists() or OUT.read_text(encoding="utf-8")!=s):
  raise ValueError("Cycle108 source-derived cascade offer triage not reproducible")
 print("Cycle108 exact seven physical offers:",obj["paired_oracle_verified_real_card_names"],flush=True)
 print("Unknown cast legality/value remains; NO improved deck or Pass-C certification",flush=True)
if __name__=="__main__":main()
