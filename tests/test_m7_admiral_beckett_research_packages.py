"""Finite structural and source-Oracle gates for Admiral M7 RESEARCH_ONLY packages.

These checks do not grant strategic approval, M6 certification, or a win-rate claim.
"""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data/grixis/m6/authority_snapshots/Admiral_Beckett_Brass_Canonical_Approved_20261022.txt"
DIR = ROOT / "data/grixis/m7/research_challengers"
ORACLE = DIR / "Admiral_Beckett_Brass_M7_Oracle_Candidates_20261022.json"
PACKAGES = {
    "A": DIR / "Admiral_Beckett_Brass_fast_connection_package.txt",
    "B": DIR / "Admiral_Beckett_Brass_grind_evasion_package.txt",
}
SOURCE_SHA256 = "4ba5c483eb67b5f2647d375450adf9c2b7e79a036d0ba1866e58de8441bf3414"
COMMON_CUTS = {
    "Crumbling Necropolis",
    "Daring Saboteur",
    "Dire Fleet Captain",
    "Merchant Raiders",
    "The Indomitable",
}
PACKAGE_ADDS = {
    "A": {"City of Brass", "Departed Deckhand", "Skyship Plunderer", "Broadside Bombardiers", "Blustersquall"},
    "B": {"City of Brass", "Slippery Scoundrel", "Dire Fleet Neckbreaker", "Herald's Horn", "Blustersquall"},
}


def load_cards(path: Path) -> Counter[str]:
    cards: Counter[str] = Counter()
    for row_number, row in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        assert row.startswith("1x ") or row.startswith("2x ") or row.startswith("3x "), (path, row_number)
        amount_text, name = row.split("x ", 1)
        amount = int(amount_text)
        if row_number == 1:
            assert name == "Admiral Beckett Brass [Commander]", (path, name)
            name = name.removesuffix(" [Commander]")
        else:
            assert "[Commander]" not in name
        assert name not in cards, (path, name)
        assert amount == 1 or name in {"Island", "Mountain"}, (path, name)
        cards[name] += amount
    assert sum(cards.values()) == 100, path
    assert cards["Admiral Beckett Brass"] == 1, path
    return cards


class AdmiralM7ResearchPackagesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = load_cards(SOURCE)
        cls.packages = {k: load_cards(path) for k, path in PACKAGES.items()}
        cls.oracle_payload = json.loads(ORACLE.read_text(encoding="utf-8"))
        cls.oracle = {row["name"]: row for row in cls.oracle_payload["cards"]}

    def test_canonical_approved_bytes_are_unchanged(self):
        self.assertEqual(hashlib.sha256(SOURCE.read_bytes()).hexdigest(), SOURCE_SHA256)
        self.assertEqual(len(self.source), 97)
        self.assertEqual(self.source["Island"], 3)
        self.assertEqual(self.source["Mountain"], 2)

    def test_two_independent_five_replacement_100_card_fixtures(self):
        self.assertNotEqual(PACKAGES["A"].read_bytes(), PACKAGES["B"].read_bytes())
        for key, fixture in self.packages.items():
            adds = set(fixture) - set(self.source)
            cuts = set(self.source) - set(fixture)
            self.assertEqual(adds, PACKAGE_ADDS[key], key)
            self.assertEqual(cuts, COMMON_CUTS, key)
            self.assertEqual(len(adds), 5)
            self.assertEqual(len(cuts), 5)
            self.assertEqual(len(fixture), 97)
            self.assertEqual(sum(fixture.values()), 100)
            self.assertEqual(fixture["Admiral Beckett Brass"], 1)

    def test_source_bound_challenger_oracle_and_color_identity(self):
        self.assertEqual(self.oracle_payload["canonical_baseline_raw_sha256"], SOURCE_SHA256)
        self.assertEqual(self.oracle_payload["retrieved_date"], "2026-10-22")
        self.assertEqual(len(self.oracle), 24)
        self.assertEqual(len(self.oracle_payload["cards"]), 24)
        for name in set().union(*PACKAGE_ADDS.values()):
            with self.subTest(challenger=name):
                card = self.oracle[name]
                self.assertEqual(card["commander"], "legal")
                self.assertTrue(set(card["color_identity"]) <= {"U", "B", "R"})
                self.assertTrue(card["oracle_id"])
                self.assertTrue(card["oracle_text"])

    def test_connection_package_retains_pirate_source_slots(self):
        removed = {"Daring Saboteur", "Dire Fleet Captain", "Merchant Raiders"}
        added = {"Departed Deckhand", "Skyship Plunderer", "Broadside Bombardiers"}
        self.assertEqual(len(removed), len(added))
        for name in added:
            self.assertIn("Pirate", self.oracle[name]["type_line"])
        self.assertIn("Flying", self.oracle["Skyship Plunderer"]["oracle_text"])
        self.assertIn("Spirit Pirate", self.oracle["Departed Deckhand"]["type_line"])

    def test_one_shot_blocker_tap_is_not_a_repeatable_draw_effect(self):
        blustersquall = self.oracle["Blustersquall"]
        self.assertEqual(blustersquall["mana_cost"], "{U}")
        self.assertIn("Overload {3}{U}", blustersquall["oracle_text"])
        self.assertIn("Tap target creature you don't control", blustersquall["oracle_text"])
        self.assertNotIn("draw", blustersquall["oracle_text"].lower())
        # Replacing The Indomitable necessarily sacrifices a recurring draw engine.
        self.assertEqual(self.source["The Indomitable"], 1)
        self.assertEqual(self.packages["A"]["The Indomitable"], 0)

    def test_bombardiers_boast_is_paid_not_free_treasure_damage(self):
        oracle = self.oracle["Broadside Bombardiers"]["oracle_text"]
        self.assertIn("Menace, haste", oracle)
        self.assertIn("Sacrifice another creature or artifact", oracle)
        self.assertIn("2 plus the sacrificed permanent's mana value", oracle)
        self.assertIn("Activate only if this creature attacked this turn and only once each turn", oracle)
        self.assertEqual(2 + 0, 2, "A sacrificed Treasure has mana value 0")

    def test_grind_package_tempo_caveats_are_real(self):
        scoundrel = self.oracle["Slippery Scoundrel"]["oracle_text"]
        self.assertIn("ten or more permanents", scoundrel)
        self.assertIn("As long as you have the city's blessing", scoundrel)
        self.assertIn("{1} less to cast", self.oracle["Herald's Horn"]["oracle_text"])
        self.assertIn("Attacking Pirates", self.oracle["Dire Fleet Neckbreaker"]["oracle_text"])
        self.assertNotIn("Pirate", self.oracle["Herald's Horn"]["type_line"])

    def test_research_is_not_an_approval_or_certificate(self):
        audit = (DIR / "Admiral_Beckett_Brass_decisive_opportunity_audit_20261022.md").read_text(encoding="utf-8")
        self.assertIn("RESEARCH_ONLY", audit)
        self.assertIn("UNVERIFIED", audit)
        self.assertIn("owner-approved Admiral M7 replacement", audit)
        self.assertNotIn("stage: OWNER_READY", audit)


if __name__ == "__main__":
    unittest.main()
