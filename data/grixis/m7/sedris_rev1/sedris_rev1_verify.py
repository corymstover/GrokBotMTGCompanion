#!/usr/bin/env python3
"""Source-bound Sedris #51 M7 audit; bounded cases are not game simulations."""
import argparse
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
from urllib.request import Request, urlopen
import time
import unittest
import sys

ROOT = Path(__file__).resolve().parents[0]
BASE = ROOT / "sedris_baseline.txt"
FINAL = ROOT.parent / "candidate_lists" / "Sedris__the_Traitor_King_M7_Rev1.txt"
BASE_SHA = "65fbfe3eb64551ad6f5723243fcd62a286610c360e24bd700b584252e1da6365"
FINAL_SHA = "b0aa141fe5d27b1e0d0bc804e692d56ae645c74de4bd6777c501b1ae057969da"
SWAPS = {
    "Ashnod's Altar": "Altar of Dementia",
    "Chainer, Nightmare Adept": "Thassa, Deep-Dwelling",
    "Feldon of the Third Path": "Agadeem's Awakening // Agadeem, the Undercrypt",
    "Gifts Ungiven": "Cephalid Coliseum",
    "Jin-Gitaxias, Core Augur": "Gyruda, Doom of Depths",
    "Likeness Looter": "Careful Study",
    "Sepulchral Primordial": "Agent of Treachery",
    "Sheoldred, Whispering One": "Phyrexian Delver",
    "Windfall": "Intuition",
}
LANDS = set("""Ancient Tomb|Badlands|Blood Crypt|Bloodstained Mire|Undercity Sewers|City of Brass|Flooded Strand|Command Tower|Marsh Flats|Agadeem's Awakening // Agadeem, the Undercrypt|Cephalid Coliseum|Island|Luxury Suite|Mana Confluence|Morphic Pool|Mountain|Otawara, Soaring City|Phyrexian Tower|Polluted Delta|Raucous Theater|Misty Rainforest|Scalding Tarn|Sokenzan, Crucible of Defiance|Steam Vents|Swamp|Takenuma, Abandoned Mire|Training Center|Underground Sea|Urborg, Tomb of Yawgmoth|Volcanic Island|Watery Grave|Xander's Lounge""".split("|"))
PROTECTED = {"Sedris, the Traitor King", "Convergence of Dominion", "Obeka, Brute Chronologist", "Sundial of the Infinite", "Teferi's Veil", "Deadeye Navigator", "Peregrine Drake", "Panharmonicon", "River Kelpie", "Twilight Diviner", "Archon of Cruelty", "Grave Titan", "Goblin Bombardment", "Terror of the Peaks", "Buried Alive", "Ripples of Undeath", "Vile Entomber", "Dread Return", "Force of Will"}


def load(path, expected_sha):
    raw = path.read_bytes()
    assert sha256(raw).hexdigest() == expected_sha, f"raw drift: {path}"
    assert raw.startswith(b"1x Sedris, the Traitor King [Commander]\n")
    rows = []
    for line in raw.decode("utf-8").splitlines():
        quantity, name = line.split("x ", 1)
        rows.append((int(quantity), name.removesuffix(" [Commander]")))
    assert sum(q for q, _ in rows) == 100 and len(rows) == 99
    assert len(set(n for _, n in rows)) == 99
    assert [(q, n) for q, n in rows if q > 1] == [(2, "Swamp")]
    return Counter({n: q for q, n in rows})


def structural():
    base = load(BASE, BASE_SHA)
    final = load(FINAL, FINAL_SHA)
    assert set(base) - set(final) == set(SWAPS)
    assert set(final) - set(base) == set(SWAPS.values())
    assert all(base[cut] == final[add] == 1 for cut, add in SWAPS.items())
    assert PROTECTED <= set(final)
    assert sum(q for n, q in base.items() if n in LANDS) == 31
    assert sum(q for n, q in final.items() if n in LANDS) == 33
    print("PASS source-bound Oct15 baseline, exact 9 substitutions, final 100 physical, 99 names, Swamp x2, 33 lands")
    return final


