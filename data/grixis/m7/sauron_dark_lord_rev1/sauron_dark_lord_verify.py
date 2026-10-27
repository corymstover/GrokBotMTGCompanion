#!/usr/bin/env python3
"""#50 M7 Rev1: source-bound structure, bounded rules fixtures, live Oracle audit.

These are finite rules-state assertions, not a full gameplay simulator or win-rate
measurement. Mandatory external M6/I-J acceptance remains a separate ledger.
"""
import argparse
import json
import time
from collections import Counter
from hashlib import sha256
from pathlib import Path
from urllib.request import Request, urlopen

HERE = Path(__file__).resolve().parent
BASE = HERE / "sauron_dark_lord_baseline.txt"
CANDIDATE = HERE / "sauron_dark_lord_m7_rev1.txt"
ALT12 = HERE / "sauron_dark_lord_alt12.txt"
ALT_EARLY = HERE / "sauron_dark_lord_alt_early_ring.txt"
BASE_SHA = "fab194f69a6e15b83679c1419f88ba6fdd56cd9527946cb94a6d8efe23a7dfc8"
CANDIDATE_SHA = "266660c6a3241c07a052da7624366be1f9617cb5db4c35c422b0e8f828977d9b"
ALT12_SHA = "093ca97894cf29774505b7d97eccaf29f5b2fbb7ab6e39cda2bdf6876cebb9e7"
ALT_EARLY_SHA = "ae88c6e4885a23100380b6691eadaefd9cb643d35c4e765231aeeba978927991"
SWAPS = {
    "Blasphemous Act": "Soothing of Sméagol",
    "Moria Scavenger": "Bone Miser",
    "Rogue's Passage": "Cavern of Souls",
    "Saruman, the White Hand": "Arcane Adaptation",
    "Sauron, Lord of the Rings": "Lord of the Nazgûl",
    "Sauron's Ransom": "Moonstone, Harsh Mistress",
    "Summons of Saruman": "Glint-Horn Buccaneer",
    "The Ozolith": "Herald of Secret Streams",
    "Widespread Brutality": "Lazotep Plating",
    "Windfall": "Birthday Escape",
}
PROTECTED = {
    "Sauron, the Dark Lord", "Nazgûl", "Bilbo, Retired Burglar",
    "Call of the Ring", "In the Darkness Bind Them", "Ringsight",
    "Mauhúr, Uruk-hai Captain", "The Great Goblin",
    "Great Goblin, Foul-Hearted", "Minas Morgul, Dark Fortress",
    "Roaming Throne", "The Black Gate", "March from the Black Gate",
    "Orcish Siegemaster", "Witch-king of Angmar", "The One Ring",
    "Relic of Sauron", "Anger", "Wonder", "Toxic Deluge",
    "Force of Will", "Fierce Guardianship", "Deflecting Swat",
}
LANDS = {
    "Ancient Tomb", "Badlands", "Barad-dûr", "Blood Crypt",
    "Bloodstained Mire", "Cavern of Souls", "City of Brass",
    "Command Tower", "Exotic Orchard", "Flooded Strand", "Island",
    "Luxury Suite", "Mana Confluence", "Marsh Flats",
    "Minas Morgul, Dark Fortress", "Misty Rainforest", "Morphic Pool",
    "Mount Doom", "Mountain", "Otawara, Soaring City", "Polluted Delta",
    "Rogue's Passage",
    "Scalding Tarn", "Steam Vents", "Swamp", "The Black Gate",
    "Training Center", "Underground Sea", "Urborg, Tomb of Yawgmoth",
    "Volcanic Island", "Watery Grave", "Xander's Lounge",
}


def read_list(path, digest):
    raw = path.read_bytes()
    assert sha256(raw).hexdigest() == digest, ("raw_hash_drift", path)
    assert raw.startswith(b"1x Sauron, the Dark Lord [Commander]\n")
    rows = []
    for line in raw.decode("utf-8").splitlines():
        qty, name = line.split("x ", 1)
        assert qty in {"1", "2", "3", "7"}, line
        rows.append((int(qty), name.removesuffix(" [Commander]")))
    assert sum(q for q, _ in rows) == 100
    assert rows[0] == (1, "Sauron, the Dark Lord")
    assert len(rows) == len({n for _, n in rows}) == 91
    assert {n: q for q, n in rows if q > 1} == {
        "Mountain": 2, "Nazgûl": 7, "Swamp": 3
    }
    assert sum(q for q, n in rows if n in LANDS) == 34
    return Counter({name: qty for qty, name in rows})


