#!/usr/bin/env python3
"""Audit November 25 owned copies and exact active deck allocation.

Immutable prior snapshots remain untouched. Proxy placeholders are not owned.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path


def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
from audit_physical_collection_2026_11_23 import read_csv, available_csv, INCOMING

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "data" / "physical_collection"
SNAP = BASE / "2026-11-25"
OLD = BASE / "2026-11-23"
POOL = BASE / "current_available.csv"
STATUS = BASE / "current_status.json"
RETIRED = "MonoBlack_Pauper_IRL.csv"
MAPPING = {
    "Xander_EDH_IRL.csv": ("Cory_s_Lord_Xander_IRL_EDH.csv", 101, "Lord Xander, the Collector"),
    "Dihada_EDH_IRL.csv": ("Stefanie_Dihada_EDH_IRL.csv", 100, "Dihada, Binder of Wills"),
    "Korvold_Jund_EDH_IRL.csv": ("Stefanie_s_IRL_Jund_EDH.csv", 100, "Korvold, Fae-Cursed King"),
    "Locutus_Orzhov_Borg_EDH_IRL.csv": ("Cory_s_IRL_Orzhov_Borg_EDH.csv", 100, "Locutus, the One Who Speaks"),
    "MonoRed_Pauper_IRL.csv": ("Mono_Red_Madness.csv", 60, None),
}
ACTIVE_MAPPING = MAPPING

def verify(write=False):
    status = json.loads(STATUS.read_text(encoding="utf-8"))
    manifest = json.loads((SNAP / "manifest.json").read_text(encoding="utf-8"))
    event_file = "data/physical_collection/updates/2026-11-25_collection_reconciliation.json"
    event = json.loads((ROOT / event_file).read_text(encoding="utf-8"))
    assert status["as_of_date"] == manifest["as_of_date"] == event["as_of_date"] == "2026-11-25"
    assert status["source_master_inventory"] == "data/physical_collection/live_inventory/2026-11-25_after_balrog_sale.csv"
    assert status["uploaded_master_inventory_path"] == "data/physical_collection/2026-11-25/Every_Card_we_own_IRL_corrected.csv"
    assert status["uploaded_master_inventory_sha256"] == manifest["source_inventory_sha256"]
    assert hashlib.sha256((ROOT / status["source_master_inventory"]).read_bytes()).hexdigest() == status["source_master_inventory_sha256"]
    assert status["source_archive_sha256"] == manifest["source_deck_archive_sha256"]
    assert status["reconciliation_event"] == event_file
    xander_event_path = "data/physical_collection/updates/2026-11-25_lord_xander_upgrade.json"
    xander_event = json.loads((ROOT / xander_event_path).read_text(encoding="utf-8"))
    assert xander_event["owner_confirmed"] is True
    assert xander_event["date"] == "2026-11-25"
    assert status["xander_current_deck_update_event"] == xander_event_path
    assert status["xander_current_deck_last_confirmed"] == "2026-11-25"
    assert status["xander_current_deck_git_blob_sha"] == xander_event["current_git_blob_sha"]
    assert len(xander_event["added"]) == len(xander_event["removed"]) == 18
    assert len(set(xander_event["added"])) == len(set(xander_event["removed"])) == 18
    for name, expected in manifest["file_sha256"].items():
        assert hashlib.sha256((SNAP / name).read_bytes()).hexdigest() == expected, name
    assert set(manifest["file_sha256"]) == {"Every_Card_we_own_IRL_corrected.csv"} | {d[0] for d in MAPPING.values()}
    original_upload = read_csv(SNAP / "Every_Card_we_own_IRL_corrected.csv")
    owned = read_csv(ROOT / status["source_master_inventory"])
    previous = read_csv(OLD / "Every_Card_we_own_IRL_corrected.csv")
    assert (sum(original_upload.values()), len(original_upload)) == (1471, 845)
    assert (sum(owned.values()), len(owned)) == (1470, 844)
    assert (sum(previous.values()), len(previous)) == (1395, 793)
    assert dict(original_upload - previous) == event["added_or_increased_by_name"]
    assert dict(previous - original_upload) == event["removed_or_decreased_by_name"] == {"Cavern-Hoard Dragon": 1}
    assert sum((original_upload - previous).values()) == 77
    sale_path = "data/physical_collection/updates/2026-11-25_balrog_sale.json"
    sale = json.loads((ROOT / sale_path).read_text(encoding="utf-8"))
    assert status["inventory_sale_event"] == sale_path
    assert status["last_physical_inventory_correction"] == "2026-11-25"
    assert sale["owner_confirmed"] is True and sale["sold_copies"] == 1
    assert sale["card_sold"] == "The Balrog, Durin's Bane"
    assert original_upload - owned == Counter({"The Balrog, Durin's Bane": 1})
    assert owned - original_upload == Counter()
    assert sale["corrected_live_inventory_sha256"] == status["source_master_inventory_sha256"]
    assert sale["immutable_original_source_sha256"] == manifest["source_inventory_sha256"]
    assert set(status["built_decks"]) == set(status["active_built_decklists"]) == set(MAPPING)
    assert status["disassembled_built_decks"] == [RETIRED]
    assert not (BASE / "current_decks" / RETIRED).exists()
    assert sum(read_csv(OLD / "Mono_Black_Devotion_Control.csv").values()) == 60
    total = Counter()
    for filename, (source, expected_size, commander) in MAPPING.items():
        historical = read_csv(SNAP / source)
        live_path = BASE / "current_decks" / filename
        deck = read_csv(live_path)
        assert sum(historical.values()) == sum(deck.values()) == expected_size, filename
        assert status["active_built_decklists"][filename] == "data/physical_collection/current_decks/" + filename
        if filename == "Xander_EDH_IRL.csv":
            assert historical - deck == Counter(dict.fromkeys(xander_event["removed"], 1))
            assert deck - historical == Counter(dict.fromkeys(xander_event["added"], 1))
            assert git_blob_sha((SNAP / source).read_bytes()) == xander_event["previous_git_blob_sha"]
            assert git_blob_sha(live_path.read_bytes()) == xander_event["current_git_blob_sha"]
        else:
            assert live_path.read_bytes() == (SNAP / source).read_bytes(), filename
        if commander:
            assert deck[commander] == 1, commander
        old_deck = read_csv(OLD / source)
        if filename == "Dihada_EDH_IRL.csv":
            assert old_deck - historical == Counter({"The Balrog, Durin's Bane": 1})
            assert historical - old_deck == Counter({"Ingris Stingerquill": 1})
        else:
            assert old_deck == historical, filename
        total.update(deck)
    xander = read_csv(BASE / "current_decks" / "Xander_EDH_IRL.csv")
    assert xander["Lutri, the Spellchaser"] == 1 and sum(xander.values()) == 101
    assert status["xander_main_deck_cards_including_commander"] == 100
    assert status["xander_companion_counted_outside_main_deck"] is True
    assert total - owned == INCOMING
    assert (sum(total.values()), sum(INCOMING.values())) == (461, 13)
    pool = owned - total
    assert (sum(pool.values()), len(pool)) == (1022, 609)
    assert status["deck_slots_including_xander_companion"] == 461
    assert status["physical_deck_cards_reserved"] == status["reserved_cards"] == 448
    assert status["proxy_cards_pending"] == 13
    assert status["proxies_by_name"] == dict(INCOMING)
    assert status["owned_cards"] == 1470 and status["owned_distinct_names"] == 844
    assert status["available_cards"] == 1022 and status["available_distinct_names"] == 609
    assert status["current_available_pool"] == "data/physical_collection/current_available.csv"
    assert pool["The Balrog, Durin's Bane"] == 0
    assert owned["The Balrog, Durin's Bane"] == 0
    assert owned["Ingris Stingerquill"] == 1
    assert total["Ingris Stingerquill"] == 1
    assert pool["Ingris Stingerquill"] == 0
    assert pool["Gandalf, Goblins' Bane // Flameshape"] == 1
    assert pool["Fraying Sanity"] == 0 and pool["Hedron Crab"] == 0
    assert pool["Ruin Crab"] == 0 and pool["Zellix, Sanity Flayer"] == 0
    assert pool["Nicol Bolas, God-Pharaoh"] == 0
    expected = available_csv(pool, owned)
    if write:
        POOL.write_bytes(expected)
    else:
        assert POOL.read_bytes() == expected, "Current available pool is stale"
    result = {"verified": True, "as_of_date": "2026-11-25", "owned": 1470,
              "distinct_owned": 844, "decks": 5, "deck_slots": 461,
              "physical_reserved": 448, "incoming_proxies": 13,
              "available": 1022, "available_names": 609}
    print(json.dumps(result, sort_keys=True))
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    flags = parser.add_mutually_exclusive_group(required=True)
    flags.add_argument("--check", action="store_true")
    flags.add_argument("--write", action="store_true")
    args = parser.parse_args()
    verify(write=args.write)