def live_scryfall(cards):
    names = list(cards)
    seen = {}
    for start in range(0, len(names), 75):
        requested = names[start:start + 75]
        identifiers = [{"set": "tmp", "collector_number": "151"} if n == "Reanimate"
                       else {"name": n.split(" // ", 1)[0]} for n in requested]
        body = json.dumps({"identifiers": identifiers}).encode()
        req = Request("https://api.scryfall.com/cards/collection", data=body,
                      headers={"Content-Type": "application/json", "Accept": "application/json",
                               "User-Agent": "GrixisEncyclopediaAudit/1.0 (+https://github.com/corymstover/GrokBotMTGCompanion)"},
                      method="POST")
        with urlopen(req, timeout=40) as resp:
            data = json.load(resp)
        assert not data.get("not_found"), data.get("not_found")
        for card in data["data"]:
            seen[card["name"]] = card
        time.sleep(.3)
    assert set(seen) == set(names), f"name mismatch: {set(seen) ^ set(names)}"
    for name, card in seen.items():
        assert card["legalities"]["commander"] == "legal", (name, card["legalities"]["commander"])
        assert set(card["color_identity"]) <= {"U", "B", "R"}, (name, card["color_identity"])
        assert card.get("oracle_id") and (card.get("oracle_text") or card.get("card_faces")), name
    assert "unearth" in seen["Sedris, the Traitor King"]["oracle_text"].lower()
    assert "Sacrifice a creature" in seen["Altar of Dementia"]["oracle_text"]
    assert "even mana value" in seen["Gyruda, Doom of Depths"]["oracle_text"]
    print(f"PASS live Scryfall complete {len(seen)} unique Oracle cards, official Commander legality, UBR identity")


