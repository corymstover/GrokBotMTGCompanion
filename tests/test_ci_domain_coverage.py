"""No silently missing CI domain or false branch-protection assertion."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_ci_domain_coverage as C


class CIDomainCoverageTests(unittest.TestCase):
    def test_nine_domains_are_live_pr_workflows(self):
        result = C.build()
        self.assertEqual(result["count"], 9)
        self.assertEqual(len(result["coverage_domains"]), result["count"])
        for record in result["coverage_domains"].values():
            self.assertTrue(record["pull_request_trigger"])
            self.assertTrue(record["no_continue_on_error"])
            self.assertGreater(len(record["required_step_fragments"]), 0)
        self.assertIn("does NOT prove", result["administrative_limitation"])

    def test_missing_required_step_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp)
            for filename in {v[0] for v in C.DOMAINS.values()}:
                source = C.WORKFLOWS / filename
                content = source.read_text(encoding="utf-8")
                if filename == "phase6-lore-pilots.yml":
                    content = content.replace("run: python3 scripts/audit_lore_pilot.py", "run: true")
                (dest / filename).write_text(content, encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "expected executable step/test"):
                C.build(dest)

    def test_report_reproducibly_tracks_workflow_sha(self):
        self.assertEqual(json.loads(C.OUT.read_text(encoding="utf-8")), C.build())


if __name__ == "__main__":
    unittest.main()
