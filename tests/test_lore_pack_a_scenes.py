"""Regression checks for direct scene art versus location/character captions."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import audit_lore_pack_a_scenes as SC


class TarkirArtContextTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.src = json.loads(SC.INPUT.read_text(encoding="utf-8"))
        cls.report = SC.build()

    def test_report_replay_and_source_scope(self):
        self.assertEqual(SC.OUTPUT.read_bytes(), SC.encode(self.report))
        self.assertEqual((self.report["claims"], self.report["entities"],
                          self.report["primary_sources"], self.report["graded_art_context_cards"]),
                         (8, 7, 6, 6))
        self.assertEqual(self.report["result"], "OFFICIAL_STORY_SCENE_AND_HISTORICAL_NAME_JOIN_PASS")

    def test_direct_scene_is_sole_crux_caption(self):
        direct = [c for c in self.report["cards"]
                  if c["art_context_tier"] == "DIRECT_EVENT_SCENE_CAPTION"]
        self.assertEqual(len(direct), 1)
        self.assertEqual(direct[0]["name"], "Crux of Fate")
        self.assertEqual(direct[0]["source_ids"], ["reforged_chain"])
        self.assertFalse(direct[0]["specific_artist_to_printing_id_match_proven"])

    def test_every_card_id_and_printing_is_real_but_variant_art_uncertified(self):
        cards = self.report["cards"]
        self.assertEqual(len({c["oracle_id"] for c in cards}), 6)
        self.assertTrue(all(c["historical_english_paper_printings"] >= 1 for c in cards))
        self.assertTrue(all(c["first_indexed_english_paper_printing"]["printing_id"] for c in cards))
        self.assertTrue(all(c["specific_artist_to_printing_id_match_proven"] is False for c in cards))
        self.assertTrue(self.report["all_six_historical_identity_colors_fit_grixis"])

    def test_story_branch_and_caption_grades_not_collapsed(self):
        claims = {c["id"]: c for c in self.src["claims"]}
        self.assertEqual(claims["A028"]["continuity"], "revised Tarkir timeline created by intervention")
        self.assertEqual(claims["A030"]["source_ids"], ["reforged_chain"])
        tiers = {c["name"]: c["tier"] for c in self.src["card_art_context"]}
        self.assertEqual(tiers["Ugin's Nexus"], "OFFICIAL_STORY_DEVICE")
        self.assertEqual(tiers["Tomb of the Spirit Dragon"], "STORY_LOCATION_ART_CAPTION")
        self.assertEqual(tiers["Ugin, the Spirit Dragon"], "NAMED_CHARACTER_ART_IN_STORY")


if __name__ == "__main__":
    unittest.main()
