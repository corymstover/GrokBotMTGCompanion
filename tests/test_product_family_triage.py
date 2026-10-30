"""Portable Phase 1B product-family triage regression tests. No network or bulk download."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import audit_product_family_triage as P


class TriageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = json.loads(P.CATALOG.read_text(encoding="utf-8"))
        cls.prior = json.loads(P.PREVIOUS.read_text(encoding="utf-8"))

    def test_all_1062_codes_conserved_without_premier_inference(self):
        result = P.build(self.catalog, self.prior)
        self.assertEqual(sum(result["exclusive_whole_corpus_counts"].values()), 1062)
        self.assertEqual(result["released_nondigital_other_type_codes"], 848)
        self.assertEqual(sum(result["metadata_research_cohorts"].values()), 848)
        self.assertEqual(result["wizards_reviewed_examples"], 12)
        self.assertEqual(result["metadata_only_pending_wizards_individual_review"], 836)
        self.assertEqual(len(result["all_848_released_nondigital_other_type_records"]), 848)
        self.assertEqual(len(result["pending_836_individual_source_review_queue"]), 836)
        self.assertEqual(
            len({r["code"] for r in result["all_848_released_nondigital_other_type_records"]}), 848
        )
        self.assertEqual(
            {r["premier_release_status"] for r in result["all_848_released_nondigital_other_type_records"]},
            {"not_inferred_from_set_type"},
        )

    def test_reviewed_source_is_only_for_exact_twelve_examples(self):
        result = P.build(self.catalog, self.prior)
        rows = {r["code"]: r for r in result["all_848_released_nondigital_other_type_records"]}
        for code in ("ltr", "mh1", "mh2", "mh3", "cmm", "cmr", "j22", "pip"):
            self.assertTrue(rows[code]["wizards_individual_source_review"])
            self.assertTrue(rows[code]["wizards_primary_source"].startswith("https://magic.wizards.com"))
        for code in ("plst", "ren", "bchr", "por", "tneo", "tdmu"):
            if code not in rows:
                continue
            self.assertFalse(rows[code]["wizards_individual_source_review"])
            self.assertIsNone(rows[code]["wizards_primary_source"])
        self.assertEqual(rows["plst"]["metadata_cohort_not_official_classification"],
                         "reprint_and_curated_products")

    def test_parent_absence_is_not_claim_of_standalone_booster(self):
        rows = {
            r["code"]: r
            for r in P.build(self.catalog, self.prior)["all_848_released_nondigital_other_type_records"]
        }
        self.assertEqual(rows["afc"]["parent_set_code_explicit_only"], "afr")
        self.assertEqual(rows["afc"]["parent_association_status"], "scryfall_explicit_parent")
        self.assertIsNone(rows["plst"]["parent_set_code_explicit_only"])
        self.assertEqual(rows["plst"]["parent_association_status"],
                         "not_given_does_not_prove_standalone")

    def test_new_unknown_type_or_changed_review_is_rejected(self):
        catalog = copy.deepcopy(self.catalog)
        catalog["sets"]["plst"]["scryfall_set_type"] = "mystery_type"
        with self.assertRaisesRegex(ValueError, "Unknown released non-digital"):
            P.build(catalog, self.prior)
        prior = copy.deepcopy(self.prior)
        prior["reviewed_non_expansion_core_products"].pop()
        with self.assertRaisesRegex(ValueError, "review ledger has changed"):
            P.build(self.catalog, prior)

    def test_deterministic_and_priority_order(self):
        a = P.build(self.catalog, self.prior)
        self.assertEqual(P.encode(a), P.encode(P.build(self.catalog, self.prior)))
        queue = a["pending_836_individual_source_review_queue"]
        self.assertEqual(queue, sorted(
            queue, key=lambda x: (x["priority"], x["scryfall_set_type"],
                                  x["release"] or "", x["code"])
        ))
        self.assertEqual(queue[0]["priority"], 1)


if __name__ == "__main__":
    unittest.main()
