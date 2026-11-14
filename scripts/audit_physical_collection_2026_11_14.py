#!/usr/bin/env python3
"""Audit the Nov 14 physical master, six built decks and available card pool.

This verifies physical copy allocation, not Oracle text, legality or power.
All 2026-11-08 historical source files remain immutable.
"""
import argparse
import csv
import hashlib
import io
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "data/physical_collection"
SNAP = BASE / "2026-11-14"
MAPPING = {
    "Xander_EDH_IRL.csv": ("Cory_s_Lord_Xander_IRL_EDH.csv", 101, "Lord Xander, the Collector"),
    "Dihada_EDH_IRL.csv": ("Stefanie_Dihada_EDH_IRL.csv", 100, "Dihada, Binder of Wills"),
    "Wasitora_Jund_EDH_IRL.csv": ("Stefanie_s_IRL_Jund_EDH.csv", 100, "Wasitora, Nekoru Queen"),
    "Locutus_Orzhov_Borg_EDH_IRL.csv": ("Cory_s_IRL_Orzhov_Borg_EDH.csv", 100, "Locutus, the One Who Speaks"),
    "Izzet_Pauper_IRL.csv": ("Izzet.csv", 60, None),
    "Stefanie_MonoBlack_Pauper_IRL.csv": ("Mono_Black_Devotion_Control.csv", 60, None),
}
PURCHASES = Counter({
    "Cavern-Hoard Dragon":1, "Deep Space Scan":1, "Geyadrone Dihada":1,
    "Glimpse the Unthinkable":1, "Kefka, Court Mage // Kefka, Ruler of Ruin":1,
    "Kuja, Genome Sorcerer // Trance Kuja, Fate Defied":1, "Mai and Zuko":1,
    "Mairsil, the Pretender":1, "Obeka, Brute Chronologist":1,
    "Obeka, Splitter of Seconds":1, "Slimefoot and Squee":1,
    "Sol'Kanar the Tainted":1, "Sol'kanar the Swamp King":1,
    "The Caretaker":1, "Vazi, Keen Negotiator":1,
    "Yurlok of Scorch Thrash":1,
})

def read_csv(path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != ["Quantity", "Name"]:
            raise ValueError(f"Invalid header in {path}")
        data = Counter()
        for row in reader:
            name = row["Name"]
            count = int(row["Quantity"])
            if not name or name.strip() != name or count <= 0 or name in data:
                raise ValueError(f"Invalid or duplicate line in {path}: {row!r}")
            data[name] = count
        return data

def csv_bytes(data):
    stream = io.StringIO(newline="")
    writer = csv.writer(stream, lineterminator="\n")
    writer.writerow(["Quantity", "Name"])
    for name in sorted(data, key=lambda s: (s.casefold(), s)):
        writer.writerow([data[name], name])
    return stream.getvalue().encode("utf-8")

def verify(write=False):
    manifest = json.loads((SNAP / "manifest.json").read_text())
    status = json.loads((BASE / "current_status.json").read_text())
    assert manifest["as_of_date"] == status["as_of_date"] == "2026-11-14"
    assert set(manifest["file_sha256"]) == {"Every_Card_we_own_IRL.csv"} | {v[0] for v in MAPPING.values()}
    for filename, expected in manifest["file_sha256"].items():
        assert hashlib.sha256((SNAP / filename).read_bytes()).hexdigest() == expected, f"Source file changed: {filename}"
    owned = read_csv(SNAP / "Every_Card_we_own_IRL.csv")
    original = read_csv(BASE / "2026-11-08/master_inventory.csv")
    assert len(original) == 751 and sum(original.values()) == 1332
    assert owned - original == PURCHASES and not original - owned, "Unexpected inventory difference"
    assert len(owned) == 766 and sum(owned.values()) == 1348
    assert set(status["built_decks"]) == set(MAPPING)
    assert set(status["active_built_decklists"]) == set(MAPPING)
    reserved = Counter()
    for current, (source, expected_size, commander) in MAPPING.items():
        assert status["active_built_decklists"][current] == f"data/physical_collection/current_decks/{current}"
        src = read_csv(SNAP / source)
        actual = read_csv(BASE / "current_decks" / current)
        assert src == actual, f"Active cards differ from confirmed source: {current}"
        assert sum(src.values()) == expected_size, f"Bad deck size: {current}"
        if commander:
            assert src[commander] == 1, f"Missing commander: {commander}"
        reserved.update(src)
    assert not reserved - owned, "Physical copy over-allocation"
    available = owned - reserved
    assert (sum(reserved.values()), sum(available.values()), len(available)) == (521, 827, 508)
    assert (status["reserved_cards"], status["available_cards"], status["available_distinct_names"]) == (521, 827, 508)
    assert status["current_available_pool"] == "data/physical_collection/current_available.csv"
    expected = csv_bytes(available)
    if write:
        (BASE / "current_available.csv").write_bytes(expected)
    else:
        assert (BASE / "current_available.csv").read_bytes() == expected, "Stale free-pool export"
    result = {"verified": True, "owned":sum(owned.values()), "reserved":sum(reserved.values()),
              "available":sum(available.values()), "available_names":len(available), "decks":len(MAPPING)}
    print(json.dumps(result, sort_keys=True))
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", action="store_true")
    group.add_argument("--write", action="store_true")
    args = parser.parse_args()
    verify(write=args.write)
