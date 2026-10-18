#!/usr/bin/env python3
"""Cycle105 evidence-to-decision readiness matrix; NEVER chooses a deck swap.

This reads approved/locked historical authority, M5's 98-item screening packet,
M6's bounded evidence, and the commander blueprint. No new MTG simulation,
effect coverage or opponent outcomes are inferred from screening scores.
"""
from __future__ import annotations
import argparse,hashlib,json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
PLAN=ROOT/"data/grixis/m6/phase_b_plans/abaddon_decision_readiness_01.json"
OUT=ROOT/"data/grixis/m6/phase_b_bounded/abaddon_decision_readiness_01.json"
REG=ROOT/"data/grixis/registry.json"
SOURCE=ROOT/"exports/grixis-archidekt/source-baseline/abaddon-the-despoiler.txt"
AUTH={"can_change_decklists":False,"can_approve_or_lock":False,"can_decide":False,"can_certify_M6":False}
def read(path):return json.loads(path.read_text(encoding="utf-8"))
def sha(path):return "sha256:"+hashlib.sha256(path.read_bytes()).hexdigest()
def encode(x):return json.dumps(x,ensure_ascii=False,sort_keys=True,indent=2)+"\n"
def rel(path):return str(path.relative_to(ROOT))

def list_cards():
 out=[]
 for line in SOURCE.read_text(encoding="utf-8").splitlines():
  if not line.strip():continue
  count,name=line.split(" ",1)
  if name.endswith(" [Commander]"):name=name[:-12]
  out.extend([name]*int(count))
 if len(out)!=100 or out[0]!="Abaddon the Despoiler":
  raise ValueError("Wrong approved Abaddon physical list or card count")
 return out

def assertions(plan,packet,bp,registry,dev,tut,access):
 frozen=plan["frozen"]
 if (plan["cycle"]!=105 or plan["status"]!="preregistered_before_implementation"
     or plan["authority"]!=AUTH or len(packet["items"])!=98
     or packet["deck_id"]!=frozen["baseline_deck_id"]
     or bp["deck_id"]!=frozen["baseline_deck_id"]
     or packet["list_hash"]!=frozen["baseline_logical_hash"]
     or bp["canonical_hash"]!=frozen["baseline_logical_hash"]
     or registry["decks"]["Abaddon_the_Despoiler"]["current_canonical_hash"]!=frozen["baseline_logical_hash"]
     or registry["decks"]["Abaddon_the_Despoiler"]["source"]["recorded_sha256"]!=frozen["approved_list_sha256"]
     or registry["program"]["milestones"]["M6"]["status"]!="in_progress"
     or dev["approved_source_sha256"]!=frozen["approved_list_sha256"]
     or tut["approved_raw_sha256"]!=frozen["approved_list_sha256"]
     or tut["logical_hash"]!=frozen["baseline_logical_hash"]
     or sha(SOURCE)!="sha256:"+frozen["baseline_export_sha256"]
     or access["decks"]!=62 or access["samples"]!=744
     or dev["effect_aware_deckwide_paired_test_executed"]
     or tut["full_deck_gameplay_simulation"]
     or tut["supports_improvement_claim"]
     or tut["formal_independent_pass_c_complete"]):
  raise ValueError("Original deck authority, preregistration or evidence scope drift")
 cards=list_cards()
 for n in plan["focus"]["cuts"]:
  if n not in cards:raise ValueError("Proposed cut absent from original 100 cards "+n)
 for n in plan["focus"]["adds"]:
  if n in cards:raise ValueError("Candidate already in approved main deck "+n)
 # Five-threshold role preservation: cannot silently delete core items.
 if "Bituminous Blast" not in cards or "Kessig Flamebreather" not in cards or not any(x.startswith("Birgi,") for x in cards):
  raise ValueError("Required commander-first packages already modified")
 if len(dev["hypotheses"])!=2 or {x["add"] for x in dev["hypotheses"]}!=set(plan["focus"]["adds"]):
  raise ValueError("Only two registered non-core alternate cuts were studied")

def screening(packet):
 out=[];ids=set()
 for i,item in enumerate(packet["items"],1):
  sid=item.get("swap_id") or item.get("id") or item.get("refs",{}).get("swap_id")
  if sid is None:
   # Older accepted M5 packet stores IDs in swap.ref, not guaranteed item root.
   sid=item.get("refs",{}).get("birthday_evidence","")
  if not item.get("add") or not item.get("cut"):
   raise ValueError("Missing concrete screened swap")
  if item.get("authority",{}).get("can_decide") is not False:
   raise ValueError("M5 screening given unauthorized decision power")
  out.append({"row":i,"add":item["add"],"cut":item["cut"],
    "screening_source_class":item.get("priority_class"),
    "screening_flags":sorted(item.get("flags",[])),
    "screening_verdict_not_a_deck_verdict":True,
    "requires_independent_commander_first_review":True,
    "candidate_swap_approved":False,
    "decision_readiness":"BLOCKED_PENDING_VALID_COMPARISON"})
  ids.add(str(sid))
 if len(out)!=98:raise ValueError("98 screening row conservation failed")
 return out

