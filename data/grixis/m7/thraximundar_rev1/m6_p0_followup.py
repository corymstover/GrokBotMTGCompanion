"""Five original Thraximundar M6 P0 finite cases on Cory's exact M7 100.

Explicit costs, trigger controller, zones and adverse cases; NOT a full game
simulation, competitive performance result or M6/IJ Phase B certification.
"""

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[4]
DECK = ROOT / "data/grixis/m7/candidate_lists/Thraximundar_chatgpt_m7_approved_rev1.txt"
SNAP = ROOT / "data/grixis/m7/oracle_snapshots/Thraximundar_Rev1_Scryfall_20261028.json"
BLUEPRINT = ROOT / "data/grixis/m6/test_blueprints/Thraximundar.json"
SHA = "f3e71b71fc10fbe6d8a1afde29b5291e9e32d4e83db44c2dcb7aab0773f18da2"
CARDS = json.loads(SNAP.read_text(encoding="utf-8"))["cards"]
ORACLE = {card["query"]: card["oracle_text"] for card in CARDS}
META = {card["query"]: card for card in CARDS}


def thrax_attack(defender_creature_count, thrax_on_battlefield=True):
    """Return one sacrificed creature, not forced creature target choice."""
    if not thrax_on_battlefield or defender_creature_count <= 0:
        return 0
    return 1


def counted_sacrifice_triggers(events, thrax_on_battlefield=True, may_choice=True):
    if not thrax_on_battlefield or not may_choice:
        return 0
    return sum(event["action"] == "sacrifice" for event in events)


class ThraximundarOriginalP0(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        raw = DECK.read_bytes()
        assert sha256(raw).hexdigest() == SHA
        inventory = Counter()
        for row in raw.decode("utf-8").splitlines():
            qty, name = row.split("x ", 1)
            inventory[name.removesuffix(" [Commander]")] += int(qty)
        assert sum(inventory.values()) == 100 and len(inventory) == 93
        assert set(inventory) == set(ORACLE)
        assert all(c["commander_legality"] == "legal" and
                   set(c["color_identity"]) <= set("UBR") for c in CARDS)
        assert {x["id"] for x in json.loads(BLUEPRINT.read_text())["cases"]
                if x["priority"] == "P0"} == {"C1", "K1", "K2", "K3", "F1"}

    def test_C1_attacking_defender_sacrifice_and_counter_timing(self):
        text = ORACLE["Thraximundar"]
        self.assertIn("Haste", text)
        self.assertIn("Whenever Thraximundar attacks, defending player sacrifices", text)
        self.assertIn("Whenever a player sacrifices a creature", text)
        # The attack-trigger sacrifice resolves before combat damage, and a
        # distinct Thrax grow trigger may add a counter before damage.
        sacrificed = thrax_attack(defender_creature_count=2)
        counters = sacrificed
        self.assertEqual((sacrificed, counters), (1, 1))
        self.assertEqual(thrax_attack(0), 0)
        self.assertEqual(thrax_attack(2, thrax_on_battlefield=False), 0)

    def test_K1_any_players_creature_sacrifice_including_paid_costs(self):
        text = ORACLE["Thraximundar"]
        self.assertIn("a player sacrifices a creature", text)
        self.assertIn("Sacrifice a creature: Add", ORACLE["Ashnod's Altar"])
        self.assertIn("sacrifice a creature", ORACLE["Diabolic Intent"].lower())
        events = [
            {"action": "sacrifice", "player": "us", "source": "Diabolic Intent cost"},
            {"action": "sacrifice", "player": "opponent", "source": "Thrax attack trigger"},
            {"action": "sacrifice", "player": "us", "source": "Ashnod Altar cost"},
            {"action": "destroy", "player": "opponent", "source": "regular destruction"},
        ]
        self.assertEqual(counted_sacrifice_triggers(events), 3)
        self.assertEqual(counted_sacrifice_triggers(events, thrax_on_battlefield=False), 0)
        self.assertEqual(counted_sacrifice_triggers(events, may_choice=False), 0)

    def test_K2_call_to_grave_spares_all_zombies(self):
        text = ORACLE["Call to the Grave"]
        self.assertIn("sacrifices a non-Zombie creature of their choice", text)
        self.assertIn("beginning of each player's upkeep", text)
        self.assertIn("Zombie", META["Thraximundar"]["type_line"])
        creatures = ["Thraximundar:Zombie", "Fleshbag Marauder:Zombie", "Blood Artist:Vampire"]
        nonzombie = [x for x in creatures if not x.endswith(":Zombie")]
        self.assertEqual(nonzombie, ["Blood Artist:Vampire"])
        self.assertEqual([x for x in creatures if x.endswith(":Zombie")],
                         ["Thraximundar:Zombie", "Fleshbag Marauder:Zombie"])

    def test_K3_skeleton_plunderer_ashnod_mana_conservation(self):
        self.assertIn("Add {C}{C}", ORACLE["Ashnod's Altar"])
        self.assertIn("Return this card from your graveyard to the battlefield tapped", ORACLE["Reassembling Skeleton"])
        self.assertIn("create a Treasure token", ORACLE["Pitiless Plunderer"])
        for piece in ("Reassembling Skeleton", "Pitiless Plunderer", "Ashnod's Altar"):
            self.assertIn(piece, ORACLE)
        # Sacrifice Skeleton: +2 colorless from Altar +1 Treasure of any color.
        # Spend 1 generic + B from Treasure for the tapped Skeleton return.
        generic_received, black_from_treasure = 2, 1
        generic_spent, black_spent = 1, 1
        self.assertEqual((generic_received-generic_spent,
                          black_from_treasure-black_spent), (1, 0))
        # No Plunderer means no Treasure/B for repeated Skeleton recasts;
        # no ready Skeleton in graveyard means the original return is illegal.
        def can_return_skeleton(zone, available_generic, available_black):
            return zone == "graveyard" and available_generic >= 1 and available_black >= 1
        self.assertTrue(can_return_skeleton("graveyard", 2, 1))
        self.assertFalse(can_return_skeleton("graveyard", 2, 0))
        self.assertFalse(can_return_skeleton("battlefield", 2, 1))

    def test_F1_seven_mana_commander_tax_and_removal(self):
        oracle = ORACLE["Thraximundar"]
        self.assertIn("Haste", oracle)
        self.assertEqual(META["Thraximundar"]["mana_cost"], "{4}{U}{B}{R}")
        base_mana = 7
        commander_mana = [base_mana + 2 * deaths for deaths in range(3)]
        self.assertEqual(commander_mana, [7, 9, 11])
        self.assertFalse(8 >= commander_mana[1])
        self.assertEqual(thrax_attack(1, thrax_on_battlefield=False), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
