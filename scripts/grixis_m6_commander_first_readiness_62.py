#!/usr/bin/env python3
"""Cycle111: deterministic 62-commander M6 RESEARCH READINESS audit.

No swap is selected, approved, tested or certified. M5 screening is never a
replacement for named commander-first judgment or a real effect-aware Phase B.
Canonical approved 62 lists live in a SEPARATE GitHub repository; this script
requires source consistency only, not an invented fresh canonical API read.
"""
from __future__ import annotations
import argparse,hashlib,json
from collections import Counter,defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
PLAN=ROOT/"data/grixis/m6/phase_b_plans/commander_first_readiness_62_01.json"
REG=ROOT/"data/grixis/registry.json"
BP=ROOT/"data/grixis/blueprints"
PACK=ROOT/"data/grixis/m6/review_packets"
ABADDON=ROOT/"data/grixis/m6/phase_b_bounded/abaddon_common_board_summary_01.json"
OUT=ROOT/"data/grixis/m6/phase_b_bounded/commander_first_readiness_62_01.json"
SUMMARY=ROOT/"data/grixis/m6/phase_b_bounded/commander_first_readiness_62_summary_01.json"
PRIORITIES=("P0_independent_agreement","P1_measured_performance_only","P2_commander_named_blueprint_only","P3_commander_fit_only")
TIERS=("A_source_agreement_low_triage_burden","B_source_agreement_needs_specific_review","C_commander_only_or_performance_only")
AUTH={"can_change_decklists":False,"can_approve_or_lock":False,"can_decide":False,"can_certify_M6":False}
def get(p):return json.loads(p.read_text(encoding="utf-8"))
def hash_(p):return "sha256:"+hashlib.sha256(p.read_bytes()).hexdigest()
def fmt(x):return json.dumps(x,sort_keys=True,indent=2,ensure_ascii=False)+"\n"

def checked_packet(packet,deck,blueprint):
 slug=deck["slug"]
 did=deck["deck_id"]
 if (packet["deck_id"]!=did or packet["slug"]!=slug or
     blueprint["deck_id"]!=did or blueprint["slug"]!=slug or
     packet["list_hash"]!=deck["current_canonical_hash"] or
     blueprint["canonical_hash"]!=deck["current_canonical_hash"]):
  raise ValueError("Blue/packet/registry ID, slug or canonical hash drift: "+did)
 # Exactly one registered, intentional approved-vs-current logical hash
 # reconciliation is allowed: designated Lutri COMPANION outside the 100.
 # Other baseline/current mismatch is a hard stop.
 if deck["baseline_hash"]!=deck["current_canonical_hash"]:
  intentional=(did=="Cecily__Bjorna__Lutri" and
    deck.get("canonical_differs_from_source")==[
      "canonical adds 1x Lutri, the Spellchaser (companion)",
      "reason: the source's approval record designates Lutri as companion outside the 100 (missing from its approved 100-card file); authorized project exception"]
    and any("lutri-the-spellchaser" in x for x in deck.get("project_exceptions",[])))
  if not intentional:
   raise ValueError("Unregistered baseline/current deck mismatch: "+did)
 if (packet["stage"]!="M6_strategic_review_packet" or
    packet["authority"].get("can_apply_swap") is not False or
    packet["authority"].get("can_approve_or_lock") is not False or
    packet["authority"].get("can_decide") is not False or
    packet["authority"].get("can_write_judgment_review") is not False):
  raise ValueError("M5 packet made unauthorized decision for "+did)
 items=packet["items"]
 if not items or packet["counts"]["deep_review"]!=len(items):
  raise ValueError("Missing or miscounted deep review items for "+did)
 if packet["policy"]["priority_order"]!=list(PRIORITIES):
  raise ValueError("M5 source priority classes were modified for "+did)
 swapids=[x.get("swap_id") for x in items]
 if any(not q for q in swapids) or len(swapids)!=len(set(swapids)):
  raise ValueError("Duplicate or blank M5 swap IDs in "+did)
 if not blueprint.get("plan",{}).get("value",{}).get("primary"):
  raise ValueError("Blueprint lacks distinct commander-first primary plan: "+did)
 if not blueprint.get("commanders",{}).get("value"):
  raise ValueError("Blueprint lacks named actual commanders: "+did)
 counts=Counter()
 for it in items:
  if (it.get("base_hash")!=packet["list_hash"] or
      it.get("authority",{}).get("can_decide") is not False or
      it.get("candidate",{}).get("screening_can_decide") is not False or
      not it.get("add") or not it.get("cut") or
      not it.get("expected_cost") or not it.get("hypothesis")):
   raise ValueError("Unverified M5 source item cannot be read as card decision: "+did)
  if it["priority_class"] not in PRIORITIES:raise ValueError("Unknown M5 category")
  counts["priority:"+it["priority_class"]]+=1
  counts["source:"+it["source"]]+=1
  counts["scrutiny:"+it["scrutiny"]]+=1
  for f in it["flags"]:counts["flag:"+f]+=1
 for k,v in counts.items():
  if k in packet["counts"] and packet["counts"][k]!=v:
   raise ValueError("M5 aggregate packet integrity mismatch "+did+" "+k)
 for k,v in packet["counts"].items():
  if k.startswith(("source:","scrutiny:","priority:","flag:")) and counts.get(k,0)!=v:
   raise ValueError("M5 declared versus observed "+k+" mismatch for "+did)
 return counts

