"""Source-bound Admiral M7 explicit owner receipt; preserve historical packet provenance."""
from collections import Counter
import hashlib
import json
from pathlib import Path
import unittest

from scripts.grixis_m7_decision_gate import parse_list, verify_packet

ROOT=Path(__file__).resolve().parents[1]
RECEIPT=ROOT/"data/grixis/m7/owner_approvals/Admiral_Beckett_Brass_M7_20261022.json"
CANDIDATE=ROOT/"data/grixis/m7/candidate_lists/Admiral_Beckett_Brass_rev2.txt"
DECISION=ROOT/"data/grixis/m7/decision_reviews/Admiral_Beckett_Brass_rev2.json"
TRACKER=ROOT/"data/grixis/milestone_m6_m7_subtracker.json"
LEDGER=ROOT/"data/grixis/m7/research_challengers/Admiral_Beckett_Brass_current_continuation_20261022.json"
NEW_SHA="ff5f54f9f608ab0facd62fd3b79df16a0255b4dbbc12d39154a127f27bb8c000"
OLD_SHA="4ba5c483eb67b5f2647d375450adf9c2b7e79a036d0ba1866e58de8441bf3414"


class AdmiralM7OwnerApprovalReceipt(unittest.TestCase):
    def test_exact_source_and_owner_boundary(self):
        receipt=json.loads(RECEIPT.read_text(encoding="utf-8"))
        decision=json.loads(DECISION.read_text(encoding="utf-8"))
        self.assertEqual(receipt["owner_response_verbatim"],"Approved")
        self.assertEqual(receipt["owner_decision"],"APPROVE_EXACT_CANDIDATE")
        self.assertEqual(receipt["owner_approval_date"],"2026-10-22")
        self.assertEqual(receipt["approved_raw_sha256"],NEW_SHA)
        self.assertEqual(receipt["replaced_prior_approved_raw_sha256"],OLD_SHA)
        self.assertEqual(receipt["canonical_approval_merge_commit"],"51175f42db559bf161efc0e043a3f2f8d7e1d0d5")
        self.assertEqual(receipt["canonical_approved_deck_git_blob_sha"],"7f5624abc938b097820913c9278fd85fb4771c7e")
        self.assertEqual(hashlib.sha256(CANDIDATE.read_bytes()).hexdigest(),NEW_SHA)
        cards,commanders,companions=parse_list(CANDIDATE)
        self.assertEqual(len(cards),100)
        self.assertEqual(commanders,["Admiral Beckett Brass"])
        self.assertEqual(companions,[])
        self.assertEqual(sum(Counter(cards)[basic] for basic in ("Island","Mountain","Swamp")),6)
        self.assertEqual(receipt["new_swaps"],6)
        self.assertEqual(receipt["new_material_candidate_judgments"],28)
        self.assertEqual(receipt["challenged_plausible_incumbent_roles"],16)
        self.assertEqual(receipt["complete_larger_researched_100_card_alternative_swaps"],[7,9])
        self.assertEqual(decision["final_candidate"]["sha256"],NEW_SHA)
        self.assertEqual(verify_packet(decision)["new_swaps"],6)
        # Historical staged packets were not approved at their creation; the
        # actual later owner decision lives in the immutable separate receipt.
        self.assertFalse(decision["owner_authority"]["exact_candidate_owner_approved"])

    def test_canonical_owner_receipt_is_not_milestone_acceptance(self):
        r=json.loads(RECEIPT.read_text(encoding="utf-8"))
        t=json.loads(TRACKER.read_text(encoding="utf-8"))
        l=json.loads(LEDGER.read_text(encoding="utf-8"))
        self.assertTrue(r["authority"]["m7_exact_owner_approval"])
        self.assertFalse(r["authority"]["formal_m6_milestone_accepted"])
        self.assertFalse(r["authority"]["formal_m7_milestone_accepted"])
        self.assertFalse(r["authority"]["formal_m8_milestone_accepted"])
        self.assertEqual(l["m7_status"],"M7_EXACT_OWNER_APPROVED_CANONICAL_LOCKED")
        self.assertEqual(l["canonical_authority"]["approved_raw_sha256"],NEW_SHA)
        self.assertEqual(l["owner_sequence_override"]["active_commander"],"Abaddon_the_Despoiler")
        self.assertTrue(l["owner_sequence_override"]["deck3_hold"])
        self.assertEqual(t["m6"]["formal_m6_certified_decks"],0)
        self.assertEqual(t["m7"]["formal_m7_review_decisions"],0)
        self.assertEqual(t["m7"]["prospective_exact_owner_approvals_recorded"],2)
        self.assertEqual(t["m7"]["gates"][0]["status"],"BLOCKED")
        self.assertEqual(t["m7"]["gates"][1]["completed"],0)
        self.assertEqual(t["m7"]["gates"][2]["completed"],0)
        self.assertEqual(t["m7"]["gates"][5]["completed"],0)


if __name__=="__main__":
    unittest.main()
