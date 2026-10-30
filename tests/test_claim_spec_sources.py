"""Every committed claim spec has an authoring script in scripts/claim_spec_sources/ that regenerates it
byte-for-byte, so any pack can be rebuilt from source (overnight batch 7)."""
import os
import re
import subprocess
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "scripts", "claim_spec_sources")
SPECS = os.path.join(ROOT, "data", "lore_research", "claim_specs")


class ClaimSpecSources(unittest.TestCase):
    def test_every_spec_has_a_script_that_regenerates_it(self):
        scripts = {}
        for f in sorted(os.listdir(SRC)):
            if f.endswith(".py") and f != "mv.py":
                m = re.search(r'spec\("([a-z0-9_]+)"', open(os.path.join(SRC, f), encoding="utf-8").read())
                if m:
                    scripts[m.group(1)] = f
        specs = sorted(f[: -len(".spec.json")] for f in os.listdir(SPECS) if f.endswith(".spec.json"))
        self.assertEqual(sorted(scripts), specs, "spec JSONs without a generating script (or vice versa)")
        with tempfile.TemporaryDirectory() as tmp:
            os.makedirs(os.path.join(tmp, "data", "lore_research", "claim_specs"))
            env = dict(os.environ, MV_ROOT=tmp)
            for pack_id, f in scripts.items():
                subprocess.run([sys.executable, f], cwd=SRC, env=env, check=True, capture_output=True)
                with open(os.path.join(tmp, "data", "lore_research", "claim_specs", pack_id + ".spec.json"), "rb") as a, \
                        open(os.path.join(SPECS, pack_id + ".spec.json"), "rb") as b:
                    self.assertEqual(a.read(), b.read(), f"{f} does not regenerate {pack_id}.spec.json")


if __name__ == "__main__":
    unittest.main()
