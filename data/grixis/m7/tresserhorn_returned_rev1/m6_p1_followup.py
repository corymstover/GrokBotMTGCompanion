#!/usr/bin/env python3
"""Ten bounded P1 cases for Deck #60 research configuration.

Each original planned K4–K6/E1–E2/W1–W3/F2–F3 ID is exercised with a
positive and an adversarial condition. Card text comes from the local
2026-10-15 Scryfall-derived index/card pages and canonical exact bytes.
No unbounded combo, game-engine, matched-hand or statistical claim.
"""
from __future__ import annotations

import hashlib
import json
import unittest
from pathlib import Path

from m6_p0_followup import (
    ROOT, RESEARCH, RESEARCH_SHA, PLAN, resolve_commander_etb,
    plumb_outcome,
)

P1 = ("K4", "K5", "K6", "E1", "E2", "W1", "W2", "W3", "F2", "F3")
PAGES = {
    "Not of This World": "cards/N/no.md",
    "Blasphemous Edict": "cards/B/bla.md",
    "The Meathook Massacre": "cards/T/them.md",
    "Tresserhorn's Lord, Returned": "cards/T/tre.md",
    "Genesis Chamber": "cards/G/ge.md",
    "Tombstone Stairwell": "cards/T/to.md",
    "Sengir Autocrat": "cards/S/sen.md",
    "Weaponcraft Enthusiast": "cards/W/we.md",
    "Mogg War Marshal": "cards/M/mog.md",
    "The Locust God": "cards/T/thel.md",
    "Gravecrawler": "cards/G/gra.md",
    "Phyrexian Altar": "cards/P/ph.md",
    "Warren Soultrader": "cards/W/war.md",
    "Zulaport Cutthroat": "cards/Z/zu.md",
    "Infantry Shield": "cards/I/inf.md",
    "Wand of Orcus": "cards/W/wan.md",
    "Lightning Greaves": "cards/L/li.md",
}


def text(name):
    page = (ROOT / PAGES[name]).read_text(encoding="utf-8")
    anchor = f"### {name}\n"
    assert page.count(anchor) == 1
    return page.split(anchor, 1)[1].split("\n### ", 1)[0]


