"""Nine graded Wizards citations for inserts, two Clash Packs and Gideon's box."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import audit_inserts_clash_spellbook_sources as A
from product_family_lookup import load_current_index, select


class InsertsClashSpellbookTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = json.loads(A.BASE.read_text(encoding="utf-8"))
        cls.previous = json.loads(A.PREV.read_text(encoding="utf-8"))
        cls.ledger = json.loads(A.LEDGER.read_text(encoding="utf-8"))

    def build(self, ledger=None):
        return A.build(self.base, self.previous, self.ledger if ledger is None else ledger)

    def test_all_nine_conserve_848_and_clear_special_insert_queue(self):
        report = self.build()
        self.assertEqual({r["code"] for r in report["reviewed_inserts_clash_spellbook_codes"]}, A.REQUIRED)
        self.assertEqual(report["new_source_backed_product_family_codes"], 9)
        self.assertEqual(report["cumulative_family_source_backed_codes"], 179)
        self.assertEqual(report["cumulative_source_pending_codes"], 669)
        self.assertEqual(report["remaining_special_inserts_and_eternal_subsets"], 0)
        self.assertEqual(report["remaining_draft_and_starter_variants"], 11)
        self.assertEqual(report["remaining_reprint_and_curated_products"], 2)
        self.assertEqual(report["remaining_boxed_preconstructed"], 11)
        self.assertEqual(179 + 669, 848)

    def test_exact_code_article_vs_printing_gallery_vs_family_only(self):
        rows = {r["code"]: r for r in self.build()["reviewed_inserts_clash_spellbook_codes"]}
        self.assertEqual({code for code, r in rows.items() if r["wizards_set_code_printed_in_article"]}, A.INSERTS)
        self.assertEqual({code for code, r in rows.items() if r["wizards_printing_code_printed_in_card_gallery"]}, {"ss2"})
        self.assertFalse(rows["ss2"]["wizards_set_code_printed_in_article"])
        self.assertIn("card-gallery", rows["ss2"]["wizards_secondary_gallery_url"])
        for code in A.CLASH:
            self.assertFalse(rows[code]["wizards_set_code_printed_in_article"])
            self.assertFalse(rows[code]["wizards_printing_code_printed_in_card_gallery"])
        for row in rows.values():
            self.assertFalse(row["standalone_premier_set_certified"])
            self.assertFalse(row["exact_box_printing_inventory_certified"])
            self.assertFalse(row["new_card_count_certified"])
            self.assertFalse(row["current_format_legality_certified"])

    def test_fate_reforged_product_date_distinct_from_metadata(self):
        row = next(r for r in self.build()["reviewed_inserts_clash_spellbook_codes"] if r["code"] == "cp2")
        self.assertEqual(row["scryfall_release_or_first_card_date"], "2015-01-23")
        self.assertIn("January 30", row["wizards_source_note"])
        self.assertIn("January 23", row["wizards_source_note"])

    def test_source_tampering_wrong_grade_and_fake_legality_rejected(self):
        damaged = copy.deepcopy(self.ledger)
        damaged["records"].append(copy.deepcopy(damaged["records"][0]))
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            self.build(damaged)
        damaged = copy.deepcopy(self.ledger)
        damaged["records"][0]["official_url"] = "https://not-wizards.example/reprint"
        with self.assertRaisesRegex(ValueError, "direct Wizards"):
            self.build(damaged)
        damaged = copy.deepcopy(self.ledger)
        next(r for r in damaged["records"] if r["code"] == "cp1")["source_grade"] = "wizards_article_explicit_set_code"
        with self.assertRaisesRegex(ValueError, "evidence grade"):
            self.build(damaged)
        damaged = copy.deepcopy(self.ledger)
        next(r for r in damaged["records"] if r["code"] == "ss2")["secondary_official_gallery_url"] = "https://example.com/ss2"
        with self.assertRaisesRegex(ValueError, "direct Wizards card gallery"):
            self.build(damaged)
        damaged = copy.deepcopy(self.ledger)
        next(r for r in damaged["records"] if r["code"] == "cp2")["source_note"] = "The first-card date was also the boxed product on January 23, 2015."
        with self.assertRaisesRegex(ValueError, "product versus first-card"):
            self.build(damaged)

    def test_live_lookup_retains_old_sources(self):
        self.assertEqual(A.encode(self.build()), A.encode(self.build()))
        current = load_current_index()
        self.assertGreaterEqual(current["wizards_reviewed_examples"], 179)
        self.assertLessEqual(len(select(current, only_pending=True)), 669)
        self.assertEqual(len(select(current, cohort="special_inserts_and_eternal_subsets", only_pending=True)), 0)
        self.assertTrue(select(current, code="bot")[0]["wizards_code_explicitly_confirmed"])
        self.assertTrue(select(current, code="rex")[0]["wizards_code_explicitly_confirmed"])
        self.assertTrue(select(current, code="ss2")[0]["wizards_card_gallery_printing_code_confirmed"])
        self.assertFalse(select(current, code="ss2")[0]["wizards_code_explicitly_confirmed"])
        self.assertTrue(select(current, code="gs1")[0]["wizards_code_explicitly_confirmed"])
        self.assertTrue(select(current, code="fdc")[0]["wizards_individual_source_review"])
        self.assertEqual(select(current, code="fdc")[0]["scryfall_release_or_first_card_date"], "2024-11-15")
        self.assertTrue(select(current, code="dvd")[0]["box_component_of_parent_product"])


if __name__ == "__main__":
    unittest.main()
