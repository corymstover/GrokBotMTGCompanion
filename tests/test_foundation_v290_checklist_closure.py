"""Independent, snapshot-scoped acceptance of K053, K104 and K122.

These checks prove specific engineering deliverables. They do not certify a
universal first-print street date, complete story canon or open-domain Q&A.
"""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import mv_ask  # noqa: E402


class FoundationChecklistClosure(unittest.TestCase):
    def test_k053_independently_recount_dated_oracle_debuts_from_history(self):
        # Reconstruct distinct first dates/codes from the published Oracle-ID
        # buckets rather than trusting the separate audit's generated totals.
        ids, tied, single = 0, 0, 0
        for path in sorted((ROOT / 'data/set_atlas').glob('historical_cards_?.json')):
            cards = json.loads(path.read_text(encoding='utf-8'))
            for oid, rows in cards.items():
                self.assertEqual(len(oid), 36)
                dates = [(r[5], r[0]) for r in rows
                         if r[6] == 'en' and r[7] and r[5] and r[5] <= '2026-10-29']
                if not dates:
                    continue
                ids += 1
                earliest = min(day for day, _ in dates)
                first_sets = {code for day, code in dates if day == earliest}
                tied += len(first_sets) > 1
                single += len(first_sets) == 1
        g6 = json.loads((ROOT / 'data/set_atlas/phase1b_snapshot_gates_2026-10-30.json')
                        .read_text(encoding='utf-8'))['g6_debut_reprint']
        self.assertEqual((ids, single, tied), (37853, 33766, 4087))
        self.assertEqual(ids, g6['released_en_paper_oracle_ids'])
        self.assertEqual(single, g6['single_set_debut_identities'])
        self.assertEqual(tied, g6['same_day_multi_set_ties'])
        self.assertEqual(g6['per_set_debut_mismatch_count'], 0)
        self.assertEqual(sum(g6['debut_layouts'].values()), ids)
        self.assertGreater(g6['debut_layouts']['transform'], 0)
        self.assertGreater(g6['debut_layouts']['token'], 0)
        self.assertGreater(g6['debut_only_in_promo_sets'], 0)
        self.assertGreater(g6['identities_without_released_en_paper_printing'], 0)
        self.assertGreater(g6['earliest_printing_flagged_reprint_by_scryfall'], 0)

    def test_k104_every_existing_first_party_set_story_bridge_is_navigable(self):
        bridge = json.loads((ROOT / 'data/set_atlas/phase1b_release_scope_story_bridge_2026-10-29.json')
                            .read_text(encoding='utf-8'))
        links = bridge['wizards_story_series_set_links']
        self.assertEqual(len(links), 12)
        self.assertEqual(bridge['all_set_codes'], 1062)
        for code, link in links.items():
            with self.subTest(code=code):
                q = mv_ask.ask('Show the release date and official story series for ' + code)
                self.assertEqual(q['route'], 'ask->set_atlas:set_story')
                self.assertEqual(q['confidence'], 'QUALIFIED')
                self.assertEqual(q['result']['set']['code'], code)
                self.assertEqual(q['result']['set']['scryfall_recorded_release_date'],
                                 bridge['set_scope_records'][code]['released_at'])
                self.assertEqual(q['result']['official_story_series']['official_title'],
                                 link['series_name_as_published'])
                self.assertIn('NO_IN_UNIVERSE_EVENT_ORDER_INFERRED', q['flags'])
                self.assertIn('SET_DATE_NOT_IN_UNIVERSE_CHRONOLOGY', q['flags'])
                for source in link['sample_first_party_story_sources']:
                    self.assertTrue(source['url'].startswith('https://magic.wizards.com/'))
                    self.assertIn(source['url'], q['sources'])
        missing = mv_ask.ask('Is War of the Spark linked to an official story series?')
        self.assertIsNone(missing['result']['official_story_series'])
        self.assertIn('NO_OFFICIAL_TITLE_STORY_LINK_IN_BOUNDED_INDEX', missing['flags'])

    def test_k122_qa_matrix_covers_difficult_domains_and_honest_unknowns(self):
        qa = json.loads((ROOT / 'data/release/foundation_acceptance_packet_2026-10-30.json')
                        .read_text(encoding='utf-8'))
        cases = qa['representative_questions']
        self.assertGreaterEqual(len(cases), 86)
        self.assertFalse(qa['release_certified'])
        self.assertFalse(qa['owner_accepted'])
        prefixes = ('ask->chronology', 'ask->set_atlas:', 'ask->rules_evidence:interaction',
                    'ask->lore:', 'ask->plane_history', 'ask->entity_history',
                    'ask->card_lore_commander_evidence')
        for prefix in prefixes:
            with self.subTest(route=prefix):
                self.assertTrue(any(c['route'].startswith(prefix) for c in cases))
        names = {c['id']: c for c in cases}
        for key in ('cross_ledger_beyond_bridge_unknown',
                    'gatewatch_cross_arc_war_spark_unknown', 'set_story_war_missing_bridge',
                    'cross_domain_unknown_card', 'rules_published_interaction'):
            self.assertIn(key, names)
        self.assertTrue(names['rules_published_interaction']['sources'])
        self.assertEqual(names['cross_domain_unknown_card']['confidence'], 'NOT_FOUND')
        self.assertEqual(names['set_story_war_missing_bridge']['confidence'], 'QUALIFIED')

    def test_three_scoped_engineering_items_are_checked_without_release_claims(self):
        import audit_full_checklist
        rows = audit_full_checklist.items()
        self.assertEqual(len(rows), 137)
        for item in ("Verify debut/reprint attribution using dated",
                     "Use the Phase 1B Set & Printing Atlas",
                     "Test difficult representative queries"):
            found = [r for r in rows if r['task'].startswith(item)]
            self.assertEqual(len(found), 1)
            self.assertTrue(found[0]['checked'], item)
        self.assertTrue(all(not r['checked'] for r in rows if r['section'].startswith('Phase 6')))
        self.assertEqual([r['checked'] for r in rows
                          if r['section'].startswith('Definition of the first major')],
                         [True, False, False, True, False, False, False])


if __name__ == '__main__':
    unittest.main()
