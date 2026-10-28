#!/usr/bin/env python3
"""Deck #60 historical-baseline M6 P0 source-paid finite assertions.

These cases execute the exact C1, K1, K2, K3 and F1 IDs in the immutable
Tresserhorn_s_Lord__Returned M6 design plan.  They are bounded rules fixtures,
NOT a general Magic engine, a randomized game test, or a certification of a
future M7 replacement list.  Their source is the October 15, 2026 canonical
approved 100 and the engineering repository's October 16 Oracle card pages;
the commander's November 13 legality date remains a registered exception.
"""
from __future__ import annotations

import hashlib
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
DECK = HERE / "Tresserhorn_Returned_Oct15_baseline.txt"
PLAN = ROOT / "data/grixis/m6/test_blueprints/Tresserhorn_s_Lord__Returned.json"
BASELINE_SHA = "8c802586a4742156fb96246f4f23331eb51d1a77d6717da63ceed2446e98adf8"
RESEARCH = ROOT / "data/grixis/m7/candidate_lists/Tresserhorn_s_Lord__Returned_M7_Rev1_RESEARCH.txt"
RESEARCH_SHA = "9a9d2f7a344e2491444c0a0e4c48525dfe8faa37032eaf8e22a94082f6fbf60e"
CASE_IDS = ("C1", "K1", "K2", "K3", "F1")


def oracle_section(name: str) -> str:
    """Recover the frozen Scryfall-derived Oracle section, not an invented card."""
    pages = {
        "Tresserhorn's Lord, Returned": "cards/T/tre.md",
        "Nightscape Familiar": "cards/N/ni.md",
        "Plumb the Forbidden": "cards/P/pl.md",
    }
    path = ROOT / pages[name]
    text = path.read_text(encoding="utf-8")
    anchor = f"### {name}\n"
    assert text.count(anchor) == 1, (name, path)
    return text.split(anchor, 1)[1].split("\n### ", 1)[0]


def resolve_commander_etb(*, other_creatures: int, life: int,
                          target_opponent: bool = True) -> dict:
    """Finite resolution when Tresserhorn and its trigger are on the battlefield.

    A legal targeted opponent is the ordinary Commander-pod precondition.
    Life=3 can pay three life but loses on state-based actions at zero.
    When unable to complete all payments, the commander is sacrificed and its
    last ability observes that sacrifice, yielding one pending card draw.
    """
    if not target_opponent:
        return {"retained": True, "creatures_sacrificed": 0,
                "draws": 0, "opponent_draws": 0, "life_after": life,
                "survives": life > 0, "trigger_countered": True}
    can_pay = other_creatures >= 3 and life >= 3
    spent = 3 if can_pay else 0
    sacrificed = 3 if can_pay else 1
    return {"retained": can_pay, "creatures_sacrificed": sacrificed,
            "draws": sacrificed, "opponent_draws": 3 if can_pay else 0,
            "life_after": life - spent, "survives": life - spent > 0,
            "trigger_countered": False}


def plumb_outcome(sacrifices: int, *, lord_on_battlefield: bool,
                  life: int, library_cards: int) -> dict:
    """Explicit stack arithmetic, before opponents or intervening replacements."""
    if sacrifices < 0:
        raise ValueError("negative sacrifices")
    plumb_spells = 1 + sacrifices
    lord_triggers = sacrifices if lord_on_battlefield else 0
    cards_demanded = plumb_spells + lord_triggers
    life_after = life - plumb_spells
    return {"copies": sacrifices, "originals": 1, "draws": cards_demanded,
            "life_after": life_after,
            "can_survive_full_resolution": life_after > 0 and
            library_cards >= cards_demanded}


