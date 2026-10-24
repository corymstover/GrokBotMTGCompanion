"""Finite source-anchored rules/mana cases for the Anhelo, the Painter M7 candidate.

Seed 0, no randomness. Bounded rules model, NOT a game engine or win-rate measurement;
supports no improvement claim by itself.
"""
from collections import Counter
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SNAP = ROOT / "data/grixis/m6/oracle_snapshots/Anhelo__the_Painter_M7_Scryfall_20261023.json"
CAND = ROOT / "data/grixis/m7/candidate_lists/Anhelo__the_Painter.txt"
BASE = ROOT / "data/grixis/m7/baseline_sources/Anhelo_the_Painter_approved_source_2026-10-13.txt"
ADDS = ["Skyclave Shade", "Sinister Concierge", "Dogged Detective", "Tenacious Underdog", "Bedevil"]
CUTS = ["Fellwar Stone", "Talisman of Indulgence", "Exotic Orchard", "Talisman of Dominance", "Feed the Swarm"]
ROCKS = {"Sol Ring", "Arcane Signet", "Fellwar Stone", "Dimir Signet", "Izzet Signet", "Rakdos Signet",
         "Talisman of Creativity", "Talisman of Dominance", "Talisman of Indulgence"}
COMBO = ["Reiterate", "Mana Geyser", "Jeska's Will", "Narset's Reversal", "Twinning Staff", "Dualcaster Mage",
         "Twinflame", "Primal Amulet", "Frantic Search", "Ral, Storm Conduit", "Storm-Kiln Artist"]


def names(path):
    out = Counter()
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            q, raw = line.split("x ", 1)
            out[raw.removesuffix(" [Commander]").split(" // ")[0]] += int(q)
    return out


def casualty_turn(spells, board):
    """Model Anhelo: only the first instant/sorcery CAST this turn has casualty 2.

    spells: list of (name, creates_token_power or None). board: list of creature powers.
    Returns number of casualty copies made. Tokens made by a spell arrive after its casting.
    """
    copies, first = 0, True
    board = list(board)
    for _, token in spells:
        if first:
            first = False
            eligible = [p for p in board if p >= 2]
            if eligible:
                board.remove(min(eligible))
                copies += 1
        if token is not None:
            board.append(token)
    return copies


class AnheloM7Mechanics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        snap = json.loads(SNAP.read_text())
        cls.cards = {c["name"].split(" // ")[0]: c for c in snap["cards"]}
        cls.cand, cls.base = names(CAND), names(BASE)

    def test_commander_oracle_is_first_spell_casualty_2(self):
        t = self.cards["Anhelo, the Painter"]["oracle_text"]
        self.assertIn("The first instant or sorcery spell you cast each turn has casualty 2", t)

    def test_instant_made_token_cannot_pay_same_turn_casualty(self):
        self.assertEqual(casualty_turn([("Startle", 2)], []), 0)
        self.assertEqual(casualty_turn([("Startle", 2), ("Counterspell", None)], []), 0)
        self.assertEqual(casualty_turn([("Counterspell", None)], [3]), 1)

    def test_selected_bodies_are_casualty_legal_and_recursive(self):
        for n in ["Skyclave Shade", "Sinister Concierge", "Dogged Detective", "Tenacious Underdog"]:
            c = self.cards[n]
            self.assertGreaterEqual(int(c["power"]), 2, n)
            self.assertIn("Creature", c["type_line"])
        self.assertIn("cast it from your graveyard", self.cards["Skyclave Shade"]["oracle_text"])
        self.assertIn("cast this card from your graveyard using its blitz ability", self.cards["Tenacious Underdog"]["oracle_text"])
        self.assertIn("return this card from your graveyard to your hand", self.cards["Dogged Detective"]["oracle_text"])
        self.assertIn("gains suspend", self.cards["Sinister Concierge"]["oracle_text"])

    def test_blitz_underdog_sacrificed_to_casualty_draws(self):
        t = self.cards["Tenacious Underdog"]["oracle_text"]
        self.assertIn("When this creature dies, draw a card", t)
        self.assertEqual(casualty_turn([("Demonic Tutor", None)], [3]), 1)

    def test_bedevil_is_instant_and_feed_the_swarm_sorcery(self):
        self.assertEqual(self.cards["Bedevil"]["type_line"], "Instant")
        self.assertEqual(self.cards["Feed the Swarm"]["type_line"], "Sorcery")
        self.assertIn("artifact, creature, or planeswalker", self.cards["Bedevil"]["oracle_text"])

    def test_exact_swaps_and_combo_core_preserved(self):
        self.assertEqual(sorted((self.cand - self.base).elements()), sorted(ADDS))
        self.assertEqual(sorted((self.base - self.cand).elements()), sorted(CUTS))
        for n in COMBO:
            self.assertEqual(self.cand[n], 1, n)

    def test_quantity_counted_lands_and_rocks(self):
        land = lambda deck: sum(q for n, q in deck.items() if "Land" in self.cards[n]["type_line"].split(" // ")[0])
        self.assertEqual(land(self.base), 34)
        self.assertEqual(land(self.cand), 33)
        self.assertEqual(sum(q for n, q in self.base.items() if n in ROCKS), 9)
        self.assertEqual(sum(q for n, q in self.cand.items() if n in ROCKS), 6)
        self.assertEqual(sum(self.cand.values()), 100)

    def test_legality_identity_singleton(self):
        for n, q in self.cand.items():
            c = self.cards[n]
            self.assertEqual(c["commander_legality"], "legal", n)
            self.assertTrue(set(c["color_identity"]) <= {"U", "B", "R"}, n)
            if n not in {"Island", "Swamp", "Mountain"}:
                self.assertEqual(q, 1, n)

    def test_game_changers_unchanged(self):
        gc = lambda deck: sorted(n for n in deck if self.cards[n]["game_changer"])
        self.assertEqual(gc(self.cand), gc(self.base))
        self.assertEqual(len(gc(self.cand)), 7)


if __name__ == "__main__":
    unittest.main()
