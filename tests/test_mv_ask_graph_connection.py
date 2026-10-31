"""Adversarial Phase 7 graph-connection questions: navigation is not canon synthesis."""
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import mv_ask as A  # noqa: E402
from query_multiverse_graph import MG  # noqa: E402


def _graph_fixture():
    nodes = [{'id': f'character:{x}', 'type': 'Character', 'name': x.title()}
             for x in ('alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta')]
    nodes += [{'id': 'source:official', 'type': 'Source', 'name': 'Official primary text',
               'url': 'https://magic.wizards.com/en/story/example'}]

    def edge(a, b, claim, grade):
        return {'from': f'character:{a}', 'to': f'character:{b}',
                'relation': 'met', 'claim': claim, 'grade': grade, 'sources': ['official']}

    return {'evidence_cutoff': '2026-10-30', 'nodes': nodes, 'inverse_relations': {}, 'edges': [
        edge('alpha', 'beta', 'TEST001', 'CANON_CONFIRMED'),
        edge('delta', 'beta', 'TEST002', 'CANON_CONFIRMED'),  # must traverse in reverse
        edge('delta', 'epsilon', 'TEST003', 'CANON_CONFIRMED'),
        edge('epsilon', 'zeta', 'TEST004', 'CANON_CONFIRMED'),
        edge('gamma', 'zeta', 'TEST005', 'CANON_DISPUTED'),
    ]}


class GraphConnectionQuestionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        path = Path(self.temp.name) / 'graph.json'
        path.write_text(json.dumps(_graph_fixture()), encoding='utf-8')
        self.graph = MG(path)
        self.patched = patch.object(A, 'graph', return_value=self.graph)
        self.patched.start()
        self.addCleanup(self.patched.stop)

    def test_confirmed_multi_hop_is_qualified_navigation_with_true_endpoint(self):
        out = A.ask('How is Alpha connected to Delta?')
        self.assertEqual(out['route'], 'ask->graph_connection')
        self.assertEqual(out['confidence'], 'QUALIFIED')
        self.assertEqual(out['result']['left_id'], 'character:alpha')
        self.assertEqual(out['result']['right_id'], 'character:delta')
        self.assertEqual(out['result']['hops'], 2)
        self.assertEqual(out['result']['path'][-1]['traversal_direction'], 'reverse')
        self.assertFalse(out['result']['direct_cited_relation'])
        self.assertIn('NOT_TEMPORAL_OR_CAUSAL_PROOF', out['flags'])
        self.assertEqual(out['sources'], ['https://magic.wizards.com/en/story/example'])

    def test_disputed_shortcut_never_becomes_confirmed_path(self):
        out = A.ask('What is the connection between Alpha and Gamma?')
        self.assertEqual(out['confidence'], 'NOT_FOUND')
        self.assertIsNone(out['result']['path'])
        self.assertEqual(out['sources'], [])
        self.assertIn('NO_CITED_GRAPH_PATH_WITHIN_FOUR_HOPS', out['flags'])

    def test_depth_and_unknown_endpoints_do_not_invent_links(self):
        # The strictly confirmed Alpha→Zeta path has four hops and is valid.
        yes = A.ask('How is Alpha linked to Zeta?')
        self.assertEqual(yes['result']['hops'], 4)
        self.assertEqual(yes['confidence'], 'QUALIFIED')
        for query in ('How is Alpha connected to Nobody?', 'How is Alpha connected to Alpha?'):
            with self.subTest(query=query):
                self.assertEqual(A.ask(query)['confidence'], 'NOT_FOUND')

    def test_real_graph_regression(self):
        # A real graph proof must not silently collapse several separate
        # official claims into one causal Tezzeret/Kaladesh story.
        with patch.object(A, 'graph', return_value=MG()):
            out = A.ask('How is Tezzeret connected to Kaladesh?')
        self.assertEqual(out['confidence'], 'QUALIFIED')
        self.assertEqual(out['result']['hops'], 3)
        self.assertEqual(out['result']['right_id'], 'plane:kaladesh')
        self.assertTrue(out['sources'])
        self.assertTrue(all(h['status'] == 'CANON_CONFIRMED' for h in out['result']['path']))
        with patch.object(A, 'graph', return_value=MG()):
            planes = A.ask('How is Amonkhet connected to Ravnica?')
        self.assertEqual(planes['confidence'], 'QUALIFIED')
        self.assertEqual(planes['result']['left_id'], 'plane:amonkhet')
        self.assertEqual(planes['result']['right_id'], 'plane:ravnica')
        self.assertIn('NOT_TEMPORAL_OR_CAUSAL_PROOF', planes['flags'])


if __name__ == '__main__':
    unittest.main()
