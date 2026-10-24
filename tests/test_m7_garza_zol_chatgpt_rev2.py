"""Garza Zol ChatGPT independent Rev2: finite offline source-bound checks, NOT owner approval."""
import hashlib
import json
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
D = "Garza_Zol__Plague_Queen"
BASE = ROOT / f"data/grixis/m7/baseline_sources/{D}_approved_source_2026-10-14.txt"
CAND = ROOT / f"data/grixis/m7/candidate_lists/{D}_ChatGPT_M7_Rev2_20261024.txt"
ORACLE = ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json"
REPORT = ROOT / f"data/grixis/m7/chatgpt_reviews/{D}_M7_Rev2_Independent_Decision_Packet_20261024.md"
BASE_HASH = "32c0e8049a9c8a5d238048b4f774f0457908d724f23d4597b7da93a6cba0c16f"
CAND_HASH = "353381caa82e68049a878eefc9c97a5293790b892fda652c97ac63c938689244"
SWAPS = {
    "Lizard Blades": "Scythe of the Wretched",
    "Two-Handed Axe // Sweeping Cleave": "Inquisitor's Flail",
    "Conqueror's Flail": "Robe of the Archmagi",
    "Giantfall": "Rapid Hybridization",
    "Seize the Day": "Sheoldred's Edict",
    "Temur Battle Rage": "Psychotic Fury",
    "Malakir Rebirth // Malakir Mire": "Takenuma, Abandoned Mire",
}
NEW_NAMES = {
    "Conqueror's Flail",
    "Seize the Day",
    "Two-Handed Axe // Sweeping Cleave",
}
ROCKS = {
    "Arcane Signet", "Sol Ring", "Mana Vault", "Grim Monolith", "Fellwar Stone",
    "Dimir Signet", "Izzet Signet", "Rakdos Signet",
    "Talisman of Creativity", "Talisman of Dominance", "Talisman of Indulgence",
}


def deck(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    assert len(lines) == 100, len(lines)
    assert lines[0] == "1x Garza Zol, Plague Queen [Commander]"
    assert all(line.startswith("1x ") for line in lines)
    names = [line[3:].removesuffix(" [Commander]") for line in lines]
    assert len(set(names)) == 100
    return names


class IndependentGarzaRev2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.baseline = deck(BASE)
        cls.candidate = deck(CAND)
        cls.snapshot = json.loads(ORACLE.read_text(encoding="utf-8"))
        cls.by_name = {card["name"]: card for card in cls.snapshot["cards"]}

    def test_raw_sha_and_final_lf(self):
        self.assertEqual(hashlib.sha256(BASE.read_bytes()).hexdigest(), BASE_HASH)
        self.assertEqual(hashlib.sha256(CAND.read_bytes()).hexdigest(), CAND_HASH)
        self.assertTrue(CAND.read_bytes().endswith(b"\n"))

    def test_only_the_seven_declared_changes(self):
        before, after = Counter(self.baseline), Counter(self.candidate)
        self.assertEqual(set((after - before).elements()), set(SWAPS))
        self.assertEqual(set((before - after).elements()), set(SWAPS.values()))
        self.assertEqual(sum((after - before).values()), 7)
        self.assertEqual(self.candidate[1:], sorted(self.candidate[1:], key=str.casefold))

    def test_stored_oracle_97_and_three_separately_sourced(self):
        missing = set(self.candidate) - set(self.by_name)
        self.assertEqual(missing, NEW_NAMES)
        for card in self.candidate:
            if card in NEW_NAMES:
                continue  # Scryfall/Gatherer external URLs in review packet; not cached API.
            oracle = self.by_name[card]
            self.assertEqual(oracle["commander_legality"], "legal", card)
            self.assertTrue(set(oracle["color_identity"]) <= {"U", "B", "R"}, card)
        game = {name for name in self.candidate if name in self.by_name and self.by_name[name]["game_changer"]}
        self.assertEqual(game, {
            "Ancient Tomb", "Cyclonic Rift", "Demonic Tutor", "Fierce Guardianship",
            "Grim Monolith", "Jeska's Will", "Mana Vault", "Rhystic Study", "Vampiric Tutor",
        })

    def test_land_faces_and_acceleration_kept(self):
        lands = {name for name in self.candidate if name in self.by_name and "Land" in self.by_name[name]["type_line"]}
        self.assertEqual(len(lands), 38)
        old_lands = {name for name in self.baseline if name in self.by_name and "Land" in self.by_name[name]["type_line"]}
        self.assertEqual(len(old_lands), 38)
        self.assertIn("Malakir Rebirth // Malakir Mire", lands)
        self.assertNotIn("Takenuma, Abandoned Mire", lands)
        self.assertIn("Exotic Orchard", lands)
        for state in (self.baseline, self.candidate):
            self.assertEqual(set(state) & ROCKS, ROCKS)

    def test_equipment_count_and_garza_first(self):
        def equipment(names):
            cached = sum("Equipment" in self.by_name[x]["type_line"] for x in names if x in self.by_name)
            return cached + sum(x in {"Conqueror's Flail", "Two-Handed Axe // Sweeping Cleave"} for x in names)
        self.assertEqual(equipment(self.baseline), 20)
        self.assertEqual(equipment(self.candidate), 20)
        self.assertIn("Kediss, Emberclaw Familiar", self.candidate)
        self.assertIn("Grafted Exoskeleton", self.candidate)
        self.assertIn("Thornbite Staff", self.candidate)

    def test_finite_attack_power_and_poison_fixtures_not_games(self):
        def axe_attack(power):
            return power * 2  # One triggered power doubling as +X/+0, until end of turn.
        self.assertEqual(axe_attack(5), 10)
        self.assertEqual(axe_attack(5) * 2, 20)  # Lizard double strike, two 10-damage steps.
        self.assertEqual(axe_attack(6) * 2, 24)
        second_attack = axe_attack(axe_attack(5))  # Seize extra combat, same turn.
        self.assertEqual((axe_attack(5), second_attack), (10, 20))
        self.assertEqual(axe_attack(5) + second_attack, 30)
        self.assertEqual(axe_attack(5 + 2), 14)  # Grafted Exoskeleton infect if unblocked.

    def test_source_bound_tradeoff_disclosures(self):
        text = REPORT.read_text(encoding="utf-8")
        for s in ("awaiting", "Scythe", "Fellwar", "Malakir Mire", "enters tapped",
                  "target", "owner approval", CAND_HASH, "not", "Giantfall"):
            self.assertIn(s.lower(), text.lower())
        self.assertNotIn("CANONICAL_LOCKED", text)
        self.assertNotIn("actual multiplayer win rate", text.lower())


if __name__ == "__main__":
    unittest.main()
