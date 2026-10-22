#!/usr/bin/env python3
"""Current Scryfall Oracle audit for Abaddon's *new* six-swap research portfolio.

Reuses the established bounded transport and full-list assessment, but does
not reuse the withdrawn two-swap M6 I/J identity or claim M7 owner readiness.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import json
from pathlib import Path

from scripts.grixis_m7_decision_gate import parse_list
from scripts.grixis_m7_abaddon_live_oracle import (
    CANONICAL_SNAPSHOT, ROOT, SCRYFALL, OracleGateError, assess,
    collected_cards, source_reconcile, sha256_bytes,
)

MANIFEST = ROOT / "data/grixis/m7/research_challengers/Abaddon_the_Despoiler_rev2_six_swap_manifest.json"


def validate_portfolio(manifest: dict):
    if manifest["stage"] != "M7_RESEARCH_COMPARATIVE_NOT_OWNER_READY":
        raise OracleGateError("Revised portfolio stage changed")
    if manifest["owner_approved"] or manifest["m6_certified"] or manifest["oracle_complete"]:
        raise OracleGateError("Cannot launder research portfolio into an accepted certificate")
    source_cards, approved_sha = source_reconcile(manifest, CANONICAL_SNAPSHOT.read_bytes())
    result = {"baseline": source_cards}
    variants = manifest["comparisons"]
    if len(variants) != 3 or {v["id"] for v in variants} != {
        "six_swap_selected_research", "five_swap_clone_focused_alternative",
        "five_swap_combat_focused_alternative",
    }:
        raise OracleGateError("Three physical comparison variants required")
    for v in variants:
        rel = v["path"]
        if not rel.startswith("data/grixis/m7/research_challengers/") or not rel.endswith(".txt"):
            raise OracleGateError("Untrusted variant location")
        path = ROOT / rel
        if sha256_bytes(path.read_bytes()) != v["sha256"]:
            raise OracleGateError("Revised physical SHA mismatch: " + v["id"])
        cards, cmd, companions = parse_list(path)
        if cmd != ["Abaddon the Despoiler"] or companions:
            raise OracleGateError("Unexpected commander/companion")
        if Counter(cards) - Counter(source_cards) != Counter(v["adds"]):
            raise OracleGateError("Revised add delta drift: " + v["id"])
        if Counter(source_cards) - Counter(cards) != Counter(v["cuts"]):
            raise OracleGateError("Revised cut delta drift: " + v["id"])
        result[v["id"]] = cards
    return result, approved_sha


def audit(*, fetch=None, sleeper=None):
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    variants, baseline_sha = validate_portfolio(manifest)
    all_names = {n for cards in variants.values() for n in cards}
    options = {}
    if fetch is not None:
        options["fetch"] = fetch
    if sleeper is not None:
        options["sleeper"] = sleeper
    evidence = assess(collected_cards(all_names, **options), variants)
    for name, expected in manifest["newly_checked_scryfall_oracle"].items():
        actual = evidence[name]
        for key in ("oracle_id", "mana_value", "mana_cost", "color_identity",
                    "commander_legality", "oracle_text"):
            if actual[key] != expected[key]:
                raise OracleGateError("Changed candidate Oracle property: " + name + "." + key)
    receipts = {"baseline": {
        "source": manifest["baseline_source_path"], "card_count": len(variants["baseline"]),
        "physical_sha256": baseline_sha,
    }}
    for v in manifest["comparisons"]:
        receipts[v["id"]] = {
            "source": v["path"], "card_count": len(variants[v["id"]]),
            "physical_sha256": v["sha256"], "oracle_rows_covered": len(set(variants[v["id"]])),
        }
    return {
        "stage": "LIVE_ORACLE_REVISED_ABADDON_RESEARCH_NOT_M6_M7_CERTIFICATION",
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "scryfall_endpoint": SCRYFALL,
        "source_approved_sha256": baseline_sha,
        "card_identity_count": len(evidence),
        "physical_lists": receipts,
        "oracle_snapshot": evidence,
        "owner_m7_approval": False,
        "formal_m6_certificate": False,
        "old_two_swap_ij_not_rebound": True,
        "limitations": [
            "All named identities checked live, but this is not executable proof of gameplay interactions.",
            "Canonical source read uses a SHA-pinned engineering snapshot; live canonical main verified separately via GitHub connector.",
            "This audit does not update two-swap M6 I/J source hashes, owner approval or canonical lists.",
        ],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    report = audit()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("ABADDON_REV2_LIVE_ORACLE_PASS", json.dumps({
        "timestamp": report["checked_at_utc"],
        "unique_cards": report["card_identity_count"],
        "physical_lists": len(report["physical_lists"]),
        "research_only": True,
        "owner_approval_inferred": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
