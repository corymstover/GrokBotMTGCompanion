"""Guard five Secret Lair / Global Series family-source claims."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import audit_boxed_special_lair_global_sources as A
from product_family_lookup import load_current_index, select


class SecretLairGlobalSourcesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = json.loads(A.BASE.read_text(encoding="utf-8"))
        cls.previous = json.loads(A.PREV.read_text(encoding="utf-8"))
        cls.ledger = json.loads(A.LEDGER.read_text(encoding="utf-8"))

    def build(self, ledger=None):
        return A.build(self.base, self.previous, self.ledger if ledger is None else ledger)

    def test_five_sources_and_catalog_partition(self):
        report = self.build()
        self.assertEqual({r["code"] for r in report["reviewed_secret_lair_global_codes"]}, A.REQUIRED)
        self.assertEqual(report["cumulative_family_source_backed_codes"], 170)
        self.assertEqual(report["cumulative_source_pending_codes"], 678)
        self.assertEqual(report["boxed_source_pending_after_batch"], 11)
        self.assertEqual(170 + 678, 848)

    def test_only_global_series_has_official_explicit_code(self):
        rows = {r["code"]: r for r in self.build()["reviewed_secret_lair_global_codes"]}
        self.assertEqual({code for code, row in rows.items() if row["wizards_exact_scryfall_code_explicit"]}, {"gs1"})
        self.assertEqual(rows["gs1"]["scryfall_type"], "duel_deck")
        self.assertIn("two 60-card", rows["gs1"]["wizards_product_section"])
        for code in ("sld", "slu", "slc", "slz"):
            self.assertEqual(rows[code]["scryfall_type"], "box")
            self.assertFalse(rows[code]["wizards_exact_scryfall_code_explicit"])
        self.assertIn("ongoing", rows["sld"]["wizards_supported_relationship_note"])
        self.assertIn("Pauper", rows["slz"]["wizards_supported_relationship_note"])
        for row in rows.values():
            self.assertFalse(row["exact_deck_or_card_printing_inventory_certified"])
            self.assertFalse(row["current_format_legality_certified"])
            self.assertFalse(row["premier_set_certified"])

    def test_non_official_duplicate_and_unfounded_grade_rejected(self):
        data = copy.deepcopy(self.ledger)
        data["records"].append(copy.deepcopy(data["records"][0]))
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            self.build(data)
        data = copy.deepcopy(self.ledger)
        data["records"][0]["official_url"] = "https://unofficial.example.com/deck"
        with self.assertRaisesRegex(ValueError, "direct official"):
            self.build(data)
        data = copy.deepcopy(self.ledger)
        next(x for x in data["records"] if x["code"] == "sld")["evidence_grade"] = "official_product_code_and_release"
        with self.assertRaisesRegex(ValueError, "printed-code"):
            self.build(data)
        data = copy.deepcopy(self.ledger)
        data["records"][0]["code"] = "g17"
        with self.assertRaisesRegex(ValueError, "Unsupported"):
            self.build(data)

    def test_unchanged_prior_sources_and_live_search(self):
        self.assertEqual(A.encode(self.build()), A.encode(self.build()))
        live = load_current_index()
        self.assertGreaterEqual(live["wizards_reviewed_examples"], 170)
        self.assertLessEqual(len(select(live, only_pending=True)), 678)
        self.assertLessEqual(len(select(live, cohort=A.COHORT, only_pending=True)), 11)
        self.assertEqual(len(select(live, set_type="commander", only_pending=True)), 0)
        self.assertTrue(select(live, code="gs1")[0]["wizards_code_explicitly_confirmed"])
        self.assertTrue(select(live, code="h09")[0]["wizards_code_explicitly_confirmed"])
        self.assertTrue(select(live, code="fdc")[0]["wizards_individual_source_review"])
        self.assertEqual(select(live, code="fdc")[0]["scryfall_release_or_first_card_date"], "2024-11-15")
        self.assertFalse(select(live, code="g17")[0]["wizards_individual_source_review"])


if __name__ == "__main__":
    unittest.main()
