"""Canon-safe Bolas/Ugin 2019-25 chronology; never infer fate or spark."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import mv_ask  # noqa: E402
import query_lore_chronology as Q  # noqa: E402
import source_event_sequences as S  # noqa: E402

WAR = 'https://magic.wizards.com/en/news/making-magic/even-more-war-games-2019-05-06'
DRAGONSTORM = 'https://magic.wizards.com/en/news/magic-story/tarkir-dragonstorm-episode-7-return'
LORWYN = 'https://magic.wizards.com/en/news/magic-story/lorwyn-eclipsed-episode-2-shake-off-slumber'


class BolasPostWarChronologyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.local = json.loads(S.OUT.read_text(encoding='utf-8'))
        cls.old = json.loads(Q.DATA.read_text(encoding='utf-8'))
        cls.claims = json.loads((ROOT / 'data/lore_research/pack_a_ugin_bolas_evidence_2026-10-30.json')
                                .read_text(encoding='utf-8'))

    def test_2019_imprisonment_has_independent_official_source(self):
        claim = next(c for c in self.claims['claims'] if c['id'] == 'A008')
        self.assertEqual(claim['grade'], 'CANON_CONFIRMED')
        self.assertEqual(self.claims['source_register'][claim['source_ids'][0]]['url'], WAR)
        node = next(n for n in self.local['nodes'] if n['id'] == 'W:bolas_imprisoned')
        self.assertEqual(node['claims'], [{'id': 'A008', 'grade': 'CANON_CONFIRMED'}])

    def test_imprisonment_to_escape_and_ugin_intervention_are_qualified(self):
        chain = S.proof(self.local, 'W:bolas_imprisoned', 'W:brothers_vanish')
        self.assertEqual(chain['result'], 'BEFORE')
        self.assertEqual(len(chain['proof']), 3)
        self.assertEqual({e['source_url'] for e in chain['proof']}, {DRAGONSTORM})
        self.assertEqual(chain['confidence'], 'QUALIFIED_OFFICIAL_SOURCE_SEQUENCE')
        self.assertIn('explicitly questions whether they died', chain['limitation'])

    def test_narset_exit_precedes_later_report_but_does_not_establish_spark(self):
        chain = S.proof(self.local, 'W:brothers_vanish', 'W:ajani_reports')
        self.assertEqual(chain['result'], 'BEFORE')
        self.assertEqual([e['source_url'] for e in chain['proof']], [DRAGONSTORM, LORWYN])
        spark_claim = next(c for c in self.claims['claims'] if c['id'] == 'A011')
        self.assertEqual(spark_claim['grade'], 'OPEN_QUESTION')
        self.assertEqual(spark_claim['object'], 'unknown')

    def test_parallel_events_and_ancient_realm_do_not_get_unsourced_order(self):
        for before, after in [
            ('W:meditation_unravels', 'W:bolas_freed'),
            ('W:bolas_freed', 'W:meditation_unravels'),
            ('W:bolas_imprisoned', 'B:ugin_reforms'),
            ('B:ugin_reforms', 'W:bolas_imprisoned'),
            ('W:brothers_vanish', 'R:planeswalkers_mend_rifts'),
        ]:
            with self.subTest(before=before, after=after):
                self.assertEqual(Q.compare_across_datasets(
                    self.old, self.local, before, after)['result'], 'UNKNOWN')

    def test_companion_exposes_positive_and_unknown_answers_with_sources(self):
        answered = mv_ask.ask('Did W:bolas_imprisoned happen before W:bolas_freed?')
        self.assertEqual(answered['route'], 'ask->chronology')
        self.assertEqual(answered['result']['relation'], 'BEFORE')
        self.assertEqual(answered['sources'], [DRAGONSTORM])
        followed = mv_ask.ask('Did W:brothers_vanish happen before W:ajani_reports?')
        self.assertEqual(followed['result']['relation'], 'BEFORE')
        self.assertEqual(set(followed['sources']), {DRAGONSTORM, LORWYN})
        unresolved = mv_ask.ask('Did W:meditation_unravels happen before W:bolas_freed?')
        self.assertEqual(unresolved['result']['relation'], 'UNKNOWN')
        self.assertIsNone(unresolved['result']['answer'])
        self.assertEqual(unresolved['sources'], [])

    def test_legacy_event_counts_and_same_event_bridges_unchanged(self):
        self.assertEqual(self.old['counts']['event_nodes'], 56)
        self.assertEqual(self.local['counts']['verified_legacy_bridges'], 8)
        self.assertEqual(Q.check_composite(self.old, self.local)['strict_cycles'], 0)


if __name__ == '__main__':
    unittest.main()
