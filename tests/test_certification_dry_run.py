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
        self.assertTrue(rows["knowledge_foundation"]["blocked_by_owner"])
        self.assertTrue(rows["foundation_graph"]["blocked_by_owner"])
        self.assertNotIn("reviewed_graph_deck", rows)

    def test_foundation_packet_and_scheduled_watch_have_honest_remaining_gates(self):
        rows = {r['id']: r for r in self.d['release_definition']}
        foundation = rows['knowledge_foundation']
        self.assertNotIn('ENGINEERING_OPEN', {b['kind'] for b in foundation['blockers']})
        self.assertIn('EXTERNAL_CI', {b['kind'] for b in foundation['blockers']})
        p8 = self.d['phase8']
        watch = next(r for r in p8 if r['item'].startswith('Monitor new official stories'))
        self.assertEqual({b['kind'] for b in watch['blockers']}, {'ONGOING'})
        self.assertTrue((ROOT / '.github/workflows/multiverse-update-watch.yml').is_file())
        tracker = next(r for r in p8 if r['item'].startswith('Maintain an honest progress tracker'))
        self.assertEqual({b['kind'] for b in tracker['blockers']}, {'ONGOING'})


if __name__ == "__main__":
    unittest.main()
