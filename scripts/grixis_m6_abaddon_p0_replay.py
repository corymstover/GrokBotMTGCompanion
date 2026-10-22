#!/usr/bin/env python3
"""Execute the *actual named* Abaddon P0 cases on an exact GitHub Actions head.

A PASS here means ONLY the registered cases passed. Three declared mandatory
P0 cases remain unexecuted; M6.6 and I/J cannot be certified.
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
    if len(items) != 35 or len(remaining) != 1:
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
    if len(new) != 6 or len(items) - len(new) != 29:
        raise P0GateError("Replayed/new case count drift")
    # P0-021 is a parent topic with eight individually executed, preregistered
    # tests; no file-name substring count is accepted in lieu of real execution.
    call_plan_path = ROOT / "data/grixis/m6/phase_b_plans/abaddon_p0_call_forth_20261022.json"
    call_plan = json.loads(call_plan_path.read_text(encoding="utf-8"))
    new_call = [x for x in items if x["expected_execution"] == "NEW_CALL_FORTH_THIS_PR_CI"]
    expected_call = {"test_" + row["id"] for row in call_plan["cases"]}
    if len(new_call) != 8 or {r["test_method"].split(".", 1)[-1] for r in new_call} != expected_call:
        raise P0GateError("P0-021 test set differs from preregistration")
    if {x["id"] for x in remaining} != {"P0-023"}:
        raise P0GateError("Known open P0 obligations missing")
    parent = doc.get("newly_covered_parent_topics", [])
    if len(parent) != 2 or parent[0]["id"] != "P0-021" or set(parent[0]["case_ids"]) != {r["id"] for r in new_call}:
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
