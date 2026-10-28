#!/usr/bin/env python3
"""Offline exact-list RogSi M7 Rev1 certification; live Scryfall audit performed separately."""
from collections import Counter
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "RogSi_Approved_2026-10-15_Preserved_Source.txt"
REV1 = ROOT / "RogSi_M7_Rev1_Candidate_2026-10-27.txt"
OLD_HASH = "06c9e22b5afc46bd58bbbfdef5c42a796d2a986a2972456107c29aee1b5f905c"
NEW_HASH = "97f3c0ca70303b44cd887938c320b75de01e991feec7d71d4c18811aeaa88225"
PAIRS = {
    "Force of Negation": "Misdirection",
    "Into the Flood Maw": "Snapback",
    "Windfall": "Chromatic Star",
    "Grim Monolith": "Last Chance",
    "Demonic Counsel": "Flashback",
    "Undercity Sewers": "Starting Town",
}
PARTNERS = ["Rograkh, Son of Rohgahh", "Silas Renn, Seeker Adept"]
REQUIRED_NATIVE = [
    "Mox Amber", "Springleaf Drum", "Paradise Mantle", "Culling the Weak",
    "Infernal Plunge", "Diabolic Intent", "Fierce Guardianship",
    "Deflecting Swat", "Deadly Rollick", "Flare of Duplication",
    "Hexing Squelcher", "Vexing Bauble",
]
REQUIRED_COMBOS = [
    "Thassa's Oracle", "Demonic Consultation", "Tainted Pact",
    "Underworld Breach", "Lion's Eye Diamond", "Brain Freeze",
    "Grinding Station",
]
LANDS = {
    "Ancient Tomb", "Arid Mesa", "Badlands", "Blood Crypt",
    "Bloodstained Mire", "City of Brass", "City of Traitors",
    "Command Tower", "Flooded Strand", "Gemstone Caverns",
    "Mana Confluence", "Marsh Flats", "Misty Rainforest",
    "Otawara, Soaring City", "Phyrexian Tower", "Polluted Delta",
    "Scalding Tarn", "Starting Town", "Steam Vents",
    "Underground Sea", "Verdant Catacombs", "Volcanic Island",
    "Watery Grave", "Wooded Foothills",
}


def parse(raw):
    rows = raw.decode("utf-8").splitlines()
    names = []
    for row in rows:
        assert row.startswith("1x "), row
        names.append(row[3:].removesuffix(" [Commander]"))
    assert len(rows) == 100
    assert len(Counter(names)) == 100
    assert rows[:2] == [f"1x {x} [Commander]" for x in PARTNERS]
    return names


def main():
    original, candidate = BASE.read_bytes(), REV1.read_bytes()
    assert sha256(original).hexdigest() == OLD_HASH, "approved source mutated"
    assert sha256(candidate).hexdigest() == NEW_HASH, "candidate mutated"
    old, new = parse(original), parse(candidate)
    assert set(old) - set(new) == set(PAIRS)
    assert set(new) - set(old) == set(PAIRS.values())
    assert len(LANDS & set(new)) == 24
    assert all(card in new for card in PARTNERS + REQUIRED_NATIVE + REQUIRED_COMBOS)
    assert "Flashback" in new and "Last Chance" in new
    assert "Chromatic Star" in new and "Grinding Station" in new
    assert "Misdirection" in new and "Snapback" in new
    assert "Undercity Sewers" not in new and "Starting Town" in new
    print("PASS: exact raw old/new hashes, 100 physical, two partners, 100 unique,")
    print("PASS: six 1:1 changes, 24 lands, Rograkh native core and both win packages")
    print("NOTICE: current Oracle/card legality is separately documented from the live Scryfall collection audit.")


if __name__ == "__main__":
    main()
