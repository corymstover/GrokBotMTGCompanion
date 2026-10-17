#!/usr/bin/env python3
"""Fail-closed verifier for FINAL M6 J reproducibility bundles.

This script never creates receipts or certificates and never changes deck state.
Missing bundles are reported as pending; a missing bundle cannot be counted ready.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import grixis_authority as ga

BUNDLES = ROOT / "data/grixis/m6/bundles"
REGISTRY = ROOT / "data/grixis/registry.json"
SEALS = ROOT / "data/grixis/m6/sealed/reconciliation_manifest.json"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def safe_repo_file(name):
    path = Path(name)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError("unsafe artifact path")
    full = (ROOT / path).resolve()
    if not full.is_relative_to(ROOT.resolve()) or not full.is_file():
        raise ValueError("missing/outside-repo artifact: " + name)
    return full


def content_hash(name):
    return "sha256:" + hashlib.sha256(safe_repo_file(name).read_bytes()).hexdigest()


def bind(name, h):
    if content_hash(name) != h:
        raise ValueError("SHA-256 drift: " + name)


def validate_bundle(b, registry, seals):
    errors = ga.validate_file(b, "m6_reproducibility_bundle.schema.json")
    if errors:
        raise ValueError("invalid J bundle schema: " + "; ".join(errors[:8]))
    deck = registry["decks"].get(b["deck_id"])
    if not deck or b["slug"] != deck["slug"] or b["baseline_hash"] != deck["current_canonical_hash"]:
        raise ValueError("bundle baseline is not the preserved canonical hash")
    if b["snapshot"]["birthday_id"] != load(ROOT / "data/grixis/birthday_m5/summary.json")["birthday_authority_snapshot"]:
        raise ValueError("bundle Birthday snapshot mismatch")
    for item in b["inputs"]:
        bind(item["path"], item["sha256"])
    if b["sealed_passes"]["a_commit"] != seals["pass_a_commit"] or b["sealed_passes"]["b_commit"] != seals["pass_b_commit"]:
        raise ValueError("A/B committed hashes mismatch")
    bind("data/grixis/m6/sealed/reconciliation_manifest.json",
         b["sealed_passes"]["reconciliation_manifest_sha256"])
    slug = b["slug"]
    for side in ("a", "b"):
        name = b["sealed_passes"][side + "_output_ref"]
        expected = f"data/grixis/m6/sealed/{side.upper()}/{slug}.json"
        if name != expected:
            raise ValueError("sealed pass path mismatch")
        sealed = load(safe_repo_file(name))
        if sealed["pass"]["list_hash"] != b["baseline_hash"]:
            raise ValueError("sealed pass list hash mismatch")
    judgment = b["pass_c"]
    bind(judgment["judgment_receipt_path"], judgment["judgment_receipt_sha256"])
    reviewer = load(safe_repo_file(judgment["judgment_receipt_path"]))
    if reviewer.get("reviewer") != judgment["reviewer"] or reviewer.get("status") != "critical_review_complete":
        raise ValueError("Pass C reviewer receipt not complete/identified")
    if reviewer.get("can_approve_or_lock") is not False:
        raise ValueError("Pass C reviewer attempted approval")
    for t in b["phase_b"]["tests"]:
        bind(t["test_ref"], t["source_sha256"])
        if t["supports_improvement_claim"] and (t["effect_coverage"] != "fully_modeled" or t["verdict"] != "pass"):
            raise ValueError("unmodeled or failing test was promoted as improvement proof")
    for key in ("red_team", "mana_analysis"):
        bind(b[key]["report_path"], b[key]["sha256"])
    for key in ("oracle_ref", "rules_ref", "legality_ref"):
        safe_repo_file(b["snapshot"][key])
    if b["authority"]["can_approve_or_lock"] or b["authority"]["can_decide"]:
        raise ValueError("bundle illegally contains human approval")
    return True


def check():
    reg = load(REGISTRY)
    if len(reg["decks"]) != 62 or reg["program"]["milestones"]["M5"]["status"] != "accepted":
        raise ValueError("M5 authority incomplete")
    seals = load(SEALS)
    if seals["pass_c"]["complete"] is not False:
        raise ValueError("reconciliation manifest may not self-certify Pass C")
    expected = {x["slug"] for x in reg["decks"].values()}
    files = sorted(BUNDLES.glob("*.json")) if BUNDLES.exists() else []
    if len(files) > 62:
        raise ValueError("more than 62 bundles")
    seen = set()
    for p in files:
        bundle = load(p)
        if p.stem != bundle.get("slug") or p.stem not in expected or p.stem in seen:
            raise ValueError("unknown/duplicated final bundle: " + p.name)
        seen.add(p.stem)
        validate_bundle(bundle, reg, seals)
    print(f"M6 J final bundle verification: {len(seen)}/62 valid; {62-len(seen)} pending; no approval authority")
    return len(seen)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", required=True)
    ap.add_argument("--require-complete", action="store_true")
    args = ap.parse_args()
    count = check()
    if args.require_complete and count != 62:
        raise SystemExit("not enough complete bundles for M6 closure")
