"""Exact source, snapshot, typed reprint distinction, and overlay guard tests."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import audit_reprint_curated_sources as A
from product_family_lookup import (
    apply_reprint_source_overlay, apply_source_overlay, apply_second_source_overlay, select
)

class SourceAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = json.loads(A.BASE.read_text(encoding="utf-8"))
        cls.previous = json.loads(A.PREVIOUS.read_text(encoding="utf-8"))
        cls.ledger = json.loads(A.EVIDENCE.read_text(encoding="utf-8"))

    def build(self, ledger=None):
        return A.build(self.base, self.previous, self.ledger if ledger is None else ledger)

    def test_entire_848_reconciles_to_71_and_777(self):
        j = self.build()
        self.assertEqual(j["source_reviewed_this_batch"], 28)
        self.assertEqual(j["source_confirmed_product_with_scryfall_code_crosswalk"], 27)
        self.assertEqual(j["wizards_explicitly_prints_exact_code"], 1)
        self.assertEqual(j["cumulative_wizards_family_evidence_codes"], 71)
        self.assertEqual(j["cumulative_pending_codes"], 777)
        self.assertEqual(j["reprint_curated_source_pending_codes"], ["bchr", "rin", "ss2"])
        self.assertEqual(len(j["still_source_pending_queue"]), 777)
        self.assertEqual(43+28+777, 848)

    def test_independent_booster_vs_fixed_collections_and_insert(self):
        rows={x["code"]:x for x in self.build()["newly_sourced_family_evidence"]}
        for code in ("mma","mm2","ema","mm3","ima","a25","uma","2xm","2x2","dmr","tsr","chr","mb2"):
            self.assertEqual(rows[code]["standalone_booster_classification"], "source_confirmed_booster")
        for code in ("drb","v09","v17","ss1","ss3","plst","slx"):
            self.assertEqual(rows[code]["standalone_booster_classification"], "not_assumed_standalone_booster")
        self.assertTrue(rows["slx"]["wizards_explicit_scryfall_code"])
        self.assertFalse(rows["plst"]["wizards_explicit_scryfall_code"])
        self.assertTrue(all(not x["wizards_premier_status_certified"] for x in rows.values()))

    def test_previous_reviews_untouched_and_search_up_to_date(self):
        older23 = json.loads((A.DATA/"draft_starter_primary_audit_2026-10-29.json").read_text(encoding="utf-8"))
        base=apply_source_overlay(self.base,older23)
        base=apply_second_source_overlay(base,self.previous)
        self.assertEqual(base["wizards_reviewed_examples"],43)
        new=apply_reprint_source_overlay(base,self.build())
        self.assertEqual(new["wizards_reviewed_examples"],71)
        self.assertEqual(new["metadata_only_pending_wizards_individual_review"],777)
        self.assertEqual(len(select(new,only_pending=True)),777)
        self.assertEqual(len(select(new,cohort="reprint_and_curated_products",only_pending=True)),3)
        self.assertTrue(select(new,code="ss1")[0]["wizards_individual_source_review"])
        self.assertFalse(select(new,code="ss2")[0]["wizards_individual_source_review"])
        self.assertEqual(len(select(base,cohort="reprint_and_curated_products",only_pending=True)),31)

    def test_duplicate_tamper_and_invented_wizards_code_grade_fail(self):
        m=copy.deepcopy(self.ledger);m["records"][0]["source_url"]="https://example.com/"
        with self.assertRaisesRegex(ValueError,"Non-Wizards"): self.build(m)
        m=copy.deepcopy(self.ledger);m["records"].append(copy.deepcopy(m["records"][0]))
        with self.assertRaisesRegex(ValueError,"Duplicate"): self.build(m)
        m=copy.deepcopy(self.ledger);next(x for x in m["records"] if x["code"]=="mma")["evidence_grade"]="exact_code_and_group_primary"
        with self.assertRaisesRegex(ValueError,"incorrectly promoted"):self.build(m)
        m=copy.deepcopy(self.ledger);m["records"].pop()
        with self.assertRaisesRegex(ValueError,"Wrong 28-code"):self.build(m)

    def test_deterministic_bytes(self):
        self.assertEqual(A.serialized(self.build()),A.serialized(self.build()))

if __name__=="__main__":
    unittest.main()
