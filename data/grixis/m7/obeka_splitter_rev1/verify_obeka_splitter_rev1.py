"""Bounded exact-file and deterministic scenario checks for Obeka Splitter M7 Rev1.

This intentionally does not claim matchup simulation, multiplayer win rates, or a
live 100-card Oracle lookup. Run: python3 obeka_splitter_m7_rev1_verify.py
"""

from collections import Counter
from hashlib import sha256
from pathlib import Path


CANDIDATE = Path(__file__).with_name("obeka_splitter_m7_rev1.txt")
EXPECTED_SHA = "f80d882944d5e39f3c6661da4dcdce3ec6eead577cd981dc54f7dc522be50859"
ADDS = {
    "Academy Manufactor", "Aggravated Assault", "Blackblade Reforged",
    "Jeska, Thrice Reborn", "Karlach, Fury of Avernus", "Rising of the Day",
}
CUTS = {
    "Darksteel Reactor", "Jhoira of the Ghitu", "Paradox Haze",
    "Ring of Valkas", "Ring of Xathrid", "Rousing Refrain",
}
LANDS = {
    "Ancient Tomb", "Arena of Glory", "Arid Mesa", "Badlands", "Blood Crypt",
    "Bloodstained Mire", "City of Brass", "Command Tower", "Flooded Strand",
    "Island", "Luxury Suite", "Mana Confluence", "Marsh Flats", "Misty Rainforest",
    "Morphic Pool", "Mountain", "Otawara, Soaring City", "Polluted Delta",
    "Reflecting Pool", "Scalding Tarn", "Shizo, Death's Storehouse", "Steam Vents",
    "Swamp", "Training Center", "Underground Sea", "Urborg, Tomb of Yawgmoth",
    "Verdant Catacombs", "Volcanic Island", "Watery Grave", "Wooded Foothills",
    "Xander's Lounge",
}
def load():
    raw = CANDIDATE.read_bytes()
    assert sha256(raw).hexdigest() == EXPECTED_SHA, "raw candidate changed"
    assert raw.endswith(b"\n") and b"\r" not in raw, "requires LF-terminated UTF-8"
    lines = raw.decode("utf-8").splitlines()
    names = Counter()
    for line in lines:
        quantity, sep, name = line.partition("x ")
        assert sep and quantity.isdecimal() and int(quantity) > 0, line
        names[name.removesuffix(" [Commander]")] += int(quantity)
    assert lines[0] == "1x Obeka, Splitter of Seconds [Commander]"
    assert sum(names.values()) == 100, sum(names.values())
    assert len(names) == 96, len(names)
    assert names["Island"] == 3 and names["Mountain"] == 2 and names["Swamp"] == 2
    assert all(qty == 1 for name, qty in names.items() if name not in {"Island", "Mountain", "Swamp"})
    assert sum(names[name] for name in LANDS) == 35
    assert all(names[name] == 1 for name in ADDS)
    assert not CUTS.intersection(names)
    return names


def check_scenarios():
    def upkeep_count(power, damage_factors=(), extra_trigger_effects=0, hits=1):
        damage = power
        for factor in damage_factors:
            damage *= factor
        return damage * (1 + extra_trigger_effects) * hits

    # Requires unprevented player damage each hit; double strike only gets two hits
    # when Obeka actually connects in both combat damage steps.
    assert upkeep_count(2) == 2
    assert upkeep_count(2, damage_factors=(3,)) == 6  # Jeska's 0
    assert upkeep_count(2 + 5) == 7  # Blackblade on five-land Obeka
    assert upkeep_count(2 + 1) == 3  # Rising first hit
    assert upkeep_count(2, hits=2) == 4  # Karlach's second successful combat
    assert upkeep_count(4, damage_factors=(2, 3), extra_trigger_effects=2) == 72

    def artifact_tokens(upkeeps, separate_clue_or_treasure_events, manufactor):
        return upkeeps * separate_clue_or_treasure_events * (3 if manufactor else 1)

    # Smaug + Journal create separate token events each upkeep. Sieve requires
    # five actual expendable artifacts; neither upkeep nor token creation untaps Sieve.
    assert artifact_tokens(2, 2, False) == 4
    assert artifact_tokens(2, 2, True) == 12
    assert artifact_tokens(2, 1, True) >= 5
    assert not artifact_tokens(1, 1, True) >= 5

    def assault_fuel_after_hit(power, treasure_producers=1):
        treasures = upkeep_count(power) * treasure_producers
        return treasures >= 5  # {3}{R}{R}, assuming any-color Treasure mana

    assert assault_fuel_after_hit(5)
    assert not assault_fuel_after_hit(4)


if __name__ == "__main__":
    names = load()
    check_scenarios()
    print("PASS exact SHA, 100 cards, 96 distinct, 35 lands, basics-only repeats")
    print("PASS six intended additions/six cuts and bounded conditional engine checks")
    print("LIMIT: no fresh full-batch Scryfall/Oracle or empirical win-rate certification")
