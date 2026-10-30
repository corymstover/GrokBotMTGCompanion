import hashlib, json, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUD = ROOT / "data/scryfall_snapshots/manifest_audit_2026-10-30.json"


class SnapshotManifestAuditTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.a = json.loads(AUD.read_text())
        cls.m = json.loads((ROOT / cls.a["manifest_copy"]).read_text())

    def test_copy_hash_stable(self):
        self.assertEqual(hashlib.sha256((ROOT / self.a["manifest_copy"]).read_bytes()).hexdigest(), self.a["manifest_copy_sha256"])
        self.assertEqual(self.m["snapshot_id"], self.a["snapshot_id"])

    def test_every_file_has_bytes_and_hash_matching_release(self):
        self.assertEqual({r["kind"] for r in self.a["files"]}, set(self.m["files"]))
        for r in self.a["files"]:
            self.assertGreater(r["manifest_bytes"], 0)
            self.assertRegex(r["manifest_sha256"], r"^[0-9a-f]{64}$")
            self.assertEqual(r["release_asset_bytes"], r["manifest_bytes"])
            self.assertIsNot(r["local_match"], False)

    def test_references_and_l291_open(self):
        refs = {r["path"]: r for r in self.a["in_repo_references"]}
        self.assertTrue(refs["data/set_atlas/phase1b_snapshot_gates_2026-10-30.json"]["matches_active_manifest"])
        self.assertFalse(refs["data/printing_lore/manifest.json"]["has_bytes"])
        self.assertTrue(self.a["l291"]["active_snapshot_ok"])
        self.assertFalse(self.a["l291"]["closes_l291"])

    def test_no_grixis_lock_touched(self):
        self.assertNotIn("grixis", json.dumps(self.a["in_repo_references"]).lower())


if __name__ == "__main__":
    unittest.main()
