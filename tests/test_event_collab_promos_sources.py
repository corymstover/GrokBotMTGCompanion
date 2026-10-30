"""Seven primary-source event/collaboration program crosswalks."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import audit_event_collab_promos_sources as A
from product_family_lookup import load_current_index, select


class EventCollabPromosSourcesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = [json.loads(path.read_text(encoding="utf-8"))
                    for path in (A.BASE, A.PREV, A.LEDGER)]

    def build(self, ledger=None):
        first, second, third = self.data
        return A.build(first, second, third if ledger is None else ledger)

    def test_seven_promo_citations_and_conservation(self):
        result = self.build()
        self.assertEqual({r["code"] for r in result["reviewed_event_collab_promo_families"]}, A.REQUIRED)
        self.assertEqual(result["cumulative_family_source_backed_codes"], 221)
        self.assertEqual(result["cumulative_source_pending_codes"], 627)
        self.assertEqual(result["remaining_promo_record_extras"], 603)
        self.assertEqual(result["remaining_promo_parent_linked_explicit"], 457)
        self.assertEqual(result["remaining_promo_without_explicit_parent"], 146)
        self.assertEqual(221 + 627, 848)

    def test_program_not_code_or_complete_printing_certification(self):
        result = self.build()
        self.assertEqual(result["new_exact_wizards_code_declarations"], 0)
        by_code = {r["code"]: r for r in result["reviewed_event_collab_promo_families"]}
        self.assertEqual(by_code["gdy"]["official_source_url"], by_code["sch"]["official_source_url"])
        self.assertNotEqual(by_code["gdy"]["officially_supported_product_family"], by_code["sch"]["officially_supported_product_family"])
        self.assertEqual(by_code["pr23"]["official_source_publication_date"], "2022-10-04")
        self.assertEqual(by_code["pspl"]["official_source_publication_date"], "2024-08-20")
        for row in by_code.values():
            self.assertFalse(row["wizards_prints_exact_scryfall_code"])
            self.assertFalse(row["standalone_premier_expansion_certified"])
            self.assertFalse(row["individual_card_printing_inventory_certified"])
            self.assertFalse(row["new_card_debut_count_certified"])
            self.assertFalse(row["current_format_legality_certified"])

    def test_live_lookup_preserves_all_seven_after_later_batches(self):
        report = load_current_index()
        self.assertGreaterEqual(report["wizards_reviewed_examples"], 221)
        self.assertLessEqual(len(select(report, only_pending=True)), 627)
        self.assertLessEqual(len(select(report, cohort="promotional_and_record_extras", only_pending=True)), 603)
        for code in sorted(A.REQUIRED):
            record = select(report, code=code)[0]
            self.assertTrue(record["wizards_individual_source_review"])
            self.assertFalse(record["wizards_code_explicitly_confirmed"])
            self.assertEqual(record["parent_set_code_explicit_only"], None)
        self.assertTrue(select(report, code="pl26")[0]["wizards_individual_source_review"])
        self.assertFalse(select(report, code="plny")[0]["wizards_individual_source_review"])

    def test_forged_source_duplicate_wrong_program_and_language_fail(self):
        tampered = copy.deepcopy(self.data[2])
        tampered["records"].append(tampered["records"][0])
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            self.build(tampered)
        tampered = copy.deepcopy(self.data[2])
        tampered["records"][0]["official_url"] = "https://third-party.invalid/game-day"
        with self.assertRaisesRegex(ValueError, "first-party"):
            self.build(tampered)
        tampered = copy.deepcopy(self.data[2])
        next(x for x in tampered["records"] if x["code"] == "pmda")["evidence_grade"] = "wizards_dated_program_family"
        with self.assertRaisesRegex(ValueError, "Misgraded"):
            self.build(tampered)
        tampered = copy.deepcopy(self.data[2])
        next(x for x in tampered["records"] if x["code"] == "pr23")["official_section"] = "An unrelated 2023 card set without a program name or any primary promotional event citation whatsoever."
        with self.assertRaisesRegex(ValueError, "Missing dated"):
            self.build(tampered)

    def test_generated_report_is_byte_exact(self):
        self.assertEqual(A.OUTPUT.read_bytes(), A.encode(self.build()))


if __name__ == "__main__":
    unittest.main()
