"""Re-execute Admiral's original P0/P1 finite models against the *current* Rev2 roster.

The original executed models bind the older Oct 13 roster. This adapter
independently binds the six-swap Oct 22 approved raw 100, checks each case's
actual retained source cards, runs the relevant original positive/adversarial
methods, and substitutes the executed current Cosmotronic Wave / retained
Cannonade checks for the cut Raise the Palisade branch.

Scope: bounded mechanical equivalence only. No full Magic engine, tournament
win rate, historical I/J relabelling, new owner approval, or new decklist.
"""

from collections import Counter
import hashlib
import json
from pathlib import Path
import unittest

import test_m6_admiral_beckett_brass_p0 as old_p0
import test_m6_admiral_beckett_brass_p1_tranche1 as old_p1a
import test_m6_admiral_beckett_brass_p1_tranche2 as old_p1b
import test_m7_admiral_stage8_wave_palisade_paid_combat as stage8

AdmiralBeckettP0 = old_p0.AdmiralBeckettP0
AdmiralBeckettP1Tranche1 = old_p1a.AdmiralBeckettP1Tranche1
AdmiralBeckettP1Tranche2 = old_p1b.AdmiralBeckettP1Tranche2
AdmiralStage8PayableBlockers = stage8.AdmiralStage8PayableBlockers

ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = ROOT / "data/grixis/m7/research_challengers/Admiral_Beckett_Brass_six_Wave_Palisade_draw_resilient_20261022.txt"
BLUEPRINT = ROOT / "data/grixis/m6/test_blueprints/Admiral_Beckett_Brass.json"
CURRENT_SHA = "ff5f54f9f608ab0facd62fd3b79df16a0255b4dbbc12d39154a127f27bb8c000"

P0 = {
    "C01": [(AdmiralBeckettP0, "test_c01_live_oracle_and_commander_source_permissions")],
    "K01": [(AdmiralBeckettP0, "test_k01_same_player_three_distinct_pirates_and_permanent_theft")],
    "K02": [(AdmiralBeckettP0, "test_k02_throne_two_separate_triggers_not_lower_threshold")],
    "K03": [(AdmiralBeckettP0, "test_k03_kari_token_monkey_not_pirate")],
    "F01": [(AdmiralBeckettP0, "test_f01_blocker_fog_and_paid_mitigation")],
}
P1 = {
    "K04": [(AdmiralBeckettP1Tranche1, "test_k04_changeling_counts_and_different_sources"),
            (AdmiralBeckettP1Tranche1, "test_k04_blocked_or_prevented_outcast_no_false_threshold")],
    "K05": [(AdmiralBeckettP1Tranche1, "test_k05_fiery_cannonade_saves_all_pirates_not_only_ours"),
            (AdmiralStage8PayableBlockers, "test_sources_bound_and_no_borrowed_legality_cert"),
            (AdmiralStage8PayableBlockers, "test_retained_cannonade_defends_opponent_turn_versus_two_toughness")],
    "E01": [(AdmiralBeckettP1Tranche2, "test_e01_two_targets_stacked_after_three_distinct_pirates"),
            (AdmiralBeckettP1Tranche2, "test_e01_no_infinite_stolen_objects_or_trigger_without_fresh_hits")],
    "E02": [(AdmiralBeckettP1Tranche2, "test_e02_six_card_oracle_cost_and_trigger_differences"),
            (AdmiralBeckettP1Tranche2, "test_e02_physical_draw_treasure_exile_and_no_free_cast"),
            (AdmiralBeckettP1Tranche2, "test_e02_fog_stops_hit_value_not_attack_trigger_value")],
    "W01": [(AdmiralBeckettP1Tranche2, "test_w01_four_real_combat_steps_reach_40_life_only_if_3_connect"),
            (AdmiralBeckettP1Tranche2, "test_w01_fog_and_end_step_commander_removal_are_distinct_failures"),
            (AdmiralStage8PayableBlockers, "test_threshold_is_same_player_and_commander_end_step_survival")],
    "W02": [(AdmiralBeckettP1Tranche1, "test_w02_port_razer_new_player_combat_only_and_own_untap"),
            (AdmiralBeckettP1Tranche1, "test_w02_no_hit_no_combat_and_distinct_sources_across_phases")],
    "F02": [(AdmiralBeckettP1Tranche2, "test_f02_toxic_deluge_self_wipe_paid_life_and_full_type_coverage"),
            (AdmiralBeckettP1Tranche2, "test_f02_pirate_reanimation_finality_and_timed_token_recovery")],
    "F03": [(AdmiralBeckettP1Tranche1, "test_f03_commander_removal_timing_and_source_paid_recast"),
            (AdmiralBeckettP1Tranche1, "test_f03_swat_fierce_and_stormtamer_are_conditional"),
            (AdmiralBeckettP1Tranche1, "test_f03_greaves_shroud_requires_sorcery_speed_equip")],
}

