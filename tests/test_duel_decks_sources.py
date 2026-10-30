"""Official Duel Decks source crosswalk, Anthology box, and 848-code conservation."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import audit_duel_decks_sources as A
from product_family_lookup import (
    apply_boxed_source_overlay, apply_duel_decks_source_overlay,
    apply_reprint_source_overlay, apply_second_source_overlay,
    apply_source_overlay, load_current_index, select,
)


class DuelDecksSourcesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = json.loads(A.BASE.read_text(encoding="utf-8"))
        cls.previous = json.loads(A.PREV.read_text(encoding="utf-8"))
        cls.evidence = json.loads(A.LEDGER.read_text(encoding="utf-8"))

    def build(self, evidence=None):
        return A.build(self.base, self.previous, self.evidence if evidence is None else evidence)

    def test_25_codes_are_22_actual_products_and_848_codes_conserved(self):
        report = self.build()
        self.assertEqual(len(report["reviewed_duel_decks_codes"]), 25)
        self.assertEqual(report["new_individual_duel_deck_box_codes"], 21)
        self.assertEqual(report["new_anthology_deck_component_codes"], 4)
        self.assertEqual(report["distinct_sold_duel_decks_products_represented"], 22)
        self.assertEqual(report["cumulative_family_source_backed_codes"], 111)
        self.assertEqual(report["cumulative_source_pending_codes"], 737)
        self.assertEqual(report["boxed_source_pending_after_batch"], 70)
        self.assertEqual(111 + 737, 848)

    def test_anthology_is_one_box_without_fabricated_scryfall_parent(self):
        rows = {r["code"]: r for r in self.build()["reviewed_duel_decks_codes"]}
        for code, original in A.ANTHOLOGY_COMPONENTS.items():
            row = rows[code]
            self.assertEqual(row["original_product_scryfall_code_when_anthology_component"], original)
            self.assertEqual(row["scryfall_explicit_parent_code_unchanged"], None)
            self.assertTrue(row["anthology_component_of_one_2014_box"])
            self.assertFalse(row["is_separately_sold_duel_decks_box"])
            self.assertEqual(row["anthology_official_box_code_when_component"], "DD3")
            self.assertEqual(row["wizards_primary_url"], A.OFFICIAL_ANTHOLOGY)
        for code in A.ORIGINAL_CODES:
            row = rows[code]
            self.assertTrue(row["is_separately_sold_duel_decks_box"])
            self.assertFalse(row["anthology_component_of_one_2014_box"])
        self.assertTrue(all(not r["premier_set_status_certified"] and not r["card_format_legality_inferred"]
                            for r in rows.values()))

    def test_unknown_duplicate_wrong_source_and_false_component_rejected(self):
        evidence = copy.deepcopy(self.evidence)
        evidence["records"].append(copy.deepcopy(evidence["records"][0]))
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            self.build(evidence)
        evidence = copy.deepcopy(self.evidence)
        evidence["records"][0]["official_product_url"] = "https://example.com/incorrect"
        with self.assertRaisesRegex(ValueError, "primary source"):
            self.build(evidence)
        evidence = copy.deepcopy(self.evidence)
        evidence["records"][0]["code"] = "gs1"
        with self.assertRaisesRegex(ValueError, "Unexpected"):
            self.build(evidence)
        evidence = copy.deepcopy(self.evidence)
        component = next(r for r in evidence["records"] if r["code"] == "dvd")
        component["family"] = "individually_sold_duel_decks_box"
        with self.assertRaisesRegex(ValueError, "Anthology component"):
            self.build(evidence)
        evidence = copy.deepcopy(self.evidence)
        component = next(r for r in evidence["records"] if r["code"] == "gvl")
        component["reprinted_original_product_scryfall_code"] = "dd2"
        with self.assertRaisesRegex(ValueError, "Anthology component"):
            self.build(evidence)

    def test_current_lookup_preserves_all_prior_evidence_and_exposes_components(self):
        prior23 = json.loads((A.DATA / "draft_starter_primary_audit_2026-10-29.json").read_text(encoding="utf-8"))
        prior8 = json.loads((A.DATA / "draft_starter_batch2_audit_2026-10-29.json").read_text(encoding="utf-8"))
        prior28 = json.loads((A.DATA / "reprint_curated_source_audit_2026-10-29.json").read_text(encoding="utf-8"))
        indexed = apply_source_overlay(self.base, prior23)
        indexed = apply_second_source_overlay(indexed, prior8)
        indexed = apply_reprint_source_overlay(indexed, prior28)
        indexed = apply_boxed_source_overlay(indexed, self.previous)
        self.assertEqual(indexed["wizards_reviewed_examples"], 86)
        current = apply_duel_decks_source_overlay(indexed, self.build())
        self.assertEqual(current["wizards_reviewed_examples"], 111)
        self.assertEqual(len(select(current, only_pending=True)), 737)
        self.assertEqual(len(select(current, cohort=A.COHORT, only_pending=True)), 70)
        self.assertEqual(len(select(current, set_type="duel_deck", only_pending=True)), 1)
        self.assertEqual(select(current, set_type="duel_deck", only_pending=True)[0]["code"], "gs1")
        self.assertTrue(select(current, code="evg")[0]["box_component_of_parent_product"])
        self.assertEqual(select(current, code="evg")[0]["wizards_anthology_official_product_code"], "DD3")
        self.assertIsNone(select(current, code="evg")[0]["parent_set_code_explicit_only"])
        self.assertFalse(select(current, code="ddu")[0]["box_component_of_parent_product"])
        self.assertEqual(len(current["all_848_released_nondigital_other_type_records"]), 848)
        self.assertEqual(load_current_index()["wizards_reviewed_examples"], 111)

    def test_report_is_reproducible_and_prior_86_762_unchanged(self):
        self.assertEqual(A.encode(self.build()), A.encode(self.build()))
        self.assertEqual(self.previous["cumulative_family_source_backed_codes"], 86)
        self.assertEqual(self.previous["cumulative_source_pending_codes"], 762)


if __name__ == "__main__":
    unittest.main()
