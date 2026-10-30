"""Phase 1B: test second official product-family evidence overlay and scope."""
import copy
import json
import sys
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import audit_draft_starter_batch2 as B
from product_family_lookup import apply_source_overlay, apply_second_source_overlay, select


class SecondBatchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.previous = json.loads(B.OLDER.read_text(encoding="utf-8"))
        cls.evidence = json.loads(B.EVIDENCE.read_text(encoding="utf-8"))
        cls.base = json.loads(B.BASE.read_text(encoding="utf-8"))

    def audit(self, evidence=None):
        return B.build(self.previous, self.evidence if evidence is None else evidence, self.base)

    def test_all_codes_and_pending_conserved(self):
        j = self.audit()
        self.assertEqual(j["new_wizards_family_evidence_count"], 8)
        self.assertEqual(j["new_exact_code_printed_by_wizards"], 2)
        self.assertEqual(j["new_wizards_family_evidence_with_scryfall_crosswalk"], 6)
        self.assertEqual(j["cumulative_outside_category_codes_with_wizards_source_family_evidence"], 43)
        self.assertEqual(j["cumulative_outside_category_codes_individual_wizards_source_pending"], 805)
        self.assertEqual(j["draft_starter_source_pending_count"], 13)
        self.assertEqual(43+805, 848)
        self.assertEqual(len(j["still_source_pending_queue"]), 805)

    def test_source_grades_and_non_premier_limits(self):
        j = self.audit()
        x = {r["code"]: r for r in j["newly_sourced_family_evidence"]}
        self.assertEqual(x["h2r"]["wizards_family_evidence_grade"], "exact_code_and_group_primary")
        self.assertTrue(x["w17"]["wizards_explicitly_printed_set_code"])
        self.assertFalse(x["h1r"]["wizards_explicitly_printed_set_code"])
        self.assertEqual(x["ulst"]["product_family_wizards_supported"], "unfinity_collector_booster_list_insert_reprints")
        self.assertTrue(all(not r["independent_premier_status_verified"] for r in x.values()))
        self.assertTrue(all(not r["individual_card_legality_date_verified"] for r in x.values()))
        self.assertEqual(x["ptg"]["name"], "Ponies: The Galloping")

    def test_tamper_duplicate_and_source_mismatch_rejected(self):
        bad = copy.deepcopy(self.evidence)
        bad["records"][0]["url"] = "https://example.com/source"
        with self.assertRaisesRegex(ValueError, "direct Wizards"):
            self.audit(bad)
        bad = copy.deepcopy(self.evidence)
        bad["records"].append(copy.deepcopy(bad["records"][0]))
        with self.assertRaisesRegex(ValueError, "Duplicated"):
            self.audit(bad)
        bad = copy.deepcopy(self.evidence)
        bad["records"][0]["grade"] = "certified_premier"
        with self.assertRaisesRegex(ValueError, "Unrecognized evidence"):
            self.audit(bad)
        bad = copy.deepcopy(self.evidence)
        bad["records"].pop()
        with self.assertRaisesRegex(ValueError, "exactly eight"):
            self.audit(bad)

    def test_previous_read_overlay_preserved_and_deterministic(self):
        old = apply_source_overlay(self.base, self.previous)
        self.assertEqual(old["wizards_reviewed_examples"], 35)
        self.assertEqual(len([r for r in old["all_848_released_nondigital_other_type_records"]
                              if r["wizards_individual_source_review"]]), 35)
        after = apply_second_source_overlay(old, self.audit())
        self.assertEqual(after["wizards_reviewed_examples"], 43)
        self.assertEqual(after["metadata_only_pending_wizards_individual_review"], 805)
        self.assertEqual(len(select(after, only_pending=True)), 805)
        self.assertEqual(len(select(after, cohort="draft_and_starter_variants", only_pending=True)), 13)
        self.assertTrue(select(after, code="h2r")[0]["wizards_code_explicitly_confirmed"])
        self.assertFalse(select(after, code="unk")[0]["wizards_code_explicitly_confirmed"])
        self.assertEqual(B.encode(self.audit()), B.encode(self.audit()))


if __name__ == "__main__":
    unittest.main()
