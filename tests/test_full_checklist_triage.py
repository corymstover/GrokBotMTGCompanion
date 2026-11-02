"""Every Master Workflow checkbox must have a conservative explicit triage."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_full_checklist as C  # noqa: E402


class FullChecklistTriageTests(unittest.TestCase):
    def test_all_137_items_are_accounted_without_silent_completion(self):
        report = C.build()
        t = report["totals"]
        self.assertEqual(t["items"], 137)
        self.assertEqual(t["checked"] + t["open"], 137)
        self.assertEqual(sum(t["by_status"].values()), 137)
        self.assertEqual(len(report["items"]), 137)
        self.assertTrue(all(r["status"] in C.STATES and r["reason"] and r["section"] for r in report["items"]))
        self.assertTrue(all((r["status"] == "Completed") == r["checked"] for r in report["items"]))

    def test_phase6_resumes_bounded_engineering_only_after_foundation_certificate(self):
        report = C.build()
        phase = [r for r in report["items"] if r["section"].startswith("Phase 6")]
        self.assertEqual(len(phase), 10)
        self.assertEqual({r["id"] for r in phase if r["status"] == "Completed"},
                         {"K106", "K107", "K109", "K111", "K115"})
        self.assertEqual(len([r for r in phase if r["status"] != "Completed"]), 5)
        self.assertTrue(all(r["blocker_kind"] == "INDIVIDUAL_PILOT_APPROVAL_PENDING"
                            for r in phase if r["id"] in ("K112", "K113", "K114")))

    def test_owner_finish_line_excludes_pilot_signoff_and_perpetual_upkeep(self):
        report = C.build()
        t = report["totals"]
        self.assertEqual(t["remaining_repository_build"], 16)
        self.assertEqual(t["excluded_from_repository_build"], 6)
        self.assertEqual(t["post_build_pilot_reviews"], 3)
        self.assertEqual(t["recurring_maintenance"], 3)
        self.assertEqual(t["remaining_repository_build"] + t["excluded_from_repository_build"], t["open"])
        excluded = {r["id"]: r for r in report["items"]
                    if r["completion_scope"] in ("POST_BUILD_PILOT_REVIEW", "RECURRING_MAINTENANCE")}
        self.assertEqual(set(excluded), {"K105", "K112", "K113", "K114", "K125", "K126"})
        self.assertTrue(all(not r["checked"] and r["status"] != "Completed" for r in excluded.values()))
        self.assertEqual({r["id"] for r in report["items"] if r["completion_scope"] == "ACTIVE_REPOSITORY_BUILD"}
                         & set(excluded), set())
        self.assertTrue(all(r["completion_scope"] == "ACTIVE_REPOSITORY_BUILD"
                            for r in report["items"] if r["id"] in ("K108", "K110")))
        self.assertTrue(all(r["checked"] and r["completion_scope"] == "COMPLETED"
                            for r in report["items"] if r["id"] in ("K064", "K069")))

    def test_finish_line_report_does_not_present_pilot_approvals_as_build_blockers(self):
        text = C.markdown(C.build())
        self.assertIn("16 actionable build items remain", text)
        self.assertIn("Outside repository-build completion", text)
        self.assertNotIn("K112 · Blocked", text)
        self.assertIn("K112 · POST_BUILD_PILOT_REVIEW", text)

    def test_dated_json_and_human_report_are_exactly_rebuildable(self):
        report = C.build()
        self.assertEqual(C.OUT.read_text(encoding="utf-8"),
                         __import__("json").dumps(report, indent=1, ensure_ascii=False) + "\n")
        self.assertEqual(C.MD.read_text(encoding="utf-8"), C.markdown(report))


if __name__ == "__main__":
    unittest.main()
