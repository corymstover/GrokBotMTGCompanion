"""Release-time current Scryfall is compared without changing locked decks."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_release_snapshot_delta as D  # noqa: E402


class ReleaseSnapshotFreshnessTests(unittest.TestCase):
    def test_frozen_six_file_source_manifest_and_delta(self):
        old, new = D.manifest(D.OLD), D.manifest(D.NEW)
        doc = D.check_stored()
        self.assertEqual(doc["baseline_snapshot"], old["snapshot_id"])
        self.assertEqual(doc["current_snapshot"], new["snapshot_id"])
        self.assertTrue(doc["archives_strictly_verified"])
        self.assertFalse(doc["source_text_embedded"])
        self.assertEqual(set(doc["delta"]), set(D.KINDS))
        for kind in D.KINDS:
            self.assertTrue(new["files"][kind]["scryfall_updated_at"].startswith("2026-10-30"))

    def test_release_snapshot_has_no_new_text_or_legality_change_for_indexed_cards(self):
        manifest = D.manifest(D.NEW)
        report = json.loads((ROOT / "data/card_db/oracle_drift_2026-10-30.json").read_text())
        rec = json.loads((ROOT / "data/scryfall_snapshots/reconciliation_2026-10-31.json").read_text())
        self.assertEqual(report["snapshot_file"], manifest["files"]["oracle-cards"]["filename"])
        self.assertEqual(rec["snapshot_id"], manifest["snapshot_id"])
        for field in ("oracle_text", "name", "type_line", "color_identity", "commander_legality", "game_changer",
                      "missing_from_snapshot", "shard_text_unparsed"):
            self.assertEqual(report["counts"][field], 0, field)
        for field in ("type_line_differences", "color_identity_differences", "commander_legality_differences",
                      "game_changer_differences", "indexed_ruling_count_differences",
                      "previously_indexed_oracle_ids_missing_now"):
            self.assertEqual(rec["review_categories"][field]["count"], 0, field)
        self.assertEqual(report["counts"]["new_in_snapshot"], 5393)
        self.assertFalse(D.check_stored()["delta"]["rulings"]["added"])

    def test_changed_snapshot_fields_are_reported_without_mutating_original_card_text(self):
        before = {"name": "Source", "oracle_text_digest": "x", "type_line": "Legendary Creature",
                  "color_identity": ("U",), "commander_legality": "legal", "game_changer": False}
        after = dict(before, type_line="Legendary Creature — Human")
        report = D.compare({"id": before}, {"id": after}, D.ORACLE_FIELDS)
        self.assertEqual(report["existing_ids_changed"], 1)
        self.assertEqual(report["changed_fields"]["type_line"], 1)
        self.assertEqual(report["changed_fields"]["oracle_text_digest"], 0)
        self.assertNotIn("oracle_text\"", json.dumps(report))


if __name__ == "__main__":
    unittest.main()
