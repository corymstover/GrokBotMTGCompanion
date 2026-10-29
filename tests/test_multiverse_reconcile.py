"""The new snapshot comparison reports evidence without mutating research."""
import csv
import gzip
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import multiverse_snapshot_reconcile as recon  # noqa: E402
import scryfall_snapshot as snap  # noqa: E402


class MultiverseReconcileTests(unittest.TestCase):
    def test_report_is_read_only_and_flags_real_changes(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "repo"
            folder = Path(temp) / "snapshot"
            (root / "data/printing_lore").mkdir(parents=True)
            folder.mkdir()
            names = "name,oracle_id,shard,anchor,edhrec_rank,color_identity,type_line,commander_legality,game_changer,batch,rulings\n"
            names += "Old Card,oid-1,cards/O/old.md,old,10,U,Creature,legal,0,test,1\n"
            names += "Lost Card,oid-gone,cards/L/lost.md,lost,20,B,Creature,legal,0,test,0\n"
            (root / "data/card_index.csv").write_text(names, encoding="utf-8")
            (root / "data/card_enrichment.json").write_text(json.dumps({
                "bulk": "2026-10-16", "cards": {"oid-1": {"name": "Old Card"},
                                                   "oid-gone": {"name": "Lost Card"}},
            }), encoding="utf-8")
            (root / "data/printing_lore/manifest.json").write_text(json.dumps({
                "source": "default-cards-old.jsonl.gz", "source_sha256": "historical-sha",
                "sets": {"abc": {"english_paper": 7}},
            }), encoding="utf-8")

            payload = {
                "oracle-cards": [
                    {"name": "Old Card", "oracle_id": "oid-1", "color_identity": ["U", "R"],
                     "type_line": "Legendary Creature", "legalities": {"commander": "banned"},
                     "game_changer": True, "edhrec_rank": 11},
                    {"name": "New Card", "oracle_id": "oid-new", "type_line": "Creature"},
                ],
                "default-cards": [
                    {"name": "New Card", "digital": False, "lang": "en", "story_spotlight": True,
                     "flavor_text": "Lore"},
                    {"name": "Digital", "digital": True},
                ],
                "rulings": [{"oracle_id": "oid-1"}, {"oracle_id": "oid-1"}],
            }
            manifest = {"schema_version": 1, "snapshot_id": "snap-20261029-test", "files": {}}
            for kind in snap.KINDS:
                name = kind + "-20261029090000.jsonl.gz"
                blob = gzip.compress("".join(json.dumps(v) + "\n" for v in payload[kind]).encode())
                (folder / name).write_bytes(blob)
                manifest["files"][kind] = {"filename": name, "sha256": hashlib.sha256(blob).hexdigest(),
                                           "compressed_bytes": len(blob), "records": len(payload[kind])}
            (folder / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")

            before = {str(p): p.read_bytes() for p in (root / "data").rglob("*") if p.is_file()}
            report = recon.reconcile(folder, root)
            after = {str(p): p.read_bytes() for p in (root / "data").rglob("*") if p.is_file()}
            self.assertEqual(before, after)
            self.assertFalse(report["decision_authority"])
            changed = report["review_categories"]
            for key in ("previously_indexed_oracle_ids_missing_now", "new_oracle_ids_not_in_committed_index",
                        "type_line_differences", "color_identity_differences", "commander_legality_differences",
                        "game_changer_differences", "indexed_ruling_count_differences"):
                self.assertEqual(changed[key]["count"], 1, key)
            self.assertEqual(report["counts"]["prior_printing_archive_english_paper"], 7)


if __name__ == "__main__":
    unittest.main()
