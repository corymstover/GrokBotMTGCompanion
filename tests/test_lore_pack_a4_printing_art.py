"""Pack A4 regressions: exact printing traceability without tier inflation."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import audit_lore_pack_a4_printing_art as A4


class PrintingArtAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = A4.build()
        cls.cards = {c["name"]: c for c in json.loads(A4.LEDGER.read_text())["cards"]}

    def test_six_compared_images_and_twenty_variant_ids(self):
        self.assertEqual(self.report["visually_reviewed_source_to_printing_pairs"], 6)
        self.assertEqual(self.report["same_illustration_printing_ids"], 20)
        self.assertEqual(self.report["distinct_illustration_ids"], 6)
        self.assertFalse(self.report["realtime_image_or_legality_fetch"])

    def test_ugin_story_art_is_not_the_earliest_promo_art(self):
        ugin = self.cards["Ugin, the Spirit Dragon"]
        self.assertEqual(ugin["visually_reviewed_printing"]["id"],
                         "58c1e824-c8a9-4312-8e4c-a29a26d189a4")
        self.assertEqual(ugin["known_different_art_first_indexed_promo"]["id"],
                         "8cec48b8-58b2-4894-96e4-8477b83d4cf6")
        self.assertNotEqual(ugin["matched_illustration_id"],
                            ugin["known_different_art_first_indexed_promo"]["illustration_id"])

    def test_story_scene_vs_location_grades_preserved(self):
        self.assertEqual(self.cards["Crux of Fate"]["context_tier"],
                         "DIRECT_EVENT_SCENE_CAPTION")
        self.assertEqual(self.cards["Ugin's Nexus"]["context_tier"],
                         "OFFICIAL_STORY_DEVICE")
        self.assertEqual(self.cards["Tomb of the Spirit Dragon"]["context_tier"],
                         "STORY_LOCATION_ART_CAPTION")

    def test_fixed_scryfall_observation_does_not_claim_whole_deck_legality(self):
        self.assertTrue(self.report["all_six_commander_legal_at_review"])
        self.assertEqual(self.report["reviewed_at"], "2026-10-30")


if __name__ == "__main__":
    unittest.main()