def candidate_triage(item,bp):
 core={x["card"] for x in bp.get("identity_core",[]) if x.get("card")}
 protected_packages=[
    {"id":x["id"],"role":x.get("role"),"required":True}
    for x in bp.get("packages",[])
    if x.get("required") and item["cut"] in x.get("cards",[])]
 flags=set(item["flags"])
 blockers=[]
 if item["cut"] in core:blockers.append("CUTS_EXPLICIT_BLUEPRINT_IDENTITY_CORE")
 if protected_packages:blockers.append("CUTS_REQUIRED_COMMANDER_BLUEPRINT_PACKAGE")
 if item.get("burden",{}).get("level")=="elevated":blockers.append("ELEVATED_STRUCTURAL_BURDEN")
 if "structural_route_risk" in flags:blockers.append("STRUCTURAL_WIN_OR_COMBO_ROUTE_REVIEW")
 if "mechanics_not_modelable" in flags:blockers.append("MECHANICS_NOT_MODELED_BY_M5")
 if "test_fail" in flags:blockers.append("EXPLORATORY_TEST_FAIL")
 if "test_inconclusive" in flags:blockers.append("EXPLORATORY_TEST_INCONCLUSIVE")
 if "project_exception_burden" in flags:blockers.append("EXPLICIT_EXCEPTION_INTERACTION_REVIEW")
 if item["legality"].get("official")!="legal":
  blockers.append("SOURCE_LISTED_OFFICIAL_LEGALITY_NOT_PLAIN_LEGAL_CHECK_EXCEPTION")
 # An absence of these flags is only low screening burden, NOT evidence a
 # replacement is beneficial or has been independently verified.
 low=(item["priority_class"]=="P0_independent_agreement" and not blockers
   and "test_pass" in flags)
 return {"swap_id":item["swap_id"],"add":item["add"],"cut":item["cut"],
   "source":item["source"],"M5_priority_class":item["priority_class"],
   "source_review_order":item.get("review_order"),"screening_tier":item["candidate"].get("tier"),
   "screening_rank_not_a_quality_verdict":item["candidate"].get("rank"),
   "screening_score_NOT_real_game_performance":item["candidate"].get("screening_score"),
   "experimental_test_verdicts":item.get("test_evidence",{}).get("verdict_counts",{}),
   "scrutiny":item["scrutiny"],"M5_flags":sorted(flags),
   "protected_package_deletions":protected_packages,
   "blueprint_identity_core_cut":item["cut"] in core,
   "required_next_from_packet":item["required_next"],
   "triage_caution_codes":blockers,
   "low_M5_triage_burden_only":bool(low),
   "expected_benefit_as_hypothesis_not_verified":item["expected_benefit"],
   "expected_cut_cost_from_M5_not_independent_judgment":item["expected_cost"],
   "card_added_to_canonical_deck":False,"strategic_improvement_verified":False,
   "independent_commander_first_judgment_completed":False}

