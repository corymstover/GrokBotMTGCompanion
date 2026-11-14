#!/usr/bin/env python3
"""Audit the immutable six-deck snapshot and owner-confirmed live allocations.

The original ZIP, master inventory and six historical decklists are never edited.
Both rebuilt Commander decks and the two newly sleeved Pauper decks are
independently reproduced from owner confirmations. The current pool subtracts
all four live decks from the immutable physical master.
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
CURRENT_DIHADA = ROOT / "data" / "physical_collection" / "current_decks" / "Dihada_EDH_IRL.csv"
CURRENT_IZZET = ROOT / "data" / "physical_collection" / "current_decks" / "Izzet_Pauper_IRL.csv"
CURRENT_STEFANIE_PAUPER = ROOT / "data" / "physical_collection" / "current_decks" / "Stefanie_MonoBlack_Pauper_IRL.csv"
XANDER_REBUILD = ROOT / "data" / "physical_collection" / "updates" / "2026-11-08_xander_rebuild.json"
DIHADA_REBUILD = ROOT / "data" / "physical_collection" / "updates" / "2026-11-08_dihada_rebuild.json"
IZZET_BUILD = ROOT / "data" / "physical_collection" / "updates" / "2026-11-08_izzet_pauper_build.json"
STEFANIE_PAUPER_BUILD = ROOT / "data" / "physical_collection" / "updates" / "2026-11-08_stefanie_monoblack_pauper_build.json"
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
    # A newer owner-confirmed snapshot supersedes only the current allocation,
    # not the immutable 2026-11-08 source records or their prior receipts.
    if CURRENT_STATUS.exists() and json.loads(CURRENT_STATUS.read_text(encoding="utf-8")).get("as_of_date") == "2026-11-14":
        from audit_physical_collection_2026_11_14 import verify
        verify(write=write)
        return
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
        expected_built = [name for name, info in DECKS.items() if info[2] == "keep_built"]
        expected_built.extend(["Izzet_Pauper_IRL.csv", "Stefanie_MonoBlack_Pauper_IRL.csv"])
        if sorted(current["built_decks"]) != sorted(expected_built):
            raise ValueError("Current built deck list disagrees with owner-confirmed decks")
        if sorted(current["disassembled_decks"]) != sorted(name for name, info in DECKS.items()
                                                          if info[2] == "proposed_disassembly"):
            raise ValueError("Current disassembled deck list disagrees with original six decks")
        if current.get("active_built_decklists") != {
            "Xander_EDH_IRL.csv": "data/physical_collection/current_decks/Xander_EDH_IRL.csv",
            "Dihada_EDH_IRL.csv": "data/physical_collection/current_decks/Dihada_EDH_IRL.csv",
            "Izzet_Pauper_IRL.csv": "data/physical_collection/current_decks/Izzet_Pauper_IRL.csv",
            "Stefanie_MonoBlack_Pauper_IRL.csv": "data/physical_collection/current_decks/Stefanie_MonoBlack_Pauper_IRL.csv",
        }:
            raise ValueError("Current deck references do not identify all built physical lists")
        if current.get("xander_rebuild_event") != "data/physical_collection/updates/2026-11-08_xander_rebuild.json":
            raise ValueError("Current Xander rebuild event reference is missing")
        if current.get("dihada_rebuild_event") != "data/physical_collection/updates/2026-11-08_dihada_rebuild.json":
            raise ValueError("Current Dihada rebuild event reference is missing")
        if current.get("izzet_pauper_build_event") != "data/physical_collection/updates/2026-11-08_izzet_pauper_build.json":
            raise ValueError("Current Izzet Pauper build event reference is missing")
        if current.get("stefanie_monoblack_pauper_build_event") != "data/physical_collection/updates/2026-11-08_stefanie_monoblack_pauper_build.json":
            raise ValueError("Current Stefanie Mono-Black Pauper build event reference is missing")
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
        dihada_event = json.loads(DIHADA_REBUILD.read_text(encoding="utf-8"))
        if (dihada_event.get("deck") != "Dihada_EDH_IRL.csv"
                or dihada_event.get("source_snapshot") != "data/physical_collection/2026-11-08/decks/Dihada_EDH_IRL.csv"
                or dihada_event.get("current_deck") != "data/physical_collection/current_decks/Dihada_EDH_IRL.csv"
                or len(dihada_event.get("swaps", [])) != 15):
            raise ValueError("Malformed confirmed Dihada rebuild event")
        active_dihada = deck_counts["Dihada_EDH_IRL.csv"].copy()
        dihada_outs, dihada_ins = set(), set()
        for item in dihada_event["swaps"]:
            old, new = item["out"], item["in"]
            if (old == new or old in dihada_outs or new in dihada_ins
                    or active_dihada[old] < 1
                    or (old != "Swamp" and active_dihada[old] != 1)):
                raise ValueError(f"Invalid or duplicated Dihada physical swap: {item}")
            dihada_outs.add(old)
            dihada_ins.add(new)
            active_dihada[old] -= 1
            if active_dihada[old] == 0:
                del active_dihada[old]
            active_dihada[new] += 1
        if (sum(active_dihada.values()) != 100
                or active_dihada["Dihada, Binder of Wills"] != 1
                or active_dihada["Swamp"] != 4
                or active_dihada["Plains"] != 7
                or active_dihada["Blood Crypt"] != 1
                or active_dihada["Meticulous Commons"] != 1):
            raise ValueError("Rebuilt Dihada list does not match the confirmed 15 swaps")
        current_dihada_bytes = csv_bytes(active_dihada)
        if sha256(current_dihada_bytes) != dihada_event.get("current_deck_sha256"):
            raise ValueError("Rebuilt Dihada deck checksum does not match owner-confirmed event")
        if write:
            CURRENT_DIHADA.parent.mkdir(parents=True, exist_ok=True)
            CURRENT_DIHADA.write_bytes(current_dihada_bytes)
        elif not CURRENT_DIHADA.is_file() or CURRENT_DIHADA.read_bytes() != current_dihada_bytes:
            raise ValueError("Current Dihada deck does not match confirmed 15-swap reconstruction")
        izzet_event = json.loads(IZZET_BUILD.read_text(encoding="utf-8"))
        if (izzet_event.get("deck") != "Izzet_Pauper_IRL.csv"
                or izzet_event.get("current_deck") != "data/physical_collection/current_decks/Izzet_Pauper_IRL.csv"
                or izzet_event.get("format") != "pauper"
                or izzet_event.get("main_deck_cards") != 60
                or izzet_event.get("sideboard_cards") != 0
                or izzet_event.get("sideboard") != []):
            raise ValueError("Malformed owner-confirmed Izzet Pauper build event or sideboard")
        cards = izzet_event.get("main_deck")
        if not isinstance(cards, list) or len(cards) != 16:
            raise ValueError("The Izzet Pauper event must declare all 16 distinct main-deck names")
        active_izzet: Counter[str] = Counter()
        for entry in cards:
            name, quantity = entry.get("name"), entry.get("quantity")
            if (not isinstance(name, str) or not name or name in active_izzet
                    or type(quantity) is not int or quantity < 1
                    or (name not in {"Island", "Mountain"} and quantity > 4)):
                raise ValueError(f"Invalid Izzet Pauper main-deck entry: {entry}")
            active_izzet[name] = quantity
        if (sum(active_izzet.values()) != 60
                or sum(active_izzet[name] for name in ("Island", "Mountain", "Andoria", "Izzet Guildgate")) != 21
                or active_izzet["Jace's Phantasm"] != 4
                or active_izzet["Guttersnipe"] != 4):
            raise ValueError("Izzet Pauper main deck differs from Cory's physically sleeved list")
        current_izzet_bytes = csv_bytes(active_izzet)
        if sha256(current_izzet_bytes) != izzet_event.get("current_deck_sha256"):
            raise ValueError("Izzet Pauper checksum does not match the confirmation event")
        if write:
            CURRENT_IZZET.parent.mkdir(parents=True, exist_ok=True)
            CURRENT_IZZET.write_bytes(current_izzet_bytes)
        elif not CURRENT_IZZET.is_file() or CURRENT_IZZET.read_bytes() != current_izzet_bytes:
            raise ValueError("Current Izzet Pauper deck does not match owner-confirmed 60-card list")
        stefanie_event = json.loads(STEFANIE_PAUPER_BUILD.read_text(encoding="utf-8"))
        if (stefanie_event.get("deck") != "Stefanie_MonoBlack_Pauper_IRL.csv"
                or stefanie_event.get("current_deck") != "data/physical_collection/current_decks/Stefanie_MonoBlack_Pauper_IRL.csv"
                or stefanie_event.get("format") != "pauper"
                or stefanie_event.get("main_deck_cards") != 60
                or stefanie_event.get("sideboard_cards") != 0
                or stefanie_event.get("sideboard") != []):
            raise ValueError("Malformed owner-confirmed Stefanie Pauper build event or sideboard")
        stefanie_cards = stefanie_event.get("main_deck")
        if not isinstance(stefanie_cards, list) or len(stefanie_cards) != 15:
            raise ValueError("Stefanie's Pauper event must declare all 15 distinct main-deck names")
        active_stefanie_pauper: Counter[str] = Counter()
        for entry in stefanie_cards:
            name, quantity = entry.get("name"), entry.get("quantity")
            if (not isinstance(name, str) or not name or name in active_stefanie_pauper
                    or type(quantity) is not int or quantity < 1
                    or (name != "Swamp" and quantity > 4)):
                raise ValueError(f"Invalid Stefanie Pauper main-deck entry: {entry}")
            active_stefanie_pauper[name] = quantity
        if (sum(active_stefanie_pauper.values()) != 60
                or active_stefanie_pauper["Swamp"] != 24
                or active_stefanie_pauper["Corrupt"] != 4
                or active_stefanie_pauper["Gray Merchant of Asphodel"] != 3):
            raise ValueError("Stefanie Pauper main deck differs from her sleeved Mono-Black list")
        current_stefanie_bytes = csv_bytes(active_stefanie_pauper)
        if sha256(current_stefanie_bytes) != stefanie_event.get("current_deck_sha256"):
            raise ValueError("Stefanie Pauper checksum does not match the confirmation event")
        if write:
            CURRENT_STEFANIE_PAUPER.parent.mkdir(parents=True, exist_ok=True)
            CURRENT_STEFANIE_PAUPER.write_bytes(current_stefanie_bytes)
        elif not CURRENT_STEFANIE_PAUPER.is_file() or CURRENT_STEFANIE_PAUPER.read_bytes() != current_stefanie_bytes:
            raise ValueError("Current Stefanie Pauper deck does not match owner-confirmed 60-card list")
        active_reserved = active_xander + active_dihada + active_izzet + active_stefanie_pauper
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
            raise ValueError("Current available pool does not match all four active decks")
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
