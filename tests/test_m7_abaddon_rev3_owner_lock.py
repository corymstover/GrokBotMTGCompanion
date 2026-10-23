"""Owner-approved Abaddon Rev3 receipt: exact source bytes, lock, and milestone scope.

Canonical GitHub main was read after PR #48 merge; this test is an offline,
fail-closed authenticity check of that recorded fact, not a live network call.
"""
import hashlib
import json
from collections import Counter
from pathlib import Path
import unittest

from scripts.grixis_m7_decision_gate import parse_list

ROOT = Path(__file__).resolve().parents[1]
RECEIPT = ROOT / "data/grixis/m7/owner_approvals/Abaddon_the_Despoiler_M7_Rev3_20261023.json"
OLDER = ROOT / "data/grixis/m7/owner_approvals/Abaddon_the_Despoiler_M7_20261022.json"
DECISION = ROOT / "data/grixis/m7/decision_reviews/Abaddon_the_Despoiler_rev3.json"
CONTINUATION = ROOT / "data/grixis/m7/research_challengers/Abaddon_the_Despoiler_current_continuation_20261022.json"
TRACKER = ROOT / "data/grixis/milestone_m6_m7_subtracker.json"
EXPECTED = "5ab1a3628352016be52233917b27ce8cbb0a538916fe757a5384cd06ad3dee24"
OLD = "0d9f6df80cafc2a380199b7aec8112e4e54ccfec70024679607032cdf10f5790"
BLOB = "13ada6e731799dc77519a907e1a3c37fc1575e6b"
CANON_MERGE = "511bcb88b5b5e1dd280d74f983de62310f0ea816"

class AbaddonRev3OwnerLocked(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.a = json.loads(RECEIPT.read_text(encoding="utf-8"))
        cls.d = json.loads(DECISION.read_text(encoding="utf-8"))
        cls.c = json.loads(CONTINUATION.read_text(encoding="utf-8"))
        cls.t = json.loads(TRACKER.read_text(encoding="utf-8"))

    def test_owner_exact_100_and_git_blob(self):
        a = self.a
        data = (ROOT / a["candidate_source"]).read_bytes()
        self.assertEqual(hashlib.sha256(data).hexdigest(), EXPECTED)
        blob = hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()
        self.assertEqual(blob, BLOB)
        self.assertEqual(a["canonical_approved_deck_git_blob_sha"], BLOB)
        self.assertEqual(a["approved_raw_sha256"], EXPECTED)
        self.assertEqual(a["replaced_prior_approved_raw_sha256"], OLD)
        self.assertEqual(a["owner_decision"], "APPROVE_EXACT_CANDIDATE")
        self.assertIn("I explicitly approve and authorize locking Abaddon", a["owner_response_verbatim"])
        self.assertTrue(a["repeated_owner_authorization_same_hash"])
        self.assertEqual(a["owner_approval_date"], "2026-10-23")
        cards, commanders, companions = parse_list(ROOT / a["candidate_source"])
        self.assertEqual(len(cards), 100)
        self.assertEqual(len(set(cards)), 95)
        self.assertEqual(commanders, ["Abaddon the Despoiler"])
        self.assertEqual(companions, [])
        self.assertEqual({k:v for k,v in Counter(cards).items() if v > 1},
                         {"Island":3,"Mountain":2,"Swamp":3})

    def test_source_approval_and_predecessor_immutable(self):
        a = self.a
        d = self.d
        old = json.loads(OLDER.read_text(encoding="utf-8"))
        self.assertEqual(old["approved_raw_sha256"], OLD)
        self.assertEqual(old["canonical_approval_merge_commit"],
                         "2e5a7ee6770d4a9f16d9716e53fb2c2ef440c50d")
        self.assertEqual(d["final_candidate"]["sha256"], EXPECTED)
        self.assertEqual(a["canonical_approval_merge_commit"], CANON_MERGE)
        self.assertIn("/pull/48", a["canonical_approval_pr"])
        self.assertEqual(a["canonical_branch"], "main")
        self.assertEqual(a["canonical_approved_deck_path"],
            "refinement/decklists/Abaddon_the_Despoiler_M7_Rev3_Approved_2026-10-23.txt")
        self.assertEqual(a["canonical_approval_status"], "APPROVED")
        self.assertEqual(a["canonical_lock_status"], "LOCKED")
        self.assertTrue(a["canonical_verified"])
        self.assertEqual(len(a["canonical_exact_head_ci"]), 2)
        self.assertEqual(len(a["additions"]), 6)
        self.assertEqual(len(a["cuts"]), 6)
        self.assertEqual(a["power_bracket"], 4)
        self.assertEqual(a["archidekt_tags"], ["Cascade", "Exile Cast", "40K Chaos"])

    def test_handoff_releases_only_deck3_and_no_global_acceptance(self):
        a, c, t = self.a, self.c, self.t
        self.assertTrue(c["status"].startswith("APPROVED_LOCKED_M7_REV3"))
        self.assertFalse(c["deck3_hold"])
        self.assertTrue(c["owner_ready"])
        self.assertEqual(c["canonical_authority"]["approved_raw_sha256"], EXPECTED)
        self.assertEqual(c["canonical_authority"]["status"], "APPROVED_LOCKED_M7_REV3")
        self.assertIn("Admiral Brass, Unsinkable", c["next_action"])
        self.assertEqual(c["new_work"]["final_rev3_canonical_lock"]["canonical_pr"], 48)
        self.assertTrue(a["authority"]["m7_exact_owner_approval"])
        self.assertTrue(a["authority"]["canonical_hash_updated"])
        self.assertTrue(a["authority"]["canonical_61_other_approved_decks_untouched"])
        for key in ("formal_m6_milestone_accepted",
                    "formal_m7_milestone_accepted",
                    "formal_m8_milestone_accepted"):
            self.assertFalse(a["authority"][key])
        self.assertEqual(t["m6"]["formal_m6_certified_decks"], 0)
        self.assertEqual(t["m7"]["formal_m7_review_decisions"], 0)
        self.assertEqual(t["m7"]["prospective_exact_owner_approvals_recorded"], 2)

if __name__ == "__main__":
    unittest.main()
