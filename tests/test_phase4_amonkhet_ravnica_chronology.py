"""Official-source Amonkhet → Ravnica event order, without imagined synchrony."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import mv_ask  # noqa: E402
import query_lore_chronology as Q  # noqa: E402
import source_event_sequences as SEQ  # noqa: E402

RALLYING = 'https://magic.wizards.com/en/news/magic-story/war-spark-ravnica-rallying-reluctant-2019-05-22'
ASHES = 'https://magic.wizards.com/en/news/magic-story/war-spark-ravnica-ashes-2019-06-12'


class AmonkhetRavnicaChronology(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.local = json.loads(SEQ.OUT.read_text(encoding='utf-8'))
        cls.legacy = json.loads(Q.DATA.read_text(encoding='utf-8'))

    def test_witnessed_amonkhet_devastation_precedes_ravnica_warning(self):
        proof = SEQ.proof(self.local, 'E:amonkhet_devastated', 'E:samut_warns_ravnica')
        self.assertEqual(proof['result'], 'BEFORE')
        self.assertEqual(len(proof['proof']), 1)
        self.assertEqual(proof['proof'][0]['source_url'], RALLYING)
        self.assertEqual(proof['confidence'], 'QUALIFIED_OFFICIAL_SOURCE_SEQUENCE')
        claim = next(n for n in self.local['nodes'] if n['id'] == 'E:amonkhet_devastated')['claims']
        self.assertEqual(claim, [{'id': 'AKH029', 'grade': 'CANON_CONFIRMED'}])

    def test_eternal_flow_is_underway_before_plan_and_shutoff(self):
        for dest, url in [('E:bridge_mission_planned', RALLYING),
                          ('E:eternal_flow_stopped', ASHES)]:
            with self.subTest(dest=dest):
                result = SEQ.proof(self.local, 'E:eternals_begin_arriving', dest)
                self.assertEqual(result['result'], 'BEFORE')
                self.assertEqual(len(result['proof']), 1)
                self.assertEqual(result['proof'][0]['source_url'], url)
                self.assertTrue(result['proof'][0]['quote_sha256'])

    def test_unproved_cross_thread_and_gatewatch_links_remain_unknown(self):
        for a, b in [('E:samut_warns_ravnica', 'E:eternal_flow_stopped'),
                     ('E:bridge_mission_planned', 'E:eternal_flow_stopped'),
                     ('Z:gatewatch_oath', 'E:amonkhet_devastated'),
                     ('E:eternal_flow_stopped', 'W:bolas_imprisoned')]:
            with self.subTest(a=a, b=b):
                evidence = Q.compare_across_datasets(self.legacy, self.local, a, b)
                self.assertEqual(evidence['result'], 'UNKNOWN')
                self.assertEqual(evidence.get('proof', []), [])

    def test_companion_exposes_cited_order_and_honest_unknown(self):
        stated = mv_ask.ask('Did E:amonkhet_devastated happen before E:samut_warns_ravnica?')
        self.assertEqual(stated['route'], 'ask->chronology')
        self.assertEqual(stated['result']['relation'], 'BEFORE')
        self.assertTrue(stated['result']['answer'])
        self.assertEqual(stated['sources'], [RALLYING])
        shutoff = mv_ask.ask('Did E:eternals_begin_arriving happen before E:eternal_flow_stopped?')
        self.assertEqual(shutoff['result']['relation'], 'BEFORE')
        self.assertEqual(shutoff['sources'], [ASHES])
        unknown = mv_ask.ask('Did E:samut_warns_ravnica happen before E:eternal_flow_stopped?')
        self.assertEqual(unknown['result']['relation'], 'UNKNOWN')
        self.assertIsNone(unknown['result']['answer'])
        self.assertEqual(unknown['sources'], [])


if __name__ == '__main__':
    unittest.main()
