"""Thirty-four primary-source booster, Commander and supplemental token families."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import audit_token_families_primary_sources as A
from product_family_lookup import load_current_index, select


class TokenFamiliesPrimarySourcesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.inputs = [json.loads(path.read_text(encoding="utf-8"))
                      for path in (A.BASE, A.PREV, A.LEDGER)]

    def build(self, ledger=None):
        base, prev, sources = self.inputs
        return A.build(base, prev, sources if ledger is None else ledger)

    def test_34_token_families_18_first_party_sources_848_code_conservation(self):
        r = self.build()
        self.assertEqual({x["code"] for x in r["reviewed_token_product_families"]}, set(A.EXPECTED_PARENTS))
        self.assertEqual(r["official_token_articles_cited"], 18)
        self.assertEqual(r["cumulative_family_source_backed_codes"], 293)
        self.assertEqual(r["cumulative_source_pending_codes"], 555)
        self.assertEqual(r["remaining_promo_record_extras"], 531)
        self.assertEqual(r["remaining_promo_parent_linked_explicit"], 385)
        self.assertEqual(r["remaining_promo_without_explicit_parent"], 146)
        self.assertEqual(293 + len(r["remaining_source_pending_queue"]), 848)

    def test_official_products_not_literal_scryfall_token_codes(self):
        r = self.build()
        self.assertEqual(r["new_exact_wizards_token_code_declarations"], 0)
        rows = {x["code"]: x for x in r["reviewed_token_product_families"]}
        self.assertEqual(rows["tbig"]["wizards_product_context"], "supplemental_booster")
        self.assertEqual(rows["totc"]["wizards_product_context"], "commander_decks")
        self.assertEqual(rows["tfin"]["wizards_product_context"], "main_booster")
        for code, source in rows.items():
            self.assertEqual(source["scryfall_type"], "token")
            self.assertEqual(source["scryfall_parent_set_code_explicit_only_unchanged"], A.EXPECTED_PARENTS[code])
            self.assertFalse(source["wizards_prints_exact_scryfall_token_code"])
            self.assertFalse(source["standalone_premier_expansion_certified"])
            self.assertFalse(source["individual_token_printing_inventory_certified"])
            self.assertFalse(source["new_playable_card_debut_count_certified"])
            self.assertFalse(source["current_format_legality_certified"])

    def test_live_lookup_and_previous_evidence_untouched(self):
        r = load_current_index()
        self.assertEqual(r["wizards_reviewed_examples"], 293)
        self.assertEqual(len(select(r, only_pending=True)), 555)
        self.assertEqual(len(select(r, cohort="promotional_and_record_extras", only_pending=True)), 531)
        for code in A.EXPECTED_PARENTS:
            x = select(r, code=code)[0]
            self.assertTrue(x["wizards_individual_source_review"])
            self.assertEqual(x["review_status"], "wizards_named_token_product_family_source_reviewed")
            self.assertFalse(x["wizards_code_explicitly_confirmed"])
            self.assertFalse(x["wizards_premier_status_certified"])
        self.assertTrue(select(r, code="amh1")[0]["wizards_individual_source_review"])
        self.assertFalse(select(r, code="atla")[0]["wizards_individual_source_review"])
        self.assertFalse(select(r, code="ttmc")[0]["wizards_individual_source_review"])
        self.assertFalse(select(r, code="wmkm")[0]["wizards_individual_source_review"])

    def test_duplicate_third_party_wrong_context_and_insufficient_notes_rejected(self):
        forged = copy.deepcopy(self.inputs[2]); forged["records"].append(forged["records"][0])
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            self.build(forged)
        forged = copy.deepcopy(self.inputs[2]); forged["records"][0]["official_url"] = "https://unofficial.invalid/tokens"
        with self.assertRaisesRegex(ValueError, "first-party"):
            self.build(forged)
        forged = copy.deepcopy(self.inputs[2]); next(x for x in forged["records"] if x["code"]=="twoc")["token_context"] = "main_booster"
        with self.assertRaisesRegex(ValueError, "Wrong product context"):
            self.build(forged)
        forged = copy.deepcopy(self.inputs[2]); forged["records"][0]["specific_source_note"] = "tokens"
        with self.assertRaisesRegex(ValueError, "concrete family-specific evidence"):
            self.build(forged)

    def test_generated_report_replays_byte_exact(self):
        self.assertEqual(A.OUTPUT.read_bytes(), A.encode(self.build()))


if __name__ == "__main__":
    unittest.main()