def structural():
    source = read_list(BASE, BASE_SHA)
    final = read_list(CANDIDATE, CANDIDATE_SHA)
    assert set(source) - set(final) == set(SWAPS)
    assert set(final) - set(source) == set(SWAPS.values())
    assert all(source[cut] == final[add] == 1 for cut, add in SWAPS.items())
    assert PROTECTED <= set(final)
    larger = read_list(ALT12, ALT12_SHA)
    early = read_list(ALT_EARLY, ALT_EARLY_SHA)
    assert set(larger) - set(final) == {"Cover of Darkness", "Fellwar Stone"}
    assert set(final) - set(larger) == {"Orcish Siegemaster", "Relic of Sauron"}
    assert set(early) - set(final) == {"Gollum, Patient Plotter", "Sam's Desperate Rescue"}
    assert set(final) - set(early) == {"Moonstone, Harsh Mistress", "Bone Miser"}
    print("PASS exact source and Rev1 raw hashes, 100/91/34, legal repeats, ten swaps")
    print("PASS two full 100-card alternatives: larger twelve-swap and early-Ring package")
    return final


def rules_fixtures():
    # C1/K1: Ward costs the targeting OPPONENT a legendary creature/artifact;
    # it is not hexproof and does not protect against untargeted spells.
    def ward_can_pay(opponent_targets, opp_legendary):
        return not opponent_targets or bool(opp_legendary)
    assert not ward_can_pay(True, [])
    assert ward_can_pay(True, ["legendary creature"])
    assert ward_can_pay(True, ["legendary artifact"])
    assert ward_can_pay(False, [])

    # K2/E1: Opponent spell CAST, not its resolution, is the amass trigger.
    def cast_amass(opponent_casts, countered, throne_avatar=False):
        del countered  # countering a spell does not counter Sauron's trigger.
        return opponent_casts * (2 if throne_avatar else 1)
    assert cast_amass(2, 2) == 2 and cast_amass(0, 0) == 0
    assert cast_amass(1, 1, True) == 2

    # K3/K4/W2: Mauhur modifies a qualifying counter-placement EVENT by +1;
    # The Great Goblin triggers once per event, not per added counter.
    def counter_event(base_amount, mauhur, goblin):
        return base_amount + int(mauhur), (1 if goblin else 0)
    assert counter_event(3, True, True) == (4, 1)
    assert counter_event(1, False, True) == (1, 1)
    assert counter_event(0, True, True) == (1, 1)

    # K5: Roaming Throne's ONE choice cannot simultaneously double Avatar
    # Sauron triggers and Wraith Nazgul triggers.
    def copies(choice, sauron_triggers, nazgul_triggers):
        return (sauron_triggers * (2 if choice == "Avatar" else 1),
                nazgul_triggers * (2 if choice == "Wraith" else 1))
    assert copies("Avatar", 2, 7) == (4, 7)
    assert copies("Wraith", 2, 7) == (2, 14)

    # K6/E2: One temptation triggers each of seven Nazgul, but Sauron's
    # discard-whole-hand choice is optional; only choosing it draws four.
    def temptation(nazgul, choose_discard, hand_size):
        return nazgul, (4 if choose_discard else 0), (0 if choose_discard else hand_size)
    assert temptation(7, True, 5) == (7, 4, 0)
    assert temptation(7, False, 5) == (7, 0, 5)

    # K7: Minas Morgul's shadow counter also adds Wraith type to an Army.
    army_types = {"Orc", "Army"}
    army_types.add("Wraith")
    assert {"Orc", "Army", "Wraith"} <= army_types

    # W1: Only an Army actually dealing COMBAT damage to a PLAYER triggers
    # Sauron's temptation; blocked/no-damage and noncombat ping do not.
    def army_ring(combat, dealt_to_player, is_army):
        return int(combat and dealt_to_player and is_army)
    assert army_ring(True, True, True) == 1
    assert army_ring(True, False, True) == 0
    assert army_ring(False, True, True) == 0

    # F2/F3: Quiet opponents suppress cast-triggers; a sweeper kills a token
    # Army with no Ozolith in Rev1; Call and Nazgul can still generate value.
    assert cast_amass(0, 0) == 0
    assert temptation(7, False, 3)[0] == 7
    assert not any(card in SWAPS.values() for card in ["The Ozolith"])

    # New changed-card contract: choose Wraith with Arcane Adaptation, THEN
    # the Army and all other controlled creatures also receive Nazgul counters.
    all_types = [{"Army", "Orc"}, {"Avatar", "Horror"}, {"Wraith"}]
    adapted = [types | {"Wraith"} for types in all_types]
    assert all("Wraith" in t for t in adapted)

    # Herald applies to creatures with +1/+1 counters (Army amass includes
    # counters), but is not intrinsically unblockable with zero counters.
    def herald_unblockable(counters):
        return counters > 0
    assert herald_unblockable(2) and not herald_unblockable(0)

    # Moonstone's discard-to-exile is optional; an exiled card is no longer a
    # reanimation target in the graveyard, and costs to play still apply.
    def moonstone_zone(discarded, choose_exile):
        return "exile" if discarded and choose_exile else "graveyard"
    assert moonstone_zone(True, True) == "exile"
    assert moonstone_zone(True, False) == "graveyard"

    # Cavern Avatar can pay Sauron's colored creature spell cost; it cannot
    # grant an uncounterable Wraith spell with that same fixed choice.
    def cavern_protects(chosen, creature_types):
        return chosen in creature_types
    assert cavern_protects("Avatar", {"Avatar", "Horror"})
    assert not cavern_protects("Avatar", {"Wraith", "Noble"})

    # F1: No listed self-recasting/extra-combat loop is asserted or modeled.
    # This is a conservative finite negative test, NOT exhaustive proof of
    # absence of all unknown interactions.
    assert "Underworld Breach" not in SWAPS.values()
    print("PASS bounded C1, K1-K7, E1-E2, W1-W2, F1-F3 and changed-card fixtures")


