"""Persistent, bounded GitHub shard export and offline set lookup tests."""

import gzip
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import export_printing_lore as ex
import printing_lore_index as ix


class ExportPrintingLoreTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        base = Path(self.tmp.name)
        self.db, self.out, src = base / "index.sqlite3", base / "shards", base / "source.jsonl.gz"
        rows = [
            {"id": "a1", "oracle_id": "plains", "name": "Plains", "set": "lea",
             "set_name": "Limited Edition Alpha", "collector_number": "1", "lang": "en",
             "games": ["paper"], "flavor_text": "The first Urza plain."},
            {"id": "a2", "oracle_id": "plains", "name": "Plains", "set": "lea",
             "set_name": "Limited Edition Alpha", "collector_number": "2", "lang": "en",
             "games": ["paper"], "flavor_text": "The first Mishra plain."},
            {"id": "n1", "oracle_id": "saga", "name": "A Saga // Its Hero", "set": "neo",
             "set_name": "Kamigawa: Neon Dynasty", "collector_number": "80", "lang": "en",
             "games": ["paper"], "card_faces": [
                 {"name": "A Saga", "type_line": "Enchantment — Saga", "oracle_text": "I — Begin.\nII — Finish."},
                 {"name": "Its Hero", "type_line": "Enchantment Creature", "flavor_text": "A forgotten hero."}]},
            {"id": "d1", "oracle_id": "digital", "name": "A Digital Thing", "set": "neo",
             "set_name": "Kamigawa: Neon Dynasty", "collector_number": "500", "lang": "en",
             "digital": True, "games": ["arena"], "flavor_text": "Virtual lore."},
        ]
        with gzip.open(src, "wt", encoding="utf-8") as fh:
            for row in rows:
                fh.write(json.dumps(row) + "\n")
        ix.build(src, self.db)
        self.manifest = ex.export(self.db, self.out, max_bytes=750)

    def tearDown(self):
        self.tmp.cleanup()

    def test_manifest_shard_size_and_reproducibility(self):
        self.assertEqual(self.manifest["total_printings"], 4)
        self.assertEqual(set(self.manifest["sets"]), {"lea", "neo"})
        self.assertTrue(all(x["bytes"] <= 750 for x in self.manifest["shards"].values()))
        self.assertTrue(ex.check(self.db, self.out))

    def test_set_count_distinguishes_printings_from_names(self):
        a = ex.lookup(self.out, "lea", None)
        self.assertEqual((a["matches"], a["distinct_names"], a["oracle_cards"]), (2, 1, 1))
        self.assertEqual([x["c"] for x in a["items"]], ["1", "2"])

    def test_flavor_query_preserves_land_edition_and_saga(self):
        a = ex.lookup(self.out, "lea", "Mishra")
        self.assertEqual([x["id"] for x in a["items"]], ["a2"])
        saga = ex.lookup(self.out, "neo", "forgotten")
        self.assertEqual([x["id"] for x in saga["items"]], ["n1"])
        self.assertIn("II — Finish", saga["items"][0]["faces"][0]["chapters"])

    def test_default_paper_filter(self):
        self.assertEqual(ex.lookup(self.out, "neo", None)["matches"], 1)
        self.assertEqual(ex.lookup(self.out, "neo", None, paper_only=False)["matches"], 2)


if __name__ == "__main__":
    unittest.main()