def queue_key(d):
 t=d["tier"]
 return (TIERS.index(t),-d["low_burden_agreement_hypothesis_count"],
  -d["M5_P0_agreement_count"],d["high_scrutiny_M5_item_count"],d["slug"])

def evaluate():
 plan=get(PLAN);reg=get(REG);abaddon=get(ABADDON)
 if (plan["cycle"]!=111 or plan["status"]!="preregistered_before_implementation"
     or plan["authority"]!=AUTH or plan["roster_exact"]!=62 or
     len(reg["decks"])!=62 or
     any(reg["program"]["milestones"][f"M{i}"]["status"]!="accepted" for i in range(6))
     or reg["program"]["milestones"]["M6"]["status"]!="in_progress"
     or reg["program"]["milestones"]["M6"]["accepted_by"] is not None
     or abaddon["relative_deck_strength"]!="CANNOT_EVALUATE"
     or abaddon["paired_seeds"]!=240):
  raise ValueError("Cycle111 prereg/roster/milestone/original Abaddon evidence drift")
 decks=list(reg["decks"].values())
 slugs={d["slug"] for d in decks}
 if len(slugs)!=62:raise ValueError("Duplicate deck slug in M6 registry")
 actual_bp={p.stem for p in BP.glob("*.json")}
 actual_packets={p.stem for p in PACK.glob("*.json")}
 if actual_bp!=slugs or actual_packets!=slugs:
  raise ValueError("Not exactly 62 matching blueprint+packet slugs; missing or extra: "+
   str(sorted(slugs-actual_bp))+str(sorted(slugs-actual_packets)))
 result=[];grand=Counter()
 all_candidate_ids=set()
 for d in sorted(decks,key=lambda x:x["slug"]):
  bp_path=BP/(d["slug"]+".json")
  packet_path=PACK/(d["slug"]+".json")
  bp=get(bp_path);packet=get(packet_path)
  counts=checked_packet(packet,d,bp)
  candidates=[candidate_triage(it,bp) for it in packet["items"]]
  for row in candidates:
   if row["swap_id"] in all_candidate_ids:
    raise ValueError("Globally repeated swap evidence ID "+row["swap_id"])
   all_candidate_ids.add(row["swap_id"])
  safe=[x for x in candidates if x["low_M5_triage_burden_only"]]
  p0=[x for x in candidates if x["M5_priority_class"]==PRIORITIES[0]]
  tier=TIERS[0] if safe else TIERS[1] if p0 else TIERS[2]
  # Sample ordering only: favor original P0 candidates without identified
  # risk flags, then prior source triage order. Do not let screening score pick.
  ordered=sorted(candidates,key=lambda x:(
    0 if x["low_M5_triage_burden_only"] else 1,
    PRIORITIES.index(x["M5_priority_class"]),len(x["triage_caution_codes"]),
    x["source_review_order"] if isinstance(x["source_review_order"],int) else 999999,
    x["swap_id"]))
  role=bp["commander_role"].get("value",{})
  dependency=bp.get("dependency_level",bp.get("dependency",{}))
  dep=dependency.get("value") if isinstance(dependency,dict) else dependency
  exception=bp.get("project_exceptions") or {}
  named=list(exception.get("exceptions",{}).get("value") or [])
  future=exception.get("future_release") or []
  identities=[x["card"] for x in bp["identity_core"] if x.get("card")]
  exceptions_by_registry=d.get("project_exceptions") or []
  required_pkg=[{"id":x["id"],"role":x.get("role"),"min_count":x.get("min_count")}
    for x in bp.get("packages",[]) if x.get("required")]
  exact_cast={c["name"] for c in bp["commanders"]["value"]}
  if not exact_cast or set(d["commanders"])!=exact_cast:
   raise ValueError("Commander identities drift between registry and blueprint "+d["deck_id"])
  unmodeled=sum("MECHANICS_NOT_MODELED_BY_M5" in x["triage_caution_codes"] for x in candidates)
  identitycuts=sum(x["blueprint_identity_core_cut"] for x in candidates)
  pkgcuts=sum(bool(x["protected_package_deletions"]) for x in candidates)
  allflags=Counter(x for item in packet["items"] for x in item["flags"])
  grand["total_M5_review_hypotheses"]+=len(candidates)
  grand["low_M5_burden_P0_hypotheses"]+=len(safe)
  grand["source_agreement_P0_hypotheses"]+=len(p0)
  grand["cut_explicit_identity_core_hypotheses"]+=identitycuts
  grand["cut_required_package_hypotheses"]+=pkgcuts
  grand["mechanics_not_modelable_M5_hypotheses"]+=unmodeled
  grand["high_scrutiny_M5_hypotheses"]+=counts.get("scrutiny:high_scrutiny",0)
  grand["M5_test_pass_is_not_phase_B_hypotheses"]+=allflags["test_pass"]
  grand["deck_tier_"+tier]+=1
  grand["blueprints_central_role"]+=int(role.get("level")=="central")
  grand["blueprints_significant_role"]+=int(role.get("level")=="significant")
  grand["blueprints_supporting_or_other_role"]+=int(role.get("level")not in ("central","significant"))
  grand["decks_with_intentional_registered_project_exceptions"]+=int(bool(named or future or exceptions_by_registry))
  grand["decks_with_future_release_exception"]+=int(bool(future))
  if d["deck_id"]=="Abaddon_the_Despoiler":
   specialized={"source":"Cycles105-110",
    "exact_comparative_conclusion":"CANNOT_EVALUATE",
    "hold_without_authorizing_card_change":True,
    "role_costs":"Bituminous Blast printed cascade/removal versus delayed opponent life loss; no numeric common payoff"}
  else:specialized=None
  result.append({"deck_id":d["deck_id"],"slug":d["slug"],"commanders":d["commanders"],
    "tier":tier,"source_canonical_logical_hash":d["current_canonical_hash"],
    "recorded_source_approved_raw_sha256":d["source"].get("recorded_sha256"),
    "M6_registry_state":"SOURCE_BASELINE_not_current_approval_authority",
    "documented_baseline_to_companion_reconciliation":d.get("canonical_differs_from_source",[]),
    "blueprint_sha256":hash_(bp_path),"review_packet_sha256":hash_(packet_path),
    "blueprint_core":identities,
    "blueprint_commander_role":role.get("level"),
    "blueprint_role_honest_note":role.get("honest_note"),
    "blueprint_dependency_level":dep,
    "commander_first_primary_plan":bp["plan"]["value"]["primary"],
    "blueprint_anti_goals":bp["anti_goals"].get("value",[]),
    "required_package_protection":required_pkg,
    "intentional_project_exceptions":named,
    "intentional_future_release_exceptions":future,
    "registry_exception_refs":exceptions_by_registry,
    "registered_source_official_legality_status":d.get("official_commander_compliance",{}).get("status"),
    "M5_items_screened_not_approved":len(candidates),
    "M5_P0_agreement_count":len(p0),
    "low_burden_agreement_hypothesis_count":len(safe),
    "high_scrutiny_M5_item_count":counts.get("scrutiny:high_scrutiny",0),
    "required_package_cut_hypothesis_count":pkgcuts,
    "identity_core_cut_hypothesis_count":identitycuts,
    "mechanics_not_modelable_count":unmodeled,
    "source_M5_flag_counts":dict(sorted(allflags.items())),
    "source_M5_priority_counts":{p:sum(c["M5_priority_class"]==p for c in candidates) for p in PRIORITIES},
    "first_three_TO_REVIEW_NOT_TO_APPLY":ordered[:plan["triage_rules"]["review_samples_per_deck"]],
    "all_M5_items_covered_in_risk_inventory":True,
    "formal_phase_b_ready_or_passed":False,
    "named_independent_commander_judgment_completed":False,
    "any_swap_independently_approved_by_this_report":False,
    "tested_pool_zero_improvement_certified":False,
    "Abaddon_prior_comparison":specialized,
    "next_reviewer_task":(
      "Inspect low M5-triage-risk agreement swaps for commander-specific role and actual cost; obtain independent strategic judgment + necessary Phase B."
      if tier==TIERS[0] else
      "Resolve required package, mechanic and structural risks for agreement hypotheses before a candidate is considered for Phase B."
      if tier==TIERS[1] else
      "Conduct commander-first independent role review of nonagreement hypotheses; old goldfish screening cannot choose a swap.")})
 result.sort(key=queue_key)
 for i,d in enumerate(result,1):d["review_queue_position_NOT_a_deck_strength_rank"]=i
 if len(result)!=62 or len(all_candidate_ids)!=grand["total_M5_review_hypotheses"]:
  raise ValueError("Incomplete 62-card per-hypothesis coverage")
 return {"schema_version":1,"cycle":111,"stage":"M6_62_deck_commander_first_source_evidence_triage_not_formal_judgment",
  "plan_sha256":hash_(PLAN),"registry_sha256":hash_(REG),
  "abaddon_cycle110_sha256":hash_(ABADDON),
  "deck_count":62,"blueprint_file_count":len(actual_bp),"packet_file_count":len(actual_packets),
  "source_review_hypothesis_count":grand["total_M5_review_hypotheses"],
  "aggregates":dict(sorted(grand.items())),
  "triage_tiers_not_approval_stages":list(TIERS),
  "queue_tie_breaker_from_registered_plan":plan["triage_rules"]["tie_breaker"],
  "ordered_decks":result,
  "all_62_canonical_approved_unchanged_not_verified_by_this_script":True,
  "all_62_deck_approval_and_final_certificate_unmodified":True,
  "current_official_legality_reverified":False,
  "all_62_actual_phase_b_and_independent_pass_c_completed":False,
  "all_M5_test_pass_flags_provisional":True,
  "can_issue_any_swap_recommendation":False,
  "can_issue_tested_pool_zero_improvement":False,
  "M6_accepted":False,"authority":AUTH,
  "next_gate":"Independent commander-specific priority review with actual effect-aware evidence; external canonical lock check and owner approval are separate."}
