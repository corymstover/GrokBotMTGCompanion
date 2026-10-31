"""Quoted 2008 Wizards histories: positive orders and deliberate UNKNOWN boundaries."""
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


class SourceHistoryExpansionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.legacy = json.loads(Q.DATA.read_text(encoding='utf-8'))
        cls.local = json.loads(SEQ.OUT.read_text(encoding='utf-8'))

    def test_weatherlight_mercadia_episode_has_cited_order(self):
        events = [
            'T:weatherlight_mercadia', 'T:mercadia_crash',
            'T:weatherlight_seized', 'T:weatherlight_recovered',
            'T:mercadia_fleet_discovered', 'T:mercadia_strike',
            'T:weatherlight_leaves_mercadia',
        ]
        for earlier, later in zip(events, events[1:]):
            with self.subTest(earlier=earlier, later=later):
                p = SEQ.proof(self.local, earlier, later)
                self.assertEqual(p['result'], 'BEFORE')
                self.assertEqual(len(p['proof']), 1)
                self.assertEqual(p['proof'][0]['source_url'], WIZARDS)
        full = Q.compare_across_datasets(
            self.legacy, self.local, 'B:phyrexia_creator_dies', events[-1]
        )
        self.assertEqual(full['result'], 'BEFORE')
        self.assertTrue(any(e['relation'] == 'SAME_EVENT' for e in full['proof']))
        self.assertTrue(all(e['source_url'] == WIZARDS for e in full['proof']))

    def test_mirrodin_history_is_internally_ordered_but_not_falsely_merged(self):
        events = [
            'H:karn_creates_argentum', 'H:karn_creates_warden',
            'H:karn_jeska_contagion', 'H:warden_becomes_memnarch',
            'H:memnarch_ensnares_beings', 'H:glissa_defeats_memnarch',
            'H:karn_restores_order',
        ]
        for earlier, later in zip(events, events[1:]):
            with self.subTest(earlier=earlier, later=later):
                p = SEQ.proof(self.local, earlier, later)
                self.assertEqual(p['result'], 'BEFORE')
                self.assertEqual(p['proof'][0]['source_url'], WIZARDS)
        self.assertEqual(len(SEQ.proof(self.local, events[0], events[-1])['proof']), 6)
        self.assertEqual(
            Q.compare_across_datasets(self.legacy, self.local,
                                      'H:karn_restores_order', 'P:mirrans_overwhelmed')['result'],
            'UNKNOWN',
        )
        self.assertEqual(
            Q.compare_across_datasets(self.legacy, self.local,
                                      'H:karn_creates_argentum', 'C:mirrodin_created')['result'],
            'UNKNOWN',
        )

    def test_no_uncited_war_or_serra_order_is_added(self):
        pairs = [
            ('T:weatherlight_leaves_mercadia', 'T:rath_overlay'),
            ('T:old_phyrexia_decimated', 'T:yawgmoth_destroyed'),
            ('S:radiant_paranoid', 'S:realm_powerstone_collapse'),
        ]
        for left, right in pairs:
            with self.subTest(left=left, right=right):
                self.assertEqual(
                    Q.compare_across_datasets(self.legacy, self.local, left, right)['result'],
                    'UNKNOWN',
                )
        radiant = SEQ.proof(self.local, 'S:radiant_assumes_rule', 'S:radiant_paranoid')
        self.assertEqual(radiant['result'], 'BEFORE')

    def test_companion_reports_provenance_and_unknown_limitation(self):
        yes = mv_ask.ask('Did T:weatherlight_seized happen before T:mercadia_strike?')
        self.assertEqual(yes['result']['relation'], 'BEFORE')
        self.assertIs(yes['result']['answer'], True)
        self.assertEqual(yes['sources'], [WIZARDS])
        self.assertIn('PARTIAL_IN_UNIVERSE_CHRONOLOGY', yes['flags'])

        unknown = mv_ask.ask('Did H:karn_restores_order happen before P:mirrans_overwhelmed?')
        self.assertEqual(unknown['result']['relation'], 'UNKNOWN')
        self.assertIsNone(unknown['result']['answer'])
        self.assertIn('NO_CITED_CHRONOLOGY_PATH', unknown['flags'])

    def test_composite_remains_cycle_free_with_existing_seven_bridges(self):
        self.assertEqual(Q.check_composite(self.legacy, self.local)['strict_cycles'], 0)
        self.assertEqual(self.local['counts']['verified_legacy_bridges'], 7)


if __name__ == '__main__':
    unittest.main()
