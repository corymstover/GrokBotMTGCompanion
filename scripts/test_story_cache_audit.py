"""Offline fixture-based checks for the recovered story source evidence."""

import hashlib
import tempfile
import unittest
from pathlib import Path

import story_cache_audit as S


URL = "https://magic.wizards.com/en/news/story/story-of-yawgmoth"
JOB = {"kind": "story", "url": URL, "reference_words": 200, "arc": "Test"}


class CacheAuditTests(unittest.TestCase):
    def test_missing_is_not_claimed_as_recovered(self):
        with tempfile.TemporaryDirectory() as folder:
            row = S.check_job(JOB, Path(folder))
        self.assertEqual(row["status"], "missing")

    def test_cache_validates_url_without_exposing_body(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            file = S.cache_path(JOB, root)
            file.parent.mkdir(parents=True)
            text = f"URL: {URL}\nTITLE: Yawgmoth\nDATE: 2026-01-01\n\n" + "Phyrexia " * 70
            file.write_text(text, encoding="utf-8")
            report = S.audit([JOB], root)
        row = report["records"][0]
        self.assertEqual(row["status"], "present")
        self.assertEqual(row["words"], 70)
        self.assertEqual(row["sha256"], hashlib.sha256(text.encode()).hexdigest())
        self.assertNotIn("Phyrexia", str(report))
        self.assertFalse(report["source_text_embedded"])

    def test_short_or_wrong_source_is_not_trusted(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            file = S.cache_path(JOB, root)
            file.parent.mkdir(parents=True)
            file.write_text(f"URL: {URL}\nTITLE: Story\nDATE: \n\nvery short", encoding="utf-8")
            self.assertEqual(S.check_job(JOB, root)["status"], "suspect-short")
            file.write_text("URL: https://example.org/wrong\nTITLE: Story\nDATE: \n\n" + "lore " * 80,
                            encoding="utf-8")
            self.assertEqual(S.check_job(JOB, root)["status"], "invalid-source")

    def test_colliding_paths_are_flagged(self):
        with tempfile.TemporaryDirectory() as folder:
            report = S.audit([JOB, JOB], Path(folder))
        self.assertEqual(len(report["colliding_cache_paths"]), 1)

    def test_repair_preserves_valid_cache_and_refetches_bad_cache(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            file = S.cache_path(JOB, root)
            self.assertTrue(S.needs_fetch(JOB, root, repair=True))
            file.parent.mkdir(parents=True)
            file.write_text(f"URL: {URL}\nTITLE: Yawgmoth\nDATE: \n\n" + "lore " * 80,
                            encoding="utf-8")
            self.assertFalse(S.needs_fetch(JOB, root, repair=True))
            self.assertTrue(S.needs_fetch(JOB, root, refresh=True))
            file.write_text(f"URL: {URL}\nTITLE: Yawgmoth\nDATE: \n\nshort",
                            encoding="utf-8")
            self.assertFalse(S.needs_fetch(JOB, root))  # legacy resumable default
            self.assertTrue(S.needs_fetch(JOB, root, repair=True))

    def test_repair_detects_wrong_url_without_dropping_good_file(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            file = S.cache_path(JOB, root)
            file.parent.mkdir(parents=True)
            file.write_text("URL: https://example.org/wrong\nTITLE: X\nDATE: \n\n" +
                            "lore " * 80, encoding="utf-8")
            self.assertTrue(S.needs_fetch(JOB, root, repair=True))


if __name__ == "__main__":
    unittest.main()
