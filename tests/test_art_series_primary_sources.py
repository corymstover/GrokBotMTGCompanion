"""38 individual first-party Art Series collectible insert citations."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import audit_art_series_primary_sources as A
from product_family_lookup import load_current_index, select


class ArtSeriesPrimarySourcesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.inputs = [json.loads(path.read_text(encoding="utf-8"))
                      for path in (A.BASE, A.PREV, A.LEDGER)]

    def build(self, ledger=None):
        base, previous, sources = self.inputs
        return A.build(base, previous, sources if ledger is None else ledger)

    def test_all_38_art_records_and_exact_frozen_queue_conservation(self):
        result = self.build()
        self.assertEqual({r["code"] for r in result["reviewed_art_series_families"]}, A.EXPECTED_ART_CODES)
        self.assertEqual(result["cumulative_family_source_backed_codes"], 259)
        self.assertEqual(result["cumulative_source_pending_codes"], 589)
        self.assertEqual(result["remaining_promo_record_extras"], 565)
        self.assertEqual(result["remaining_promo_parent_linked_explicit"], 419)
        self.assertEqual(result["remaining_promo_without_explicit_parent"], 146)
        self.assertEqual(result["remaining_unreviewed_art_series_codes"], ["ahoc", "atla", "atle"])
        self.assertEqual(259 + len(result["remaining_source_pending_queue"]), 848)

    def test_named_art_product_evidence_does_not_certify_playable_cards(self):
        result = self.build()
        self.assertEqual(result["new_exact_wizards_code_declarations"], 0)
        by_code = {r["code"]: r for r in result["reviewed_art_series_families"]}
        self.assertEqual(by_code["amh1"]["source_grade"], "wizards_release_notes_explicit_nonplayability")
        self.assertEqual(by_code["amid"]["source_grade"], "wizards_set_product_page_art_card_inclusion")
        for row in by_code.values():
            self.assertEqual(row["scryfall_type"], "memorabilia")
            self.assertIsNotNone(row["scryfall_parent_set_code_explicit_only_unchanged"])
            self.assertFalse(row["wizards_prints_exact_scryfall_art_series_code"])
            self.assertFalse(row["standalone_premier_expansion_certified"])
            self.assertFalse(row["individual_art_printing_inventory_certified"])
            self.assertFalse(row["new_playable_card_debut_count_certified"])
            self.assertFalse(row["current_format_legality_certified"])

    def test_lookup_preserves_art_families_after_later_source_batches(self):
        data = load_current_index()
        self.assertGreaterEqual(data["wizards_reviewed_examples"], 259)
        self.assertLessEqual(len(select(data, only_pending=True)), 589)
        self.assertLessEqual(len(select(data, cohort="promotional_and_record_extras", only_pending=True)), 565)
        for code in A.EXPECTED_ART_CODES:
            row = select(data, code=code)[0]
            self.assertTrue(row["wizards_individual_source_review"])
            self.assertEqual(row["review_status"], "wizards_named_art_series_component_source_reviewed")
            self.assertFalse(row["wizards_code_explicitly_confirmed"])
            self.assertFalse(row["wizards_premier_status_certified"])
        for code in A.UNSOURCED_SUBGROUPS:
            self.assertFalse(select(data, code=code)[0]["wizards_individual_source_review"])
        self.assertTrue(select(data, code="pcbb")[0]["wizards_individual_source_review"])

    def test_forged_duplicate_third_party_and_misgraded_sources_fail(self):
        forged = copy.deepcopy(self.inputs[2])
        forged["records"].append(forged["records"][0])
        with self.assertRaisesRegex(ValueError, "Duplicated"):
            self.build(forged)
        forged = copy.deepcopy(self.inputs[2])
        forged["records"][0]["official_url"] = "https://example.invalid/art-cards"
        with self.assertRaisesRegex(ValueError, "direct official Wizards"):
            self.build(forged)
        forged = copy.deepcopy(self.inputs[2])
        next(x for x in forged["records"] if x["code"] == "amh1")["source_kind"] = "wizards_dedicated_art_gallery"
        with self.assertRaisesRegex(ValueError, "evidence grade"):
            self.build(forged)

    def test_generated_report_exact_reproducibility(self):
        self.assertEqual(A.OUTPUT.read_bytes(), A.encode(self.build()))


if __name__ == "__main__":
    unittest.main()
