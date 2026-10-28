#!/usr/bin/env python3
"""Exact Deck #60 research candidate: current 2026-10-27 Scryfall snapshot audit.

This verifies one consent-authorized 100 only, not two unqueried alternatives.
The commander is NOT yet officially Commander legal. Project exception alone
is not a substitute for a future-release or M7 approval gate.
"""
from __future__ import annotations

import collections
import csv
import hashlib
import json
from pathlib import Path

from verify import CAND, MAIN_SHA, COMMANDER, INDEX, deck

ROOT = Path(__file__).resolve().parents[4]
SNAP = ROOT / "data/grixis/m7/oracle_snapshots/Tresserhorn_Returned_M7_Rev1_Scryfall_20261027.json"
SNAP_SHA = "d8b6d52a4611e58facf14e03fbd25c4b7a321b85bf5b56cd177133b851e0b48b"


def main():
    names, raw_sha = deck(CAND)
    assert raw_sha == MAIN_SHA
    snap_bytes = SNAP.read_bytes()
    assert hashlib.sha256(snap_bytes).hexdigest() == SNAP_SHA
    snapshot = json.loads(snap_bytes)
    assert snapshot["source"] == "https://api.scryfall.com/cards/collection"
    assert snapshot["source_100_hashes"][CAND.name] == raw_sha
    assert snapshot["unique_identifiers"] == len(set(names)) == 94
    assert snapshot["retrieved_utc"].startswith("2026-10-28T01:40:54")
    cards = {c["name"]: c for c in snapshot["cards"]}
    assert len(cards) == len(snapshot["cards"]) == 94
    assert set(cards) == set(names)
    with INDEX.open(encoding="utf-8", newline="") as input_file:
        frozen = {row["name"]: row for row in csv.DictReader(input_file)}
    for name, qty in collections.Counter(names).items():
        item = cards[name]
        assert item["oracle_id"] and len(item["oracle_id"]) >= 32, name
        assert item["oracle_id"] == frozen[name]["oracle_id"], (
            "frozen/current card identity drift", name)
        assert set(item["color_identity"]) <= {"U", "B", "R"}, (name, item["color_identity"])
        assert item.get("oracle_text") or any(f.get("oracle_text") for f in item["card_faces"]), name
        assert (item["commander_legality"] == "not_legal") == (name == COMMANDER), (
            name, item["commander_legality"])
        if " // " in name:
            assert len(item["card_faces"]) >= 2, name
            assert " // " in item["name"], name
        assert qty <= 1 or name in {"Island", "Mountain", "Swamp"}, (name, qty)

    lord = cards[COMMANDER]
    assert lord["mana_cost"] == "{2}{U}{B}{R}"
    assert "Trample, indestructible" in lord["oracle_text"]
    assert "sacrifice three creatures" in lord["oracle_text"]
    assert "Whenever you sacrifice a creature, draw a card." in lord["oracle_text"]

    sengir = cards["Sengir Autocrat"]["oracle_text"]
    assert "create three 0/1 black Serf" in sengir
    assert "exile all Serf tokens" in sengir
    assert "Whenever a nontoken creature enters" in cards["Genesis Chamber"]["oracle_text"]
    assert "power 7 or greater" in cards["Not of This World"]["oracle_text"]
    assert "gets -X/-X" in cards["The Meathook Massacre"]["oracle_text"]
    assert "gain haste" in cards["Song of Totentanz"]["oracle_text"]
    agadeem = cards["Agadeem's Awakening // Agadeem, the Undercrypt"]
    assert len(agadeem["card_faces"]) == 2 and "Land" in agadeem["card_faces"][1]["type_line"]

    print("Deck #60 exact candidate + live Scryfall snapshot SHA: PASS")
    print("Live query cards:", len(cards), "| physical:", len(names))
    print("All 93 noncommander identities legal and UBR: PASS")
    print("All 94 current Oracle IDs match frozen October 15 identities: PASS")
    print("Commander official Commander legality: NOT LEGAL until expected 2026-11-13")
    print("No unqueried alternative or full I/J/M7 gate asserted")


if __name__ == "__main__":
    main()
