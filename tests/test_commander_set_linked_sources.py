"""Primary-source review of twelve 2020–2022 Commander release-family codes."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import audit_commander_set_linked_sources as A
from product_family_lookup import (
    apply_commander_set_linked_source_overlay, load_current_index, select,
)


class SetLinkedCommanderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = json.loads(A.BASE.read_text(encoding="utf-8"))
        cls.previous = json.loads(A.PREV.read_text(encoding="utf-8"))
        cls.ledger = json.loads(A.LEDGER.read_text(encoding="utf-8"))

    def build(self, ledger=None):
        return A.build(self.base, self.previous, self.ledger if ledger is None else ledger)

    def test_all_twelve_source_codes_conserve_848_and_boxed_cohort(self):
        report = self.build()
        self.assertEqual(len(report["reviewed_commander_set_linked_codes"]), 12)
        self.assertEqual(report["new_source_backed_commander_release_codes"], 12)
        self.assertEqual(report["cumulative_family_source_backed_codes"], 132)
        self.assertEqual(report["cumulative_source_pending_codes"], 716)
        self.assertEqual(report["boxed_source_pending_after_batch"], 49)
        self.assertEqual(132 + 716, 848)

    def test_official_release_family_sources_do_not_claim_printing_or_legality(self):
        records = {r["code"]: r for r in self.build()["reviewed_commander_set_linked_codes"]}
        self.assertEqual(set(records), A.REQUIRED)
        for code, row in records.items():
            self.assertEqual(row["scryfall_type"], "commander")
            self.assertIn("magic.wizards.com/en/news/", row["wizards_primary_url"])
            self.assertFalse(row["wizards_exact_scryfall_code_confirmed"])
            self.assertFalse(row["decklist_exact_card_printing_inventory_certified"])
            self.assertFalse(row["new_card_count_certified"])
            self.assertFalse(row["card_legality_inferred"])
            self.assertFalse(row["premier_set_certified"])

    def test_unsafe_research_evidence_mutations_rejected(self):
        data = copy.deepcopy(self.ledger)
        data["records"].append(copy.deepcopy(data["records"][0]))
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            self.build(data)
        data = copy.deepcopy(self.ledger)
        data["records"][0]["official_url"] = "https://example.net/commander"
        with self.assertRaisesRegex(ValueError, "direct Wizards"):
            self.build(data)
        data = copy.deepcopy(self.ledger)
        data["records"][0]["code"] = "c20"
        with self.assertRaisesRegex(ValueError, "Unsupported"):
            self.build(data)
        data = copy.deepcopy(self.ledger)
        data["records"][0]["source_section"] = "not independently cited"
        with self.assertRaisesRegex(ValueError, "precise product"):
            self.build(data)
        data = copy.deepcopy(self.ledger)
        data["records"][0]["official_url"] = data["records"][1]["official_url"]
        with self.assertRaisesRegex(ValueError, "Duplicate URL"):
            self.build(data)

    def test_lookup_adds_twelve_without_overwriting_previous_120(self):
        self.assertEqual(self.previous["cumulative_family_source_backed_codes"], 120)
        live = load_current_index()
        self.assertEqual(live["wizards_reviewed_examples"], 132)
        self.assertEqual(len(select(live, only_pending=True)), 716)
        self.assertEqual(len(select(live, cohort=A.COHORT, only_pending=True)), 49)
        self.assertEqual(len(select(live, set_type="commander", only_pending=True)), 19)
        self.assertTrue(select(live, code="znc")[0]["wizards_individual_source_review"])
        self.assertFalse(select(live, code="who")[0]["wizards_individual_source_review"])
        self.assertTrue(select(live, code="c17")[0]["wizards_individual_source_review"])
        self.assertTrue(select(live, code="dvd")[0]["box_component_of_parent_product"])

    def test_deterministic_derived_audit(self):
        self.assertEqual(A.encode(self.build()), A.encode(self.build()))


if __name__ == "__main__":
    unittest.main()
