#!/usr/bin/env python3
"""Cycle127: reproducible 62-deck M6 review intake. Preparation, never judgment.

Reviewers must independently check Oracle text, game behavior, candidate
quality and the locked canonical list before issuing a finding. This script
does NOT contact an independent critic or certify any milestone.
"""
from __future__ import annotations
import argparse, hashlib, json, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_m6_cycle117_independent_review_readiness as prior

PLAN=ROOT/"data/grixis/m6/phase_b_plans/cycle127_batch_intake_preregistered_01.json"
REG=ROOT/"data/grixis/registry.json"
TRI=ROOT/"data/grixis/m6/phase_b_bounded/commander_first_readiness_62_01.json"
TRACK=ROOT/"data/grixis/milestone_m6_m7_subtracker.json"
OUT=ROOT/"data/grixis/m6/independent_review_intake/cycle127_62_deck_batch_queue_01.json"
ZERO={"formal_pass_c_completed":0,"complete_phase_b_certified":0,
      "new_authored_reviews":0,"canonical_deck_changes":0,
      "approved_swaps":0,"M6_accepted":False,"M7_started":False}
SHA=lambda path:"sha256:"+hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(p):return json.loads(Path(p).read_text(encoding="utf-8"))
def encode(data):return json.dumps(data,sort_keys=True,indent=2,ensure_ascii=False)+"\n"

def verify_source(plan,reg,tri,track,authored):
    if (plan["cycle"]!=127 or plan["status"]!="PREREGISTERED_BEFORE_IMPLEMENTATION"
        or plan["schema_version"]!=1 or len(reg["decks"])!=62 or
        any(plan["authority"].values()) or
        any(reg["program"]["milestones"]["M"+str(i)]["status"]!="accepted" for i in range(6)) or
        reg["program"]["milestones"]["M6"]["status"]!="in_progress" or
        reg["program"]["milestones"]["M6"]["accepted_by"] is not None or
        reg["program"]["milestones"]["M7"]["status"]!="not_started" or
        track["m6"]["formal_m6_certified_decks"]!=0 or
        track["display"]["m6_completed_gates"]!=3 or
        track["display"]["m7_completed_gates"]!=0):
        raise ValueError("Milestone, preregistration or authority drift")
    tri_rows=tri["ordered_decks"]
    if len(tri_rows)!=62 or len({r["deck_id"] for r in tri_rows})!=62 or len(authored)!=15:
        raise ValueError("Expected exact 62 source decks and 15 preexisting authored reviews")
    if set(reg["decks"])!={r["deck_id"] for r in tri_rows}:
        raise ValueError("Unlisted or missing authoritative deck")
    if len({r["deck_id"] for r in authored})!=15:
        raise ValueError("Reused authored review to inflate progress")
    return tri_rows

