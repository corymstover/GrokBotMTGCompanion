"""Primary-source set taxonomy audit regressions; no network needed."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
import audit_wotc_premier_sets as W


class WotcPremierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.evidence = json.loads(W.EVIDENCE.read_text(encoding='utf-8'))
        cls.catalog = json.loads(W.CATALOG.read_text(encoding='utf-8'))

    def test_reviewed_2023_2026_count_is_not_all_time_census(self):
        result = W.build(self.evidence, self.catalog)
        summary = result['summary']
        self.assertEqual(summary['all_scryfall_set_codes'], 1062)
        self.assertEqual(summary['wotc_reviewed_codes'], 30)
        self.assertEqual(summary['wotc_reviewed_released_main_set_codes_2023_2026'], 21)
        self.assertEqual(summary['scryfall_released_nondigital_expansion_core_candidates_all_history'], 142)
        self.assertEqual(summary['reviewed_expansion_core_auxiliary_not_a_main_release'], 2)
        self.assertEqual(summary['unreviewed_released_nondigital_expansion_core_candidates'], 119)
        self.assertIn('not the all-time premier', result['caveats'][0])

    def test_expansion_exceptions_and_future_remain_separate(self):
        result = W.build(self.evidence, self.catalog)
        rows = {v['code']: v for v in result['reviewed']}
        for code in ('mat', 'big', 'om1', 'trk', 'mdd', 'mh3'):
            self.assertFalse(rows[code]['count_as_reviewed_main_release_by_cutoff'])
        self.assertTrue(rows['fdn']['count_as_reviewed_main_release_by_cutoff'])
        self.assertEqual(rows['fdn']['scryfall_type'], 'core')
        self.assertEqual(rows['om1']['scryfall_digital'], True)
        self.assertEqual(rows['trk']['publication_status'], 'future')
        self.assertEqual(len(result['unreviewed_released_nondigital_expansion_core_codes']), 119)

    def test_tampering_fails_before_publishing(self):
        sample = copy.deepcopy(self.evidence)
        sample['records'][0]['source'] = 'https://example.com/guess'
        with self.assertRaisesRegex(ValueError, 'Non-Wizards'):
            W.build(sample, self.catalog)
        sample = copy.deepcopy(self.evidence)
        sample['records'].append(copy.deepcopy(sample['records'][0]))
        with self.assertRaisesRegex(ValueError, 'Duplicate'):
            W.build(sample, self.catalog)
        sample = copy.deepcopy(self.evidence)
        item = next(v for v in sample['records'] if v['code'] == 'trk')
        item['group'] = 'official_main_set_release'
        with self.assertRaisesRegex(ValueError, 'Main release has inconsistent'):
            W.build(sample, self.catalog)

    def test_commit_replay_matches_exact_generated_bytes(self):
        self.assertEqual(W.encoding(W.build(self.evidence, self.catalog)),
                         W.encoding(W.build(self.evidence, self.catalog)))


if __name__ == '__main__':
    unittest.main()
