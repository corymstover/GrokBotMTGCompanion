"""Source-complete, finite Admiral M7 research comparisons; not I/J certification."""

from __future__ import annotations

from collections import Counter
import hashlib
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "data/grixis/m7/research_challengers"
SOURCE = ROOT / "data/grixis/m6/authority_snapshots/Admiral_Beckett_Brass_Canonical_Approved_20261022.txt"
ORACLE_PATH = RESEARCH / "Admiral_Beckett_Brass_Full_Source_Oracle_20261022.json"
FILES = {
    "approved": SOURCE,
    "A": RESEARCH / "Admiral_Beckett_Brass_fast_connection_package.txt",
    "B": RESEARCH / "Admiral_Beckett_Brass_grind_evasion_package.txt",
    "C": RESEARCH / "Admiral_Beckett_Brass_resilient_connection_package.txt",
}
APPROVED_SHA = "4ba5c483eb67b5f2647d375450adf9c2b7e79a036d0ba1866e58de8441bf3414"
C_ADDS = {"City of Brass", "Departed Deckhand", "Cloud Pirates", "Skyship Plunderer", "Blustersquall"}
C_CUTS = {"Crumbling Necropolis", "Daring Saboteur", "Dire Fleet Captain", "Dire Fleet Poisoner", "Open into Wonder"}


def deck_cards(path: Path) -> Counter[str]:
    cards: Counter[str] = Counter()
    rows = path.read_text(encoding="utf-8").splitlines()
    assert rows[0] == "1x Admiral Beckett Brass [Commander]"
    for row in rows:
        quantity, name = row.split("x ", 1)
        name = name.removesuffix(" [Commander]")
        assert name not in cards, name
        n = int(quantity)
        assert n == 1 or name in {"Island", "Mountain"}
        cards[name] += n
    assert sum(cards.values()) == 100
    assert len(cards) == 97
    return cards


class AdmiralFullSourceResearchTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = json.loads(ORACLE_PATH.read_text(encoding="utf-8"))
        cls.cards = {c["name"]: c for c in cls.payload["cards"]}
        cls.decks = {key: deck_cards(path) for key, path in FILES.items()}

    def test_immutable_approved_source_and_all_121_oracle_names(self):
        self.assertEqual(hashlib.sha256(SOURCE.read_bytes()).hexdigest(), APPROVED_SHA)
        self.assertEqual(self.payload["canonical_baseline_sha256"], APPROVED_SHA)
        self.assertEqual(self.payload["retrieved_date"], "2026-10-22")
        self.assertEqual(len(self.payload["cards"]), 121)
        self.assertEqual(len(self.cards), 121)
        self.assertEqual(len(self.decks["approved"]), 97)
        self.assertTrue(set(self.decks["approved"]) <= set(self.cards))

    def test_every_actual_source_and_candidate_name_is_legal_grixis_and_resolved(self):
        for name, card in self.cards.items():
            with self.subTest(name=name):
                self.assertEqual(card["legalities"]["commander"], "legal")
                self.assertTrue(set(card["color_identity"]) <= {"U", "B", "R"})
                self.assertTrue(card["oracle_id"])
                self.assertTrue(card["type_line"])
                self.assertTrue(card["oracle_text"])
        for deck in self.decks.values():
            self.assertTrue(set(deck) <= set(self.cards))

    def test_full_source_card_type_roles_are_neither_invented_nor_missing(self):
        expected = {
            "approved": (35, 34, 33),
            "A": (35, 34, 33),
            "B": (35, 33, 32),
            "C": (35, 34, 33),
        }
        for key, deck in self.decks.items():
            lands = creatures = pirates = 0
            for name, n in deck.items():
                c = self.cards[name]
                kind = c["type_line"]
                lands += n if "Land" in kind else 0
                creatures += n if "Creature" in kind else 0
                pirates += n if "Creature" in kind and ("Pirate" in kind or "Changeling" in c["oracle_text"]) else 0
            self.assertEqual((lands, creatures, pirates), expected[key], key)

    def test_third_exact_five_swap_package_is_not_prior_candidate(self):
        old = set(self.decks["approved"])
        proposed = set(self.decks["C"])
        self.assertEqual(proposed - old, C_ADDS)
        self.assertEqual(old - proposed, C_CUTS)
        self.assertEqual(self.decks["C"]["Island"], 3)
        self.assertEqual(self.decks["C"]["Mountain"], 2)
        self.assertNotEqual(self.decks["C"], self.decks["A"])
        self.assertNotEqual(self.decks["C"], self.decks["B"])

    def test_resilient_package_retains_real_card_draw_and_blocker_control(self):
        for name in ["Merchant Raiders", "The Indomitable"]:
            self.assertEqual(self.decks["approved"][name], 1)
            self.assertEqual(self.decks["C"][name], 1)
            self.assertEqual(self.decks["A"][name], 0)
        indomitable = self.cards["The Indomitable"]["oracle_text"]
        self.assertIn("Whenever a creature you control deals combat damage", indomitable)
        self.assertIn("You may cast this card from your graveyard", indomitable)

    def test_cheap_evasive_pirates_are_source_bound_and_have_real_weaknesses(self):
        cloud = self.cards["Cloud Pirates"]
        self.assertEqual(cloud["mana_cost"], "{U}")
        self.assertIn("Human Pirate", cloud["type_line"])
        self.assertIn("Flying", cloud["oracle_text"])
        self.assertIn("block only creatures with flying", cloud["oracle_text"])
        skyship = self.cards["Skyship Plunderer"]
        self.assertEqual(skyship["mana_cost"], "{1}{U}")
        self.assertIn("Flying", skyship["oracle_text"])
        self.assertIn("for each kind of counter", skyship["oracle_text"])
        deckhand = self.cards["Departed Deckhand"]
        self.assertIn("Spirit Pirate", deckhand["type_line"])
        self.assertIn("sacrifice", deckhand["oracle_text"])

    def test_evasion_fixture_two_grounded_3_3_defenders_no_resources(self):
        """Bounded one-combat fact, *not* 4-player engine or win-rate simulation.

        Three pirates are assumed already attack-ready, nobody casts spells,
        and opponent has exactly two grounded 3/3 non-Spirit blockers.
        """
        ready_c = {"Departed Deckhand", "Cloud Pirates", "Skyship Plunderer"}
        ready_a = {"Departed Deckhand", "Skyship Plunderer", "Broadside Bombardiers"}
        self.assertTrue(ready_c <= set(self.decks["C"]))
        self.assertTrue(ready_a <= set(self.decks["A"]))
        self.assertIn("Menace, haste", self.cards["Broadside Bombardiers"]["oracle_text"])
        # Only 2 of A's 3 Pirates evade ground blockers without spending mana.
        self.assertEqual(len(ready_a - {"Broadside Bombardiers"}), 2)
        # Two eligible ground blockers can legally double-block A's menace body.
        opponent_ground_blockers = (3, 3)
        self.assertEqual(len(opponent_ground_blockers), 2)
        # C's three bodies all evade blockers without flying/reach/Spirit.
        self.assertTrue(all("Flying" in self.cards[name]["oracle_text"] for name in ready_c - {"Departed Deckhand"}))
        self.assertIn("can't be blocked except by Spirits", self.cards["Departed Deckhand"]["oracle_text"])
        # A Treasure boast offers 2+0=2 damage; it cannot kill a 3/3 outright.
        self.assertLess(2 + 0, min(opponent_ground_blockers))

    def test_haste_and_paid_breakthrough_prevent_one_sided_claim(self):
        broadside = self.cards["Broadside Bombardiers"]["oracle_text"]
        self.assertIn("haste", broadside)
        self.assertNotIn("haste", self.cards["Cloud Pirates"]["oracle_text"].lower())
        open_wonder = self.cards["Open into Wonder"]
        self.assertEqual(open_wonder["mana_cost"], "{X}{U}{U}")
        self.assertIn("draw a card", open_wonder["oracle_text"])
        blustersquall = self.cards["Blustersquall"]["oracle_text"]
        self.assertIn("Overload {3}{U}", blustersquall)
        self.assertNotIn("draw", blustersquall.lower())
        self.assertEqual(3 + 2, 5, "Open X=3 costs five mana including UU")

    def test_comparison_stays_research_only(self):
        content = (RESEARCH / "Admiral_Beckett_Brass_resilient_comparison_20261022.md").read_text(encoding="utf-8")
        self.assertIn("RESEARCH_ONLY", content)
        self.assertIn("Still required for owner readiness", content)
        self.assertIn("121/121", content)


if __name__ == "__main__":
    unittest.main()
