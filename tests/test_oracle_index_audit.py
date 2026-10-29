"""Read-only regressions for dated, policy-aligned Oracle index exclusions."""

import json
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import audit_oracle_index as A  # noqa: E402


def card(oid, name, **kwargs):
    return {"oracle_id": oid, "name": name, "layout": "normal",
            "games": ["paper"], "digital": False,
            "legalities": {"commander": "legal"},
            "set": "abc", "released_at": "2026-10-20", **kwargs}


class OracleIndexAuditTests(unittest.TestCase):
    def test_every_exclusion_reason_is_disjoint_and_dated(self):
        cases = [
            card("indexed", "Existing card"),
            card("token", "Token", layout="token"),
            card("digital", "Arena only", games=["arena"], digital=True,
                 legalities={"commander": "not_legal", "legacy": "not_legal", "vintage": "not_legal"}),
            card("future", "Announced card", released_at="2026-11-13", set="trk"),
            card("missing", "Previously released card"),
            card("unknown", "Undated card", released_at=""),
        ]
        report = A.classify(cases, {"indexed"}, date(2026, 10, 29))
        self.assertEqual(report["oracle_records"], 6)
        self.assertEqual(report["unindexed_records"], 5)
        self.assertEqual(report["classifications"], {
            "excluded_layout": 1, "nonpaper_noneternal": 1,
            "eligible_future_dated": 1, "eligible_released_missing": 1,
            "eligible_undated_review": 1,
        })
        self.assertEqual(report["future_by_set"], {"trk": 1})

    def test_eternal_legal_nonpaper_object_uses_existing_ingest_policy(self):
        one = card("x", "Legacy-legal special printing", games=["arena"], digital=True,
                   legalities={"legacy": "legal", "commander": "not_legal"})
        report = A.classify([one], set(), date(2026, 10, 29))
        self.assertEqual(report["classifications"]["eligible_released_missing"], 1)

    def test_duplicate_ids_fail_loudly(self):
        with self.assertRaisesRegex(ValueError, "repeated"):
            A.classify([card("x", "A"), card("x", "B")], set(), date(2026, 10, 29))

    def test_indexed_outside_policy_does_not_disappear(self):
        report = A.classify([card("x", "Token", layout="token")], {"x"}, date(2026, 10, 29))
        self.assertEqual(report["indexed_outside_policy"], 1)

    def test_manifest_requires_valid_sha_and_size(self):
        import hashlib
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "oracle.jsonl.gz"
            path.write_bytes(b"fixed fixture bytes")
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            manifest = {"files": {"oracle-cards": {"sha256": digest, "records": 1,
                                                    "compressed_bytes": path.stat().st_size}}}
            self.assertEqual(A.verify_archive(path, manifest), (digest, 1))
            manifest["files"]["oracle-cards"]["sha256"] = "invalid"
            with self.assertRaisesRegex(ValueError, "SHA-256"):
                A.verify_archive(path, manifest)

    def test_saved_checkpoint_accounts_for_every_unindexed_id(self):
        saved = json.loads((ROOT / "data/multiverse_audits/oracle_index_2026-10-29.json").read_text(encoding="utf-8"))
        counts = saved["classifications"]
        self.assertEqual(sum(counts.values()), saved["unindexed_records"])
        self.assertEqual(sum(saved["excluded_layouts"].values()), counts["excluded_layout"])
        self.assertEqual(sum(saved["future_by_set"].values()), counts["eligible_future_dated"])
        self.assertTrue(saved["manifest_verified"])


if __name__ == "__main__":
    unittest.main()
