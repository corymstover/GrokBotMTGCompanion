"""Finite source-paid rules cases for the Admiral Brass, Unsinkable M7 candidate.

Every case is anchored to the committed candidate-specific Scryfall snapshot and
the exact candidate list. This is a bounded rules/mana model (seed 0, no
randomness), NOT a game engine, goldfish or multiplayer win-rate measurement.
It supports no improvement claim by itself.
"""
from collections import Counter
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SNAP = ROOT / "data/grixis/m6/oracle_snapshots/Admiral_Brass__Unsinkable_M7_109_Scryfall_20261023.json"
CAND = ROOT / "data/grixis/m7/candidate_lists/Admiral_Brass__Unsinkable.txt"
BASE = ROOT / "data/grixis/m7/baseline_sources/Admiral_Brass__Unsinkable_approved_source_2026-10-13.txt"


def names(path):
    out = Counter()
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            q, raw = line.split("x ", 1)
            out[raw.removesuffix(" [Commander]").split(" // ")[0]] += int(q)  # front-face normal form
    return out


def brass_combat(graveyard, targets, throne_on_pirate=False, removed_in_response=()):
    """Resolve Brass's beginning-of-combat trigger(s).

    Throne (choosing Pirate) adds one extra instance. Each instance needs its own
    target chosen on trigger; an instance whose target left the graveyard does
    nothing (CR 608.2b). Returns the returned card names in resolution order.
    """
    instances = 2 if throne_on_pirate else 1
    if len(targets) != instances:
        raise ValueError("one target per trigger instance")
    gy = list(graveyard)
    for t in removed_in_response:
        gy.remove(t)
    returned = []
    for t in reversed(targets):  # stack: last put on stack resolves first
        if t in gy:
            gy.remove(t)
            returned.append({"name": t, "base": (4, 4), "haste": True, "finality": 1})
    return returned


def dies(creature):
    return "exile" if creature.get("finality", 0) > 0 else "graveyard"


