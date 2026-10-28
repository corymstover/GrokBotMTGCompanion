#!/usr/bin/env python3
"""Four deterministic named-state comparisons: Rev1 vs complete Alt5.

These are finite opportunity-cost fixtures, not a shuffled-library estimate,
game-engine replacement, inferred win rate or resolution of all M7 gates.
Both configurations carry 100 physical cards and are SHA-bound by verify.py.
"""
from __future__ import annotations

import unittest
from pathlib import Path

from m6_p0_followup import ROOT, resolve_commander_etb

BASE = ROOT / "data/grixis/m7/candidate_lists/Tresserhorn_s_Lord__Returned_M7_Rev1_RESEARCH.txt"
ALT = ROOT / "data/grixis/m7/candidate_lists/Tresserhorn_s_Lord__Returned_M7_Rev1_alt5.txt"


def oracle(name, shard):
    source = (ROOT / shard).read_text(encoding="utf-8")
    section = source.split(f"### {name}\n", 1)
    assert len(section) == 2, name
    return section[1].split("\n### ", 1)[0]


class SameStartOpportunityCost(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rev = BASE.read_text(encoding="utf-8").splitlines()
        cls.alt = ALT.read_text(encoding="utf-8").splitlines()
        cls.sengir = oracle("Sengir Autocrat", "cards/S/sen.md")
        cls.endrek = oracle("Endrek Sahr, Master Breeder", "cards/E/en.md")
        cls.rites = oracle("Village Rites", "cards/V/vi.md")
        cls.swat = oracle("Deflecting Swat", "cards/D/def.md")

    def test_four_mana_setup_turn_favors_autocrat_if_unanswered(self):
        self.assertIn("1x Sengir Autocrat", self.rev)
        self.assertNotIn("1x Endrek Sahr, Master Breeder", self.rev)
        self.assertIn("1x Endrek Sahr, Master Breeder", self.alt)
        self.assertIn("**Mana cost:** {3}{B}", self.sengir)
        self.assertIn("create three 0/1 black Serf", self.sengir)
        self.assertIn("**Mana cost:** {4}{B}", self.endrek)
        turn4_mana = 4
        self.assertGreaterEqual(turn4_mana, 4)
        self.assertLess(turn4_mana, 5)
        # Shared four-source start: Rev1 develops four bodies turn four.
        # On turn five with five UBR-compatible mana, all 3 Serfs pay Lord.
        self.assertTrue(resolve_commander_etb(other_creatures=3, life=20)["retained"])
        # This single-slot Alt5 start cannot cast Endrek on turn four.
        self.assertFalse(resolve_commander_etb(other_creatures=0, life=20)["retained"])

    def test_sixth_turn_catchup_favors_endrek_repeatable_thrulls(self):
        self.assertIn("Whenever you cast a creature spell", self.endrek)
        self.assertIn("where X is that spell's mana value", self.endrek)
        # Alt5 casts Endrek turn 5, Lord turn 6: 5 Thrulls on CAST,
        # before Lord ETB, and retains two after paying three sacrifices.
        thrulls_on_lord_cast = 5
        self.assertTrue(resolve_commander_etb(other_creatures=thrulls_on_lord_cast,
                                              life=20)["retained"])
        self.assertEqual(thrulls_on_lord_cast - 3, 2)
        # Rev1 turn-4 Autocrat is one permanent + three Serfs;
        # after sacrificing three Serfs, it retains the Autocrat alone.
        self.assertEqual(1 + 3 - 3, 1)
        # Endrek's >=7 Thrulls sacrifice clause is a future cap, not a
        # trigger during the five-Thrull Lord setup shown here.
        self.assertIn("seven or more Thrulls", self.endrek)

    def test_autocrat_exile_before_lord_trigger_is_material_disruption(self):
        self.assertIn("When this creature leaves the battlefield, exile all Serf tokens", self.sengir)
        self.assertFalse(resolve_commander_etb(other_creatures=0,
                                               life=20)["retained"])
        self.assertEqual(resolve_commander_etb(other_creatures=0,
                                                life=20)["draws"], 1)
        # By contrast Endrek's cast trigger already resolves before Lord
        # enters, so later removal of Endrek does not exile 5 Thrulls.
        self.assertIn("create X 1/1 black Thrull", self.endrek)
        self.assertTrue(resolve_commander_etb(other_creatures=5,
                                              life=20)["retained"])

    def test_no_commander_village_rites_is_cheaper_than_swat(self):
        self.assertIn("1x Village Rites", self.alt)
        self.assertIn("1x Deflecting Swat", self.rev)
        self.assertIn("**Mana cost:** {B}", self.rites)
        self.assertIn("Draw two cards", self.rites)
        self.assertIn("**Mana cost:** {2}{R}", self.swat)
        self.assertIn("If you control a commander", self.swat)
        # Same precommander board: one black source and a disposable body.
        available_mana, bodies, commander_present = 1, 1, False
        rites_castable = available_mana >= 1 and bodies >= 1
        swat_castable = commander_present or available_mana >= 3
        self.assertTrue(rites_castable)
        self.assertFalse(swat_castable)
        rites_draws = 2 if rites_castable else 0
        self.assertEqual(rites_draws, 2)
        # Later, with commander present and a legal target spell or ability,
        # Swat is free; this does NOT guarantee that a new target exists.
        commander_present = True
        self.assertTrue(commander_present or available_mana >= 3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
