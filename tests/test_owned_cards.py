"""Offline regression tests for Cory's dated card-data overlay."""

import importlib.util
import sys
import unittest
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from build_owned_card_knowledge import load_shards, check
from owned_cards import OwnedCards, eligible


class OwnedCardKnowledgeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalogue = OwnedCards()
        cls.records = list(cls.catalogue.records())

    def test_full_source_and_allocation_reconciliation(self):
        self.assertEqual(len(self.records), 751)
        self.assertEqual(sum(c["copies_owned"] for c in self.records), 1332)
        self.assertEqual(sum(c["copies_available"] for c in self.records), 1071)
        self.assertEqual(sum(bool(c["copies_available"]) for c in self.records), 611)
        self.assertEqual(self.catalogue.manifest["index_coverage"], {"present": 663, "missing": 88})
        self.assertEqual(self.catalogue.manifest["drift"].get("oracle_text", []), [])
        check(load_shards())

    def test_new_prerelease_card_can_be_looked_up_by_name(self):
        drone = self.catalogue.get("tenacious drone")
        self.assertIsNotNone(drone)
        self.assertTrue(drone["future_only"])
        self.assertEqual(drone["legalities"]["pauper"], "not_legal")
        self.assertIsNotNone(drone["mana_value"])
        self.assertTrue(drone["oracle_id"])
        self.assertTrue(drone["rulings_uri"].startswith("https://"))

    def test_pauper_legality_does_not_equal_one_printing_rarity(self):
        strix = self.catalogue.get("Baleful Strix")
        self.assertEqual(strix["legalities"]["pauper"], "legal")
        self.assertTrue(strix["has_regular_common_printing"])
        sol_ring = self.catalogue.get("Sol Ring")
        self.assertEqual(sol_ring["legalities"]["pauper"], "not_legal")
        self.assertFalse(sol_ring["has_regular_common_printing"])
        self.assertEqual(sum(c["legalities"]["pauper"] == "legal" for c in self.records), 239)
        self.assertEqual(sum(c["legalities"]["pauper"] == "legal" and c["copies_available"] > 0
                             for c in self.records), 206)

    def test_confirmed_rebuilds_and_pauper_build_update_available_cards(self):
        # The two Commander upgrades and the Pauper build reserve their own
        # cards. The official legalities snapshot remains date-pinned.
        self.assertEqual(self.catalogue.get("Trepanation Blade")["copies_available"], 1)
        self.assertEqual(self.catalogue.get("The Unicomplex")["copies_available"], 0)
        self.assertEqual(self.catalogue.get("Vraska's Final Mercy")["copies_available"], 0)
        self.assertTrue(self.catalogue.get("The Unicomplex")["future_only"])
        self.assertEqual(self.catalogue.get("Moira, Urborg Haunt")["copies_available"], 1)
        self.assertEqual(self.catalogue.get("Kaya's Wrath")["copies_available"], 1)
        self.assertEqual(self.catalogue.get("Blood Crypt")["copies_available"], 0)
        self.assertEqual(self.catalogue.get("Hobbit Hole")["copies_available"], 0)
        self.assertEqual(self.catalogue.get("Belladonna Took")["copies_available"], 1)
        self.assertEqual(self.catalogue.get("Meticulous Commons")["copies_available"], 0)
        self.assertEqual(self.catalogue.get("Andoria")["copies_available"], 0)
        self.assertEqual(self.catalogue.get("Tome Scour")["copies_available"], 0)
        self.assertEqual(self.catalogue.get("Mind Sculpt")["copies_available"], 0)
        self.assertEqual(self.catalogue.get("Guttersnipe")["copies_available"], 3)

    def test_search_filters_color_identity_and_available_copies(self):
        pool = [c for c in self.records if eligible(c, True, "WB", True, "Creature", "")]
        self.assertTrue(pool)
        self.assertTrue(all(c["copies_available"] > 0 for c in pool))
        self.assertTrue(all(set(c["color_identity"]).issubset(set("WB")) for c in pool))
        self.assertTrue(all(c["legalities"]["pauper"] == "legal" for c in pool))

    def test_multiple_faces_and_printing_evidence(self):
        multi = [c for c in self.records if c["card_faces"]]
        self.assertGreater(len(multi), 0)
        self.assertTrue(all("name" in f and "type_line" in f for c in multi for f in c["card_faces"]))
        self.assertEqual(sum(c["future_only"] for c in self.records), 137)
        self.assertEqual(Counter(c["representative_printing_rarity"] for c in self.records),
                         Counter({"common": 281, "uncommon": 238, "rare": 195, "mythic": 37}))

    def test_main_qa_tool_resolves_the_new_and_existing_owned_cards(self):
        import mv_ask

        new = mv_ask.card("Tenacious Drone")
        self.assertIn("OWNED_COLLECTION_OVERLAY_NOT_IN_CANONICAL_INDEX", new["flags"])
        self.assertTrue(new["result"]["future_only"])
        self.assertIn("PRE", new["flags"][-1])
        original = mv_ask.card("Baleful Strix")
        self.assertNotIn("owned_collection_update", original["result"])
        old = mv_ask.card("Baleful Strix", include_owned=True)
        self.assertEqual(old["result"]["owned_collection_update"]["pauper_legality"], "legal")
        self.assertEqual(old["collection_data_as_of"], "2026-11-08")


if __name__ == "__main__":
    unittest.main()
