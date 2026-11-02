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

    def test_dated_json_and_human_report_are_exactly_rebuildable(self):
        report = C.build()
        self.assertEqual(C.OUT.read_text(encoding="utf-8"),
                         __import__("json").dumps(report, indent=1, ensure_ascii=False) + "\n")
        self.assertEqual(C.MD.read_text(encoding="utf-8"), C.markdown(report))


if __name__ == "__main__":
    unittest.main()
