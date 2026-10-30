"""The Phase 1B source-archive audit cannot substitute arbitrary newer Scryfall data."""
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_phase1b_snapshot_gates as A  # noqa: E402


class PinnedCacheDiagnostics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.product = json.loads((ROOT / "data/set_atlas/product_catalog_2026-10-29.json").read_text())

    def test_missing_cache_is_clear_blocker_not_index_error(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(A, "CACHE", Path(tmp)):
            with self.assertRaisesRegex(SystemExit, "MTG_PINNED_BULK_MISSING") as ctx:
                A.pinned_bulk(self.product)
            self.assertIn("SHA-256", str(ctx.exception))

    def test_newer_bulk_cannot_impersonate_locked_source(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(A, "CACHE", Path(tmp)):
            (Path(tmp) / "default-cards-20990101000000.jsonl.gz").write_bytes(b"not the pinned file")
            with self.assertRaisesRegex(SystemExit, "MTG_PINNED_BULK_MISSING"):
                A.pinned_bulk(self.product)

    def test_manifest_and_catalog_hashes_must_agree(self):
        with self.assertRaisesRegex(SystemExit, "MTG_SNAPSHOT_MANIFEST_CONFLICT"):
            A.pinned_bulk({"oracle_printing_source_sha256": "not-an-accepted-source"})


if __name__ == "__main__":
    unittest.main()
