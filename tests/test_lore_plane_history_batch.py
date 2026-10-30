import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import audit_lore_plane_history_batch as AUDIT
import build_plane_history_dossiers as DOSSIERS
import mv_ask


class LorePlaneHistoryBatchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dossiers = DOSSIERS.build()
        cls.by_name = {row['plane']: row for row in cls.dossiers['planes']}

    def test_official_source_register_and_all_twenty_claims(self):
        self.assertEqual(AUDIT.audit()['claims'], 20)
        self.assertEqual(AUDIT.audit()['official_sources'], 3)

    def test_both_plane_histories_now_have_direct_claims(self):
        for name, expected in [('Kamigawa', 8), ('New Phyrexia', 9)]:
            self.assertGreaterEqual(self.by_name[name]['distinct_claims'], expected)
            self.assertTrue(all(f['sources'] for f in self.by_name[name]['facts']))

    def test_kamigawa_span_is_quoted_and_not_ar(self):
        dates = json.loads((ROOT / 'data/lore_research/in_universe_dates_2026-10-30.json').read_text())
        row = next(x for x in dates['dates'] if x['claim'] == 'KMH004')
        self.assertEqual(row['value'], '1,200 years ago')
        self.assertEqual(row['kind'], 'RELATIVE_SPAN')

    def test_new_phyrexia_does_not_claim_current_praetor_regime(self):
        nph = json.loads(AUDIT.NPH.read_text())
        row = next(x for x in nph['claims'] if x['id'] == 'NPHH007')
        self.assertIn('historical', row['limitation'])
        self.assertIn('early', row['event_stage'])

    def test_regenerated_dossiers_equal_committed_file(self):
        self.assertEqual(self.dossiers, json.loads(DOSSIERS.OUT.read_text()))
        self.assertEqual(self.dossiers['counts']['registered_planes'], 33)

    def test_plain_english_qa_remains_qualified(self):
        for name in ('Kamigawa', 'New Phyrexia'):
            run = subprocess.run([sys.executable, 'scripts/mv_ask.py', 'ask', f'What is the history of {name}?'],
                                 cwd=ROOT, capture_output=True, text=True, check=True)
            self.assertIn('QUALIFIED', run.stdout)
            self.assertIn('NO_VERIFIED_TOTAL_CHRONOLOGY', run.stdout)


if __name__ == '__main__':
    unittest.main()
