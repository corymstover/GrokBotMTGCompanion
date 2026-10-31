"""Phase 5/7 Character and Faction histories must be bounded by cited graph edges."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import mv_ask  # noqa: E402


class EntityHistoryTests(unittest.TestCase):
    def test_bolas_history_is_partial_and_deduplicates_claims(self):
        result = mv_ask.ask('What is the lore of Nicol Bolas?')
        self.assertEqual(result['route'], 'ask->entity_history')
        self.assertEqual(result['confidence'], 'QUALIFIED')
        self.assertEqual(result['result']['type'], 'Character')
        self.assertGreaterEqual(result['result']['direct_claims'], 51)
        self.assertEqual(len({r['claim_id'] for r in result['result']['claims']}),
                         result['result']['direct_claims'])
        self.assertFalse(result['result']['complete_history'])
        self.assertFalse(result['result']['verified_total_chronology'])
        self.assertIn('PARTIAL_CITED_ENTITY_HISTORY', result['flags'])
        self.assertIn('NO_VERIFIED_TOTAL_CHRONOLOGY', result['flags'])
        self.assertTrue(result['sources'])

    def test_faction_alias_and_full_name_resolve_same_history(self):
        short = mv_ask.ask('What is the history of the Izzet?')
        full = mv_ask.ask('Tell me about the history of Izzet League')
        self.assertEqual(short['result']['entity'], 'faction:izzet_league')
        self.assertEqual(short['result']['claims'], full['result']['claims'])
        self.assertIn('MATCHED_BY_FACTION_ALIAS', short['flags'])
        self.assertNotIn('MATCHED_BY_FACTION_ALIAS', full['flags'])

    def test_gatewatch_keeps_multiple_relationships_per_claim(self):
        r = mv_ask.ask('Give me the history of the Gatewatch')
        self.assertEqual(r['route'], 'ask->entity_history')
        self.assertEqual(r['result']['entity'], 'faction:gatewatch')
        self.assertTrue(all(c['relations'] and c['sources'] for c in r['result']['claims']))

    def test_all_character_and_faction_claims_are_exactly_direct_and_cited(self):
        graph = mv_ask.graph()
        nodes = {k for k, v in graph.nodes.items() if v['type'] in {'Character', 'Faction'}}
        self.assertGreaterEqual(len(nodes), 628)
        evidence = {k: set() for k in nodes}
        for edge in graph.g['edges']:
            if edge.get('claim') and edge['relation'] not in mv_ask.STRUCTURAL:
                for nid in (edge['from'], edge['to']):
                    if nid in evidence:
                        evidence[nid].add(edge['claim'])
        cited_nodes = 0
        for nid in sorted(nodes):
            r = mv_ask.entity_history(nid)
            self.assertIsNotNone(r, nid)
            self.assertEqual(r['result']['entity'], nid)
            actual = r['result']['claims']
            self.assertEqual({c['claim_id'] for c in actual}, evidence[nid], nid)
            self.assertEqual(len(actual), len(evidence[nid]), nid)
            self.assertFalse(r['result']['complete_history'])
            self.assertFalse(r['result']['verified_total_chronology'])
            if actual:
                cited_nodes += 1
                self.assertEqual(r['confidence'], 'QUALIFIED')
            else:
                self.assertEqual(r['confidence'], 'NOT_FOUND')
                self.assertIn('NO_CITED_ENTITY_HISTORY', r['flags'])
            for row in actual:
                self.assertEqual(row['grade'], graph.nodes['claim:' + row['claim_id']]['grade'])
                self.assertTrue(row['sources'], (nid, row['claim_id']))
                self.assertTrue(row['relations'], (nid, row['claim_id']))
                self.assertNotIn('before', row)
                self.assertNotIn('after', row)
                for url in row['sources']:
                    self.assertIn(url, r['sources'])
                    self.assertTrue(any(s['type'] == 'Source'
                                        and s.get('source_class') == 'WIZARDS_OFFICIAL'
                                        and s.get('url') == url for s in graph.nodes.values()))
        self.assertGreaterEqual(cited_nodes, 623)

    def test_older_routes_stay_distinct(self):
        self.assertEqual(mv_ask.ask('What is the history of Alara?')['route'], 'ask->plane_history')
        self.assertEqual(mv_ask.ask('Who was Ugin\'s twin?')['route'], 'ask->lore:sibling_of|twin_sibling_of')
        self.assertEqual(mv_ask.ask('What is the history of Imaginary Wizard?')['confidence'], 'NOT_FOUND')
        self.assertEqual(mv_ask.ask('What is Sol Ring?')['route'], 'card')


if __name__ == '__main__':
    unittest.main()
