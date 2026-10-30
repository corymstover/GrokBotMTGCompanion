import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import audit_pack_a_open_questions as A  # noqa: E402

REVIEW = json.loads(A.REVIEW.read_text(encoding="utf-8"))
PACK = json.loads((ROOT / REVIEW["pack_file"]).read_text(encoding="utf-8"))


class T(unittest.TestCase):
    def test_committed_review_passes(self):
        self.assertEqual(A.audit(REVIEW, PACK), [])

    def test_covers_all_non_confirmed_prime_claims(self):
        targets = {c["id"] for c in PACK["claims"] if c["grade"] in ("CANON_DISPUTED", "OPEN_QUESTION")}
        self.assertEqual(targets, {r["claim_id"] for r in REVIEW["reviews"]})

    def test_silent_grade_change_fails(self):
        r = copy.deepcopy(REVIEW)
        r["reviews"][2]["grade_after"] = "CANON_CONFIRMED"
        self.assertTrue(any("RETAIN but grade differs" in e for e in A.audit(r, PACK)))

    def test_non_wizards_evidence_fails(self):
        r = copy.deepcopy(REVIEW)
        r["reviews"][0]["evidence"].append("mtgwiki_elder_dragon_war")
        self.assertTrue(any("not a checked Wizards source" in e for e in A.audit(r, PACK)))

    def test_mislabelled_official_fails(self):
        r = copy.deepcopy(REVIEW)
        r["sources_checked"]["mtgwiki_elder_dragon_war"]["class"] = "WIZARDS_OFFICIAL"
        self.assertTrue(A.audit(r, PACK))

    def test_status_stays_preliminary(self):
        r = copy.deepcopy(REVIEW)
        r["status"] = "APPROVED"
        self.assertTrue(A.audit(r, PACK))

    def test_proposals_not_applied_to_pack(self):
        ids = {c["id"] for c in PACK["claims"]}
        self.assertFalse(ids & {p["proposal_id"] for p in REVIEW["proposed_claims_not_applied"]})
        self.assertEqual(len(PACK["claims"]), 12)


if __name__ == "__main__":
    unittest.main()
