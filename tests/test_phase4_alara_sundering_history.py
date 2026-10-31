"""First-party Alara Sundering/Conflux/Gideon partial-order with overlap safety."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import mv_ask  # noqa: E402
import query_lore_chronology as Q  # noqa: E402
import source_event_sequences as S  # noqa: E402

ORIGINS = 'https://magic.wizards.com/en/news/feature/worlds-magic-origins-2015-07-09'
ALARA = 'https://magic.wizards.com/en/story/alara-plane'


class AlaraSunderingHistoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.local = json.loads(S.OUT.read_text(encoding='utf-8'))
        cls.old = json.loads(Q.DATA.read_text(encoding='utf-8'))

    def test_gideon_arrived_during_isolation_before_the_reunion(self):
        ordered = ('G:unknown_sundering', 'G:shards_isolated', 'G:gideon_bant_arrival',
                   'G:conflux_reunion', 'G:five_colors_return')
        path = S.proof(self.local, ordered[0], ordered[-1])
        self.assertEqual(path['result'], 'BEFORE')
        self.assertEqual([(e['earlier'], e['later']) for e in path['proof']],
                         list(zip(ordered, ordered[1:])))
        self.assertEqual([e['source_url'] for e in path['proof']], [ORIGINS] * 3 + [ALARA])
        self.assertEqual(path['confidence'], 'QUALIFIED_OFFICIAL_SOURCE_SEQUENCE')

    def test_war_and_borders_are_overlap_not_invented_strict_order(self):
        r = S.proof(self.local, 'G:borders_dissolve', 'G:shard_wars')
        self.assertEqual(r['result'], 'DURING_OR_AFTER_START')
        self.assertEqual(r['proof'][0]['source_url'], ALARA)
        self.assertEqual(S.proof(self.local, 'G:shard_wars', 'G:borders_dissolve')['result'], 'UNKNOWN')
        self.assertEqual(S.proof(self.local, 'G:conflux_reunion', 'G:borders_dissolve')['result'],
                         'DURING_OR_AFTER_START')
        self.assertEqual(S.proof(self.local, 'G:conflux_reunion', 'G:shard_wars')['result'], 'UNKNOWN')

    def test_unknown_sundering_cause_not_attributed_to_bolas(self):
        sundering = next(n for n in self.local['nodes'] if n['id'] == 'G:unknown_sundering')
        self.assertEqual(sundering['claims'], [])  # no fabricated causal pack claim
        self.assertIn('UNKNOWN', next(s for s in self.local['strands'] if s['id'] == 'G')['limitation'])
        self.assertEqual(Q.compare_across_datasets(
            self.old, self.local, 'G:unknown_sundering', 'W:bolas_imprisoned')['result'], 'UNKNOWN')
        self.assertEqual(Q.compare_across_datasets(
            self.old, self.local, 'R:planeswalkers_mend_rifts', 'G:conflux_reunion')['result'], 'UNKNOWN')

    def test_normal_question_answering_preserves_sources_and_unknown(self):
        history = mv_ask.ask('Did G:shards_isolated happen before G:five_colors_return?')
        self.assertEqual(history['route'], 'ask->chronology')
        self.assertEqual(history['result']['relation'], 'BEFORE')
        self.assertEqual(set(history['sources']), {ORIGINS, ALARA})
        overlap = mv_ask.ask('Did G:borders_dissolve happen before G:shard_wars?')
        self.assertEqual(overlap['result']['relation'], 'DURING_OR_AFTER_START')
        self.assertIsNone(overlap['result']['answer'])
        self.assertIn('OVERLAP_NOT_STRICT_ORDER', overlap['flags'])
        gap = mv_ask.ask('Did R:planeswalkers_mend_rifts happen before G:conflux_reunion?')
        self.assertEqual(gap['result']['relation'], 'UNKNOWN')
        self.assertEqual(gap['sources'], [])

    def test_new_strand_does_not_change_legacy_or_bridges(self):
        self.assertEqual(self.old['counts']['event_nodes'], 56)
        self.assertEqual(self.local['counts']['verified_legacy_bridges'], 8)
        self.assertEqual(Q.check_composite(self.old, self.local)['strict_cycles'], 0)


if __name__ == '__main__':
    unittest.main()
