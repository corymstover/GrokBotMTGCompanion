"""A passing foundation review packet may never imply actual certification."""
import json
import sys
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import build_foundation_acceptance_packet as P  # noqa: E402


class FoundationPacketTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.current = json.loads(P.OUT.read_text(encoding='utf-8'))

    def test_committed_copy_and_review_report_are_exactly_reproducible(self):
        self.assertEqual(self.current, P.build())
        self.assertEqual(P.REPORT.read_text(encoding='utf-8'), P.markdown(self.current))
        body = {k: v for k, v in self.current.items() if k != 'content_sha256'}
        self.assertEqual(self.current['content_sha256'], P.sha(body))
        for v in self.current['input_sha256'].values():
            self.assertEqual(len(v['sha256']), 64)

    def test_never_approves_owner_scope_or_decks(self):
        self.assertFalse(self.current['owner_accepted'])
        self.assertFalse(self.current['release_certified'])
        self.assertTrue(self.current['phase6_deckbuilding_deferred'])
        self.assertEqual(self.current['scope'], 'KNOWLEDGE_FOUNDATION_ONLY')
        self.assertIn('NOT_CERTIFICATION', self.current['status'])
        self.assertIn('PENDING', self.current['owner_review_status'])

    def test_partial_histories_and_two_distinct_chronology_ledgers(self):
        c = self.current['coverage']
        self.assertEqual(c['registered_character_nodes'] + c['registered_faction_nodes'],
                         c['characters_and_factions_with_direct_claims'] +
                         c['characters_and_factions_without_direct_claims'])
        self.assertEqual(c['source_pages_in_inventoried_scope'],
                         c['source_pages_cited'] + c['source_pages_reviewed_without_claim'])
        self.assertGreater(c['thin_plane_dossiers'], 0)
        ch = self.current['chronology']
        self.assertEqual(ch['legacy_unresolved_pairs'], ch['legacy_total_pairs'] - ch['legacy_ordered_pairs'])
        self.assertGreater(ch['legacy_unresolved_pairs'], 0)
        self.assertGreater(ch['legacy_disconnected_components'], 1)
        self.assertFalse(ch['l244_complete'])
        self.assertIn('may not be summed', ch['not_additive'].lower())
        self.assertEqual(c['characters_and_factions_without_direct_claims'], 0)
        self.assertEqual(c['registered_character_faction_direct_claim_gaps'], [])
        self.assertEqual(c['characters_and_factions_with_direct_claims'], 630)
        self.assertEqual(c['thin_plane_dossiers'], 12)

    def test_qa_sources_and_unknown_are_preserved(self):
        cases = {r['id']: r for r in self.current['representative_questions']}
        self.assertEqual(set(cases), {x[0] for x in P.QA_CASES})
        self.assertEqual(cases['unanchored_order']['chronology_relation'], 'UNKNOWN')
        self.assertEqual(cases['unanchored_order']['sources'], [])
        self.assertIn('NO_CITED_CHRONOLOGY_PATH', cases['unanchored_order']['flags'])
        self.assertIn('CURRENT_LEADER_NOT_ESTABLISHED', cases['present_leader_unknown']['flags'])
        self.assertIn('magic.wizards.com', cases['character_bolas']['sources'][0])
        self.assertEqual({key for key in cases if key.startswith('history_')},
                         {'history_eric', 'history_hazel', 'history_lyra',
                          'history_valentin', 'history_cabaretti'})
        self.assertEqual({key for key in cases if key.startswith('plane_')},
                         {'plane_alara', 'plane_argentum', 'plane_eldraine',
                          'plane_ikoria', 'plane_new_capenna'})
        self.assertTrue(any('media.wizards.com' in url for url in cases['commander_identity']['sources']))
        for r in cases.values():
            self.assertEqual(len(r['response_sha256']), 64)

    def test_cross_plane_paths_are_cited_but_not_time_proofs(self):
        paths = self.current['cross_plane_graph_navigation']
        self.assertEqual(len(paths), 2)
        for p in paths:
            self.assertEqual(p['evidence_type'], 'GRAPH_NAVIGATION_ONLY_NOT_TEMPORAL_OR_CAUSAL_PROOF')
            self.assertTrue(all(e['claim'] and e['source_urls'] for e in p['hops']))
            self.assertNotIn('chronological_order', p)

    def test_qa_drift_fails_closed(self):
        fake = {'route': 'ask->plane_history', 'confidence': 'VERIFIED'}
        with mock.patch.object(P.mv_ask, 'ask', return_value=fake):
            with self.assertRaisesRegex(ValueError, 'Q&A evidence drift'):
                P.qa_cases()


if __name__ == '__main__':
    unittest.main()