def provenance_of(a,cut,rows):
 matches=[x for x in rows if x["add"]==a and x["cut"]==cut]
 if len(matches)>1:raise ValueError("Repeated exact M5 swap hypothesis")
 return {"source":"M5_review_packet","row":matches[0]["row"]} if matches else {
  "source":"M6_independently_proposed_alt_cut_not_in_98_M5_rows","row":None}

def decision_rows(plan,rows,dev,tut,bp):
 results=[]
 ids=set((x["add"],x["cut"]) for x in rows)
 h={x["add"]:x for x in dev["hypotheses"]}
 script={x["swap"]["add"]:x for x in tut["results"]}
 for add in plan["focus"]["adds"]:
  for cut in plan["focus"]["cuts"]:
   m5=provenance_of(add,cut,rows)
   core=cut in ("Kessig Flamebreather",
                "Birgi, God of Storytelling // Harnfel, Horn of Bounty")
   if core and (add,cut) not in ids:
    raise ValueError("Expected protected core cut absent from screening packet")
   if not core and (add,cut) in ids:
    raise ValueError("Alternate printed cascade cut mislabeled as not in M5")
   proxy=h[add]["paired_development"] if not core else None
   profile=script[add]["profiles"]["no_removal"] if not core else None
   paired_stats=None if proxy is None else {
     "commander_t4_original_proxy":proxy["commander_cast_by_t4"]["baseline"],
     "commander_t4_challenger_proxy":proxy["commander_cast_by_t4"]["challenger"],
     "commander_t4_delta_proxy":proxy["commander_cast_by_t4"]["paired_diff"],
     "paired_trials":proxy["commander_cast_by_t4"]["trials"],
     "NOT_effect_aware_or_a_win_metric":True}
   cascade=None if profile is None else {
    "baseline_modeled_casts":profile["baseline"]["effect_coverage"]["modeled_casts"],
    "baseline_offers":profile["baseline"]["effect_coverage"]["offered"],
    "baseline_unmodeled_offers":profile["baseline"]["effect_coverage"]["unmodeled_offers"],
    "challenger_modeled_casts":profile["challenger"]["effect_coverage"]["modeled_casts"],
    "challenger_offers":profile["challenger"]["effect_coverage"]["offered"],
    "challenger_unmodeled_offers":profile["challenger"]["effect_coverage"]["unmodeled_offers"],
    "NOT_relative_spell_value_or_a_win_metric":True}
   if cascade and (cascade["baseline_unmodeled_offers"]<=0 or
                   cascade["challenger_unmodeled_offers"]<=0):
    raise ValueError("Former unknown-effect coverage gate unexpectedly closed")
   results.append({
    "add":add,"cut":cut,"registry":m5,
    "phase_b_experiment_priority":"first_comparator" if add=="Heartless Hidetsugu" and not core else
      "secondary_control" if add=="Tree of Perdition" and not core else
      "do_not_promote_before_protected_engine_comparison",
    "preliminary_strategic_status":"DISFAVOR_PROTECTED_ENGINE_CUT" if core else
       "HOLD_PRINTED_CASCADE_AND_INTERACTION_COST_UNMEASURED",
    "protected_role_loss":{
      "early_repeatable_spell_damage":cut=="Kessig Flamebreather",
      "cast_time_mana_and_Harnfel_card_access":cut.startswith("Birgi,"),
      "printed_cascade_plus_instant_speed_creature_removal":cut=="Bituminous Blast",
      "requires_explicit_alternative_role_compensation":True},
    "already_proven_only_as":(
      ["M5_screening_not_effect_aware","commander_role_preliminary_critique"] if core else
      ["800_paired_development_proxies","240_scripted_residual_library_replays",
       "bounded_conditional_life_loss_and_removal_rules"]),
    "paired_development_proxy":paired_stats,
    "finite_cascade_offer_coverage":cascade,
    "hard_gates":{
       "legal_tap_activation_turn_and_source_survival_measured":False,
       "real_card_held_at_follow_up_cast_timing_measured":False,
       "full_color_accurate_mana_and_spell_chain_outcomes_measured":False,
       "opponent_target_and_priority_policy_measured":False,
       "printed_cascade_removal_slot_opportunity_cost_measured":False,
       "unmodeled_cascade_effects_bounded_for_value_comparison":False,
       "independent_pass_c_complete":False,
       "formal_phase_b_ready":False},
    "approved_swap":False,
    "zero_improvement_proven":False,
    "owner_decision_requested":False
   })
 if len(results)!=6:raise ValueError("Six exact swap focus tests missing")
 return results

