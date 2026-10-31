"""Independent all-pair oracle for the 12 source-local history strands.

Do not use the production closure implementation to calculate expected answers:
an error in the builder and retriever must not pass both sides of the test.
The corpus remains a partial order, not a universal MTG timeline.
"""
from collections import defaultdict
import itertools
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import source_event_sequences as S  # noqa: E402


class GlobalChronologyPairMatrix(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(S.OUT.read_text(encoding='utf-8'))
        cls.nodes = {n['id']: n for n in cls.data['nodes']}
        cls.adj = defaultdict(set)
        cls.non_strict = set()
        for e in cls.data['edges']:
            a, b = e['earlier'], e['later']
            if e['relation'] == 'BEFORE':
                cls.adj[a].add(b)
            else:
                cls.non_strict.add((a, b))
        cls.reach = {}
        for start in cls.nodes:
            seen = set()
            frontier = list(cls.adj[start])
            while frontier:
                nxt = frontier.pop()
                if nxt in seen:
                    continue
                seen.add(nxt)
                frontier.extend(cls.adj[nxt] - seen)
            cls.reach[start] = seen

    def test_reachability_rebuilt_independently_for_all_114_event_nodes(self):
        self.assertEqual(self.data['counts']['events'], len(self.nodes))
        self.assertEqual(self.data['counts']['strands'], len(set(n['strand'] for n in self.nodes.values())))
        self.assertEqual(self.data['counts']['ordered_pairs'], sum(len(v) for v in self.reach.values()))
        self.assertEqual(self.data['precedes'], {k: sorted(v) for k, v in sorted(self.reach.items())})
        for start, later in self.reach.items():
            self.assertNotIn(start, later, f'strict cycle for {start}')
            self.assertTrue(all(self.nodes[start]['strand'] == self.nodes[end]['strand'] for end in later))

    def test_every_unordered_pair_is_compared_to_independent_oracle(self):
        pairs = 0
        for a, b in itertools.combinations(sorted(self.nodes), 2):
            pairs += 1
            if b in self.reach[a]:
                expected = 'BEFORE'
            elif a in self.reach[b]:
                expected = 'AFTER'
            elif (a, b) in self.non_strict:
                expected = 'DURING_OR_AFTER_START'
            else:
                expected = 'UNKNOWN'
            actual = S.proof(self.data, a, b)
            self.assertEqual(actual['result'], expected, f'{a} vs {b}')
            proof = actual['proof']
            if expected in {'BEFORE', 'AFTER'}:
                point = a if expected == 'BEFORE' else b
                for edge in proof:
                    self.assertEqual(edge['earlier'], point)
                    self.assertEqual(edge['relation'], 'BEFORE')
                    self.assertIn(edge['later'], self.adj[point])
                    self.assertTrue(edge['source_url'].startswith('https://magic.wizards.com/'))
                    point = edge['later']
                self.assertEqual(point, b if expected == 'BEFORE' else a)
            elif expected == 'UNKNOWN':
                self.assertEqual(proof, [])
            else:
                self.assertEqual(len(proof), 1)
                self.assertIn((a, b), self.non_strict)
        self.assertEqual(pairs, self.data['counts']['total_pairs'])

    def test_no_strict_edge_can_be_derived_from_three_overlap_relations(self):
        self.assertEqual(len(self.non_strict), self.data['counts']['non_ordering_relations'])
        for a, b in self.non_strict:
            self.assertNotIn(b, self.reach[a])
            self.assertNotIn(a, self.reach[b])
            self.assertEqual(S.proof(self.data, a, b)['result'], 'DURING_OR_AFTER_START')
            self.assertEqual(S.proof(self.data, b, a)['result'], 'UNKNOWN')


if __name__ == '__main__':
    unittest.main()
