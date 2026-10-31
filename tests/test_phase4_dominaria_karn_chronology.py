"""Primary-source Dominaria/Kamigawa chronology and a precise Karn identity bridge."""
import json
import sys
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import mv_ask  # noqa: E402
import query_lore_chronology as Q  # noqa: E402
import source_event_sequences as S  # noqa: E402

DOMINARIA = 'https://magic.wizards.com/en/story/dominaria-plane'
KARN = 'https://magic.wizards.com/en/story/karn-planeswalker'
RETROSPECTIVE = 'https://magic.wizards.com/en/news/feature/known-mutliverse-2008-03-19'


class DominariaKarnChronologyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.old = json.loads(Q.DATA.read_text(encoding='utf-8'))
        cls.local = json.loads(S.OUT.read_text(encoding='utf-8'))

    def test_dominarian_brothers_war_through_weatherlight(self):
        known = [
            'R:urza_mishra_born', 'R:koilos_powerstones_found',
            'R:brothers_war', 'R:urza_discovers_phyrexia',
            'R:phyrexian_threat', 'R:weatherlight_thwarts_phyrexia',
        ]
        for first, second in zip(known, known[1:]):
            with self.subTest(first=first, second=second):
                r = S.proof(self.local, first, second)
                self.assertEqual(r['result'], 'BEFORE')
                self.assertEqual(len(r['proof']), 1)
                self.assertEqual(r['proof'][0]['source_url'], DOMINARIA)
        self.assertEqual(len(S.proof(self.local, known[0], known[-1])['proof']), 5)
        self.assertEqual(S.proof(self.local, 'R:brothers_war', 'R:dominarian_ice_age')['result'], 'BEFORE')

    def test_cross_plane_damage_explicitly_precedes_kamigawa_kami_war(self):
        r = S.proof(self.local, 'R:dominarian_temporal_fractures', 'R:kami_war_begins')
        self.assertEqual(r['result'], 'BEFORE')
        self.assertEqual(len(r['proof']), 3)
        self.assertTrue(all(e['source_url'] == RETROSPECTIVE for e in r['proof']))
        mending = S.proof(self.local, 'R:dominarian_temporal_fractures', 'R:dominaria_rebuilds')
        self.assertEqual(mending['result'], 'BEFORE')
        self.assertEqual(len(mending['proof']), 3)
        self.assertTrue(all(e['source_url'] == DOMINARIA for e in mending['proof']))

    def test_no_false_interbranch_or_profile_present_order(self):
        unknown = [
            ('R:dominarian_ice_age', 'R:urza_discovers_phyrexia'),
            ('R:kami_war_begins', 'R:planeswalkers_mend_rifts'),
            ('R:phyrexian_threat', 'R:dominarian_temporal_fractures'),
            ('R:brothers_war', 'T:yawgmoth_destroyed'),
            ('R:dominarian_temporal_fractures', 'D:marina_lures'),
            ('H:karn_creates_argentum', 'U:karn_creates_world'),
        ]
        for a, b in unknown:
            with self.subTest(a=a, b=b):
                self.assertEqual(Q.compare_across_datasets(self.old, self.local, a, b)['result'], 'UNKNOWN')

    def test_one_source_corroborated_karn_bridge_with_traceable_proof(self):
        same = Q.compare_across_datasets(self.old, self.local, 'C:karn_created', 'U:karn_created')
        self.assertEqual(same['result'], 'SAME_EVENT')
        self.assertEqual(len(same['proof']), 1)
        self.assertEqual(same['proof'][0]['relation'], 'SAME_EVENT')
        self.assertEqual(same['proof'][0]['source_url'], KARN)

        ordered = Q.compare_across_datasets(
            self.old, self.local, 'C:karn_created', 'U:karn_resolves_against_phyrexians'
        )
        self.assertEqual(ordered['result'], 'BEFORE')
        self.assertTrue(any(e['relation'] == 'SAME_EVENT' for e in ordered['proof']))
        self.assertEqual({e['source_url'] for e in ordered['proof']}, {KARN})
        self.assertEqual(Q.check_composite(self.old, self.local)['strict_cycles'], 0)

    def test_companion_exposes_bounded_positive_and_unknown_answers(self):
        war = mv_ask.ask('Did R:brothers_war happen before R:weatherlight_thwarts_phyrexia?')
        self.assertEqual(war['result']['relation'], 'BEFORE')
        self.assertEqual(war['sources'], [DOMINARIA])
        karn = mv_ask.ask('Did C:karn_created happen before U:world_phyrexian_corruption?')
        self.assertEqual(karn['result']['relation'], 'BEFORE')
        self.assertIn('CROSS_LEDGER_SOURCE_BRIDGED', karn['flags'])
        self.assertEqual(karn['sources'], [KARN])
        ambiguous = mv_ask.ask('Did R:kami_war_begins happen before R:planeswalkers_mend_rifts?')
        self.assertEqual(ambiguous['result']['relation'], 'UNKNOWN')
        self.assertIn('NO_CITED_CHRONOLOGY_PATH', ambiguous['flags'])

    def test_duplicate_strand_ids_fail_closed(self):
        spec = json.loads(S.SPEC.read_text(encoding='utf-8'))
        spec['strands'][1]['id'] = spec['strands'][0]['id']
        with mock.patch.object(S, 'SPEC') as path:
            path.read_text.return_value = json.dumps(spec)
            with self.assertRaisesRegex(ValueError, 'duplicate source-local strand ID'):
                S.build()


if __name__ == '__main__':
    unittest.main()
