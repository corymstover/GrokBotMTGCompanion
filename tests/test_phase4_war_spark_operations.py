"""Official 2019 Ravnica narrative sequence: evidence and anti-overclaim gates."""
import hashlib
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import mv_ask as ASK  # noqa: E402
import source_event_sequences as SEQ  # noqa: E402


class WarSparkOperationsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(SEQ.OUT.read_text(encoding='utf-8'))

    def test_bounded_historical_story_and_original_citations(self):
        strand = next(s for s in self.data['strands'] if s['id'] == 'Y')
        self.assertEqual((strand['events'], strand['strict_edges']), (11, 10))
        self.assertEqual(strand['certainty'], 'HISTORICAL_SOURCE_ACCOUNT')
        self.assertIn("Rat's", strand['limitation'])
        self.assertIn('Rat infers', strand['limitation'])
        self.assertIn('not with an on-page final defeat', strand['limitation'])
        proof = SEQ.proof(self.data, 'Y:portal_opens', 'Y:dack_dies')
        self.assertEqual(proof['result'], 'BEFORE')
        self.assertEqual(len(proof['proof']), 9)
        self.assertEqual({e['source_id'] for e in proof['proof']},
                         {'wr_old_friends', 'wr_rallying', 'wr_operation', 'wr_ashes'})
        for edge in proof['proof']:
            self.assertEqual(edge['quote_sha256'], hashlib.sha256(SEQ.canon(edge['quote']).encode()).hexdigest())
            self.assertTrue(edge['source_url'].startswith('https://magic.wizards.com/'))

    def test_war_stories_do_not_merge_or_fabricate_ending_order(self):
        # The same war is discussed in other ledgers, but no cited SAME_EVENT
        # bridge or chronological claim is inferred across those ledgers.
        for a, b in [
            ('Y:dack_dies', 'Y:blackblade_shatters'),
            ('Y:blackblade_shatters', 'W:bolas_imprisoned'),
            ('Y:war_council', 'X:dovin_flees'),
            ('E:samut_warns_ravnica', 'Y:bridge_disabled'),
        ]:
            r = SEQ.proof(self.data, a, b)
            self.assertEqual((r['result'], r['proof']), ('UNKNOWN', []))
        self.assertEqual(SEQ.proof(self.data, 'Y:final_assault', 'Y:blackblade_shatters')['result'], 'BEFORE')

    def test_public_qa_supports_proven_and_unknown_sequences(self):
        r = ASK.ask('Did Y:portal_opens happen before Y:dack_dies?')
        self.assertEqual((r['route'], r['confidence'], r['result']['relation']),
                         ('ask->chronology', 'QUALIFIED', 'BEFORE'))
        self.assertEqual(len(r['result']['proof']), 9)
        unknown = ASK.ask('Did Y:dack_dies happen before Y:blackblade_shatters?')
        self.assertEqual((unknown['route'], unknown['result']['relation'], unknown['sources']),
                         ('ask->chronology', 'UNKNOWN', []))


if __name__ == '__main__':
    unittest.main()
