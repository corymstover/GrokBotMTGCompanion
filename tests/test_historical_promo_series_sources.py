"""Ten bounded Wizards family reviews of Vanguard, world decks and local-store promos."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import audit_historical_promo_series_sources as A
from product_family_lookup import load_current_index, select


class HistoricalPromoSeriesSourcesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = [json.loads(path.read_text(encoding="utf-8"))
                    for path in (A.BASE, A.PREV, A.LEDGER)]

    def build(self, ledger=None):
        first, second, third = self.data
        return A.build(first, second, third if ledger is None else ledger)

    def test_ten_sources_keep_four_cohorts_and_all_848_conserved(self):
        report = self.build()
        self.assertEqual({r["code"] for r in report["reviewed_named_promo_families"]}, A.REQUIRED)
        self.assertEqual(report["source_backed_world_championship_years_this_batch"], 5)
        self.assertEqual(report["source_backed_local_store_promotion_years_this_batch"], 4)
        self.assertEqual(report["source_backed_vanguard_codes_this_batch"], 1)
        self.assertEqual(report["cumulative_family_source_backed_codes"], 208)
        self.assertEqual(report["cumulative_source_pending_codes"], 640)
        self.assertEqual(report["remaining_promo_record_extras"], 616)
        self.assertEqual(report["remaining_promo_parent_linked_explicit"], 457)
        self.assertEqual(report["remaining_promo_without_explicit_parent"], 159)
        self.assertEqual(208 + 640, 848)

    def test_wizards_yearly_name_not_exact_scryfall_code_or_debut_legality(self):
        r = self.build()
        self.assertEqual(r["new_exact_wizards_code_declarations"], 0)
        for x in r["reviewed_named_promo_families"]:
            self.assertFalse(x["wizards_prints_exact_scryfall_code"])
            self.assertFalse(x["standalone_premier_expansion_certified"])
            self.assertFalse(x["individual_card_printing_inventory_certified"])
            self.assertFalse(x["new_card_debut_count_certified"])
            self.assertFalse(x["current_format_legality_certified"])

    def test_offline_lookup_and_prior_sources_preserved(self):
        c = load_current_index()
        self.assertGreaterEqual(c["wizards_reviewed_examples"], 208)
        self.assertLessEqual(len(select(c, only_pending=True)), 640)
        self.assertLessEqual(len(select(c, cohort="promotional_and_record_extras", only_pending=True)), 616)
        self.assertTrue(select(c, code="plg24")[0]["wizards_individual_source_review"])
        self.assertFalse(select(c, code="plg24")[0]["wizards_code_explicitly_confirmed"])
        self.assertFalse(select(c, code="plg25")[0]["wizards_individual_source_review"])
        self.assertTrue(select(c, code="brr")[0]["wizards_code_explicitly_confirmed"])
        self.assertTrue(select(c, code="wc97")[0]["wizards_individual_source_review"])
        self.assertFalse(select(c, code="wc03")[0]["wizards_individual_source_review"])

    def test_duplicate_fake_source_wrong_year_and_evidence_grade_rejected(self):
        b = copy.deepcopy(self.data[2])
        b["records"].append(b["records"][0])
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            self.build(b)
        b = copy.deepcopy(self.data[2])
        b["records"][0]["official_url"] = "https://third-party.example/claim"
        with self.assertRaisesRegex(ValueError, "first-party"):
            self.build(b)
        b = copy.deepcopy(self.data[2])
        next(x for x in b["records"] if x["code"] == "wc97")["evidence_grade"] = "wizards_contemporary_promotion"
        with self.assertRaisesRegex(ValueError, "grade misused"):
            self.build(b)
        b = copy.deepcopy(self.data[2])
        next(x for x in b["records"] if x["code"] == "plg24")["official_section"] = "A promo happened at stores, no specific year is documented in this official source."
        with self.assertRaisesRegex(ValueError, "promo year undocumented"):
            self.build(b)

    def test_exact_bytes_regenerated(self):
        self.assertEqual(A.OUTPUT.read_bytes(), A.encode(self.build()))


if __name__ == "__main__":
    unittest.main()
