#!/usr/bin/env python3
"""M7 Deck 48 exact-source gate and bounded live all-card Scryfall legality audit.

No research pipeline, Monte Carlo, or automatic canonical edits. The preserved
October 15 approval is immutable; this review-only candidate needs owner approval.
"""
import argparse
import json
import time
from collections import Counter
from hashlib import sha256
from pathlib import Path
from urllib.request import Request, urlopen

HERE = Path(__file__).resolve().parent
BASE = HERE / "Saruman_Approved_2026-10-15_Preserved_Source.txt"
PROPOSED = HERE / "Saruman_M7_Rev1_Candidate_2026-10-27.txt"
BASE_SHA = "4981499230898c8b36c6f46b0f60a5277630d92abe477d48ed77091e2203ffe2"
PROPOSED_SHA = "dbf71bc86caec1be73c4333bf43e4104cccb5f91a06d2766e8b586adabd9724b"
SWAPS = {
    "Kazuul's Fury // Kazuul's Cliffs": "Valakut Awakening // Valakut Stoneforge",
    "Black Waltz No. 3": "Tainted Strike",
    "Commence the Endgame": "Mind's Desire",
    "Sauron, the Dark Lord": "Arcane Bombardment",
    "Feed the Swarm": "Chaos Warp",
    "Mana Geyser": "Temporal Trespass",
    "The Ozolith": "March of Swirling Mist",
}
NATIVE_CORE = {
    "Saruman, the White Hand", "Blasphemous Act", "Blood for the Blood God!",
    "Dig Through Time", "Treasure Cruise", "Volcanic Salvo", "Fall of Cair Andros",
    "Harmonic Prodigy", "Wizard's Staff", "Veyran, Voice of Duality",
    "Bothersome Noisemaker", "Mauhúr, Uruk-hai Captain", "The Great Goblin",
    "All Will Be One", "Orcish Siegemaster", "Orcish Medicine",
    "Widespread Brutality", "Chandra's Ignition", "Soul's Fire",
    "The Black Gate", "The One Ring", "Swan Song", "Force of Will",
}
FRONT_LANDS = {
    "Ancient Tomb", "Badlands", "Barad-dûr", "Blood Crypt", "Bloodstained Mire",
    "City of Brass", "Command Tower", "Exotic Orchard", "Flooded Strand",
    "Island", "Luxury Suite", "Mana Confluence", "Marsh Flats",
    "Misty Rainforest", "Morphic Pool", "Mount Doom", "Mountain",
    "Otawara, Soaring City", "Polluted Delta", "Scalding Tarn",
    "Steam Vents", "Swamp", "The Black Gate", "Training Center",
    "Underground Sea", "Volcanic Island", "Watery Grave", "Xander's Lounge",
}
MDFC_LANDS = {
    "Valakut Awakening // Valakut Stoneforge",
    "Sea Gate Restoration // Sea Gate, Reborn",
    "Shatterskull Smashing // Shatterskull, the Hammer Pass",
    "Sink into Stupor // Soporific Springs",
}


def read_exact(path, expected_hash):
    raw = path.read_bytes()
    assert sha256(raw).hexdigest() == expected_hash, f"hash changed: {path}"
    rows = []
    for line in raw.decode("utf-8").splitlines():
        assert line.startswith(("1x ", "2x ")), line
        qty, name = line.split("x ", 1)
        rows.append((int(qty), name.removesuffix(" [Commander]")))
    assert sum(qty for qty, _ in rows) == 100
    assert rows[0] == (1, "Saruman, the White Hand")
    assert raw.startswith(b"1x Saruman, the White Hand [Commander]\n")
    assert len(rows) == 97
    names = [name for _, name in rows]
    assert len(set(names)) == 97
    assert {name: qty for qty, name in rows if qty > 1} == {
        "Island": 2, "Mountain": 2, "Swamp": 2
    }
    return Counter({name: qty for qty, name in rows})


def offline():
    original = read_exact(BASE, BASE_SHA)
    candidate = read_exact(PROPOSED, PROPOSED_SHA)
    assert set(original) - set(candidate) == set(SWAPS)
    assert set(candidate) - set(original) == set(SWAPS.values())
    assert all(original[x] == candidate[y] == 1 for x, y in SWAPS.items())
    assert NATIVE_CORE <= candidate.keys()
    assert sum(candidate[name] for name in FRONT_LANDS if name in candidate) == 31
    assert MDFC_LANDS <= candidate.keys()
    assert sum(candidate[name] for name in MDFC_LANDS) == 4
    print("PASS: preserved baseline + candidate exact hashes, 100 physical each,")
    print("PASS: 97 distinct, legal basic repeats only, 31 printed lands + 4 land MDFCs,")
    print("PASS: exact 7x 1:1 changes; Orc Army cast/MV and finisher engine preserved.")
    return candidate


def scryfall_live(candidate):
    names = list(candidate)
    seen = {}
    for start in range(0, len(names), 75):
        batch = names[start:start + 75]
        request = Request(
            "https://api.scryfall.com/cards/collection",
            data=json.dumps({"identifiers": [{"name": name} for name in batch]}).encode(),
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json;q=0.9,*/*;q=0.8",
                "User-Agent": "GrixisEncyclopediaAudit/1.0 (+https://github.com/corymstover/GrokBotMTGCompanion)",
            },
            method="POST",
        )
        with urlopen(request, timeout=25) as resp:
            data = json.load(resp)
        not_found = data.get("not_found", [])
        assert not not_found, f"unresolved Oracle identity: {not_found}"
        for card in data["data"]:
            seen[card["name"]] = card
        if start + 75 < len(names):
            time.sleep(0.25)
    assert set(seen) == set(names), f"card mismatch: {set(names)^set(seen)}"
    for name, card in seen.items():
        assert card["legalities"]["commander"] == "legal", f"{name}: official Commander illegal"
        assert set(card["color_identity"]) <= {"U", "B", "R"}, f"{name}: color mismatch"
        assert card.get("oracle_id"), f"{name}: missing Oracle identity"
        assert card.get("oracle_text") or card.get("card_faces"), f"{name}: no Oracle text"
    assert "Legendary Creature" in seen["Saruman, the White Hand"]["type_line"]
    print(f"PASS: current Scryfall Oracle identities / legalities / UBR for all {len(seen)} distinct cards.")


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--live-scryfall", action="store_true")
    opt = args.parse_args()
    verified = offline()
    if opt.live_scryfall:
        scryfall_live(verified)
