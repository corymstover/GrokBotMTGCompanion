import json, os, subprocess, sys, unittest
from urllib.parse import urlparse
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "data/lore_research/pack_dossiers_2026-10-30.json"
ORACLE = ROOT / ".cache/multiverse/oracle-cards-20261029090202.jsonl.gz"

class PackDossiers(unittest.TestCase):
    def setUp(self):
        self.d = json.loads(ART.read_text())

    def test_families_and_sections(self):
        self.assertEqual(sorted(self.d["families"]), ["A", "B", "C"])
        for f in self.d["families"].values():
            for k in ("stage_sequence", "relationship_map", "bibliography", "uncertainties", "lore_deck_commander_candidates"):
                self.assertIn(k, f)
            self.assertEqual(len(f["relationship_map"]), f["claim_count"])

    def test_every_claim_source_in_bibliography(self):
        for f in self.d["families"].values():
            for r in f["relationship_map"]:
                for s in r["source_ids"]:
                    self.assertIn(s, f["bibliography"])
                    self.assertIn(urlparse(f["bibliography"][s]["url"]).netloc, {"magic.wizards.com", "www.magic.wizards.com"})

    def test_honest_labels(self):
        self.assertIn("NOT an asserted in-universe chronology", self.d["stage_sequence_basis"])
        self.assertIn("UNAPPROVED", self.d["not"])
        for f in self.d["families"].values():
            nc = [c["claim"] for c in f["uncertainties"]["non_confirmed_claims"]]
            self.assertEqual(len(nc), f["claim_count"] - f["grade_counts"].get("CANON_CONFIRMED", 0))

    @unittest.skipUnless(ORACLE.exists(), "oracle snapshot cache absent")
    def test_check_mode_current(self):
        env = dict(os.environ, MTG_SCRYFALL_MODE="multiverse", SCRYFALL_OFFLINE="1")
        r = subprocess.run([sys.executable, "scripts/build_pack_dossiers.py", "--check"], cwd=ROOT, env=env,
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

if __name__ == "__main__":
    unittest.main()
