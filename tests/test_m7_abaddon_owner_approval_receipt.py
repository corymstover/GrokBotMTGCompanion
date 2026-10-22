"""Explicit owner acceptance of exact M7 Abaddon bytes, not M6/M8 acceptance."""
from collections import Counter
import hashlib
import json
from pathlib import Path
import unittest

from scripts.grixis_m7_decision_gate import parse_list,verify_packet

ROOT=Path(__file__).resolve().parents[1]
RECEIPT=ROOT/"data/grixis/m7/owner_approvals/Abaddon_the_Despoiler_M7_20261022.json"
TRACKER=ROOT/"data/grixis/milestone_m6_m7_subtracker.json"
DECISION=ROOT/"data/grixis/m7/decision_reviews/Abaddon_the_Despoiler_rev2.json"
OLD_SHA="2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf"
NEW_SHA="0d9f6df80cafc2a380199b7aec8112e4e54ccfec70024679607032cdf10f5790"


class AbaddonOwnerAcceptedM7(unittest.TestCase):
    def test_explicit_owner_decision_binds_exact_physical_copy_and_github_blob(self):
        a=json.loads(RECEIPT.read_text(encoding="utf-8"))
        d=json.loads(DECISION.read_text(encoding="utf-8"))
        p=ROOT/a["candidate_source"]
        data=p.read_bytes()
        self.assertEqual(hashlib.sha256(data).hexdigest(),NEW_SHA)
        self.assertEqual(hashlib.sha1(f"blob {len(data)}\0".encode()+data).hexdigest(),
                         a["canonical_approved_deck_git_blob_sha"])
        self.assertEqual(a["approved_raw_sha256"],NEW_SHA)
        self.assertEqual(a["replaced_prior_approved_raw_sha256"],OLD_SHA)
        self.assertEqual(a["owner_response_verbatim"],"Approve")
        self.assertEqual(a["owner_decision"],"APPROVE_EXACT_CANDIDATE")
        self.assertEqual(a["canonical_approval_merge_commit"],
                         "2e5a7ee6770d4a9f16d9716e53fb2c2ef440c50d")
        cards,commanders,companions=parse_list(p)
        self.assertEqual(len(cards),100)
        self.assertEqual(commanders,["Abaddon the Despoiler"])
        self.assertEqual(companions,[])
        self.assertEqual(sum(Counter(cards)[basic] for basic in ("Island","Mountain","Swamp")),9)
        self.assertEqual(a["new_swaps"],6)
        self.assertEqual(d["final_candidate"]["sha256"],NEW_SHA)
        self.assertEqual(verify_packet(d)["new_swaps"],6)

    def test_approving_one_m7_deck_does_not_accept_entire_milestone(self):
        a=json.loads(RECEIPT.read_text(encoding="utf-8"))
        t=json.loads(TRACKER.read_text(encoding="utf-8"))
        self.assertTrue(a["authority"]["m7_exact_owner_approval"])
        self.assertFalse(a["authority"]["formal_m6_milestone_accepted"])
        self.assertFalse(a["authority"]["formal_m7_milestone_accepted"])
        self.assertFalse(a["authority"]["formal_m8_milestone_accepted"])
        self.assertEqual(t["m6"]["formal_m6_certified_decks"],0)
        self.assertEqual(t["m7"]["formal_m7_review_decisions"],0)
        self.assertEqual(t["m7"]["prospective_exact_owner_approvals_recorded"],1)
        self.assertEqual(t["m7"]["gates"][0]["status"],"BLOCKED")
        self.assertEqual(t["m7"]["gates"][1]["completed"],0)
        self.assertEqual(t["m7"]["gates"][2]["completed"],0)
        self.assertEqual(t["m7"]["gates"][5]["completed"],0)


if __name__=="__main__":
    unittest.main()
