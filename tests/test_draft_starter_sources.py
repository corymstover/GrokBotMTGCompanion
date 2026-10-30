"""Regression tests for a dated official-source 23-product research batch."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import audit_draft_starter_sources as A


class DraftStarterSourceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.triage = json.loads(A.BASE.read_text(encoding="utf-8"))
        cls.ledger = json.loads(A.EVIDENCE.read_text(encoding="utf-8"))

    def test_23_new_reports_and_21_remaining_codes_conserve_original_848(self):
        result = A.build(self.triage, self.ledger)
        self.assertEqual(result["reviewed_batch_size"], 23)
        self.assertEqual(result["cumulative_wizards_source_reviewed_other_category_codes"], 35)
        self.assertEqual(result["cumulative_source_pending_other_category_codes"], 813)
        self.assertEqual(result["draft_starter_reviewed_prior"], 7)
        self.assertEqual(result["draft_starter_reviewed_this_batch"], 23)
        self.assertEqual(result["draft_starter_pending_after_batch"], 21)
        self.assertEqual(len(result["draft_starter_pending_codes"]), 21)
        self.assertEqual(len(result["remaining_source_pending_queue_all_other_categories"]), 813)
        self.assertEqual(35+813, 848)

    def test_bonus_sheet_and_legality_not_silently_reclassified(self):
        rows = {x["code"]: x for x in A.build(self.triage, self.ledger)["newly_wizards_reviewed"]}
        self.assertEqual(rows["sunf"]["wizards_product_group"], "component_sticker_sheet")
        self.assertEqual(rows["cmb1"]["wizards_product_group"], "mystery_booster_convention_playtest_sheet")
        self.assertFalse(rows["sunf"]["regular_premier_release_certified"])
        self.assertEqual(rows["mbc"]["new_card_legality_date_claim"]["commander"], "2026-11-13")
        self.assertEqual(rows["mbc"]["release_or_first_card_date_from_scryfall"], "2026-10-19")
        self.assertEqual(rows["und"]["wizards_product_group"], "un_set_preconstructed_box")

    def test_previous_twelve_not_mutated_and_future_only_out(self):
        output = A.build(self.triage, self.ledger)
        previously = {x["code"] for x in self.triage["all_848_released_nondigital_other_type_records"]
                      if x["wizards_individual_source_review"]}
        new = {x["code"] for x in output["newly_wizards_reviewed"]}
        self.assertFalse(previously & new)
        self.assertNotIn("trk", new)
        self.assertNotIn("ph23", new)

    def test_primary_source_tampering_duplication_and_wrong_family_rejected(self):
        a = copy.deepcopy(self.ledger)
        a["records"][0]["source_url"] = "https://example.com/guide"
        with self.assertRaisesRegex(ValueError, "Official Wizards URL"):
            A.build(self.triage, a)
        a = copy.deepcopy(self.ledger)
        a["records"].append(copy.deepcopy(a["records"][0]))
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            A.build(self.triage, a)
        a = copy.deepcopy(self.ledger)
        row = next(x for x in a["records"] if x["code"] == "sunf")
        row["group"] = "multiplayer_conspiracy_draft_booster"
        with self.assertRaisesRegex(ValueError, "improperly reclassified"):
            A.build(self.triage, a)

    def test_determinism(self):
        self.assertEqual(A.encode(A.build(self.triage, self.ledger)),
                         A.encode(A.build(self.triage, self.ledger)))


if __name__ == "__main__":
    unittest.main()
