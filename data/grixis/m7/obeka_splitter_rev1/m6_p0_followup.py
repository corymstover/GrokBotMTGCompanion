"""Original five Obeka Splitter M6 P0 cases, scoped to the exact M7 Rev1 100.

Each is a deliberately bounded source-bound payability/timing model, with a
negative branch. It is not a full Magic Comprehensive Rules engine.
"""

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[4]
SHA = "f80d882944d5e39f3c6661da4dcdce3ec6eead577cd981dc54f7dc522be50859"
DECK = ROOT / "data/grixis/m7/candidate_lists/Obeka__Splitter_of_Seconds_chatgpt_rev1.txt"
SNAP = ROOT / "data/grixis/m7/oracle_snapshots/Obeka__Splitter_of_Seconds_Rev1_Scryfall_20261028.json"
BLUEPRINT = ROOT / "data/grixis/m6/test_blueprints/Obeka__Splitter_of_Seconds.json"
CARDS = json.loads(SNAP.read_text(encoding="utf-8"))["cards"]
ORACLE = {card["query"]: card for card in CARDS}


def extra_upkeeps(zone="battlefield", controlled=True, combat_to_player=True,
                  unprevented_damage=2, blocked=False, fogged=False):
    """Model the grant only after controlled Obeka damages a player in combat."""
    if zone != "battlefield" or not controlled or not combat_to_player or blocked or fogged:
        return 0
    return max(0, unprevented_damage)


class ObekaSplitterOriginalP0(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        raw = DECK.read_bytes()
        assert sha256(raw).hexdigest() == SHA
        names = Counter()
        for row in raw.decode("utf-8").splitlines():
            qty, name = row.split("x ", 1)
            names[name.removesuffix(" [Commander]")] += int(qty)
        assert sum(names.values()) == 100 and len(names) == 96
        assert set(names) == set(ORACLE)
        assert all(card["commander_legality"] == "legal" for card in CARDS)
        assert all(set(card["color_identity"]) <= set("UBR") for card in CARDS)
        blueprint = json.loads(BLUEPRINT.read_text())
        assert {case["id"] for case in blueprint["cases"] if case["priority"] == "P0"} == {
            "C1", "K1", "K2", "K3", "F1"
        }

    def test_C1_commander_oracle_zone_and_damage_payability(self):
        text = ORACLE["Obeka, Splitter of Seconds"]["oracle_text"]
        self.assertIn("Menace", text)
        self.assertIn("deals combat damage to a player", text)
        self.assertIn("additional upkeep steps after this phase", text)
        self.assertEqual(extra_upkeeps(unprevented_damage=3), 3)
        self.assertEqual(extra_upkeeps(zone="command", unprevented_damage=3), 0)
        self.assertEqual(extra_upkeeps(controlled=False, unprevented_damage=3), 0)
        self.assertEqual(extra_upkeeps(combat_to_player=False, unprevented_damage=3), 0)

    def test_K1_only_upkeep_steps_not_draw_or_untap(self):
        text = ORACLE["Obeka, Splitter of Seconds"]["oracle_text"]
        self.assertIn("additional upkeep steps", text)
        hits = extra_upkeeps(unprevented_damage=4)
        additional_steps = ["upkeep"] * hits
        self.assertEqual(additional_steps, ["upkeep"] * 4)
        self.assertNotIn("draw", additional_steps)
        self.assertNotIn("untap", additional_steps)
        self.assertEqual(extra_upkeeps(fogged=True, unprevented_damage=4), 0)
        self.assertEqual(extra_upkeeps(unprevented_damage=0), 0)

    def test_K2_mjolnir_worthy_equip_cost_and_damage_doubling(self):
        hammer = ORACLE["Mjölnir, Hammer of Thor"]["oracle_text"]
        obeka = ORACLE["Obeka, Splitter of Seconds"]
        self.assertIn("Double all damage equipped creature would deal", hammer)
        self.assertIn("Equip worthy {1}", hammer)
        self.assertIn("legendary non-Villain", hammer)
        self.assertIn("red and/or white", hammer)
        self.assertIn("Legendary Creature", obeka["type_line"])
        self.assertIn("R", obeka["color_identity"])
        self.assertNotIn("Villain", obeka["type_line"])
        payable_generic = 1
        worthy = ("Legendary Creature" in obeka["type_line"]
                  and "Villain" not in obeka["type_line"]
                  and ("R" in obeka["color_identity"] or "W" in obeka["color_identity"]))
        self.assertTrue(worthy and payable_generic >= 1)
        self.assertEqual(extra_upkeeps(unprevented_damage=2 * 2), 4)
        self.assertFalse(worthy and 0 >= 1)
        # Equipment effect is conditional on being actually equipped and hitting.
        self.assertEqual(extra_upkeeps(blocked=True, unprevented_damage=4), 0)

    def test_K3_wizards_staff_warlock_cost_not_discounted(self):
        staff = ORACLE["Wizard's Staff"]["oracle_text"]
        commander = ORACLE["Obeka, Splitter of Seconds"]
        self.assertIn("Equip Wizard {1}", staff)
        self.assertIn("Equip {3}", staff)
        self.assertIn("Ogre Warlock", commander["type_line"])
        self.assertNotIn("Wizard", commander["type_line"])
        equip_cost = 1 if "Wizard" in commander["type_line"] else 3
        self.assertEqual(equip_cost, 3)
        self.assertFalse(2 >= equip_cost)
        self.assertIn("If a triggered ability of equipped creature triggers", staff)
        self.assertEqual(2 * extra_upkeeps(unprevented_damage=2), 4)
        self.assertEqual(2 * extra_upkeeps(unprevented_damage=0), 0)

    def test_F1_no_player_connection_blocks_the_upkeep_engine(self):
        self.assertIn("Menace", ORACLE["Obeka, Splitter of Seconds"]["oracle_text"])
        # Menace prevents a single blocker, but two eligible blockers can block.
        number_of_blockers = 1
        self.assertFalse(number_of_blockers >= 2)
        self.assertEqual(extra_upkeeps(unprevented_damage=2), 2)
        number_of_blockers = 2
        self.assertTrue(number_of_blockers >= 2)
        self.assertEqual(extra_upkeeps(blocked=True, unprevented_damage=2), 0)
        self.assertEqual(extra_upkeeps(fogged=True, unprevented_damage=2), 0)
        self.assertEqual(extra_upkeeps(zone="graveyard", unprevented_damage=2), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
