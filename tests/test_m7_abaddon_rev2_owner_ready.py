"""Fail-closed owner-ready six-swap M7 candidate, without canonical approval.

Historical two-swap M6 I/J remain untouched. Their exact revised analogues
must independently validate against committed source bytes and Oracle identity.
"""
import copy
from collections import Counter
import hashlib
import json
from pathlib import Path
import unittest

from scripts import grixis_authority
from scripts.grixis_m6_abaddon_oracle_capture import logical_hash
from scripts.grixis_m6_bundle_check import validate_bundle, load, REGISTRY, SEALS
from scripts.grixis_m7_abaddon_rev2_live_oracle import MANIFEST, validate_portfolio
from scripts.grixis_m7_decision_gate import DecisionGateError, verify_packet

ROOT=Path(__file__).resolve().parents[1]
DIR=ROOT/"data/grixis/m7"
READY=DIR/"decision_reviews/Abaddon_the_Despoiler_rev2.json"
HISTORICAL=DIR/"decision_reviews/Abaddon_the_Despoiler.json"
EVIDENCE=DIR/"research_challengers"
I=EVIDENCE/"Abaddon_the_Despoiler_rev2_I_candidate_draft.json"
J=EVIDENCE/"Abaddon_the_Despoiler_rev2_J_bundle_draft.json"
ORACLE=ROOT/"data/grixis/m6/oracle_snapshots/Abaddon_the_Despoiler_Rev2_Scryfall_20261022.json"
SHA="0d9f6df80cafc2a380199b7aec8112e4e54ccfec70024679607032cdf10f5790"
LOGICAL="lh1:853567925301becc5b646c193795a18871c269abce1368690cca5d9bda73a0b7"

def read(p):
    return json.loads(p.read_text(encoding="utf-8"))

def evidence_check(packet):
    """A structurally READY packet must match a truly verified revised I/J."""
    result=verify_packet(packet)
    if not result["owner_presentable"] or packet["verification"]["known_hard_blockers"]:
        raise ValueError("M7 not ready or undisposed genuine blockers")
    i,j=read(I),read(J)
    if grixis_authority.validate_file(i,"zero_improvement_certificate.schema.json"):
        raise ValueError("I certificate schema invalid")
    if not validate_bundle(j,load(REGISTRY),load(SEALS)):
        raise ValueError("J bundle failed strict committed-source verification")
    snapshot=read(ORACLE)["oracle_snapshot"]
    manifest=read(MANIFEST)
    lists,_=validate_portfolio(manifest)
    physical=ROOT/packet["final_candidate"]["path"]
    raw=hashlib.sha256(physical.read_bytes()).hexdigest()
    cards=lists["six_swap_selected_research"]
    if (raw!=SHA or packet["final_candidate"]["sha256"]!=SHA
            or i["list_hash"]!=LOGICAL or j["result_hash"]!=LOGICAL
            or logical_hash(cards,snapshot)!=LOGICAL):
        raise ValueError("Selected physical 100 or I/J logical binding has drifted")
    if (i["candidate_pool"]["source_sha256"]!="sha256:"+hashlib.sha256(MANIFEST.read_bytes()).hexdigest()
            or i["candidate_pool"]["tested_pool_size"]!=4):
        raise ValueError("I local-optimum pool lacks current physical alternatives")
    selected_inputs={item["path"]:item["sha256"] for item in j["inputs"]}
    if selected_inputs.get(packet["final_candidate"]["path"])!="sha256:"+raw:
        raise ValueError("J did not hash-bind exactly the owner proposed 100")
    if (j["pass_c"]["review_class"]!="FORMAL_PASS_C_OWNER_EQUIVALENT"
            or j["pass_c"]["technically_independent"] is not False
            or j["authority"]["can_approve_or_lock"] is not False):
        raise ValueError("Pass C provenance/owner authority was misstated")
    if any(not set(snapshot[card]["color_identity"]).issubset({"U","B","R"})
           or snapshot[card]["commander_legality"]!="legal" for card in cards):
        raise ValueError("Source snapshot fails selected full-100 legality/color identity")
    if (Counter(cards)["Abaddon the Despoiler"]!=1 or len(cards)!=100
            or len(packet["final_changes"]["adds"])<5):
        raise ValueError("Commander, full physical list or owner five-swap floor lost")
    if (packet["owner_authority"]["exact_candidate_owner_approved"]
            or packet["owner_authority"]["canonical_deck_changed"]):
        raise ValueError("Only Cory may approve or lock canonical Abaddon")
    return result

class AbaddonRevisedOwnerReady(unittest.TestCase):
    def test_exact_six_swap_rev2_is_ready_for_owner_decision_not_approved(self):
        packet=read(READY)
        result=evidence_check(packet)
        self.assertEqual(result["new_swaps"],6)
        self.assertEqual(result["material_candidates"],13)
        self.assertTrue(result["canonical_unchanged"])
        self.assertEqual(packet["verification"]["power_bracket"],4)
        self.assertEqual(packet["verification"]["archidekt_tags"],
                         ["Cascade","Exile Cast","40K Chaos"])

    def test_old_two_swap_rejected_packet_remains_complete_and_withdrawn(self):
        old=read(HISTORICAL)
        self.assertEqual(old["final_candidate"]["sha256"],
                         "1fabe1251a7868838365144bf0cb1ee903d394ed90ac146b2dd9cdd45683b7dd")
        self.assertEqual(old["readiness"],"RESEARCH_ONLY_WITHDRAWN_NOT_OWNER_PRESENTABLE")
        self.assertFalse(verify_packet(old)["owner_presentable"])

    def test_forged_or_missing_source_cannot_get_owner_ready(self):
        packet=read(READY)
        for mutation in ("hash","blockers","approval","swap_count"):
            p=copy.deepcopy(packet)
            if mutation=="hash":
                p["final_candidate"]["sha256"]="0"*64
            elif mutation=="blockers":
                p["verification"]["known_hard_blockers"]=["Actual unanswered required rules issue"]
            elif mutation=="approval":
                p["owner_authority"]["exact_candidate_owner_approved"]=True
            else:
                p["final_changes"]["adds"]=p["final_changes"]["adds"][:2]
            with self.subTest(mutation=mutation), self.assertRaises((ValueError,DecisionGateError)):
                evidence_check(p)

    def test_62_canonical_approvals_and_formal_milestone_still_unmodified(self):
        tracker=read(ROOT/"data/grixis/milestone_m6_m7_subtracker.json")
        self.assertEqual(tracker["m6"]["formal_m6_certified_decks"],0)
        self.assertEqual(tracker["m7"]["formal_m7_review_decisions"],0)

if __name__=="__main__":
    unittest.main()
