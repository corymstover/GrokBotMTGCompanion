#!/usr/bin/env python3
"""Strict Abaddon-only pre-J provenance crosswalk; NEVER a complete M6 J bundle.

Binds the *selected physical 100*, original canonical 100, four authored
red-team responses, candidate-specific mana analysis, owner-waived nonindependent
Pass C, and 95 actually registered P0 source tests. Does not claim PASS for
unexecuted tests or convert bounded tests into all-effect gameplay reproduction.
"""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path

from scripts.grixis_m6_bundle_check import validate_pass_c
from scripts.grixis_m7_decision_gate import canonical_source, parse_list

ROOT=Path(__file__).resolve().parents[1]
DECK="Abaddon_the_Despoiler"
CANON="data/grixis/m7/authority_snapshots/Abaddon_the_Despoiler_Approved_2026-10-13.txt"
SELECTED="data/grixis/m7/candidate_lists/Abaddon_the_Despoiler.txt"
J_RED="data/grixis/m6/certification_preflight/Abaddon_M6_J_candidate_red_team_20261022.md"
J_MANA="data/grixis/m6/certification_preflight/Abaddon_M6_J_candidate_mana_20261022.md"
P0="data/grixis/m6/phase_b_plans/abaddon_p0_case_inventory_20261022.json"
M7="data/grixis/m7/decision_reviews/Abaddon_the_Despoiler.json"
M5="data/grixis/m6/ij/input_receipts/abaddon-the-despoiler.json"
PASS_C_ROOT=f"data/grixis/m6/owner_pass_c_substitute/{DECK}"
REG="data/grixis/registry.json"
WAIVER="data/grixis/m6/governance/pass_c_owner_waiver_20261021.json"
PROGRESS="data/grixis/m6/owner_pass_c_substitute/progress.json"
SHA_BASE="2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf"
SHA_CHOSEN="1fabe1251a7868838365144bf0cb1ee903d394ed90ac146b2dd9cdd45683b7dd"
LANDS=set("""Ancient Tomb|Badlands|Blood Crypt|Bloodstained Mire|City of Brass|Command Tower|Exotic Orchard|Flooded Strand|Island|Luxury Suite|Mana Confluence|Marsh Flats|Misty Rainforest|Morphic Pool|Mountain|Otawara, Soaring City|Polluted Delta|Scalding Tarn|Steam Vents|Swamp|Takenuma, Abandoned Mire|Training Center|Underground Sea|Urborg, Tomb of Yawgmoth|Verdant Catacombs|Volcanic Island|Watery Grave|Xander's Lounge""".split("|"))
EXPECTED_RED={"repeated_removal_attrition","pillowfort","token_stall","artifact_enchantment_interaction"}

def digest(relative):
    path=ROOT/relative
    if not path.is_file() or not path.resolve().is_relative_to(ROOT.resolve()):
        raise ValueError("Missing or escaped source "+relative)
    return hashlib.sha256(path.read_bytes()).hexdigest()

def fetch(relative):
    return json.loads((ROOT/relative).read_text(encoding="utf-8"))

