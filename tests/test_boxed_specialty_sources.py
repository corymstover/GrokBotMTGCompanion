"""Fourteen bounded Wizards source reviews of boxed and premium decks."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import audit_boxed_specialty_sources as A
from product_family_lookup import load_current_index, select


class SpecialtyBoxTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = json.loads(A.BASE.read_text(encoding="utf-8"))
        cls.previous = json.loads(A.PREV.read_text(encoding="utf-8"))
        cls.ledger = json.loads(A.LEDGER.read_text(encoding="utf-8"))

    def build(self, ledger=None):
        return A.build(self.base, self.previous, self.ledger if ledger is None else ledger)

    def test_exact_fourteen_evidence_codes_and_848_partition(self):
        report = self.build()
        self.assertEqual({x["code"] for x in report["reviewed_boxed_specialty_codes"]}, A.REQUIRED)
        self.assertEqual(report["source_reviewed_this_batch"], 14)
        self.assertEqual(report["cumulative_family_source_backed_codes"], 165)
        self.assertEqual(report["cumulative_source_pending_codes"], 683)
        self.assertEqual(report["boxed_source_pending_after_batch"], 16)
        self.assertEqual(165 + 683, 848)

    def test_japanese_wizards_explicit_codes_stronger_than_family_crosswalk(self):
        rows = {x["code"]: x for x in self.build()["reviewed_boxed_specialty_codes"]}
        self.assertEqual({code for code, row in rows.items() if row["wizards_exact_scryfall_code_explicit"]}, A.EXPLICIT_WIZARDS_CODES)
        for code, row in rows.items():
            self.assertFalse(row["exact_deck_printing_inventory_certified"])
            self.assertFalse(row["individual_card_legality_certified"])
            self.assertFalse(row["new_card_count_certified"])
            self.assertFalse(row["premier_set_certified"])
            if code in A.EXPLICIT_WIZARDS_CODES:
                self.assertIn("mtg-jp.com/products/", row["wizards_primary_url"])
                self.assertIn(code.upper(), row["wizards_product_section"])

    def test_shared_2018_game_night_and_gift_pack_are_separate_sections(self):
        rows = {x["code"]: x for x in self.build()["reviewed_boxed_specialty_codes"]}
        self.assertEqual(rows["g18"]["wizards_primary_url"], rows["gnt"]["wizards_primary_url"])
        self.assertNotEqual(rows["g18"]["wizards_product_section"], rows["gnt"]["wizards_product_section"])
        self.assertIn("Gift Pack", rows["g18"]["wizards_product_section"])
        self.assertIn("Game Night", rows["gnt"]["wizards_product_section"])

    def test_unsourced_code_wrong_domain_duplicate_grade_and_date_rejected(self):
        bad = copy.deepcopy(self.ledger)
        bad["records"].append(copy.deepcopy(bad["records"][0]))
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            self.build(bad)
        bad = copy.deepcopy(self.ledger)
        bad["records"][0]["official_url"] = "https://unofficial.example.com/decks"
        with self.assertRaisesRegex(ValueError, "direct official"):
            self.build(bad)
        bad = copy.deepcopy(self.ledger)
        next(x for x in bad["records"] if x["code"] == "gk1")["source_grade"] = "official_product_code_and_release"
        with self.assertRaisesRegex(ValueError, "printed-code evidence"):
            self.build(bad)
        bad = copy.deepcopy(self.ledger)
        bad["records"][0]["code"] = "c17"
        with self.assertRaisesRegex(ValueError, "Unsupported"):
            self.build(bad)

    def test_prior_history_and_live_lookup(self):
        self.assertEqual(A.encode(self.build()), A.encode(self.build()))
        current = load_current_index()
        self.assertGreaterEqual(current["wizards_reviewed_examples"], 165)
        self.assertLessEqual(len(select(current, only_pending=True)), 683)
        self.assertLessEqual(len(select(current, cohort=A.COHORT, only_pending=True)), 16)
        self.assertEqual(len(select(current, set_type="commander", only_pending=True)), 0)
        self.assertTrue(select(current, code="md1")[0]["wizards_code_explicitly_confirmed"])
        self.assertTrue(select(current, code="q06")[0]["wizards_individual_source_review"])
        self.assertTrue(select(current, code="fdc")[0]["wizards_individual_source_review"])
        self.assertEqual(select(current, code="fdc")[0]["scryfall_release_or_first_card_date"], "2024-11-15")
        self.assertTrue(select(current, code="dvd")[0]["box_component_of_parent_product"])


if __name__ == "__main__":
    unittest.main()