def verify():
 plan=read(PLAN)
 paths={k:ROOT/v for k,v in plan["frozen"].items() if k.startswith("source_")}
 # source_ prefixes in the preregistration are paths, not trusted code to run
 pkt=read(paths["source_packet"])
 bp=read(paths["source_blueprint"])
 dev=read(paths["source_paired_development"])
 tut=read(paths["source_partial_effects"])
 access=read(paths["source_real_source_access"])
 reg=read(REG)
 assertions(plan,pkt,bp,reg,dev,tut,access)
 rows=screening(pkt)
 focus=decision_rows(plan,rows,dev,tut,bp)
 flags=Counter(x for row in rows for x in row["screening_flags"])
 base_profile=tut["results"][0]["profiles"]["no_removal"]["baseline"]["effect_coverage"]
 if (base_profile["offered"]!=480 or base_profile["unmodeled_offers"]!=307):
  raise ValueError("Unexpected frozen 240-trial baseline coverage")
 return {"schema_version":1,"cycle":105,"status":"decision_gates_open_no_valid_swap_proven",
  "stage":"M6_Abaddon_evidence_readiness_and_falsification_queue",
  "canonical_deck_id":"Abaddon_the_Despoiler",
  "source_approved_list_sha256":plan["frozen"]["approved_list_sha256"],
  "source_list_sha256":sha(SOURCE),"source_blueprint_sha256":sha(paths["source_blueprint"]),
  "source_packet_sha256":sha(paths["source_packet"]),"source_dev_sha256":sha(paths["source_paired_development"]),
  "source_partial_effects_sha256":sha(paths["source_partial_effects"]),
  "source_cycle104_summary_sha256":sha(paths["source_real_source_access"]),
  "prereg_sha256":sha(PLAN),
  "packet_screening_rows":len(rows),"screening_flags_counts":dict(sorted(flags.items())),
  "all_98_items_provisional":True,"screening_queue":rows,
  "deep_focus_comparisons":focus,
  "ready_for_any_card_swap":False,"tested_pool_zero_improvement_certified":False,
  "independent_phase_b_completed":False,"independent_pass_c_completed":False,
  "true_gameplay_win_rate_available":False,"M6_accepted":False,
  "next_discriminating_experiment":{
    "name":"Abaddon hand-cast cascade chain versus protected printed-cascade removal slot",
    "preregister_requirements":[
      "Pair exact 100-card approved baseline and Bituminous Blast -> Heartless challenger, plus Tree secondary control under identical shuffled seeds",
      "Model turn-based access using real physical IDs, actual legal colored mana sources, commander cast/tax, threshold accumulated before subsequent HAND casts, and summoning sickness",
      "Use explicit opponent response policies including creature removal BEFORE tap, source removal AFTER tap, damage prevention, spell counter, and actual legal Bituminous Blast creature targets",
      "Evaluate loss of Bituminous printed cascade/removal, stop if > defined unknown-effect budget and record explicit cannot-evaluate for unsupported effects",
      "Capture conditional cast-from-exile value, residual hand and mana follow-through, source survival, controller self damage and opponent losses",
      "Falsify whether Heartless improves measured commander-first outcomes before considering any swap; Tree is a separate secondary comparator",
      "After a credible discriminating comparison, request named independent Pass C and I/J; user approval is required for any changed list"],
    "unsupported_effects_are_not_zero_value":True},
  "authority":AUTH}
def main():
 ap=argparse.ArgumentParser()
 ap.add_argument("--build",action="store_true")
 ap.add_argument("--check",action="store_true")
 a=ap.parse_args()
 if not (a.build or a.check):ap.error("require --build or --check")
 report=encode(verify())
 if a.build:
  OUT.parent.mkdir(parents=True,exist_ok=True)
  OUT.write_text(report,encoding="utf-8")
 if a.check and (not OUT.exists() or OUT.read_text(encoding="utf-8")!=report):
  raise ValueError("Abaddon Cycle105 independently reproduced readiness matrix drift")
 print("Cycle105: 98 hypotheses, six no-auto-approval commander-specific checks, NO complete Phase B or deck changes")
if __name__=="__main__":main()
