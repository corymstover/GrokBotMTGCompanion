#!/usr/bin/env python3
"""Emit a bounded current Abaddon Scryfall proof for durable M6 J source archival.

The GitHub Actions Oracle source file is already generated and fail-closed by
grixis_m7_abaddon_live_oracle. This command prints public card Oracle rows only,
with stable prefixes that a connected source auditor can preserve as JSON.
No GitHub token, account data, secrets or approval markers are emitted.
"""
from __future__ import annotations
from collections import Counter
import argparse
import hashlib
import json
from pathlib import Path

from scripts.grixis_m7_decision_gate import parse_list
from scripts.grixis_m7_abaddon_live_oracle import parse_approved_raw

ROOT = Path(__file__).resolve().parents[1]
CHOSEN = ROOT / "data/grixis/m7/candidate_lists/Abaddon_the_Despoiler.txt"
BASE = ROOT / "data/grixis/m7/authority_snapshots/Abaddon_the_Despoiler_Approved_2026-10-13.txt"
EXPECTED_CHOSEN = "1fabe1251a7868838365144bf0cb1ee903d394ed90ac146b2dd9cdd45683b7dd"
EXPECTED_BASE = "2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf"


def logical_hash(cards, oracle):
    if len(cards) != 100 or cards[0] != "Abaddon the Despoiler":
        raise ValueError("Incorrect 100-card source")
    entries = Counter(("commander" if i == 0 else "main", oracle[name]["oracle_id"])
                      for i, name in enumerate(cards))
    if sum(entries.values()) != 100:
        raise ValueError("Card census mismatch")
    value = "".join(f"{zone}|{oid}|{count}\n" for (zone, oid), count in sorted(entries.items()))
    return "lh1:" + hashlib.sha256(value.encode("utf-8")).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--oracle", type=Path, required=True)
    args = parser.parse_args()
    source = args.oracle.read_bytes()
    data = json.loads(source)
    oracle = data["oracle_snapshot"]
    if data["card_identity_count"] != 97 or len(oracle) != 97:
        raise ValueError("Source oracle count changed; fail closed")
    if data["approved_canonical_raw_sha256"] != EXPECTED_BASE:
        raise ValueError("Approved source SHA mismatch")
    if (hashlib.sha256(CHOSEN.read_bytes()).hexdigest() != EXPECTED_CHOSEN
        or hashlib.sha256(BASE.read_bytes()).hexdigest() != EXPECTED_BASE):
        raise ValueError("Pinned exact deck drift")
    chosen, commanders, companions = parse_list(CHOSEN)
    base, bc = parse_approved_raw(BASE.read_bytes())
    if commanders != ["Abaddon the Despoiler"] or bc != commanders or companions:
        raise ValueError("Commander or companion mismatch")
    if not set(chosen + base) <= set(oracle):
        raise ValueError("Physical names not all in current Oracle snapshot")
    digest = hashlib.sha256(source).hexdigest()
    header = {k: v for k, v in data.items() if k != "oracle_snapshot"}
    header["capture_raw_sha256"] = digest
    header["chosen_research_candidate_raw_sha256"] = EXPECTED_CHOSEN
    header["chosen_research_candidate_logical_hash"] = logical_hash(chosen, oracle)
    header["baseline_logical_hash"] = logical_hash(base, oracle)
    print("ABADDON_ORACLE_CAPTURE_START")
    print("ABADDON_ORACLE_HEADER_JSON:" + json.dumps(header, sort_keys=True, separators=(",", ":"), ensure_ascii=False))
    for name in sorted(oracle):
        print("ABADDON_ORACLE_ROW_JSON:" + json.dumps({"name": name, "card": oracle[name]},
                                                    sort_keys=True, separators=(",", ":"), ensure_ascii=False))
    print("ABADDON_ORACLE_CAPTURE_FINISH:" + str(len(oracle)))


if __name__ == "__main__":
    main()
