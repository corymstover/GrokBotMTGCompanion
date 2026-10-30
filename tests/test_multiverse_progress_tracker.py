"""The public progress tracker must not lag the verified Master Workflow checkpoint."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import update_multiverse_progress_tracker as P  # noqa: E402


class ProgressTrackerCheckpoint(unittest.TestCase):
    def test_checkpoint_reflects_live_workflow_graph_and_recount(self):
        content = P.TRACKER.read_text(encoding="utf-8")
        self.assertEqual(P.current_block(content), P.build())

    def test_legacy_content_is_preserved_below_checkpoint(self):
        content = P.TRACKER.read_text(encoding="utf-8")
        self.assertIn("## Cards", content)
        self.assertIn("## Lore", content)
        self.assertIn("## EDH", content)
        self.assertIn("historical", P.build())


if __name__ == "__main__":
    unittest.main()
