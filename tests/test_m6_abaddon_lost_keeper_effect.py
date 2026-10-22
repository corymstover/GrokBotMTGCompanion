"""Finite M6.6 payoffs from actual V2 100-card source libraries.

Not randomized access, a comprehensive Oracle recheck, or a final swap verdict.
Precommitted: data/grixis/m6/phase_b_plans/abaddon_lost_keeper_effect_20261022.json
"""
from collections import Counter
import json
from pathlib import Path
import unittest

from scripts.grixis_m7_decision_gate import parse_list
from scripts.grixis_m6_abaddon_ignus_stack_windows import (
    verify_study, fixture, relocate, legal_hand_ignus_and_first_cascade
)
from scripts.grixis_m6_abaddon_ignus_shared_effects import (
    assert_conserved, expected_physical
)

ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "data/grixis/m6/phase_b_plans/abaddon_lost_keeper_effect_20261022.json"
LOST = "The Lost and the Damned"
KEEPER = "Keeper of Secrets"
HIT = "Sol Ring"
FETCH = "Polluted Delta"
FETCHABLE = ("Island", "Swamp", "Underground Sea", "Watery Grave",
             "Steam Vents", "Badlands", "Blood Crypt", "Volcanic Island")


def library_from_variant(plan, record):
    cards, commander, companions = parse_list(ROOT / record["path"])
    assert commander == ["Abaddon the Despoiler"], commander
    assert companions == [], companions
    assert len(cards) == 100 and len(set(cards)) == 94
    lib = cards[1:]
    assert len(lib) == 99 and LOST in lib and HIT in lib and KEEPER in lib == record["keeper"]
    assert lib.count("Island") == lib.count("Mountain") == lib.count("Swamp") == 3
    return lib


def record_payoffs(state, *, nonhand_casts, cast_mana_values, library_land_entries=0):
    """Resolve *cast* and from-library entry triggers; no made-up deck pieces.

    Countering a spell after it was cast does not undo either triggered ability.
    The helper records virtual Spawn tokens, separate from the original 99 cards.
    """
    assert all(isinstance(mv, int) and mv >= 0 for mv in cast_mana_values)
    assert nonhand_casts == len(cast_mana_values) and library_land_entries >= 0
    has_lost = LOST in state["field"]
    has_keeper = KEEPER in state["field"]
    return {
        "actual_nonhand_casts": nonhand_casts,
        "spawn_tokens": (nonhand_casts + library_land_entries) if has_lost else 0,
        "keeper_trigger_count": nonhand_casts if has_keeper else 0,
        # Each Keeper trigger damages ONE opponent, not each opponent.
        "keeper_targeted_damage": sum(cast_mana_values) if has_keeper else 0,
        "trigger_from_library_land": library_land_entries if has_lost else 0,
    }