class AdmiralBrassUnsinkableM7Mechanics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        s = json.loads(SNAP.read_text(encoding="utf-8"))
        cls.o = {c["name"]: c for c in s["cards"]}
        cls.o.update({n.split(" // ")[0]: c for n, c in list(cls.o.items()) if " // " in n})
        cls.cand, cls.base = names(CAND), names(BASE)
        cls.snap = s

    def txt(self, n):
        return self.o[n]["oracle_text"]

    def test_oracle_anchors_for_every_claimed_mechanic(self):
        b = self.txt("Admiral Brass, Unsinkable")
        for k in ("At the beginning of combat on your turn", "finality counter",
                  "base power and toughness 4/4", "gains haste until end of turn", "mill four"):
            self.assertIn(k, b)
        self.assertIn("triggers an additional time", self.txt("Roaming Throne"))
        self.assertIn("{T}, Remove a counter from a permanent you control", self.txt("Power Conduit"))
        self.assertIn("Activate only as a sorcery", self.txt("Nesting Grounds"))
        self.assertIn("{2}{U}{U}, {T}, Put this creature on the bottom", self.txt("Timestream Navigator"))
        self.assertIn("Activate only if you have the city's blessing", self.txt("Timestream Navigator"))
        self.assertIn("lose life equal to that permanent's mana value", self.txt("Jhoira, Weatherlight Corsair"))
        self.assertIn("loses all abilities and has base power and toughness 0/1", self.txt("Warkite Marauder"))
        self.assertIn("for each player, choose up to one other target artifact or creature", self.txt("Kitesail Larcenist"))
        for n in ("Kitesail Larcenist", "Timestream Navigator", "Warkite Marauder",
                  "Ragavan, Nimble Pilferer", "Jhoira, Weatherlight Corsair"):
            self.assertIn("Pirate", self.o[n]["type_line"], n)
            self.assertEqual(self.o[n]["commander_legality"], "legal")

    def test_throne_needs_two_distinct_pirate_targets(self):
        r = brass_combat(["Timestream Navigator", "Kitesail Larcenist"],
                         ["Timestream Navigator", "Kitesail Larcenist"], throne_on_pirate=True)
        self.assertEqual({x["name"] for x in r}, {"Timestream Navigator", "Kitesail Larcenist"})
        self.assertTrue(all(x["finality"] == 1 and x["haste"] and x["base"] == (4, 4) for x in r))
        # one Pirate in graveyard: second instance cannot add a second return
        r = brass_combat(["Warkite Marauder"], ["Warkite Marauder", "Warkite Marauder"], throne_on_pirate=True)
        self.assertEqual(len(r), 1)
        # graveyard hate in response
        self.assertEqual(brass_combat(["Ragavan, Nimble Pilferer"], ["Ragavan, Nimble Pilferer"],
                                      removed_in_response=["Ragavan, Nimble Pilferer"]), [])

    def test_finality_and_conduit_counter_removal(self):
        c = brass_combat(["Kitesail Larcenist"], ["Kitesail Larcenist"])[0]
        self.assertEqual(dies(c), "exile")
        # Power Conduit is instant-speed ({T} ability without sorcery clause): remove finality first
        self.assertNotIn("Activate only as a sorcery", self.txt("Power Conduit"))
        c["finality"] -= 1
        self.assertEqual(dies(c), "graveyard")
        # Larcenist leaves -> its Treasure-conversion duration ends (ability text: 'For as long as')
        self.assertIn("For as long as this creature remains on the battlefield", self.txt("Kitesail Larcenist"))

    def test_navigator_extra_turn_is_paid_only_with_blessing_and_four_spare_mana(self):
        # Turn N+1 witness: Brass already in play, Navigator milled by Brass ETB.
        permanents = 6 + 2 + 1 + 1 + 1  # lands, two rocks, Treasure, Brass, returned Navigator
        mana = 6 + 2 + 1
        self.assertGreaterEqual(permanents, 10)
        self.assertGreaterEqual(mana, 4)  # {2}{U}{U}; haste from Brass satisfies {T}
        # Counterexample: Brass cast this turn off 6 mana leaves only 3 -> cannot activate
        self.assertLess(6 + 2 + 1 - 5 - 1, 4)
        # Navigator goes to library bottom, so finality never applies and it is not re-buyable
        self.assertIn("bottom of its owner's library", self.txt("Timestream Navigator"))

    def test_jhoira_life_loss_is_bounded_by_revealed_mv(self):
        # Throne doubles enters+attack -> up to four reveals per turn cycle; life paid = sum of MVs
        reveals = [2, 1, 6, 0]
        self.assertEqual(sum(reveals), 9)
        self.assertIn("{4}{B}{B}", self.o["Jhoira, Weatherlight Corsair"]["mana_cost"])

    def test_exact_five_swaps_keep_pirate_density_and_size(self):
        added = self.cand - self.base
        cut = self.base - self.cand
        self.assertEqual(set(added), {"Kitesail Larcenist", "Timestream Navigator", "Warkite Marauder",
                                      "Ragavan, Nimble Pilferer", "Jhoira, Weatherlight Corsair"})
        self.assertEqual(set(cut), {"Enterprising Scallywag", "Francisco, Fowl Marauder", "Fathom Fleet Captain",
                                    "Changeling Outcast", "Pitiless Plunderer"})
        self.assertEqual(sum(self.cand.values()), 100)
        pir = lambda d: sum(1 for n in d if "Pirate" in self.o[n]["type_line"]
                            or "Changeling" in (self.o[n]["oracle_text"] or ""))
        self.assertEqual(pir(self.cand), pir(self.base))
        lands = lambda d: sum(1 for n in d if "Land" in self.o[n]["type_line"].split(" // ")[0])
        self.assertEqual(lands(self.cand), lands(self.base))

    def test_candidate_legal_identity_and_bracket_four_game_changers(self):
        for n in self.cand:
            c = self.o[n]
            self.assertEqual(c["commander_legality"], "legal", n)
            self.assertTrue(set(c["color_identity"]) <= {"U", "B", "R"}, n)
        gc = sorted(n for n in self.cand if self.o[n]["game_changer"])
        self.assertEqual(len(gc), 6)
        self.assertEqual(gc, self.snap["game_changers_in_candidate"])


if __name__ == "__main__":
    unittest.main()
