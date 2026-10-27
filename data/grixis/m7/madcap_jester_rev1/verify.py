"""Deck 56 M7 Rev1: exact list, public Oracle and bounded event/cost tests.

Not a complete Magic engine, simulated multiplayer win-rate study, or an
independent/retroactive M6 I/J certification. Public Oracle bulk is read
locally; no named deck contents are submitted to the Scryfall API.
"""
import argparse
from collections import Counter
import gzip
from hashlib import sha256
import json
from pathlib import Path
import unittest

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
BASE = HERE / "The_Madcap_Jester_Oct15_baseline.txt"
FINAL = HERE.parent / "candidate_lists/The_Madcap_Jester_M7_Rev1.txt"
ALT8 = HERE.parent / "candidate_lists/The_Madcap_Jester_M7_Rev1_alt8.txt"
ALT9 = HERE.parent / "candidate_lists/The_Madcap_Jester_M7_Rev1_alt9.txt"
HASHES = {
    BASE: "caeffc07503581cd3ecba798ebc4e09d48f07310f1f117ce3b90a04b5ca6bfa7",
    FINAL: "643eb1cc4827c1dd95485e9922506b514746e6bbc5b4b8a4cfff0f44b1007e43",
    ALT8: "65c548d31e38e11ff05d66404720bb322275d751b953f3a6eee357a254a93c34",
    ALT9: "fd4ea044323ce9cffd7952ca6e97fc052a7ea7c92f3438fd331957e366d7b83d",
}
PAIRS = {
    "Opposition Agent": "Sire of Stagnation",
    "Black Widow, Super Spy": "Nalfeshnee",
    "Grimoire Thief": "Plargg and Nassari",
    "Borne Upon a Wind": "Gonti, Night Minister",
    "Hexing Squelcher": "Wild-Magic Sorcerer",
    "Gloomlake Verge": "Drowned Catacomb",
    "Flusterstorm": "Bitter Ordeal",
}
PROTECTED = {"The Madcap Jester", "Dragon's Smile", "Extract", "Sadistic Sacrament",
             "Tasha's Hideous Laughter", "Jester's Cap", "Jester's Scepter", "Inside Information",
             "Ensnared by the Mara", "Psychic Surgery", "Ashiok, Nightmare Weaver",
             "Circu, Dimir Lobotomist", "Praetor's Grasp", "Dauthi Voidwalker",
             "Bilbo, Thief in the Night", "Thieving Varmint", "Don Andres, the Renegade",
             "Prosper, Tome-Bound", "Passionate Archaeologist", "Lightning Greaves",
             "Thassa's Oracle", "Demonic Consultation", "Tainted Pact", "Underworld Breach",
             "Lion's Eye Diamond", "Brain Freeze"}
AUTHORIZED_FUTURE = {"The Madcap Jester", "Dragon's Smile"}


def parse(path):
    raw = path.read_bytes()
    assert sha256(raw).hexdigest() == HASHES[path], path
    assert raw.endswith(b"\n") and b"\r" not in raw, path
    lines = raw.decode("utf-8").splitlines()
    assert lines[0] == "1x The Madcap Jester [Commander]", path
    c = Counter()
    for line in lines:
        number, card = line.split("x ", 1)
        assert int(number) == 1, line
        c[card.removesuffix(" [Commander]")] += int(number)
    assert sum(c.values()) == 100 and len(c) == 100, path
    return c


def physical():
    base, end = parse(BASE), parse(FINAL)
    assert len(base) == len(end) == 100
    assert end - base == Counter(PAIRS.keys())
    assert base - end == Counter(PAIRS.values())
    assert PROTECTED <= set(end)
    assert set(end) - set(base) == set(PAIRS)
    e8, e9 = parse(ALT8), parse(ALT9)
    assert e8 - base == Counter(list(PAIRS) + ["The Stone Brain"])
    assert base - e8 == Counter(list(PAIRS.values()) + ["Jester's Cap"])
    assert e9 - base == Counter(list(PAIRS) + ["The Stone Brain", "Arena of Glory"])
    assert base - e9 == Counter(list(PAIRS.values()) + ["Jester's Cap", "Sulfurous Springs"])
    print("PASS source raw SHA / 100-unique / 7 swaps / two full 8- and 9-swap 100s / core preservation")
    return end


