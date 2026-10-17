#!/usr/bin/env python3
"""M6 promotion/lock preflight for the Grixis Commander Encyclopedia.

This is deliberately authority-safe. It consumes accepted M5 evidence, inventories
M6 requirements, and builds a decision-preparation queue. It does not apply swaps,
edit canonical decklists, promote challengers, approve decks, or lock decks.

M6 PASS eventually requires, per deck:
  * independent commander-first + performance optimizer passes and reconciliation,
  * all required Phase-B tests passing,
  * a tested-pool zero-improvement/local-optimum certificate,
  * no unresolved requires_human_judgment items,
  * an artifact bundle with list hashes, tests, and receipts.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "data/grixis/registry.json"
M5_SUMMARY = ROOT / "data/grixis/birthday_m5/summary.json"
M5_CANDIDATES = ROOT / "data/grixis/birthday_m5/candidates"
M5_REGEN = ROOT / "data/grixis/birthday_m5/regen"
M5_EVIDENCE = ROOT / "data/grixis/birthday_m5/evidence"
OUT = ROOT / "data/grixis/m6"
PREFLIGHT = OUT / "preflight.json"
QUEUE = OUT / "decision_queue.json"
CERT_SCHEMA = ROOT / "data/grixis/schemas/zero_improvement_certificate.schema.json"
OPT_SCHEMA = ROOT / "data/grixis/schemas/optimizer_pass.schema.json"

AUTHORITY = {
    "can_decide": False,
    "can_apply_swap": False,
    "can_change_canonical_list": False,
    "can_approve_or_lock": False,
    "note": (
        "M6 preflight and queue are decision-preparation evidence only. "
        "Human approval remains required for any deck change, approval, or lock."
    ),
}


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return "sha256:" + h.hexdigest()


def require_milestones(registry: dict[str, Any]) -> None:
    milestones = registry["program"]["milestones"]
    for key in ("M2", "M4", "M5"):
        if milestones.get(key, {}).get("status") != "accepted":
            raise SystemExit(f"M6 blocked: {key} is not accepted")
    m5 = milestones["M5"]
    if m5.get("accepted_by") != "corymstover":
        raise SystemExit("M6 blocked: M5 lacks Cory acceptance authority")


def artifact_status(slug: str) -> tuple[dict[str, Any], list[str]]:
    expected = {
        "optimizer_pass": OUT / "optimizer" / f"{slug}.json",
        "phase_b": OUT / "phase_b" / f"{slug}.json",
        "judgment_review": OUT / "judgment" / f"{slug}.json",
        "artifact_bundle": OUT / "bundles" / f"{slug}.json",
        "zero_improvement_certificate": OUT / "certificates" / f"{slug}.json",
    }
    present = {name: path.exists() for name, path in expected.items()}
    blockers: list[str] = []
    if not present["optimizer_pass"]:
        blockers.append("independent_optimizer_pass_and_reconciliation_missing")
    if not present["phase_b"]:
        blockers.append("phase_b_test_bundle_missing")
    if not present["judgment_review"]:
        blockers.append("human_judgment_resolution_missing")
    if not present["artifact_bundle"]:
        blockers.append("receipt_bundle_missing")
    if not present["zero_improvement_certificate"]:
        blockers.append("zero_improvement_certificate_missing")
    return present, blockers


def build() -> None:
    registry = load(REGISTRY)
    require_milestones(registry)
    summary = load(M5_SUMMARY)

    decks = summary.get("decks", [])
    if len(decks) != 62:
        raise SystemExit(f"M6 requires 62 M5 decks; found {len(decks)}")
    slugs = [d.get("slug") for d in decks]
    if len(set(slugs)) != 62 or any(not s for s in slugs):
        raise SystemExit("M6 requires 62 unique non-empty deck slugs")

    missing_inputs: list[str] = []
    queue_rows: list[dict[str, Any]] = []
    preflight_rows: list[dict[str, Any]] = []

    for order, d in enumerate(decks, start=1):
        slug = d["slug"]
        candidate = M5_CANDIDATES / f"{slug}.json.gz"
        regen = M5_REGEN / f"{slug}.json.gz"
        evidence = M5_EVIDENCE / f"{slug}.json"
        for path in (candidate, regen, evidence):
            if not path.exists():
                missing_inputs.append(str(path.relative_to(ROOT)))

        candidate_sha = sha256_file(candidate) if candidate.exists() else None
        present, blockers = artifact_status(slug)
        input_complete = candidate.exists() and regen.exists() and evidence.exists()
        if not input_complete:
            blockers = ["accepted_m5_input_missing", *blockers]

        queue_rows.append(
            {
                "order": order,
                "slug": slug,
                "canonical_hash": d.get("canonical_hash"),
                "m5_counts": {
                    "candidate_universe": d.get("universe"),
                    "full_reviews": d.get("reviews"),
                    "swap_hypotheses": d.get("swaps"),
                    "tests": d.get("tests"),
                },
                "accepted_m5_inputs": {
                    "candidate_pool": str(candidate.relative_to(ROOT)),
                    "candidate_pool_sha256": candidate_sha,
                    "regen": str(regen.relative_to(ROOT)),
                    "evidence": str(evidence.relative_to(ROOT)),
                },
                "next_required_stage": (
                    "independent_optimizer_passes" if input_complete else "repair_m5_input_coverage"
                ),
                "authority": AUTHORITY,
            }
        )
        preflight_rows.append(
            {
                "slug": slug,
                "canonical_hash": d.get("canonical_hash"),
                "accepted_m5_input_complete": input_complete,
                "m6_artifacts_present": present,
                "blockers": blockers,
                "approval_ready": len(blockers) == 0,
            }
        )

    if missing_inputs:
        raise SystemExit("M6 input coverage failure: " + ", ".join(missing_inputs[:10]))

    milestones = registry["program"]["milestones"]
    m6 = milestones["M6"]
    if m6.get("status") not in {"not_started", "in_progress"}:
        raise SystemExit(f"refusing to reopen M6 from state {m6.get('status')}")
    m6["status"] = "in_progress"
    m6["pending_note"] = (
        "Cycle 76 M6 is in progress. Accepted Birthday M5 evidence is queued for independent "
        "commander-first/performance optimizer passes, reconciliation, Phase-B testing, "
        "human-judgment resolution, tested-pool zero-improvement certification, and receipt "
        "bundling. No swap, canonical list change, approval, or lock is authorized by this state."
    )
    dump(REGISTRY, registry)

    approval_ready = sum(1 for row in preflight_rows if row["approval_ready"])
    complete_inputs = sum(1 for row in preflight_rows if row["accepted_m5_input_complete"])
    counts = {
        "decks": len(preflight_rows),
        "accepted_m5_input_complete": complete_inputs,
        "optimizer_pass_present": sum(row["m6_artifacts_present"]["optimizer_pass"] for row in preflight_rows),
        "phase_b_present": sum(row["m6_artifacts_present"]["phase_b"] for row in preflight_rows),
        "judgment_review_present": sum(row["m6_artifacts_present"]["judgment_review"] for row in preflight_rows),
        "artifact_bundle_present": sum(row["m6_artifacts_present"]["artifact_bundle"] for row in preflight_rows),
        "zero_improvement_certificate_present": sum(
            row["m6_artifacts_present"]["zero_improvement_certificate"] for row in preflight_rows
        ),
        "approval_ready": approval_ready,
    }

    preflight = {
        "schema_version": 1,
        "cycle": 76,
        "stage": "M6_preflight",
        "input_authority": {
            "m5_status": milestones["M5"]["status"],
            "m5_accepted_by": milestones["M5"].get("accepted_by"),
            "birthday_snapshot": summary.get("birthday_authority_snapshot"),
            "summary_ref": "data/grixis/birthday_m5/summary.json",
        },
        "requirements": {
            "independent_optimizer_schema": "data/grixis/schemas/optimizer_pass.schema.json",
            "zero_improvement_schema": "data/grixis/schemas/zero_improvement_certificate.schema.json",
            "phase_b_all_required_tests_pass": True,
            "unresolved_requires_human_judgment_must_be_zero": True,
            "receipt_bundle_required": True,
            "scope": "tested_pool_local_optimum_not_global_proof",
        },
        "counts": counts,
        "decks": preflight_rows,
        "authority": AUTHORITY,
    }
    queue = {
        "schema_version": 1,
        "cycle": 76,
        "stage": "M6_decision_preparation_queue",
        "order_source": "data/grixis/birthday_m5/summary.json",
        "decks": queue_rows,
        "authority": AUTHORITY,
    }
    dump(PREFLIGHT, preflight)
    dump(QUEUE, queue)

    print(json.dumps(counts, sort_keys=True))


def check() -> None:
    registry = load(REGISTRY)
    require_milestones(registry)
    if registry["program"]["milestones"]["M6"].get("status") != "in_progress":
        raise SystemExit("M6 registry status is not in_progress")
    if not CERT_SCHEMA.exists() or not OPT_SCHEMA.exists():
        raise SystemExit("required M6 schema missing")
    json.loads(CERT_SCHEMA.read_text(encoding="utf-8"))
    json.loads(OPT_SCHEMA.read_text(encoding="utf-8"))

    preflight = load(PREFLIGHT)
    queue = load(QUEUE)
    if preflight.get("counts", {}).get("decks") != 62 or len(preflight.get("decks", [])) != 62:
        raise SystemExit("M6 preflight does not cover exactly 62 decks")
    if len(queue.get("decks", [])) != 62:
        raise SystemExit("M6 decision queue does not cover exactly 62 decks")
    if preflight["counts"]["accepted_m5_input_complete"] != 62:
        raise SystemExit("M6 accepted-M5 input coverage is incomplete")
    if preflight["authority"] != AUTHORITY or queue["authority"] != AUTHORITY:
        raise SystemExit("M6 authority contract changed")
    if any(row.get("approval_ready") for row in preflight["decks"]):
        # Initial Cycle 76 is an architecture/preflight pass. Readiness must be earned by
        # later artifacts, never inferred just because M5 exists.
        raise SystemExit("unexpected approval-ready deck during initial M6 preflight")
    if any(row.get("authority") != AUTHORITY for row in queue["decks"]):
        raise SystemExit("decision-queue row escaped non-decisional authority")
    print("M6 preflight check: PASS (62/62 M5 inputs; 0 auto-promotions; authority preserved)")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--build", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if not args.build and not args.check:
        parser.error("choose --build and/or --check")
    if args.build:
        build()
    if args.check:
        check()


if __name__ == "__main__":
    main()
