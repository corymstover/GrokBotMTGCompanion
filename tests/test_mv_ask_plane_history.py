import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import mv_ask  # noqa: E402


class PlaneHistoryQATests(unittest.TestCase):
    def test_alara_exact_citations_and_no_invented_complete_history(self):
        result = mv_ask.ask('What is the history of Alara?')
        self.assertEqual(result['route'], 'ask->plane_history')
        self.assertEqual(result['confidence'], 'QUALIFIED')
        self.assertIn('PARTIAL_REGISTERED_PLANE_HISTORY', result['flags'])
        self.assertEqual(result['result']['direct_claims'], 5)
        self.assertFalse(result['result']['complete_history'])
        self.assertFalse(result['result']['verified_total_chronology'])
        self.assertIn('https://magic.wizards.com/en/story/alara-plane', result['sources'])
        claims = result['result']['claims']
        self.assertEqual(len(claims), 5)
        shard = next(x for x in claims if x['claim_id'] == 'ALA001')
        self.assertEqual(len(shard['relations']), 5)
        self.assertEqual(len(shard['sources']), 1)

    def test_theros_six_direct_claims_preserve_prior_packs(self):
        result = mv_ask.ask('Tell me about the history of Theros')
        self.assertEqual(result['route'], 'ask->plane_history')
        self.assertEqual(result['result']['direct_claims'], 6)
        ids = {claim['claim_id'] for claim in result['result']['claims']}
        self.assertTrue({'THP001', 'THP002', 'THP010'} <= ids)
        self.assertTrue(all(claim['sources'] for claim in result['result']['claims']))

    def test_phyrexia_unresolved_claims_stay_qualified(self):
        result = mv_ask.ask('What happened on Phyrexia?')
        self.assertEqual(result['confidence'], 'QUALIFIED')
        self.assertIn('CANON_IMPLIED_PRESENT', result['flags'])
        self.assertIn('OPEN_QUESTION_PRESENT', result['flags'])
        self.assertNotIn('VERIFIED', result['confidence'])

    def test_unregistered_plane_falls_back_without_inventing_history(self):
        result = mv_ask.ask('What is the history of An Imaginary Plane?')
        self.assertEqual(result['confidence'], 'NOT_FOUND')
        self.assertNotEqual(result.get('route'), 'ask->plane_history')

    def test_generic_character_lore_unchanged(self):
        result = mv_ask.ask('What is the lore of Nicol Bolas?')
        self.assertNotEqual(result.get('route'), 'ask->plane_history')


if __name__ == '__main__':
    unittest.main()
