"""Safe modern snapshots coexist with the original frozen Grixis baseline."""
import gzip
import io
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import ingest_scryfall as ing  # noqa: E402
import scryfall_snapshot as snap  # noqa: E402


def gz_card(name="Island"):
    return gzip.compress((json.dumps({"name": name, "oracle_id": "test-id"}) + "\n").encode())


class MultiverseSnapshotTests(unittest.TestCase):
    def test_multiverse_isolated_offline_and_legacy_lock_unchanged(self):
        original = ing.LOCK_FILE.read_bytes()
        with tempfile.TemporaryDirectory() as temp:
            modern_cache = Path(temp)
            filename = "oracle-cards-20261029090000.jsonl.gz"
            (modern_cache / filename).write_bytes(gz_card())
            env = {"MTG_SCRYFALL_MODE": "multiverse", "MTG_MULTIVERSE_CACHE": temp,
                   "SCRYFALL_OFFLINE": "1"}
            with patch.dict(os.environ, env):
                self.assertIsNone(ing.snapshot_lock())
                self.assertEqual(ing.get_bulk(ing.DEFAULT_CACHE, None)[0][0]["name"], "Island")
            self.assertEqual(ing.LOCK_FILE.read_bytes(), original)

    def test_legacy_mode_still_blocks_missing_frozen_input(self):
        with tempfile.TemporaryDirectory() as temp:
            with patch.dict(os.environ, {"MTG_SCRYFALL_MODE": "", "SCRYFALL_BIRTHDAY_SNAPSHOT": ""}):
                with self.assertRaisesRegex(SystemExit, "locked bulk.*missing"):
                    ing.get_bulk(Path(temp), None)

    def test_modern_fetch_does_not_evict_previous_files(self):
        with tempfile.TemporaryDirectory() as temp:
            cache = Path(temp)
            older = cache / "oracle-cards-20261027090000.jsonl.gz"
            older.write_bytes(gz_card("Old"))
            name = "oracle-cards-20261029090000.jsonl.gz"
            new_data = gz_card("New")

            def fake_get(url):
                if url.endswith("/bulk-data/oracle-cards"):
                    return json.dumps({"updated_at": "2026-10-29T09:00:00Z",
                                       "jsonl_download_uri": "https://data.scryfall.io/oracle-cards/" + name}).encode()
                return new_data

            env = {"MTG_SCRYFALL_MODE": "multiverse", "MTG_MULTIVERSE_CACHE": temp,
                   "SCRYFALL_OFFLINE": ""}
            with patch.dict(os.environ, env), patch.object(ing, "http_get", fake_get):
                cards, _ = ing.get_bulk(ing.DEFAULT_CACHE, None)
            self.assertEqual(cards[0]["name"], "New")
            self.assertEqual(older.read_bytes(), gz_card("Old"))
            self.assertEqual((cache / name).read_bytes(), new_data)

    def test_snapshot_archive_capture_verify_and_tamper_detection(self):
        blobs = {}
        metadata = {}
        for kind in snap.KINDS:
            name = f"{kind}-20261029090000.jsonl.gz"
            url = f"https://data.scryfall.io/{kind}/{name}"
            metadata[f"{snap.API}/{kind}"] = json.dumps({
                "updated_at": "2026-10-29T09:00:00Z", "jsonl_download_uri": url,
            }).encode()
            blobs[url] = gz_card(kind)

        def fake_request(url):
            return io.BytesIO(metadata.get(url, blobs.get(url, b"")))

        with tempfile.TemporaryDirectory() as temp, patch.object(snap, "request", fake_request):
            folder = Path(temp)
            snap.capture(folder, "snap-20261029-test")
            manifest = snap.verify(folder)
            self.assertEqual(manifest["snapshot_id"], "snap-20261029-test")
            self.assertEqual({d["records"] for d in manifest["files"].values()}, {1})
            with self.assertRaises(FileExistsError):
                snap.capture(folder, "snap-20261029-test")
            item = manifest["files"]["oracle-cards"]
            (folder / item["filename"]).write_bytes(b"corrupted")
            with self.assertRaisesRegex(ValueError, "checksum/size mismatch"):
                snap.verify(folder)


if __name__ == "__main__":
    unittest.main()
