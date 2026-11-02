#!/usr/bin/env python3
"""Fail-closed owner overlay for three exact historical Phase 6 pilot approvals.

The original specs/draft proposals intentionally remain at their historical
UNAPPROVED state. Only the later exact owner receipt changes approval status;
an engine build, new version or checksum mismatch cannot manufacture approval.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import audit_lore_pilot as pilot_audit

ROOT = Path(__file__).resolve().parents[1]
RECORD = ROOT / "data/lore_decks/owner_decisions/2026-11-02_cory_approved_phase6_pilots.json"
RECEIPT = ROOT / "data/lore_decks/owner_decisions/2026-11-02_cory_approved_phase6_pilots.md"
SOURCE_MAIN = "e620fd60a75abf8e1b966a89a518ff105d8aa7df"
SNAPSHOT = "snap-20261029-40848334824-1"
EXPECTED = {
    "K112": (1, "ugin_bolas_elder_dragon_duality", "Nicol Bolas, the Ravager // Nicol Bolas, the Arisen",
             "01d087aa2819b1ed3c7ac1f64843f76f36b551b72fda62d64218d19c40b0ab45", 823),
    "K113": (2, "original_primeval_dragons", "The Ur-Dragon",
             "6ef1af37c371891b7d3e60a08c2d1bcee1d1205f2c01e5c3093a220fb4414888", 832),
    "K114": (3, "ugins_allies_and_heroes", "Jace, Multiverse Architect",
             "05cd56bd3d58b153f35ad86f896d6c383f99bca9722e6124e627daad74641c6c", 844),
}


def check(record: Path = RECORD, receipt: Path = RECEIPT,
          deck_overrides: dict[str, Path] | None = None) -> dict:
    data = json.loads(record.read_text(encoding="utf-8"))
    if (data.get("schema") != "phase6-owner-exact-approval/v1"
            or data.get("owner") != "Cory" or data.get("decision_date") != "2026-11-02"
            or data.get("reviewed_main_commit") != SOURCE_MAIN
            or data.get("status") != "APPROVED_EXACT_HISTORICAL_REVISIONS"
            or data.get("original_draft_files_remain_unchanged") is not True
            or data.get("current_legality_or_bracket_certified") is not False
            or data.get("approval_applies_to_future_revisions") is not False
            or "Approve these three exact historical decklists" not in data.get("owner_decision", "")
            or "without changing cards" not in data.get("owner_decision", "")):
        raise ValueError("owner's bounded exact historical approval decision drifted")
    entries = data.get("pilots")
    if not isinstance(entries, list) or len(entries) != 3 or {p.get("checklist_id") for p in entries} != set(EXPECTED):
        raise ValueError("approval must cover exactly K112/K113/K114 once each")
    receipt_text = receipt.read_text(encoding="utf-8")
    if ("Approve these three exact historical decklists" not in receipt_text
            or "without changing cards" not in receipt_text
            or "Future card changes require" not in receipt_text):
        raise ValueError("exact owner approval receipt or revision boundary missing")
    for p in entries:
        key = p["checklist_id"]
        num, stem, commander, sha, pr = EXPECTED[key]
        path = f"data/lore_decks/drafts/{stem}_decklist.txt"
        if (p.get("number"), p.get("stem"), p.get("commander"), p.get("raw_sha256"),
                p.get("original_proposal_pr"), p.get("decklist"), p.get("cards"), p.get("snapshot")) != (
                    num, stem, commander, sha, pr, path, 100, SNAPSHOT):
            raise ValueError(f"{key}: owner's exact hash, card count or source identity drifted")
        raw = (deck_overrides or {}).get(key, ROOT / path).read_bytes()
        if hashlib.sha256(raw).hexdigest() != sha:
            raise ValueError(f"{key}: exact owner-approved decklist bytes changed")
        if sha not in receipt_text or f"K{112 + num - 1}" not in receipt_text:
            raise ValueError(f"{key}: receipt omits approved raw SHA")
        proposal = pilot_audit.audit(pilot_audit.SPECS / f"pilot{num}_{stem}.json")
        if (proposal["decklist_sha256"] != sha or proposal["total"] != 100
                or proposal["snapshot"] != SNAPSHOT or not proposal["status"].startswith("UNAPPROVED")):
            raise ValueError(f"{key}: immutable original proposal no longer independently audits")
    return {"status": data["status"], "owner": "Cory", "cards_per_pilot": 100,
            "checklist_ids": sorted(EXPECTED), "source_sha256": {k: EXPECTED[k][3] for k in sorted(EXPECTED)},
            "current_rules_or_power_certified": False}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="replay the exact approval audit")
    parser.parse_args()
    report = check()
    print("PASS exact owner-approved Phase 6 pilots:", ", ".join(report["checklist_ids"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
