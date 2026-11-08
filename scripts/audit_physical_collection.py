#!/usr/bin/env python3
"""Audit the immutable six-deck snapshot and owner-confirmed live allocations.

The original ZIP, master inventory and six historical decklists are never edited.
The current Xander deck is independently reproduced from confirmed physical
swaps; the active available pool subtracts it and unchanged Dihada from master.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
from collections import Counter
from pathlib import Path
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = ROOT / "data" / "physical_collection" / "2026-11-08"
CURRENT_STATUS = ROOT / "data" / "physical_collection" / "current_status.json"
CURRENT_POOL = ROOT / "data" / "physical_collection" / "current_available.csv"
CURRENT_XANDER = ROOT / "data" / "physical_collection" / "current_decks" / "Xander_EDH_IRL.csv"
XANDER_REBUILD = ROOT / "data" / "physical_collection" / "updates" / "2026-11-08_xander_rebuild.json"
MASTER = SNAPSHOT / "master_inventory.csv"
ARCHIVE = SNAPSHOT / "original_six_decks.zip"
DECKS = {
    "Xander_EDH_IRL.csv": ("Lord Xander, the Collector", "commander_with_companion", "keep_built"),
    "Dihada_EDH_IRL.csv": ("Dihada, Binder of Wills", "commander", "keep_built"),
    "Rith__Liberated_Primeval.csv": ("Rith, Liberated Primeval", "commander", "proposed_disassembly"),
    "Saruman__the_White_Hand_.csv": ("Saruman, the White Hand", "commander", "proposed_disassembly"),
    "Cory_Orzhov_Prerelease.csv": ("Orzhov Borg prerelease", "limited", "proposed_disassembly"),
    "Stefanie_Jund_Prerelease.csv": ("Jund prerelease", "limited", "proposed_disassembly"),
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def parse_counts(data: bytes, source: str) -> Counter[str]:
    text = data.decode("utf-8-sig")
    reader = csv.DictReader(io.StringIO(text, newline=""))
    if reader.fieldnames != ["Quantity", "Name"]:
        raise ValueError(f"{source}: expected Quantity,Name header")
    counts: Counter[str] = Counter()
    for line, row in enumerate(reader, 2):
        name = row.get("Name")
        quantity = row.get("Quantity")
        if not name or name != name.strip() or not quantity or not quantity.isdecimal():
            raise ValueError(f"{source}:{line}: invalid name or quantity")
        number = int(quantity)
        if number < 1 or name in counts:
            raise ValueError(f"{source}:{line}: zero quantity or duplicate name {name!r}")
        counts[name] = number
    return counts


def csv_bytes(counts: Counter[str]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.writer(stream, lineterminator="\n")
    writer.writerow(["Quantity", "Name"])
    for name in sorted(counts, key=lambda n: (n.casefold(), n)):
        writer.writerow([counts[name], name])
    return stream.getvalue().encode("utf-8")


def main(write: bool) -> None:
    master_bytes = MASTER.read_bytes()
    archive_bytes = ARCHIVE.read_bytes()
    master = parse_counts(master_bytes, str(MASTER))
    with ZipFile(ARCHIVE) as archive:
        if sorted(archive.namelist()) != sorted(DECKS):
            raise ValueError("The source ZIP does not contain exactly the six declared decks")
        deck_bytes = {name: archive.read(name) for name in DECKS}

    deck_counts: dict[str, Counter[str]] = {}
    deck_manifest: dict[str, dict] = {}
    reserved: Counter[str] = Counter()
    allocated: Counter[str] = Counter()
    for filename, (display_name, deck_format, status) in DECKS.items():
        original = deck_bytes[filename]
        actual = (SNAPSHOT / "decks" / filename).read_bytes()
        if original != actual:
            raise ValueError(f"Extracted deck does not match exact ZIP bytes: {filename}")
        counts = parse_counts(original, filename)
        deck_counts[filename] = counts
        allocated.update(counts)
        if status == "keep_built":
            reserved.update(counts)
        deck_manifest[filename] = {
            "display_name": display_name,
            "format": deck_format,
            "status": status,
            "cards": sum(counts.values()),
            "distinct_names": len(counts),
            "sha256": sha256(original),
        }

    shortfalls = {name: {"owned": master[name], "allocated": count}
                  for name, count in allocated.items() if count > master[name]}
    if shortfalls:
        raise ValueError(f"Deck cards exceed master ownership quantities: {shortfalls}")
    if sum(master.values()) != 1332 or len(master) != 751:
        raise ValueError("Master source changed from its verified 1332 copies / 751 names")
    if sum(allocated.values()) != 484 or sum(reserved.values()) != 201:
        raise ValueError("An archived deck size changed from its verified source")
    if deck_counts["Xander_EDH_IRL.csv"]["Lord Xander, the Collector"] != 1:
        raise ValueError("The Xander commander record is missing")
    if deck_counts["Xander_EDH_IRL.csv"]["Lutri, the Spellchaser"] != 1:
        raise ValueError("Lutri's companion record is missing")
    if deck_counts["Dihada_EDH_IRL.csv"]["Dihada, Binder of Wills"] != 1:
        raise ValueError("Dihada's commander record is missing")

    unassigned = master - allocated
    after_disassembly = master - reserved
    if sum(unassigned.values()) != 848 or sum(after_disassembly.values()) != 1131:
        raise ValueError("Available pool does not match reconciliation")
    outputs = {
        "available_unassigned.csv": csv_bytes(unassigned),
        "available_after_proposed_disassembly.csv": csv_bytes(after_disassembly),
    }
    manifest = {
        "snapshot_date": "2026-11-08",
        "source": "Cory's original physical inventory and six deck CSVs",
        "master_includes_deck_cards": True,
        "original_master_sha256": sha256(master_bytes),
        "original_archive_sha256": sha256(archive_bytes),
        "master": {"cards": sum(master.values()), "distinct_names": len(master)},
        "all_six_decks": {"cards": sum(allocated.values()), "distinct_names": len(allocated)},
        "keep_built_two_decks": {"cards": sum(reserved.values()), "distinct_names": len(reserved)},
        "unassigned_now": {"cards": sum(unassigned.values()), "distinct_names": len(unassigned)},
        "available_after_proposed_disassembly": {
            "cards": sum(after_disassembly.values()), "distinct_names": len(after_disassembly)},
        "decks": deck_manifest,
        "known_discrepancies": [
            "Stefanie_Jund_Prerelease.csv has 43 cards, although described as a 40-card deck. All 43 entries are preserved."
        ],
        "interpretation": "The four proposed disassemblies are hypothetical; the six original lists stay intact.",
        "identity_note": "Names and quantities only; editions, conditions, foils and prices are not specified.",
    }
    outputs["manifest.json"] = (json.dumps(manifest, indent=2, ensure_ascii=False) + "\n").encode("utf-8")
    for filename, content in outputs.items():
        path = SNAPSHOT / filename
        if write:
            path.write_bytes(content)
        elif not path.is_file() or path.read_bytes() != content:
            raise ValueError(f"Missing, modified, or stale generated file: {path}")
    if not CURRENT_STATUS.exists():
        raise ValueError("Missing active physical collection status")
    if CURRENT_STATUS.exists():
        current = json.loads(CURRENT_STATUS.read_text(encoding="utf-8"))
        if sorted(current["built_decks"]) != sorted(name for name, info in DECKS.items()
                                                    if info[2] == "keep_built"):
            raise ValueError("Current built deck list disagrees with reserved original decks")
        if sorted(current["disassembled_decks"]) != sorted(name for name, info in DECKS.items()
                                                          if info[2] == "proposed_disassembly"):
            raise ValueError("Current disassembled deck list disagrees with original six decks")
        if current.get("active_built_decklists") != {
            "Xander_EDH_IRL.csv": "data/physical_collection/current_decks/Xander_EDH_IRL.csv",
            "Dihada_EDH_IRL.csv": "data/physical_collection/2026-11-08/decks/Dihada_EDH_IRL.csv",
        }:
            raise ValueError("Current deck references do not identify Xander's rebuilt physical list")
        if current.get("xander_rebuild_event") != "data/physical_collection/updates/2026-11-08_xander_rebuild.json":
            raise ValueError("Current Xander rebuild event reference is missing")
        event = json.loads(XANDER_REBUILD.read_text(encoding="utf-8"))
        if (event.get("deck") != "Xander_EDH_IRL.csv"
                or event.get("source_snapshot") != "data/physical_collection/2026-11-08/decks/Xander_EDH_IRL.csv"
                or event.get("current_deck") != "data/physical_collection/current_decks/Xander_EDH_IRL.csv"
                or len(event.get("swaps", [])) != 20):
            raise ValueError("Malformed confirmed Xander rebuild event")
        active_xander = deck_counts["Xander_EDH_IRL.csv"].copy()
        outs, ins = set(), set()
        for item in event["swaps"]:
            old, new = item["out"], item["in"]
            if old in outs or new in ins or old == new or active_xander[old] != 1:
                # A basic Swamp is the only multi-copy card removed; all 20
                # changes are otherwise distinct singleton replacements.
                if not (old == "Swamp" and old not in outs and active_xander[old] > 1
                        and new not in ins):
                    raise ValueError(f"Invalid or duplicated physical swap: {item}")
            outs.add(old)
            ins.add(new)
            active_xander[old] -= 1
            if active_xander[old] == 0:
                del active_xander[old]
            active_xander[new] += 1
        if (sum(active_xander.values()) != 101
                or active_xander["Lord Xander, the Collector"] != 1
                or active_xander["Lutri, the Spellchaser"] != 1
                or active_xander["Swamp"] != 8
                or active_xander["The Unicomplex"] != 1):
            raise ValueError("Rebuilt Xander list is not the owner-confirmed 100 + companion")
        current_deck_bytes = csv_bytes(active_xander)
        if write:
            CURRENT_XANDER.parent.mkdir(parents=True, exist_ok=True)
            CURRENT_XANDER.write_bytes(current_deck_bytes)
        elif not CURRENT_XANDER.is_file() or CURRENT_XANDER.read_bytes() != current_deck_bytes:
            raise ValueError("Current Xander deck does not match confirmed 20-swap reconstruction")
        active_reserved = active_xander + deck_counts["Dihada_EDH_IRL.csv"]
        overbooked = active_reserved - master
        if overbooked:
            raise ValueError(f"Current built decks exceed owned copies: {dict(overbooked)}")
        available_now = master - active_reserved
        if (current["reserved_cards"] != sum(active_reserved.values())
                or current["available_cards"] != sum(available_now.values())
                or current["available_distinct_names"] != len(available_now)
                or current["current_available_pool"] != "data/physical_collection/current_available.csv"):
            raise ValueError("Current collection status counts or pool path disagree")
        current_bytes = csv_bytes(available_now)
        if write:
            CURRENT_POOL.write_bytes(current_bytes)
        elif not CURRENT_POOL.is_file() or CURRENT_POOL.read_bytes() != current_bytes:
            raise ValueError("Current available pool does not match rebuilt Xander plus Dihada")
    print(json.dumps({"result": "written" if write else "verified",
                      "master_cards": sum(master.values()),
                      "distinct_names": len(master),
                      "allocated_cards": sum(allocated.values()),
                      "unassigned_cards": sum(unassigned.values()),
                      "available_after_proposed_disassembly": sum(after_disassembly.values()),
                      "current_available_cards": current["available_cards"] if CURRENT_STATUS.exists() else None,
                      "jund_list_cards": sum(deck_counts["Stefanie_Jund_Prerelease.csv"].values())}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="Read-only verification")
    mode.add_argument("--write", action="store_true", help="Regenerate derived outputs")
    arguments = parser.parse_args()
    main(write=arguments.write)
