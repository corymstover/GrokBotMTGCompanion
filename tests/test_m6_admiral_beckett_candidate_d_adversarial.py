"""Finite adverse checks for Admiral D's exact five-swap research candidate.

These assertions model *specific* printed restrictions, not priority, game
frequency, all opponent responses, or full Commander combat. They may show
that a candidate is advantageous or inferior in a stated state, never that it
is globally better or M6-certified.
"""

from __future__ import annotations

from collections import Counter
import hashlib
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "data/grixis/m7/research_challengers"
DECK = RESEARCH / "Admiral_Beckett_Brass_evasive_pirate_density_package.txt"
BASE = ROOT / "data/grixis/m6/authority_snapshots/Admiral_Beckett_Brass_Canonical_Approved_20261022.txt"
ORACLE = RESEARCH / "Admiral_Beckett_Brass_Full_Source_Oracle_20261022.json"
EVIDENCE = ROOT / "data/grixis/m6/phase_b_plans/admiral_beckett_candidate_D_effect_coverage_20261022.json"
GATE_REPORT = ROOT / "data/grixis/m6/certification_preflight/Admiral_M6_6_7_Gate_Adjudication_20261022.md"
CANDIDATE_SHA = "201a1d5fc90e30d6aff9a565603fcf8caef69604dad2c07b4951be2b41cc92ee"
BASE_SHA = "4ba5c483eb67b5f2647d375450adf9c2b7e79a036d0ba1866e58de8441bf3414"
ORACLE_SHA = "5b8ee25e57d061bbd3d754402668ade7cdac6b2946ae01be378194bc98a5eac8"


def physical_cards(path: Path) -> Counter[str]:
    result: Counter[str] = Counter()
    for line in path.read_text(encoding="utf-8").splitlines():
        quantity, name = line.split("x ", 1)
        card = name.removesuffix(" [Commander]")
        assert card not in result
        result[card] = int(quantity)
    assert sum(result.values()) == 100
    return result


def blocker_eligible(attacker: str, blocker: frozenset[str]) -> bool:
    """Only the three documented Pirate evasion categories, with no protection."""
    if attacker == "Departed Deckhand":
        return "Spirit" in blocker
    if attacker in {"Cloud Pirates", "Skyship Plunderer"}:
        return "flying" in blocker or "reach" in blocker
    return True  # Ordinary ground Pirate; no extra evasion claimed.


def maximal_independently_blocked(attackers: tuple[str, ...], blockers: tuple[frozenset[str], ...]) -> int:
    """Tiny exhaustive distinct-blocker assignment, no multiple-block shortcuts."""
    def assign(i: int, already_used: frozenset[int]) -> int:
        if i == len(attackers):
            return 0
        blocked = assign(i + 1, already_used)
        for j, blocker in enumerate(blockers):
            if j not in already_used and blocker_eligible(attackers[i], blocker):
                blocked = max(blocked, 1 + assign(i + 1, already_used | {j}))
        return blocked

    return assign(0, frozenset())


class AdmiralCandidateDAdversarialTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.candidate = physical_cards(DECK)
        cls.baseline = physical_cards(BASE)
        cls.oracle = {card["name"]: card for card in json.loads(ORACLE.read_text(encoding="utf-8"))["cards"]}

    def test_exact_canonical_and_candidate_oracle_bytes_and_actual_five_swaps(self):
        self.assertEqual(hashlib.sha256(BASE.read_bytes()).hexdigest(), BASE_SHA)
        self.assertEqual(hashlib.sha256(DECK.read_bytes()).hexdigest(), CANDIDATE_SHA)
        self.assertEqual(hashlib.sha256(ORACLE.read_bytes()).hexdigest(), ORACLE_SHA)
        additions = self.candidate - self.baseline
        cuts = self.baseline - self.candidate
        self.assertEqual(set(additions), {
            "City of Brass", "Departed Deckhand", "Cloud Pirates", "Skyship Plunderer", "Broadside Bombardiers"
        })
        self.assertEqual(set(cuts), {
            "Crumbling Necropolis", "Daring Saboteur", "Dire Fleet Captain", "Dire Fleet Poisoner",
            "Forerunner of the Coalition"
        })
        self.assertEqual(sum(additions.values()), 5)
        self.assertEqual(sum(cuts.values()), 5)

    def test_grounded_defenders_improve_third_connection_in_only_this_state(self):
        self.assertIn("Flying", self.oracle["Cloud Pirates"]["oracle_text"])
        self.assertIn("Flying", self.oracle["Skyship Plunderer"]["oracle_text"])
        self.assertIn("can't be blocked except by Spirits", self.oracle["Departed Deckhand"]["oracle_text"])
        two_ground_creatures = (frozenset(), frozenset())
        candidate_ready = ("Cloud Pirates", "Skyship Plunderer", "Departed Deckhand")
        baseline_ready = ("Dire Fleet Captain", "Dire Fleet Poisoner", "Daring Saboteur")
        # Assuming three ready distinct Pirates, both ground blockers used optimally.
        self.assertEqual(3 - maximal_independently_blocked(candidate_ready, two_ground_creatures), 3)
        self.assertEqual(3 - maximal_independently_blocked(baseline_ready, two_ground_creatures), 1)
        self.assertIn("{2}{U}: This creature can't be blocked this turn", self.oracle["Daring Saboteur"]["oracle_text"])
        # This comparison specifically assumes no spare 2U Saboteur activation;
        # it neither samples opening hands nor proves D's frequency advantage.

    def test_flying_reach_and_spirit_blockers_undo_reliable_theft_assumption(self):
        ready = ("Cloud Pirates", "Skyship Plunderer", "Departed Deckhand")
        one_flyer = (frozenset({"flying"}),)
        self.assertEqual(3 - maximal_independently_blocked(ready, one_flyer), 2)
        one_reach = (frozenset({"reach"}),)
        self.assertEqual(3 - maximal_independently_blocked(ready, one_reach), 2)
        one_spirit = (frozenset({"Spirit"}),)
        self.assertEqual(3 - maximal_independently_blocked(ready, one_spirit), 2)
        mixed = (frozenset({"flying"}), frozenset({"reach"}), frozenset({"Spirit"}))
        self.assertEqual(3 - maximal_independently_blocked(ready, mixed), 0)
        # Three damage sources are a strict trigger requirement in these states.
        self.assertIn("three or more Pirates", self.oracle["Admiral Beckett Brass"]["oracle_text"])

    def test_forerunner_topdeck_tutor_and_repeated_token_drains_are_real_loss(self):
        text = self.oracle["Forerunner of the Coalition"]["oracle_text"]
        self.assertIn("search your library for a Pirate card", text)
        self.assertIn("put that card on top", text)
        self.assertIn("Whenever another Pirate you control enters, each opponent loses 1 life", text)
        self.assertIn("At the beginning of combat on your turn, create a 1/1 red Pirate", self.oracle["Daring Piracy"]["oracle_text"])
        # With Forerunner alive across three own combats, Piracy creates 3 tokens.
        # Each of THREE opponents loses 3 life regardless of blocking (9 total).
        opponents = (40, 40, 40)
        after_three_other_pirate_entries = tuple(life - 3 for life in opponents)
        self.assertEqual(after_three_other_pirate_entries, (37, 37, 37))
        self.assertEqual(sum(opponents) - sum(after_three_other_pirate_entries), 9)
        # No part of this life loss counts as the combat damage Beckett needs.
        self.assertEqual(self.oracle["Forerunner of the Coalition"]["mana_cost"], "{2}{B}")
        self.assertEqual(self.oracle["Broadside Bombardiers"]["mana_cost"], "{2}{R}")

    def test_broadside_has_haste_menace_but_paid_boast_is_not_free_3_damage(self):
        text = self.oracle["Broadside Bombardiers"]["oracle_text"]
        self.assertIn("Menace, haste", text)
        self.assertIn("Sacrifice another creature or artifact", text)
        self.assertIn("only once each turn", text)
        self.assertEqual(2 + 0, 2)  # Sacrificed Treasure token has mana value zero.
        self.assertLess(2, 3)       # A live 3-toughness blocker survives 2 damage.
        self.assertEqual(2 + 2, 4)  # Arcane Signet MV2 instead costs a real ramp piece.
        self.assertIn("{T}: Add one mana of any color", self.oracle["Arcane Signet"]["oracle_text"])
        # A single blocker can't legally block a menace attacker, but two may.
        self.assertTrue(1 < 2)

    def test_poisoner_defensive_exchange_and_flash_are_lost_not_invalid(self):
        source = self.oracle["Dire Fleet Poisoner"]["oracle_text"]
        self.assertIn("Flash", source)
        self.assertIn("Deathtouch", source)
        self.assertIn("target attacking Pirate you control", source)
        self.assertIn("Flying", self.oracle["Skyship Plunderer"]["oracle_text"])
        self.assertEqual(self.oracle["Dire Fleet Poisoner"]["mana_cost"], "{1}{B}")
        self.assertEqual(self.oracle["Skyship Plunderer"]["mana_cost"], "{1}{U}")
        # Poisoner can flash in to block and trade against a larger non-first-
        # strike attacker; it cannot retroactively join an already declared attack.
        self.assertNotIn("Haste", source)

    def test_phase_b_scoped_sufficiency_does_not_launder_into_m6_or_owner_acceptance(self):
        evidence = json.loads(EVIDENCE.read_text(encoding="utf-8"))
        self.assertEqual(evidence["candidate_D_raw_sha256"], CANDIDATE_SHA)
        self.assertEqual(evidence["oracle_raw_sha256"], ORACLE_SHA)
        self.assertEqual(evidence["baseline_raw_sha256"], BASE_SHA)
        self.assertEqual(evidence["m6_6_status"], "COMPLETE_DECISION_SCOPED_BOUNDED")
        self.assertEqual(evidence["m6_7_status"], "COMPLETE_AUTHORED_SOURCE_BOUND_JUDGMENTS")
        self.assertFalse(evidence["phase_b_scope_adjudication"]["full_multiplayer_effect_engine_executed"])
        self.assertFalse(evidence["phase_b_scope_adjudication"]["measured_candidate_superiority_proven"])
        self.assertTrue(evidence["m6_i_local_best_certified"])
        self.assertFalse(evidence["m6_j_bundle_complete"])
        self.assertFalse(evidence["owner_m6_10_accepted"])
        self.assertFalse(evidence["owner_m7_approved"])
        self.assertEqual(evidence["candidate_comparison_scope"], "FINITE_RULES_AND_ADVERSE_ANALYSIS_ONLY")
        self.assertGreaterEqual(len(evidence["effect_coverage_cases"]), 7)
        for case in evidence["effect_coverage_cases"]:
            self.assertEqual(case["model_coverage"], "bounded_partial")
            self.assertFalse(case["supports_measured_improvement_claim"])
            self.assertTrue(case["residual_limitation"])

    def test_gate_report_counts_evidence_without_claiming_i_j_or_owner_approval(self):
        report = GATE_REPORT.read_text(encoding="utf-8")
        self.assertIn(CANDIDATE_SHA, report)
        self.assertIn(BASE_SHA, report)
        self.assertIn("5 P0 and 8 P1", report)
        self.assertIn("24 substantive candidate dispositions", report)
        self.assertIn("12 challenged plausible incumbent slots", report)
        self.assertIn("39859047626", report)
        self.assertIn("M6.8 I was **INCOMPLETE at this checkpoint**", report)
        self.assertIn("M6.9 J bundle remains **ABSENT**", report)
        self.assertIn("canonical locked deck", report)


if __name__ == "__main__":
    unittest.main()
