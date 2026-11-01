"""Acceptance for K054: publication chronology and cited fictional chronology are distinct axes."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import mv_ask  # noqa: E402


class DualTimelineAcceptance(unittest.TestCase):
    def test_all_twelve_official_series_keep_independent_axes(self):
        bridge = json.loads((ROOT / 'data/set_atlas/phase1b_release_scope_story_bridge_2026-10-29.json')
                            .read_text(encoding='utf-8'))
        ledgers = [json.loads((ROOT / path).read_text(encoding='utf-8'))
                   for path in ('data/lore_research/relative_chronology_2026-10-30.json',
                                'data/lore_research/source_event_sequences_2026-10-30.json')]
        proof_count = 0
        for code in bridge['wizards_story_series_set_links']:
            with self.subTest(code=code):
                result = mv_ask.ask('Compare the release and lore timelines for ' + code)
                self.assertEqual(result['route'], 'ask->set_atlas:dual_timeline')
                self.assertEqual(result['confidence'], 'QUALIFIED')
                axes = result['result']['two_chronology_axes']
                self.assertEqual(axes['real_world_set_release'],
                                 bridge['set_scope_records'][code]['released_at'])
                self.assertIsNone(axes['fictional_event_date_corresponding_to_set_release'])
                self.assertEqual(axes['release_vs_fictional_event_order'],
                                 'NOT_COMPARABLE_DIFFERENT_CHRONOLOGY_AXES')
                self.assertIn('NO_REAL_WORLD_TO_FICTIONAL_TIME_CONVERSION', result['flags'])
                pages = {p['url'] for p in bridge['wizards_story_series_set_links'][code]
                         ['sample_first_party_story_sources']}
                expected_edges = [e for ledger in ledgers
                                  for e in (ledger['stated_edges'] if 'stated_edges' in ledger else ledger['edges'])
                                  if e.get('source_url') in pages]
                self.assertEqual(axes['cited_in_universe_relations_total'], len(expected_edges))
                proof_count += len(expected_edges)
                for edge in axes['in_universe_relations_on_exact_linked_pages']:
                    self.assertIn(edge['source_url'], pages)
                    self.assertIn(edge['source_url'], result['sources'])
                    self.assertIn(edge['relation'], {'BEFORE', 'AFTER', 'SAME_TIME_AS_LABEL',
                                                    'OVERLAPS', 'SAME_EVENT'})
        # An actual citation-backed bridge must exist; a zero-proof join is
        # merely a pair of unrelated datasets and cannot close K054.
        self.assertGreaterEqual(proof_count, 3)

    def test_k054_checked_but_source_and_release_gaps_are_not(self):
        import audit_full_checklist
        rows = audit_full_checklist.items()
        item = [r for r in rows if r['task'].startswith('Maintain two separately labeled timelines')]
        self.assertEqual(len(item), 1)
        self.assertTrue(item[0]['checked'])
        self.assertTrue(all(not r['checked'] for r in rows
                            if r['section'].startswith('Definition of the first major')))
        self.assertTrue(all(not r['checked'] for r in rows if r['section'].startswith('Phase 6')))


if __name__ == '__main__':
    unittest.main()
