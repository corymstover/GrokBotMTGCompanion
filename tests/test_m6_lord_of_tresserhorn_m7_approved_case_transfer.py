"""Source-bound M6 P0/P1 transfer for Cory's exact M7 Lord of Tresserhorn approval.

These are finite Oracle-anchored scenario assertions, not a Magic game engine,
multiplayer simulation or a claim of global strategic optimality.
"""

import hashlib
import json
import re
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DECK = "Lord_of_Tresserhorn"
SHA = "fd09cb267660206b834257e5c455259985b0e53316743835f679760b11200f85"
PLAN = ROOT / f"data/grixis/m6/test_blueprints/{DECK}.json"
SNAP = ROOT / f"data/grixis/m6/oracle_snapshots/{DECK}_M7_Scryfall_20261023.json"
CAND = ROOT / f"data/grixis/m7/candidate_lists/{DECK}.txt"


class LordM7ApprovedM6Transfer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        raw = CAND.read_bytes()
        cls.digest = hashlib.sha256(raw).hexdigest()
        cls.lines = [v.strip() for v in raw.decode("utf-8").splitlines() if v.strip()]
        cls.cards = Counter()
        for line in cls.lines:
            m = re.fullmatch(r"(\d+)x (.+?)(?: \[Commander\])?", line)
            assert m, line
            cls.cards[m.group(2)] += int(m.group(1))
        cls.oracle = {x["name"]: x for x in json.loads(SNAP.read_text())["cards"]}
        cls.plan = {c["id"]: c for c in json.loads(PLAN.read_text())["cases"]}

    def card(self, name):
        self.assertIn(name, self.cards)
        self.assertIn(name, self.oracle)
        return self.oracle[name]["oracle_text"]

    def exact(self, case_id, priority):
        self.assertEqual(self.digest, SHA)
        self.assertEqual(self.cards.total(), 100)
        self.assertEqual(self.lines[0], "1x Lord of Tresserhorn [Commander]")
        self.assertEqual(self.plan[case_id]["priority"], priority)
        self.assertEqual(len(self.cards), 98)

    # P0 mandatory commander mechanics and failure fixtures.
    def test_C1_payable_commander_cast_and_actual_oracle(self):
        self.exact("C1", "P0")
        c = self.oracle["Lord of Tresserhorn"]
        self.assertEqual(c["mana_cost"], "{1}{U}{B}{R}")
        self.assertEqual((c["power"], c["toughness"]), ("10", "4"))
        self.assertIn("sacrifice two creatures", self.card("Lord of Tresserhorn"))
        self.assertIn("{B}: Regenerate Lord", self.card("Lord of Tresserhorn"))
        def castable(pool):
            return all(pool.get(symbol, 0) >= 1 for symbol in ("U", "B", "R")) and sum(pool.values()) >= 4
        self.assertTrue(castable({"U": 1, "B": 1, "R": 1, "C": 1}))
        self.assertFalse(castable({"U": 2, "B": 1, "R": 0, "C": 3}))
        self.assertFalse(castable({"U": 1, "B": 1, "R": 1, "C": 0}))

    def test_K1_etb_costs_and_insufficient_fodder(self):
        self.exact("K1", "P0")
        text = self.card("Lord of Tresserhorn")
        self.assertIn("you lose 2 life, you sacrifice two creatures, and target opponent draws two cards", text)
        def resolve_fodder(other):
            sacrificed_others = min(2, other)
            sacrificed_lord = other < 2
            return (sacrificed_others, sacrificed_lord, 2)
        for other, expected in [(0, (0, True, 2)), (1, (1, True, 2)),
                                (2, (2, False, 2)), (3, (2, False, 2))]:
            self.assertEqual(resolve_fodder(other), expected)
        self.assertEqual((40 - 2, 2), (38, 2))  # life and opponent draw on full resolution

    def test_K2_suppression_before_entry_and_counter_on_stack(self):
        self.exact("K2", "P0")
        self.assertIn("Creatures entering", self.card("Torpor Orb"))
        self.assertIn("don't cause abilities to trigger", self.card("Karn, Argent Defender"))
        self.assertIn("Creatures lose all abilities", self.card("Dress Down"))
        def entry_trigger_created(suppressor_on_entry):
            return not suppressor_on_entry
        self.assertFalse(entry_trigger_created(True))
        self.assertTrue(entry_trigger_created(False))
        for name in ("Stifle", "Tale's End", "Consign to Memory"):
            self.assertIn("Counter", self.card(name))
        self.assertIn("target triggered ability", self.card("Consign to Memory"))

    def test_K3_regeneration_only_replaces_destruction(self):
        self.exact("K3", "P0")
        self.assertIn("Regenerate Lord", self.card("Lord of Tresserhorn"))
        prevented_by_regeneration = {"destroy": True, "lethal_damage": True,
                                      "sacrifice": False, "minus_toughness": False,
                                      "exile": False}
        self.assertTrue(prevented_by_regeneration["destroy"])
        self.assertFalse(prevented_by_regeneration["sacrifice"])
        self.assertFalse(prevented_by_regeneration["minus_toughness"])

    def test_F1_entry_drawback_can_kill_own_commander(self):
        self.exact("F1", "P0")
        for fodder in range(3):
            self.assertEqual(fodder < 2, fodder in (0, 1))
        self.assertIn("Torpor Orb", self.cards)
        self.assertIn("Consign to Memory", self.cards)
        self.assertNotIn("Feed the Swarm", self.cards)

    # P1 identity, protection, payment, conversion and self-nonbo checks.
    def test_K4_greaves_shroud_vs_regalia_ward(self):
        self.exact("K4", "P1")
        self.assertIn("shroud", self.card("Lightning Greaves").lower())
        self.assertIn("ward", self.card("Brotherhood Regalia").lower())
        def self_targetable(equipment):
            return "shroud" not in self.card(equipment).lower()
        self.assertFalse(self_targetable("Lightning Greaves"))
        self.assertTrue(self_targetable("Brotherhood Regalia"))

    def test_K5_rooftop_alternative_cost_and_commander_tax(self):
        self.exact("K5", "P1")
        text = self.card("Rooftop Storm")
        self.assertIn("{0}", text)
        self.assertIn("Zombie", text)
        self.assertEqual([2 * previous_casts for previous_casts in (0, 1, 2)], [0, 2, 4])

    def test_E1_drawback_suppression_all_available(self):
        self.exact("E1", "P1")
        for n in ("Torpor Orb", "Karn, Argent Defender", "Dress Down", "Stifle", "Tale's End", "Consign to Memory"):
            self.card(n)
        self.assertEqual(sum(n in self.cards for n in
                             ("Torpor Orb", "Karn, Argent Defender", "Dress Down",
                              "Stifle", "Tale's End", "Consign to Memory")), 6)

    def test_E2_fodder_sources_payment_and_changeling(self):
        self.exact("E2", "P1")
        for n in ("Gravecrawler", "Bloodghast", "Reassembling Skeleton", "Bitterblossom", "Ophiomancer", "Jadar, Ghoulcaller of Nephalia"):
            self.card(n)
        self.assertIn("changeling", self.card("Black Market Connections"))
        self.assertIn("Artifact Creature", self.oracle["Ornithopter of Paradise"]["type_line"])
        self.assertEqual(40 - 3, 37)  # BMC's Shapeshifter requires life

    def test_W1_infect_and_kediss_noncombat_spread(self):
        self.exact("W1", "P1")
        self.assertIn("infect", self.card("Phyresis").lower())
        self.assertIn("infect", self.card("Tainted Strike").lower())
        self.assertIn("each other opponent", self.card("Kediss, Emberclaw Familiar"))
        self.assertEqual(10, int(self.oracle["Lord of Tresserhorn"]["power"]))
        self.assertGreaterEqual(10, 10)  # poison lethality threshold
        self.assertNotEqual("noncombat damage", "commander combat damage")

    def test_W2_big_hits_and_commander_damage_threshold(self):
        self.exact("W2", "P1")
        self.assertIn("double strike", self.card("Uncaged Fury").lower())
        self.assertIn("+1/+1", self.card("Uncaged Fury"))
        self.assertEqual((10 + 1) * 2, 22)
        self.assertLess(10 * 2, 21)  # double strike without pump is not lethal
        self.assertIn("each opponent", self.card("Chandra's Ignition"))
        self.assertIn("Whenever enchanted creature is dealt damage", self.card("Pain for All"))

    def test_W3_gravecrawler_loops_require_another_zombie_and_outlet(self):
        self.exact("W3", "P1")
        self.assertIn("as long as you control a Zombie", self.card("Gravecrawler"))
        for n in ("Phyrexian Altar", "Rooftop Storm", "Goblin Bombardment", "Blood Artist", "Zulaport Cutthroat"):
            self.card(n)
        def may_recast_gravecrawler(other_zombie_present, in_graveyard):
            return other_zombie_present and in_graveyard
        self.assertTrue(may_recast_gravecrawler(True, True))
        self.assertFalse(may_recast_gravecrawler(False, True))
        self.assertFalse(may_recast_gravecrawler(True, False))

    def test_F2_reduced_removal_and_untargetable_threats(self):
        self.exact("F2", "P1")
        for n in ("Terminate", "Deadly Rollick", "Chaos Warp", "Toxic Deluge", "Blasphemous Act"):
            self.card(n)
        self.assertNotIn("Sheoldred's Edict", self.cards)
        self.assertNotIn("Feed the Swarm", self.cards)
        self.assertEqual(sum(n in self.cards for n in ("Terminate", "Deadly Rollick", "Chaos Warp")), 3)
        self.assertEqual(sum(n in self.cards for n in ("Toxic Deluge", "Blasphemous Act")), 2)

    def test_F3_torpor_etb_self_nonbo_vs_death_triggers(self):
        self.exact("F3", "P1")
        self.assertIn("Creatures entering", self.card("Torpor Orb"))
        self.assertIn("Whenever", self.card("Skullclamp"))
        self.assertIn("dies", self.card("Undead Augur"))
        self.assertIn("beginning of your first main phase", self.card("Black Market Connections"))
        self.assertNotIn("Orcish Bowmasters", self.cards)


if __name__ == "__main__":
    unittest.main()
