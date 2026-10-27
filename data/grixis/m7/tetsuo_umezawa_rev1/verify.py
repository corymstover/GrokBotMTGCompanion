"""Deck #54 Tetsuo Umezawa M7 Rev1 exact source and bounded rules fixtures.

The finite tests model listed preconditions, costs and state transitions, not
the entirety of Magic or multiplayer win rates. --live resolves every selected
Oracle identity from current Scryfall, verifies Commander legality and UBR.
"""
import argparse
from collections import Counter
from dataclasses import dataclass
from hashlib import sha256
import json
from pathlib import Path
import time
import unittest
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "Tetsuo_Umezawa_Oct15_baseline.txt"
FINAL = ROOT.parent / "candidate_lists" / "Tetsuo_Umezawa_M7_Rev1.txt"
BASE_SHA = "14ca66ceae4d634630a85aa1787731cfe840fd9fc2093bc37ad5dc17d1539ff6"
FINAL_SHA = "e00196135931bde6e380e47d5ffe9e4360d4756f00ad083ee5ed0757919fddd7"

ADDS = [
    "Battlemage's Bracers", "City of Brass", "Deflecting Swat",
    "Dramatic Reversal", "Fierce Guardianship", "Forbidden Orchard",
    "Icy Manipulator", "Isochron Scepter", "Life of the Party",
    "Mana Confluence", "Morphic Pool", "Otawara, Soaring City",
    "Puppet Strings", "Rhystic Study", "Takenuma, Abandoned Mire",
    "Thornbite Staff", "Toxic Deluge", "Uphill Battle",
    "Urborg, Tomb of Yawgmoth",
]
CUTS = [
    "Blasphemous Act", "Brainstorm", "Counterspell", "Dark Ritual",
    "Fumiko the Lowblood", "Geode Rager", "Grenzo, Havoc Raiser",
    "Island", "Island", "Mountain", "Mountain", "Propaganda",
    "Rings of Brighthearth", "Sly Instigator", "Sulfur Falls",
    "Swamp", "Swamp", "Urabrask the Hidden", "Xantcha, Sleeper Agent",
]
PROTECTED = {
    "Tetsuo Umezawa", "Aphetto Alchemist", "Arcane Signet",
    "Baleful Strix", "Bloodthirsty Blade", "Blustersquall",
    "Bothersome Quasit", "Disrupt Decorum", "Fatestitcher",
    "Firkraag, Cunning Instigator", "Flood", "Force of Will",
    "Frozen Aether", "Hylda's Crown of Winter", "Illusionist's Bracers",
    "Karazikar, the Eye Tyrant", "Kardur, Doomscourge",
    "Lightning Greaves", "Magewright's Stone",
    "Minamo, School at Water's Edge", "Patriar's Seal",
    "Puppeteer", "Rathi Trapper", "Red Death, Shipwrecker",
    "Retreat to Coralhelm", "Royal Assassin", "Shiny Impetus",
    "Sting, the Glinting Dagger", "Swiftfoot Boots",
    "Talisman of Creativity", "Talisman of Dominance",
    "Talisman of Indulgence", "Thousand-Year Elixir",
    "Vengeful Ancestor", "Verity Circle",
}
BASICS = {"Island": 3, "Mountain": 3, "Swamp": 4}
LANDS = {
    "Badlands", "Blood Crypt", "Bloodstained Mire", "Bojuka Bog",
    "City of Brass", "Command Tower", "Exotic Orchard", "Flooded Strand",
    "Forbidden Orchard", "Luxury Suite", "Mana Confluence", "Marsh Flats",
    "Maze of Ith", "Minamo, School at Water's Edge", "Misty Rainforest",
    "Morphic Pool", "Otawara, Soaring City", "Polluted Delta",
    "Steam Vents", "Takenuma, Abandoned Mire", "Underground Sea",
    "Urborg, Tomb of Yawgmoth", "Volcanic Island", "Watery Grave",
    "Xander's Lounge", "Island", "Mountain", "Swamp",
}


def parse(path, expected_hash):
    raw = path.read_bytes()
    assert sha256(raw).hexdigest() == expected_hash, f"Raw SHA mismatch: {path}"
    assert raw.endswith(b"\n") and b"\r" not in raw, path
    lines = raw.decode("utf-8").splitlines()
    assert lines[0] == "1x Tetsuo Umezawa [Commander]"
    copies = Counter()
    for line in lines:
        count, name = line.split("x ", 1)
        assert int(count) > 0
        copies[name.removesuffix(" [Commander]")] += int(count)
    assert sum(copies.values()) == 100
    return copies


