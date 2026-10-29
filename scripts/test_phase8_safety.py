#!/usr/bin/env python3
"""Read-only Phase 8 gate regressions; no repository generators executed."""
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

import phase8_status as S


class Phase8SafetyTests(unittest.TestCase):
    def test_coverage_comes_from_artifact(self):
        data = {"generated_by": "builder", "cards": {"x": {}, "y": {}},
                "coverage": {"priority pool (any tier)": {"size": 5, "enriched": 2},
                             "legendary-creature": {"size": 3, "enriched": 1}}, "batches": []}
        out = S.summarize(data)
        self.assertEqual(out["total_enrichment_records"], 2)
        self.assertEqual(out["coverage"]["priority pool (any tier)"]["remaining"], 3)
        self.assertEqual(out["coverage"]["legendary-creature"]["percent"], 33.3)

    def test_invalid_coverage_fails_instead_of_clamping(self):
        data = {"cards": {}, "coverage": {"priority pool (any tier)": {"size": 2, "enriched": 3}}}
        with self.assertRaises(ValueError):
            S.summarize(data)

    def test_missing_data_is_not_misreported_as_zero(self):
        with tempfile.TemporaryDirectory() as root:
            missing = Path(root) / "data.json"
            proc = subprocess.run(["python3", str(S.ROOT / "scripts" / "phase8_status.py"),
                                   "--data", str(missing), "--json", "--strict"],
                                  capture_output=True, text=True, check=False)
        self.assertEqual(proc.returncode, 1)
        self.assertFalse(json.loads(proc.stdout)["available"])

    def test_legacy_rebuild_now_requires_explicit_apply_and_skips_grixis_generators(self):
        path = S.ROOT / "scripts" / "rebuild_enrichment.sh"
        source = path.read_text(encoding="utf-8")
        # Do not execute the generators: this is deliberately a static boundary test.
        self.assertNotIn("step python3 scripts/grixis_refine.py", source)
        self.assertNotIn("step python3 scripts/grixis_interactions.py", source)
        self.assertIn('mode="${1:---plan}"', source)
        self.assertIn('branch" = main', source)
        self.assertIn("git status --porcelain", source)
        self.assertIn("story_cache_audit.py --strict", source)
        self.assertIn(".cache/story/text22", source)
        self.assertIn("scryfall_snapshot.py verify", source)
        syntax = subprocess.run(["bash", "-n", str(path)], capture_output=True, check=False)
        self.assertEqual(syntax.returncode, 0, syntax.stderr.decode("utf-8"))


if __name__ == "__main__":
    unittest.main()
