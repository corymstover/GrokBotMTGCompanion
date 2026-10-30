"""Tests for Phase 3 card-name anchors (scripts/build_card_name_anchors.py) and their graph ingest."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_card_name_anchors as A  # noqa: E402
import build_multiverse_graph as B  # noqa: E402

DATA = json.loads(A.OUT.read_text(encoding="utf-8"))


class CharMatchTests(unittest.TestCase):
    def test_accepts_epithets_and_one_word_suffix(self):
        for n in ["Urza", "Urza, Lord High Artificer", "Ashnod the Uncaring", "Jhoira of the Ghitu", "Karn Liberated"]:
            self.assertTrue(A.char_match(n, n.split(",")[0].split(" ")[0]), n)

    def test_rejects_possessives_and_other_names(self):
        for n, alias in [("Urza's Saga", "Urza"), ("Urzan Thing", "Urza"), ("Karn's Temporal Sundering", "Karn"),
                         ("Teferi Akosa of Zhalfir", "Teferi"), ("Urza's Tower", "Urza")]:
            self.assertFalse(A.char_match(n, alias), n)


class AnchorPackTests(unittest.TestCase):
    def test_self_hash_and_status_labels(self):
        import hashlib
        body = {k: v for k, v in DATA.items() if k != "content_sha256"}
        self.assertEqual(hashlib.sha256(json.dumps(body, sort_keys=True).encode()).hexdigest(), DATA["content_sha256"])
        self.assertIn("PRELIMINARY", DATA["status"])
        self.assertNotIn("APPROVED", DATA["status"].replace("not owner approved", ""))
        self.assertEqual(DATA["card_data_source"]["provider"], "Scryfall")

    def test_counts_consistent_and_no_unset_or_possessive_anchor(self):
        edges = [c for a in DATA["anchors"] for c in a["cards"]]
        self.assertEqual(DATA["counts"]["anchor_edges"], len(edges))
        names = {c["name"] for c in edges}
        self.assertNotIn("Urza, Academy Headmaster", names)
        chars = [a for a in DATA["anchors"] if a["entity_type"] == "Character"]
        for a in chars:
            for c in a["cards"]:
                self.assertIn("Legendary", c["type_line"])
                self.assertNotIn("'s ", c["name"].split(" // ")[0].split(",")[0])

    def test_known_anchors_present(self):
        by = {a["entity"]: {c["name"] for c in a["cards"]} for a in DATA["anchors"]}
        self.assertIn("Weatherlight", by["weatherlight"])
        self.assertIn("Golgothian Sylex", by["golgothian_sylex"])
        self.assertIn("Dakkon Blackblade", by["dakkon"])  # paper via Legends although oracle printing is MTGO
        self.assertIn("Ugin, the Spirit Dragon", by["ugin"])

    def test_check_passes(self):
        self.assertEqual(A.main(["--check"]), 0)


class GraphIngestTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.g = B.build()

    def test_named_on_card_edges_are_navigation_with_no_source_nodes(self):
        es = [e for e in self.g["edges"] if e["relation"] == "named_on_card"]
        self.assertEqual(len(es), DATA["counts"]["anchor_edges"])
        for e in es:
            self.assertEqual(e.get("tier"), "NAMED_CARD")
            self.assertTrue(e.get("card_data_source", "").startswith("Scryfall"))
            self.assertNotIn("claim", e)
        self.assertEqual(self.g["stats"]["non_wizards_sources"], 0)
        self.assertEqual(self.g["problems"], [])


if __name__ == "__main__":
    unittest.main()
