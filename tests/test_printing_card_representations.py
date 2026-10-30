"""Exact art-file printing nodes are identity/navigation, never canon claims."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from query_multiverse_graph import MG


class CardRepresentationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.g = MG()
        cls.evidence = json.loads((ROOT / "data/lore_research/story_image_label_printings_2026-10-30.json").read_text())

    def test_all_exact_printings_have_stable_uuids_and_oracle_identity(self):
        found = [n for n in self.g.nodes.values() if n["type"] == "CardRepresentation"]
        self.assertEqual(len(found), 560)
        self.assertEqual(len({n["id"] for n in found}), 560)
        self.assertTrue(all(n["id"] == "printing:" + n["scryfall_id"] for n in found))
        self.assertTrue(all(n["oracle_id"] for n in found))
        self.assertEqual(sum(e["relation"] == "has_printing" for e in self.g.g["edges"]), 560)

    def test_every_official_art_match_is_navigation_not_canon(self):
        edges = [e for e in self.g.g["edges"] if e["relation"] == "art_file_used_on_official_page"]
        self.assertEqual(len(edges), 570)
        self.assertTrue(all(e["tier"] == "OFFICIAL_IMAGE_LABEL_PRINTING_MATCH" and
                            "grade" not in e and "claim" not in e for e in edges))
        self.assertTrue(all(self.g.nodes[e["from"]]["type"] == "Source" for e in edges))
        self.assertTrue(all(self.g.nodes[e["to"]]["type"] == "CardRepresentation" for e in edges))
        self.assertTrue(all(self.g.nodes[e["from"]]["url"].startswith("https://magic.wizards.com/")
                            for e in edges))
        self.assertEqual(sum(e["status"] != "MATCHED" for e in self.evidence["labels"]), 7)

    def test_printing_lookup_links_card_and_wizards_art_page(self):
        rows = self.g.printing("blc", "1")
        bellos = [x for x in rows if x["printing"]["scryfall_id"] == "31e4b7a1-b377-49d2-a92e-4bcb0db35f16"]
        self.assertEqual(len(bellos), 1)
        links = bellos[0]["relationships"]
        self.assertTrue(any(x["relation"] == "printing_of_card" and x["name"] ==
                            "Bello, Bard of the Brambles" for x in links))
        self.assertTrue(any(x["relation"] == "official_page_uses_art_file" and
                            "magic.wizards.com" in x["source_urls"][0] for x in links))
        self.assertTrue(all(x["status"] == "NAVIGATION_ONLY" for x in links))

    def test_no_graph_link_integrity_problems(self):
        self.assertFalse(self.g.g["problems"])


if __name__ == "__main__":
    unittest.main()
