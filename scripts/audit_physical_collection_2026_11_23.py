#!/usr/bin/env python3
"""Audit owner-confirmed 2026-11-23 physical inventory and active six decks.

The owner's corrected CSV is authoritative. Incoming Mono-Red proxy copies
are deck placeholders, not physical inventory. This is a copy-allocation
audit, not a Commander/Pauper rules or Oracle certification.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "data" / "physical_collection"
SNAP = BASE / "2026-11-23"
STATUS = BASE / "current_status.json"
POOL = BASE / "current_available.csv"
MASTER = SNAP / "Every_Card_we_own_IRL_corrected.csv"
MAPPING = {
    "Xander_EDH_IRL.csv": ("Cory_s_Lord_Xander_IRL_EDH.csv", 101, "Lord Xander, the Collector"),
    "Dihada_EDH_IRL.csv": ("Stefanie_Dihada_EDH_IRL.csv", 100, "Dihada, Binder of Wills"),
    "Korvold_Jund_EDH_IRL.csv": ("Stefanie_s_IRL_Jund_EDH.csv", 100, "Korvold, Fae-Cursed King"),
    "Locutus_Orzhov_Borg_EDH_IRL.csv": ("Cory_s_IRL_Orzhov_Borg_EDH.csv", 100, "Locutus, the One Who Speaks"),
    "MonoBlack_Pauper_IRL.csv": ("Mono_Black_Devotion_Control.csv", 60, None),
    "MonoRed_Pauper_IRL.csv": ("Mono_Red_Madness.csv", 60, None),
}
INCOMING = Counter({"Fireblast": 2, "Grab the Prize": 4,
                    "Kessig Flamebreather": 1, "Lava Dart": 2,
                    "Voldaren Epicure": 4})


def read_csv(path: Path) -> Counter[str]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != ["Quantity", "Name"]:
            raise ValueError(f"Invalid header: {path}")
        result = Counter()
        for row in reader:
            name, raw_quantity = row["Name"], row["Quantity"]
            if (not name or name.strip() != name or name in result
                    or not raw_quantity or not raw_quantity.isdecimal()
                    or int(raw_quantity) < 1):
                raise ValueError(f"Invalid quantity/name in {path}: {row}")
            result[name] = int(raw_quantity)
        return result


def available_csv(available: Counter[str], owned: Counter[str]) -> bytes:
    # Preserve source inventory order rather than shifting legacy card sorting.
    output = io.StringIO(newline="")
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow(["Quantity", "Name"])
    for name in owned:
        if available[name] > 0:
            writer.writerow([available[name], name])
    return output.getvalue().encode("utf-8")


def verify(write: bool = False) -> dict:
    manifest = json.loads((SNAP / "manifest.json").read_text(encoding="utf-8"))
    status = json.loads(STATUS.read_text(encoding="utf-8"))
    assert manifest["as_of_date"] == status["as_of_date"] == "2026-11-23"
    assert set(manifest["file_sha256"]) == {"Every_Card_we_own_IRL_corrected.csv"} | {
        source for source, _, _ in MAPPING.values()}
    for filename, expected in manifest["file_sha256"].items():
        actual = hashlib.sha256((SNAP / filename).read_bytes()).hexdigest()
        assert actual == expected, f"Owner-supplied source changed: {filename}"
    owned = read_csv(MASTER)
    assert sum(owned.values()) == 1395 and len(owned) == 793
    assert status["source_master_inventory"] == "data/physical_collection/2026-11-23/Every_Card_we_own_IRL_corrected.csv"
    assert set(status["built_decks"]) == set(MAPPING)
    assert set(status["active_built_decklists"]) == set(MAPPING)

    slots = Counter()
    red = None
    for current, (source, expected_size, commander) in MAPPING.items():
        expected_path = f"data/physical_collection/current_decks/{current}"
        assert status["active_built_decklists"][current] == expected_path
        deck = read_csv(SNAP / source)
        assert (BASE / "current_decks" / current).read_bytes() == (SNAP / source).read_bytes(), current
        assert sum(deck.values()) == expected_size, current
        if commander:
            assert deck[commander] == 1, f"Missing commander: {commander}"
        if current == "Xander_EDH_IRL.csv":
            assert deck["Lutri, the Spellchaser"] == 1
            assert status["xander_main_deck_cards_including_commander"] == 100
            assert status["xander_companion_counted_outside_main_deck"] is True
        if current == "MonoRed_Pauper_IRL.csv":
            red = deck
        slots.update(deck)
    assert red is not None
    outstanding = slots - owned
    assert outstanding == INCOMING, f"Unexpected inventory shortfall: {outstanding}"
    assert all(red[name] >= qty for name, qty in outstanding.items())
    assert sum(slots.values()) == 521
    assert sum(outstanding.values()) == 13
    available = owned - slots
    assert (sum(available.values()), len(available)) == (887, 537)
    assert status["reserved_cards"] == 508
    assert status["physical_deck_cards_reserved"] == 508
    assert status["proxy_cards_pending"] == 13
    assert status["proxies_by_name"] == dict(INCOMING)
    assert status["available_cards"] == 887
    assert status["available_distinct_names"] == 537
    assert status["current_available_pool"] == "data/physical_collection/current_available.csv"
    assert manifest["deck_counts"] == {name: count for name, (_, count, _) in MAPPING.items()}
    expected_csv = available_csv(available, owned)
    if write:
        POOL.write_bytes(expected_csv)
    else:
        assert POOL.read_bytes() == expected_csv, "Stale available-card CSV"
    result = {"verified": True, "date": "2026-11-23", "owned": 1395,
              "distinct_owned": 793, "decks": 6, "deck_slots": 521,
              "physical_reserved": 508, "incoming_proxies": 13,
              "available": 887, "available_names": 537}
    print(json.dumps(result, sort_keys=True))
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", action="store_true")
    group.add_argument("--write", action="store_true")
    args = parser.parse_args()
    verify(write=args.write)