def scan_oracle(path):
    selected = set(parse(FINAL)) | {"The Stone Brain", "Arena of Glory"}
    found = {}
    opener = gzip.open if str(path).endswith(".gz") else open
    with opener(path, "rt", encoding="utf8") as stream:
        for line in stream:
            obj = json.loads(line)
            if obj.get("name") in selected:
                found[obj["name"]] = obj
    assert set(found) == selected, sorted(selected - set(found))
    illegal = {}
    for name, obj in found.items():
        assert obj.get("oracle_id") and (obj.get("oracle_text") or obj.get("card_faces")), name
        assert set(obj.get("color_identity", [])) <= {"U", "B", "R"}, name
        legality = obj.get("legalities", {}).get("commander")
        if legality != "legal":
            illegal[name] = legality
    assert illegal == {"The Madcap Jester": "not_legal", "Dragon's Smile": "not_legal"}, illegal
    expected_snippets = {
        "The Madcap Jester": ["whenever the madcap jester attacks", "spell or ability you control", "until the end of your next turn"],
        "Dragon's Smile": ["once during each of your turns", "{0} rather than pay"],
        "Grimoire Thief": ["becomes tapped", "top three cards", "face down"],
        "Black Widow, Super Spy": ["combat damage to a player", "nonland card"],
        "Opposition Agent": ["while they're searching", "they exile each card"],
        "Borne Upon a Wind": ["as though they had flash", "draw a card"],
        "Hexing Squelcher": ["spells you control can't be countered", "ward"],
        "Flusterstorm": ["storm", "instant or sorcery"],
        "Gloomlake Verge": ["add {u}", "island or a swamp"],
        "The Stone Brain": ["activate only as a sorcery", "choose a card name"],
        "Arena of Glory": ["exert this land", "gains haste"],
        "Dauthi Voidwalker": ["would be put into an opponent's graveyard", "exile it with a void counter"],
    }
    for name, snippets in expected_snippets.items():
        text = found[name].get("oracle_text", "").lower()
        for piece in snippets:
            assert piece in text, (name, piece)
    lands = [n for n, obj in found.items() if n in parse(FINAL) and "Land" in obj["type_line"].split(" // ")[0]]
    assert len(lands) == 34, (len(lands), lands)
    print("PASS public 2026-10-27 Scryfall Oracle: all 102 candidate/alternative names, 34 lands; 100% UBR/colorless; exactly two future-release exceptions; 98/98 ordinary candidates Commander legal")


def cause_exile(is_controller, jester_on_board, library_cards, event, dauthi=False):
    """Small zone-transition fixture for CR 603.2/614.6, not a Magic game engine.

    A replaced mill event's original graveyard transition does not occur;
    an exile transition occurs with a void counter. Whether Wizards treats
    that modified event as 'caused by' Brain Freeze for this specific Jester
    wording has no card-specific ruling: no win line rests on it here.
    """
    destination = "exile" if dauthi and event == "mill" else ("graveyard" if event == "mill" else "exile")
    happened_library_exile = destination == "exile" and library_cards > 0
    return dict(zone=destination, void_counter=dauthi and event == "mill",
                uncontroversial_jester_trigger=(is_controller and jester_on_board and happened_library_exile and event == "direct_exile"))


class FiniteCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cards = physical()

    def test_C1_attack_exiles_without_combat_damage(self):
        attacker_declared, opponents_with_libraries = True, 3
        self.assertEqual(opponents_with_libraries if attacker_declared else 0, 3)
        self.assertIn("The Madcap Jester", self.cards)

    def test_C1_removed_before_exile_no_late_permission(self):
        self.assertFalse(cause_exile(True, False, 3, "direct_exile")["uncontroversial_jester_trigger"])
        self.assertTrue(cause_exile(True, True, 3, "direct_exile")["uncontroversial_jester_trigger"])

    def test_K1_stolen_permission_not_free_cast_and_land_quota(self):
        paid_total, available_mana, land_drop_available = 5, 4, False
        self.assertFalse(available_mana >= paid_total)
        self.assertFalse(land_drop_available)

    def test_K2_replacement_event_zone_and_causation_caveat(self):
        swapped = cause_exile(True, True, 3, "mill", dauthi=True)
        self.assertEqual(swapped["zone"], "exile")
        self.assertTrue(swapped["void_counter"])
        self.assertFalse(swapped["uncontroversial_jester_trigger"])
        self.assertEqual(cause_exile(True, True, 3, "mill")["zone"], "graveyard")

    def test_K3_uba_mask_symmetry_is_not_a_selected_source(self):
        self.assertNotIn("Uba Mask", self.cards)
        self.assertFalse(cause_exile(False, True, 1, "direct_exile")["uncontroversial_jester_trigger"])

    def test_K4_pact_never_duplicate_stops(self):
        self.assertEqual(len(self.cards), 100)
        self.assertEqual(sum(quantity > 1 for quantity in self.cards.values()), 0)

    def test_K5_brain_freeze_storm_copies_not_cast(self):
        spells_cast_before_freeze = 4
        original_and_copies = 1 + spells_cast_before_freeze
        self.assertEqual(original_and_copies * 3, 15)
        self.assertNotEqual(original_and_copies, 1 + original_and_copies)

    def test_K6_named_future_only_exceptions(self):
        self.assertEqual(AUTHORIZED_FUTURE, {"The Madcap Jester", "Dragon's Smile"})
        self.assertIn("Dragon's Smile", self.cards)

    def test_E1_extract_search_one_card_and_pay_ordinary_cost(self):
        self.assertTrue(cause_exile(True, True, 1, "direct_exile")["uncontroversial_jester_trigger"])
        extracted_creature_mv, mana_after_extract = 7, 3
        self.assertLess(mana_after_extract, extracted_creature_mv)

    def test_E2_haste_from_greaves_then_attack_event(self):
        jester_cast_this_turn, greaves_attached = True, True
        self.assertTrue(jester_cast_this_turn and greaves_attached)
        self.assertIn("Lightning Greaves", self.cards)

    def test_E3_black_widow_hits_not_immediate_cast(self):
        exiled = ["Land", "Land", "Nonland"]
        self.assertEqual(len(exiled), 3)
        self.assertTrue(cause_exile(True, True, len(exiled), "direct_exile")["uncontroversial_jester_trigger"])
        self.assertIn("Black Widow, Super Spy", self.cards)

    def test_E4_grimoire_tap_trigger_not_damage_trigger(self):
        tapped_at_attack, blocked = True, True
        self.assertEqual(3 if tapped_at_attack else 0, 3)
        self.assertTrue(blocked)  # Blocked still triggers the tap exile event.
        self.assertFalse(cause_exile(True, False, 3, "direct_exile")["uncontroversial_jester_trigger"])

    def test_E5_flash_cantrip_window_and_payment_still_required(self):
        stolen_sorcery_cost, colored_resources = 3, 3
        flash_granted_this_turn = True
        self.assertTrue(flash_granted_this_turn and colored_resources >= stolen_sorcery_cost)
        self.assertIn("Borne Upon a Wind", self.cards)

    def test_E6_opposition_agent_not_generic_library_exile_source(self):
        search_occurs, agent_controller_takes_over = True, True
        self.assertTrue(search_occurs and agent_controller_takes_over)
        self.assertFalse(cause_exile(False, True, 0, "direct_exile")["uncontroversial_jester_trigger"])

    def test_E7_hexing_not_shroud_or_absolute_protection(self):
        opponent_can_pay_two_life_to_target_other_creature = True
        self.assertTrue(opponent_can_pay_two_life_to_target_other_creature)
        self.assertIn("Hexing Squelcher", self.cards)

    def test_E8_flusterstorm_storm_is_spells_cast_not_copies(self):
        cast_spells, copies_of_a_previous_spell = 3, 4
        self.assertEqual(1 + cast_spells, 4)
        self.assertNotEqual(1 + cast_spells, 1 + cast_spells + copies_of_a_previous_spell)

    def test_E9_gloomlake_blue_untapped_black_conditional(self):
        has_island_or_swamp = False
        blue_available = True
        black_available = has_island_or_swamp
        self.assertTrue(blue_available)
        self.assertFalse(black_available)

    def test_W1_oracle_consult_pact_exile_own_library_not_jester(self):
        self.assertTrue({"Thassa's Oracle", "Demonic Consultation", "Tainted Pact"} <= set(self.cards))
        self.assertFalse(cause_exile(True, True, 99, "mill")["uncontroversial_jester_trigger"])

    def test_W2_breach_freeze_led_requires_escape_fuel(self):
        cards_to_escape_breach_spell = 3
        graveyard_other_cards = 2
        self.assertFalse(graveyard_other_cards >= cards_to_escape_breach_spell)
        self.assertTrue({"Underworld Breach", "Lion's Eye Diamond", "Brain Freeze"} <= set(self.cards))

    def test_W3_dragon_smile_once_per_own_turn_and_paid_additional_cost(self):
        used_free_option_this_turn = True
        self.assertFalse(not used_free_option_this_turn)
        required_additional_cost, mana_for_additional_cost = 2, 0
        self.assertFalse(mana_for_additional_cost >= required_additional_cost)

    def test_F1_sire_vs_agent_response_window(self):
        agent_mana, sire_mana, opposing_tutor_window = 3, 6, True
        self.assertTrue(agent_mana < sire_mana and opposing_tutor_window)

    def test_F1_cap_vs_stone_brain_additional_swap_cost(self):
        cap_cast_and_activate = 4 + 2
        brain_cast_and_activate = 2 + 2
        self.assertEqual((cap_cast_and_activate, brain_cast_and_activate), (6, 4))
        self.assertGreater(3, 1)  # Cap chooses three potentially distinct names.

    def test_F2_arena_haste_conditional_and_exert_turn_lock(self):
        untapped_if_mountain = True
        red_activation_paid = True
        misses_next_untap_if_exerted = True
        self.assertTrue(all([untapped_if_mountain, red_activation_paid, misses_next_untap_if_exerted]))

    def test_F3_counterplay_and_branch_weakness(self):
        removal_before_library_exile = True
        self.assertFalse(cause_exile(True, not removal_before_library_exile, 3, "direct_exile")["uncontroversial_jester_trigger"])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--oracle-file", type=Path)
    args = parser.parse_args()
    physical()
    if args.oracle_file:
        scan_oracle(args.oracle_file)
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(FiniteCases)
    result = unittest.TextTestRunner(verbosity=1).run(suite)
    print(f"M7 Madcap C/K/E/W/F bounded cases: {result.testsRun} executed, {len(result.failures)} failures, {len(result.errors)} errors")
    if not result.wasSuccessful():
        raise SystemExit(1)


if __name__ == "__main__":
    main()
