"""Source-bound finite checks for Azula ChatGPT M7 research options.

All options are RESEARCH_ONLY and explicitly NOT owner-approved or canonical.
No simulated multiplayer win rate, mana goldfish or full rules engine is claimed.
"""

import hashlib
import json
import math
import re
from pathlib import Path
import unittest
from test_m6_fire_lord_azula_m7_mechanics import run_cast


ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "data/grixis/m7/chatgpt_reviews"
BASELINE = ROOT / "data/grixis/m7/baseline_sources/Fire_Lord_Azula_approved_source_2026-10-14.txt"
ORACLE = ROOT / "data/grixis/m6/oracle_snapshots/Fire_Lord_Azula_M7_Scryfall_20261023.json"
BASELINE_SHA = "b6ef396641f2b5cfac0eb81fb494f21f3745e2a3fd47fa75d2eaadbdc34ddee5"
SELECTED = ROOT / "data/grixis/m7/candidate_lists/Fire_Lord_Azula_ChatGPT_M7_Rev2_Approval_Candidate_2026-10-24.txt"

OPTIONS = {
    "defense_five": {
        "path": "Fire_Lord_Azula_ChatGPT_Defense_Preserving_Five_Under_Review.txt",
        "sha256": "390d09cd01672fb30b4f6d758db9562c04b453d11bcf9d434808c61bde4b3f7c",
        "adds": {"Turnabout", "Sink into Stupor // Soporific Springs", "Unexpected Windfall", "Flashback", "Mistrise Village"},
        "cuts": {"Samut, Tyrant of Naktamun", "Exotic Orchard", "Vivi Ornitier", "Repeal", "Wooded Foothills"},
    },
    "haste_five": {
        "path": "Fire_Lord_Azula_ChatGPT_Haste_Five_Under_Review.txt",
        "sha256": "76f298c328d5ce76e43dba32c04d4f3dc4d8e57d2ff3827e681563da254d2ec3",
        "adds": {"Turnabout", "Sink into Stupor // Soporific Springs", "Samut, Hazoret's Champion", "Flashback", "Mistrise Village"},
        "cuts": {"Samut, Tyrant of Naktamun", "Exotic Orchard", "Vivi Ornitier", "Repeal", "Wooded Foothills"},
    },
    "keep_samut_four": {
        "path": "Fire_Lord_Azula_ChatGPT_Keep_Samut_Four_Under_Review.txt",
        "sha256": "2e3deb60bce700d5a59478c4ca65c8c84b18c37c576a54bc54a3a5af9d4a91bb",
        "adds": {"Sink into Stupor // Soporific Springs", "Samut, Hazoret's Champion", "Flashback", "Mistrise Village"},
        "cuts": {"Exotic Orchard", "Vivi Ornitier", "Repeal", "Wooded Foothills"},
    },
    "electro_five": {
        "path": "Fire_Lord_Azula_ChatGPT_Electro_Five_Under_Review.txt",
        "sha256": "77ac26a4f4ff70d0a7a666b07fa9fe051e52fe0547d8320d84490d088c0cc273",
        "adds": {"Turnabout", "Sink into Stupor // Soporific Springs", "Samut, Hazoret's Champion", "Flashback", "Electrodominance"},
        "cuts": {"Samut, Tyrant of Naktamun", "Exotic Orchard", "Vivi Ornitier", "Repeal", "Redirect Lightning"},
    },
    "electro_six": {
        "path": "Fire_Lord_Azula_ChatGPT_Electro_Six_Under_Review.txt",
        "sha256": "5c50bffd5335e03e9739d1b1d8f552bf23cce0eb050bccabf0b53196b21ea25b",
        "adds": {"Turnabout", "Sink into Stupor // Soporific Springs", "Samut, Hazoret's Champion", "Flashback", "Mistrise Village", "Electrodominance"},
        "cuts": {"Samut, Tyrant of Naktamun", "Exotic Orchard", "Vivi Ornitier", "Repeal", "Wooded Foothills", "Redirect Lightning"},
    },
}


def read_list(path: Path):
    content = path.read_bytes()
    rows = content.decode("utf-8").splitlines()
    assert all(re.fullmatch(r"1x .+", row) for row in rows)
    names = [row[3:].removesuffix(" [Commander]") for row in rows]
    return content, rows, names


