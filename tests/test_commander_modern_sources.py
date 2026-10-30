"""Verify nineteen official Commander release-family sources and date caveats."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import audit_commander_modern_sources as A
from product_family_lookup import load_current_index, select


class ModernCommanderSourcesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = json.loads(A.BASE.read_text(encoding="utf-8"))
        cls.previous = json.loads(A.PREV.read_text(encoding="utf-8"))
        cls.ledger = json.loads(A.LEDGER.read_text(encoding="utf-8"))

    def build(self, ledger=None):
        return A.build(self.base, self.previous, self.ledger if ledger is None else ledger)

    def test_exact_19_sources_conserve_catalog_and_clear_commander_queue(self):
        report = self.build()
        self.assertEqual({r["code"] for r in report["reviewed_commander_modern_codes"]}, A.REQUIRED)
        self.assertEqual(report["new_source_backed_commander_product_family_codes"], 19)
        self.assertEqual(report["cumulative_family_source_backed_codes"], 151)
        self.assertEqual(report["cumulative_source_pending_codes"], 697)
        self.assertEqual(report["boxed_source_pending_after_batch"], 30)
        self.assertEqual(report["remaining_commander_type_source_pending"], 0)
        self.assertEqual(151 + 697, 848)

    def test_wizards_sources_do_not_certify_printings_legality_or_premier(self):
        records = self.build()["reviewed_commander_modern_codes"]
        for item in records:
            self.assertEqual(item["scryfall_type"], "commander")
            self.assertIn("magic.wizards.com/en/news/", item["wizards_primary_url"])
            for field in ("wizards_exact_scryfall_code_confirmed", "exact_deck_printing_inventory_certified",
                          "new_card_count_certified", "card_legality_inferred", "premier_set_certified"):
                self.assertFalse(item[field], (item["code"], field))

    def test_foundations_cross_year_date_remains_visible_and_not_rewritten(self):
        row = next(x for x in self.build()["reviewed_commander_modern_codes"] if x["code"] == "fdc")
        self.assertEqual(row["scryfall_release_or_first_card_date"], "2024-11-15")
        self.assertEqual(row["scryfall_explicit_parent_code_unchanged"], "fdn")
        self.assertIn("October 2, 2026", row["wizards_versus_scryfall_date_relationship"])
        current = select(load_current_index(), code="fdc")[0]
        self.assertEqual(current["scryfall_release_or_first_card_date"], "2024-11-15")
        self.assertIn("2026", current["wizards_versus_scryfall_date_relationship"])

    def test_duplicate_wrong_source_or_missing_cross_year_caveat_rejected(self):
        broken = copy.deepcopy(self.ledger)
        broken["records"].append(copy.deepcopy(broken["records"][0]))
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            self.build(broken)
        broken = copy.deepcopy(self.ledger)
        broken["records"][0]["official_url"] = "https://fan-site.example/commander"
        with self.assertRaisesRegex(ValueError, "direct Wizards"):
            self.build(broken)
        broken = copy.deepcopy(self.ledger)
        next(r for r in broken["records"] if r["code"] == "fdc")["date_relationship"] = "same release 2024"
        with self.assertRaisesRegex(ValueError, "cross-year"):
            self.build(broken)
        broken = copy.deepcopy(self.ledger)
        broken["records"][0]["code"] = "c21"
        with self.assertRaisesRegex(ValueError, "Unsupported"):
            self.build(broken)

    def test_lookup_and_report_deterministic(self):
        self.assertEqual(A.encode(self.build()), A.encode(self.build()))
        current = load_current_index()
        self.assertGreaterEqual(current["wizards_reviewed_examples"], 151)
        self.assertLessEqual(len(select(current, only_pending=True)), 697)
        self.assertLessEqual(len(select(current, cohort=A.COHORT, only_pending=True)), 30)
        self.assertEqual(len(select(current, set_type="commander", only_pending=True)), 0)
        self.assertTrue(select(current, code="who")[0]["wizards_individual_source_review"])
        self.assertTrue(select(current, code="frc")[0]["wizards_individual_source_review"])
        self.assertTrue(select(current, code="c17")[0]["wizards_individual_source_review"])
        self.assertTrue(select(current, code="dvd")[0]["box_component_of_parent_product"])


if __name__ == "__main__":
    unittest.main()
