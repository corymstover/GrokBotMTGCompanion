"""Nine independently sourced historical annual Commander preconstructed lines."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import audit_commander_series_sources as A
from product_family_lookup import (
    apply_commander_series_source_overlay, load_current_index, select,
)


class HistoricalCommanderSourcesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = json.loads(A.BASE.read_text(encoding="utf-8"))
        cls.previous = json.loads(A.PREV.read_text(encoding="utf-8"))
        cls.ledger = json.loads(A.LEDGER.read_text(encoding="utf-8"))

    def build(self, data=None):
        return A.build(self.base, self.previous, self.ledger if data is None else data)

    def test_nine_annual_families_conserve_entire_848_codes(self):
        report = self.build()
        self.assertEqual(len(report["reviewed_commander_codes"]), 9)
        self.assertEqual(report["new_annual_commander_release_families"], 9)
        self.assertEqual(report["cumulative_family_source_backed_codes"], 120)
        self.assertEqual(report["cumulative_source_pending_codes"], 728)
        self.assertEqual(report["boxed_source_pending_after_batch"], 61)
        self.assertEqual(120 + 728, 848)

    def test_family_not_deck_box_or_legality_claim(self):
        rows = {r["code"]: r for r in self.build()["reviewed_commander_codes"]}
        self.assertEqual({r["source_year"] for r in rows.values()}, {2011, *range(2013, 2021)})
        self.assertEqual(set(rows), set(A.EXPECTED))
        for row in rows.values():
            self.assertFalse(row["individually_packaged_deck_count_certified"])
            self.assertFalse(row["card_format_legality_inferred"])
            self.assertFalse(row["premier_set_status_certified"])
            self.assertFalse(row["scryfall_code_explicitly_confirmed_by_wizards"])

    def test_source_tampering_and_duplicates_rejected(self):
        data = copy.deepcopy(self.ledger)
        data["records"].append(copy.deepcopy(data["records"][0]))
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            self.build(data)
        data = copy.deepcopy(self.ledger)
        data["records"][0]["official_product_url"] = "https://unofficial.example.com/"
        with self.assertRaisesRegex(ValueError, "direct official"):
            self.build(data)
        data = copy.deepcopy(self.ledger)
        data["records"][0]["year"] = 2012
        with self.assertRaisesRegex(ValueError, "Unexpected"):
            self.build(data)
        data = copy.deepcopy(self.ledger)
        data["records"][0]["code"] = "c21"
        with self.assertRaisesRegex(ValueError, "Unexpected"):
            self.build(data)

    def test_previous_history_unchanged_and_live_lookup_120(self):
        self.assertEqual(self.previous["cumulative_family_source_backed_codes"], 111)
        current = load_current_index()
        # The prior 120/728 checkpoint is exact in the static audit above.
        # Current offline lookup may include additional additive source batches.
        self.assertGreaterEqual(current["wizards_reviewed_examples"], 120)
        self.assertLessEqual(len(select(current, only_pending=True)), 728)
        self.assertLessEqual(len(select(current, cohort=A.COHORT, only_pending=True)), 61)
        self.assertTrue(select(current, code="c14")[0]["wizards_individual_source_review"])
        # C21 was pending at this frozen batch, though later additive batches
        # are allowed to source it in the live index.
        self.assertIn("c21", {x["code"] for x in self.previous["remaining_source_pending_queue"]})
        self.assertFalse(select(current, code="evg")[0]["wizards_premier_status_certified"])
        self.assertEqual(len(current["all_848_released_nondigital_other_type_records"]), 848)

    def test_deterministic_report(self):
        self.assertEqual(A.encode(self.build()), A.encode(self.build()))


if __name__ == "__main__":
    unittest.main()
