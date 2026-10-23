"""Admiral M7 rev2: fail closed on exact staged owner candidate, open-ended audit, and candidate-specific I/J.
This does not approve the deck, mutate canon, certify M6.10 or infer global multiplayer performance.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import grixis_m7_decision_gate as gate

PACKET = ROOT / "data/grixis/m7/decision_reviews/Admiral_Beckett_Brass_rev2.json"
CANDIDATE = ROOT / "data/grixis/m7/candidate_lists/Admiral_Beckett_Brass_rev2.txt"
RESEARCH = ROOT / "data/grixis/m7/research_challengers/Admiral_Beckett_Brass_six_Wave_Palisade_draw_resilient_20261022.txt"
HISTORICAL = ROOT / "data/grixis/m7/decision_reviews/Admiral_Beckett_Brass.json"
I_CERT = ROOT / "data/grixis/m6/ij/certificates/admiral-beckett-brass-rev2.json"
J_BUNDLE = ROOT / "data/grixis/m6/ij/revision_bundles/admiral-beckett-brass-rev2.json"
HASH = "ff5f54f9f608ab0facd62fd3b79df16a0255b4dbbc12d39154a127f27bb8c000"
LOGICAL = "lh1:ea49d7981c9274e2ec51ca275312d2d01ab461490a853f049817c44bbdccfda9"


class AdmiralRevisedM7OwnerGate(unittest.TestCase):
    def test_source_and_staged_final_are_exact_and_separate_from_canon(self):
        actual = CANDIDATE.read_bytes()
        self.assertEqual(actual, RESEARCH.read_bytes())
        self.assertEqual(hashlib.sha256(actual).hexdigest(), HASH)
        self.assertEqual(actual.decode().splitlines()[0], "1x Admiral Beckett Brass [Commander]")
        p = json.loads(PACKET.read_text())
        self.assertEqual(p["final_candidate"]["sha256"], HASH)
        self.assertEqual(p["readiness"], "READY_FOR_EXACT_OWNER_APPROVAL_NOT_YET_APPROVED")
        self.assertEqual(p["final_changes"]["adds"], ["City of Brass","Departed Deckhand","Cloud Pirates","Skyship Plunderer","Broadside Bombardiers","Cosmotronic Wave"])
        self.assertEqual(len(p["final_changes"]["cuts"]), 6)
        self.assertGreaterEqual(len(p["material_candidates"]), 10)
        self.assertGreaterEqual(len({x["card"] for x in p["whole_deck_audit"]["weakest_slots"]}), 8)
        self.assertFalse(p["owner_authority"]["canonical_deck_changed"])
        self.assertFalse(p["owner_authority"]["exact_candidate_owner_approved"])
        self.assertEqual(p["owner_authority"]["owner_approval_question"], "This deck is complete. Do you approve it?")
        old = json.loads(HISTORICAL.read_text())
        self.assertEqual(old["readiness"], "RESEARCH_ONLY_WITHDRAWN_NOT_OWNER_PRESENTABLE")
        self.assertNotEqual(old["final_candidate"]["sha256"], HASH)
        result = gate.verify_packet(p)
        self.assertEqual(result["status"], "M7_STRUCTURALLY_DECISION_READY_NOT_OWNER_APPROVED")
        self.assertEqual(result["new_swaps"], 6)
        self.assertTrue(result["canonical_unchanged"])

    def test_post_floor_larger_complete_options_and_revised_ij_exact_logical(self):
        p = json.loads(PACKET.read_text())
        alts = p["open_ended_optimization_audit"]["larger_swap_packages"]
        self.assertEqual(sorted(len(x["adds"]) for x in alts), [7, 9])
        self.assertTrue(p["open_ended_optimization_audit"]["floor_not_target"])
        self.assertGreaterEqual(len(p["open_ended_optimization_audit"]["post_floor_challenges"]), 2)
        for alt in alts:
            source = ROOT / alt["path"]
            self.assertEqual(hashlib.sha256(source.read_bytes()).hexdigest(), alt["sha256"])
            cards, commanders, companions = gate.parse_list(source)
            self.assertEqual(len(cards), 100)
            self.assertEqual(commanders, ["Admiral Beckett Brass"])
            self.assertEqual(companions, [])
        i = json.loads(I_CERT.read_text())
        j = json.loads(J_BUNDLE.read_text())
        self.assertEqual(i["list_hash"], LOGICAL)
        self.assertEqual(i["certificate_status"], "pass")
        self.assertEqual(j["result_hash"], LOGICAL)
        self.assertEqual(j["bundle_status"], "complete_evidence_not_approval")
        self.assertFalse(j["authority"]["can_approve_or_lock"])


if __name__ == "__main__":
    unittest.main()
