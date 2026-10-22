"""Source-grounded M6.7 Abaddon disposition and no-certification regressions.

Checks archived physically paid observations; NOT a new gameplay simulation or
an approval. Existing per-mechanic rules tests and their CI receipts are separate.
"""
import json
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "data/grixis/m6/judgment_reviews/abaddon_candidate_disposition_synthesis_20261022.json"
PRIOR = ROOT / "data/grixis/m6/judgment_reviews/abaddon_phase_b_decisions_20261021.json"
LEDGER = ROOT / "data/grixis/m6/phase_b_plans/abaddon_certification_gap_20261022.json"
MILESTONE = ROOT / "data/grixis/milestone_m6_m7_subtracker.json"
REGISTRY = ROOT / "data/grixis/registry.json"
SOURCE = ROOT / "exports/grixis-archidekt/source-baseline/abaddon-the-despoiler.txt"
APPROVED_SHA = "2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf"


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


class AbaddonTestStageSynthesis(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d = read(REPORT)
        cls.prior = read(PRIOR)
        cls.ledger = read(LEDGER)
        cls.milestone = read(MILESTONE)
        cls.registry = read(REGISTRY)
        cls.cases = {x["card"]: x for x in cls.d["judgments"]}
        cls.old_cases = {x["card"]: x for x in cls.prior["candidates"]}

    def test_complete_named_candidate_scope_and_prior_alignment(self):
        self.assertEqual(len(self.d["judgments"]), 4)
        self.assertEqual(set(self.cases), set(self.old_cases))
        self.assertEqual(set(self.cases), {"Aggravated Assault", "Chaos Warp", "Grinning Ignus", "The Ruinous Powers"})
        for card, entry in self.cases.items():
            with self.subTest(card=card):
                self.assertFalse(self.old_cases[card]["approved_swap"])
                self.assertEqual(entry["existing_card_action"], "PRESERVE_CURRENT_BASELINE")
                self.assertTrue(entry["reason"])
                self.assertTrue(entry["rules_supported"])
                self.assertTrue(entry["reopen_only_if"])
                self.assertTrue(entry["incumbent_role_costs"])
                self.assertGreaterEqual(len(entry["evidence_paths"]), 2)
                for p in entry["evidence_paths"]:
                    self.assertTrue((ROOT / p).is_file(), p)

    def test_exact_approved_count_and_unchanged_authority(self):
        cards = []
        for row in SOURCE.read_text(encoding="utf-8").splitlines():
            qty, name = row.split(" ", 1)
            name = name.removesuffix(" [Commander]")
            cards.extend([name] * int(qty))
        self.assertEqual(len(cards), 100)
        self.assertEqual(cards.count("Abaddon the Despoiler"), 1)
        self.assertEqual(len(set(cards)), 94)
        self.assertEqual(sum(cards.count(x) for x in ("Island", "Mountain", "Swamp")), 9)
        for card in ("Rakdos, Lord of Riots", "Nightscape Familiar", "Rite of Flame", "The Lost and the Damned", "The Ruinous Powers"):
            self.assertIn(card, cards)
        for candidate in ("Aggravated Assault", "Chaos Warp", "Grinning Ignus"):
            self.assertNotIn(candidate, cards)
        self.assertEqual(self.d["canonical"]["approved_raw_sha256"], APPROVED_SHA)
        self.assertEqual(self.prior["canonical"]["raw_approved_sha256"], APPROVED_SHA)
        self.assertEqual(self.ledger["last_verified_progress"]["canonical_decks_modified"], 0)
        self.assertEqual(self.registry["decks"]["Abaddon_the_Despoiler"]["source"]["recorded_sha256"], APPROVED_SHA)

    def test_assault_verbatim_bounded_observations_not_win_claim(self):
        a = self.cases["Aggravated Assault"]
        old = self.old_cases["Aggravated Assault"]["chronological_observation"]
        self.assertEqual(a["observed"]["assault_for_rakdos_first_activation_paid"], old["assault_for_rakdos"]["first_activation_paid"])
        self.assertEqual(a["observed"]["assault_for_lost_first_activation_paid"], old["assault_for_lost"]["first_activation_paid"])
        self.assertEqual(a["observed"]["n_per_variant"], old["n_per_variant"])
        self.assertEqual(self.ledger["last_verified_progress"]["executed_neheb_assault_unit_tests"], 12)
        self.assertTrue(all(x["outcome"] == "PASS" for x in self.ledger["last_verified_progress"]["new_case_results"]))
        self.assertFalse(old["superiority_proven"])

    def test_ignus_exact_four_arm_source_bound_and_no_imputed_hit_value(self):
        a = self.cases["Grinning Ignus"]["observed"]
        b = self.old_cases["Grinning Ignus"]["factorial_hand_ramp_and_cascade_observation"]
        self.assertEqual(a["total_restricted_trajectories"], b["total_trajectories"])
        self.assertEqual(a["n_per_variant_policy_mode"], b["n_per_variant_policy_mode"])
        named = b["turn10_engine_first_both_per500"]
        self.assertEqual(a["engine_first_both_ignus_for_rakdos_any_paid_ignus_cascade"], named["ignus_for_rakdos"]["any_ignus_cascade"])
        self.assertEqual(a["engine_first_both_ignus_for_familiar_any_paid_ignus_cascade"], named["ignus_for_nightscape_familiar"]["any_ignus_cascade"])
        self.assertEqual(a["engine_first_both_ignus_for_rite_any_paid_ignus_cascade"], named["ignus_for_rite_of_flame"]["any_ignus_cascade"])
        self.assertFalse(b["superiority_proven"])
        self.assertFalse(b["full_99_spell_package_simulated"])
        self.assertFalse(b["opponents_modeled"])
        self.assertFalse(b["each_zero_mv_cascade_free_spell_cast"])

    def test_chaos_warp_reserve_policy_is_not_opponent_frequency(self):
        a = self.cases["Chaos Warp"]["observed"]
        b = self.old_cases["Chaos Warp"]["stax_answer_observation"]
        self.assertEqual(a["n_per_variant_per_policy"], b["n_per_variant_per_policy"])
        z = b["turn_10_reserve_policy"]
        self.assertEqual(a["t10_reserve_otawara_baseline_payable"], z["approved_baseline_otawara_payable"])
        for our, prior in (("rakdos", "warp_for_rakdos"), ("lost", "warp_for_lost"), ("ruinous", "warp_for_ruinous")):
            self.assertEqual(a["t10_reserve_warp_for_" + our + "_any_answer_payable"], z[prior + "_any_payable"])
        self.assertEqual(a["otawara_reservation_skipped_land_drops"], b["aggregate_land_drops_skipped_if_otawara_held_for_channel"])
        self.assertTrue(b["stax_incidence_unmeasured"])
        self.assertTrue(b["replacement_randomness_unmodeled"])

    def test_ruinous_card_identity_is_retained_and_four_mana(self):
        case = self.cases["The Ruinous Powers"]
        self.assertEqual(case["m6_test_stage_disposition"], "RETAIN_ON_COMMANDER_IDENTITY_AND_CURRENT_EVIDENCE")
        self.assertIn("Mana value four", case["rules_supported"])
        self.assertEqual(self.prior["other_pool_resolution"]["protected_engine_oracle_errata"]["ruinous"]["mana_value"], 4)
        self.assertTrue(self.prior["other_pool_resolution"]["protected_engine_oracle_errata"]["lost"]["mana_value"] == 3)

    def test_no_false_m6_certificate_or_m7_owner_approval(self):
        stage = self.d["stage_outcome"]
        self.assertEqual(stage["evaluated_named_candidates"], 4)
        self.assertEqual(stage["validated_swaps_authorized"], 0)
        self.assertTrue(stage["not_a_proof_of_optimality"])
        self.assertTrue(stage["not_a_final_M7_deck_decision"])
        self.assertTrue(stage["not_a_zero_improvement_certificate"])
        self.assertTrue(stage["not_a_multiplayer_win_rate"])
        self.assertTrue(all(value is False for value in self.d["authority"].values()))
        self.assertEqual(self.d["formal_milestone"]["M6_6"], "PARTIAL")
        self.assertEqual(self.d["formal_milestone"]["M6_7"], "PARTIAL")
        self.assertEqual(self.d["formal_milestone"]["certified_decks"], 0)
        self.assertEqual(self.milestone["m6"]["formal_m6_certified_decks"], 0)
        self.assertEqual(self.milestone["m7"]["formal_m7_review_decisions"], 0)
        self.assertEqual(self.ledger["status"], "OPEN_NOT_CERTIFIED")
        self.assertEqual(self.ledger["latest_decision_synthesis"], str(REPORT.relative_to(ROOT)))


if __name__ == "__main__":
    unittest.main()
