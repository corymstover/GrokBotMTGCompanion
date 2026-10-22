"""Abaddon P0: actual staged 100-card Betrayal MV0 vs Keeper nonhand-cast effects.

Six preregistered deterministic, conditional physical-zone fixtures. This is
NOT a metagame, opponent action-probability, or comparative win-rate model.
"""
from __future__ import annotations

from collections import Counter
import hashlib
import json
from pathlib import Path
import unittest

from scripts.grixis_m6_abaddon_ignus_shared_effects import (
    ABADDON, BIRGI, IGNUS, source_cast, effect_add, assert_conserved,
    expected_physical,
)
from scripts.grixis_m6_abaddon_ignus_stack_windows import fixture, relocate
from scripts.grixis_m7_decision_gate import parse_list

ROOT = Path(__file__).resolve().parents[1]
PLAN = json.loads((ROOT / "data/grixis/m6/phase_b_plans/abaddon_p0_theft_keeper_diff_20261022.json").read_text())
LOST = "The Lost and the Damned"
KEEPER = "Keeper of Secrets"
BETRAYAL = "Inevitable Betrayal"
SOL_RING = "Sol Ring"
PETAL = "Lotus Petal"
OPPONENT_LIBRARY = ["Baleful Strix", "Island", "Swamp"]
COST_MV = {BETRAYAL: 0, PETAL: 0, SOL_RING: 1}


def source_deck(kind):
    v = next(x for x in PLAN["known_physical_variants"] if x["id"] == kind)
    path = ROOT / v["path"]
    assert hashlib.sha256(path.read_bytes()).hexdigest() == v["sha256"]
    cards, commander, companions = parse_list(path)
    assert len(cards) == 100 and len(set(cards)) == 94
    assert commander == [ABADDON] and companions == []
    library = cards[1:]
    assert len(library) == 99
    assert (BETRAYAL in library) == v["betrayal"]
    assert (KEEPER in library) == v["keeper"]
    assert LOST in library and IGNUS in library and SOL_RING in library and PETAL in library
    return library


def setup(kind, hit):
    library = source_deck(kind)
    if hit not in library:
        raise AssertionError("Cannot create an absent hit")
    state = fixture(library)
    relocate(state, LOST, "field")
    if kind == "preferred":
        relocate(state, KEEPER, "field")
    # CONDITIONAL top placement; physical card moved from source hand/deck.
    relocate(state, hit, "top")
    assert_conserved(state, expected_physical(library))
    return library, state


def hand_ignus_cascade(state, library, hit, *, drannith=False, rule_of_law=False,
                      counter_hit=False, opponent_library=None):
    """One true paid hand spell and one guaranteed *prearranged* first hit.

    The opponent inventory is a separate, explicitly modeled physical source.
    Putting a creature onto our battlefield does NOT cast that creature.
    """
    if opponent_library is None:
        opponent_library = list(OPPONENT_LIBRARY)
    else:
        opponent_library = list(opponent_library)
    own_original = expected_physical(library)
    opponent_original = Counter(opponent_library)
    paid = source_cast(state["lands"], state["pool"], IGNUS,
                       familiar_controlled=False, rakdos_controlled=False,
                       opponent_loss=state["loss"])
    if paid is None:
        raise AssertionError("Ignus cannot be source-paid from prearranged 3 colored lands")
    if ABADDON not in state["field"] or state["loss"] < 3:
        raise AssertionError("Ignus not a qualifying hand cascade cast")
    state["hand"].remove(IGNUS)
    state["pool"] = effect_add(paid, r=1)  # Birgi hand-cast trigger; resolves
    first = state["deck"].pop(0)
    if first != hit or COST_MV[first] >= 3:
        raise AssertionError("Physical cascade first eligible card not registered")
    cast = not (drannith or rule_of_law)
    opponent_on_our_battlefield = []
    spawn = 0
    keeper_damage = 0
    other_nonhand_spell_casts = 0
    if cast:
        other_nonhand_spell_casts = 1
        state["pool"] = effect_add(state["pool"], r=1)  # Birgi's second cast trigger
        spawn = int(LOST in state["field"])
        keeper_damage = COST_MV[first] if KEEPER in state["field"] else 0
        if first == BETRAYAL and not counter_hit:
            # Inevitable Betrayal TARGETS opponent, searching their library.
            # Conditional opponent library: first actual creature chosen is
            # Baleful Strix; NOT cast and NOT sourced from our 99 cards.
            if "Baleful Strix" in opponent_library:
                opponent_library.remove("Baleful Strix")
                opponent_on_our_battlefield.append("Baleful Strix")
        if first == SOL_RING and not counter_hit:
            state["field"].add(SOL_RING)
        else:
            state["graveyard"].append(first)
    else:
        state["deck"].append(first)  # not cast: cascade puts hit onto bottom
    state["field"].add(IGNUS)  # original hand spell resolves, independently
    if state["loss"] != 9:
        raise AssertionError("Unmodeled opponent damage should not be attributed to ignus")
    assert_conserved(state, own_original)
    if Counter(opponent_library) + Counter(opponent_on_our_battlefield) != opponent_original:
        raise AssertionError("Opponent source card created or lost")
    return {
        "first_hit": first, "cast_from_exile": cast, "nonhand_spell_casts": other_nonhand_spell_casts,
        "lost_spawn_tokens": spawn, "keeper_targeted_damage": keeper_damage,
        "opponent_creatures_put_onto_our_battlefield": opponent_on_our_battlefield,
        "opponent_library_after": opponent_library,
        "opponent_creatures_cast": 0,
        "cascades_granted_to_exile_cast": 0,
        "countered_after_cast": counter_hit,
    }


