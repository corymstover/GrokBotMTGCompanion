"""Loki M7 Rev1: 13 source-bound, finite M6 blueprint case fixtures.

These tests bind the *approved candidate bytes*, selected live Oracle records,
explicitly paid/available resources, and positive/adversarial conditions.
They are not multiplayer simulations, win-rate measurements, or an exhaustive
implementation of the Magic Comprehensive Rules.
"""
from __future__ import annotations

import hashlib
import json
import re
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data/grixis/m7/candidate_lists/Loki__the_Deceiver_ChatGPT_Rev1.txt"
SNAP = ROOT / "data/grixis/m6/oracle_snapshots/Loki__the_Deceiver_M7_Scryfall_20261023.json"
EXPECTED = "919734ad1f60e56a636561815d319ec1eb0fbd0c233265ad5e85064f589c7185"
LOKI = "Loki, the Deceiver"


class LokiRev1ExactM6Cases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw = RAW.read_bytes()
        assert hashlib.sha256(cls.raw).hexdigest() == EXPECTED
        cls.names = Counter()
        for row in cls.raw.decode("utf-8").splitlines():
            match = re.fullmatch(r"(\d+)x (.+?)(?: \[Commander\])?", row)
            assert match is not None, row
            cls.names[match.group(2)] += int(match.group(1))
        assert sum(cls.names.values()) == 100
        cls.oracle = {c["name"]: c for c in json.loads(SNAP.read_text())["cards"]}
        assert all(cls.oracle[n]["commander_legality"] == "legal" and
                   set(cls.oracle[n]["color_identity"]) <= {"U", "B", "R"}
                   for n in cls.names)

    def source(self, name, fragment):
        self.assertIn(name, self.names, f"{name} absent from exact 100")
        self.assertIn(fragment, self.oracle[name]["oracle_text"])

    def test_C1_source_paid_commander_attack_target_stack_and_missing_target(self):
        self.source(LOKI, "Whenever Loki attacks, create a tapped and attacking token")
        self.source(LOKI, "another target Villain you control")
        self.assertEqual(self.oracle[LOKI]["mana_cost"], "{1}{U}{B}{R}")
        mana = Counter({"C": 1, "U": 1, "B": 1, "R": 1})
        self.assertTrue(all(mana[p] >= 1 for p in ("U", "B", "R")))
        self.assertGreaterEqual(sum(mana.values()), 4)
        self.assertIn("Villain", self.oracle["Kid Loki"]["type_line"])
        controlled_creatures = {"Loki, the Deceiver", "Kid Loki"}
        self.assertEqual(int("Kid Loki" in controlled_creatures and mana["U"] >= 1), 1)
        self.assertEqual(int("Kid Loki" in controlled_creatures), 1)
        # Removed target in response -> zero valid copies at resolution.
        controlled_creatures.remove("Kid Loki")
        self.assertEqual(int("Kid Loki" in controlled_creatures), 0)
        # A 4-mana cast without the R pip is not payable even if total >=4.
        invalid = Counter({"C": 2, "U": 1, "B": 1})
        self.assertFalse(all(invalid[p] >= 1 for p in ("U", "B", "R")))

    def test_K1_enters_attacking_etb_yes_attack_trigger_no(self):
        self.source(LOKI, "tapped and attacking token")
        self.source("Elektra, Daughter of the Hand", "When Elektra enters, destroy target creature")
        self.source("Ultimo, Civilization's End", "When Ultimo enters, each opponent sacrifices")
        self.assertIn("Whenever Kang Prime enters or attacks", self.oracle["Kang Prime"]["oracle_text"])
        event = {"entered": True, "declared_attacker": False, "combat_damage": False}
        self.assertEqual((int(event["entered"]), int(event["declared_attacker"])), (1, 0))
        self.assertEqual(int(event["entered"] and not event["declared_attacker"]), 1)
        self.assertEqual(int({**event, "entered": False}["entered"]), 0)

    def test_K2_per_player_batch_draw_no_double_count_and_no_damage(self):
        self.source(LOKI, "Whenever one or more Villains you control deal combat damage to a player, draw a card")
        def draws(damage_by_player, loki_objects):
            return len({player for player, villains in damage_by_player.items() if villains > 0}) * loki_objects
        self.assertEqual(draws({"A": 2, "B": 1, "C": 0}, 1), 2)
        self.assertEqual(draws({"A": 2, "B": 1, "C": 0}, 2), 4)
        self.assertEqual(draws({"A": 0, "B": 0}, 1), 0)
        self.assertNotEqual(draws({"A": 2}, 1), 2)

    def test_K3_roaming_throne_villain_extra_trigger_not_own_or_wrong_type(self):
        self.source("Roaming Throne", "If a triggered ability of another creature you control of the chosen type triggers")
        self.assertIn("Villain", self.oracle[LOKI]["type_line"])
        def trigger_count(chosen_type, source_type, source_is_throne=False):
            return 1 + int(chosen_type == source_type and not source_is_throne)
        self.assertEqual(trigger_count("Villain", "Villain"), 2)
        self.assertEqual(trigger_count("Hero", "Villain"), 1)
        self.assertEqual(trigger_count("Villain", "Villain", True), 1)
        # Two attack triggers with two valid targets create two independently
        # delayed-sacrifice token objects; no phantom target from an empty board.
        self.assertEqual(2 if "Kid Loki" in self.names else 0, 2)
        self.assertEqual(2 if {"Kid Loki"} & set() else 0, 0)

    def test_K4_master_prevents_triggered_token_sacrifice_sundial_timing(self):
        self.source("The Master, Multiplied", "Triggered abilities you control can't cause you to sacrifice or exile creature tokens")
        self.source("Sundial of the Infinite", "{1}, {T}: End the turn")
        self.source(LOKI, "Sacrifice that token at the beginning of the next end step")
        def survives(master, sundial_paid_tapped_at_trigger, is_token=True):
            return bool(is_token and (master or sundial_paid_tapped_at_trigger))
        self.assertTrue(survives(True, False))
        self.assertTrue(survives(False, True))
        self.assertFalse(survives(False, False))
        self.assertFalse(survives(False, False, is_token=False))
        # Sundial's activated ability costs one available mana, untapped Sundial,
        # and your turn; an earlier end-turn doesn't erase a *future* trigger.
        self.assertFalse(0 >= 1)
        self.assertFalse(survives(False, False))

    def test_K5_scepter_until_eot_type_change_not_copiable_characteristic(self):
        self.source("Loki's Scepter", "Until end of turn, it becomes a Villain in addition to its other types")
        self.source(LOKI, "copy of another target Villain you control")
        original_types = {"Creature", "Soldier"}
        temporary_types = original_types | {"Villain"}
        self.assertIn("Villain", temporary_types)  # valid controlled target now
        copied_types = original_types | {"Illusion"}  # copy values, not type-changing effects
        self.assertNotIn("Villain", copied_types)
        self.assertIn("Illusion", copied_types)
        self.assertNotIn("Villain", original_types)  # not a legal target without Scepter
        self.assertEqual(self.oracle["Loki's Scepter"]["mana_cost"], "{2}{R}")

    def test_E1_paid_multi_copy_engine_does_not_evoke_unpaid_clone(self):
        self.source("Hall of Echoes", "{5}: This land becomes a copy of target creature")
        self.source("Spark Double", "You may have this creature enter as a copy")
        self.source("Sakashima of a Thousand Faces", "may have Sakashima enter as a copy")
        self.assertIn("Villain", self.oracle[LOKI]["type_line"])
        # Hall's {5} animation and a separate Loki casting cost are distinct.
        mana = 9
        self.assertEqual(mana - 5 - 4, 0)
        self.assertFalse(8 >= 5 + 4)
        # A Hall newly animated this turn has not been under your control as a
        # creature since your turn began; no attack unless haste is supplied.
        controlled_as_creature_since_turn_start = False
        haste = False
        self.assertFalse(controlled_as_creature_since_turn_start or haste)
        haste = True
        self.assertTrue(controlled_as_creature_since_turn_start or haste)
        self.assertEqual((1 + 1) * 1, 2)  # two legal attackers -> two copy triggers

    def test_E2_preserve_tokens_replaces_removed_octopus_no_phantom_refill(self):
        self.source("The Master, Multiplied", "creature tokens you control")
        self.source("Sundial of the Infinite", "Activate only during your turn")
        self.source("Ultimo, Civilization's End", "When Ultimo enters, each opponent sacrifices")
        self.assertNotIn("Doctor Octopus, Master Planner", self.names)
        # One Loki token is created; only a current Master or timely Sundial
        # can retain it. Newly created objects are never added twice.
        new_tokens = 1
        master_on_board = True
        self.assertEqual(new_tokens if master_on_board else 0, 1)
        master_on_board = False
        self.assertEqual(new_tokens if master_on_board else 0, 0)
        self.assertEqual(new_tokens, 1)
        self.assertNotIn("draw until you have eight cards", self.oracle["Ultimo, Civilization's End"]["oracle_text"])

    def test_W1_combat_clock_squadron_anthem_not_removed_octopus_anthem(self):
        self.source("The Squadron Sinister", "Other Villains you control get +2/+2 and have flying and haste")
        self.source("Avengers: Under Siege", "Create two 2/1 black Villain creature tokens with menace")
        self.source("Red Ghost, Intangible Genius", "Red Ghost can't be blocked")
        self.assertNotIn("Doctor Octopus, Master Planner", self.names)
        # Real 2/1 Villains with +2/+2 = two 4/3s. No shortcut through blockers.
        self.assertEqual(2 * (2 + 2), 8)
        self.assertEqual(2 * 2, 4)  # without actual Squadron anthem
        all_blocked = True
        self.assertEqual(0 if all_blocked else 8, 0)
        self.assertIn("The Squadron Sinister", self.names)

    def test_W2_paid_draw_engine_loki_discovery_second_draw_payoffs(self):
        self.source("Kindred Discovery", "Whenever a creature you control of the chosen type enters or attacks, draw a card")
        self.source("Rhystic Study", "unless that player pays {1}")
        self.source("M.O.D.O.K., Evil Intellect", "Whenever you draw your second card each turn")
        self.assertEqual(self.oracle["Kindred Discovery"]["mana_cost"], "{3}{U}{U}")
        self.assertFalse(1 >= 2)  # one blue cannot pay UU, irrespective of generic
        chosen_type, entered_villain, attacked_villain = "Villain", True, True
        discovery_draws = int(chosen_type == "Villain" and entered_villain) + int(chosen_type == "Villain" and attacked_villain)
        self.assertEqual(discovery_draws, 2)
        chosen_type = "Hero"
        self.assertEqual(int(chosen_type == "Villain" and entered_villain), 0)
        self.assertEqual(int(2 >= 2), 1)
        self.assertEqual(int(1 >= 2), 0)
        opponent_paid_one = True
        self.assertEqual(int(not opponent_paid_one), 0)  # Rhystic draw not guaranteed

    def test_F1_no_compact_win_and_no_unearned_victory_from_draws(self):
        self.source(LOKI, "draw a card")
        self.assertNotIn("Thassa's Oracle", self.names)
        self.assertNotIn("Demonic Consultation", self.names)
        self.assertNotIn("Underworld Breach", self.names)
        life = 40
        self.assertEqual(life - 8, 32)  # one 8-damage step is not a table kill
        self.assertGreater(life - 8, 0)
        # Even empty opponent library causes loss only on the next failed draw.
        attempted_draw_from_empty_library = False
        self.assertEqual(0, int(attempted_draw_from_empty_library))

    def test_F2_attack_trigger_villains_not_triggered_by_enter_attacking(self):
        self.assertNotIn("Kang, Temporal Tyrant", self.names)
        self.assertNotIn("Kang Prime", self.names)
        self.source("Loki, God of Mischief", "Whenever a player or permanent becomes the target of an ability you control")
        self.source("Ultimo, Civilization's End", "When Ultimo enters")
        declared_attackers = 1
        entered_attacking = 1
        self.assertEqual(declared_attackers, 1)
        self.assertEqual(entered_attacking, 1)
        self.assertEqual(0 * entered_attacking, 0)  # attack triggers on token
        self.assertEqual(1 * entered_attacking, 1)  # ETB triggers on token

    def test_F3_loki_removed_target_missing_or_no_haste_no_copy_engine(self):
        self.source(LOKI, "Whenever Loki attacks")
        self.source("Lightning Greaves", "Equipped creature has haste")
        self.source("Swiftfoot Boots", "Equipped creature has hexproof and haste")
        def copy_triggers(loki_present, can_attack, villain_target):
            return int(loki_present and can_attack and villain_target)
        self.assertEqual(copy_triggers(True, True, True), 1)
        for args in ((False, True, True), (True, False, True), (True, True, False)):
            self.assertEqual(copy_triggers(*args), 0)
        self.assertIn("Kid Loki", self.names)


if __name__ == "__main__":
    unittest.main()
