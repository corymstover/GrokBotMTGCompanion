"""Preserve source-pack display variants without guessing alias identity."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from build_multiverse_graph import Graph
from query_multiverse_graph import MG


class DisplayNameVariantTests(unittest.TestCase):
    def test_registered_same_id_names_are_searchable(self):
        mg = MG()
        for name, id_ in [("Ajani Goldmane", "character:ajani"),
                          ("Queen Marchesa", "character:marchesa"),
                          ("Weatherlight (skyship)", "artifact:weatherlight"),
                          ("Surrak Dragonclaw", "character:surrak")]:
            self.assertEqual(mg.find(name, prefer=mg.nodes[id_]["type"]), id_)
        self.assertGreaterEqual(sum(bool(n.get("name_variants")) for n in mg.nodes.values()), 22)
        self.assertIn("character:ajani", {n["id"] for n in mg.search("Ajani Goldmane")})

    def test_display_name_is_stable_and_provenance_preserved(self):
        g = Graph()
        g.add_node("character:ajani", "Character", "Ajani", "pack_A")
        g.add_node("character:ajani", "Character", "Ajani Goldmane", "pack_B")
        self.assertEqual(g.nodes["character:ajani"]["name"], "Ajani")
        self.assertEqual(g.nodes["character:ajani"]["name_variants"], ["Ajani", "Ajani Goldmane"])
        self.assertEqual(g.nodes["character:ajani"]["origins"], ["pack_A", "pack_B"])

    def test_similar_names_never_merge_distinct_ids(self):
        g = Graph()
        g.add_node("character:one", "Character", "Teysa", "pack_A")
        g.add_node("character:two", "Character", "Teysa", "pack_B")
        self.assertEqual(len(g.nodes), 2)
        self.assertFalse(any("name_variants" in n for n in g.nodes.values()))


if __name__ == "__main__":
    unittest.main()