class BetrayalKeeperP0(unittest.TestCase):
    def test_p0_betrayal_source_paid_hit(self):
        library, state = setup("alternative", BETRAYAL)
        r = hand_ignus_cascade(state, library, BETRAYAL)
        self.assertTrue(r["cast_from_exile"])
        self.assertEqual(r["nonhand_spell_casts"], 1)
        self.assertEqual(r["lost_spawn_tokens"], 1)
        self.assertEqual(r["keeper_targeted_damage"], 0)
        self.assertEqual(r["opponent_creatures_put_onto_our_battlefield"], ["Baleful Strix"])
        self.assertEqual(r["opponent_creatures_cast"], 0)
        self.assertEqual(r["cascades_granted_to_exile_cast"], 0)

    def test_p0_betrayal_no_creatures(self):
        library, state = setup("alternative", BETRAYAL)
        r = hand_ignus_cascade(state, library, BETRAYAL, opponent_library=["Island", "Swamp"])
        self.assertTrue(r["cast_from_exile"])
        self.assertEqual(r["lost_spawn_tokens"], 1)
        self.assertEqual(r["opponent_creatures_put_onto_our_battlefield"], [])

    def test_p0_betrayal_countered(self):
        library, state = setup("alternative", BETRAYAL)
        r = hand_ignus_cascade(state, library, BETRAYAL, counter_hit=True)
        self.assertTrue(r["cast_from_exile"])
        self.assertEqual(r["lost_spawn_tokens"], 1)
        self.assertEqual(r["opponent_creatures_put_onto_our_battlefield"], [])
        self.assertIn(BETRAYAL, state["graveyard"])

    def test_p0_betrayal_drannith(self):
        library, state = setup("alternative", BETRAYAL)
        r = hand_ignus_cascade(state, library, BETRAYAL, drannith=True)
        self.assertFalse(r["cast_from_exile"])
        self.assertEqual(r["lost_spawn_tokens"], 0)
        self.assertEqual(r["keeper_targeted_damage"], 0)
        self.assertEqual(r["opponent_creatures_put_onto_our_battlefield"], [])
        self.assertIn(BETRAYAL, state["deck"])
        self.assertNotIn(BETRAYAL, state["graveyard"])

    def test_p0_betrayal_rule_of_law(self):
        library, state = setup("alternative", BETRAYAL)
        r = hand_ignus_cascade(state, library, BETRAYAL, rule_of_law=True)
        self.assertFalse(r["cast_from_exile"])
        self.assertEqual(r["lost_spawn_tokens"], 0)
        self.assertEqual(r["nonhand_spell_casts"], 0)
        self.assertEqual(r["opponent_creatures_put_onto_our_battlefield"], [])

    def test_p0_keeper_mv1_and_mv0(self):
        for hit, damage, destination in ((SOL_RING, 1, "field"), (PETAL, 0, "graveyard")):
            with self.subTest(hit=hit):
                lib, state = setup("preferred", hit)
                r = hand_ignus_cascade(state, lib, hit)
                self.assertEqual(r["first_hit"], hit)
                self.assertTrue(r["cast_from_exile"])
                self.assertEqual(r["lost_spawn_tokens"], 1)
                self.assertEqual(r["keeper_targeted_damage"], damage)
                self.assertEqual(r["opponent_creatures_put_onto_our_battlefield"], [])
                self.assertNotIn(BETRAYAL, lib)
                self.assertIn(hit, state[destination])


if __name__ == "__main__":
    unittest.main()
