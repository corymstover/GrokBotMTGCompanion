"""Source-local timeline overviews preserve partial ordering and account identity."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from mv_ask import ask


class ChronologyOverviewTests(unittest.TestCase):
    def test_azorius_exact_source_local_chain(self):
        r = ask('Show timeline of Azorius')
        self.assertEqual((r['route'], r['confidence']),
                         ('ask->chronology_overview', 'QUALIFIED'))
        self.assertEqual(r['result']['strand']['id'], 'X')
        self.assertEqual((len(r['result']['events']), len(r['result']['strict_edges'])), (5, 4))
        self.assertEqual((r['result']['ordered_event_pairs'],
                          r['result']['possible_event_pairs'],
                          r['result']['unresolved_strict_pairs']), (10, 10, 0))
        self.assertTrue(r['result']['source_local_total_order'])
        self.assertFalse(r['result']['verified_total_chronology'])
        self.assertEqual(len(r['sources']), 3)
        self.assertTrue(all(e['quote'] and e['source_url'] in r['sources'] and
                            e['source_id'] for e in r['result']['strict_edges']))
        self.assertTrue(all(n['claims'] for n in r['result']['events']))
        self.assertIn('today', r['result']['limitation'].lower())

    def test_explicit_strand_id_and_natural_article(self):
        x = ask('Show chronology strand x?')
        self.assertEqual(x['result']['strand']['id'], 'X')
        g = ask('Show chronology of the Gatewatch')
        self.assertEqual(g['result']['strand']['id'], 'Z')
        self.assertEqual(len(g['result']['events']), 13)
        w = ask('Show chronology of the War of the Spark')
        self.assertEqual(w['confidence'], 'NOT_FOUND')
        self.assertIn('AMBIGUOUS_SOURCE_STRAND', w['flags'])
        self.assertEqual({s['id'] for s in w['result']['candidates']}, {'X', 'Y'})
        self.assertEqual(w['sources'], [])
        y = ask('Show chronology strand Y')
        self.assertEqual(y['result']['strand']['id'], 'Y')
        self.assertEqual(len(y['result']['events']), 11)
        self.assertFalse(y['result']['source_local_total_order'])
        bare = ask('Timeline of Azorius')
        self.assertEqual(bare['result']['strand']['id'], 'X')

    def test_mirrodin_has_two_unmerged_strands(self):
        r = ask('Show timeline of Mirrodin')
        self.assertEqual(r['confidence'], 'NOT_FOUND')
        self.assertIn('AMBIGUOUS_SOURCE_STRAND', r['flags'])
        self.assertEqual({s['id'] for s in r['result']['candidates']}, {'P', 'H'})
        self.assertEqual(r['sources'], [])
        self.assertEqual(r['result']['events'], [])
        self.assertEqual(ask('Show chronology strand P')['result']['strand']['id'], 'P')
        self.assertEqual(ask('Show chronology strand H')['result']['strand']['id'], 'H')

    def test_unknown_topic_and_strand_fail_closed(self):
        for question in ('Show timeline of Zorblax', 'Show chronology strand Q',
                         'Show timeline of Z'):
            with self.subTest(question=question):
                r = ask(question)
                self.assertEqual(r['confidence'], 'NOT_FOUND')
                self.assertIn('NO_MATCHING_SOURCE_STRAND', r['flags'])
                self.assertFalse(r['sources'])
                self.assertFalse(r['result']['events'])

    def test_legend_exposes_non_strict_overlap_and_unknown_pairs(self):
        r = ask('Show timeline of Bloomburrow Valley')
        self.assertEqual(r['result']['strand']['id'], 'V')
        self.assertEqual(r['confidence'], 'QUALIFIED')
        self.assertIn('NARRATED_LEGEND_NOT_VERIFIED_HISTORY', r['flags'])
        self.assertIn('NON_STRICT_TEMPORAL_RELATIONS_PRESENT', r['flags'])
        self.assertIn('UNRESOLVED_STRICT_EVENT_ORDER', r['flags'])
        self.assertEqual(r['result']['possible_event_pairs'], 36)
        self.assertGreater(r['result']['unresolved_strict_pairs'], 0)
        self.assertEqual(len(r['result']['non_strict_relations']), 1)
        self.assertNotEqual(r['result']['non_strict_relations'][0]['relation'], 'BEFORE')
        self.assertFalse(r['result']['source_local_total_order'])
        self.assertFalse(r['result']['verified_total_chronology'])
        self.assertTrue(r['sources'])

    def test_unresolved_within_one_historical_strand_is_not_chained(self):
        r = ask('Show chronology strand E')
        self.assertEqual(r['result']['strand']['id'], 'E')
        self.assertGreater(r['result']['unresolved_strict_pairs'], 0)
        self.assertEqual(len(r['result']['strict_edges']), 3)
        self.assertFalse(r['result']['source_local_total_order'])
        self.assertTrue(r['sources'])

    def test_two_event_comparison_remains_separate_route(self):
        r = ask('Did X:isperia_assassinated happen before X:lavinia_acting?')
        self.assertEqual(r['route'], 'ask->chronology')
        self.assertEqual(r['result']['relation'], 'BEFORE')


if __name__ == '__main__':
    unittest.main()
