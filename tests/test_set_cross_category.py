"""CI tests for source-backed cross-category Magic set taxonomy."""
import copy
import json
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'scripts'))
import audit_set_cross_category as A


class CrossCategoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.values = [json.loads(x.read_text(encoding='utf-8'))
                      for x in (A.CATALOG, A.EVIDENCE, A.EARLY, A.MID)]

    def test_all_codes_partition_and_review_scope(self):
        report = A.build(*self.values)
        a = report['all_code_census']
        self.assertEqual(a['total_all_scryfall_codes'], 1062)
        self.assertEqual(sum(a['status_exclusive_partitions'].values()), 1062)
        self.assertEqual(a['status_exclusive_partitions']['released_nondigital_expansion_core'], 142)
        self.assertEqual(a['status_exclusive_partitions']['released_nondigital_other_categories'], 848)
        self.assertEqual(report['reviewed_count'], 12)
        self.assertEqual(report['unreviewed_released_nondigital_other_category_codes'], 836)

    def test_known_modern_only_and_reprint_products(self):
        r = {x['code']:x for x in A.build(*self.values)['reviewed_non_expansion_core_products']}
        for code in ('mh1', 'mh2', 'mh3'):
            self.assertEqual(r[code]['product_group'], 'modern_horizons_supplemental')
        self.assertEqual(r['ltr']['product_group'], 'modern_legal_full_booster_not_2023_standard_premier')
        self.assertEqual(r['j22']['product_group'], 'jumpstart_special_product')
        self.assertEqual(r['cmm']['product_group'], 'masters_reprint_product')
        self.assertEqual(r['ltc']['scryfall_set_type'], 'commander')

    def test_foreign_black_border_remains_provisional(self):
        out = A.build(*self.values)
        self.assertEqual({x['code'] for x in out['localized_printing_variants']}, {'fbb', '4bb'})
        self.assertTrue(all(x['status'].endswith('primary_source_pending')
                            for x in out['localized_printing_variants']))

    def test_tamper_source_and_uncited_reclassification_fails(self):
        data = copy.deepcopy(self.values)
        data[1]['records'][0]['source'] = 'https://example.com/unsupported'
        with self.assertRaisesRegex(ValueError, 'not Wizards'):
            A.build(*data)
        data = copy.deepcopy(self.values)
        data[1]['localized_printing_leads'][0]['status'] = 'officially_certified'
        with self.assertRaisesRegex(ValueError, 'silently promoted'):
            A.build(*data)
        data = copy.deepcopy(self.values)
        data[1]['records'].pop()
        with self.assertRaisesRegex(ValueError, 'Missing official-source reviews'):
            A.build(*data)

    def test_repeatability(self):
        self.assertEqual(A.encode(A.build(*self.values)), A.encode(A.build(*self.values)))


if __name__ == '__main__':
    unittest.main()