def packet(queue,reg,authored):
    did=queue["deck_id"]; meta=reg["decks"][did]
    if (meta["deck_id"]!=did or meta["slug"]!=queue["slug"] or
        meta["commanders"]!=queue["commanders"] or
        meta["current_canonical_hash"]!=queue["source_canonical_logical_hash"] or
        meta["source"]["recorded_sha256"]!=queue["recorded_source_approved_raw_sha256"] or
        meta["source"]["raw_sha256"]!="sha256:"+meta["source"]["recorded_sha256"] and
        meta["source"]["recorded_matches_raw"] is True):
        raise ValueError("Canonical identity/raw SHA drift: "+did)
    bp_path=ROOT/"data/grixis/blueprints"/(meta["slug"]+".json")
    bp=read(bp_path)
    if (bp["deck_id"]!=did or bp["canonical_hash"]!=meta["current_canonical_hash"] or
        SHA(bp_path)!=queue["blueprint_sha256"]):
        raise ValueError("Blueprint or commander-specific strategy drift: "+did)
    opts=queue["first_three_TO_REVIEW_NOT_TO_APPLY"]
    if len(opts)!=3 or len({c["swap_id"] for c in opts})!=3:
        raise ValueError("Source candidate queue missing or duplicated: "+did)
    if any(not x["add"] or not x["cut"] or x["add"]==x["cut"] or
           x["card_added_to_canonical_deck"] is not False for x in opts):
        raise ValueError("Invalid M5 hypothetical add/cut: "+did)
    author=authored.get(did)
    if author:
        matches=[x for x in opts if x["swap_id"]==author["swap_id"] and
                 (x["add"],x["cut"])==(author["add"],author["cut"])]
        if len(matches)!=1 or meta["source"]["recorded_sha256"]!=author["approved_raw_sha256"]:
            raise ValueError("Preexisting author review source pair mismatch: "+did)
        chosen=matches[0]
    else:
        chosen=opts[0]
    if not chosen["swap_id"].startswith("swap:"+meta["slug"]+":m5:"):
        raise ValueError("Candidate does not belong to this deck: "+did)
    exception_status={
      "official_status_at_frozen_snapshot":meta["official_commander_compliance"]["status"],
      "project_authorization_status":meta["project_authorization_status"],
      "registered_project_exceptions":meta["project_exceptions"],
      "future_release_handling_from_source":queue["intentional_future_release_exceptions"],
      "current_official_legality_reverified":False,
    }
    return {
      "deck_id":did,"slug":meta["slug"],"commander_names":meta["commanders"],
      "queue_position_not_power_rank":queue["review_queue_position_NOT_a_deck_strength_rank"],
      "triage_tier_not_power_bracket":queue["tier"],
      "approved_engineering_logical_hash":meta["current_canonical_hash"],
      "recorded_source_raw_sha256_not_rehashed":meta["source"]["recorded_sha256"],
      "historical_recorded_source_hash_matches_raw":meta["source"]["recorded_matches_raw"],
      "source_path":meta["source"]["path"],
      "source_blueprint_sha256":SHA(bp_path),
      "commander_first_primary":bp["plan"]["value"]["primary"],
      "commander_first_secondary":bp["plan"]["value"]["secondary"],
      "protected_identity_core":bp["identity_core"],
      "source_anti_goals":bp["anti_goals"]["value"],
      "candidate_id":chosen["swap_id"],"challenger_add":chosen["add"],
      "baseline_cut":chosen["cut"],"M5_screening_flags_not_evidence":chosen["M5_flags"],
      "historical_author_review_exists":bool(author),
      "authored_source_path":author["source_path"] if author else None,
      "author_review_cycle":author["author_cycle"] if author else None,
      "next_required_gate":"INDEPENDENT_PASS_C_AND_EFFECT_AWARE_TESTING" if author else "COMMANDER_SPECIFIC_AUTHORED_REVIEW",
      "required_review_fields":["frozen_and_current_Oracle_checks","commander_mechanics",
        "positive_candidate_case","baseline_cut_cost","adversarial_candidate_case",
        "nonhomogenization_analysis","necessary_effect_aware_tests",
        "provisional_recommendation_with_limits","attributable_independent_critic",
        "conflict_reconciliation"],
      "exception_treatment":exception_status,
      "no_author_verdict_in_packet":True,
      "no_current_oracle_or_gameplay_claim":True,
    }

def generate():
    p,reg,tri,track=map(read,(PLAN,REG,TRI,TRACK))
    authors=prior.source_rows()
    rows=verify_source(p,reg,tri,track,authors)
    by_author={x["deck_id"]:x for x in authors}
    # No authored recommendation is copied into the neutral reviewer-facing packet.
    packets=[packet(x,reg,by_author) for x in rows]
    old=sum(x["historical_author_review_exists"] for x in packets)
    missing=sum(not x["historical_author_review_exists"] for x in packets)
    if (old,missing)!=(15,47) or len({x["candidate_id"] for x in packets})!=62:
        raise ValueError("Authored backlog count drift, duplicate candidate or source gap")
    source_hashes={str(n):SHA(ROOT/path) for n,path in prior.SOURCES.items()}
    source_hashes.update({"registry":SHA(REG),"triage":SHA(TRI),"tracker":SHA(TRACK),
                          "preregistration":SHA(PLAN)})
    return {"schema_version":1,"cycle":127,
      "stage":"AUTHOR_PREPARED_M6_INTAKE_ONLY_NO_MILESTONE_PROMOTION",
      "prepared_decks":62,"previous_authored_decks":old,"awaiting_authored_review":missing,
      "previous_independent_reviews_formally_certified":0,
      "prepared_neutral_packet_count":len(packets),"source_sha256":source_hashes,
      "packets":packets,"zero_authority_outcomes":ZERO,
      "CI_is_not_independent_review":True,
      "full_phase_b_or_m6_certificates_created":False,
      "durability_notice":"Committed exact source references and CI artifacts persist. No GitHub runner or ChatGPT process will independently write future engineering commits.",
      "next_recommended_batch":"Start 47 missing case-specific author reviews in source-locked batches. Request separate named independent critique and reconcile evidence without changing approved lists."}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--build",action="store_true")
    parser.add_argument("--check",action="store_true")
    args=parser.parse_args()
    if not(args.build or args.check):parser.error("Select --build and/or --check")
    data=encode(generate())
    if args.build:
        OUT.parent.mkdir(parents=True,exist_ok=True)
        OUT.write_text(data,encoding="utf-8")
    if args.check and (not OUT.exists() or OUT.read_text(encoding="utf-8")!=data):
        raise ValueError("Source-bound Cycle127 intake replay differs")
    print("Cycle127 PASS: 62 review packets; 15 historical authored, 47 pending; zero newly certified, zero swaps.")
if __name__=="__main__":main()
