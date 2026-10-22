"""Admiral M7 evasion-horizon physical-source fixtures: RESEARCH_ONLY.

Tests exact canonical vs withdrawn D vs four expanded 100-card hypotheses.
The test never confers Oracle clearance, M6 I/J certification or owner approval.
"""
from collections import Counter
import hashlib
from pathlib import Path
import unittest

from scripts.grixis_m7_decision_gate import parse_list

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "data/grixis/m6/authority_snapshots/Admiral_Beckett_Brass_Canonical_Approved_20261022.txt"
D = ROOT / "data/grixis/m7/candidate_lists/Admiral_Beckett_Brass.txt"
DIR = ROOT / "data/grixis/m7/research_challengers"
BASE_HASH = "4ba5c483eb67b5f2647d375450adf9c2b7e79a036d0ba1866e58de8441bf3414"
D_HASH = "201a1d5fc90e30d6aff9a565603fcf8caef69604dad2c07b4951be2b41cc92ee"
HISTORIC = {
    "City of Brass": "Crumbling Necropolis",
    "Departed Deckhand": "Daring Saboteur",
    "Cloud Pirates": "Dire Fleet Captain",
    "Skyship Plunderer": "Dire Fleet Poisoner",
    "Broadside Bombardiers": "Forerunner of the Coalition",
}
REVISIONS = {
    "Admiral_Beckett_Brass_six_Glaring_Spotlight_20261022.txt": {"Glaring Spotlight": "Bident of Thassa"},
    "Admiral_Beckett_Brass_six_Brotherhood_Regalia_20261022.txt": {"Brotherhood Regalia": "Bident of Thassa"},
    "Admiral_Beckett_Brass_six_Cosmotronic_Wave_20261022.txt": {"Cosmotronic Wave": "Fiery Cannonade"},
    "Admiral_Beckett_Brass_seven_Regalia_Wave_20261022.txt": {
        "Brotherhood Regalia": "Bident of Thassa",
        "Cosmotronic Wave": "Fiery Cannonade",
    },
}


class AdmiralEvasionHorizon(unittest.TestCase):
    def test_preserve_canon_and_withdrawn_five(self):
        self.assertEqual(hashlib.sha256(BASE.read_bytes()).hexdigest(), BASE_HASH)
        self.assertEqual(hashlib.sha256(D.read_bytes()).hexdigest(), D_HASH)

    def test_full_card_source_counts_and_exact_package_deltas(self):
        canon, cmd, comp = parse_list(BASE)
        d, dcmd, dcomp = parse_list(D)
        self.assertEqual(len(canon), 100)
        self.assertEqual(len(d), 100)
        self.assertEqual(cmd, ["Admiral Beckett Brass"])
        self.assertEqual(comp, [])
        self.assertEqual((cmd, comp), (dcmd, dcomp))
        for filename, more in REVISIONS.items():
            with self.subTest(filename=filename):
                path = DIR / filename
                physical, command, companion = parse_list(path)
                self.assertEqual(len(physical), 100)
                self.assertEqual((command, companion), (cmd, comp))
                self.assertEqual(len(path.read_text(encoding="utf-8").strip().splitlines()), 97)
                expected = HISTORIC | more
                self.assertEqual(Counter((Counter(physical) - Counter(canon)).elements()), Counter(expected.keys()))
                self.assertEqual(Counter((Counter(canon) - Counter(physical)).elements()), Counter(expected.values()))
                self.assertEqual(Counter((Counter(physical) - Counter(d)).elements()), Counter(more.keys()))
                self.assertEqual(Counter((Counter(d) - Counter(physical)).elements()), Counter(more.values()))
                print("RESEARCH_ONLY", filename, "physical=100", "swaps=", len(expected),
                      "sha256=", hashlib.sha256(path.read_bytes()).hexdigest())

    def test_owner_approval_withheld_and_unbounded_horizon(self):
        horizon = (DIR / "Admiral_Beckett_Brass_evasion_horizon_stage2_20261022.md").read_text()
        self.assertIn("OWNER APPROVAL WITHHELD", horizon)
        self.assertIn("not a search budget", horizon)
        self.assertIn("UNVERIFIED / RESEARCH_ONLY", horizon)
        self.assertIn("three different Pirates", horizon)


if __name__ == "__main__":
    unittest.main()
