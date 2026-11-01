"""A release bulk replay must compare stable Oracle IDs and reject tampered files."""
import gzip
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_release_bulk_delta as A  # noqa: E402


class ReleaseBulkDeltaTests(unittest.TestCase):
    def test_november_source_report_retains_all_material_drift_and_art_limits(self):
        doc = json.loads((ROOT / "data/scryfall_snapshots/oct30_to_nov01_release_delta_2026-11-01.json").read_text())
        self.assertTrue(doc["source_bytes_sha256_and_counts_verified"])
        self.assertEqual(doc["current_snapshot"], "snap-20261101-live-20261101")
        self.assertEqual(doc["delta"]["oracle-cards"]["existing_ids_with_tracked_field_changes"], 7)
        self.assertEqual(doc["delta"]["default-cards"]["existing_ids_with_tracked_field_changes"], 49)
        self.assertTrue(doc["delta"]["rulings"]["identical_record_multiset"])
        self.assertEqual(doc["indexed_card_parity"]["missing_indexed_ids"], 0)
        self.assertEqual(doc["indexed_card_parity"]["field_differences"]["color_identity"]["count"], 0)
        self.assertEqual(doc["prior_art_source_integrity"]["checked_specific_printings"], 581)
        self.assertEqual(doc["prior_art_source_integrity"]["material_art_identity_changes"], [])
        self.assertEqual(doc["prior_art_source_integrity"]["missing_from_new_bulk"], [])

    def test_uses_stable_oracle_id_not_rolling_printing_id(self):
        old = {"id": "old-print", "oracle_id": "oracle-stable", "name": "Test",
               "type_line": "Creature", "color_identity": ["U"], "legalities": {"commander": "legal"}}
        new = {**old, "id": "new-print"}
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp)
            manifests = []
            for sub, oracle in (("old", old), ("new", new)):
                folder = path / sub
                folder.mkdir()
                files = {}
                for kind in A.KINDS:
                    obj = oracle if kind == "oracle-cards" else {"id": "printing", "name": "Other"} if kind == "default-cards" else {"oracle_id": "oracle-stable", "comment": "ruling"}
                    name = kind + "-fixture.jsonl.gz"
                    dest = folder / name
                    with gzip.open(dest, "wt", encoding="utf-8") as f:
                        f.write(json.dumps(obj) + "\n")
                    data = dest.read_bytes()
                    files[kind] = {"filename": name, "compressed_bytes": len(data),
                                   "sha256": hashlib.sha256(data).hexdigest(), "records": 1}
                manifests.append({"schema_version": 1, "snapshot_id": sub, "files": files})
            out = A.audit(*manifests, path / "old", path / "new")
            self.assertEqual(out["delta"]["oracle-cards"]["added_ids"], 0)
            self.assertEqual(out["delta"]["oracle-cards"]["removed_ids"], 0)
            self.assertEqual(out["delta"]["oracle-cards"]["existing_ids_with_tracked_field_changes"], 0)
            self.assertTrue(out["delta"]["rulings"]["identical_record_multiset"])
            (path / "new" / "default-cards-fixture.jsonl.gz").write_bytes(b"tampered")
            with self.assertRaisesRegex(ValueError, "unverified source bytes"):
                A.audit(*manifests, path / "old", path / "new")

    def test_differing_oracle_text_is_not_ignored(self):
        prior = {"n": ({"oracle_text_digest": "a", "name": "X"}, "one")}
        now = {"n": ({"oracle_text_digest": "b", "name": "X"}, "two")}
        # Supply all selected keys to exercise the public comparison contract.
        for value in (prior["n"][0], now["n"][0]):
            for key in A.ORACLE_FIELDS:
                value.setdefault(key, None)
        out = A.summarize_changes(prior, now, "oracle-cards")
        self.assertEqual(out["existing_ids_with_tracked_field_changes"], 1)
        self.assertEqual(out["changed_fields"]["oracle_text_digest"], 1)


if __name__ == "__main__":
    unittest.main()