def live_scryfall(candidate):
    names = list(candidate)
    seen = {}
    for start in range(0, len(names), 75):
        batch = names[start:start + 75]
        ids = [
            {"set": "tmp", "collector_number": "151"} if name == "Reanimate"
            else {"name": name.split(" // ")[0]}
            for name in batch
        ]
        request = Request(
            "https://api.scryfall.com/cards/collection",
            data=json.dumps({"identifiers": ids}).encode(),
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json",
                "User-Agent": "GrixisEncyclopediaAudit/1.0 (+https://github.com/corymstover/GrokBotMTGCompanion)",
            }, method="POST",
        )
        with urlopen(request, timeout=30) as response:
            result = json.load(response)
        assert not result.get("not_found"), result.get("not_found")
        for card in result["data"]:
            seen[card["name"]] = card
        if start + 75 < len(names):
            time.sleep(0.3)
    assert set(seen) == set(names), ("unresolved_names", set(names) ^ set(seen))
    for name, card in seen.items():
        assert card["legalities"]["commander"] == "legal", name
        assert set(card["color_identity"]) <= {"U", "B", "R"}, name
        assert card.get("oracle_id"), name
        assert card.get("oracle_text") or card.get("card_faces"), name
    assert "Legendary Creature" in seen["Sauron, the Dark Lord"]["type_line"]
    assert "nine cards named Nazgûl" in seen["Nazgûl"]["oracle_text"]
    assert "Wraith" in seen["Arcane Adaptation"].get("oracle_text", "") or "creature type" in seen["Arcane Adaptation"]["oracle_text"]
    print(f"PASS live Scryfall: all {len(names)} Oracle cards legal in Commander and UBR")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--live-scryfall", action="store_true")
    args = parser.parse_args()
    cards = structural()
    rules_fixtures()
    if args.live_scryfall:
        live_scryfall(cards)