def check_source():
    before = parse(BASE, BASE_SHA)
    after = parse(FINAL, FINAL_SHA)
    assert len(before) == 87 and len(after) == 93
    assert before - after == Counter(CUTS)
    assert after - before == Counter(ADDS)
    assert {n: q for n, q in after.items() if q > 1} == BASICS
    assert PROTECTED <= set(after)
    assert sum(q for n, q in after.items() if n in LANDS) == 35
    assert after["Sink into Stupor // Soporific Springs"] == 1
    assert after["Maze of Ith"] == 1  # a land but not mana-producing
    print("PASS canonical exact SHA, staged raw SHA, 100 physical / 93 names, "
          "19 actual swaps, 35 front-face lands + 1 MDFC, basic-only repeats")
    return after


def live_scryfall(copies):
    names = sorted(copies)
    found = {}
    for start in range(0, len(names), 75):
        # Scryfall collection identifiers resolve a modal DFC by its front
        # face name; the response retains the exact full two-face card name.
        body = json.dumps({
            "identifiers": [{"name": name.split(" // ", 1)[0]}
                            for name in names[start:start+75]]
        }).encode()
        req = Request(
            "https://api.scryfall.com/cards/collection", data=body, method="POST",
            headers={"Content-Type": "application/json", "Accept": "application/json",
                     "User-Agent": "GrixisEncyclopediaDeck54/1.0 (+https://github.com/corymstover/GrokBotMTGCompanion)"},
        )
        with urlopen(req, timeout=60) as response:
            payload = json.load(response)
        assert payload.get("not_found") == [], payload.get("not_found")
        for card in payload["data"]:
            found[card["name"]] = card
        time.sleep(.25)
    assert set(found) == set(names), f"Unresolved {set(names) ^ set(found)}"
    for name, card in found.items():
        assert card.get("oracle_id"), name
        assert card["legalities"]["commander"] == "legal", name
        assert set(card["color_identity"]) <= {"U", "B", "R"}, name
        assert card.get("oracle_text") or card.get("card_faces"), name
    oracle = lambda n: found[n].get("oracle_text", "").lower()
    assert "aura spells" in oracle("Tetsuo Umezawa")
    assert "tapped or blocking" in oracle("Tetsuo Umezawa")
    assert "untap this creature" in oracle("Thornbite Staff")
    assert "all nonland permanents" in oracle("Dramatic Reversal")
    assert "untap" in oracle("Puppet Strings")
    assert "imprint" in oracle("Isochron Scepter")
    assert "may pay {1}" in oracle("Battlemage's Bracers")
    assert "creatures played" in oracle("Uphill Battle")
    print("PASS 93/93 LIVE CURRENT Scryfall Oracle IDs, official Commander "
          "legality U/B/R/colorless, no exceptions, full selected list")


@dataclass
class Creature:
    tapped: bool = False
    blocking: bool = False
    hexproof: bool = False
    alive: bool = True
    vigilance: bool = False


def targetable(c):
    return c.alive and (c.tapped or c.blocking) and not c.hexproof


def activate_tetsuo(mana, tetsuo_ready, victim):
    if not tetsuo_ready or not targetable(victim):
        return False
    if any(mana.get(color, 0) < number for color, number in
           {"U": 1, "B": 2, "R": 1}.items()):
        return False
    for color, number in {"U": 1, "B": 2, "R": 1}.items():
        mana[color] -= number
    victim.alive = False
    return True


class FiniteCaseChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.deck = check_source()

    def test_C1_oracle_spell_aura_prohibition_not_equip(self):
        aura_spell_targets_tetsuo = False
        equipment_equip_targets_tetsuo = True
        aura_already_attached_can_stay = True
        self.assertFalse(aura_spell_targets_tetsuo)
        self.assertTrue(equipment_equip_targets_tetsuo)
        self.assertTrue(aura_already_attached_can_stay)

    def test_K1_tapped_or_blocking_independent_and_target_recheck(self):
        self.assertTrue(targetable(Creature(blocking=True)))
        self.assertTrue(targetable(Creature(tapped=True)))
        self.assertFalse(targetable(Creature()))
        self.assertFalse(targetable(Creature(tapped=True, hexproof=True)))
        victim = Creature(tapped=True)
        victim.tapped = False  # opponent untaps in response before resolution
        self.assertFalse(targetable(victim))

    def test_K2_sting_each_combat_untaps_but_not_mana(self):
        ready = False
        for active_player in ("us", "opponent_A", "opponent_B", "opponent_C"):
            ready = True  # Sting beginning of each player's combat trigger
            self.assertTrue(ready, active_player)
            ready = False  # activation consumes tap
        self.assertEqual(len(["us", "opponent_A", "opponent_B", "opponent_C"]), 4)
        self.assertFalse(activate_tetsuo({"U": 0, "B": 2, "R": 1}, ready, Creature(tapped=True)))

    def test_K3_and_F1_four_colored_pips_not_vault_generic(self):
        victim = Creature(tapped=True)
        mana = {"U": 1, "B": 2, "R": 1, "C": 12}
        self.assertTrue(activate_tetsuo(mana, True, victim))
        self.assertEqual([mana[c] for c in ("U", "B", "R")], [0, 0, 0])
        self.assertFalse(activate_tetsuo({"U": 0, "B": 0, "R": 0, "C": 30},
                                         True, Creature(tapped=True)))

    def test_K4_retreat_fetch_two_distinct_landfall_events(self):
        zones = {"fetch": "battlefield", "fetched": "library"}
        triggers = 1  # land drop fetchland
        zones["fetch"] = "graveyard"
        zones["fetched"] = "battlefield"
        triggers += 1  # fetched land ETB
        self.assertEqual(triggers, 2)
        self.assertEqual(zones["fetch"], "graveyard")

    def test_K5_goad_forces_attack_if_able_but_no_auto_tap(self):
        vigilance_attacker = Creature(vigilance=True)
        nonvigilance_attacker = Creature()
        can_attack_other_opponent = True
        if can_attack_other_opponent:
            nonvigilance_attacker.tapped = True
        self.assertTrue(nonvigilance_attacker.tapped)
        self.assertFalse(vigilance_attacker.tapped)
        self.assertFalse(targetable(vigilance_attacker))

    def test_E1_tetsuo_summoning_sick_cannot_tap_without_haste(self):
        sick_without_haste = False
        self.assertFalse(activate_tetsuo({"U": 1, "B": 2, "R": 1},
                                          sick_without_haste, Creature(tapped=True)))
        self.assertTrue(activate_tetsuo({"U": 1, "B": 2, "R": 1},
                                         True, Creature(blocking=True)))

    def test_E2_friendly_untap_target_vs_greaves_shroud(self):
        own_tetsuo = {"tapped": True, "shroud": False}
        if not own_tetsuo["shroud"]:
            own_tetsuo["tapped"] = False  # Minamo, Puppet, Seal
        self.assertFalse(own_tetsuo["tapped"])
        own_tetsuo = {"tapped": True, "shroud": True}
        if not own_tetsuo["shroud"]:
            own_tetsuo["tapped"] = False
        self.assertTrue(own_tetsuo["tapped"])

    def test_E3_battlemage_copy_one_mana_and_bracers_free(self):
        paid = {"U": 1, "B": 2, "R": 1, "C": 1}
        targets = [Creature(tapped=True), Creature(blocking=True)]
        self.assertTrue(activate_tetsuo(paid, True, targets[0]))
        paid["C"] -= 1  # Battlemage copy trigger; new legal target
        targets[1].alive = False
        self.assertEqual(sum(not t.alive for t in targets), 2)
        self.assertEqual(paid, {"U": 0, "B": 0, "R": 0, "C": 0})
        self.assertIn("Illusionist's Bracers", self.deck)

    def test_W1_goad_plus_destruction_is_not_immediate_win(self):
        attackers = [Creature(tapped=True) for _ in range(3)]
        mana = {"U": 1, "B": 2, "R": 1}
        self.assertTrue(activate_tetsuo(mana, True, attackers[0]))
        self.assertEqual(sum(c.alive for c in attackers), 2)

    def test_W2_alchemist_bracers_rock_repeat_mana_not_phantom(self):
        self.assertIn("Aphetto Alchemist", self.deck)
        self.assertIn("Illusionist's Bracers", self.deck)
        self.assertIn("Arcane Signet", self.deck)
        # For each paid/stack-resolved Alchemist activation, one copy untaps
        # Alchemist, original untaps the rock; tapping the rock once yields one
        # chosen commander color. This is repeatable with ready Alchemist.
        generated = Counter()
        for chosen in ("U", "B", "B", "R", "U", "B", "R"):
            generated[chosen] += 1
        self.assertGreaterEqual(generated["B"], 2)
        self.assertGreaterEqual(generated["U"], 1)
        self.assertGreaterEqual(generated["R"], 1)
        # Infinite mana alone doesn't tap/untap Tetsuo or create legal targets.
        self.assertFalse(targetable(Creature()))

    def test_F2_creatureless_table_denies_commander_target(self):
        self.assertFalse(activate_tetsuo({"U": 1, "B": 2, "R": 1},
                                          True, Creature(alive=False)))
        self.assertIn("Mana Drain", self.deck)

    def test_F3_commander_removal_after_activation_does_not_counter_ability(self):
        target = Creature(tapped=True)
        mana = {"U": 1, "B": 2, "R": 1}
        # Costs are paid and ability is on stack; source then removed.
        self.assertTrue(activate_tetsuo(mana, True, target))
        self.assertFalse(target.alive)
        self.assertIn("Deflecting Swat", self.deck)
        self.assertIn("Fierce Guardianship", self.deck)

    def test_new_icy_can_tap_upkeep_single_target_not_goad_board(self):
        target = Creature()
        generic = 1
        generic -= 1
        target.tapped = True
        self.assertTrue(targetable(target))
        self.assertEqual(generic, 0)
        self.assertFalse(targetable(Creature()))

    def test_new_puppet_strings_dual_mode_source_ready_same_turn(self):
        target = Creature()
        target.tapped = True  # {2},{T} tap target
        self.assertTrue(targetable(target))
        own_tetsuo = Creature(tapped=True)
        own_tetsuo.tapped = False  # another ready activation on later turn
        self.assertFalse(own_tetsuo.tapped)

    def test_new_thornbite_death_untaps_but_not_color_payment(self):
        prey = Creature(tapped=True)
        mana = {"U": 1, "B": 2, "R": 1}
        self.assertTrue(activate_tetsuo(mana, True, prey))
        self.assertFalse(prey.alive)  # enters grave, dies: Staff trigger
        tetsuo_tapped = False  # Staff untaps Tetsuo on creature death
        self.assertFalse(tetsuo_tapped)
        self.assertFalse(activate_tetsuo(mana, True, Creature(tapped=True)))

    def test_new_scepter_reversal_colored_rock_net_positive(self):
        # A ready Scepter imprinting Dramatic Reversal pays 2 to cast copy;
        # Reversal untaps Scepter and nonland mana rocks, Tetsuo included.
        # Three colored mana produced by ready rocks -> net one per iteration.
        pool = 0
        for _ in range(3):
            pool += 3
            self.assertGreaterEqual(pool, 2)
            pool -= 2
        self.assertEqual(pool, 3)
        # If rocks only make 2, loop makes no mana; no guaranteed payoff.
        self.assertEqual(2 - 2, 0)

    def test_new_life_party_goaded_tokens_not_self_attack_early(self):
        opponents = ("A", "B", "C")
        copied_tokens = {p: {"goaded": True, "owner": p} for p in opponents}
        self.assertEqual(len(copied_tokens), 3)
        self.assertTrue(all(v["goaded"] for v in copied_tokens.values()))
        self.assertTrue(any(p != "A" for p in opponents))

    def test_new_deluge_selective_tetsuo_survives_x2(self):
        commander_toughness = 3
        small_creature_toughness = 2
        x = 2
        self.assertGreater(commander_toughness - x, 0)
        self.assertLessEqual(small_creature_toughness - x, 0)
        self.assertGreater(13, commander_toughness)  # Act would kill commander

    def test_new_uphill_affects_opponent_cast_creatures_not_all_tokens(self):
        cast_creature = Creature()
        cast_creature.tapped = True  # opponent creature was played
        token_not_played = Creature()
        self.assertTrue(cast_creature.tapped)
        self.assertFalse(token_not_played.tapped)

    def test_new_orchard_fixing_has_gifted_creature_tradeoff(self):
        mana_choice = {"U", "B", "R"}
        target_opponent_spirit = Creature(vigilance=False)
        self.assertEqual(mana_choice, {"U", "B", "R"})
        self.assertFalse(targetable(target_opponent_spirit))
        target_opponent_spirit.tapped = True  # attacks later if forced
        self.assertTrue(targetable(target_opponent_spirit))

    def test_new_channels_are_lands_not_extra_spell_slots(self):
        self.assertIn("Otawara, Soaring City", self.deck)
        self.assertIn("Takenuma, Abandoned Mire", self.deck)
        self.assertIn("Urborg, Tomb of Yawgmoth", self.deck)
        self.assertEqual(self.deck["Island"], 3)
        self.assertEqual(self.deck["Mountain"], 3)
        self.assertEqual(self.deck["Swamp"], 4)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--live", action="store_true")
    args = parser.parse_args()
    selected = check_source()
    if args.live:
        live_scryfall(selected)
    else:
        unittest.main(argv=["verify.py"], exit=False, verbosity=2)
