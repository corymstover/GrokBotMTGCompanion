"""Admiral open-ended stage-1 FULL 100-card six/seven-swap physical comparisons.

These are RESEARCH ONLY; passing does not certify current Oracle, changed M6 I/J,
comparative power, owner approval, or a new canonical deck.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path
import unittest

from scripts.grixis_m7_decision_gate import parse_list

ROOT = Path(__file__).resolve().parents[1]
BASELINE = ROOT / "data/grixis/m6/authority_snapshots/Admiral_Beckett_Brass_Canonical_Approved_20261022.txt"
D = ROOT / "data/grixis/m7/candidate_lists/Admiral_Beckett_Brass.txt"
REVIEW = ROOT / "data/grixis/m7/decision_reviews/Admiral_Beckett_Brass.json"
RESEARCH = ROOT / "data/grixis/m7/research_challengers"
BASE_SHA = "4ba5c483eb67b5f2647d375450adf9c2b7e79a036d0ba1866e58de8441bf3414"
D_SHA = "201a1d5fc90e30d6aff9a565603fcf8caef69604dad2c07b4951be2b41cc92ee"
FIVE = {
    "City of Brass": "Crumbling Necropolis",
    "Departed Deckhand": "Daring Saboteur",
    "Cloud Pirates": "Dire Fleet Captain",
    "Skyship Plunderer": "Dire Fleet Poisoner",
    "Broadside Bombardiers": "Forerunner of the Coalition",
}
SIX_STORM = {
    "Captain Storm, Cosmium Raider": "March of the Drowned",
}
SIX_SHIZO = {
    "Shizo, Death's Storehouse": "Path of Ancestry",
}
OPTIONS = {
    "Admiral_Beckett_Brass_six_Captain_Storm_20261022.txt": SIX_STORM,
    "Admiral_Beckett_Brass_six_Shizo_20261022.txt": SIX_SHIZO,
    "Admiral_Beckett_Brass_seven_Storm_Shizo_20261022.txt": SIX_STORM | SIX_SHIZO,
}


class AdmiralUnboundedStageOne(unittest.TestCase):
    def test_preserve_historical_canonical_and_withdrawn_five_swap_source(self):
        self.assertEqual(hashlib.sha256(BASELINE.read_bytes()).hexdigest(), BASE_SHA)
        self.assertEqual(hashlib.sha256(D.read_bytes()).hexdigest(), D_SHA)
        original, bc, cp = parse_list(BASELINE)
        old_d, dc, dp = parse_list(D)
        self.assertEqual(len(original), len(old_d))
        self.assertEqual(len(original), 100)
        self.assertEqual(bc, dc)
        self.assertEqual(bc, ["Admiral Beckett Brass"])
        self.assertEqual(cp, dp)
        self.assertEqual(cp, [])
        review = json.loads(REVIEW.read_text(encoding="utf-8"))
        self.assertEqual(review["readiness"], "RESEARCH_ONLY_WITHDRAWN_NOT_OWNER_PRESENTABLE")
        self.assertFalse(review["owner_authority"]["exact_candidate_owner_approved"])
        self.assertEqual(review["final_candidate"]["sha256"], D_SHA)
        self.assertEqual(Counter((Counter(old_d)-Counter(original)).elements()),
                         Counter(FIVE.keys()))
        self.assertEqual(Counter((Counter(original)-Counter(old_d)).elements()),
                         Counter(FIVE.values()))

    def test_six_and_seven_are_real_source_matched_commander_first_research(self):
        baseline, commander, companion = parse_list(BASELINE)
        prior, _, _ = parse_list(D)
        for name, extensions in OPTIONS.items():
            with self.subTest(name=name):
                path = RESEARCH / name
                self.assertTrue(path.is_file())
                cards, cmd, comp = parse_list(path)
                self.assertEqual(len(cards), 100)
                self.assertEqual(cmd, commander)
                self.assertEqual(comp, companion)
                self.assertEqual(len(path.read_text(encoding="utf-8").strip().splitlines()), 97)
                expected = FIVE | extensions
                adds = Counter((Counter(cards) - Counter(baseline)).elements())
                cuts = Counter((Counter(baseline) - Counter(cards)).elements())
                self.assertEqual(adds, Counter(expected.keys()))
                self.assertEqual(cuts, Counter(expected.values()))
                self.assertEqual(sum(adds.values()), 5 + len(extensions))
                self.assertEqual(sum(cuts.values()), sum(adds.values()))
                changed = Counter((Counter(cards) - Counter(prior)).elements())
                self.assertEqual(changed, Counter(extensions.keys()))
                print("RESEARCH_ONLY", name, "physical", len(cards),
                      "swaps", sum(adds.values()), "raw_sha256",
                      hashlib.sha256(path.read_bytes()).hexdigest())

    def test_owner_floor_never_promotes_research_packages(self):
        text = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("FIVE IS A FLOOR, NEVER A TARGET OR STOPPING RULE", text)
        standard = (ROOT / "grixis/Commander-First Decisive Optimization and Test Economy Standard.md").read_text(encoding="utf-8")
        self.assertIn("unbounded optimization", standard)
        audit = (RESEARCH / "Admiral_Beckett_Brass_open_ended_stage1_20261022.md").read_text(encoding="utf-8")
        self.assertIn("OWNER APPROVAL WITHHELD", audit)
        self.assertIn("not an M7 final recommendation", audit)


if __name__ == "__main__":
    unittest.main()