def castable_with_pool(cost: str, pool):
    """Finite colored/generic payment check; not a substitute for all MTG rules."""
    symbols = re.findall(r"\{([^}]+)\}", cost)
    remaining = list(pool)
    generic = 0
    for symbol in symbols:
        if symbol.isdigit():
            generic += int(symbol)
        else:
            if symbol not in remaining:
                return False
            remaining.remove(symbol)
    return len(remaining) >= generic


def probability_at_least_one(population, hits, draws):
    return 1 - math.comb(population - hits, draws) / math.comb(population, draws)


class AzulaChatGPTResearchChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.oracle = {card["name"]: card for card in json.loads(ORACLE.read_text())["cards"]}
        baseline_raw, _, cls.baseline_names = read_list(BASELINE)
        assert hashlib.sha256(baseline_raw).hexdigest() == BASELINE_SHA

    def test_options_are_exactly_100_ubr_and_commander_legal(self):
        for label, option in OPTIONS.items():
            with self.subTest(option=label):
                content, rows, names = read_list(RESEARCH / option["path"])
                self.assertEqual(hashlib.sha256(content).hexdigest(), option["sha256"])
                self.assertEqual(len(rows), 100)
                self.assertEqual(len(set(names)), 100)
                self.assertEqual(rows[0], "1x Fire Lord Azula [Commander]")
                self.assertTrue(all(name in self.oracle for name in names))
                self.assertTrue(all(self.oracle[n]["commander_legality"] == "legal" for n in names))
                self.assertTrue(all(set(self.oracle[n]["color_identity"]) <= {"U", "B", "R"} for n in names))
                self.assertEqual(sum("Land" in self.oracle[n]["type_line"] for n in names), 26)
                self.assertEqual(sum(bool(self.oracle[n]["game_changer"]) for n in names), 20)

    def test_owner_review_candidate_is_exactly_sealed_electro_five(self):
        selected_raw, rows, names = read_list(SELECTED)
        source_raw, _, _ = read_list(RESEARCH / OPTIONS["electro_five"]["path"])
        self.assertEqual(selected_raw, source_raw)
        self.assertEqual(hashlib.sha256(selected_raw).hexdigest(), OPTIONS["electro_five"]["sha256"])
        self.assertEqual(len(rows), 100)
        self.assertEqual(rows[0], "1x Fire Lord Azula [Commander]")
        self.assertEqual(len(set(names)), 100)
        self.assertEqual(set(names) - set(self.baseline_names), OPTIONS["electro_five"]["adds"])
        self.assertEqual(set(self.baseline_names) - set(names), OPTIONS["electro_five"]["cuts"])
        self.assertIn("Wooded Foothills", names)
        self.assertNotIn("Mistrise Village", names)  # Tested sixth rejected on mana/tempo grounds.

    def test_exact_source_bound_swaps_and_protected_cedh_keeps(self):
        source = set(self.baseline_names)
        self.assertEqual(len(source), 100)
        for label, option in OPTIONS.items():
            with self.subTest(option=label):
                _, _, names = read_list(RESEARCH / option["path"])
                candidate = set(names)
                self.assertEqual(candidate - source, option["adds"])
                self.assertEqual(source - candidate, option["cuts"])
                self.assertEqual(len(option["adds"]), len(option["cuts"]))
                self.assertIn("Swan Song", candidate)
                self.assertIn("Gemstone Caverns", candidate)
                self.assertIn("Hexing Squelcher", candidate)

    def test_firebending_big_score_and_windfall_same_mana_in_combat(self):
        big = self.oracle["Big Score"]["mana_cost"]
        wind = self.oracle["Unexpected Windfall"]["mana_cost"]
        self.assertEqual(big, "{3}{R}")
        self.assertEqual(wind, "{2}{R}{R}")
        # Firebending contributes two R; U and B are the other two mana.
        for cost in (big, wind):
            self.assertTrue(castable_with_pool(cost, ["R", "R", "U", "B"]))
            self.assertFalse(castable_with_pool(cost, ["R", "R", "U"]))
        # Outside combat, Big Score has a strictly less demanding red requirement.
        self.assertTrue(castable_with_pool(big, ["R", "U", "U", "B"]))
        self.assertFalse(castable_with_pool(wind, ["R", "U", "U", "B"]))
        self.assertEqual(
            self.oracle["Big Score"]["oracle_text"].split("\nDraw two cards")[1],
            self.oracle["Unexpected Windfall"]["oracle_text"].split("\nDraw two cards")[1],
        )

    def test_mdfc_life_and_ad_nauseam_cost_are_explicit(self):
        split = self.oracle["Sink into Stupor // Soporific Springs"]
        orchard = self.oracle["Exotic Orchard"]
        self.assertEqual(split["cmc"], 3)
        self.assertEqual(orchard["cmc"], 0)
        self.assertIn("pay 3 life", split["oracle_text"])
        self.assertIn("lose life equal to its mana value", self.oracle["Ad Nauseam"]["oracle_text"])

    def test_mistrise_and_samut_tradeoffs_are_visible(self):
        village = self.oracle["Mistrise Village"]["oracle_text"]
        self.assertIn("enters tapped unless you control a Mountain or a Forest", village)
        self.assertIn("The next spell you cast this turn can't be countered", village)
        self.assertIn("split second", self.oracle["Samut, Tyrant of Naktamun"]["oracle_text"])
        self.assertIn("copy target instant or sorcery spell", self.oracle["Narset's Reversal"]["oracle_text"].lower())

    def test_electrodominance_copied_free_casts_require_real_conditions(self):
        electro = self.oracle["Electrodominance"]
        self.assertEqual(electro["mana_cost"], "{X}{R}{R}")
        self.assertEqual(electro["commander_legality"], "legal")
        self.assertIn("deals X damage to any target", electro["oracle_text"])
        self.assertIn("cast a spell with mana value X or less from your hand without paying its mana cost", electro["oracle_text"])
        self.assertIn("Whenever you cast a spell while Fire Lord Azula is attacking, copy that spell",
                      self.oracle["Fire Lord Azula"]["oracle_text"])
        # At X=1 or 2, two red firebending mana cover RR; one or two other mana pay X.
        self.assertTrue(castable_with_pool("{1}{R}{R}", ["R", "R", "U"]))
        self.assertTrue(castable_with_pool("{2}{R}{R}", ["R", "R", "U", "B"]))
        self.assertFalse(castable_with_pool("{2}{R}{R}", ["R", "R", "U"]))
        for label in ("electro_five", "electro_six"):
            _, _, names = read_list(RESEARCH / OPTIONS[label]["path"])
            self.assertIn("Electrodominance", names)
            self.assertNotIn("Samut, Tyrant of Naktamun", names)
            self.assertNotIn("Redirect Lightning", names)  # Explicit protection opportunity cost.

    def test_haste_access_raw_draw_proxy_not_game_model(self):
        source = set(self.baseline_names)
        base_haste = {"Arena of Glory", "Crimson Wisps", "Expedite"}
        self.assertTrue(base_haste <= source)
        haste_option = OPTIONS["haste_five"]
        _, _, names = read_list(RESEARCH / haste_option["path"])
        self.assertIn("Samut, Hazoret's Champion", names)
        self.assertIn("Creatures you control have haste", self.oracle["Samut, Hazoret's Champion"]["oracle_text"])
        self.assertAlmostEqual(probability_at_least_one(99, 3, 10), 0.27596605652570305)
        self.assertAlmostEqual(probability_at_least_one(99, 4, 10), 0.3513862589709422)

    def test_bounded_azula_castability_proxy_discloses_mana_cost(self):
        # Reuse Grok's finite test helper, with all its disclosed blind spots:
        # no moxen, rituals, haste, tapped-land timing or real multiplayer play.
        self.assertEqual(run_cast(BASELINE, mdfc_land=True)["play"]["4"], 0.492)
        expected = {
            "defense_five": (0.4874, 0.4604),
            "haste_five": (0.4874, 0.4604),
            "keep_samut_four": (0.4874, 0.4604),
            "electro_five": (0.49, 0.4626),
            "electro_six": (0.4874, 0.4604),
        }
        for label, option in OPTIONS.items():
            with self.subTest(option=label):
                path = RESEARCH / option["path"]
                self.assertEqual(run_cast(path, mdfc_land=True)["play"]["4"], expected[label][0])
                self.assertEqual(run_cast(path, mdfc_land=False)["play"]["4"], expected[label][1])


if __name__ == "__main__":
    unittest.main()
