import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import audit_lore_bloomburrow_duskmourn as A
import build_plane_history_dossiers as H


class BloomburrowDuskmournHistoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dossiers = {d['plane']:d for d in H.build()['planes']}
        cls.blh = json.loads(A.PACKS[0].read_text())
        cls.dh = json.loads(A.PACKS[1].read_text())

    def test_source_and_structure_audit(self):
        report = A.audit()
        self.assertEqual(report['claims'], 25)
        self.assertEqual(report['official_sources'], 3)

    def test_direct_plane_history_is_no_longer_thin(self):
        self.assertGreaterEqual(self.dossiers['Bloomburrow']['distinct_claims'], 5)
        self.assertGreaterEqual(self.dossiers['Duskmourn']['distinct_claims'], 5)

    def test_valley_history_keeps_legend_uncertainty(self):
        legend = self.blh['claims'][:11]
        self.assertTrue(all(c['grade'] == 'CANON_IMPLIED' for c in legend))
        self.assertIn('legend', next(c for c in legend if c['id'] == 'BLH003')['limitation'])

    def test_local_government_not_claimed_plane_wide(self):
        c = next(c for c in self.blh['claims'] if c['id'] == 'BLH013')
        self.assertEqual(c['subject'], 'valley')
        self.assertIn('not proof that the whole plane', c['limitation'])

    def test_duskmourn_original_name_and_origin_limits(self):
        name = next(c for c in self.dh['claims'] if c['id'] == 'DH001')
        self.assertIn('forgotten', name['predicate'])
        hints = next(c for c in self.dh['claims'] if c['id'] == 'DH002')
        self.assertEqual(hints['grade'], 'CANON_IMPLIED')

    def test_two_generations_is_quoted_relative_not_ar_year(self):
        d = json.loads((ROOT/'data/lore_research/in_universe_dates_2026-10-30.json').read_text())
        row = next(x for x in d['dates'] if x['claim'] == 'BLH005')
        self.assertEqual(row['value'], 'two generations')
        self.assertEqual(row['kind'], 'RELATIVE_SPAN')

    def test_history_qa_reports_qualification_not_exhaustiveness(self):
        for name in ('Bloomburrow', 'Duskmourn'):
            r = subprocess.run([sys.executable, 'scripts/mv_ask.py', 'ask', f'What is the history of {name}?'],
                               cwd=ROOT, capture_output=True, text=True, check=True)
            self.assertIn('QUALIFIED', r.stdout)
            self.assertIn('NO_VERIFIED_TOTAL_CHRONOLOGY', r.stdout)


if __name__ == '__main__':
    unittest.main()