def report():
    if digest(CANON)!=SHA_BASE or digest(SELECTED)!=SHA_CHOSEN:
        raise ValueError("Original or selected immutable full 100 SHA drift")
    registry=fetch(REG)["decks"][DECK]
    source_path,md=canonical_source(ROOT,registry)
    baseline,commanders,companions=parse_list(source_path,source_markdown=md)
    chosen,actual_commanders,actual_companions=parse_list(ROOT/SELECTED)
    if (commanders!=["Abaddon the Despoiler"]
         or actual_commanders!=commanders or companions or actual_companions
         or len(baseline)!=100 or len(chosen)!=100):
        raise ValueError("Canonical parsed 100 does not match explicitly pinned candidate")
    original,selected=Counter(baseline),Counter(chosen)
    if (selected-original != Counter({"Grinning Ignus":1,"Chaos Warp":1})
        or original-selected!=Counter({"Rakdos, Lord of Riots":1,"Inevitable Betrayal":1})):
        raise ValueError("Chosen candidate is not exactly authorized research two-swap")
    lands_original=Counter({card:n for card,n in original.items() if card in LANDS})
    lands_selected=Counter({card:n for card,n in selected.items() if card in LANDS})
    if sum(lands_original.values())!=34 or lands_original!=lands_selected or sum(lands_selected.values())!=34:
        raise ValueError("Selected 100 mana base changed or not exactly 34 named original lands")
    old=fetch("data/grixis/commander_mana/abaddon-the-despoiler.json")
    if (old["method"]["samples"]!=500 or old["method"]["seed"]!=6813
        or old["method"]["model"]!="1.1" or old["canonical_hash"]!=registry["current_canonical_hash"]):
        raise ValueError("Historical old-baseline mana evidence misattributed to current candidate")
    red_source=fetch("data/grixis/bracket_red_team/abaddon-the-despoiler.json")
    if {x["id"] for x in red_source["reviews"]}!=EXPECTED_RED or any(x["analysis"] is not None for x in red_source["reviews"]):
        raise ValueError("Expected four *unanswered* source prompts changed; authored evidence must be reconsidered")
    red=(ROOT/J_RED).read_text(encoding="utf-8")
    mana=(ROOT/J_MANA).read_text(encoding="utf-8")
    for n in EXPECTED_RED:
        if ("\x60"+n+"\x60") not in red:
            raise ValueError("Missing authored red-team challenge "+n)
    if red.count("## 1. ")!=1 or red.count("## 2. ")!=1 or red.count("## 3. ")!=1 or red.count("## 4. ")!=1:
        raise ValueError("Candidate red-team review does not answer all four questions")
    if ("no new randomized" not in mana.lower() or "baseline-only" not in mana.lower()
        or "34 lands" not in mana or SHA_CHOSEN not in mana
        or "500-sample" not in mana or "No new" not in red):
        raise ValueError("Source baseline-only mana and authored red-team uncertainty not disclosed")
    waiver=fetch(WAIVER)
    prog=fetch(PROGRESS)
    if (waiver["accepted_substitute"]["technically_independent"] is not False or
        prog["formal_pass_c_owner_equivalent_completed"]!=62 or
        prog["genuinely_independent_third_model_reviews"]!=0):
        raise ValueError("Owner-waived Pass C provenance was silently recast as independent")
    judgment_path=f"{PASS_C_ROOT}/final_disposition.md"
    pass_c={"reviewer":"ChatGPT/OpenAI GPT-6",
        "judgment_receipt_path":judgment_path,
        "judgment_receipt_sha256":"sha256:"+digest(judgment_path),
        "conflicts_resolved":True,"review_class":"FORMAL_PASS_C_OWNER_EQUIVALENT",
        "technically_independent":False,
        "waiver_receipt_path":WAIVER,
        "waiver_receipt_sha256":"sha256:"+digest(WAIVER),
        "progress_receipt_path":PROGRESS,
        "progress_receipt_sha256":"sha256:"+digest(PROGRESS),
        "stage_a_seal_path":f"{PASS_C_ROOT}/seal.json",
        "stage_a_seal_sha256":"sha256:"+digest(f"{PASS_C_ROOT}/seal.json")}
    validate_pass_c(pass_c,DECK)
    inventory=fetch(P0)
    if (len(inventory["replay_cases"])!=95 or inventory["required_open"] or
         inventory["authority"]["formal_m6_certified"]):
        raise ValueError("Incomplete or promoted limited Phase B case inventory")
    paths={x["test_file"] for x in inventory["replay_cases"]}
    if any(not (ROOT/p).is_file() for p in paths):
        raise ValueError("Absent actual named P0 test source")
    decision=fetch(M7)
    if (decision["final_candidate"]["sha256"]!=SHA_CHOSEN or
        decision["owner_authority"]["exact_candidate_owner_approved"] is not False or
        decision["owner_authority"]["canonical_deck_changed"] is not False):
        raise ValueError("Unauthorized selected-candidate mutation or owner approval")
    refs=[CANON,SELECTED,M7,M5,P0,J_RED,J_MANA,WAIVER,PROGRESS,
          "data/grixis/bracket_red_team/abaddon-the-despoiler.json",
          "data/grixis/commander_mana/abaddon-the-despoiler.json",
          "data/grixis/mana_resilience/abaddon-the-despoiler.json",
          "data/grixis/m6/sealed/reconciliation_manifest.json",
          "data/grixis/m6/certification_preflight/abaddon_97_card_effect_coverage_20261022.json"]
    refs+=sorted(paths)
    manifest={
      "schema_version":1,"kind":"ABADDON_M6_J_INPUTS_PARTIAL_ACTUAL_EVIDENCE",
      "deck_id":DECK,"baseline_source_sha256":SHA_BASE,
      "selected_candidate_sha256":SHA_CHOSEN,
      "original_land_count":34,"selected_land_count":34,
      "land_multiset_unchanged":True,
      "author_reviewed_red_team_prompt_ids":sorted(EXPECTED_RED),
      "pass_c_provenance":{"review_class":pass_c["review_class"],"reviewer":pass_c["reviewer"],
                           "technically_independent":False,
                           "waiver_and_deck_stage_a_validated":True},
      "mechanical_case_inventory":{"registered":95,"known_open":0,
          "scope":"Bounded fixture cases only; exact-head execution must be separately evidenced by GitHub Actions."},
      "mana_study":{"source":"BASELINE_ONLY_500_SAMPLES","candidate_simulated":False,
                    "selected_100_land_delta":"UNCHANGED_34_SOURCE_LANDS"},
      "source_hashes":{"sha256:"+p:digest(p) for p in sorted(set(refs))},
      "readiness":{"m6_5":"COMPLETE_OWNER_WAIVED_NONINDEPENDENT",
         "authored_red_team_questions":"FOUR_OF_FOUR_ANSWERED_NOT_INDEPENDENT",
         "selected_candidate_land_delta":"VERIFIED",
         "phase_b_complete":False,
         "m6_6":"PARTIAL","m6_7":"PARTIAL",
         "m6_i":"BLOCKED","m6_j":"BLOCKED",
         "m7_owner_approved":False,"canonical_modified":False}}
    if manifest["readiness"]["phase_b_complete"] or manifest["readiness"]["m7_owner_approved"]:
        raise ValueError("No authority to certify partial evidence")
    return manifest

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--out",type=Path,required=True)
    args=parser.parse_args()
    report_data=report()
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report_data,indent=2,sort_keys=True)+"\n")
    print("ABADDON_M6_J_CANDIDATE_INPUTS_PARTIAL_PASS",json.dumps({
        "sources_bound":len(report_data["source_hashes"]),
        "authored_red_team_responses":len(EXPECTED_RED),
        "selected_lands":report_data["selected_land_count"],
        "mechanical_cases":95,
        "pass_c_owner_waiver_integrity":"PASS",
        "m6_j_certified":False,"path":str(args.out),
        "sha256":hashlib.sha256(args.out.read_bytes()).hexdigest()},sort_keys=True))

if __name__=="__main__":
    main()
