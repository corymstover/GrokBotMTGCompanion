"""Batch 14 Phase 8: the certification dry run lists blockers for every unchecked box and certifies nothing."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import certification_dry_run as C  # noqa: E402


class DryRunTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d = C.dry_run()

    def test_no_problems_and_committed_copy_matches(self):
        self.assertEqual(self.d["problems"], [])
        self.assertEqual(json.loads(C.OUT.read_text(encoding="utf-8")), self.d)

    def test_covers_every_release_and_phase8_item(self):
        self.assertEqual(len(self.d["release_definition"]), len(C.section_items(r"## Definition of the first major Companion release")))
        self.assertEqual(len(self.d["phase8"]), len(C.section_items(r"## Phase 8")))

    def test_every_unchecked_box_names_a_blocker(self):
        for r in self.d["release_definition"] + self.d["phase8"]:
            if not r["workflow_checked"]:
                self.assertTrue(r["blockers"], r)

    def test_certifies_nothing(self):
        self.assertEqual(self.d["status"], "DRY_RUN_NOT_CERTIFICATION")
        self.assertNotEqual(self.d["readiness_verdict"], "RELEASE_READY")
        src = (ROOT / "scripts/certification_dry_run.py").read_text(encoding="utf-8")
        self.assertNotIn("write_text(text.replace", src)
        self.assertNotIn("WORKFLOW.write", src)

    def test_owner_gated_items_are_marked(self):
        rows = {r["id"]: r for r in self.d["release_definition"]}
        self.assertFalse(rows["knowledge_foundation"]["blocked_by_owner"])
        self.assertFalse(rows["foundation_graph"]["blocked_by_owner"])
        self.assertEqual(rows["knowledge_foundation"]["machine_status"], "MET")
        self.assertEqual(rows["foundation_graph"]["machine_status"], "MET")
        self.assertEqual(rows["grixis_no_regression"]["blockers"], [])
        self.assertEqual(rows["ci_and_coverage"]["blockers"], [])
        self.assertNotIn("reviewed_graph_deck", rows)

    def test_foundation_packet_and_scheduled_watch_have_honest_remaining_gates(self):
        rows = {r['id']: r for r in self.d['release_definition']}
        foundation = rows['knowledge_foundation']
        self.assertNotIn('ENGINEERING_OPEN', {b['kind'] for b in foundation['blockers']})
        self.assertEqual(foundation['blockers'], [])
        self.assertEqual(rows['ci_and_coverage']['blockers'], [])
        self.assertTrue((ROOT / 'data/release/foundation_milestone_certificate_2026-11-01.json').is_file())
        p8 = self.d['phase8']
        self.assertFalse(any(r['item'].startswith('Monitor new official stories') for r in p8))
        self.assertFalse(any(r['item'].startswith('Rebuild and reconcile the Phase 1B') for r in p8))
        self.assertIn('K125', (ROOT / 'docs/archive/RECURRING_CHECKLIST_ITEMS_2026-11-02.md').read_text(encoding='utf-8'))
        self.assertTrue((ROOT / '.github/workflows/multiverse-update-watch.yml').is_file())
        tracker = next(r for r in p8 if r['item'].startswith('Maintain an honest progress tracker'))
        self.assertEqual({b['kind'] for b in tracker['blockers']}, {'ONGOING'})


if __name__ == "__main__":
    unittest.main()