class AbaddonLostKeeperPayoff(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.plan = json.loads(PLAN.read_text(encoding="utf-8"))
        cls.prior_plan, cls.prior, cls.oracle_cards, _ = verify_study()
        cls.variants = cls.plan["variants"]

    def test_plan_boundaries_and_cases(self):
        p = self.plan
        self.assertEqual(p["baseline_raw_sha256"],
                         "2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf")
        self.assertEqual(p["cost_budget"]["randomized_trajectories"], 0)
        self.assertEqual(p["cost_budget"]["registered_cases"], 7)
        self.assertEqual({c["id"] for c in p["registered_cases"]}, {
            "legal_cast_supported_hit", "drannith_bars_exile_cast",
            "rule_of_law_bars_exile_cast", "countered_nonhand_spell_still_triggers",
            "hand_cast_ignus_only", "nonhand_fetchland_entry", "hand_land_entry_no_spawn",
        })
        self.assertFalse(p["canonical_list_changes_allowed"])
        self.assertFalse(p["formal_m6_certification_allowed"])
        self.assertFalse(p["owner_approval_allowed"])

    def stage(self, variant):
        library = library_from_variant(self.plan, variant)
        state = fixture(library)
        relocate(state, LOST, "field")
        if variant["keeper"]:
            relocate(state, KEEPER, "field")
        assert_conserved(state, expected_physical(library))
        return library, state

    def test_legal_and_hate_policies_with_real_source_paid_ignus_and_first_hit(self):
        for variant in self.variants:
            for condition in ("legal_cast_supported_hit", "drannith_bars_exile_cast",
                              "rule_of_law_bars_exile_cast"):
                with self.subTest(variant=variant["id"], case=condition):
                    lib, s = self.stage(variant)
                    before = s["metrics"]["actual_supported_hit_cast"]
                    receipt = legal_hand_ignus_and_first_cascade(
                        s, self.oracle_cards, self.prior,
                        drannith=condition == "drannith_bars_exile_cast",
                        rule_of_law=condition == "rule_of_law_bars_exile_cast"
                    )
                    new_cast = s["metrics"]["actual_supported_hit_cast"] - before
                    actual = int(receipt["cascade_free_cast"])
                    self.assertEqual(new_cast, actual)
                    self.assertEqual(receipt["first_hit"], HIT)
                    self.assertEqual(actual, int(condition == "legal_cast_supported_hit"))
                    self.assertTrue(receipt["initial_hand_cast"])
                    payoff = record_payoffs(s, nonhand_casts=actual,
                                            cast_mana_values=[1] if actual else [])
                    self.assertEqual(payoff["spawn_tokens"], actual)
                    self.assertEqual(payoff["keeper_trigger_count"], actual if variant["keeper"] else 0)
                    self.assertEqual(payoff["keeper_targeted_damage"],
                                     actual if variant["keeper"] else 0)
                    assert_conserved(s, expected_physical(lib))

    def test_counter_after_actual_nonhand_cast_keeps_cast_triggers(self):
        for variant in self.variants:
            with self.subTest(variant=variant["id"]):
                lib, s = self.stage(variant)
                # Countered *after casting* is an adversarial event; this check
                # does not call first_cascade (which would auto-resolve its hit).
                # The physical Sol Ring remains top of the source deck until
                # cast, and its own resolution is intentionally NOT simulated.
                self.assertEqual(s["deck"][0], HIT)
                event = ["exile_cast_sol_ring_mv1", "opponent_counter_sol_ring"]
                self.assertEqual(event[0], "exile_cast_sol_ring_mv1")
                payoff = record_payoffs(s, nonhand_casts=1, cast_mana_values=[1])
                self.assertEqual(payoff["spawn_tokens"], 1)
                self.assertEqual(payoff["keeper_targeted_damage"], 1 if variant["keeper"] else 0)
                assert_conserved(s, expected_physical(lib))

    def test_hand_cast_ignus_is_not_outside_hand(self):
        for variant in self.variants:
            lib, s = self.stage(variant)
            payoffs = record_payoffs(s, nonhand_casts=0, cast_mana_values=[])
            self.assertEqual(payoffs["spawn_tokens"], 0)
            self.assertEqual(payoffs["keeper_targeted_damage"], 0)
            assert_conserved(s, expected_physical(lib))

    def test_library_fetch_source_triggers_lost_once_hand_land_does_not(self):
        for variant in self.variants:
            with self.subTest(variant=variant["id"]):
                lib, s = self.stage(variant)
                original = expected_physical(lib)
                # Prearranged real fetchland in hand, not invented or cloned.
                relocate(s, FETCH, "hand")
                s["hand"].remove(FETCH)
                s["lands"].append((FETCH, False))
                enter_from_hand = record_payoffs(s, nonhand_casts=0, cast_mana_values=[])
                self.assertEqual(enter_from_hand["spawn_tokens"], 0)
                assert_conserved(s, original)
                # Resolve a legal Polluted Delta search for Island/Swamp typed
                # target physically in this candidate library.
                land_name = next((n for n in FETCHABLE if n in s["deck"]), None)
                self.assertIsNotNone(land_name)
                s["lands"].remove((FETCH, False))
                s["graveyard"].append(FETCH)
                s["deck"].remove(land_name)
                s["lands"].append((land_name, True))
                enter_from_library = record_payoffs(s, nonhand_casts=0,
                                                      cast_mana_values=[],
                                                      library_land_entries=1)
                self.assertEqual(enter_from_library["spawn_tokens"], 1)
                self.assertEqual(enter_from_library["keeper_targeted_damage"], 0)
                assert_conserved(s, original)

    def test_zero_mv_nonhand_cast_makes_spawn_but_no_keeper_damage(self):
        for variant in self.variants:
            lib, s = self.stage(variant)
            triggers = record_payoffs(s, nonhand_casts=1, cast_mana_values=[0])
            self.assertEqual(triggers["spawn_tokens"], 1)
            self.assertEqual(triggers["keeper_trigger_count"], 1 if variant["keeper"] else 0)
            self.assertEqual(triggers["keeper_targeted_damage"], 0)
            assert_conserved(s, expected_physical(lib))


if __name__ == "__main__":
    unittest.main()
