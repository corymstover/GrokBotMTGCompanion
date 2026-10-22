#!/usr/bin/env python3
"""Abaddon M6 pre-certification: verify ACTUAL CI Oracle + 44 P0 receipt bytes.

This refuses to certify M6, local optimality, J, M7, or modify the canonical
deck. It binds owner-waived Pass C and the sealed A/B references against the
committed sources, and emits explicit, actionable I/J blockers.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path

from scripts.grixis_m7_decision_gate import parse_list
from scripts.grixis_m6_bundle_check import (
    OWNER_EQUIVALENT, OWNER_PROGRESS, OWNER_WAIVER,
    validate_pass_c, content_hash
)

ROOT=Path(__file__).resolve().parents[1]
PINNED="2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf"
SNAPSHOT="data/grixis/m7/authority_snapshots/Abaddon_the_Despoiler_Approved_2026-10-13.txt"
INVENTORY="data/grixis/m6/phase_b_plans/abaddon_p0_case_inventory_20261022.json"
DECISION="data/grixis/m7/research_challengers/Abaddon_the_Despoiler_portfolio_v3_decisive.json"
CONFLICT="data/grixis/m6/certification_preflight/Abaddon_the_Despoiler_M6_6_7_reconciliation_20261022.md"
SEALS="data/grixis/m6/sealed/reconciliation_manifest.json"
PASS_C_DIR="data/grixis/m6/owner_pass_c_substitute/Abaddon_the_Despoiler"
SOURCE_MIRROR="exports/grixis-archidekt/source-baseline/abaddon-the-despoiler.txt"
BUNDLE="data/grixis/m6/bundles/abaddon-the-despoiler.json"
COVERAGE="data/grixis/m6/certification_preflight/abaddon_97_card_effect_coverage_20261022.json"
KNOWN_P0_GAPS={"P0-024","P0-025","P0-026","P0-027"}
GATES=["M6.6","M6.7","M6.8","M6.9","M6.10"]


class PreflightFailure(ValueError):
    pass


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def verify_prerequisites():
    if sha(ROOT/SNAPSHOT)!=PINNED:
        raise PreflightFailure("Approved raw exact bytes drifted")
    old,commanders,companions=parse_list(ROOT/SOURCE_MIRROR)
    if len(old)!=100 or len(set(old))!=94 or commanders!=["Abaddon the Despoiler"] or companions:
        raise PreflightFailure("Source deck structural authority drift")
    manifest=load(ROOT/DECISION)
    chosen=manifest["proposed"]
    alternative=manifest["competing"]
    if (manifest["owner_approved"] or manifest["m6_certified"]
        or manifest["canonical"]["approved_sha256"]!=PINNED
        or chosen["adds"]!=["Grinning Ignus","Chaos Warp"]
        or chosen["cuts"]!=["Rakdos, Lord of Riots","Inevitable Betrayal"]):
        raise PreflightFailure("Premature approval or changed commander-first selection")
    checked={}
    for key, variant in [("preferred",chosen),("competing",alternative)]:
        path=ROOT/variant["file"]
        if sha(path)!=variant["physical_sha256"]:
            raise PreflightFailure(key+" physical candidate byte hash mismatch")
        cards,cmd,comp=parse_list(path)
        if (len(cards)!=100 or len(set(cards))!=94 or cmd!=commanders or comp
            or Counter(cards)-Counter(old)!=Counter(variant["adds"])
            or Counter(old)-Counter(cards)!=Counter(variant["cuts"])):
            raise PreflightFailure(key+" source/changes/count reconciliation failed")
        checked[key]=dict(path=variant["file"],physical_sha256=sha(path),
                          actual_100=True,actual_94_unique=True)
    old=load(ROOT/SEALS)
    matches=[x for x in old["passes"] if x["deck_id"]=="Abaddon_the_Despoiler"]
    if len(matches)!=1:
        raise PreflightFailure("No unique Abaddon sealed A/B binding")
    sealed=matches[0]
    logical=sealed["list_hash"]
    if manifest["canonical"].get("cards")!=100:
        raise PreflightFailure("Canonical physical count drift")
    for side in ("a","b"):
        path=f"data/grixis/m6/sealed/{side.upper()}/abaddon-the-despoiler.json"
        j=load(ROOT/path)
        if content_hash(path)!=sealed[side+"_sha256"] or j["pass"]["list_hash"]!=logical:
            raise PreflightFailure("Sealed optimizer "+side+" corrupted")
    if not (old["pass_a_commit"] and old["pass_b_commit"]):
        raise PreflightFailure("Original sealed optimizer commit reference missing")

    waiver={ "reviewer":"ChatGPT/OpenAI GPT-6",
        "review_class":OWNER_EQUIVALENT,"technically_independent":False,
        "judgment_receipt_path":f"{PASS_C_DIR}/final_disposition.md",
        "waiver_receipt_path":OWNER_WAIVER,
        "progress_receipt_path":OWNER_PROGRESS,
        "stage_a_seal_path":f"{PASS_C_DIR}/seal.json"}
    for key in ("judgment_receipt","waiver_receipt","progress_receipt","stage_a_seal"):
        waiver[key+"_sha256"]=content_hash(waiver[key+"_path"])
    try:
        validate_pass_c(waiver,"Abaddon_the_Despoiler")
    except Exception as exc:
        raise PreflightFailure("Owner-equivalent Pass C provenance invalid") from exc
    if not (ROOT/CONFLICT).is_file():
        raise PreflightFailure("Actual M6.7 reconciliation is absent")
    material=(ROOT/CONFLICT).read_text(encoding="utf-8")
    for text in ("Aggravated Assault","Grinning Ignus","Inevitable Betrayal",
                 "Keeper of Secrets","NO_EVIDENCE_JUSTIFIED_SWAP_AT_M6",
                 "zero-improvement","not an M6.6"):
        if text.lower() not in material.lower():
            raise PreflightFailure("Missing actual M6.7 conflict substance: "+text)
    return {
      "approved_source_sha256":PINNED,"canonical_logical_hash":logical,
      "canonical_physical_100":True,
      "sealed_a_b_git_commits":[old["pass_a_commit"],old["pass_b_commit"]],
      "sealed_a_b_manifest_sha256":sha(ROOT/SEALS),
      "owner_waiver_sha256":sha(ROOT/OWNER_WAIVER),
      "pass_c_provenance":"OWNER_EQUIVALENT_GPT6_NONINDEPENDENT_M6_5_ONLY",
      "pass_c_evidence_sha256":sha(ROOT/f"{PASS_C_DIR}/final_disposition.md"),
      "strategic_disposition_sha256":sha(ROOT/DECISION),
      "M6_7_authored_reconciliation_sha256":sha(ROOT/CONFLICT),
      "staged_full_list_variants":checked,
    }


def validate_runtime(oracle, p0):
    inventory=load(ROOT/INVENTORY)
    if (len(inventory["replay_cases"])!=44
        or {x["id"] for x in inventory["required_open"]}!=KNOWN_P0_GAPS
        or inventory["completion_claim"]):
        raise PreflightFailure("Current 44-P0 known-case inventory not closed")
    if inventory["authority"]["formal_m6_certified"] or inventory["authority"]["m6_6"]!="PARTIAL":
        raise PreflightFailure("P0 inventory claims premature milestone certification")

    expected={row["id"]:row for row in inventory["replay_cases"]}
    receipts=p0.get("case_receipts")
    if (p0.get("replayed_case_count")!=44 or p0.get("passed")!=44
        or p0.get("failed")!=0 or p0.get("open_required_count")!=4
        or {x["id"] for x in p0.get("open_required_p0_cases",[])}!=KNOWN_P0_GAPS
        or p0.get("M6_6_certified") is not False or p0.get("owner_approved") is not False
        or p0.get("canonical_pinned_raw_sha256")!=PINNED or
        p0.get("registry_sha256")!=sha(ROOT/INVENTORY) or
        not isinstance(receipts,list) or len(receipts)!=44):
        raise PreflightFailure("Actual CI P0 report is missing/inconsistent")
    ids={row.get("id") for row in receipts}
    if ids!=set(expected):
        raise PreflightFailure("P0 individual case IDs missing/repeated")
    for row in receipts:
        source=expected[row["id"]]
        if (row.get("status")!="PASS" or row.get("executed")!=1
            or row.get("test_file")!=source["test_file"]
            or row.get("test_method")!=source["test_method"]
            or row.get("test_sha256")!=sha(ROOT/source["test_file"])
            or row.get("error_messages")):
            raise PreflightFailure("Not truly executed, stale, or failed P0: "+row["id"])

    expected_variants={"baseline","engine_only","engine_answer_keeper",
                       "engine_answer_betrayal","combat_answer_keeper"}
    listed=oracle.get("physical_lists",{})
    data=oracle.get("oracle_snapshot",{})
    if (oracle.get("card_identity_count")!=97
        or len(data)!=97 or set(listed)!=expected_variants
        or oracle.get("approved_canonical_raw_sha256")!=PINNED
        or oracle.get("owner_m7_approval") is not False
        or oracle.get("formal_m6_certificate") is not False
        or oracle.get("canonical_authority_mode")!="SHA_PINNED_CANONICAL_BYTES_NOT_LIVE_CROSS_REPO_READ"):
        raise PreflightFailure("Live source Oracle receipt incomplete or falsely approved")
    combined=set()
    for tag,row in listed.items():
        path=ROOT/row["source"]
        if not path.is_file() or sha(path)!=row["physical_sha256"] or row["card_count"]!=100 or not row["checked"]:
            raise PreflightFailure("Current Oracle list physical source mismatch: "+tag)
        names,cmd,comp=parse_list(path)
        if len(names)!=100 or len(set(names))!=row["distinct_names"] or cmd!=["Abaddon the Despoiler"] or comp:
            raise PreflightFailure("Oracle source physical list card mismatch: "+tag)
        if row["oracle_rows_covered"]!=len(set(names)):
            raise PreflightFailure("Incomplete Oracle name coverage: "+tag)
        combined.update(names)
    if combined!=set(data):
        raise PreflightFailure("Oracle 97-name coverage not exactly the full five lists")
    coverage=load(ROOT/COVERAGE)
    rows=coverage["names"]
    if (coverage.get("expected_unique_names")!=97
        or len(rows)!=97 or len({x["name"] for x in rows})!=97
        or {x["name"] for x in rows}!=combined
        or len([x for x in rows if x["baseline"]])!=94
        or {x["id"] for x in coverage["identified_unresolved"]}!=KNOWN_P0_GAPS):
        raise PreflightFailure("Every live Oracle card must have exactly one coverage row and four declared new P0")
    baseline=set(parse_list(ROOT/SOURCE_MIRROR)[0])
    for row in rows:
        if row["baseline"]!=(row["name"] in baseline):
            raise PreflightFailure("Coverage baseline card membership falsely classified: "+row["name"])
        expected={"P0-024":"Wild-Magic Sorcerer","P0-025":"Nalfeshnee",
                  "P0-026":"Passionate Archaeologist","P0-027":"Prosper, Tome-Bound"}
        if row["name"] in expected.values():
            if row.get("new_gap_id")!=next(k for k,v in expected.items() if v==row["name"]) or row["coverage_class"]!="IDENTIFIED_MATERIAL_P0_GAP":
                raise PreflightFailure("False mandatory card gap classification")
    for name,c in data.items():
        oracle_text=c.get("oracle_text","")
        if (c.get("commander_legality")!="legal" or not set(c.get("color_identity",[])) <= {"B","R","U"}
           or not c.get("oracle_id") or not oracle_text
           or hashlib.sha256(oracle_text.encode("utf-8")).hexdigest()!=c.get("oracle_text_sha256")):
            raise PreflightFailure("Oracle current legality/identity/text hash violation: "+name)

    return {"phase_b_actual_named_P0_methods":44,"phase_b_pass":44,
        "current_identified_open_P0":4,
        "current_oracle_unique_names":97,"full_physical_lists":5,
        "current_oracle_checked_at_utc":oracle["checked_at_utc"],
        "oracle_input_sha256":None, "p0_input_sha256":None,
        "rules_effect_coverage":"BOUNDED_SELECTED_CONDITIONAL_INTERACTIONS",
        "all_99_game_effects_modeled":False,
        "no_new_randomized_trajectories":True}


def build(oracle_path,p0_path):
    static=verify_prerequisites()
    oracle=load(oracle_path);p0=load(p0_path)
    dynamic=validate_runtime(oracle,p0)
    dynamic["oracle_input_sha256"]=sha(oracle_path)
    dynamic["p0_input_sha256"]=sha(p0_path)
    return {"schema_version":1,"stage":"ABADDON_M6_EVIDENCE_PREFLIGHT_NOT_CERTIFICATION",
        "checked_utc":datetime.now(timezone.utc).isoformat(),
        "github_exact_head":os.environ.get("GITHUB_HEAD_REF") or os.environ.get("GITHUB_SHA"),
        "source_integrity":static,"runtime_verification":dynamic,
        "quality_gates":{
           "M6_5":"PASS_OWNER_WAIVER_NONINDEPENDENT",
           "M6_6":"44_HISTORICAL_P0_PASS_FOUR_NEW_COMMANDER_CORE_P0_PENDING_FORMAL_COMPLETENESS_PENDING",
           "M6_7":"AUTHORED_CONFLICT_RECONCILED_FORMAL_JUDGMENT_GATE_PENDING",
           "M6_8_I":"BLOCKED_PLAUSIBLE_POSITIVE_SWAP_POOL_NOT_ZERO_IMPROVEMENT",
           "M6_9_J":"BLOCKED_NO_COMPLETE_EFFECT_AWARE_FINAL_BUNDLE",
           "M6_10":"BLOCKED_NO_OWNER_MILESTONE_ACCEPTANCE",
           "M7":"NO_NEW_OWNER_APPROVAL",
        },
        "remaining_material_dependencies":[
           "M6.6: four new unexecuted critical exile-trigger mechanic groups (Wild-Magic, Nalfeshnee, Passionate Archaeologist, Prosper); previous 44 cases remain passing.",
           "M6.7 material contradiction with historical Pass C Assault proposal reconciled narratively, but comparative strength remains qualitative, not measured net-game superiority.",
           "M6 I cannot certify original baseline local optimum while a plausible two-swap challenger remains and exact tested pool is not declared closed for local optimum.",
           "M6 J complete schema requires durable rules/Oracle/legality snapshots, fully reconciled decision-grade Phase B effect coverage, mana/red-team stress and exact result logical hashes. Actions evidence artifacts expire.",
           "Only user can approve the M7 exact proposed list and milestone; historic 62 approved lists cannot be changed here.",
        ],
        "authority":{"canonical_changed":False,"m6_certified":False,
          "I_certificate_pass":False,"J_bundle_complete":False,
          "m7_owner_approval":False,"technically_independent_pass_C":False}}
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--oracle",type=Path,required=True)
    ap.add_argument("--p0",type=Path,required=True)
    ap.add_argument("--out",type=Path,required=True)
    args=ap.parse_args()
    report=build(args.oracle,args.p0)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    print("ABADDON_M6_PREFLIGHT_PASS",json.dumps({
        "P0_verified":report["runtime_verification"]["phase_b_pass"],
        "P0_open_new":report["runtime_verification"]["current_identified_open_P0"],
        "oracles":report["runtime_verification"]["current_oracle_unique_names"],
        "complete_decks":report["runtime_verification"]["full_physical_lists"],
        "M6_certified":False,"M6_I_pass":False,"M6_J_complete":False,
        "report_sha256":sha(args.out),
        "report_path":str(args.out)},sort_keys=True))

if __name__=="__main__":
    main()