# The mapping retains the original TestCase classes, but they must not be
# collected a second time as standalone *current* tests. In particular, the
# historical Palisade method is not a current-card certification.
del AdmiralBeckettP0, AdmiralBeckettP1Tranche1
del AdmiralBeckettP1Tranche2, AdmiralStage8PayableBlockers


class AdmiralCurrentOriginalCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        raw = CANDIDATE.read_bytes()
        if hashlib.sha256(raw).hexdigest() != CURRENT_SHA:
            raise AssertionError("Admiral current 100 changed; refuse original-case equivalence")
        names = Counter()
        for line in raw.decode("utf-8").splitlines():
            qty, name = line.split("x ", 1)
            names[name.removesuffix(" [Commander]")] += int(qty)
        cls.names = names
        cls.plan = json.loads(BLUEPRINT.read_text())
        cls.by_case = {x["test_id"]: x for x in cls.plan["tests"]}
        for model in (old_p0.AdmiralBeckettP0, old_p1a.AdmiralBeckettP1Tranche1,
                      old_p1b.AdmiralBeckettP1Tranche2, stage8.AdmiralStage8PayableBlockers):
            model.setUpClass()

    def _run(self, case_id, priority):
        methods = (P0 if priority == "P0" else P1)[case_id]
        plan = self.by_case[case_id]
        self.assertEqual(plan["priority"], priority)
        self.assertEqual(sum(self.names.values()), 100)
        self.assertEqual(self.names["Admiral Beckett Brass"], 1)
        self.assertEqual(self.names["Roaming Throne"], 1)
        self.assertTrue(all(q == 1 or name in {"Island", "Mountain", "Swamp"}
                            for name, q in self.names.items()))

        # Only the obsolete Palisade branch of K05 and historical Dire Fleet
        # reference in W01 are exempt. Neither gets a current test pass.
        missing = {name for name in plan["associated_cards"] if self.names[name] == 0}
        expected_missing = {"Raise the Palisade"} if case_id == "K05" else (
            {"Dire Fleet Captain"} if case_id == "W01" else set())
        self.assertEqual(missing, expected_missing, f"Changed source invalidated {case_id}")
        if case_id == "K05":
            self.assertEqual(self.names["Fiery Cannonade"], 1)
            self.assertEqual(self.names["Cosmotronic Wave"], 1)
            self.assertEqual(self.names["Raise the Palisade"], 0)
        if case_id == "W01":
            for attacker in ("Changeling Outcast", "Storm Fleet Sprinter",
                             "Spyglass Siren", "Corsair Captain"):
                self.assertEqual(self.names[attacker], 1)
            self.assertEqual(self.names["Cloud Pirates"], 1)

        # Actually execute original bounded source-paid methods within the
        # exact-current-roster precondition above; never just scan their names.
        for model, name in methods:
            with self.subTest(original_case=case_id, executed_method=name):
                result = unittest.TestResult()
                model(methodName=name).run(result)
                self.assertEqual(result.testsRun, 1)
                self.assertEqual(result.errors, [])
                self.assertEqual(result.failures, [])
                self.assertEqual(result.skipped, [])

    def test_C01(self): self._run("C01", "P0")
    def test_K01(self): self._run("K01", "P0")
    def test_K02(self): self._run("K02", "P0")
    def test_K03(self): self._run("K03", "P0")
    def test_F01(self): self._run("F01", "P0")
    def test_K04(self): self._run("K04", "P1")
    def test_K05(self): self._run("K05", "P1")
    def test_E01(self): self._run("E01", "P1")
    def test_E02(self): self._run("E02", "P1")
    def test_W01(self): self._run("W01", "P1")
    def test_W02(self): self._run("W02", "P1")
    def test_F02(self): self._run("F02", "P1")
    def test_F03(self): self._run("F03", "P1")


if __name__ == "__main__":
    unittest.main()