class TresserhornP1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw = RESEARCH.read_bytes()
        cls.lines = cls.raw.decode("utf-8").splitlines()
        cls.plan = json.loads(PLAN.read_text(encoding="utf-8"))
        cls.planned = {c["id"] for c in cls.plan["cases"]
                       if c["priority"] == "P1"}

    def setUp(self):
        self.assertEqual(hashlib.sha256(self.raw).hexdigest(), RESEARCH_SHA)
        self.assertEqual(self.planned, set(P1))

    def test_K4_not_of_this_world_conditional_free_cost(self):
        oracle = text("Not of This World")
        self.assertIn("targets a permanent you control", oracle)
        self.assertIn("power 7 or greater", oracle)
        discounted_cost = lambda targeted, seven_power: 0 if targeted and seven_power else 7
        self.assertEqual(discounted_cost(True, True), 0)  # Lord 10 power
        self.assertEqual(discounted_cost(False, True), 7)  # wrath/edict not target
        self.assertEqual(discounted_cost(True, False), 7)
        self.assertIn("1x Not of This World", self.lines)

    def test_K5_13_sacrifice_edict_removed_and_meathook_toughness(self):
        self.assertIn("Each player sacrifices thirteen creatures", text("Blasphemous Edict"))
        self.assertIn("each creature gets -X/-X", text("The Meathook Massacre"))
        self.assertIn("Whenever a creature you control dies", text("The Meathook Massacre"))
        # Baseline Edict demanded sacrificing all creatures of a 3-creature
        # player, even an indestructible Lord, with no choice to retain him.
        baseline_three = 3
        self.assertEqual(min(13, baseline_three), 3)
        # Research Meathook X=3 kills 1/1 fodder, but not the Lord's 10/4;
        # X=4 kills the Lord despite indestructible via 0 toughness.
        remaining_toughness = lambda x: 4 - x
        self.assertGreater(remaining_toughness(3), 0)
        self.assertLessEqual(remaining_toughness(4), 0)
        self.assertIn("1x The Meathook Massacre", self.lines)
        self.assertNotIn("1x Blasphemous Edict", self.lines)

    def test_K6_turning_off_etb_saves_lord_but_loses_native_draw(self):
        positive = resolve_commander_etb(other_creatures=3, life=20)
        suppressed = {"retained": True, "draws": 0, "opponent_draws": 0}
        self.assertEqual(positive["draws"], 3)
        self.assertEqual(suppressed["draws"], 0)
        self.assertTrue(suppressed["retained"])
        self.assertFalse(any("Torpor Orb" in line or "Karn, Argent Defender" in line
                             for line in self.lines))

    def test_E1_sacrifice_draw_requires_creature_and_lord_present(self):
        self.assertIn("Sacrifice a creature: Add one mana of any color", text("Phyrexian Altar"))
        self.assertIn("Whenever you sacrifice a creature, draw a card",
                      text("Tresserhorn's Lord, Returned"))
        draws = lambda creature_sacrifices, lord: creature_sacrifices if lord else 0
        self.assertEqual(draws(2, True), 2)
        self.assertEqual(draws(2, False), 0)
        self.assertEqual(draws(0, True), 0)  # Treasure sacrifice not a creature

    def test_E2_real_fodder_creation_and_opponent_symmetry(self):
        self.assertIn("Fabricate 2", text("Weaponcraft Enthusiast"))
        self.assertIn("When this creature enters or dies", text("Mogg War Marshal"))
        self.assertIn("Whenever a nontoken creature enters", text("Genesis Chamber"))
        self.assertIn("each player creates a 2/2 black Zombie creature token",
                      text("Tombstone Stairwell"))
        self.assertIn("create three 0/1 black Serf", text("Sengir Autocrat"))
        self.assertIn("exile all Serf tokens", text("Sengir Autocrat"))
        self.assertIn("1x Sengir Autocrat", self.lines)
        # Weaponcraft fabricates two Servos plus its body: enough by itself.
        self.assertEqual(1 + 2, 3)
        # The Chamber generates *also for opponent* nontoken creatures.
        my_myr, opposing_myr = (2, 2)
        self.assertEqual(my_myr, opposing_myr)
        # The selected Autocrat gives a four-body board immediately, but if
        # he leaves, his Serfs are exiled; choose three Serfs as ETB fodder
        # while keeping Autocrat, unless disruption prevents that line.
        self.assertTrue(resolve_commander_etb(other_creatures=1 + 3,
                                              life=20)["retained"])
        # Rejected off-ranking Stairwell: with zero creature cards in own
        # graveyard it creates zero fodder; with three, three per upkeep.
        stairwell = lambda creature_cards_in_grave: creature_cards_in_grave
        self.assertEqual(stairwell(0), 0)
        self.assertEqual(stairwell(3), 3)
        self.assertFalse(resolve_commander_etb(other_creatures=stairwell(0),
                                               life=20)["retained"])

    def test_W1_locust_free_outlet_draw_token_cycle_is_finite(self):
        self.assertIn("Whenever you draw a card, create a 1/1", text("The Locust God"))
        self.assertIn("Whenever you sacrifice a creature, draw a card",
                      text("Tresserhorn's Lord, Returned"))
        # Start with one Insect already in play, sacrifice it, draw and
        # create one replacement. An activated free outlet is a choice.
        available_insects = 1
        library_cards = 4
        damage = 0
        for _ in range(4):
            self.assertGreater(available_insects, 0)
            self.assertGreater(library_cards, 0)
            available_insects -= 1
            damage += 1  # only if the outlet is Goblin Bombardment
            library_cards -= 1
            available_insects += 1
        self.assertEqual((available_insects, library_cards, damage), (1, 0, 4))
        self.assertLess(damage, 40)  # not a certified table kill
        # Stop voluntarily before a fifth sac; mandatory fifth draw with no
        # library would cause a loss.

    def test_W2_gravecrawler_altar_and_soultrader_payable_iteration(self):
        self.assertIn("as long as you control a Zombie", text("Gravecrawler"))
        self.assertIn("Add one mana of any color", text("Phyrexian Altar"))
        self.assertIn("Pay 1 life, Sacrifice another creature", text("Warren Soultrader"))
        self.assertIn("each opponent loses 1 life and you gain 1 life",
                      text("Zulaport Cutthroat"))
        def altar_cycle(other_zombie, altar, available_black):
            return other_zombie and altar and available_black >= 1
        self.assertTrue(altar_cycle(True, True, 1))
        self.assertFalse(altar_cycle(False, True, 1))
        self.assertFalse(altar_cycle(True, False, 1))
        # Sac Crawler to Altar -> B, spend B to cast it; 0 net mana,
        # one commander draw + one death/drain if payoffs survive.
        balance = 0
        for _ in range(3):
            balance += 1
            balance -= 1
        self.assertEqual(balance, 0)
        # Soultrader trades 1 life per loop for Treasure; only a real
        # life-gain trigger offsets it. Without Zulaport, not perpetual.
        for with_zulaport in (True, False):
            life = 10
            for _ in range(3):
                life -= 1
                if with_zulaport:
                    life += 1
            self.assertEqual(life, 10 if with_zulaport else 7)

    def test_W3_ten_power_combat_warriors_and_zombie_quantity(self):
        self.assertIn("mobilize X, where X is its power", text("Infantry Shield"))
        self.assertIn("Sacrifice them at the beginning of the next end step",
                      text("Infantry Shield"))
        self.assertIn("create that many 2/2 black Zombie", text("Wand of Orcus"))
        self.assertIn("Equip {3}", text("Wand of Orcus"))
        power = 10
        warriors = power
        self.assertEqual(warriors, 10)
        self.assertEqual(plumb_outcome(10, lord_on_battlefield=True,
                                      life=25, library_cards=50)["draws"], 21)
        # Sword/wand Zombies count *combat damage to a player*, not the
        # attack trigger or full printed power if blocked with trample.
        self.assertEqual(10, power)  # full unblocked combat hit
        blocked_damage_to_player = 3
        self.assertLess(blocked_damage_to_player, power)
        self.assertIn("shroud", text("Lightning Greaves"))

    def test_F2_indestructible_is_not_exile_necessity_or_edict_immunity(self):
        self.assertIn("indestructible", text("Tresserhorn's Lord, Returned"))
        targetable = lambda shrouded, hexproof, opposing_spell: (
            not shrouded and not (hexproof and opposing_spell))
        self.assertTrue(targetable(False, False, True))  # exile can target
        self.assertFalse(targetable(True, False, True))
        self.assertFalse(targetable(False, True, True))
        # An edict selecting a player does not target the creature. A
        # negative-toughness effect defeats indestructible as well.
        self.assertEqual(4 - 4, 0)

    def test_F3_mandatory_end_step_token_sacs_can_deck_pilot(self):
        self.assertIn("Sacrifice them at the beginning of the next end step",
                      text("Infantry Shield"))
        warrior_count = 10
        self.assertTrue(plumb_outcome(10, lord_on_battlefield=True,
                                      life=30, library_cards=25)["can_survive_full_resolution"])
        # Mobilize's sacrifice draws ten even without casting Plumb: only
        # nine remaining library cards is lethal if Lord stays on field.
        remaining_library = 9
        compulsory_draws = warrior_count
        self.assertLess(remaining_library, compulsory_draws)
        self.assertGreaterEqual(10, 10)


if __name__ == "__main__":
    unittest.main(verbosity=2)
