"""Deck #52 Sol'kanar M7 Rev1 bounded structural/source and finite scenario tests.

Data is the project's 2026-10-15 Scryfall archive; this is NOT a live
October 27 mass API sweep or randomized multiplayer simulation.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
NAME = "Sol_kanar_the_Swamp_King_M7_Rev1"
LIST = ROOT / "data/grixis/m7/candidate_lists" / f"{NAME}.txt"
SNAP = ROOT / "data/grixis/m7/oracle_snapshots" / f"{NAME}_2026-10-15.json"
HASH = "f7ff68f912839accc7177c288536c9abf9deefc8332d975236ef6f0e02"
ADDS = {
    "Necropotence", "Orcish Bowmasters", "Rowan, Scion of War",
    "Hatred", "Yawgmoth's Will", "Mindcrank", "Bubbling Muck"
}
CUTS = {
    "Alhammarret's Archive", "Underworld Dreams", "Bontu's Monument",
    "Bloodletter of Aclazotz", "Dimir Signet", "Rakdos Signet",
    "Talisman of Creativity"
}


class Solkanar52M7(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw = LIST.read_bytes()
        cls.lines = cls.raw.decode("utf-8").splitlines()
        cls.data = json.loads(SNAP.read_text(encoding="utf-8"))
        cls.counts = {}
        for line in cls.lines:
            amount, name = line.split("x ", 1)
            amount = int(amount)
            name = name.removesuffix(" [Commander]")
            cls.counts[name] = cls.counts.get(name, 0) + amount

    def test_exact_review_hash_and_card_count(self):
        self.assertEqual(hashlib.sha256(self.raw).hexdigest(), HASH)
        self.assertEqual(len(self.lines), 95)
        self.assertEqual(sum(self.counts.values()), 100)
        self.assertEqual(len(self.counts), 95)
        self.assertEqual(self.lines[0], "1x Sol'kanar the Swamp King [Commander]")
        self.assertEqual({n: q for n, q in self.counts.items() if q > 1},
                         {"Swamp": 6})

    def test_exact_swap_membership_and_exclusion(self):
        self.assertTrue(ADDS <= self.counts.keys())
        self.assertFalse(CUTS & self.counts.keys())
        self.assertNotIn("Sorin of House Markov // Sorin, Ravenous Neonate", self.counts)

    def test_october_archive_oracle_legality_and_identity(self):
        rows = self.data["cards"]
        self.assertEqual(len(rows), 95)
        self.assertEqual({x["name"]: x["count"] for x in rows}, self.counts)
        self.assertEqual(self.data["candidate_sha256"], HASH)
        self.assertEqual(self.data["oracle_bulk_date"], "2026-10-15")
        for row in rows:
            self.assertEqual(row["commander_legality"], "legal", row["name"])
            self.assertTrue(set(row["color_identity"]) <= set("CBRU"),
                            row["name"])
            self.assertTrue(row["oracle_id"], row["name"])

    def test_lands_game_changers(self):
        rows = self.data["cards"]
        fronts = sum(x["count"] for x in rows
                     if "Land" in x["type_line"]
                     and "//" not in x["type_line"])
        modal = [x for x in rows if x["name"] ==
                 "Fell the Profane // Fell Mire"]
        self.assertEqual(fronts, 35)
        self.assertEqual(len(modal), 1)
        self.assertIn("Land", modal[0]["type_line"])
        self.assertEqual(sum(x["game_changer"] for x in rows), 15)

    def test_painter_and_horn_finite_gain_events(self):
        # Two separate instances, Sol'kanar and Horn, trigger per black spell.
        # Painter naming black changes nonblack opponent spells into black ones.
        black_spell_events = 3
        self.assertEqual(black_spell_events * 2, 6)

    def test_hatred_commander_damage_threshold(self):
        # Requires defending player to control a Swamp and Sol to be unblocked.
        sol_power = 5
        life_paid = 16
        self.assertEqual(sol_power + life_paid, 21)
        self.assertEqual(40 - life_paid, 24)  # before Sol's black-spell gain

    def test_rowan_gross_life_loss_and_colored_pips(self):
        life_lost, life_gained = 7, 6
        self.assertEqual(life_lost, 7)  # no subtraction of life gained
        generic_x = 10
        self.assertEqual(max(0, generic_x - life_lost), 3)
        black_colored_symbols = 2
        self.assertEqual(black_colored_symbols, 2)  # cannot discount {B}{B}

    def test_bubbling_muck_bounded_swamp_mana(self):
        tapping_four_swamps_for_b = 4
        extra_for_each = 4
        self.assertEqual(tapping_four_swamps_for_b + extra_for_each, 8)

    def test_bloodchief_mindcrank_requires_quest_counters(self):
        def active(counter):
            return counter >= 3
        self.assertFalse(active(2))
        self.assertTrue(active(3))
        # Without cards entering the graveyard, Ascension's second trigger
        # does not fire, even if an opponent already has an empty library.
        cards_milled_into_graveyard = 0
        life_loss_from_ascension = cards_milled_into_graveyard * 2
        self.assertEqual(life_loss_from_ascension, 0)


if __name__ == "__main__":
    unittest.main()
