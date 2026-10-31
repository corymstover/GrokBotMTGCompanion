"""Fail-closed tests for immutable historical Scryfall replay records."""
import hashlib
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import replay_pinned_scryfall as R  # noqa: E402


class ReplayPinnedScryfallTests(unittest.TestCase):
    def test_replay_evidence_is_still_consistent_with_committed_sources(self):
        evidence = R.portable_check()
        self.assertEqual(evidence["oct28"]["printing_records"], 119509)
        self.assertEqual(evidence["oct28"]["shards_rebuilt_byte_identical"], 105)
        self.assertEqual(evidence["active_companion"]["art_metadata"]["official_story_labels_metadata_matched"], 570)
        self.assertEqual(evidence["active_companion"]["art_metadata"]["unresolved_image_labels_unchanged"], 7)
        self.assertFalse(evidence["protected_decks_modified"])

    def test_exact_hash_and_byte_size_are_mandatory(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            name = "default-cards-20261028090549.jsonl.gz"
            payload = b"archived fixture bytes"
            (directory / name).write_bytes(payload)
            sha = hashlib.sha256(payload).hexdigest()
            self.assertEqual(R.verify_file(directory, name, sha, len(payload))["compressed_bytes"], len(payload))
            with self.assertRaisesRegex(ValueError, "historical source mismatch"):
                R.verify_file(directory, name, sha, len(payload) + 1)
            with self.assertRaisesRegex(ValueError, "historical source mismatch"):
                R.verify_file(directory, name, "0" * 64, len(payload))
            with self.assertRaisesRegex(ValueError, "missing historical source"):
                R.verify_file(directory, "missing.jsonl.gz", sha)


if __name__ == "__main__":
    unittest.main()
