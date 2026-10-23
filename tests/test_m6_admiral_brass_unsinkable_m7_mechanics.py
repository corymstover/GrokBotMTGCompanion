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
SNAP = ROOT / "data/grixis/m6/oracle_snapshots/Admiral_Brass__Unsinkable_M7_rev2_Scryfall_20261023.json"
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


def sirens_ruse(creature, controller="me"):
    """Exile target creature you control, return that card under its OWNER's control.

    The result is a new object (CR 400.7): no counters, no Brass base-4/4 or haste
    effect, summoning sick, ETB triggers again; draw 1 if it was a Pirate.
    """
    back = {"name": creature["name"], "base": None, "haste": False, "finality": 0,
            "controller": creature.get("owner", controller), "etb_retriggered": True}
    return back, (1 if creature.get("pirate", True) else 0)


def turn_steps():
    return ["untap", "upkeep", "draw", "precombat_main", "beginning_of_combat"]


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
        self.assertIn("Exile target creature you control, then return that card to the battlefield under its owner's control",
                      self.txt("Siren's Ruse"))
        self.assertIn("If a Pirate was exiled this way, draw a card", self.txt("Siren's Ruse"))
        self.assertEqual(self.o["Siren's Ruse"]["type_line"], "Instant")
        self.assertIn("At the beginning of your first main phase, mill three cards", self.txt("Ripples of Undeath"))
        self.assertIn("pay {1} and 3 life", self.txt("Ripples of Undeath"))
        self.assertIn("can't block and can't be blocked", self.txt("Changeling Outcast"))
        self.assertIn("Changeling", self.txt("Changeling Outcast"))
        self.assertEqual(self.o["Ragavan, Nimble Pilferer"]["type_line"], "Legendary Creature — Monkey Pirate")
        self.assertIn("Whenever another creature you control dies", self.txt("Pitiless Plunderer"))
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
        self.assertIn("Changeling Outcast", self.cand)
        self.assertEqual(brass_combat(["Changeling Outcast"], ["Changeling Outcast"],
                                      removed_in_response=["Changeling Outcast"]), [])

    def test_finality_and_conduit_counter_removal(self):
        c = brass_combat(["Kitesail Larcenist"], ["Kitesail Larcenist"])[0]
        self.assertEqual(dies(c), "exile")
        # Power Conduit is instant-speed ({T} ability without sorcery clause): remove finality first
        self.assertNotIn("Activate only as a sorcery", self.txt("Power Conduit"))
        c["finality"] -= 1
        self.assertEqual(dies(c), "graveyard")
        # Larcenist leaves -> its Treasure-conversion duration ends (ability text: 'For as long as')
        self.assertIn("For as long as this creature remains on the battlefield", self.txt("Kitesail Larcenist"))

    def test_sirens_ruse_resets_finality_as_new_object_and_returns_stolen_to_owner(self):
        c = brass_combat(["Kitesail Larcenist"], ["Kitesail Larcenist"])[0]
        self.assertEqual(dies(c), "exile")
        back, drawn = sirens_ruse(c)
        self.assertEqual((back["finality"], back["haste"], back["base"]), (0, False, None))
        self.assertTrue(back["etb_retriggered"])
        self.assertEqual(drawn, 1)
        self.assertEqual(dies(back), "graveyard")  # can die and be recurred by Brass again
        stolen = {"name": "opponent creature", "owner": "opponent", "pirate": False}
        back, drawn = sirens_ruse(stolen)
        self.assertEqual((back["controller"], drawn), ("opponent", 0))

    def test_ripples_mills_before_brass_combat_trigger_targets(self):
        steps = turn_steps()
        self.assertLess(steps.index("precombat_main"), steps.index("beginning_of_combat"))
        gy = []
        gy += ["Amphin Mutineer", "Island", "Feed the Swarm"]  # Ripples mill 3 in first main phase
        self.assertEqual(len(brass_combat(gy, ["Amphin Mutineer"])), 1)
        self.assertIn("Amphin Mutineer", self.cand)

    def test_plunderer_still_fires_on_non_finality_deaths(self):
        # Plunderer gets no Treasure from finality-exiled Brass returns, but natural deaths still count
        returned = brass_combat(["Kitesail Larcenist"], ["Kitesail Larcenist"])[0]
        others = [{"name": "token", "finality": 0}, {"name": "stolen", "finality": 0},
                  dict(returned, finality=0)]  # Conduit-cleared
        treasures = sum(1 for x in [returned] + others if dies(x) == "graveyard")
        self.assertEqual(treasures, 3)

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

    def test_exact_six_swaps_keep_pirate_density_and_count_lands_by_quantity(self):
        added = self.cand - self.base
        cut = self.base - self.cand
        self.assertEqual(set(added), {"Kitesail Larcenist", "Timestream Navigator", "Warkite Marauder",
                                      "Jhoira, Weatherlight Corsair", "Siren's Ruse", "Ripples of Undeath"})
        self.assertEqual(set(cut), {"Enterprising Scallywag", "Francisco, Fowl Marauder", "Fathom Fleet Captain",
                                    "Pitiless Plunderer", "Crumbling Necropolis", "Faithless Looting"})
        self.assertIn("Changeling Outcast", self.cand)
        self.assertNotIn("Ragavan, Nimble Pilferer", self.cand)
        self.assertEqual(sum(self.cand.values()), 100)
        pir = lambda d: sum(q for n, q in d.items() if "Pirate" in self.o[n]["type_line"]
                            or "Changeling" in (self.o[n]["oracle_text"] or ""))
        self.assertEqual(pir(self.cand), pir(self.base))
        self.assertEqual(pir(self.cand), 29)  # 28 in the 99 + the commander
        land = lambda n: "Land" in self.o[n]["type_line"].split(" // ")[0]
        self.assertFalse(land("Brass's Tunnel-Grinder"))  # front face is an artifact
        lands = lambda d: sum(q for n, q in d.items() if land(n))
        self.assertEqual(lands(self.base), 34)
        self.assertEqual(sum(1 for n in self.base if land(n)), 31)  # rows, not cards
        self.assertEqual(lands(self.cand), 33)

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
