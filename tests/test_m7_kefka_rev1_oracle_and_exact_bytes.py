"""Fail-closed offline current-Oracle / exact-100 gate for Kefka's M7 Rev1.

Live Oracle evidence is pinned to its October 24 Scryfall collection retrieval.
This does not re-query the API or pretend to be a comprehensive rules engine.
"""

import hashlib
import json
import re
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = ROOT / 'data/grixis/m7/independent_candidates/Kefka__Court_Mage_M7_Rev1_Provisional_Unapproved_SHA14277f6e_20261024.txt'
FALLBACK = ROOT / 'data/grixis/m7/independent_candidates/Kefka__Court_Mage_M7_Sakashima_StepThrough_TwoSwap_Research_20261024.txt'
SNAPSHOT = ROOT / 'data/grixis/m7/independent_reviews/Kefka__Court_Mage_M7_Current_Scryfall_20261024.json'
SHA = '14277f6e9774c5ef02b4f92332b52684794367007abf81bc2d84ef7ad7bcaa7d'
COMMANDER = 'Kefka, Court Mage // Kefka, Ruler of Ruin'
ALLOWED = frozenset('BRU')


class ExactKefkaOracleAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.snapshot = json.loads(SNAPSHOT.read_text(encoding='utf-8'))
        # The approval artifact on GitHub has NO terminal LF. Local research
        # variants are otherwise identical, with exactly one terminal LF.
        if CANDIDATE.exists():
            cls.raw = CANDIDATE.read_bytes()
        else:
            research = FALLBACK.read_bytes()
            cls.raw = research[:-1] if research.endswith(b'\n') else research
        cls.lines = cls.raw.decode('utf-8').splitlines()

    def test_exact_raw_sha_and_strict_copy_paste_format(self):
        self.assertEqual(hashlib.sha256(self.raw).hexdigest(), SHA)
        self.assertFalse(self.raw.endswith(b'\n'))
        self.assertEqual(len(self.lines), 100)
        self.assertEqual(self.lines[0], f'1x {COMMANDER} [Commander]')
        for line in self.lines[1:]:
            self.assertRegex(line, r'^1x [^\[\]\r\n]+$')
        names = [re.sub(r' \[Commander\]$', '', line[3:]) for line in self.lines]
        self.assertEqual(len(set(names)), 100)

    def test_current_100_card_scryfall_identity_legality_and_color(self):
        self.assertEqual(self.snapshot['raw_candidate_sha256_no_terminal_lf'], SHA)
        self.assertIn('2026-10-24', self.snapshot['verified_utc'])
        self.assertEqual(self.snapshot['count'], 100)
        self.assertEqual(self.snapshot['distinct_count'], 100)
        self.assertEqual(self.snapshot['printed_lands'], 28)
        self.assertTrue(self.snapshot['official_commander_legal_all'])
        self.assertEqual(self.snapshot['project_exceptions'], [])
        self.assertEqual(set(self.snapshot['commander_identity']), ALLOWED)
        cards = {card['name']: card for card in self.snapshot['cards']}
        names = [re.sub(r' \[Commander\]$', '', line[3:]) for line in self.lines]
        self.assertEqual(set(cards), set(names))
        for name in names:
            card = cards[name]
            self.assertEqual(card['legalities_commander'], 'legal', name)
            self.assertTrue(card['oracle_id'], name)
            self.assertTrue(set(card['color_identity']) <= ALLOWED, name)
        self.assertEqual(sum('Land' in c['type_line'].split(' // ')[0].split(' — ')[0] for c in cards.values()), 28)

    def test_distinct_duties_and_owner_waiver_do_not_imply_approval(self):
        names = {re.sub(r' \[Commander\]$', '', line[3:]) for line in self.lines}
        self.assertTrue({'Step Through', 'Sakashima of a Thousand Faces'} <= names)
        self.assertTrue({'Demonic Counsel', 'Phyrexian Metamorph'}.isdisjoint(names))
        self.assertEqual(self.snapshot['owner_approval_status'], 'NOT_APPROVED')
        self.assertIn('SEPARATE', self.snapshot['mechanics_test_status'])


if __name__ == '__main__':
    unittest.main()
