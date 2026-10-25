"""Independent owner-review verification for Loki M7 Rev1.

Finite Oracle/structural checks only. No multiplayer win rate and no owner lock.
The preceding two-swap GrokBot M7 candidate remains archived unchanged.
"""
from __future__ import annotations

import hashlib
import json
import re
import unittest
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DECK_ID = "Loki__the_Deceiver"
BASE = ROOT / "data/grixis/m7/baseline_sources/Loki__the_Deceiver_approved_source_2026-10-14.txt"
CAND = ROOT / "data/grixis/m7/candidate_lists/Loki__the_Deceiver_ChatGPT_Rev1.txt"
ORACLE = ROOT / "data/grixis/m6/oracle_snapshots/Loki__the_Deceiver_M7_Scryfall_20261023.json"
REVIEW = ROOT / "data/grixis/m7/decision_reviews/Loki__the_Deceiver_ChatGPT_Rev1_20261025.md"
BASE_SHA = "5079291c08c5af212b3d90d63ac5b01849d45c7700b1d64100ef57fb13458062"
CAND_SHA = "919734ad1f60e56a636561815d319ec1eb0fbd0c233265ad5e85064f589c7185"
SWAPS = {
    "Sakashima of a Thousand Faces": "Thunderbolts Conspiracy",
    "Elektra, Daughter of the Hand": "Kang Prime",
    "Ultimo, Civilization's End": "Doctor Octopus, Master Planner",
    "M.O.D.O.K., Evil Intellect": "Venom, Eddie Brock",
    "Living Lies of Loki": "Kang, Temporal Tyrant",
    "Kid Loki": "Dark Ritual",
    "City of Brass": "Path of Ancestry",
}
BASICS = {"Island", "Mountain", "Swamp"}


