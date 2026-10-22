#!/usr/bin/env python3
"""Strict semantic and source integrity check for selected-result Abaddon M6 I.

The generic JSON schema validator does not prove its conditional PASS logic in
all standalone paths. This checker explicitly enforces each requirement,
including actual stored candidate source binding and no owner authority.
"""
from __future__ import annotations

from collections import Counter
import argparse
import hashlib
import json
from pathlib import Path

from scripts import grixis_authority as ga
from scripts.grixis_m7_decision_gate import parse_list

ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "data/grixis/m6/ij/certificates/abaddon-the-despoiler.json"
BUNDLE = ROOT / "data/grixis/m6/bundles/abaddon-the-despoiler.json"
SNAP = ROOT / "data/grixis/m6/oracle_snapshots/Abaddon_the_Despoiler_Scryfall_20261022.json"
TRACK = ROOT / "data/grixis/milestone_m6_m7_subtracker.json"
SOURCE = ROOT / "data/grixis/m7/candidate_lists/Abaddon_the_Despoiler.txt"
P0 = ROOT / "data/grixis/m6/phase_b_plans/abaddon_p0_case_inventory_20261022.json"
AUDIT = ROOT / "data/grixis/m6/certification_preflight/abaddon_residual_70_decision_relevance_20261022.json"
EXPECTED_RAW = "1fabe1251a7868838365144bf0cb1ee903d394ed90ac146b2dd9cdd45683b7dd"
EXPECTED_LH = "lh1:4bb15eb5acc051871e7d818890f71705eb74f1281e933e73b0e77ff770be1efc"
CAVEAT = "Local optimum over the explicitly tested candidate pool only; not a mathematical or global proof of optimality."


class ICompletedEvidenceError(ValueError):
    pass


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def check(doc=None):
    cert = load(CERT) if doc is None else doc
    errs = ga.validate_file(cert, "zero_improvement_certificate.schema.json")
    if errs:
        raise ICompletedEvidenceError("I schema error: " + "; ".join(errs[:4]))
    mandatory = {
        "schema_version": 1, "deck_id": "Abaddon_the_Despoiler",
        "slug": "abaddon-the-despoiler", "list_hash": EXPECTED_LH,
        "reconciliation_complete": True, "improving_substitution_found": False,
        "local_optimum_for_tested_pool": True, "certificate_status": "pass",
        "scope_caveat": CAVEAT,
    }
    for key, value in mandatory.items():
        if cert.get(key) != value:
            raise ICompletedEvidenceError("I unsupported PASS field: " + key)
    if (cert.get("unresolved_requires_human_judgment") != [] or cert.get("blockers") != []
        or cert.get("phase_b", {}).get("all_required_tests_pass") is not True
        or cert.get("authority", {}).get("can_decide") is not False
        or cert.get("authority", {}).get("can_approve_or_lock") is not False):
        raise ICompletedEvidenceError("I unresolved obligation, effect-test gap, or owner-right inflation")
    pool = cert["candidate_pool"]
    expected_pool = "data/grixis/m7/research_challengers/Abaddon_the_Despoiler_portfolio_v2.json"
    if pool["source_ref"] != expected_pool or pool["tested_pool_size"] != 5:
        raise ICompletedEvidenceError("I tested-pool scope drift")
    f = ROOT / expected_pool
    if pool["source_sha256"] != "sha256:" + hashlib.sha256(f.read_bytes()).hexdigest():
        raise ICompletedEvidenceError("I tested-pool contents drift")
    if cert["optimizer_pass_ref"] != "data/grixis/m6/sealed/reconciliation_manifest.json":
        raise ICompletedEvidenceError("I sealed A/B optimizer reference changed")
    needed = {str(P0.relative_to(ROOT)),
              "tests/test_m6_abaddon_residual_p1.py",
              "tests/test_m6_abaddon_remaining_p1.py"}
    if not needed <= set(cert["phase_b"]["test_refs"]):
        raise ICompletedEvidenceError("I actual P0/P1 sources missing")
    if not any("github.com/" in p and "/actions/runs/" in p
               for p in cert["phase_b"]["test_refs"]):
        raise ICompletedEvidenceError("I exact-head Actions provenance missing")
    p0 = load(P0)
    audit = load(AUDIT)
    if (len(p0["replay_cases"]) != 104 or p0["required_open"]
        or audit["residual_p1_executed_cases"] != 14
        or len(audit["rows"]) != 70
        or not all("PENDING" not in x["disposition"] for x in audit["rows"])):
        raise ICompletedEvidenceError("Actual finite mechanical obligations not closed")
    if hashlib.sha256(SOURCE.read_bytes()).hexdigest() != EXPECTED_RAW:
        raise ICompletedEvidenceError("Chosen 100-card raw source drift")
    cards, commanders, companions = parse_list(SOURCE)
    snap = load(SNAP)
    oracle = snap["oracle_snapshot"]
    if len(cards) != 100 or commanders != ["Abaddon the Despoiler"] or companions:
        raise ICompletedEvidenceError("Chosen full Commander source invalid")
    counts = Counter(("commander" if i == 0 else "main", oracle[n]["oracle_id"])
                     for i, n in enumerate(cards))
    payload = "".join(f"{z}|{oid}|{n}\n" for (z, oid), n in sorted(counts.items()))
    if "lh1:" + hashlib.sha256(payload.encode()).hexdigest() != cert["list_hash"]:
        raise ICompletedEvidenceError("Chosen result logical identity drift")
    J = load(BUNDLE)
    if J["result_hash"] != cert["list_hash"] or not J["phase_b"]["complete"]:
        raise ICompletedEvidenceError("I/J selected result disagreement")
    t = load(TRACK)
    for gate_id in ("M6.6", "M6.7"):
        gate = next(x for x in t["m6"]["gates"] if x["id"] == gate_id)
        scoped = gate.get("per_deck_completion", {}).get("Abaddon_the_Despoiler")
        if (gate["status"] != "PARTIAL"
            or gate["completed"] != len(gate.get("per_deck_completion", {}))
            or gate["completed"] < 1
            or not scoped
            or scoped.get("status") != "COMPLETE_DECISION_SCOPED_ONLY"
            or scoped.get("owner_m7_approved") is not False):
            raise ICompletedEvidenceError("Missing Abaddon mechanical/judgment evidence or false owner promotion")
    if (t["m6"]["formal_m6_certified_decks"] != 0
        or t["m7"]["formal_m7_review_decisions"] != 0):
        raise ICompletedEvidenceError("A tested-pool certificate is not an owner approval")
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", required=True)
    parser.parse_args()
    check()
    print("ABADDON_SELECTED_TESTED_POOL_I_PASS_BOUND_TO_SOURCE_NO_APPROVAL")


if __name__ == "__main__":
    main()
