"""Phase 4: a supported detour through cited SAME_EVENT bridges is not UNKNOWN.

The original chronology's B/C pairs can be partially ordered using a 2008
Wizards account already quoted and checked in the source-local T strand. No
extra same-event identities, transitive eras, or absolute years are inferred.
"""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import mv_ask  # noqa: E402
import query_lore_chronology as Q  # noqa: E402
import source_event_sequences as SEQ  # noqa: E402

WIZARDS = 'https://magic.wizards.com/en/news/feature/known-mutliverse-2008-03-19'

# These eight were UNKNOWN in the legacy-only comparison on workflow v2.77.
BRIDGED_PAIRS = [
    ('B:phyrexia_creator_dies', 'B:phyrexia_portal_closed', 'BEFORE'),
    ('B:phyrexia_creator_dies', 'B:thran_defeated', 'BEFORE'),
    ('B:phyrexia_creator_dies', 'C:rath_overlay', 'BEFORE'),
    ('B:phyrexia_portal_closed', 'B:yawgmoth_to_phyrexia', 'AFTER'),
    ('B:phyrexia_portal_closed', 'C:rath_overlay', 'BEFORE'),
    ('B:thran_defeated', 'B:yawgmoth_to_phyrexia', 'AFTER'),
    ('B:thran_defeated', 'C:rath_overlay', 'BEFORE'),
    ('B:yawgmoth_to_phyrexia', 'C:rath_overlay', 'BEFORE'),
]


class SameLedgerBridgeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.old = json.loads(Q.DATA.read_text(encoding='utf-8'))
        cls.local = json.loads(SEQ.OUT.read_text(encoding='utf-8'))

    def test_eight_previously_unknown_pairs_now_have_primary_cited_paths(self):
        for first, second, expected in BRIDGED_PAIRS:
            with self.subTest(first=first, second=second):
                native = Q.compare(self.old, first, second)
                self.assertEqual(native['result'], 'UNKNOWN')
                result = Q.compare_across_datasets(self.old, self.local, first, second)
                self.assertEqual(result['result'], expected)
                proof = result['proof']
                self.assertTrue(any(edge['relation'] == 'SAME_EVENT' for edge in proof))
                self.assertTrue(any(edge['relation'] == 'BEFORE' for edge in proof))
                self.assertTrue(all(edge.get('source_url') == WIZARDS for edge in proof))
                self.assertEqual(result['confidence'], 'QUALIFIED_CITED_CROSS_LEDGER_SEQUENCE')

    def test_natural_language_flags_a_same_ledger_bridged_proof(self):
        before = mv_ask.ask('Did B:phyrexia_creator_dies happen before B:phyrexia_portal_closed?')
        self.assertEqual(before['result']['relation'], 'BEFORE')
        self.assertIs(before['result']['answer'], True)
        self.assertIn('CROSS_LEDGER_SOURCE_BRIDGED', before['flags'])
        self.assertEqual(before['sources'], [WIZARDS])

        reverse = mv_ask.ask('Did B:phyrexia_portal_closed happen before B:phyrexia_creator_dies?')
        self.assertEqual(reverse['result']['relation'], 'AFTER')
        self.assertIs(reverse['result']['answer'], False)

    def test_direct_evidence_retains_its_original_scope_and_proof(self):
        first, second = 'A:elder_dragon_war', 'A:primeval_rule'
        native = Q.compare(self.old, first, second)
        combined = Q.compare_across_datasets(self.old, self.local, first, second)
        self.assertEqual(combined, native)

        first, second = 'K:konda_imprisons', 'K:realm_barrier_breaks'
        native = SEQ.proof(self.local, first, second)
        combined = Q.compare_across_datasets(self.old, self.local, first, second)
        self.assertEqual(combined, native)

    def test_unbridged_events_are_still_unknown(self):
        for a, b in [('B:phyrexia_creator_dies', 'T:yawgmoth_destroyed'),
                     ('A:elder_dragon_war', 'C:rath_overlay'),
                     ('K:konda_imprisons', 'M:ancient_collapse')]:
            with self.subTest(a=a, b=b):
                result = Q.compare_across_datasets(self.old, self.local, a, b)
                self.assertEqual(result['result'], 'UNKNOWN')
                self.assertFalse(result['proof'])

    def test_no_new_cycle_or_unsourced_bridge(self):
        self.assertEqual(Q.check_composite(self.old, self.local)['strict_cycles'], 0)
        self.assertEqual(len(self.local['legacy_bridges']), 8)


if __name__ == '__main__':
    unittest.main()
