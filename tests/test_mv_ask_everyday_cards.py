"""Everyday card questions must not be mistaken for nonexistent card names.

Snapshot legality is never presented as a real-time Commander ban check.
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import mv_ask


class EverydayCardQuestions(unittest.TestCase):
    def test_ban_question_uses_dated_legality_not_lore_fallback(self):
        result = mv_ask.ask('Is Sol Ring banned in Commander?')
        self.assertEqual(result['route'], 'ask->commander_format')
        self.assertEqual(result['confidence'], 'QUALIFIED')
        self.assertFalse(result['result']['is_banned_in_snapshot'])
        self.assertEqual(result['result']['scryfall_commander_legality'], 'legal')
        self.assertIn('DATED_SCRYFALL_LEGALITY_NOT_LIVE', result['flags'])
        self.assertTrue(any('scryfall.com/card/' in s for s in result['sources']))

    def test_banned_card_is_not_declared_playable(self):
        result = mv_ask.ask('Is Griselbrand legal in Commander?')
        self.assertEqual(result['route'], 'ask->commander_format')
        self.assertFalse(result['result']['format_legal_in_snapshot'])
        self.assertEqual(result['result']['scryfall_commander_legality'], 'banned')

    def test_generic_deck_question_does_not_invent_a_commander(self):
        result = mv_ask.ask('Can Sol Ring be in a Commander deck?')
        self.assertEqual(result['route'], 'ask->commander_format')
        self.assertTrue(result['result']['can_be_in_some_commander_deck_in_snapshot'])
        self.assertIn('COMMANDER_IDENTITY_NOT_SPECIFIED', result['flags'])
        self.assertNotIn('commander_configuration', result['result'])

    def test_specific_commander_uses_actual_deck_checker(self):
        result = mv_ask.ask('Can I put Sol Ring in my Krark, the Thumbless deck?')
        self.assertEqual(result['route'], 'ask->rules:include')
        self.assertTrue(result['result']['allowed'])
        self.assertEqual(result['result']['card'], 'Sol Ring')

    def test_oracle_prose_uses_exact_card_data(self):
        for question in ('What does Sol Ring do?', 'How much mana does Sol Ring cost?',
                         'What is the Oracle text of Sol Ring?'):
            with self.subTest(question=question):
                result = mv_ask.ask(question)
                self.assertEqual(result['route'], 'ask->card')
                self.assertEqual(result['result']['name'], 'Sol Ring')
                self.assertEqual(result['result']['oracle_text'], '{T}: Add {C}{C}.')

    def test_unknown_card_never_responds_with_a_guessed_legality(self):
        result = mv_ask.ask('Is Zorblax the Unreal banned in Commander?')
        self.assertEqual(result['confidence'], 'NOT_FOUND')


if __name__ == '__main__':
    unittest.main()
