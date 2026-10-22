"""Strict source-specific I/J review for the revised six-swap Abaddon pool.

Candidate-limited reproducibility does not accept M6.10, make a third-model
review independent, or approve and rewrite the canonical owner list.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path
import unittest

from scripts import grixis_authority as ga
from scripts.grixis_m6_bundle_check import validate_bundle,load,REGISTRY,SEALS
from scripts.grixis_m6_abaddon_oracle_capture import logical_hash
from scripts.grixis_m7_abaddon_rev2_live_oracle import MANIFEST,validate_portfolio
from scripts.grixis_m7_decision_gate import DecisionGateError,verify_packet

ROOT = Path(__file__).resolve().parents[1]
REV2 = ROOT / "data/grixis/m7/research_challengers/"
I_FILE=REV2/"Abaddon_the_Despoiler_rev2_I_candidate_draft.json"
J_FILE=REV2/"Abaddon_the_Despoiler_rev2_J_bundle_draft.json"
M7_FILE=REV2/"Abaddon_the_Despoiler_rev2_M7_schema_draft.json"
ORACLE=ROOT/"data/grixis/m6/oracle_snapshots/Abaddon_the_Despoiler_Rev2_Scryfall_20261022.json"
SELECTED_RAW="0d9f6df80cafc2a380199b7aec8112e4e54ccfec70024679607032cdf10f5790"
SELECTED_LOGICAL="lh1:853567925301becc5b646c193795a18871c269abce1368690cca5d9bda73a0b7"


class AbaddonSixSwapSourceBoundIJ(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest=json.loads(MANIFEST.read_text(encoding="utf-8"))
        cls.cards,_=validate_portfolio(cls.manifest)
        cls.oracle=json.loads(ORACLE.read_text(encoding="utf-8"))["oracle_snapshot"]
        cls.i=json.loads(I_FILE.read_text(encoding="utf-8"))
        cls.j=json.loads(J_FILE.read_text(encoding="utf-8"))
        cls.m7=json.loads(M7_FILE.read_text(encoding="utf-8"))

    def test_new_i_schema_valid_and_strictly_candidate_bound(self):
        self.assertEqual(ga.validate_file(self.i,"zero_improvement_certificate.schema.json"),[])
        self.assertEqual(self.i["list_hash"],SELECTED_LOGICAL)
        self.assertEqual(self.i["certificate_status"],"pass")
        self.assertEqual(self.i["candidate_pool"]["tested_pool_size"],4)
        pool=self.i["candidate_pool"]["source_ref"]
        self.assertEqual(pool,str(MANIFEST.relative_to(ROOT)))
        self.assertEqual(self.i["candidate_pool"]["source_sha256"],
                         "sha256:"+hashlib.sha256(MANIFEST.read_bytes()).hexdigest())
        self.assertEqual(logical_hash(self.cards["six_swap_selected_research"],self.oracle),SELECTED_LOGICAL)
        self.assertIn("tests/test_m6_abaddon_rev2_new_effects_p0.py",self.i["phase_b"]["test_refs"])
        self.assertIn("https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/39833569544",self.i["phase_b"]["test_refs"])
        self.assertIs(self.i["authority"]["can_approve_or_lock"],False)
        self.assertIs(self.i["authority"]["can_decide"],False)

    def test_new_j_validates_hashed_seals_waived_nonindependent_pass_c_and_oracle(self):
        self.assertIs(validate_bundle(self.j,load(REGISTRY),load(SEALS)),True)
        self.assertEqual(self.j["result_hash"],SELECTED_LOGICAL)
        self.assertEqual(self.j["snapshot"]["oracle_ref"],str(ORACLE.relative_to(ROOT)))
        self.assertEqual(self.j["snapshot"]["legality_ref"],str(ORACLE.relative_to(ROOT)))
        refs={x["path"] for x in self.j["inputs"]}
        self.assertIn("data/grixis/m7/candidate_lists/Abaddon_the_Despoiler_rev2.txt",refs)
        self.assertIn("data/grixis/m7/research_challengers/Abaddon_the_Despoiler_rev2_six_swap_manifest.json",refs)
        self.assertEqual(len(self.j["phase_b"]["tests"]),4)
        self.assertFalse(any(x["supports_improvement_claim"] for x in self.j["phase_b"]["tests"]))
        self.assertTrue(all(x["effect_coverage"]=="bounded_partial" for x in self.j["phase_b"]["tests"]))
        self.assertEqual(self.j["pass_c"]["review_class"],"FORMAL_PASS_C_OWNER_EQUIVALENT")
        self.assertIs(self.j["pass_c"]["technically_independent"],False)

    def test_source_candidate_is_exact_100_with_six_genuine_selected_swaps(self):
        staging=ROOT/"data/grixis/m7/candidate_lists/Abaddon_the_Despoiler_rev2.txt"
        self.assertEqual(hashlib.sha256(staging.read_bytes()).hexdigest(),SELECTED_RAW)
        self.assertEqual(self.m7["final_candidate"]["sha256"],SELECTED_RAW)
        self.assertEqual(set(self.m7["final_changes"]["adds"]),
                         {x["card"] for x in self.m7["material_candidates"] if x["judgment"]=="SELECT_ADD"})
        self.assertEqual(len(self.m7["final_changes"]["adds"]),6)
        self.assertGreaterEqual(len(self.m7["material_candidates"]),10)
        self.assertGreaterEqual(len(self.m7["whole_deck_audit"]["weakest_slots"]),8)
        self.assertEqual(len(self.m7["low_swap_heightened_audit"]["multi_slot_packages"]),2)

    def test_owner_packet_remains_fail_closed_until_final_ij_adoption(self):
        # The research draft deliberately records hard adoption/certification
        # blockers, so generic M7 READY validation must continue to reject it.
        with self.assertRaisesRegex(DecisionGateError,"known_hard_blockers"):
            verify_packet(self.m7)
        self.assertEqual(self.m7["readiness"],"RESEARCH_ONLY_WITHDRAWN_NOT_OWNER_PRESENTABLE")
        self.assertIs(self.m7["owner_authority"]["exact_candidate_owner_approved"],False)
        self.assertTrue(self.m7["verification"]["known_hard_blockers"])

    def test_no_milestone_or_canonical_m7_approval_inferred(self):
        tracker=json.loads((ROOT/"data/grixis/milestone_m6_m7_subtracker.json").read_text(encoding="utf-8"))
        self.assertEqual(tracker["m6"]["formal_m6_certified_decks"],0)
        self.assertEqual(tracker["m7"]["formal_m7_review_decisions"],0)
        self.assertIs(self.j["authority"]["can_approve_or_lock"],False)
        self.assertEqual(self.i["scope_caveat"],
                         "Local optimum over the explicitly tested candidate pool only; not a mathematical or global proof of optimality.")


if __name__ == "__main__":
    unittest.main()
