"""Source and exact-code-grade regression tests for nineteen promo-category records."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import audit_masterpiece_memorabilia_sources as A
from product_family_lookup import load_current_index, select


class MasterpieceMemorabiliaSourceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base, cls.previous, cls.ledger = (
            json.loads(f.read_text(encoding="utf-8")) for f in (A.BASE, A.PREVIOUS, A.LEDGER)
        )

    def build(self, ledger=None):
        return A.build(self.base, self.previous, self.ledger if ledger is None else ledger)

    def test_all_masterpiece_records_source_reviewed(self):
        report = self.build()
        self.assertEqual({r["code"] for r in report["reviewed_source_records"]}, A.REQUIRED)
        self.assertEqual(report["reviewed_masterpiece_records"], 17)
        self.assertEqual(report["remaining_masterpiece_records"], 0)
        self.assertEqual(report["new_source_backed_codes"], 19)
        self.assertEqual(report["cumulative_family_source_backed_codes"], 198)
        self.assertEqual(report["cumulative_source_pending_codes"], 650)
        self.assertEqual(report["remaining_promo_record_extras"], 626)
        self.assertEqual(report["remaining_promo_parent_links_explicit_in_scryfall"], 457)
        self.assertEqual(report["remaining_promo_no_explicit_parent"], 169)
        self.assertEqual(198 + 650, 848)

    def test_exact_code_claims_only_where_wizards_printed_code(self):
        report = self.build()
        self.assertEqual({r["code"] for r in report["reviewed_source_records"]
                          if r["wizards_exact_code_in_source"]}, A.EXPLICIT)
        self.assertEqual(report["new_exact_code_wizards_confirmations"], 12)
        self.assertEqual(report["new_named_family_only_code_crosswalks"], 7)
        for item in report["reviewed_source_records"]:
            self.assertFalse(item["premier_set_certified"])
            self.assertFalse(item["one_code_one_sold_product_certified"])
            self.assertFalse(item["complete_printing_inventory_certified"])
            self.assertFalse(item["current_legality_certified"])

    def test_family_and_parent_distinctions_in_lookup(self):
        lookup = load_current_index()
        self.assertEqual(lookup["wizards_reviewed_examples"], 198)
        self.assertEqual(len(select(lookup, only_pending=True)), 650)
        self.assertFalse(select(lookup, code="med")[0]["wizards_code_explicitly_confirmed"])
        self.assertTrue(select(lookup, code="sta")[0]["wizards_code_explicitly_confirmed"])
        self.assertEqual(select(lookup, code="sta")[0]["parent_set_code_explicit_only"], "stx")
        self.assertTrue(select(lookup, code="30a")[0]["wizards_individual_source_review"])
        self.assertFalse(select(lookup, code="cei")[0]["wizards_individual_source_review"])
        self.assertEqual(len(select(lookup, cohort="promotional_and_record_extras", only_pending=True)), 626)
        self.assertEqual(len(select(lookup, cohort="preconstructed_and_boxed", only_pending=True)), 11)

    def test_rejects_duplicate_external_source_fake_exact_code_and_rewriting_legality(self):
        dup = copy.deepcopy(self.ledger)
        dup["records"].append(dup["records"][0])
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            self.build(dup)
        bad = copy.deepcopy(self.ledger)
        bad["records"][0]["official_url"] = "https://fake.example/article"
        with self.assertRaisesRegex(ValueError, "Non-Wizards"):
            self.build(bad)
        bad = copy.deepcopy(self.ledger)
        next(r for r in bad["records"] if r["code"] == "med")["evidence_grade"] = "wizards_article_printed_exact_set_code"
        with self.assertRaisesRegex(ValueError, "exact-code"):
            self.build(bad)
        bad = copy.deepcopy(self.ledger)
        next(r for r in bad["records"] if r["code"] == "spg")["evidence_caution"] = "This is exactly one premier set with full known inventory and legality."
        with self.assertRaisesRegex(ValueError, "Ongoing collection"):
            self.build(bad)

    def test_report_bytes_are_deterministic(self):
        self.assertEqual(A.OUTPUT.read_bytes(), A.encode(self.build()))


if __name__ == "__main__":
    unittest.main()
