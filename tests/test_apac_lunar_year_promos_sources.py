"""Verify six separately sourced APAC Lunar New Year families against frozen paper metadata."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import audit_apac_lunar_year_promos_sources as A
from product_family_lookup import load_current_index, select


class ApacLunarYearPromosSourcesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = [json.loads(path.read_text(encoding="utf-8"))
                    for path in (A.BASE, A.PREV, A.LEDGER)]

    def build(self, ledger=None):
        first, previous, current = self.data
        return A.build(first, previous, current if ledger is None else ledger)

    def test_six_annual_sources_and_whole_catalog_conservation(self):
        report = self.build()
        self.assertEqual({r["code"] for r in report["reviewed_apac_lunar_year_promo_families"]}, A.REQUIRED)
        self.assertEqual(report["cumulative_family_source_backed_codes"], 214)
        self.assertEqual(report["cumulative_source_pending_codes"], 634)
        self.assertEqual(report["remaining_promo_record_extras"], 610)
        self.assertEqual(report["remaining_promo_parent_linked_explicit"], 457)
        self.assertEqual(report["remaining_promo_without_explicit_parent"], 153)
        self.assertEqual(214 + 634, 848)

    def test_family_evidence_does_not_certify_scryfall_code_or_full_card_catalog(self):
        report = self.build()
        self.assertEqual(report["new_exact_wizards_code_declarations"], 0)
        for item in report["reviewed_apac_lunar_year_promo_families"]:
            self.assertFalse(item["wizards_prints_exact_scryfall_code"])
            self.assertFalse(item["standalone_premier_expansion_certified"])
            self.assertFalse(item["individual_card_printing_inventory_certified"])
            self.assertFalse(item["new_card_debut_count_certified"])
            self.assertFalse(item["current_format_legality_certified"])
        self.assertEqual(next(r for r in report["reviewed_apac_lunar_year_promo_families"] if r["code"] == "pl24")["official_source_publication_date"], "2023-12-18")
        self.assertTrue(next(r for r in report["reviewed_apac_lunar_year_promo_families"] if r["code"] == "pl26")["official_source_url"].startswith("https://magic.wizards.com/zh-Hant/"))

    def test_offline_lookup_and_older_sources_preserved(self):
        index = load_current_index()
        self.assertGreaterEqual(index["wizards_reviewed_examples"], 214)
        self.assertLessEqual(len(select(index, only_pending=True)), 634)
        self.assertLessEqual(len(select(index, cohort="promotional_and_record_extras", only_pending=True)), 610)
        for code in sorted(A.REQUIRED):
            item = select(index, code=code)[0]
            self.assertTrue(item["wizards_individual_source_review"])
            self.assertFalse(item["wizards_code_explicitly_confirmed"])
            self.assertEqual(item["parent_set_code_explicit_only"], None)
        self.assertFalse(select(index, code="plny")[0]["wizards_individual_source_review"])
        self.assertTrue(select(index, code="wc97")[0]["wizards_individual_source_review"])
        self.assertFalse(select(index, code="wc03")[0]["wizards_individual_source_review"])

    def test_duplicate_external_url_wrong_animal_or_language_rejected(self):
        tamper = copy.deepcopy(self.data[2])
        tamper["records"].append(tamper["records"][0])
        with self.assertRaisesRegex(ValueError, "Duplicated"):
            self.build(tamper)
        tamper = copy.deepcopy(self.data[2])
        tamper["records"][0]["official_url"] = "https://thirdparty.example/claimed-promos"
        with self.assertRaisesRegex(ValueError, "first-party"):
            self.build(tamper)
        tamper = copy.deepcopy(self.data[2])
        next(r for r in tamper["records"] if r["code"] == "pl26")["evidence_grade"] = "wizards_contemporary_promotion"
        with self.assertRaisesRegex(ValueError, "grade/language"):
            self.build(tamper)
        tamper = copy.deepcopy(self.data[2])
        next(r for r in tamper["records"] if r["code"] == "pl23")["official_section"] = "An unrelated event in 2023 that has absolutely no connection to the named annual promotional family or any cards."
        with self.assertRaisesRegex(ValueError, "named Wizards"):
            self.build(tamper)

    def test_reproduced_bytes(self):
        self.assertEqual(A.OUTPUT.read_bytes(), A.encode(self.build()))


if __name__ == "__main__":
    unittest.main()
