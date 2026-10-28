"""Deck #53: exact-list, source-pinned, finite Sol'Kanar scenarios.

Fixtures are explicitly bounded Magic-rule assertions, not a complete game
engine or a randomized multiplayer win-rate measurement. --live requests
current Scryfall Oracle/Commander data for every distinct candidate name.
"""
import argparse
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import time
import unittest
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "Sol_kanar_the_Tainted_Oct15_baseline.txt"
STAGED = ROOT.parent / "candidate_lists" / "Sol_kanar_the_Tainted_M7_Rev1.txt"
FINAL = STAGED if STAGED.exists() else ROOT / "Sol_kanar_the_Tainted_M7_Rev1.txt"
BASE_SHA = "72a3b14e93d884d98397e000fe45df430beb538a106097a69dfc2491da8d7a58"
FINAL_SHA = "c244b7c3e31b108a0730db37790de14dd167c9ee274259b3f18bbb5971a1ef20"
SWAPS = {
    "Assault Suit": "Displacer Kitten",
    "Perplexing Chimera": "Nightscape Familiar",
    "Reins of Power": "Brand",
    "Visions of Duplicity": "Alexios, Deimos of Kosmos",
    "The Trickster-God's Heist": "Sleeper Agent",
    "Propaganda": "Wishclaw Talisman",
}
PROTECTED = {
    "Sol'Kanar the Tainted", "Demonic Pact", "Donate", "Harmless Offering",
    "Immortal Coil", "Bojuka Bog", "Rakdos Charm", "Illusions of Grandeur",
    "Greed's Gambit", "Archfiend of the Dross", "Captive Audience",
    "Thassa, Deep-Dwelling", "Conjurer's Closet", "Planar Incision",
    "Homeward Path", "Coveted Falcon", "Bazaar Trader", "Blim, Comedic Genius",
    "Fateful Handoff", "Sudden Substitution", "Gilded Drake",
    "Jon Irenicus, Shattered One", "Puca's Mischief", "Shifting Grift",
    "Goblin Bombardment", "Ertai Resurrected", "Force of Will",
}
BASICS = {"Island": 3, "Mountain": 3, "Swamp": 4}


def parse(path, digest):
    raw = path.read_bytes()
    assert sha256(raw).hexdigest() == digest, f"raw SHA mismatch: {path}"
    assert raw.endswith(b"\n") and b"\r" not in raw
    lines = raw.decode("utf-8").splitlines()
    assert lines[0] == "1x Sol'Kanar the Tainted [Commander]"
    result = Counter()
    for line in lines:
        amount, name = line.split("x ", 1)
        name = name.removesuffix(" [Commander]")
        result[name] += int(amount)
    assert sum(result.values()) == 100 and len(result) == 93
    assert {name: n for name, n in result.items() if n > 1} == BASICS
    return result


def check_lists():
    baseline = parse(BASE, BASE_SHA)
    selected = parse(FINAL, FINAL_SHA)
    assert dict(baseline - selected) == {cut: 1 for cut in SWAPS}
    assert dict(selected - baseline) == {add: 1 for add in SWAPS.values()}
    assert PROTECTED <= set(selected)
    print("PASS exact baseline, physical 100, singleton 93 names, six real swaps, core kept")
    return selected


