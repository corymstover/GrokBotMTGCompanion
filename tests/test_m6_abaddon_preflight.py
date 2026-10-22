"""Adversarial tests for M6 evidence preflight; no internet or approval claims."""
from __future__ import annotations
import copy
import hashlib
import json
from pathlib import Path
import unittest
from scripts.grixis_m6_abaddon_preflight import (
    ROOT, INVENTORY, DECISION, PINNED, SNAPSHOT, PreflightFailure,
    sha, verify_prerequisites, validate_runtime
)
from scripts.grixis_m7_decision_gate import parse_list


class AbaddonM6StrictPreflight(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.inventory=json.loads((ROOT/INVENTORY).read_text())
        cls.cards={}
        cls.listings={}
        inputs={
            "baseline":cls.inventory["source_sha256"] and "exports/grixis-archidekt/source-baseline/abaddon-the-despoiler.txt",
            "engine_only":"data/grixis/m7/research_challengers/Abaddon_the_Despoiler_v2_engine_only.txt",
            "engine_answer_keeper":"data/grixis/m7/research_challengers/Abaddon_the_Despoiler_v2_engine_answer_keeper.txt",
            "engine_answer_betrayal":"data/grixis/m7/research_challengers/Abaddon_the_Despoiler_v2_engine_answer_betrayal.txt",
            "combat_answer_keeper":"data/grixis/m7/research_challengers/Abaddon_the_Despoiler_v2_combat_answer_keeper.txt",
        }
        for key,path in inputs.items():
            cards,cmd,comp=parse_list(ROOT/path)
            assert len(cards)==100 and cmd==["Abaddon the Despoiler"] and not comp
            cls.listings[key]={
                "source":path,"physical_sha256":sha(ROOT/path),"card_count":100,
                "distinct_names":len(set(cards)),"oracle_rows_covered":len(set(cards)),
                "checked":True}
            for name in cards:
                oracle=f"source-test-fixture {name}"
                cls.cards[name]={
                    "oracle_text":oracle,
                    "oracle_text_sha256":hashlib.sha256(oracle.encode()).hexdigest(),
                    "commander_legality":"legal","color_identity":[],
                    "oracle_id":"fixture-not-a-live-source"}
        cls.oracle={
            "physical_lists":cls.listings,"oracle_snapshot":cls.cards,
            "approved_canonical_raw_sha256":PINNED,
            "card_identity_count":len(cls.cards),"owner_m7_approval":False,
            "formal_m6_certificate":False,"checked_at_utc":"2026-10-22T08:18:15Z",
            "canonical_authority_mode":"SHA_PINNED_CANONICAL_BYTES_NOT_LIVE_CROSS_REPO_READ"}
        cls.p0={
            "replayed_case_count":104,"passed":104,"failed":0,
            "open_required_count":0,"open_required_p0_cases":cls.inventory["required_open"],
            "M6_6_certified":False,"owner_approved":False,
            "canonical_pinned_raw_sha256":PINNED,
            "registry_sha256":sha(ROOT/INVENTORY),
            "case_receipts":[{
                "id":row["id"],"status":"PASS","executed":1,
                "test_file":row["test_file"],"test_method":row["test_method"],
                "test_sha256":sha(ROOT/row["test_file"]),"error_messages":[]
            } for row in cls.inventory["replay_cases"]]}

    def test_expected_structural_state_unapproved_and_exact_five(self):
        self.assertEqual(len(self.cards),97)
        self.assertEqual(len(self.inventory["replay_cases"]),104)
        self.assertEqual({x["id"] for x in self.inventory["required_open"]},set())
        self.assertEqual(self.oracle["card_identity_count"],97)
        self.assertEqual(verify_prerequisites()["approved_source_sha256"],PINNED)
        ans=validate_runtime(self.oracle,self.p0)
        self.assertEqual(ans["phase_b_pass"],104)
        self.assertEqual(ans["current_identified_open_P0"],0)
        self.assertEqual(ans["current_oracle_unique_names"],97)
        self.assertFalse(ans["all_99_game_effects_modeled"])

    def test_synthetic_missing_execution_or_stealth_fail_cannot_pass(self):
        for mutate in ("lost_method","wrong_sha","silent_failure","undercount","unlisted"):
            with self.subTest(mutate=mutate):
                p0=copy.deepcopy(self.p0)
                if mutate=="lost_method":p0["case_receipts"][0]["test_method"]="Fake.test_pass"
                elif mutate=="wrong_sha":p0["case_receipts"][0]["test_sha256"]="0"*64
                elif mutate=="silent_failure":p0["case_receipts"][0]["status"]="FAIL"
                elif mutate=="undercount":p0["passed"]=43
                else:p0["case_receipts"][0]["id"]="invented_case"
                with self.assertRaises(PreflightFailure):
                    validate_runtime(self.oracle,p0)

    def test_omitted_oracle_or_nonlegal_or_unapproved_fails(self):
        for mutate in ("missing","banned","off_identity","wrong_text_hash",
                       "false_m6_cert","unchecked_card","wrong_raw_sha"):
            with self.subTest(mutate=mutate):
                oracle=copy.deepcopy(self.oracle)
                if mutate=="missing":del oracle["oracle_snapshot"]["Grinning Ignus"]
                elif mutate=="banned":oracle["oracle_snapshot"]["Grinning Ignus"]["commander_legality"]="banned"
                elif mutate=="off_identity":oracle["oracle_snapshot"]["Chaos Warp"]["color_identity"]=["G"]
                elif mutate=="wrong_text_hash":oracle["oracle_snapshot"]["Brain Freeze"]["oracle_text_sha256"]="0"*64
                elif mutate=="false_m6_cert":oracle["formal_m6_certificate"]=True
                elif mutate=="unchecked_card":oracle["physical_lists"]["baseline"]["checked"]=False
                else:oracle["approved_canonical_raw_sha256"]="0"*64
                with self.assertRaises(PreflightFailure):
                    validate_runtime(oracle,self.p0)

    def test_no_autocertification_with_all_named_p0_registered(self):
        pre=verify_prerequisites()
        self.assertIn("OWNER_EQUIVALENT_GPT6_NONINDEPENDENT_M6_5_ONLY",pre["pass_c_provenance"])
        self.assertFalse(json.loads((ROOT/DECISION).read_text())["owner_approved"])


if __name__=="__main__":
    unittest.main()
