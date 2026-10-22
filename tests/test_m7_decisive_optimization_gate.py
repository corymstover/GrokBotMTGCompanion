"""M7 62-deck final packet rules: source-backed deltas, decisions and test economy.

Uses temporary synthetic card-name fixtures exclusively to validate the gate.
These are not Abaddon simulations, Oracle verifications or approval artifacts.
"""
from __future__ import annotations
import copy
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts import grixis_m7_decision_gate as gate


STRATEGY = "This hypothetical Abaddon list advances turn-based commander-cascade identity without replacing its unique payoffs."
EVIDENCE = "Frozen candidate role audit and source-matched hypothetical case comparison, with all limitations explicitly recorded."
CANDIDATE_NAMES = ["Aggravated Assault", "Chaos Warp", "Grinning Ignus", "Stormfist Crusader", "Past in Flames"]
BASE_NAMES = ["Rakdos, Lord of Riots", "The Lost and the Damned", "The Ruinous Powers",
              "Nightscape Familiar", "Rite of Flame", "Thermo-Alchemist"]


def weak(name, proposed):
    return {"card": name, "weakness": "Situation-dependent compared with the revised commander-threshold and interaction plan.",
            "alternative_named": proposed,
            "reasoning": "The incumbent retains meaningful value; its exact lost role must be compensated by other slots."}


def candidate(name, cut, verdict):
    return {"card": name, "source": "Off-ranking archived deck candidate plus verified rules and incumbent audit.",
            "role": "Commander-aligned value, threshold acceleration or response coverage under realistic sequencing.",
            "named_cuts": [cut],
            "incumbent_opportunity_cost": "Removing the exact incumbent sacrifices a named independent role that is assessed here.",
            "commander_synergy": "Adds a complementary line without forcing a generic Grixis combo shell on Abaddon.",
            "adversarial_downside": "Can be awkward if the necessary colored mana or commander game state is disrupted.",
            "judgment": verdict,
            "reason": "Chosen or rejected by comparing the actual strategic upside against the lost incumbent functionality.",
            "confidence": "MODERATE", "evidence_refs": ["grixis/Commander-First Decisive Optimization and Test Economy Standard.md"]}


def experiment():
    return {"cluster_id": "Abaddon-Assault-vs-incumbent",
            "test_kind": "BOUNDED_COMPARATIVE_EXPERIMENT",
            "question": "Does the source-paid extra-combat mechanism improve decisive turn opportunities after lost Rakdos role costs?",
            "exact_challenger_adds": ["Aggravated Assault"],
            "exact_challenger_cuts": ["Rakdos, Lord of Riots"],
            "incumbent_effects": "Record Rakdos creature cost reductions and its conditional casting alongside baseline threshold sources.",
            "relevant_challenger_effects": "Record Assault mana-paid activation, actual new combats, and loss of incumbent creature discount.",
            "source_rules_fixture": "Exactly paid UBR mana and after-combat priority windows under a controlled source-matched board.",
            "primary_endpoint": "Real source-paid advantage of the extra combat sequence rather than merely counting printed trigger text.",
            "tradeoff_endpoint": "Creature tempo lost from cutting Rakdos plus disruption and mana-color vulnerability.",
            "choice_reversal_threshold": "A meaningful increase in repeatable, survivable damage or value after accounting for exact incumbent loss.",
            "adversarial_condition": "Opponent removes Neheb or Loyal Subordinate after the first legal triggered ability resolves.",
            "limitations": "No measured multiplayer win rate; all conclusions are limited to the declared bounded setup.",
            "why_existing_evidence_cannot_decide": "Relevant game-state effects and incumbent costs have not been compared in one identical source-paid trace.",
            "precommitted_max_runs": 12,
            "stop_rule": "One source-backed adversarial suite; decide using roles and uncertainty after the last planned case.",
            "fallback_choice_rule": "If test cannot distinguish them, select based on protected commander identity and incumbent resilience.",
            "executed": True,
            "result_summary": "The bounded case executed; interpretation is explicitly limited to legal engine operation and its vulnerabilities.",
            "execution_receipt": "https://github.com/example/repo/actions/runs/123",
            "repeat_exception_reason": None, "large_sample_justification": None}


