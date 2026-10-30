"""Guard: local rebuild and CI steps must not hide a failing command's exit code."""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REBUILD = ROOT / "scripts" / "claim_spec_sources" / "rebuild.sh"
WORKFLOWS = sorted((ROOT / ".github" / "workflows").glob("*.yml"))


class NoMaskedExitCodes(unittest.TestCase):
    def test_rebuild_uses_pipefail_and_fails_on_check_mismatch(self):
        s = REBUILD.read_text()
        self.assertIn("set -euo pipefail", s)
        self.assertNotRegex(s, r"\|\s*(head|tail)\b", "piping into head/tail can hide the producer's exit code")
        self.assertRegex(s, r'checkfail=1')
        self.assertRegex(s, r'if \[ "\$checkfail" -ne 0 \]; then .*exit 1')

    def test_workflows_do_not_swallow_failures(self):
        for wf in WORKFLOWS:
            s = wf.read_text()
            with self.subTest(wf=wf.name):
                self.assertNotIn("continue-on-error: true", s)
                self.assertNotRegex(s, r"\|\|\s*true\b")

    def test_workflow_pipes_run_under_pipefail(self):
        # GitHub's default `run` shell is `bash -e` (no pipefail); `shell: bash` or an explicit
        # `set -o pipefail` / `set -euo pipefail` adds it.
        for wf in WORKFLOWS:
            s = wf.read_text()
            piped = [l for l in s.splitlines()
                     if re.search(r"[^|]\|\s*(tee|head|tail|grep|python3?|jq)\b", l) and not l.strip().startswith("#")]
            if piped:
                with self.subTest(wf=wf.name):
                    self.assertTrue("pipefail" in s or "shell: bash" in s, f"{wf.name}: {piped[:2]}")


if __name__ == "__main__":
    unittest.main()
