#!/usr/bin/env python3
"""Execute the *actual named* Abaddon P0 cases on an exact GitHub Actions head.

A PASS here means ONLY the registered cases passed. No presently registered mandatory
P0 cases remain unexecuted after 44 checks, but M6.6 and I/J are NOT certified.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "data/grixis/m6/phase_b_plans/abaddon_p0_case_inventory_20261022.json"
SNAPSHOT = ROOT / "data/grixis/m7/authority_snapshots/Abaddon_the_Despoiler_Approved_2026-10-13.txt"
PLAN = ROOT / "data/grixis/m6/phase_b_plans/abaddon_p0_theft_keeper_diff_20261022.json"


class P0GateError(RuntimeError):
    pass


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def registry_check(doc: dict):
    items, remaining = doc["replay_cases"], doc["required_open"]
    ids = [x["id"] for x in items + remaining]
    if len(ids) != len(set(ids)):
        raise P0GateError("Duplicate P0 case IDs")
    if len(items) != 88 or len(remaining) != 0:
        raise P0GateError("Current inventory changed without a plan update")
    if not all(row["status"] == "REQUIRED_UNEXECUTED" for row in remaining):
        raise P0GateError("Unrun P0 case was marked completed")
    if doc["completion_claim"] or doc["authority"]["formal_m6_certified"]:
        raise P0GateError("Cannot promote incomplete M6 gate")
    if doc["authority"]["m6_6"] != "PARTIAL":
        raise P0GateError("M6.6 must remain PARTIAL until open case execution")
    if doc["test_boundedness"]["randomized_trajectories_this_action"] != 0:
        raise P0GateError("No randomized gameplay authorized by this registry")
    if sha256(SNAPSHOT) != doc["source_sha256"]:
        raise P0GateError("Approved source SHA drift")
    prereg = json.loads(PLAN.read_text(encoding="utf-8"))
    expected_new = {x["id"] for x in prereg["registered_cases"]}
    expected_suffixes = {"p0_betrayal_source_paid_hit",
                         "p0_betrayal_no_creatures", "p0_betrayal_countered",
                         "p0_betrayal_drannith", "p0_betrayal_rule_of_law",
                         "p0_keeper_mv1_and_mv0"}
    if expected_new != expected_suffixes:
        raise P0GateError("Preregistered new case IDs diverged")
    new = [x for x in items if x["expected_execution"] == "NEW_THIS_PR_CI"]
    if {x["test_method"].split(".", 1)[-1] for x in new} != {
            "test_" + n for n in expected_suffixes}:
        raise P0GateError("New P0 registry not identical to precommit plan")
    if len(new) != 6 or len(items) - len(new) != 82:
        raise P0GateError("Replayed/new case count drift")
    # P0-021 is a parent topic with eight individually executed, preregistered
    # tests; no file-name substring count is accepted in lieu of real execution.
    call_plan_path = ROOT / "data/grixis/m6/phase_b_plans/abaddon_p0_call_forth_20261022.json"
    call_plan = json.loads(call_plan_path.read_text(encoding="utf-8"))
    new_call = [x for x in items if x["expected_execution"] == "NEW_CALL_FORTH_THIS_PR_CI"]
    expected_call = {"test_" + row["id"] for row in call_plan["cases"]}
    if len(new_call) != 8 or {r["test_method"].split(".", 1)[-1] for r in new_call} != expected_call:
        raise P0GateError("P0-021 test set differs from preregistration")
    if remaining:
        raise P0GateError("Three newly discovered P0 obligations must remain explicitly open")
    coverage_path = ROOT / "data/grixis/m6/certification_preflight/abaddon_97_card_effect_coverage_20261022.json"
    coverage = json.loads(coverage_path.read_text(encoding="utf-8"))
    if {x["id"] for x in coverage["identified_unresolved"]} != {x["id"] for x in remaining}:
        raise P0GateError("P0 coverage source and registered gaps diverged")
    parent = doc.get("newly_covered_parent_topics", [])
    if len(parent) != 8 or parent[0]["id"] != "P0-021" or set(parent[0]["case_ids"]) != {r["id"] for r in new_call}:
        raise P0GateError("P0-021 grouping/parent receipt incomplete")
    if call_plan["candidate_sha256"] != "1fabe1251a7868838365144bf0cb1ee903d394ed90ac146b2dd9cdd45683b7dd":
        raise P0GateError("P0-021 preferred whole-deck candidate drift")
    suspend_plan_path = ROOT / "data/grixis/m6/phase_b_plans/abaddon_p0_betrayal_suspend_20261022.json"
    suspend_plan = json.loads(suspend_plan_path.read_text(encoding="utf-8"))
    new_suspend = [x for x in items if x["expected_execution"] == "NEW_BETRAYAL_SUSPEND_THIS_PR_CI"]
    if len(new_suspend) != 7 or {x["test_method"].split(".", 1)[-1] for x in new_suspend} != {
            "test_" + x["id"] for x in suspend_plan["registered_cases"]}:
        raise P0GateError("P0-022 test set diverges from preregistered suspend plan")
    if parent[1]["id"] != "P0-022" or set(parent[1]["case_ids"]) != {r["id"] for r in new_suspend}:
        raise P0GateError("P0-022 grouping/parent receipt incomplete")
    if suspend_plan["variant_sha256"] != "3ceddb947b0e7aff9cae489a0c60704214a2e580b97bfb1aaee5bb254c71fdaa":
        raise P0GateError("P0-022 alternate 100-card source changed")
    breach_plan_path = ROOT / "data/grixis/m6/phase_b_plans/abaddon_p0_breach_led_freeze_20261022.json"
    breach_plan = json.loads(breach_plan_path.read_text(encoding="utf-8"))
    new_breach = [x for x in items if x["expected_execution"] == "NEW_BREACH_LED_FREEZE_THIS_PR_CI"]
    if len(new_breach) != 9 or {x["test_method"].split(".", 1)[-1] for x in new_breach} != {
            "test_" + x["id"] for x in breach_plan["registered_cases"]}:
        raise P0GateError("P0-023 methods differ from preregistered test cases")
    if parent[2]["id"] != "P0-023" or set(parent[2]["case_ids"]) != {r["id"] for r in new_breach}:
        raise P0GateError("P0-023 grouped parent receipt incomplete")
    if breach_plan["candidate_sha256"] != "1fabe1251a7868838365144bf0cb1ee903d394ed90ac146b2dd9cdd45683b7dd":
        raise P0GateError("P0-023 source physical 100-list drift")
    if breach_plan["cost_budget"]["registered_tests"] != 9 or breach_plan["cost_budget"]["randomized_gameplay_trajectories"] != 0:
        raise P0GateError("P0-023 preregistration cost budget drift")
    wild_plan_path = ROOT / "data/grixis/m6/phase_b_plans/abaddon_p0_wild_magic_20261022.json"
    wild_plan = json.loads(wild_plan_path.read_text(encoding="utf-8"))
    new_wild = [x for x in items if x["expected_execution"] == "NEW_WILD_MAGIC_THIS_PR_CI"]
    if len(new_wild) != 8 or {x["test_method"].split(".",1)[-1] for x in new_wild} != {
            "test_" + x["id"] for x in wild_plan["registered_cases"]}:
        raise P0GateError("P0-024 actual methods diverged from preregistration")
    if parent[3]["id"] != "P0-024" or set(parent[3]["case_ids"]) != {x["id"] for x in new_wild}:
        raise P0GateError("P0-024 registered group incomplete")
    if wild_plan["candidate_sha256"] != "1fabe1251a7868838365144bf0cb1ee903d394ed90ac146b2dd9cdd45683b7dd":
        raise P0GateError("P0-024 100-card source hash drift")
    if (wild_plan["cost_budget"]["new_registered_methods"]!=8 or
            wild_plan["cost_budget"]["randomized_game_trials"]!=0):
        raise P0GateError("P0-024 stop rule/cost budget changed")
    if {x["id"] for x in coverage.get("newly_registered_tested_P0",[])} != {"P0-024","P0-025","P0-026","P0-027","P0-028"}:
        raise P0GateError("97-name matrix does not disclose registered P0-024")
    nalf_plan_path = ROOT / "data/grixis/m6/phase_b_plans/abaddon_p0_nalfeshnee_20261022.json"
    nalf_plan = json.loads(nalf_plan_path.read_text(encoding="utf-8"))
    nalf_cases = [x for x in items if x["expected_execution"] == "NEW_NALFESHNEE_THIS_PR_CI"]
    if len(nalf_cases) != 9 or {x["test_method"].split(".",1)[-1] for x in nalf_cases} != {
            "test_" + x["id"] for x in nalf_plan["registered_cases"]}:
        raise P0GateError("P0-025 test methods do not match preregistration")
    if parent[4]["id"] != "P0-025" or set(parent[4]["case_ids"]) != {x["id"] for x in nalf_cases}:
        raise P0GateError("P0-025 parent case IDs missing or fabricated")
    if nalf_plan["candidate_sha256"] != "1fabe1251a7868838365144bf0cb1ee903d394ed90ac146b2dd9cdd45683b7dd":
        raise P0GateError("P0-025 chosen whole-deck physical source hash drift")
    if nalf_plan["budget"]["new_methods"] != 9 or nalf_plan["budget"]["random_trials"] != 0:
        raise P0GateError("P0-025 preregistered test budget mismatch")
    arch_plan_path = ROOT / "data/grixis/m6/phase_b_plans/abaddon_p0_archaeologist_20261022.json"
    arch_plan = json.loads(arch_plan_path.read_text(encoding="utf-8"))
    arch_cases = [x for x in items if x["expected_execution"] == "NEW_ARCHAEOLOGIST_THIS_PR_CI"]
    if len(arch_cases) != 10 or {x["test_method"].split(".",1)[-1] for x in arch_cases} != {
            "test_" + x["id"] for x in arch_plan["registered_cases"]}:
        raise P0GateError("P0-026 actual test methods differ from preregistered names")
    if parent[5]["id"] != "P0-026" or set(parent[5]["case_ids"]) != {x["id"] for x in arch_cases}:
        raise P0GateError("P0-026 grouped source-bound receipt incomplete")
    if arch_plan["physical_candidate_sha256"] != "1fabe1251a7868838365144bf0cb1ee903d394ed90ac146b2dd9cdd45683b7dd":
        raise P0GateError("P0-026 candidate source SHA drift")
    if (arch_plan["cost_budget"]["new_registered_methods"] != 10 or
            arch_plan["cost_budget"]["randomized_trials"] != 0):
        raise P0GateError("P0-026 preregistration scope/cost drift")
    prosper_plan_path = ROOT / "data/grixis/m6/phase_b_plans/abaddon_p0_prosper_20261022.json"
    prosper_plan = json.loads(prosper_plan_path.read_text(encoding="utf-8"))
    prosper_cases = [x for x in items if x["expected_execution"] == "NEW_PROSPER_THIS_PR_CI"]
    if len(prosper_cases) != 10 or {x["test_method"].split(".",1)[-1] for x in prosper_cases} != {
            "test_" + x["id"] for x in prosper_plan["registered_cases"]}:
        raise P0GateError("P0-027 actual Prosper methods diverged from preregistration")
    if parent[6]["id"] != "P0-027" or set(parent[6]["case_ids"]) != {x["id"] for x in prosper_cases}:
        raise P0GateError("P0-027 grouped source-bound case receipt incomplete")
    if prosper_plan["candidate_sha256"] != "1fabe1251a7868838365144bf0cb1ee903d394ed90ac146b2dd9cdd45683b7dd":
        raise P0GateError("P0-027 whole-deck physical source hash drift")
    if prosper_plan["budget"]["registered_methods"] != 10 or prosper_plan["budget"]["random_game_trials"] != 0:
        raise P0GateError("P0-027 preregistered workload changed")
    if len(coverage.get("identified_unresolved",[])) != 0:
        raise P0GateError("Mismatched full 97-name existing P0 audit scope")
    kiln_plan_path = ROOT / "data/grixis/m6/phase_b_plans/abaddon_p0_storm_kiln_20261022.json"
    kiln_plan = json.loads(kiln_plan_path.read_text(encoding="utf-8"))
    kiln_cases = [x for x in items if x["expected_execution"] == "NEW_STORM_KILN_THIS_PR_CI"]
    if len(kiln_cases) != 7 or {x["test_method"].split(".",1)[-1] for x in kiln_cases} != {
            "test_" + x["id"] for x in kiln_plan["registered_cases"]}:
        raise P0GateError("P0-028 exact methods do not match earlier preregistration")
    if parent[7]["id"] != "P0-028" or set(parent[7]["case_ids"]) != {x["id"] for x in kiln_cases}:
        raise P0GateError("P0-028 source-bound grouped case receipt incomplete")
    if kiln_plan["candidate_sha256"] != "1fabe1251a7868838365144bf0cb1ee903d394ed90ac146b2dd9cdd45683b7dd":
        raise P0GateError("P0-028 exact full-100 source SHA diverged")
    if kiln_plan["budget"]["new_case_methods"] != 7 or kiln_plan["budget"]["randomized_game_trials"] != 0:
        raise P0GateError("P0-028 preregistered budget/stop rule changed")
    for row in items:
        path = Path(row["test_file"])
        if (path.is_absolute() or ".." in path.parts or
                len(path.parts) != 2 or path.parts[0] != "tests" or
                not path.name.startswith("test_") or path.suffix != ".py" or
                not (ROOT / path).is_file()):
            raise P0GateError("Invalid source test path: " + row["test_file"])
        if "." not in row["test_method"]:
            raise P0GateError("Missing fully qualified test class.method")
    return prereg


def run_all(doc: dict):
    prereg = registry_check(doc)
    out = []
    files = {}
    for row in doc["replay_cases"]:
        test_path = ROOT / row["test_file"]
        module_key = row["test_file"]
        if module_key not in files:
            module_name = "p0_abaddon_actual_" + test_path.stem
            spec = importlib.util.spec_from_file_location(module_name, test_path)
            if not spec or not spec.loader:
                raise P0GateError("Cannot import test module: " + module_key)
            module = importlib.util.module_from_spec(spec)
            sys.modules[module_name] = module
            spec.loader.exec_module(module)
            files[module_key] = (module, sha256(test_path))
        module, digest = files[module_key]
        try:
            suite = unittest.TestLoader().loadTestsFromName(row["test_method"], module=module)
        except Exception as exc:
            raise P0GateError("P0 case not loadable: " + row["id"]) from exc
        result = unittest.TestResult()
        suite.run(result)
        status = "PASS" if result.wasSuccessful() and result.testsRun == 1 else "FAIL"
        out.append({
            "id": row["id"], "mechanic": row["mechanic"],
            "test_file": row["test_file"], "test_method": row["test_method"],
            "test_sha256": digest, "status": status, "executed": result.testsRun,
            "error_messages": [str(e)[:2500] for _t, e in result.errors + result.failures],
        })
    return {
        "schema_version": 1,
        "stage": "ABADDON_P0_SELECTED_REPLAY_ONLY_NOT_FULL_M6_CERTIFICATION",
        "executed_utc": datetime.now(timezone.utc).isoformat(),
        "preregistered_plan_sha256": sha256(PLAN),
        "registry_sha256": sha256(REGISTRY),
        "canonical_pinned_raw_sha256": sha256(SNAPSHOT),
        "replayed_case_count": len(out),
        "passed": sum(x["status"] == "PASS" for x in out),
        "failed": sum(x["status"] != "PASS" for x in out),
        "case_receipts": out,
        "open_required_p0_cases": doc["required_open"],
        "open_required_count": len(doc["required_open"]),
        "exact_head_ci_env": {"github_sha": __import__("os").environ.get("GITHUB_SHA"),
                              "github_head_ref": __import__("os").environ.get("GITHUB_HEAD_REF")},
        "governance": doc["authority"],
        "effect_coverage_is_all_99_cards": False,
        "M6_6_certified": False,
        "owner_approved": False,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    doc = json.loads(REGISTRY.read_text(encoding="utf-8"))
    report = run_all(doc)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n",
                        encoding="utf-8")
    print("ABADDON_P0_REPLAY", json.dumps({
        "executed": report["replayed_case_count"], "passed": report["passed"],
        "failed": report["failed"], "open_required": report["open_required_count"],
        "source_sha": report["canonical_pinned_raw_sha256"],
        "receipt": str(args.out), "m6_6_certified": False}, sort_keys=True))
    if report["failed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
