#!/usr/bin/env python3
"""Deterministic coverage audit for existing targeted pull-request CI checks.

It verifies *configured and exercised* checks for K124, not whether GitHub's
branch protection settings require all jobs. That setting is not proven by
workflow YAML and must remain a separately reported administrative gap.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / ".github/workflows"
OUT = ROOT / "data/release/ci_domain_coverage_2026-11-01.json"

# One exact workflow and at least one executable CI command per domain.
# Independent replay on a clean clone is part of the pull-request workflow.
DOMAINS = {
    "card_counts_and_color_identity": ("phase6-lore-pilots.yml", [
        "run: python3 scripts/audit_lore_pilot.py",
        "test_lore_pilot_builder.py"]),
    "official_story_source_integrity": ("phase3-multiverse-claim-graph.yml", [
        "python3 scripts/story_claim_pipeline.py check",
        "test_story_claim_pipeline.py"]),
    "cited_graph_relationships": ("multiverse-integrity-post-grok.yml", [
        "python3 scripts/build_multiverse_graph.py --check",
        "test_graph_integrity_post_grok.py"]),
    "published_rules_and_commander_eligibility": ("phase7-companion-ask.yml", [
        "python3 scripts/commander_rules.py audit-eligibility --check",
        "test_commander_rules.py"]),
    "question_answer_regressions": ("phase7-companion-ask.yml", [
        "test_mv_ask.py",
        "test_rules_interactions.py"]),
    "historical_set_and_printing_data": ("phase1b-set-atlas-validation.yml", [
        "test_set_printing_atlas.py"]),
    "frozen_pilot_decklist_legality": ("phase6-lore-pilots.yml", [
        "run: python3 scripts/audit_lore_pilot.py",
        "test_pilot3_ugins_allies.py"]),
    "original_grixis_mechanics_regressions": ("chatgpt-branch-validation.yml", [
        "test_mech_attack_semantics.py",
        "test_mech_router_semantics.py",
        "scripts/grixis_mechanics.py --check"]),
    "whole_project_progress_and_release": ("phase8-release-readiness.yml", [
        "python3 scripts/audit_full_checklist.py --check",
        "python3 scripts/certification_dry_run.py --check"]),
}


def build(workflows: Path = WORKFLOWS):
    result = {}
    for domain, (filename, commands) in sorted(DOMAINS.items()):
        path = workflows / filename
        content = path.read_text(encoding="utf-8")
        if "on:\n  pull_request:" not in content:
            raise ValueError(f"{domain}: workflow does not trigger on pull requests")
        if "continue-on-error: true" in content:
            raise ValueError(f"{domain}: workflow contains a failure-bypass")
        if any(command not in content for command in commands):
            raise ValueError(f"{domain}: an expected executable step/test is missing from {filename}")
        for command in commands:
            if command.startswith("test_"):
                if not (ROOT / "tests" / command).exists():
                    raise ValueError(f"{domain}: referenced test file does not exist: {command}")
            elif command.startswith("run: python3 scripts/"):
                script = command.split("scripts/", 1)[1].split()[0]
                if not (ROOT / "scripts" / script).exists():
                    raise ValueError(f"{domain}: referenced audit script does not exist: {script}")
        result[domain] = {"workflow": ".github/workflows/" + filename,
                          "required_step_fragments": commands,
                          "workflow_sha256": hashlib.sha256(content.encode("utf-8")).hexdigest(),
                          "pull_request_trigger": True,
                          "no_continue_on_error": True}
    return {"schema": "bounded-targeted-ci-coverage/v1", "as_of": "2026-11-01",
            "status": "TARGETED_CI_WORKFLOWS_PRESENT_AND_ASSERTED",
            "coverage_domains": result, "count": len(result),
            "administrative_limitation": "This tests committed workflow configuration only. It does NOT prove GitHub branch protection requires status checks or that any unobserved future run is green.",
            "external_green_ancestor": "PR #972 candidate 13/13 and merge 9/9 (observed separately, not reauthenticated by this local tool)",
            "scope": "Keeps targeted CI in versioned repository code; future additions must update this map and regenerate."}


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--check", action="store_true")
    a = p.parse_args(argv)
    payload = json.dumps(build(), indent=2, ensure_ascii=False) + "\n"
    if a.check:
        if OUT.read_text(encoding="utf-8") != payload:
            raise ValueError("targeted CI domain coverage report stale")
    else:
        OUT.write_text(payload, encoding="utf-8")
    print("PASS nine targeted CI domains; branch-protection enforcement NOT asserted")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
