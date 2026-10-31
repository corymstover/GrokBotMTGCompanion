"""The ordinary Q&A route must never overstate source-local chronology."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from mv_ask import ask


class ChronologyQuestionTests(unittest.TestCase):
    def test_which_event_happened_first_returns_cited_proof(self):
        r = ask('Which happened first, Konda imprisons a part or breaks the barrier?')
        self.assertEqual(r['route'], 'ask->chronology')
        self.assertEqual(r['result']['relation'], 'BEFORE')
        self.assertEqual(r['result']['answer'], 'Konda imprisons a part of O-Kagachi')
        self.assertEqual(len(r['result']['proof']), 3)
        self.assertEqual(len(r['sources']), 1)
        self.assertEqual(r['confidence'], 'QUALIFIED')
        self.assertFalse(r['result']['verified_total_chronology'])

    def test_before_after_question_maps_yes_and_no_correctly(self):
        a = ask('Did Konda imprisons a part happen before Kyodai and Michiko defeat Konda?')
        b = ask('Did Konda imprisons a part happen after Kyodai and Michiko defeat Konda?')
        self.assertIs(a['result']['answer'], True)
        self.assertIs(b['result']['answer'], False)
        self.assertEqual(a['result']['relation'], b['result']['relation'])

    def test_reverse_query_after_yes(self):
        r = ask('Was Kyodai and Michiko defeat Konda after Konda imprisons a part?')
        self.assertEqual(r['result']['relation'], 'AFTER')
        self.assertIs(r['result']['answer'], True)

    def test_legend_is_qualified_not_confirmed_history(self):
        r = ask('Did Order of the Holly Leaf makes its legendary pact happen before War of Cinders?')
        self.assertEqual(r['result']['relation'], 'BEFORE')
        self.assertIs(r['result']['answer'], True)
        self.assertIn('NARRATED_LEGEND_NOT_VERIFIED_HISTORY', r['flags'])
        self.assertEqual(r['confidence'], 'QUALIFIED')

    def test_overlap_is_not_misreported_as_strict_before(self):
        r = ask('Did War of Cinders happen before Wildsear appears?')
        self.assertEqual(r['result']['relation'], 'DURING_OR_AFTER_START')
        self.assertIsNone(r['result']['answer'])
        self.assertIn('OVERLAP_NOT_STRICT_ORDER', r['flags'])
        self.assertTrue(r['sources'])

    def test_cross_plane_relation_remains_unknown(self):
        r = ask('Did Konda imprisons a part happen before Marina lures her bullies?')
        self.assertEqual(r['result']['relation'], 'UNKNOWN')
        self.assertIsNone(r['result']['answer'])
        self.assertEqual(r['sources'], [])
        self.assertIn('NO_CITED_CHRONOLOGY_PATH', r['flags'])

    def test_cross_legacy_and_new_ledger_unknown(self):
        r = ask('Did Elder Dragon War happen before Marina lures her bullies?')
        self.assertEqual(r['result']['relation'], 'UNKNOWN')
        self.assertIn('CROSS_LEDGER_UNANCHORED', r['flags'])

    def test_explicit_cross_ledger_same_event_and_before_proof(self):
        before=ask('Did B:phyrexia_creator_dies happen before T:rath_constructed?')
        self.assertEqual(before['result']['relation'],'BEFORE')
        self.assertIs(before['result']['answer'],True)
        self.assertIn('CROSS_LEDGER_SOURCE_BRIDGED',before['flags'])
        self.assertNotIn('CROSS_LEDGER_UNANCHORED',before['flags'])
        self.assertTrue(any(e['relation']=='SAME_EVENT' for e in before['result']['proof']))
        self.assertEqual(before['sources'],['https://magic.wizards.com/en/news/feature/known-mutliverse-2008-03-19'])
        same=ask('Did B:phyrexia_portal_closed happen before T:portal_closed?')
        self.assertEqual(same['result']['relation'],'SAME_EVENT')
        self.assertIsNone(same['result']['answer'])
        self.assertIn('CROSS_LEDGER_SOURCE_BRIDGED',same['flags'])

    def test_missing_temporal_bridge_still_unknown(self):
        r=ask('Did B:phyrexia_creator_dies happen before T:yawgmoth_destroyed?')
        self.assertEqual(r['result']['relation'],'UNKNOWN')
        self.assertIsNone(r['result']['answer'])
        self.assertIn('CROSS_LEDGER_UNANCHORED',r['flags'])

    def test_ambiguous_label_returns_not_found_without_guessing(self):
        r = ask('Did Valgavoth happen before War of Cinders?')
        self.assertEqual(r['confidence'], 'NOT_FOUND')
        self.assertEqual(r['result']['relation'], 'UNKNOWN')
        self.assertIn('UNKNOWN_OR_AMBIGUOUS_EVENT_LABEL', r['flags'])

    def test_unrelated_question_uses_existing_lore_route(self):
        r = ask("Who was Kayla bin-Kroog's husband?")
        self.assertEqual(r['route'], 'ask->lore:spouse_of')


if __name__ == '__main__':
    unittest.main()
