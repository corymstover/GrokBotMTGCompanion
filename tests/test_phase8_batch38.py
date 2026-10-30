"""Phase 8 batch 38: the explicit remaining-priority-pool enrichment batch.

Batch 38 is admitted only by an explicit `--batch 38` build. Earlier batches
keep their frozen membership, and --expand-auto can never label a card 38.
"""
import json
import sys
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import build_card_enrichment as B  # noqa: E402

# Frozen counts of the stored enrichment before batch 38 (cycles 33-37).
PRE38 = 3409


class Batch38SelectionTests(unittest.TestCase):
    def test_explicit_only(self):
        legend = {"name": "Unreviewed legend", "edhrec_rank": 30000}
        self.assertIsNone(B.select_batch(legend, {"legendary-creature"}))
        self.assertNotEqual(B.select_batch(legend, {"legendary-creature"}, allow_automatic_new=True), 38)
        self.assertEqual(B.select_batch(legend, {"legendary-creature"}, explicit_batch=38), 38)

    def test_previous_batch_and_batch37_names_win(self):
        legend = {"name": "Unreviewed legend"}
        self.assertEqual(B.select_batch(legend, {"legendary-creature"}, {"batch": 35}, explicit_batch=38), 35)
        self.assertEqual(B.select_batch({"name": "Ghalta the Unstoppable"}, {"legendary-creature"},
                                        explicit_batch=38), 37)

    def test_outside_pool_not_admitted(self):
        self.assertIsNone(B.select_batch({"name": "Plain spell"}, set(), explicit_batch=38))


class Batch38StoredDataTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d = json.loads(B.OUT.read_text(encoding="utf-8"))

    def test_earlier_batches_conserved(self):
        by = Counter(v["batch"] for v in self.d["cards"].values())
        self.assertEqual(sum(n for b, n in by.items() if b < 38), PRE38)
        self.assertGreater(by[38], 0)

    def test_batch38_cards_are_in_the_priority_pool_and_honest_about_lore(self):
        for v in self.d["cards"].values():
            if v["batch"] != 38:
                continue
            self.assertTrue(v["tiers"], v["name"])
            self.assertEqual(len(v["lines"]), 2, v["name"])

    def test_batch_rule_recorded(self):
        self.assertIn(38, [b["cycle"] for b in self.d["batches"]])


if __name__ == "__main__":
    unittest.main()
