import json
import contextlib
import io
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import build_plane_history_dossiers as H  # noqa: E402
import query_plane_history as Q  # noqa: E402


class PlaneHistoryDossierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.saved = json.loads(H.OUT.read_text(encoding='utf-8'))

    def test_full_graph_rebuild_is_exact(self):
        self.assertEqual(H.main(['--check']), 0)
        self.assertEqual(self.saved, H.build())
        self.assertTrue(self.saved['status'].startswith('PRELIMINARY_RESEARCH'))

    def test_all_33_planes_and_only_real_claim_edges(self):
        graph = json.loads(H.GRAPH.read_text(encoding='utf-8'))
        nodes = {n['id']: n for n in graph['nodes']}
        planes = {key for key, n in nodes.items() if n['type'] == 'Plane'}
        self.assertEqual({p['id'] for p in self.saved['planes']}, planes)
        evidence_edges = [e for e in graph['edges'] if e.get('claim') and
                          (e['from'] in planes or e['to'] in planes)]
        expected_occurrences = sum(sum(e['from'] == p or e['to'] == p for p in planes)
                                   for e in evidence_edges)
        self.assertEqual(self.saved['counts']['direct_claim_edges'], expected_occurrences)
        for p in self.saved['planes']:
            for fact in p['facts']:
                self.assertEqual(fact['statement'], nodes['claim:' + fact['claim_id']]['name'])
                self.assertIn(p['id'], (fact['subject']['id'], fact['object']['id']))
                self.assertIn(fact['grade'], ('CANON_CONFIRMED', 'CANON_IMPLIED',
                                             'CANON_DISPUTED', 'OPEN_QUESTION',
                                             'ALTERNATE_CONTINUITY'))
                for source in fact['sources']:
                    self.assertEqual(source['url'], nodes['source:' + source['id']]['url'])
                    self.assertEqual(nodes['source:' + source['id']]['source_class'], 'WIZARDS_OFFICIAL')

    def test_disputed_and_undated_claims_not_recast_as_timeline(self):
        dominaria = Q.query('Dominaria')['plane']
        self.assertTrue(any(f['grade'] == 'CANON_DISPUTED' for f in dominaria['facts']))
        for p in self.saved['planes']:
            for fact in p['facts']:
                self.assertNotIn('before', fact)
                self.assertNotIn('after', fact)
                if fact['in_universe_date']:
                    self.assertIn('quote', fact['in_universe_date'])
        self.assertIn('Never infer ordering', self.saved['chronology_policy'])

    def test_query_supports_names_and_unknown_is_not_a_denial(self):
        self.assertEqual(Q.query('phyrexia')['status'], 'PARTIAL_OFFICIAL_GRAPH_HISTORY')
        self.assertEqual(Q.query('NEW PHYREXIA')['plane']['id'], 'plane:new_phyrexia')
        missing = Q.query('An undiscovered plane not in this graph')
        self.assertEqual(missing['status'], 'NOT_FOUND')
        self.assertIn('does not establish nonexistence', missing['note'])

    def test_multi_target_claim_prints_once_with_all_relations(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            self.assertEqual(Q.main(['Alara']), 0)
        rendered = out.getvalue()
        self.assertEqual(rendered.count('ALA001:'), 1)
        for shard in ['Bant', 'Esper', 'Grixis (Alara shard)', 'Jund', 'Naya']:
            self.assertIn(shard, rendered)


if __name__ == '__main__':
    unittest.main()