def summary(x):
 return {"cycle":111,"deck_count":x["deck_count"],
  "source_review_hypothesis_count":x["source_review_hypothesis_count"],
  "aggregates":x["aggregates"],
  "queue":[{"position":d["review_queue_position_NOT_a_deck_strength_rank"],
    "slug":d["slug"],"deck_id":d["deck_id"],
    "commanders":d["commanders"],"tier":d["tier"],
    "commander_role":d["blueprint_commander_role"],
    "M5_items":d["M5_items_screened_not_approved"],
    "P0_agreement":d["M5_P0_agreement_count"],
    "low_burden_P0":d["low_burden_agreement_hypothesis_count"],
    "identity_core_cut_count":d["identity_core_cut_hypothesis_count"],
    "intentional_exception":bool(d["intentional_project_exceptions"] or d["intentional_future_release_exceptions"]),
    "first_review_pair":[{"add":c["add"],"cut":c["cut"],
       "risk_codes":c["triage_caution_codes"]} for c in d["first_three_TO_REVIEW_NOT_TO_APPLY"][:1]]}
      for d in x["ordered_decks"]],
  "canonical_lists_unchanged":True,
  "queue_not_deck_strength_or_swap_approval":True,
  "full_phase_b_completed":False,"M6_accepted":False}
def main():
 pa=argparse.ArgumentParser()
 pa.add_argument("--build",action="store_true")
 pa.add_argument("--check",action="store_true")
 x=pa.parse_args()
 if not(x.build or x.check):pa.error("require --build/--check")
 data=evaluate();s=fmt(data);compact=fmt(summary(data))
 if x.build:
  OUT.parent.mkdir(parents=True,exist_ok=True)
  OUT.write_text(s,encoding="utf-8");SUMMARY.write_text(compact,encoding="utf-8")
 if x.check and (not OUT.is_file() or OUT.read_text(encoding="utf-8")!=s
          or not SUMMARY.is_file() or SUMMARY.read_text(encoding="utf-8")!=compact):
  raise ValueError("Cycle111 62-deck M5 blueprint/packet triage cannot be reproduced")
 print("Cycle111 62-deck commander-first screening audit:",data["aggregates"],flush=True)
 print("All M5 screening evidence non-authoritative for swaps; no deck certification",flush=True)
if __name__=="__main__":main()
