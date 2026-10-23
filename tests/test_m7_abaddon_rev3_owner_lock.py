"""Exact owner-approved Abaddon Rev3 receipt; no retroactive milestone acceptance."""
import hashlib
import json
import unittest
from collections import Counter
from pathlib import Path
from scripts.grixis_m7_decision_gate import parse_list, verify_packet

ROOT=Path(__file__).resolve().parents[1]
RECEIPT=ROOT/"data/grixis/m7/owner_approvals/Abaddon_the_Despoiler_rev3_20261023.json"
DECISION=ROOT/"data/grixis/m7/decision_reviews/Abaddon_the_Despoiler_rev3.json"
TRACKER=ROOT/"data/grixis/milestone_m6_m7_subtracker.json"
OLD="0d9f6df80cafc2a380199b7aec8112e4e54ccfec70024679607032cdf10f5790"
NEW="5ab1a3628352016be52233917b27ce8cbb0a538916fe757a5384cd06ad3dee24"

class AbaddonRev3OwnerLock(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.a=json.loads(RECEIPT.read_text(encoding="utf-8"))
        cls.d=json.loads(DECISION.read_text(encoding="utf-8"))
        cls.p=ROOT/cls.a["candidate_source"]
        cls.data=cls.p.read_bytes()

    def test_exact_owner_message_source_and_raw_blob(self):
        a=self.a
        self.assertIn("I explicitly approve and authorize locking Abaddon the Despoiler Rev3",
                      a["owner_response_verbatim"])
        self.assertIn(NEW,a["owner_response_verbatim"])
        self.assertEqual(a["owner_decision"],"APPROVE_EXACT_CANDIDATE")
        self.assertEqual(a["approved_raw_sha256"],NEW)
        self.assertEqual(a["replaced_prior_approved_raw_sha256"],OLD)
        self.assertEqual(hashlib.sha256(self.data).hexdigest(),NEW)
        self.assertEqual(hashlib.sha1(f"blob {len(self.data)}\0".encode()+self.data).hexdigest(),
                         a["canonical_approved_deck_git_blob_sha"])
        self.assertEqual(a["canonical_approved_deck_git_blob_sha"],
                         "13ada6e731799dc77519a907e1a3c37fc1575e6b")
        self.assertEqual(a["canonical_approval_merge_commit"],
                         "511bcb88b5b5e1dd280d74f983de62310f0ea816")
        self.assertTrue(a["canonical_verified"])
        self.assertTrue(a["post_merge_cross_repository_source_git_blob_match"])
        self.assertEqual(a["canonical_lock_status"],"LOCKED")
        self.assertEqual(a["canonical_approval_status"],"APPROVED")

    def test_approved_six_exact_and_scope(self):
        cards,commanders,companions=parse_list(self.p)
        self.assertEqual(len(cards),100)
        self.assertEqual(len(set(cards)),95)
        self.assertEqual(commanders,["Abaddon the Despoiler"])
        self.assertEqual(companions,[])
        self.assertEqual({k:v for k,v in Counter(cards).items() if v>1},
                         {"Island":3,"Mountain":2,"Swamp":3})
        self.assertEqual(self.a["source_cards"],100)
        self.assertEqual(self.a["lands"],34)
        self.assertEqual(self.a["new_swaps"],6)
        self.assertEqual(self.d["final_candidate"]["sha256"],NEW)
        self.assertEqual(verify_packet(self.d)["new_swaps"],6)
        self.assertEqual(set(self.a["new_adds"]),set(self.d["final_changes"]["adds"]))
        self.assertEqual(set(self.a["new_cuts"]),set(self.d["final_changes"]["cuts"]))
        self.assertEqual(self.a["power_bracket"],4)
        self.assertEqual(len(self.a["archidekt_tags"]),3)

    def test_still_only_two_distinct_deck_approvals(self):
        a=self.a
        t=json.loads(TRACKER.read_text(encoding="utf-8"))
        self.assertTrue(a["authority"]["m7_exact_owner_approval"])
        self.assertFalse(a["authority"]["formal_m6_milestone_accepted"])
        self.assertFalse(a["authority"]["formal_m7_milestone_accepted"])
        self.assertFalse(a["authority"]["formal_m8_milestone_accepted"])
        self.assertEqual(t["m6"]["formal_m6_certified_decks"],0)
        self.assertEqual(t["m7"]["formal_m7_review_decisions"],0)
        self.assertEqual(t["m7"]["prospective_exact_owner_approvals_recorded"],2)
        self.assertEqual(t["m7"]["gates"][0]["status"],"BLOCKED")
        self.assertEqual(t["m7"]["gates"][1]["completed"],0)
        self.assertTrue(a["post_merge_61_other_registry_records_identical"])
        self.assertTrue(a["post_merge_61_other_tracker_rows_byte_identical"])
        self.assertTrue(a["post_merge_prior_rev2_source_immutable"])
        self.assertTrue(a["post_merge_admiral_source_immutable"])

if __name__=="__main__":
    unittest.main()
