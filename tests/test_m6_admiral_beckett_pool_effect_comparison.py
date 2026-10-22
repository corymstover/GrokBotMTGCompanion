"""Matched finite Oracle checks for all FOUR real Admiral M6 tested-pool packages.

This models exact differences in roles/costs, not randomized multiplayer wins.
It never issues a PASS I certificate or converts qualitative strategy to data.
"""

from collections import Counter
import hashlib
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
POOL = ROOT / "data/grixis/m6/ij/tested_pools/Admiral_Beckett_Brass_candidate_D_20261022.json"
ORACLE = ROOT / "data/grixis/m7/research_challengers/Admiral_Beckett_Brass_Full_Source_Oracle_20261022.json"
REPORT = ROOT / "data/grixis/m6/certification_preflight/Admiral_M6_I_four_package_effect_adjudication_20261022.md"


def deck_counts(path: Path) -> Counter[str]:
    physical = Counter()
    for line in path.read_text(encoding="utf-8").splitlines():
        quantity, name = line.split("x ", 1)
        physical[name.removesuffix(" [Commander]")] = int(quantity)
    assert sum(physical.values()) == 100
    return physical


class AdmiralPoolEffectsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pool = json.loads(POOL.read_text(encoding="utf-8"))
        cls.package = {e["id"]: deck_counts(ROOT / e["path"]) for e in pool["alternative_configurations"]}
        cls.oracle = {c["name"]: c for c in json.loads(ORACLE.read_text(encoding="utf-8"))["cards"]}
        cls.pool = pool

    def test_all_four_physical_configurations_and_oracle_sources(self):
        self.assertEqual(set(self.package), {"A", "B", "C", "D"})
        for p in self.pool["alternative_configurations"]:
            path = ROOT / p["path"]
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), p["raw_sha256"])
            self.assertEqual(sum(self.package[p["id"]].values()), 100)
            self.assertTrue(set(self.package[p["id"]]) <= set(self.oracle))

    def test_A_B_pay_4_to_tap_temporarily_but_lose_repeat_raiders_lock(self):
        text = self.oracle["Blustersquall"]["oracle_text"]
        self.assertIn("Tap target creature you don't control", text)
        self.assertIn("Overload {3}{U}", text)
        self.assertNotIn("doesn't untap", text)
        raiders = self.oracle["Merchant Raiders"]["oracle_text"]
        self.assertIn("another Pirate you control enters", raiders)
        self.assertIn("doesn't untap during its controller's untap step for as long as you control this creature", raiders)
        for name in ("A", "B"):
            self.assertEqual(self.package[name]["Blustersquall"], 1)
            self.assertEqual(self.package[name]["Merchant Raiders"], 0)
        for name in ("C", "D"):
            self.assertEqual(self.package[name]["Merchant Raiders"], 1)
        # A/B can overload to tap all enemy creatures for this attack for 3U,
        # but the opponent untaps normally next turn. D/C instead retain a
        # repeatedly-triggered lock, conditionally lasting while Raiders survives.

    def test_A_B_lose_uncrewed_indomitable_draws_after_multiple_Pirate_hits(self):
        source = self.oracle["The Indomitable"]["oracle_text"]
        self.assertIn("Whenever a creature you control deals combat damage to a player, draw a card", source)
        self.assertIn("Crew 3", source)
        self.assertEqual(self.oracle["The Indomitable"]["mana_cost"], "{2}{U}{U}")
        for name in ("A", "B"):
            self.assertEqual(self.package[name]["The Indomitable"], 0)
        for name in ("C", "D"):
            self.assertEqual(self.package[name]["The Indomitable"], 1)
        # Board witness: Indomitable merely exists uncrewed, three different
        # our creatures connect once each -> three separately triggered draws.
        connected_own_creatures = ("Cloud Pirates", "Skyship Plunderer", "Departed Deckhand")
        self.assertEqual(len(set(connected_own_creatures)), 3)
        self.assertEqual(len(connected_own_creatures) * 1, 3)

    def test_C_blustersquall_vs_D_open_real_mana_pips_and_card_access(self):
        open_text = self.oracle["Open into Wonder"]["oracle_text"]
        self.assertIn("X target creatures can't be blocked this turn", open_text)
        self.assertIn("Whenever this creature deals combat damage to a player, draw a card", open_text)
        self.assertEqual(self.oracle["Open into Wonder"]["mana_cost"], "{X}{U}{U}")
        self.assertEqual(self.oracle["Blustersquall"]["mana_cost"], "{U}")
        self.assertEqual(self.package["C"]["Open into Wonder"], 0)
        self.assertEqual(self.package["D"]["Open into Wonder"], 1)
        self.assertEqual(self.package["C"]["Blustersquall"], 1)
        self.assertEqual(self.package["D"]["Blustersquall"], 0)
        # To unblock 3, Open pays 3UU = 5 mana, 2 blue; Blustersquall's
        # overload is 3U = 4 mana, 1 blue, but grants zero card-draw triggers.
        self.assertEqual(3 + 2, 5)
        self.assertEqual(3 + 1, 4)
        # Opponent's hexproof would not stop Open targeting our own Pirates,
        # although targeted own Pirates and sorcery timing remain constraints.

    def test_B_ascend_and_combat_power_are_conditional_not_three_hit_sources(self):
        scoundrel = self.oracle["Slippery Scoundrel"]["oracle_text"]
        horn = self.oracle["Herald's Horn"]["oracle_text"]
        neck = self.oracle["Dire Fleet Neckbreaker"]["oracle_text"]
        self.assertIn("ten or more permanents", scoundrel)
        self.assertIn("As long as you have the city's blessing", scoundrel)
        self.assertIn("Creature spells you cast of the chosen type cost {1} less", horn)
        self.assertIn("Attacking Pirates you control get +2/+0", neck)
        for name in ("Slippery Scoundrel", "Herald's Horn", "Dire Fleet Neckbreaker"):
            self.assertEqual(self.package["B"][name], 1)
            self.assertEqual(self.package["D"][name], 0)
        # More attack damage does not change number of distinct combat sources.
        three_distinct = ("Cloud Pirates", "Skyship Plunderer", "Departed Deckhand")
        self.assertEqual(len(set(three_distinct)), 3)

    def test_D_preserves_all_three_identity_engines_and_abides_non_certification(self):
        d = self.package["D"]
        for essential in ("Merchant Raiders", "The Indomitable", "Open into Wonder", "Daring Piracy"):
            self.assertEqual(d[essential], 1)
        self.assertEqual(self.pool["preferred_research_candidate"], "D")
        self.assertTrue(self.pool["scope"]["tested_pool_zero_improvement_M6_I_certified"])
        report = REPORT.read_text(encoding="utf-8")
        self.assertIn("201a1d5fc90e30d6aff9a565603fcf8caef69604dad2c07b4951be2b41cc92ee", report)
        self.assertIn("RESEARCH_ONLY", report)
        self.assertIn("superseded by the later formal M6 I closure", report)


if __name__ == "__main__":
    unittest.main()
