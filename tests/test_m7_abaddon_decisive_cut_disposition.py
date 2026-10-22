"""Verify integrity/authority of Abaddon's authored cut-decision record.

Structural tests only: a passing test cannot decide card quality, prove
multiplayer advantage or substitute for remaining M6 I/J/P0 certifications.
"""
from __future__ import annotations

from collections import Counter
import hashlib
import json
from pathlib import Path
import unittest

from scripts.grixis_m7_decision_gate import parse_list

ROOT = Path(__file__).resolve().parents[1]
WORKING = ROOT / "data/grixis/m7/research_challengers"
PACKET = WORKING / "Abaddon_the_Despoiler_portfolio_v3_decisive.json"
PRIOR = WORKING / "Abaddon_the_Despoiler_portfolio_v2.json"
CANONICAL = ROOT / "data/grixis/m7/authority_snapshots/Abaddon_the_Despoiler_Approved_2026-10-13.txt"
SOURCE = ROOT / "exports/grixis-archidekt/source-baseline/abaddon-the-despoiler.txt"
EXPECTED_DECISIONS = {
    "Grinning Ignus": "SELECT_ADD",
    "Chaos Warp": "SELECT_ADD",
    "Aggravated Assault": "RETAIN_ALTERNATIVE",
    "The Ruinous Powers": "RETAIN_BASELINE",
    "Keeper of Secrets": "RETAIN_BASELINE",
    "Inevitable Betrayal": "SELECT_CUT",
}
PRESERVED = {
    "The Lost and the Damned", "The Ruinous Powers", "Call Forth the Tempest",
    "Keeper of Secrets", "Loyal Subordinate", "Neheb, the Eternal",
    "Birgi, God of Storytelling // Harnfel, Horn of Bounty",
    "Underworld Breach", "Brain Freeze", "Lion's Eye Diamond"
}
LANDS = set(("Ancient Tomb|Badlands|Blood Crypt|Bloodstained Mire|City of Brass|"
             "Command Tower|Exotic Orchard|Flooded Strand|Island|Luxury Suite|"
             "Mana Confluence|Marsh Flats|Misty Rainforest|Morphic Pool|Mountain|"
             "Otawara, Soaring City|Polluted Delta|Scalding Tarn|Steam Vents|"
             "Swamp|Takenuma, Abandoned Mire|Training Center|Underground Sea|"
             "Urborg, Tomb of Yawgmoth|Verdant Catacombs|Volcanic Island|"
             "Watery Grave|Xander's Lounge").split("|"))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


class AbaddonAuthoredDecisiveComparison(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.v3 = json.loads(PACKET.read_text(encoding="utf-8"))
        cls.v2 = json.loads(PRIOR.read_text(encoding="utf-8"))
        cls.original, cls.commander, cls.companions = parse_list(SOURCE)
        cls.selected, cls.cmd_final, cls.comp_final = parse_list(
            ROOT / cls.v3["proposed"]["file"])
        cls.alternative, cls.cmd_alt, cls.comp_alt = parse_list(
            ROOT / cls.v3["competing"]["file"])

    def test_raw_approved_bytes_authority_bound_without_canonical_edit(self):
        self.assertEqual(digest(CANONICAL),
                         "2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf")
        self.assertEqual(self.v3["canonical"]["approved_sha256"], digest(CANONICAL))
        self.assertEqual(self.v3["canonical"]["approval"], "APPROVED_LOCKED_UNCHANGED")
        self.assertTrue(self.v3["no_canonical_changes"])
        self.assertFalse(self.v3["owner_approved"])
        self.assertFalse(self.v3["m6_certified"])
        self.assertFalse(self.v3["gates"]["m7_final_owner_ready"])

    def test_competing_exact_100_card_samed_source_real_diff(self):
        for identifier, obj, cmd, companions in (
            ("selected", self.selected, self.cmd_final, self.comp_final),
            ("alternative", self.alternative, self.cmd_alt, self.comp_alt),
        ):
            with self.subTest(id=identifier):
                self.assertEqual(len(obj), 100)
                self.assertEqual(len(set(obj)), 94)
                self.assertEqual(cmd, self.commander)
                self.assertEqual(companions, self.companions)
                self.assertEqual(sum(n in LANDS for n in obj), 34)
                self.assertTrue(PRESERVED <= set(obj) if identifier == "selected"
                                else PRESERVED - {"Keeper of Secrets"} <= set(obj))
                manifest = self.v3["proposed" if identifier == "selected" else "competing"]
                self.assertEqual(digest(ROOT / manifest["file"]), manifest["physical_sha256"])
                self.assertEqual(Counter(obj) - Counter(self.original),
                                 Counter(manifest["adds"]))
                self.assertEqual(Counter(self.original) - Counter(obj),
                                 Counter(manifest["cuts"]))
        self.assertIn("Keeper of Secrets", self.selected)
        self.assertNotIn("Inevitable Betrayal", self.selected)
        self.assertIn("Inevitable Betrayal", self.alternative)
        self.assertNotIn("Keeper of Secrets", self.alternative)

    def test_material_judgments_complete_no_hold_and_match_changes(self):
        j = self.v3["material_judgments"]
        actual = {r["card"]: r["disposition"] for r in j}
        self.assertEqual(actual, EXPECTED_DECISIONS)
        self.assertEqual(len(actual), len(j))
        selected = {r["card"] for r in j if r["disposition"] == "SELECT_ADD"}
        cuts = {r["card"] for r in j if r["disposition"] == "SELECT_CUT"}
        self.assertEqual(selected, set(self.v3["proposed"]["adds"]))
        self.assertEqual(cuts - {"Rakdos, Lord of Riots"},
                         {"Inevitable Betrayal"})
        for item in j:
            self.assertGreater(len(item["reason"]), 80)
            self.assertIn(item["confidence"], ("HIGH", "MODERATE", "LOW_WITH_DISCLOSED_LIMITS"))
            self.assertNotIn(item["disposition"], ("HOLD", "NO_PROVEN_UPGRADE", "KEEP_BY_DEFAULT"))

    def test_historical_v2_lead_preserved_as_competitor_not_mutated(self):
        self.assertEqual(self.v2["current_preliminary_choice"], "engine_answer_keeper")
        self.assertEqual(self.v3["proposed"]["id"], "engine_answer_betrayal")
        self.assertEqual(self.v3["competing"]["id"], "engine_answer_keeper")
        self.assertIn("MV0", self.v3["strongest_counterargument"])

    def test_explicit_oracle_evidence_coverage_and_not_a_certification(self):
        src = self.v3["source_evidence"]
        self.assertEqual(src["scryfall_verified_unique_names"], 97)
        self.assertIn("39740268083", src["scryfall_live_run"])
        self.assertEqual(src["scryfall_artifact_id"], 12407954955)
        self.assertEqual(self.v3["test_decision"]["new_random_trials"], 0)
        self.assertEqual(self.v3["gates"]["m6_6"], "PARTIAL")
        self.assertEqual(self.v3["gates"]["m6_8"], "BLOCKED")
        self.assertEqual(self.v3["gates"]["m6_9"], "BLOCKED")
        self.assertEqual(self.v3["gates"]["m6_10"], "BLOCKED")
        self.assertEqual(self.v3["gates"]["m7_new_approvals"], 0)


if __name__ == "__main__":
    unittest.main()