class TresserhornP0(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        raw = DECK.read_bytes()
        cls.source_sha = hashlib.sha256(raw).hexdigest()
        cls.names = []
        for line in raw.decode("utf-8").splitlines():
            m = re.fullmatch(r"(\d+)x (.+)", line)
            assert m, line
            cls.names.extend([m[2].removesuffix(" [Commander]")] * int(m[1]))
        cls.plan = json.loads(PLAN.read_text(encoding="utf-8"))
        cls.research_bytes = RESEARCH.read_bytes()
        cls.research_names = []
        for line in cls.research_bytes.decode("utf-8").splitlines():
            m = re.fullmatch(r"(\d+)x (.+)", line)
            assert m, line
            cls.research_names.extend([m[2].removesuffix(" [Commander]")] * int(m[1]))
        cls.case_ids = {case["id"] for case in cls.plan["cases"]
                        if case["priority"] == "P0"}

    def setUp(self):
        self.assertEqual(self.source_sha, BASELINE_SHA)
        self.assertEqual(hashlib.sha256(self.research_bytes).hexdigest(), RESEARCH_SHA)
        self.assertEqual(len(self.names), 100)
        self.assertEqual(len(self.research_names), 100)
        self.assertEqual(self.names[0], "Tresserhorn's Lord, Returned")
        self.assertEqual(self.research_names[0], "Tresserhorn's Lord, Returned")
        self.assertEqual(self.case_ids, set(CASE_IDS))

    def test_C1_payable_commander_legal_zone_and_release_exception(self):
        source = oracle_section("Tresserhorn's Lord, Returned")
        self.assertIn("**Mana cost:** {2}{U}{B}{R}", source)
        self.assertIn("**P/T:** 10/4", source)
        self.assertIn("Trample, indestructible", source)
        self.assertIn("Whenever you sacrifice a creature, draw a card.", source)
        self.assertIn("Commander format: **not legal**", source)
        future = self.plan["exceptions"]["future_release"][0]
        self.assertEqual(future["legal_from"], "2026-11-13")
        self.assertEqual(future["project_authorization"], "AUTHORIZED_FUTURE_RELEASE")
        self.assertEqual(self.names.count("Tresserhorn's Lord, Returned"), 1)
        self.assertFalse(resolve_commander_etb(other_creatures=2, life=30)["retained"])

    def test_K1_three_distinct_sacrifices_three_draws_and_self_sacrifice(self):
        source = oracle_section("Tresserhorn's Lord, Returned")
        self.assertIn("sacrifice three creatures, pay 3 life", source)
        self.assertIn("target opponent draw three cards", source)
        paid = resolve_commander_etb(other_creatures=3, life=20)
        self.assertEqual(paid, {"retained": True, "creatures_sacrificed": 3,
                               "draws": 3, "opponent_draws": 3,
                               "life_after": 17, "survives": True,
                               "trigger_countered": False})
        # The official MBC release ruling explicitly observes the Lord's own
        # sacrifice, even if simultaneous with other creatures.
        failed = resolve_commander_etb(other_creatures=0, life=20)
        self.assertEqual((failed["retained"], failed["draws"],
                          failed["opponent_draws"]), (False, 1, 0))
        # A target that has become illegal counters the entire triggered
        # ability on resolution; it does not enforce an impossible payment.
        no_target = resolve_commander_etb(other_creatures=0, life=20,
                                           target_opponent=False)
        self.assertTrue(no_target["retained"])
        self.assertEqual(no_target["draws"], 0)

    def test_K2_plumb_number_of_copies_cards_life_and_deck_boundary(self):
        plumb = oracle_section("Plumb the Forbidden")
        self.assertIn("As an additional cost to cast this spell", plumb)
        self.assertIn("copy this spell for each creature sacrificed", plumb)
        self.assertIn("You draw a card and lose 1 life.", plumb)
        # Three sacrifices before resolution: 3 commander draws + 4
        # Plumb/copy draws, life -4. They are NOT seven free draws.
        a = plumb_outcome(3, lord_on_battlefield=True, life=20,
                          library_cards=50)
        self.assertEqual((a["copies"], a["draws"], a["life_after"]),
                         (3, 7, 16))
        self.assertTrue(a["can_survive_full_resolution"])
        self.assertEqual(plumb_outcome(0, lord_on_battlefield=True,
                                      life=20, library_cards=50)["draws"], 1)
        self.assertEqual(plumb_outcome(3, lord_on_battlefield=False,
                                      life=20, library_cards=50)["draws"], 4)
        self.assertFalse(plumb_outcome(3, lord_on_battlefield=True,
                                       life=3, library_cards=50)
                         ["can_survive_full_resolution"])
        self.assertFalse(plumb_outcome(3, lord_on_battlefield=True,
                                       life=20, library_cards=6)
                         ["can_survive_full_resolution"])

    def test_K3_familiar_is_one_generic_reduction_not_two(self):
        familiar = oracle_section("Nightscape Familiar")
        self.assertIn("Blue spells and red spells you cast cost {1} less", familiar)
        self.assertIn("Can never affect the colored part of the cost", familiar)
        lord = oracle_section("Tresserhorn's Lord, Returned")
        self.assertIn("**Mana cost:** {2}{U}{B}{R}", lord)
        cost = lambda generic, blue_or_red, familiar_in_play: (
            max(0, generic - int(blue_or_red and familiar_in_play)), "U", "B", "R")
        self.assertEqual(cost(2, True, True), (1, "U", "B", "R"))
        self.assertEqual(cost(2, True, False), (2, "U", "B", "R"))
        self.assertEqual(cost(2, False, True), (2, "U", "B", "R"))
        self.assertNotEqual(cost(2, True, True)[0], 0)

    def test_F1_precommit_fodder_life_gift_and_adversarial_failure(self):
        results = [resolve_commander_etb(other_creatures=b, life=20)
                   for b in (0, 1, 2, 3, 4)]
        self.assertEqual([r["retained"] for r in results],
                         [False, False, False, True, True])
        self.assertEqual([r["draws"] for r in results], [1, 1, 1, 3, 3])
        for poor in (0, 1, 2):
            self.assertFalse(resolve_commander_etb(
                other_creatures=4, life=poor)["retained"])
        exactly_three = resolve_commander_etb(other_creatures=3, life=3)
        self.assertTrue(exactly_three["retained"])
        self.assertFalse(exactly_three["survives"])
        # Token makers provide bodies but do not waive the opponent-card gift.
        for name in ("Mogg War Marshal", "Weaponcraft Enthusiast",
                     "Ophiomancer", "Bitterblossom"):
            self.assertIn(name, self.names)
            self.assertIn(name, self.research_names)
        self.assertEqual(results[3]["opponent_draws"], 3)
        # New 7-swap RESEARCH configuration has a different early-fodder
        # portfolio; transferring F1 cannot assume removed Endrek is present.
        self.assertIn("Genesis Chamber", self.research_names)
        self.assertIn("Sengir Autocrat", self.research_names)
        self.assertNotIn("Endrek Sahr, Master Breeder", self.research_names)
        # One Weaponcraft (body + fabricate-2 Servos) is enough for payment.
        # The Chamber's Myr when untapped is an optional fourth body.
        bodies_with_fabricate = 1 + 2
        self.assertTrue(resolve_commander_etb(other_creatures=bodies_with_fabricate,
                                              life=20)["retained"])
        # An opponent removing one body before Lord's ETB resolves prevents
        # the payment, even with seven appealing swaps in the library.
        self.assertFalse(resolve_commander_etb(other_creatures=bodies_with_fabricate - 1,
                                               life=20)["retained"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
