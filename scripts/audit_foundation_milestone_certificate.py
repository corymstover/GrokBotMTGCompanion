#!/usr/bin/env python3
"""Verify the immutable source scope and form of the externally observed certificate.

The two external gates were checked against GitHub for the *referenced* PR
and merged main commit. An offline test cannot establish that a future commit
has green Actions or forge a current GitHub state from a saved JSON file.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "data/release/foundation_milestone_certificate_2026-11-01.json"


def check() -> dict:
    import sys
    sys.path.insert(0, str(ROOT / "scripts"))
    import audit_foundation_graph_scope as graph
    import audit_lookup_rules_scope as lookup
    import release_readiness as readiness

    d = json.loads(CERT.read_text(encoding="utf-8"))
    assert d["schema"] == "mtg-knowledge-foundation-certificate/v1"
    assert d["status"] == "CERTIFIED_BOUNDED_KNOWLEDGE_FOUNDATION_MILESTONE"
    assert d["scope"].startswith("Finite seven-criterion")
    assert d["verified_candidate_pull_request"] == 969
    assert d["verified_candidate_head"] != d["verified_merged_main_commit"]
    assert len(d["verified_candidate_and_merge_tree"]) == 40
    assert d["superseding_untested_commit_claimed"] is False

    expected_gates = {id for id, _, _ in readiness.CRITERIA}
    assert set(d["foundation_gates"]) == expected_gates
    statuses = {id: func()[0] for id, _, func in readiness.CRITERIA}
    for id, status in d["foundation_gates"].items():
        assert status == ("EXTERNALLY_VERIFIED_MET" if id in {"grixis_no_regression", "ci_and_coverage"}
                          else "SOURCE_BOUNDED_MET")
        assert statuses[id] == ("EXTERNAL" if status == "EXTERNALLY_VERIFIED_MET" else "MET")
    assert graph.build() == json.loads((ROOT / "data/release/foundation_graph_scope_review_2026-11-01.json").read_text())
    assert lookup.build() == json.loads((ROOT / "data/release/lookup_rules_scope_review_2026-11-01.json").read_text())
    assert set(d["source_review_sha256"]) == {
        "data/release/foundation_graph_scope_review_2026-11-01.json",
        "data/release/lookup_rules_scope_review_2026-11-01.json",
        "data/release/knowledge_foundation_acceptance.json",
        "data/release/batch_recount_2026-11-01.json",
        "data/scryfall_snapshots/oct30_to_nov01_2200_release_delta_2026-11-01.json"}
    for rel, expected in d["source_review_sha256"].items():
        assert hashlib.sha256((ROOT / rel).read_bytes()).hexdigest() == expected, rel

    ext = d["external_verification"]
    assert ext["protected_path_changes_against_pre_release_main"] == []
    live = readiness.tree_digest(readiness.PROTECTED)
    assert {path: row["sha256"] for path, row in live.items()} == ext["protected_path_sha256"]
    for key, head, n in (("candidate_pr_workflows", "verified_candidate_head", 14),
                         ("merged_main_workflows", "verified_merged_main_commit", 10)):
        runs = ext[key]
        assert runs["head"] == d[head]
        assert runs["expected_runs"] == n and runs["conclusion"] == "success"
        assert len(runs["run_ids"]) == len(set(runs["run_ids"])) == n
        assert all(isinstance(run, int) and run > 0 for run in runs["run_ids"])
    assert ext["candidate_pr_workflows"]["focused_grixis_mechanics_run_id"] in ext["candidate_pr_workflows"]["run_ids"]
    assert ext["candidate_pr_workflows"]["source_bound_phase8_release_readiness_run_id"] in ext["candidate_pr_workflows"]["run_ids"]
    assert len(d["not_certified_or_not_modified"]) >= 5
    return d


if __name__ == "__main__":
    d = check()
    print(f"PASS bounded foundation certificate evidence: {len(d['foundation_gates'])}/7 gates; "
          "external runs witnessed for the referenced SHA, not reauthenticated offline")