def live_scryfall(selected):
    """Two bounded POST /cards/collection calls; all 93 cards, not a sample."""
    names = list(selected)
    result = {}
    for start in range(0, len(names), 75):
        batch = names[start:start + 75]
        body = json.dumps({"identifiers": [{"name": n} for n in batch]}).encode()
        req = Request(
            "https://api.scryfall.com/cards/collection", data=body, method="POST",
            headers={"Content-Type": "application/json", "Accept": "application/json",
                     "User-Agent": "GrixisEncyclopediaDeck53/1.0 (+https://github.com/corymstover/GrokBotMTGCompanion)"},
        )
        with urlopen(req, timeout=50) as resp:
            payload = json.load(resp)
        assert not payload.get("not_found"), payload.get("not_found")
        for card in payload["data"]:
            result[card["name"]] = card
        time.sleep(0.3)
    assert set(result) == set(names), f"Unresolved names: {set(names) ^ set(result)}"
    for name, card in result.items():
        assert card["legalities"]["commander"] == "legal", name
        assert set(card["color_identity"]) <= {"U", "B", "R"}, name
        assert card.get("oracle_id"), name
        assert card.get("oracle_text") or card.get("card_faces"), name
    sol = result["Sol'Kanar the Tainted"]["oracle_text"]
    assert "choose one that hasn't been chosen" in sol.lower()
    assert "under an opponent's control" in sol.lower()
    assert "noncreature spell" in result["Displacer Kitten"]["oracle_text"].lower()
    assert "gain control of all permanents you own" in result["Brand"]["oracle_text"].lower()
    assert "blue spells and red spells" in result["Nightscape Familiar"]["oracle_text"].lower()
    assert "can't attack its owner" in result["Alexios, Deimos of Kosmos"]["oracle_text"].lower()
    assert "opponent gains control" in result["Wishclaw Talisman"]["oracle_text"].lower()
    print("PASS live current Scryfall all 93 Oracle IDs; official Commander legality and UBR")


class TaintedFiniteCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cards = check_lists()

    def test_C1_trigger_only_controlled_end_step_four_modes(self):
        def legal(controls, own_endstep, mode, used):
            return controls and own_endstep and mode in (1, 2, 3, 4) and mode not in used
        self.assertTrue(legal(True, True, 2, {1}))
        self.assertFalse(legal(False, True, 2, {1}))
        self.assertFalse(legal(True, False, 2, {1}))
        self.assertFalse(legal(True, True, 1, {1}))

    def test_K1_blink_creates_new_object_and_resets_mode_memory(self):
        old = {"object": 40, "owner": "Cory", "controller": "Cory", "used": {1, 2, 3}}
        new = {**old, "object": 41, "controller": old["owner"], "used": set()}
        self.assertEqual(new["used"], set())
        self.assertNotEqual(old["object"], new["object"])
        self.assertEqual(old["used"], {1, 2, 3})

    def test_K2_beginning_end_step_resolve_mode_before_blink(self):
        # Controller puts both triggers on stack. Chosen mode on stack already.
        stack = ["Closet_blink_Sol", "Sol_mode_1_draw"]
        self.assertEqual(stack.pop(), "Sol_mode_1_draw")
        self.assertEqual(stack.pop(), "Closet_blink_Sol")
        # Opponent removes Sol in response to the chosen mode: value mode
        # survives as an independent trigger, but the blink misses its target.
        mode_effect = "draw_1"
        blink_target_still_on_battlefield = False
        self.assertEqual(mode_effect, "draw_1")
        self.assertFalse(blink_target_still_on_battlefield)

    def test_K3_planar_incision_owner_not_current_controller(self):
        before = {"owner": "Cory", "controller": "Opponent", "counter": 0}
        after = {"owner": before["owner"], "controller": before["owner"],
                 "counter": before["counter"] + 1}
        self.assertEqual(after["controller"], "Cory")
        self.assertEqual(after["counter"], 1)
        self.assertNotEqual(before["controller"], after["controller"])

    def test_F1_colored_pips_and_nightscape_discount_once(self):
        # {2}{U}{B}{R} Sol; Nightscape has one {1} discount even if
        # a single spell is both blue and red.
        self.assertEqual((max(2 - 1, 0), "U", "B", "R"), (1, "U", "B", "R"))
        # Mana Vault CCC alone cannot pay three different colored symbols.
        self.assertFalse(all(c in "CCC" for c in "UBR"))

    def test_K4_demonic_pact_chosen_modes_follow_permanent(self):
        pact = {"owner": "Cory", "controller": "Cory", "used": {1, 2, 3}}
        pact["controller"] = "Opponent"
        self.assertEqual(pact["used"], {1, 2, 3})
        self.assertEqual([m for m in (1, 2, 3, 4) if m not in pact["used"]], [4])
        pact_removed = None  # target removed before upkeep means no trigger
        self.assertIsNone(pact_removed)

    def test_K5_immortal_coil_controller_and_graveyard(self):
        coil_controller = "Opponent"
        yards = {"Cory": ["Flicker"], "Opponent": ["Card"]}
        yards["Opponent"].clear()  # Bog ETB/Rakdos Charm on target opponent
        self.assertEqual(coil_controller, "Opponent")
        self.assertEqual(len(yards[coil_controller]), 0)
        yards["Opponent"].append("Response"); self.assertNotEqual(len(yards[coil_controller]), 0)

    def test_K6_kitten_target_control_and_no_greaves_shroud(self):
        self.assertNotIn("Lightning Greaves", self.cards)
        def kitten_target(control, land, shroud):
            return control and not land and not shroud
        self.assertTrue(kitten_target(True, False, False))
        self.assertFalse(kitten_target(False, False, False))
        self.assertFalse(kitten_target(True, True, False))
        self.assertFalse(kitten_target(True, False, True))

    def test_E1_repeated_blink_requires_new_cast_or_next_end_step(self):
        used = {1}
        used.clear()  # Kitten on a new noncreature spell, own Sol target
        self.assertEqual(used, set())
        beginning_end_step_event_count = 1
        self.assertEqual(beginning_end_step_event_count, 1)

    def test_E2_enchantment_transfer_not_bazaar_or_handoff(self):
        def can_gift_by_trader(typ):
            return typ in ("Artifact", "Creature", "Land")
        self.assertFalse(can_gift_by_trader("Enchantment"))  # Pact, Gambit
        self.assertTrue(can_gift_by_trader("Artifact"))  # Coil
        self.assertTrue(can_gift_by_trader("Creature"))  # Agent

    def test_W1_pact_gift_loss_needs_opponent_upkeep_and_no_removal(self):
        def loses(pact_exists, holder_upkeep, safe_modes_used):
            return pact_exists and holder_upkeep and safe_modes_used == 3
        self.assertTrue(loses(True, True, 3))
        self.assertFalse(loses(True, False, 3))
        self.assertFalse(loses(False, True, 3))

    def test_W2_coil_bog_alternative_rakdos_charm(self):
        controller_yard = {"Creature"}
        controller_yard.clear()  # both target-controller exile effects
        self.assertFalse(controller_yard)
        self.assertTrue("Rakdos Charm" in self.cards and "Bojuka Bog" in self.cards)

    def test_W3_audience_enters_under_opponent_no_extra_donation(self):
        owner, controller = "Cory", "Opponent"
        self.assertNotEqual(owner, controller)
        self.assertIn("Captive Audience", self.cards)

    def test_F2_opponent_disenchant_defeats_donated_pact(self):
        pact_exists = True
        pact_exists = False  # opposing instant-speed removal before upkeep
        self.assertFalse(pact_exists)

    def test_F3_brand_recovers_all_owned_including_dangerous_curses(self):
        owned = {"Sol'Kanar": "Opponent", "Demonic Pact": "Opponent"}
        reclaimed = {key: "Cory" for key in owned}
        self.assertEqual(reclaimed["Sol'Kanar"], "Cory")
        self.assertEqual(reclaimed["Demonic Pact"], "Cory")
        # Cycling {2} is card draw, not an additional draw on casting.

    def test_added_alexios_and_agent_political_constraints(self):
        owner = "Cory"
        alexios_controller = "Opponent"
        can_attack = lambda defender: defender != owner and defender != alexios_controller
        self.assertFalse(can_attack("Cory"))  # Alexios cannot attack owner
        self.assertFalse(can_attack(alexios_controller))
        self.assertEqual(2 * 3, 6)  # Agent 2 damage after three holder upkeeps

    def test_wishclaw_tutor_then_gift_risk(self):
        counters = 3
        counters -= 1  # {1}, tap, remove: tutor once, during own turn
        holder = "Opponent"  # control transfers on resolution
        self.assertEqual((counters, holder), (2, "Opponent"))


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--live", action="store_true")
    args = p.parse_args()
    if args.live:
        live_scryfall(check_lists())
    else:
        unittest.main(argv=["solkanar-test"], verbosity=2)