def parse(path: Path) -> tuple[Counter, list[str]]:
    rows = [line for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    entries = Counter()
    for row in rows:
        m = re.fullmatch(r"(\d+)x (.+?)( \[Commander\])?", row)
        if not m:
            raise AssertionError(f"Invalid deck row: {row!r}")
        entries[m.group(2)] += int(m.group(1))
    return entries, rows


class LokiM7Rev1IndependentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.baseline, cls.baseline_rows = parse(BASE)
        cls.candidate, cls.candidate_rows = parse(CAND)
        cls.oracle = {card["name"]: card for card in json.loads(ORACLE.read_text())["cards"]}

    def test_approved_baseline_untouched_and_candidate_byte_exact(self):
        self.assertEqual(hashlib.sha256(BASE.read_bytes()).hexdigest(), BASE_SHA)
        self.assertEqual(hashlib.sha256(CAND.read_bytes()).hexdigest(), CAND_SHA)
        self.assertEqual(self.baseline_rows[0], "1x Loki, the Deceiver [Commander]")
        self.assertEqual(self.candidate_rows[0], "1x Loki, the Deceiver [Commander]")
        self.assertEqual(self.candidate["Loki, the Deceiver"], 1)

    def test_exact_seven_substitutions_no_padding(self):
        self.assertEqual(dict(self.candidate - self.baseline), {name: 1 for name in SWAPS})
        self.assertEqual(dict(self.baseline - self.candidate), {name: 1 for name in SWAPS.values()})
        self.assertEqual(len(SWAPS), 7)
        self.assertTrue(all(self.baseline[cut] == 1 for cut in SWAPS.values()))
        self.assertTrue(all(self.baseline[add] == 0 for add in SWAPS))

    def test_100_cards_95_names_and_singleton(self):
        self.assertEqual(sum(self.candidate.values()), 100)
        self.assertEqual(len(self.candidate), 95)
        self.assertEqual(len(self.candidate_rows), 95)
        self.assertEqual({k: v for k, v in self.candidate.items() if v > 1},
                         {"Island": 3, "Mountain": 2, "Swamp": 3})
        self.assertEqual(sum(row.endswith("[Commander]") for row in self.candidate_rows), 1)
        self.assertEqual(len(self.candidate) - 1, 94)

    def test_all_selected_names_grixis_and_officially_legal_from_archived_current_oracle(self):
        self.assertEqual(set(self.candidate) - set(self.oracle), set())
        for name in self.candidate:
            record = self.oracle[name]
            self.assertEqual(record["commander_legality"], "legal", name)
            self.assertTrue(set(record["color_identity"]) <= {"U", "B", "R"}, name)
            self.assertLessEqual(record["released_at"], "2026-10-25", name)
        self.assertEqual(self.oracle["Loki, the Deceiver"]["set"], "msc")
        self.assertEqual(self.oracle["Loki, the Deceiver"]["released_at"], "2026-06-26")
        self.assertEqual(sorted(n for n in self.candidate if self.oracle[n]["game_changer"]),
                         sorted(["Cyclonic Rift", "Demonic Tutor", "Fierce Guardianship",
                                 "Jeska's Will", "Rhystic Study"]))

    def test_structural_changes_preserve_lands_and_improve_early_targets_and_curve(self):
        def land_count(entries):
            return sum(count for n, count in entries.items() if "Land" in self.oracle[n]["type_line"])
        def cheap_villain_count(entries):
            return sum(count for n, count in entries.items()
                       if n != "Loki, the Deceiver"
                       and "Creature" in self.oracle[n]["type_line"]
                       and "Villain" in self.oracle[n]["type_line"]
                       and self.oracle[n]["cmc"] <= 3)
        def nonland_mean(entries):
            mana = sum(self.oracle[n]["cmc"] * count for n, count in entries.items()
                       if n != "Loki, the Deceiver" and "Land" not in self.oracle[n]["type_line"])
            number = sum(count for n, count in entries.items()
                         if n != "Loki, the Deceiver" and "Land" not in self.oracle[n]["type_line"])
            return mana / number
        self.assertEqual(land_count(self.baseline), 34)
        self.assertEqual(land_count(self.candidate), 34)
        self.assertEqual((cheap_villain_count(self.baseline), cheap_villain_count(self.candidate)),
                         (10, 12))
        self.assertLess(nonland_mean(self.candidate), nonland_mean(self.baseline))

    def test_commander_copy_and_repeatable_etb_sources_bound_to_oracle(self):
        o = self.oracle
        self.assertIn("create a tapped and attacking token", o["Loki, the Deceiver"]["oracle_text"])
        self.assertIn("another target Villain", o["Loki, the Deceiver"]["oracle_text"])
        self.assertIn("Sacrifice that token at the beginning of the next end step",
                      o["Loki, the Deceiver"]["oracle_text"])
        self.assertIn("Whenever one or more Villains you control deal combat damage",
                      o["Loki, the Deceiver"]["oracle_text"])
        self.assertIn("may have Sakashima enter as a copy of another creature you control",
                      o["Sakashima of a Thousand Faces"]["oracle_text"])
        self.assertIn('The "legend rule" doesn\'t apply to permanents you control',
                      o["Sakashima of a Thousand Faces"]["oracle_text"])
        self.assertIn("When Ultimo enters, each opponent sacrifices a creature",
                      o["Ultimo, Civilization's End"]["oracle_text"])
        self.assertIn("When Elektra enters, destroy target creature an opponent controls with power 3 or less",
                      o["Elektra, Daughter of the Hand"]["oracle_text"])
        self.assertIn("Whenever you draw your second card each turn",
                      o["M.O.D.O.K., Evil Intellect"]["oracle_text"])
        self.assertIn("sacrifices a nontoken creature", o["M.O.D.O.K., Evil Intellect"]["oracle_text"])
        self.assertIn("When this creature dies, draw a card", o["Living Lies of Loki"]["oracle_text"])
        self.assertIn("Each creature you control that you've put one or more +1/+1 counters on this turn has hexproof",
                      o["Kid Loki"]["oracle_text"])

    def test_preservation_and_mana_oracle_interactions(self):
        o = self.oracle
        self.assertIn("Triggered abilities you control can't cause you to sacrifice or exile creature tokens",
                      o["The Master, Multiplied"]["oracle_text"])
        self.assertIn("{1}, {T}: End the turn", o["Sundial of the Infinite"]["oracle_text"])
        self.assertIn("If a triggered ability of another creature you control of the chosen type triggers",
                      o["Roaming Throne"]["oracle_text"])
        self.assertNotIn("This land enters tapped", o["City of Brass"]["oracle_text"])
        self.assertIn("This land enters tapped", o["Path of Ancestry"]["oracle_text"])
        self.assertIn("Add one mana of any color", o["City of Brass"]["oracle_text"])
        self.assertIn("When this creature dies, draw a card", o["Living Lies of Loki"]["oracle_text"])
        # A token entering tapped/attacking has not attacked, so the removed Kang
        # attack-trigger line must not be credited to a Loki token.
        self.assertIn("Whenever Kang Prime enters or attacks", o["Kang Prime"]["oracle_text"])
        self.assertIn("Whenever Kang attacks", o["Kang, Temporal Tyrant"]["oracle_text"])

    def test_owner_boundary_and_past_explicit_cuts(self):
        for card in ("Construct a Cosmic Cube", "The Masters of Evil", "Reliquary Tower",
                     "Kindred Dominance", "Raise the Palisade", "Endless Ranks of HYDRA",
                     "Puppet Master, String Puller", "Vulture, Scheming Scavenger",
                     "Thassa's Oracle", "Demonic Consultation",
                     "Dockside Extortionist", "Jeweled Lotus"):
            self.assertNotIn(card, self.candidate)
        self.assertTrue(REVIEW.exists())
        receipt = REVIEW.read_text(encoding="utf-8")
        self.assertIn("OWNER REVIEW ONLY", receipt)
        self.assertIn(CAND_SHA, receipt)
        self.assertIn("No owner approval or canonical lock", receipt)


if __name__ == "__main__":
    unittest.main()
