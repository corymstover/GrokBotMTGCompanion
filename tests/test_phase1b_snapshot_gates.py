import json, os, subprocess, sys, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "data/set_atlas/phase1b_snapshot_gates_2026-10-30.json"
BULK = ROOT / ".cache/multiverse/default-cards-20261029090546.jsonl.gz"

class Phase1BSnapshotGates(unittest.TestCase):
    def setUp(self):
        self.d = json.loads(ART.read_text())

    def test_gates_cover_l193_to_l202(self):
        self.assertEqual([g["line"] for g in self.d["gates"]], [f"L{n}" for n in range(193, 203)])
        for g in self.d["gates"]:
            self.assertIn(g["verdict"], {"PASS", "QUALIFIED", "OPEN"})

    def test_historical_ids_all_present_in_pinned_bulk(self):
        g = self.d["g1_exact_id_parity"]
        self.assertEqual(g["only_in_oct28"], 0)
        self.assertEqual(g["ids_in_both"], g["historical_oct28_printing_ids"])
        self.assertEqual(g["duplicate_ids_in_bulk"], 0)
        self.assertEqual(g["oct29_bulk_printing_ids"], g["ids_in_both"] + g["only_in_oct29"])

    def test_counts_and_parents_consistent(self):
        l = self.d["l201_checks"]
        self.assertEqual(l["per_set_count_mismatch_count"], 0)
        self.assertEqual(l["broken_parent_links"], [])
        self.assertEqual(self.d["g6_debut_reprint"]["per_set_debut_mismatch_count"], 0)

    def test_not_presented_as_owner_approval(self):
        self.assertNotIn("OWNER_APPROVED", json.dumps(self.d))

    @unittest.skipUnless(BULK.exists(), "pinned bulk cache absent")
    def test_check_mode_current(self):
        env = dict(os.environ, MTG_SCRYFALL_MODE="multiverse", SCRYFALL_OFFLINE="1")
        r = subprocess.run([sys.executable, "scripts/audit_phase1b_snapshot_gates.py", "--check"],
                           cwd=ROOT, env=env, capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

if __name__ == "__main__":
    unittest.main()