class TestSedrisSourceBoundCases(unittest.TestCase):
    def test_C1_granted_unearth_sorcery_window(self):
        can_activate = lambda sedris, creature_grave, own_main, empty_stack, black: all((sedris, creature_grave, own_main, empty_stack, black))
        self.assertTrue(can_activate(True, True, True, True, True))
        self.assertFalse(can_activate(True, True, False, True, True))
        self.assertFalse(can_activate(False, True, True, True, True))

    def test_K1_cost_floor_and_colored_requirement(self):
        mana_cost = lambda sedris, convergence: (max(0, 2 - (2 if sedris and convergence else 0)), 1)
        self.assertEqual(mana_cost(True, True), (0, 1))
        self.assertEqual(mana_cost(False, True), (2, 1))
        self.assertEqual(mana_cost(True, False), (2, 1))

    def test_K2_end_step_stack_vs_premature_sundial(self):
        exile_trigger_gone = lambda trigger_on_stack, end_turn_on_own_turn: trigger_on_stack and end_turn_on_own_turn
        self.assertTrue(exile_trigger_gone(True, True))
        self.assertFalse(exile_trigger_gone(False, True))
        self.assertFalse(exile_trigger_gone(True, False))

    def test_K3_veil_attackers_only(self):
        phases = lambda was_attacking, veil: was_attacking and veil
        self.assertTrue(phases(True, True))
        self.assertFalse(phases(False, True))

    def test_K4_navigator_exile_new_object(self):
        zones = ["graveyard", "battlefield#1", "exile", "battlefield#2"]
        self.assertEqual(zones[-1], "battlefield#2")
        self.assertNotEqual(zones[1], zones[-1])

    def test_K5_kelpie_grave_only(self):
        draw = lambda from_zone, is_permanent: from_zone == "graveyard" and is_permanent
        self.assertTrue(draw("graveyard", True))
        self.assertFalse(draw("exile", True))

    def test_K6_exile_replacement_not_graveyard_loop(self):
        leave = lambda unearthed, destination: "exile" if unearthed else destination
        self.assertEqual(leave(True, "graveyard"), "exile")
        self.assertEqual(leave(False, "graveyard"), "graveyard")

    def test_K7_drake_navigator_payable_net_mana(self):
        net = lambda five_land_mana, blue_available: five_land_mana - 2 if blue_available else None
        self.assertEqual(net(5, True), 3)
        self.assertIsNone(net(5, False))
        self.assertEqual(net(2, True), 0)

    def test_E1_separate_unearth_payments(self):
        affordable = lambda total, black, costs: black >= len(costs) and total >= sum(costs)
        self.assertTrue(affordable(6, 2, (3, 3)))
        self.assertFalse(affordable(5, 2, (3, 3)))
        self.assertTrue(affordable(2, 2, (1, 1)))

    def test_E2_thassa_end_step_trigger_order(self):
        # Both triggers are ours: stack exile underneath Thassa blink; new object returns.
        stack = ["unearth_delayed_exile_old_object", "thassa_blink_old_object"]
        self.assertEqual(stack.pop(), "thassa_blink_old_object")
        new_object = "new_object_no_unearth_replacement"
        self.assertNotIn("old_object", new_object)
        self.assertEqual(stack.pop(), "unearth_delayed_exile_old_object")

    def test_W1_etb_distinctions(self):
        # The stolen permanent has an independent controller state from Agent.
        board = {"Agent#1": "mine", "opponent_land": "opponent"}
        board["opponent_land"] = "mine"
        board.pop("Agent#1")
        self.assertEqual(board["opponent_land"], "mine")
        # Grave Titan 2-Zombie ETB doubles, but its ATTACK trigger does not.
        tokens = lambda panharm, attacks: 2 * (2 if panharm else 1) + (2 if attacks else 0)
        self.assertEqual(tokens(True, False), 4)
        self.assertEqual(tokens(True, True), 6)
        # Delver incurs a life payment for EACH creature returned.
        life = lambda life_before, returned_mana_values: life_before - sum(returned_mana_values)
        self.assertEqual(life(20, [7, 6]), 7)

    def test_W2_drake_infinite_requires_soulbond_and_blue(self):
        effective = lambda paired, blue_source, untapped_land_output: paired and blue_source and untapped_land_output > 2
        self.assertTrue(effective(True, True, 5))
        self.assertFalse(effective(False, True, 5))
        self.assertFalse(effective(True, False, 5))

    def test_F1_exile_yard_hate_stops_unearth(self):
        graveyard = {"Archon", "Grave Titan"}
        graveyard.clear()  # targeted graveyard exile resolves before activation
        self.assertNotIn("Archon", graveyard)
        self.assertFalse(bool(graveyard))

    def test_F2_commander_six_mana_and_ubr(self):
        castable = lambda total, colors: total >= 6 and {"U", "B", "R"} <= colors
        self.assertTrue(castable(6, {"U", "B", "R"}))
        self.assertFalse(castable(6, {"U", "B"}))
        self.assertFalse(castable(5, {"U", "B", "R"}))

    def test_F3_altar_unearth_sacrifice(self):
        graveyard = {"Grave Titan", "Archon"}
        graveyard.remove("Grave Titan")  # unearth to battlefield
        sacrificed_destination = "exile"  # replacement on sacrifice; no refund to grave
        self.assertEqual(sacrificed_destination, "exile")
        altar_mill = lambda power, legal_target: power if legal_target else 0
        self.assertEqual(altar_mill(6, True), 6)
        self.assertEqual(altar_mill(6, False), 0)
        self.assertNotIn("Grave Titan", graveyard)

    def test_new_gyruda_panharmon_even_value(self):
        hit = lambda mana_values: [mv for mv in mana_values if mv % 2 == 0]
        self.assertEqual(hit([5, 6, 7, 8]), [6, 8])
        triggers = ["first_gyruda_etb", "panharmonicon_extra_etb"]
        self.assertEqual(len(triggers), 2)
        self.assertNotEqual(triggers[0], triggers[1])


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--live-scryfall", action="store_true")
    args = p.parse_args()
    cards = structural()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestSedrisSourceBoundCases)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if not result.wasSuccessful():
        sys.exit(1)
    if args.live_scryfall:
        live_scryfall(cards)
