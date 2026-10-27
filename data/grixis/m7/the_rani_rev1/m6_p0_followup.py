#!/usr/bin/env python3
"""Executed, source-bound finite M6 P0 follow-up for approved Deck #57.

Cases C1/K1/K2/K3/F1 map to immutable The_Rani M6 blueprint. This
performs bounded state and trigger accounting, *not* a full Magic rules engine.
All cases pin the complete exact approved list and the captured Oracle source.
"""

import hashlib
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent
APPROVED_SHA = '924296ed24fdc5e79431821d31a77134c5ed5c089a92cb5e69c78f78bde4fe27'
CASE_IDS = ('C1', 'K1', 'K2', 'K3', 'F1')


class SourceBoundRaniP0(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        candidate_dir = (ROOT.parent / 'candidate_lists' if (ROOT.parent / 'candidate_lists').is_dir() else ROOT)
        approved = candidate_dir / 'The_Rani_M7_Rev1.txt'
        cls.raw = approved.read_bytes()
        cls.cards = [name.removesuffix(' [Commander]')
                     for line in cls.raw.decode().splitlines()
                     for qty, name in [re.fullmatch(r'(\d+)x (.+)', line).groups()]
                     for _ in range(int(qty))]
        cls.snapshot = json.loads((ROOT / 'The_Rani_M7_Rev1_Scryfall_snapshot.json').read_text())
        cls.oracle = cls.snapshot['cards']

    def setUp(self):
        self.assertEqual(hashlib.sha256(self.raw).hexdigest(), APPROVED_SHA)
        self.assertEqual(len(self.cards), 100)
        self.assertEqual(self.cards[0], 'The Rani')

    def oracle_has(self, name, *phrases):
        self.assertIn(name, self.cards)
        record = self.oracle[name]
        self.assertEqual(record['commander_legality'], 'legal')
        self.assertTrue(record['oracle_id'] and record['scryfall_uri'])
        for phrase in phrases:
            self.assertIn(phrase, record['oracle_text'])

    @staticmethod
    def legal_mark_target(rani_id, creature_id, hexproof_to_us=False):
        return creature_id is not None and creature_id != rani_id and not hexproof_to_us

    def test_C1_rani_marks_and_damage_gated_investigate(self):
        """Positive: another target is marked by ETB/attack; goaded combat connects.

        Adversarial: cannot target self/absent/hexproof, and connecting to own
        player or noncombat damage does not trigger investigation.
        """
        self.oracle_has('The Rani', 'Whenever The Rani enters or attacks',
                        'another target creature', 'Enchanted creature gets +2/+2 and is goaded',
                        'Whenever a goaded creature deals combat damage to one of your opponents')
        self.assertTrue(self.legal_mark_target('rani-1', 'opposing-1'))
        for candidate, protected in [('rani-1', False), (None, False), ('enemy', True)]:
            self.assertFalse(self.legal_mark_target('rani-1', candidate, protected))
        trigger = lambda goaded, combat, opponent: int(goaded and combat and opponent)
        self.assertEqual(trigger(True, True, True), 1)
        self.assertEqual(trigger(True, False, True), 0)
        self.assertEqual(trigger(False, True, True), 0)
        self.assertEqual(trigger(True, True, False), 0)

    def test_K1_manufactor_erdwal_first_investigation(self):
        """Positive: first investigate plus Erdwal yields six total artifact tokens.

        Adversarial: subsequent investigate same turn yields only three, and
        without Manufactor they are two Clues, not six artifacts.
        """
        self.oracle_has('The Rani', 'investigate.')
        self.oracle_has('Academy Manufactor', 'instead create one of each')
        self.oracle_has('Erdwal Illuminator', 'the first time each turn',
                        'investigate an additional time')
        investigations = lambda is_first: 1 + int(is_first)
        artifacts = lambda first, manufactor: investigations(first) * (3 if manufactor else 1)
        self.assertEqual(artifacts(True, True), 6)
        self.assertEqual(artifacts(False, True), 3)
        self.assertEqual(artifacts(True, False), 2)
        self.assertEqual(artifacts(False, False), 1)

    def test_K2_thassa_exile_return_new_rani_mark(self):
        """Positive: legal controlled Rani flicker yields a new enter trigger.

        Adversarial: Thassa's target must be another controlled creature,
        its trigger is optional, and Rani's Mark still needs another target.
        """
        self.oracle_has('Thassa, Deep-Dwelling', 'At the beginning of your end step',
                        'up to one other target creature you control',
                        'return that card to the battlefield under your control')
        self.oracle_has('The Rani', 'Whenever The Rani enters or attacks', 'another target creature')
        def mark_after_end_step(blink_selected, controlled_rani, other_mark_target):
            return int(blink_selected and controlled_rani and other_mark_target)
        self.assertEqual(mark_after_end_step(True, True, True), 1)
        self.assertEqual(mark_after_end_step(False, True, True), 0)
        self.assertEqual(mark_after_end_step(True, False, True), 0)
        self.assertEqual(mark_after_end_step(True, True, False), 0)

    def test_K3_mark_baeloth_threshold_is_strict_less_than(self):
        """Positive: +2/+2 Mark raises Baeloth's 2 power to 4 (toughness 5->7).

        Adversarial: a 4-power or 5-power opposing creature is not caught,
        nor is our own 3-power creature (opponents control restriction).
        """
        self.oracle_has('Baeloth Barrityl, Entertainer',
                        "Creatures your opponents control with power less than Baeloth Barrityl's power are goaded")
        self.oracle_has('The Rani', 'gets +2/+2 and is goaded')
        base_power, base_toughness = 2, 5
        buffed_power, buffed_toughness = base_power + 2, base_toughness + 2
        self.assertEqual((buffed_power, buffed_toughness), (4, 7))
        goaded = lambda power, opponent: opponent and power < buffed_power
        self.assertTrue(goaded(3, True))
        self.assertFalse(goaded(4, True))
        self.assertFalse(goaded(5, True))
        self.assertFalse(goaded(3, False))

    def test_F1_creature_light_or_protected_board_fails_mark(self):
        """Positive: a legal creature permits first Mark.

        Adversarial: empty board, self-only board, and hexproof-only board
        produce no valid 'another target', despite Rani entering/attacking.
        """
        self.oracle_has('The Rani', 'another target creature')
        self.assertTrue(self.legal_mark_target('rani', 'opponent-creature'))
        self.assertFalse(self.legal_mark_target('rani', None))
        self.assertFalse(self.legal_mark_target('rani', 'rani'))
        self.assertFalse(self.legal_mark_target('rani', 'opponent-creature', True))
        # Deck mitigation is source-bound, but conditional; it never makes a
        # nonexistent target legal or guarantees interaction will resolve.
        self.oracle_has('Swan Song', 'Counter target enchantment, instant, or sorcery spell')


if __name__ == '__main__':
    unittest.main(verbosity=2)
