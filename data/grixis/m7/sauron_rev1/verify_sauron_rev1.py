#!/usr/bin/env python3
"""Deck #49 M7 Rev1 exact-hash structural and bounded live Oracle gate."""
import argparse
import json
import time
from collections import Counter
from hashlib import sha256
from pathlib import Path
from urllib.request import Request, urlopen

HERE = Path(__file__).resolve().parent
BASE = HERE / "Sauron_Lord_of_the_Rings_Approved_2026-10-15_Preserved_Source.txt"
PROPOSED = HERE / "Sauron_Lord_of_the_Rings_M7_Rev1_Candidate_2026-10-27.txt"
BASE_SHA = "72a814e6ae1153507c9c1469a7792043b2e5c055d9e5fcd9f6cfcf7781e287b0"
PROPOSED_SHA = "c427805f78f7aca7384db56022868a2e7cb7d01eeeabbb280a18e77e538a8159"
SWAPS = {
    "Ancient Brass Dragon": "Hoarding Broodlord",
    "Feed the Swarm": "Chaos Warp",
    "Forbidden Alchemy": "Intuition",
    "Jin-Gitaxias, Core Augur": "Doom Whisperer",
    "Relic of Sauron": "Basalt Monolith",
    "Summons of Saruman": "Sink into Stupor // Soporific Springs",
    "Thrill of Possibility": "Unmarked Grave",
    "Windfall": "Valakut Awakening // Valakut Stoneforge",
}
NATIVE_CORE = {
    "Sauron, Lord of the Rings", "Anger", "Wonder", "Archon of Cruelty",
    "Metamorphosis Fanatic", "Sauron, the Dark Lord", "Call of the Ring",
    "The One Ring", "Nazgûl", "The Balrog of Moria", "Barad-dûr",
    "The Black Gate", "Mount Doom", "The Mouth of Sauron",
    "Moria Scavenger", "Voracious Fell Beast", "Ripples of Undeath",
    "Entomb", "Buried Alive", "Reanimate", "Animate Dead",
    "Dance of the Dead", "Necromancy", "Persist", "Living Death",
    "Sneak Attack", "Victimize", "Command Beacon", "Phyrexian Tower",
    "Mana Vault", "Grim Monolith", "Sol Ring", "Orcish Bowmasters",
}
FRONT_LANDS = {
    "Ancient Tomb", "Badlands", "Barad-dûr", "Blood Crypt",
    "Bloodstained Mire", "City of Brass", "Command Beacon",
    "Command Tower", "Exotic Orchard", "Flooded Strand", "Island",
    "Luxury Suite", "Mana Confluence", "Marsh Flats", "Misty Rainforest",
    "Morphic Pool", "Mount Doom", "Mountain", "Otawara, Soaring City",
    "Phyrexian Tower", "Polluted Delta", "Scalding Tarn", "Steam Vents",
    "Swamp", "The Black Gate", "Training Center", "Underground Sea",
    "Urborg, Tomb of Yawgmoth", "Volcanic Island", "Watery Grave",
    "Xander's Lounge",
}
MDFC_LANDS = {
    "Valakut Awakening // Valakut Stoneforge",
    "Sink into Stupor // Soporific Springs",
}


def read_exact(path, expected_hash):
    raw = path.read_bytes()
    assert sha256(raw).hexdigest() == expected_hash, f"hash drift: {path}"
    assert raw.startswith(b"1x Sauron, Lord of the Rings [Commander]\n")
    rows = []
    for line in raw.decode("utf-8").splitlines():
        qty, name = line.split("x ", 1)
        assert qty in {"1", "2", "4"}, line
        rows.append((int(qty), name.removesuffix(" [Commander]")))
    assert sum(q for q, _ in rows) == 100, "physical count"
    assert rows[0] == (1, "Sauron, Lord of the Rings")
    assert len(rows) == len({name for _, name in rows}) == 96
    repeats = {name: qty for qty, name in rows if qty > 1}
    assert repeats == {"Nazgûl": 4, "Swamp": 2}, repeats
    return Counter({name: qty for qty, name in rows})


def offline():
    base = read_exact(BASE, BASE_SHA)
    candidate = read_exact(PROPOSED, PROPOSED_SHA)
    assert set(base) - set(candidate) == set(SWAPS)
    assert set(candidate) - set(base) == set(SWAPS.values())
    assert all(base[cut] == candidate[add] == 1 for cut, add in SWAPS.items())
    assert NATIVE_CORE <= candidate.keys()
    assert sum(candidate[n] for n in FRONT_LANDS if n in candidate) == 32
    assert MDFC_LANDS <= candidate.keys()
    assert sum(candidate[n] for n in MDFC_LANDS) == 2
    print("PASS: exact frozen approved + 8-swap candidate SHA-256")
    print("PASS: 100 physical / 96 distinct / Nazgûl x4 + Swamp x2 / 32 printed lands + 2 MDFCs")
    print("PASS: exact one-for-one changes and commander-first core retained")
    return candidate


def live_scryfall(candidate):
    names = list(candidate)
    seen = {}
    for start in range(0, len(names), 75):
        batch = names[start:start + 75]
        request = Request(
            "https://api.scryfall.com/cards/collection",
            data=json.dumps({"identifiers": [{"name": n.split(" // ")[0]} for n in batch]}).encode(),
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json",
                "User-Agent": "GrixisEncyclopediaAudit/1.0 (+https://github.com/corymstover/GrokBotMTGCompanion)",
            },
            method="POST",
        )
        with urlopen(request, timeout=25) as resp:
            result = json.load(resp)
        assert not result.get("not_found"), result.get("not_found")
        for card in result["data"]:
            seen[card["name"]] = card
        if start + 75 < len(names):
            time.sleep(0.25)
    assert set(seen) == set(names), f"Oracle name mismatch: {set(seen) ^ set(names)}"
    for name, card in seen.items():
        assert card["legalities"]["commander"] == "legal", name
        assert set(card["color_identity"]) <= {"U", "B", "R"}, name
        assert card.get("oracle_id"), name
        assert card.get("oracle_text") or card.get("card_faces"), name
    assert "Legendary Creature" in seen["Sauron, Lord of the Rings"]["type_line"]
    print(f"PASS: current Scryfall all {len(seen)} Oracle identities, Commander legalities and UBR identities")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--live-scryfall", action="store_true")
    args = parser.parse_args()
    verified = offline()
    if args.live_scryfall:
        live_scryfall(verified)
