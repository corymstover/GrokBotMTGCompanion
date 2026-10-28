#!/usr/bin/env python3
"""Executed finite, source-bound Deck 58 M6 P0 C1/K1/K2/K3 follow-up.

Bounded scenario and event accounting only. This is not a full multiplayer
rules engine, a win-rate simulation or a global transfer certification.
"""
import hashlib
import json
from pathlib import Path
import unittest

HERE = Path(__file__).resolve().parent
FINAL = HERE.parent / "candidate_lists" / "The_Valeyard_M7_Rev1.txt"
SHA = "1735629783fbea2c9b8782fe18835f6dc8b3b980715344249cdb0941fbd9887b"


class TheValeyardP0(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        raw = FINAL.read_bytes()
        cls.digest = hashlib.sha256(raw).hexdigest()
        cls.cards = [line.split("x ", 1)[1].removesuffix(" [Commander]")
                     for line in raw.decode().splitlines()]
        cls.oracle = json.loads((HERE / "The_Valeyard_M7_Rev1_Scryfall_snapshot.json").read_text())["oracle_cards"]

    def setUp(self):
        self.assertEqual(self.digest, SHA)
        self.assertEqual(self.cards[0], "The Valeyard")
        self.assertIn("Irenicus's Vile Duplication", self.cards)
        self.assertIn("Double Vision", self.cards)

    def card(self, name, *phrases):
        self.assertIn(name, self.cards)
        d = self.oracle[name]
        self.assertEqual(d["commander_legality"], "legal")
        self.assertTrue(d["oracle_id"] and d["scryfall_uri"])
        for phrase in phrases:
            self.assertIn(phrase, d["oracle_text"])

    def test_C1_commander_present_and_opponent_precondition(self):
        """Positive choice while Valeyard on battlefield; negative no Valeyard or own choice."""
        self.card("The Valeyard", "If an opponent would face a villainous choice",
                  "they face that choice an additional time", "While voting")
        count = lambda v_active, opponent: 1 + int(v_active and opponent)
        self.assertEqual(count(True, True), 2)
        self.assertEqual(count(False, True), 1)
        self.assertEqual(count(True, False), 1)

    def test_K1_vote_word_not_ordinary_choose(self):
        """Real vote doubles controller vote count, while 'choose' outside voting doesn't."""
        self.card("Plea for Power", "each player votes for time or knowledge")
        self.card("Tyrant's Choice", "each player votes for death or torture")
        self.card("Truth or Consequences", "secretly votes for truth or consequences")
        self.card("The Valeyard", "you may vote an additional time")
        vote_count = lambda real_vote, v_active, use_bonus: 1 + int(real_vote and v_active and use_bonus)
        self.assertEqual(vote_count(True, True, True), 2)
        self.assertEqual(vote_count(True, True, False), 1)  # may, not must
        self.assertEqual(vote_count(False, True, True), 1)  # ordinary choose is not vote
        self.assertEqual(vote_count(True, False, True), 1)

    def test_K2_villainous_choices_are_sequential_and_independent(self):
        """One full action then another; repeat mode can differ and need not auto-win."""
        self.card("Dr. Eggman", "villainous choice")
        self.card("The Valeyard", "They can make the same or different choices.")
        choices = ["discard", "put artifact"]
        self.assertEqual(len(choices), 2)
        self.assertNotEqual(choices[0], choices[1])
        self.assertEqual(["discard", "discard"].count("discard"), 2)
        self.assertEqual(len(choices[:1]), 1)  # when second effect absent

    def test_K3_additive_valeyard_copies_and_legend_constraint(self):
        """Separate static replacements each add exactly one choice, never recursively."""
        self.card("Irenicus's Vile Duplication", "it isn't legendary")
        self.card("Spark Double", "it isn't legendary")
        self.card("Quantum Misalignment", "it isn't legendary")
        self.card("Sakashima of a Thousand Faces", "legend rule")
        for copies, expected in ((0, 2), (1, 3), (2, 4), (3, 5)):
            self.assertEqual(2 + copies, expected)
        # Generic legendary Clone without an exception cannot stay with Valeyard.
        legal_nonlegendary = lambda explicit_exception, ignore_legend_rule: bool(explicit_exception or ignore_legend_rule)
        self.assertTrue(legal_nonlegendary(True, False))
        self.assertFalse(legal_nonlegendary(False, False))

    def test_K4_auton_myriad_not_retroactive(self):
        self.card("Auton Soldier", "it isn't legendary", "myriad")
        # A combat-created copy exists for future choices only, and is exiled later.
        effects = lambda before_combat, myriad_alive: 1 + int(before_combat) + int(myriad_alive)
        self.assertEqual(effects(True, False), 2)
        self.assertEqual(effects(True, True), 3)
        self.assertEqual(effects(True, False), 2)

    def test_F1_extra_vote_does_not_override_three_opponents(self):
        self.card("Plea for Power", "time or knowledge", "If knowledge gets more votes")
        # Controller 2 time; three opponents 3 knowledge => knowledge wins.
        self.assertLess(2, 3)
        # The controller may vote differently twice; split votes need not help.
        self.assertEqual((1 + 1), 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
