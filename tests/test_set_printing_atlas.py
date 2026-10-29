"""Portable, offline Phase 1B set/printing audit regressions."""

import gzip
import json
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import audit_set_printing_atlas as A  # noqa: E402
import set_atlas_lookup as Q  # noqa: E402


def printing(pid, set_code, oracle_id, released="2020-01-01", **overrides):
    card = {"id": pid, "name": oracle_id, "set": set_code, "set_name": {"aaa": "Test A", "bbb": "Test B"}[set_code],
            "set_type": "expansion" if set_code == "aaa" else "promo",
            "collector_number": pid, "oracle_id": oracle_id, "lang": "en", "games": ["paper"],
            "released_at": released}
    card.update(overrides)
    return card


class SetAtlasTests(unittest.TestCase):
    def setUp(self):
        self.baseline = {"source": "default-cards-old.jsonl.gz", "source_sha256": "oldhash",
                         "total_printings": 3, "total_shards": 1,
                         "shards": {"a-000.jsonl": {"rows": 3, "bytes": 123, "sha256": "saved"}},
                         "sets": {"aaa": {"name": "Test A", "printings": 2, "english_paper": 2,
                                           "files": ["a-000.jsonl"]},
                                  "bbb": {"name": "Test B", "printings": 1, "english_paper": 1,
                                           "files": ["a-000.jsonl"]}}}
        self.cards = [
            printing("p1", "aaa", "shared"),
            printing("p2", "bbb", "shared"),  # tied debut in two sets on the same day
            printing("p3", "aaa", "single", "2021-01-01"),
            printing("p4", "bbb", "single", "2022-01-01"),  # later reprint
            printing("p5", "bbb", "future", "2026-11-13"),  # not a released debut yet
            printing("p6", "bbb", "arena", "2020-01-01", games=["arena"]),
            printing("p7", "aaa", "foreign", "2019-01-01", lang="ja"),
        ]

    def test_baseline_manifest_joins_and_arithmetic(self):
        v = A.validate_baseline(self.baseline)
        self.assertEqual(v["printing_records"], 3)
        self.assertFalse(v["shard_content_verified"])
        self.baseline["sets"]["aaa"]["files"] = ["absent.jsonl"]
        with self.assertRaisesRegex(ValueError, "absent shard"):
            A.validate_baseline(self.baseline)

    def test_set_category_and_debut_reprint_ties_are_explicit(self):
        catalog, report = A.analyze(self.cards, date(2026, 10, 29))
        self.assertEqual(report["printings"], 7)
        self.assertEqual(report["english_paper"], 5)
        self.assertEqual(report["future_dated_printings"], 1)
        self.assertEqual(report["same_day_debut_identities"], 1)
        self.assertEqual(catalog["aaa"]["single_set_debuts"], 1)
        self.assertEqual(catalog["aaa"]["tied_same_day_debuts"], 1)
        self.assertEqual(catalog["bbb"]["tied_same_day_debuts"], 1)
        self.assertEqual(catalog["bbb"]["reprinted_oracle_ids"], 1)
        self.assertEqual(catalog["bbb"]["released_distinct_oracle_ids"], 2)
        audit = A.audit(self.baseline, catalog, report, {"sha256": "verified"}, date(2026, 10, 29))
        self.assertEqual(audit["scryfall_set_types"]["expansion"]["set_codes"], 1)
        self.assertEqual(audit["comparison"]["net_printing_delta"], 4)

    def test_duplicate_printing_id_and_set_conflicts_fail(self):
        with self.assertRaisesRegex(ValueError, "repeated"):
            A.analyze(self.cards + [self.cards[0]], date(2026, 10, 29))
        bad = printing("unique", "aaa", "other", set_name="Wrong Name")
        with self.assertRaisesRegex(ValueError, "conflicting"):
            A.analyze(self.cards + [bad], date(2026, 10, 29))

    def test_set_to_cards_and_card_to_sets_queries_obey_date_and_identity(self):
        cutoff = date(2026, 10, 29)
        a = Q.query(self.cards, cutoff, "set", "AAA")
        self.assertEqual((a["distinct_oracle_ids"], a["printings"]), (2, 2))
        self.assertEqual({x["name"]: x["classification"] for x in a["items"]},
                         {"shared": "same-day tied debut", "single": "debut"})
        b = Q.query(self.cards, cutoff, "set", "bbb")
        self.assertEqual({x["name"]: x["classification"] for x in b["items"]},
                         {"shared": "same-day tied debut", "single": "reprint"})
        self.assertEqual(Q.query(self.cards, cutoff, "card", "single")["set_codes"], ["aaa", "bbb"])
        self.assertEqual(Q.query(self.cards, cutoff, "card", "future")["printing_records"], 0)
        self.assertEqual(Q.query(self.cards, cutoff, "set", "bbb", include_future=True)["distinct_oracle_ids"], 3)
        self.assertEqual(Q.query(self.cards, cutoff, "set", "bbb", include_digital=True)["distinct_oracle_ids"], 3)
        double = printing("face", "aaa", "two-faced", name="Front // Back",
                          card_faces=[{"name": "Front"}, {"name": "Back"}])
        self.assertEqual(Q.query([double], cutoff, "card", "Back")["printing_records"], 1)
        undated = printing("undated", "bbb", "unknown", released="")
        self.assertEqual(Q.query([undated], cutoff, "set", "bbb", include_future=True)["printings"], 0)

    def test_verified_snapshot_sha_and_record_count_guard(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            snapshot = directory / "default-cards-20261029090546.jsonl.gz"
            with gzip.open(snapshot, "wt", encoding="utf-8") as fh:
                for card in self.cards:
                    fh.write(json.dumps(card) + "\n")
            manifest = directory / "manifest.json"
            manifest.write_text(json.dumps({"files": {"default-cards": {
                "filename": snapshot.name, "sha256": A.checksum(snapshot),
                "compressed_bytes": snapshot.stat().st_size, "records": len(self.cards)
            }}}), encoding="utf-8")
            baseline = directory / "baseline.json"
            baseline.write_text(json.dumps(self.baseline), encoding="utf-8")
            report, catalog = A.generate(baseline, snapshot, manifest, date(2026, 10, 29))
            self.assertEqual(report["snapshot"]["printings"], 7)
            self.assertEqual(len(catalog["sets"]), 2)
            broken = json.loads(manifest.read_text())
            broken["files"]["default-cards"]["sha256"] = "unverified"
            manifest.write_text(json.dumps(broken), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "SHA-256"):
                A.generate(baseline, snapshot, manifest, date(2026, 10, 29))

    def test_published_atlas_checkpoint_is_self_consistent(self):
        audit = json.loads((ROOT / "data/set_atlas/audit_2026-10-29.json").read_text(encoding="utf-8"))
        catalog = json.loads((ROOT / "data/set_atlas/catalog_2026-10-29.json").read_text(encoding="utf-8"))
        entries = list(catalog["sets"].values())
        self.assertEqual(len(entries), audit["snapshot"]["sets"])
        self.assertEqual(sum(e["printings"] for e in entries), audit["snapshot"]["printings"])
        self.assertEqual(sum(e["english_paper"] for e in entries), audit["snapshot"]["english_paper"])
        self.assertEqual(sum(e["future_dated_printings"] for e in entries), audit["snapshot"]["future_dated_printings"])
        self.assertEqual(catalog["source_sha256"], audit["source"]["sha256"])
        for entry in entries:
            self.assertEqual(entry["single_set_debuts"] + entry["tied_same_day_debuts"]
                             + entry["reprinted_oracle_ids"], entry["released_distinct_oracle_ids"])
        self.assertEqual(audit["comparison"]["new_set_codes"], [])
        self.assertEqual(audit["comparison"]["absent_set_codes"], [])
        self.assertEqual(audit["comparison"]["changed_set_count"], 5)
        self.assertEqual((catalog["sets"]["lea"]["printings"],
                          catalog["sets"]["lea"]["released_distinct_oracle_ids"]), (295, 290))
        self.assertEqual(catalog["sets"]["leb"]["single_set_debuts"], 2)
        self.assertEqual(catalog["sets"]["trk"]["future_dated_printings"], 530)
        self.assertEqual(catalog["sets"]["trk"]["released_distinct_oracle_ids"], 0)


if __name__ == "__main__":
    unittest.main()