class M7DecisionGateTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        s = self.root / "data/grixis/schemas/m7_decisive_optimization.schema.json"
        s.parent.mkdir(parents=True)
        s.write_bytes(gate.SCHEMA.read_bytes())
        self.baseline_text = "1x Abaddon the Despoiler [Commander]\n" + "".join("1x " + n + "\n" for n in BASE_NAMES) + "93x Island\n"
        path = self.root / "exports/grixis-archidekt/source-baseline/abaddon-the-despoiler.txt"
        path.parent.mkdir(parents=True)
        path.write_text(self.baseline_text)
        self.candidate_path = "data/grixis/m7/candidate_lists/Abaddon_the_Despoiler.txt"
        self.candidate_file = self.root / self.candidate_path
        self.candidate_file.parent.mkdir(parents=True)
        self.candidate_file.write_text(self.baseline_text.replace("1x Rakdos, Lord of Riots", "1x Aggravated Assault"))
        self.registry = {"decks": {
            "Abaddon_the_Despoiler": {
                "slug": "abaddon-the-despoiler",
                "source": {"recorded_sha256": "a"*64},
                "current_canonical_hash": "lh1:" + "b"*64}}}
        weak_slots = [weak(n, CANDIDATE_NAMES[i]) for i, n in enumerate(BASE_NAMES[:5])]
        candidates = [candidate(name, BASE_NAMES[i], "SELECT_ADD" if i == 0 else "REJECT")
                      for i, name in enumerate(CANDIDATE_NAMES)]
        self.packet = {
            "schema_version": 1,
            "stage": "M7_DECISIVE_OWNER_REVIEW_CANDIDATE",
            "deck_id": "Abaddon_the_Despoiler",
            "canonical_baseline_sha256": "a"*64,
            "canonical_baseline_logical_hash": "lh1:" + "b"*64,
            "commander_identity": {
                "mechanical_plan": STRATEGY,
                "protected_core": ["The Ruinous Powers"],
                "natural_ceiling": "Optimized commander-first life-loss and hand-cascade engine rather than generalized turbo-Grixis.",
                "anti_homogenization": "Retain threshold, cast-from-exile, printed-cascade and Warhammer identity payoffs."},
            "whole_deck_audit": {
                "all_noncommand_cards_reviewed": True,
                "roles_and_overlaps": EVIDENCE,
                "mana_base_and_curve": EVIDENCE,
                "interaction_resilience": EVIDENCE,
                "weakest_slots": weak_slots,
                "current_baseline_strength": STRATEGY,
                "candidate_pool_scope": EVIDENCE,
                "off_ranked_search_conclusion": EVIDENCE},
            "candidate_sources": ["M5 98-row ledger and original blueprint coverage",
                                  "Off-ranking archival and community synergy candidates"],
            "material_candidates": candidates,
            "expensive_experiments": [],
            "final_changes": {"adds": ["Aggravated Assault"], "cuts": ["Rakdos, Lord of Riots"],
                              "coherent_package_tradeoff": EVIDENCE},
            "low_swap_heightened_audit": {
                "weakest_slot_challenge": copy.deepcopy(weak_slots),
                "off_ranked_opportunities": EVIDENCE,
                "multi_slot_packages": [
                    {"adds": ["Aggravated Assault", "Chaos Warp"],
                     "cuts": ["Rakdos, Lord of Riots", "The Lost and the Damned"], "result_and_rationale": EVIDENCE},
                    {"adds": ["Grinning Ignus", "Past in Flames"],
                     "cuts": ["Nightscape Familiar", "Rite of Flame"], "result_and_rationale": EVIDENCE}],
                "no_two_package_reason": None,
                "fewer_than_five_weak_slots_reason": None,
                "alternate_cuts_for_prior_holds": EVIDENCE,
                "strongest_argument_against_baseline": EVIDENCE,
                "evidence_based_answer": EVIDENCE},
            "final_candidate": {"path": self.candidate_path,
                                "sha256": hashlib.sha256(self.candidate_file.read_bytes()).hexdigest(),
                                "card_count": 100, "deckwide_reconciliation": EVIDENCE},
            "verification": {
                "quantity_singleton_verified": True, "color_identity_verified": True,
                "current_oracle_verified": True, "official_legality_checked": True,
                "project_exceptions_recorded": True, "rules_and_combos_verified": True,
                "source_evidence_paths": [EVIDENCE], "power_bracket": 4,
                "archidekt_tags": ["Cascade", "Life Loss", "Warhammer 40K"],
                "known_hard_blockers": []},
            "owner_authority": {"canonical_deck_changed": False, "exact_candidate_owner_approved": False,
                                "owner_approval_question": "This deck is complete. Do you approve it?"},
            "readiness": "READY_FOR_EXACT_OWNER_APPROVAL_NOT_YET_APPROVED"}

    def verify(self):
        return gate.verify_packet(self.packet, root=self.root, registry=self.registry)

    def test_archived_canonical_import_tags_are_read_without_bot_refined_list(self):
        md=self.root / "grixis/decks/admiral-beckett-brass.md"
        md.parent.mkdir(parents=True)
        md.write_text(
            "# Not a source list\\n\\n"
            + "## Decklist (Archidekt import)\\n\\n"
            + "```text\\n"
            + "1x Admiral Beckett Brass [Commander{top}]\\n"
            + "1x Rakdos, Lord of Riots [Creature]\\n"
            + "98x Island [Land]\\n```\\n\\n"
            + "## Refined list (Bot cycle 39)\\n"
            + "```text\\n1x Not Canonical [Commander]\\n99x Swamp\\n```"
        )
        cards,commanders,companions=gate.parse_list(md,source_markdown=True)
        self.assertEqual(len(cards),100)
        self.assertEqual(commanders,["Admiral Beckett Brass"])
        self.assertEqual(companions,[])
        self.assertNotIn("Not Canonical",cards)

    def test_lutri_companion_is_outside_exact_100_and_only_authorized_for_pair(self):
        fixture=self.root/"data/grixis/m7/candidate_lists/synthetic-companion.txt"
        fixture.write_text("1x Bjorna, Nightfall Alchemist [Commander]\\n"
                           "1x Cecily, Haunted Mage [Commander]\\n"
                           "98x Island\\n"
                           "1x Lutri, the Spellchaser [Companion]\\n")
        cards,commanders,companions=gate.parse_list(fixture)
        self.assertEqual(len(cards),100)
        self.assertEqual(len(commanders),2)
        self.assertEqual(companions,["Lutri, the Spellchaser"])
        gate.validate_companion("Cecily__Bjorna__Lutri",companions)
        with self.assertRaises(gate.DecisionGateError):
            gate.validate_companion("Abaddon_the_Despoiler",companions)
        fixture.write_text(fixture.read_text().replace(
            "1x Lutri, the Spellchaser [Companion]",
            "1x Sol Ring [Companion]"))
        with self.assertRaises(gate.DecisionGateError):
            gate.validate_companion("Cecily__Bjorna__Lutri",gate.parse_list(fixture)[2])

    def test_canonical_source_priority_excludes_laundered_official_projection(self):
        deck={"slug":"abaddon-the-despoiler",
              "canonical_project_list":{"path":"grixis/decks/abaddon-the-despoiler.md#decklist-archidekt-import"}}
        source,is_md=gate.canonical_source(self.root,deck)
        self.assertFalse(is_md)
        self.assertEqual(source.name,"abaddon-the-despoiler.txt")
        self.assertEqual(gate.parse_list(source)[1],["Abaddon the Despoiler"])

    def test_one_swap_packet_with_five_slot_and_package_review_valid(self):
        r=self.verify()
        self.assertEqual(r["new_swaps"], 1)
        self.assertEqual(r["material_candidates"], 5)
        self.assertTrue(r["has_heightened_low_swap_audit"])
        self.assertTrue(r["canonical_unchanged"])

    def test_inconclusive_or_hold_cannot_be_final_candidate_verdict(self):
        self.packet["material_candidates"][1]["judgment"] = "INCONCLUSIVE"
        with self.assertRaises(gate.DecisionGateError):
            self.verify()

    def test_missing_heightened_low_swap_audit_is_rejected(self):
        self.packet.pop("low_swap_heightened_audit")
        with self.assertRaises(gate.DecisionGateError):
            self.verify()

    def test_missing_five_weakest_without_reason_is_rejected(self):
        self.packet["low_swap_heightened_audit"]["weakest_slot_challenge"].pop()
        with self.assertRaises(gate.DecisionGateError):
            self.verify()

    def test_extra_claimed_swap_not_in_actual_physical_list_is_rejected(self):
        self.packet["final_changes"]["adds"] = ["Aggravated Assault", "Chaos Warp"]
        self.packet["final_changes"]["cuts"] = ["Rakdos, Lord of Riots", "The Lost and the Damned"]
        with self.assertRaises(gate.DecisionGateError):
            self.verify()

    def test_missing_offranking_search_rejected_for_low_swap_count(self):
        self.packet["candidate_sources"] = ["M5 commander candidate ranking and blueprint audit."]
        with self.assertRaises(gate.DecisionGateError):
            self.verify()

    def test_expensive_test_must_be_decisive_and_finite(self):
        self.packet["expensive_experiments"] = [experiment()]
        self.assertEqual(self.verify()["expensive_experiments"], 1)
        self.packet["expensive_experiments"][0]["choice_reversal_threshold"] = ""
        with self.assertRaises(gate.DecisionGateError):
            self.verify()

    def test_beyond_2000_runs_requires_material_justification(self):
        test=experiment()
        test["precommitted_max_runs"]=20000
        self.packet["expensive_experiments"]=[test]
        with self.assertRaises(gate.DecisionGateError):
            self.verify()

    def test_repeated_substantive_tests_require_specific_exception(self):
        self.packet["expensive_experiments"]=[experiment(),experiment()]
        with self.assertRaises(gate.DecisionGateError):
            self.verify()
        self.packet["expensive_experiments"][1]["repeat_exception_reason"] = (
            "The prior model omitted a mandatory trigger that materially reverses the proposed swap judgment; "
            "the replacement test fixes the exact triggered effect and repeats no unrelated mechanics.")
        self.assertEqual(self.verify()["expensive_experiments"],2)

    def test_zero_swaps_still_requires_heightened_audit(self):
        self.candidate_file.write_text(self.baseline_text)
        self.packet["final_candidate"]["sha256"] = hashlib.sha256(self.candidate_file.read_bytes()).hexdigest()
        self.packet["final_changes"]["adds"] = []
        self.packet["final_changes"]["cuts"] = []
        self.packet["material_candidates"][0]["judgment"] = "REJECT"
        self.assertEqual(self.verify()["new_swaps"],0)

    def test_two_swaps_do_not_require_low_swap_heightened_audit(self):
        self.candidate_file.write_text(self.baseline_text
            .replace("1x Rakdos, Lord of Riots", "1x Aggravated Assault")
            .replace("1x The Lost and the Damned", "1x Chaos Warp"))
        self.packet["final_candidate"]["sha256"] = hashlib.sha256(self.candidate_file.read_bytes()).hexdigest()
        self.packet["final_changes"]["adds"] = ["Aggravated Assault", "Chaos Warp"]
        self.packet["final_changes"]["cuts"] = ["Rakdos, Lord of Riots", "The Lost and the Damned"]
        self.packet["material_candidates"][1]["judgment"] = "SELECT_ADD"
        self.packet.pop("low_swap_heightened_audit")
        self.assertEqual(self.verify()["new_swaps"], 2)

    def test_approval_and_certification_authority_stay_separate(self):
        self.packet["owner_authority"]["exact_candidate_owner_approved"] = True
        with self.assertRaises(gate.DecisionGateError):
            self.verify()
        self.packet["owner_authority"]["exact_candidate_owner_approved"] = False
        self.packet["verification"]["known_hard_blockers"] = ["not yet checked"]
        with self.assertRaises(gate.DecisionGateError):
            self.verify()

    def test_altered_candidate_hash_fails(self):
        self.packet["final_candidate"]["sha256"] = "f"*64
        with self.assertRaises(gate.DecisionGateError):
            self.verify()

    def test_same_count_but_changed_composition_cannot_escape_named_deltas(self):
        self.candidate_file.write_text(self.candidate_file.read_text()
            .replace("1x The Ruinous Powers", "1x Mystical Tutor"))
        self.packet["final_candidate"]["sha256"] = hashlib.sha256(self.candidate_file.read_bytes()).hexdigest()
        with self.assertRaises(gate.DecisionGateError):
            self.verify()


if __name__ == "__main__":
    unittest.main()
