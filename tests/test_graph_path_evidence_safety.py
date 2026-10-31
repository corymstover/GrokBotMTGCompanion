"""Graph navigation must be complete, bounded, cited and canon-safe by default."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from query_multiverse_graph import MG  # noqa: E402


class GraphPathEvidenceSafetyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graph = MG()

    def test_depth_limit_does_not_return_a_false_prefix_path(self):
        full = self.graph.path('piru', 'ugin')
        self.assertEqual(len(full), 2)
        self.assertEqual(full[0]['traversal_from'], 'character:piru')
        self.assertEqual(full[-1]['traversal_to'], 'character:ugin')
        self.assertIsNone(self.graph.path('piru', 'ugin', max_depth=1))
        self.assertIsNone(self.graph.path('piru', 'ugin', max_depth=0))
        self.assertEqual(self.graph.path('piru', 'ugin', max_depth=2), full)

    def test_reversed_traversal_is_labeled_without_rewriting_claim_direction(self):
        path = self.graph.path('ugin', 'piru')
        self.assertEqual(len(path), 2)
        self.assertEqual(path[-1]['traversal_direction'], 'reverse')
        self.assertEqual(path[-1]['traversal_to'], 'character:piru')
        self.assertEqual(path[-1]['from'], 'character:piru')  # asserted direction preserved
        self.assertTrue(all(h['status'] == 'CANON_CONFIRMED' and h['source_urls'] for h in path))

    def test_alternate_continuity_is_not_silently_a_canon_bridge(self):
        a, b = 'continuity:echoverse', 'character:nicol_bolas'
        self.assertIsNone(self.graph.path(a, b, max_depth=1))
        qualified = self.graph.path(a, b, max_depth=1, include_qualified=True)
        self.assertEqual(len(qualified), 1)
        self.assertEqual(qualified[0]['claim'], 'A012')
        self.assertEqual(qualified[0]['status'], 'ALTERNATE_CONTINUITY')

    def test_uncertain_facts_are_opt_in_and_always_labeled(self):
        certified = self.graph.path('nicol bolas', 'karn')
        if certified:
            self.assertTrue(all(h['status'] == 'CANON_CONFIRMED' for h in certified))
        mixed = self.graph.path('nicol bolas', 'karn', include_qualified=True)
        self.assertTrue(mixed)
        self.assertTrue(any(h['status'] == 'CANON_DISPUTED' for h in mixed))
        self.assertTrue(all(h['source_urls'] and h['claim'] for h in mixed))

    def test_invalid_depths_fail_closed(self):
        for depth in (-1, 1.25, True, None):
            with self.subTest(depth=depth), self.assertRaisesRegex(ValueError, 'max_depth'):
                self.graph.path('piru', 'ugin', max_depth=depth)

    def test_shorter_uncertain_or_unsourced_edge_never_supersedes_verified_chain(self):
        fixture = {'nodes': [
            {'id': f'character:{x}', 'name': x, 'type': 'Character'} for x in ('a', 'b', 'c')
        ] + [{'id': 'source:one', 'name': 'primary', 'type': 'Source',
              'url': 'https://magic.wizards.com/en/test-source'}],
            'edges': [
                {'from': 'character:a', 'to': 'character:c', 'relation': 'claimed_together',
                 'claim': 'DISPUTED', 'grade': 'CANON_DISPUTED', 'sources': ['one']},
                {'from': 'character:a', 'to': 'character:c', 'relation': 'unverified',
                 'claim': 'UNSOURCED', 'grade': 'CANON_CONFIRMED', 'sources': ['missing']},
                {'from': 'character:a', 'to': 'character:b', 'relation': 'met',
                 'claim': 'AB', 'grade': 'CANON_CONFIRMED', 'sources': ['one']},
                {'from': 'character:b', 'to': 'character:c', 'relation': 'met',
                 'claim': 'BC', 'grade': 'CANON_CONFIRMED', 'sources': ['one']},
            ], 'inverse_relations': {}}
        with tempfile.TemporaryDirectory() as tmp:
            file = Path(tmp) / 'graph.json'
            file.write_text(json.dumps(fixture), encoding='utf-8')
            mg = MG(file)
            self.assertIsNone(mg.path('character:a', 'character:c', max_depth=1))
            certified = mg.path('character:a', 'character:c', max_depth=2)
            self.assertEqual([h['claim'] for h in certified], ['AB', 'BC'])
            qualified = mg.path('character:a', 'character:c', max_depth=1, include_qualified=True)
            self.assertEqual([h['claim'] for h in qualified], ['DISPUTED'])

    def test_cli_honors_max_depth_and_explicit_uncertainty_opt_in(self):
        script = str(ROOT / 'scripts/query_multiverse_graph.py')
        limited = subprocess.run([sys.executable, script, 'path', 'piru', 'ugin', '--max-depth', '1'],
                                 capture_output=True, text=True, check=True)
        self.assertIsNone(json.loads(limited.stdout))
        alternate = subprocess.run([sys.executable, script, 'path', 'echoverse', 'Nicol Bolas',
                                    '--max-depth', '1', '--include-qualified'],
                                   capture_output=True, text=True, check=True)
        self.assertEqual(json.loads(alternate.stdout)[0]['status'], 'ALTERNATE_CONTINUITY')


if __name__ == '__main__':
    unittest.main()
