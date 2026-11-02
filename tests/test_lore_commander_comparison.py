"""Source-graded alternative commanders without pilot/list approval."""
import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_lore_commander_comparison as C


class LoreCommanderComparisonTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = C.build()

    def test_all_three_pilots_compare_two_color_eligible_commanders(self):
        self.assertEqual(len(self.report["pilots"]), 3)
        for group in self.report["pilots"]:
            self.assertEqual(len(group["candidates"]), 2)
            self.assertEqual(group["number_eligible_to_host_color_pool"], 2)
            self.assertEqual(sum(row["currently_selected"] for row in group["candidates"]), 1)
            self.assertTrue(group["draft_status"].startswith("UNAPPROVED"))
            for row in group["candidates"]:
                self.assertTrue(row["eligible_commander_in_dated_model"])
                self.assertTrue(row["candidate_index_source"].startswith("cards/"))
        self.assertEqual(self.report["card_index_date"], "2026-10-15")
        self.assertLess(self.report["comprehensive_rules_effective"],
                        self.report["newer_rules_bulletin"])

    def test_distinguishes_verified_story_from_creative_thematic_link(self):
        one, two, three = self.report["pilots"]
        self.assertTrue(all(row["verified_first_party_story_source"].startswith("https://magic.wizards.com/")
                            for row in one["candidates"]))
        self.assertTrue(all(row["verified_first_party_story_source"] is None
                            for row in two["candidates"]))
        self.assertTrue(three["candidates"][0]["verified_first_party_story_source"])
        self.assertIsNone(three["candidates"][1]["verified_first_party_story_source"])
        self.assertEqual(three["candidates"][1]["story_context_grade"], "NO_VERIFIED_UGIN_ALLY_LINK")

    def test_report_rebuilds_exactly(self):
        self.assertEqual(json.loads(C.OUT.read_text(encoding="utf-8")), self.report)

    def _alter(self, change):
        doc = copy.deepcopy(json.loads(C.SPEC.read_text(encoding="utf-8")))
        change(doc)
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "candidate.json"
            path.write_text(json.dumps(doc), encoding="utf-8")
            with self.assertRaises(ValueError):
                C.build(path)

    def test_fake_new_card_fails_closed(self):
        self._alter(lambda d: d["pilots"][0]["candidates"][1].update(name="Invented Bolas Commander"))

    def test_uncited_thematic_card_cannot_claim_official_story_grade(self):
        self._alter(lambda d: d["pilots"][1]["candidates"][1].update(context="CURATED_OFFICIAL_SOURCE"))

    def test_duplicate_or_missing_original_commander_fails(self):
        self._alter(lambda d: d["pilots"][0]["candidates"][1].update(
            name="Nicol Bolas, the Ravager // Nicol Bolas, the Arisen"))

    def test_no_unsupported_current_rules_or_owner_certification(self):
        combined = " ".join(self.report["limitations"])
        self.assertIn("Not a live", combined)
        self.assertIn("UNAPPROVED", combined)
        self.assertNotIn("CURRENT_RULES_CERTIFIED", json.dumps(self.report))


if __name__ == "__main__":
    unittest.main()
