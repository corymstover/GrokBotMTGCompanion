"""Owner-presentable Abaddon Rev3 must use locked Rev2, never M5 or a false approval.

The source/hash/Oracle checks are deterministic. The authored 6-vs-7
qualitative decision remains explicitly bounded; it is not a win-rate proof.
"""
import copy
import hashlib
import json
from pathlib import Path
import sys
import unittest
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import grixis_authority as ga
import grixis_m7_decision_gate as gate

PACKET = ROOT / "data/grixis/m7/decision_reviews/Abaddon_the_Despoiler_rev3.json"
CURRENT = ROOT / "data/grixis/m7/candidate_lists/Abaddon_the_Despoiler_rev2.txt"
PROPOSED = ROOT / "data/grixis/m7/candidate_lists/Abaddon_the_Despoiler_rev3.txt"
ORACLE = ROOT / "data/grixis/m6/oracle_snapshots/Abaddon_the_Despoiler_Stage17_95_Source_Reconciled_20261023.json"
RECEIPT = ROOT / "data/grixis/m7/owner_approvals/Abaddon_the_Despoiler_M7_20261022.json"
EXACT = ROOT / "data/grixis/m6/ij/adjudications/Abaddon_protected_six_stage20_20261023.json"


def parse(path):
    inventory, commanders, companions = gate.parse_list(path)
    return Counter(inventory), commanders, companions


class AbaddonRev3OwnerReadiness(unittest.TestCase):
    def packet(self):
        return json.loads(PACKET.read_text(encoding="utf-8"))

    def test_reopened_canonical_supersession_and_exact_source(self):
        packet = self.packet()
        record = json.loads(RECEIPT.read_text(encoding="utf-8"))
        actual_old = CURRENT.read_bytes()
        actual_new = PROPOSED.read_bytes()
        self.assertEqual(hashlib.sha256(actual_old).hexdigest(), record["approved_raw_sha256"])
        self.assertEqual(hashlib.sha256(actual_new).hexdigest(), packet["final_candidate"]["sha256"])
        self.assertEqual(hashlib.sha1(b"blob " + str(len(actual_old)).encode() + b"\x00" + actual_old).hexdigest(), record["canonical_approved_deck_git_blob_sha"])
        a, comm_a, comp_a = parse(CURRENT)
        b, comm_b, comp_b = parse(PROPOSED)
        self.assertEqual(sum(a.values()), sum(b.values()))
        self.assertEqual(sum(a.values()), 100)
        self.assertEqual((comm_a, comp_a), (comm_b, comp_b))
        self.assertEqual(len(b), 95)
        self.assertEqual(sum(q for n, q in b.items() if n in {"Island","Mountain","Swamp"}), 8)
        self.assertEqual(b["Mount Doom"], 1)
        self.assertEqual(Counter((b-a).elements()), Counter(packet["final_changes"]["adds"]))
        self.assertEqual(Counter((a-b).elements()), Counter(packet["final_changes"]["cuts"]))
        oracle = json.loads(ORACLE.read_text(encoding="utf-8"))["oracle_cards"]
        entries = [("commander" if name in comm_b else "main", oracle[name]["oracle_id"], q)
                   for name, q in b.items()]
        self.assertEqual(ga.logical_hash(entries), "lh1:965f298aa71b9a3f28d805ee99b2d2576913ca8ba78a0824e9aa205cc8133ceb")
        record_ij = json.loads(EXACT.read_text(encoding="utf-8"))
        self.assertEqual(record_ij["proposed_raw_sha256"], hashlib.sha256(actual_new).hexdigest())
        self.assertEqual(record_ij["proposed_lh1"], ga.logical_hash(entries))

    def test_complete_decision_gate_and_owner_separation(self):
        p = self.packet()
        result = gate.verify_packet(p, root=ROOT)
        self.assertEqual(result["status"], "M7_STRUCTURALLY_DECISION_READY_NOT_OWNER_APPROVED")
        self.assertTrue(result["owner_presentable"])
        self.assertEqual(result["new_swaps"], 6)
        self.assertEqual(result["material_candidates"], 16)
        self.assertEqual(sum(c["judgment"]=="SELECT_ADD" for c in p["material_candidates"]), 6)
        self.assertFalse(p["owner_authority"]["exact_candidate_owner_approved"])
        self.assertFalse(p["owner_authority"]["canonical_deck_changed"])
        self.assertIsNone(p["open_ended_optimization_audit"]["no_credible_larger_package_reason"])
        self.assertTrue(any(len(x["adds"])>6 for x in p["open_ended_optimization_audit"]["larger_swap_packages"]))

    def test_wrong_supersession_and_missing_post_floor_fail_closed(self):
        p = self.packet()
        forged = copy.deepcopy(p)
        forged["superseded_canonical_approval"]["canonical_live_git_blob_sha"] = "0"*40
        with self.assertRaises(gate.DecisionGateError):
            gate.verify_packet(forged, root=ROOT)
        stale = copy.deepcopy(p)
        stale["canonical_baseline_sha256"] = "2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf"
        with self.assertRaises(gate.DecisionGateError):
            gate.verify_packet(stale, root=ROOT)
        shallow = copy.deepcopy(p)
        shallow.pop("open_ended_optimization_audit")
        with self.assertRaises(gate.DecisionGateError):
            gate.verify_packet(shallow, root=ROOT)
        unauthorized = copy.deepcopy(p)
        unauthorized["owner_authority"]["exact_candidate_owner_approved"] = True
        with self.assertRaises(gate.DecisionGateError):
            gate.verify_packet(unauthorized, root=ROOT)

if __name__ == "__main__":
    unittest.main()
