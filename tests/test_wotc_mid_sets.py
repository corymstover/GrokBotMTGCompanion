"""Regression tests for all 81 2003–2022 primary-sourced release candidates."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
import audit_wotc_mid_sets as M


class MiddleEraSetsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.evidence = json.loads(M.EVIDENCE.read_text(encoding="utf-8"))
        cls.catalog = json.loads(M.CATALOG.read_text(encoding="utf-8"))
        cls.early = json.loads(M.EARLY.read_text(encoding="utf-8"))
        cls.recent = json.loads(M.RECENT.read_text(encoding="utf-8"))

    def verify(self, evidence=None):
        return M.build(evidence or self.evidence, self.catalog, self.early, self.recent)

    def test_full_candidate_partition_is_complete_but_not_premier_census(self):
        output = self.verify()
        self.assertEqual(output['period_candidates'], 81)
        self.assertEqual(output['period_reviewed_regular_expansion_core'], 80)
        self.assertEqual(output['period_integrated_bonus_sheets'], 1)
        self.assertEqual(len(output['records']), 81)
        totals = output['combined_candidate_classification']
        self.assertEqual((totals['scryfall_released_nondigital_expansion_core'],
                          totals['wotc_supported_historical_regular_or_mainline_releases'],
                          totals['directly_sourced_auxiliary_discarded_or_integrated_sheets'],
                          totals['provisional_border_language_variants']), (142, 136, 4, 2))
        self.assertEqual(totals['wholly_unreviewed_within_this_142_code_scope'], 0)
        self.assertFalse(totals['all_time_premier_status_certified'])

    def test_timeshifted_and_released_core_sets_not_miscounted(self):
        records = {x['code']: x for x in self.verify()['records']}
        self.assertFalse(records['tsb']['counted_as_historical_mainline'])
        self.assertTrue(records['tsp']['counted_as_historical_mainline'])
        self.assertEqual(records['tsb']['classification'], M.BONUS)
        self.assertEqual(records['tsb']['evidence_level'], 'Wizards_explicit_bonus_sheet_description')
        for code in ('8ed', '9ed', '10e', 'm10', 'm21', 'afr', 'bro'):
            self.assertTrue(records[code]['counted_as_historical_mainline'])
        self.assertEqual(records['9ed']['scryfall_type'], 'core')

    def test_tampered_sources_or_missing_records_fail(self):
        x = copy.deepcopy(self.evidence)
        x['records'][0]['source'] = 'https://example.com/set'
        with self.assertRaisesRegex(ValueError, 'primary source'):
            self.verify(x)
        x = copy.deepcopy(self.evidence)
        x['records'] = x['records'][:-1]
        with self.assertRaisesRegex(ValueError, 'Unreviewed middle-era'):
            self.verify(x)
        x = copy.deepcopy(self.evidence)
        row = next(x for x in x['records'] if x['code'] == 'tsb')
        row['claim'] = M.REGULAR
        with self.assertRaisesRegex(ValueError, 'Unsupported mainline'):
            self.verify(x)

    def test_repeatability_and_earlier_records_preserved(self):
        self.assertEqual(M.encode(self.verify()), M.encode(self.verify()))
        self.assertEqual(self.early["period_reviewed_regular_mainline"], 35)
        self.assertEqual(self.recent["summary"]["wotc_reviewed_released_main_set_codes_2023_2026"], 21)


if __name__ == '__main__':
    unittest.main()
