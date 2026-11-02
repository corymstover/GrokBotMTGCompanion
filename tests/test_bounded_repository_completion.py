"""Owner-scoped completion may never upgrade UNKNOWN facts or approve pilots."""
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_bounded_repository_completion as A


class BoundedRepositoryCompletionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = A.build()

    def corrupt(self, key, change, message):
        files = {"scope": A.SETS / "phase1b_release_scope_story_bridge_2026-10-29.json",
                 "draft": A.SETS / "draft_starter_primary_audit_2026-10-29.json",
                 "boxed": A.SETS / "boxed_precon_source_audit_2026-10-29.json",
                 "dispositions": A.RELEASE / "pack_a_genealogy_owner_dispositions_2026-11-01.json",
                 "chronology": A.LORE / "relative_chronology_2026-10-30.json",
                 "story_coverage": A.LORE / "story_coverage_inventory_2026-10-30.json",
                 "rules": A.RELEASE / "lookup_rules_scope_review_2026-11-01.json",
                 "strategy": A.RELEASE / "phase6_strategy_preflight_2026-11-01.json"}
        d = json.loads(files[key].read_text(encoding="utf-8"))
        change(d)
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / files[key].name
            path.write_text(json.dumps(d), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, message):
                A.build({key: path})

    def test_exact_owner_redefinition_and_preserved_unknowns(self):
        r = self.report
        self.assertEqual(r["schema"], "owner-redefined-bounded-repository-completion/v1")
        self.assertIn("NOT_UNIVERSAL_CANON", r["status"])
        self.assertEqual(len(r["gates"]), 14)
        self.assertEqual({x["id"] for x in r["gates"]}, set(A.GATES))
        self.assertEqual(r["counts"]["historical_checked"], 131)
        self.assertEqual(r["counts"]["historical_open_owner_exclusions"], 6)
        self.assertEqual(r["counts"]["active_repository_build_remaining"], 0)
        self.assertTrue(r["three_pilot_proposals_still_unapproved"])
        self.assertTrue(r["protected_grixis_digests_unchanged"])
        self.assertEqual(r["deferred_post_build_pilot_reviews"], ["K112", "K113", "K114"])
        self.assertEqual(len(r["not_certified"]), 7)
        self.assertLess(r["counts"]["chronology_known_pairs"], r["counts"]["chronology_total_pairs"])

    def test_foreign_border_cannot_be_pretended_official(self):
        self.corrupt("scope", lambda x: x["set_scope_records"]["fbb"].update(
            scope_evidence="Wizards_release_enumeration"), "foreign-border uncertainty")

    def test_draft_exception_cannot_disappear(self):
        self.corrupt("draft", lambda x: x["draft_starter_pending_codes"].remove("itp"),
                     "draft/starter primary-source exception")

    def test_boxed_exception_cannot_disappear(self):
        self.corrupt("boxed", lambda x: x["remaining_source_pending_queue"].__setitem__(
            next(i for i, r in enumerate(x["remaining_source_pending_queue"]) if r["code"] == "rqs"),
            {"code": "not_rqs"}), "boxed regional primary-source exception")

    def test_genealogy_cannot_be_promoted_to_canon(self):
        self.corrupt("dispositions", lambda x: x.update(canon_claims_promoted=1),
                     "unresolved genealogy/owner decision")

    def test_partial_chronology_not_falsely_closed(self):
        self.corrupt("chronology", lambda x: x["l244_closure"].update(closes_l244=True),
                     "partial chronology wrongly treated")

    def test_partial_story_source_coverage_not_falsely_exhaustive(self):
        self.corrupt("story_coverage", lambda x: x["totals"].update(arcs_partial=0),
                     "partial source coverage")

    def test_current_rules_not_claimed_verified(self):
        self.corrupt("rules", lambda x: x.update(
            post_bulletin_rulebreaker_and_meld_current_verdict="CERTIFIED"),
            "unverified current Commander rule")

    def test_pilot_approval_not_inferred_from_strategies(self):
        self.corrupt("strategy", lambda x: x["pilots"][0].update(
            approval_flags_all_false=False), "pilot strategy limitation")

    def test_stale_certificate_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "stale.json"
            path.write_text("{}\n", encoding="utf-8")
            with patch.object(A, "OUT", path):
                with self.assertRaisesRegex(ValueError, "stale"):
                    A.main(["--check"])


if __name__ == "__main__":
    unittest.main()
