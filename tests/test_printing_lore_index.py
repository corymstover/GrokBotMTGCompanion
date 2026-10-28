"""Small deterministic printing/edition/land/Saga coverage fixture; no network."""

import gzip
import json
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import printing_lore_index as pli


def printing(pid, name, set_code, number, **kwargs):
    return {"id": pid, "oracle_id": "oracle-" + name, "name": name,
            "set": set_code, "set_name": {"lea": "Limited Edition Alpha", "neo": "Kamigawa: Neon Dynasty", "m21": "Core Set 2021"}.get(set_code, set_code),
            "collector_number": number, "released_at": "2021-01-01", "lang": "en",
            "games": ["paper"], "digital": False, "layout": "normal",
            "scryfall_uri": "https://scryfall.com/card/" + set_code + "/" + number,
            **kwargs}


class PrintingLoreIndexTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        base = Path(self.tmp.name)
        self.db = base / "index.sqlite3"
        self.source = base / "sample.jsonl.gz"
        objects = [
            printing("alpha-1", "Plains", "lea", "1", flavor_text="Urza saw the quiet plain."),
            printing("alpha-2", "Plains", "lea", "2", flavor_text="The open plain remembers Mishra."),
            printing("m21-1", "Plains", "m21", "300", flavor_text="The plain lies before Nicol Bolas."),
            printing("saga-1", "The Restoration of Eiganjo // Architect of Restoration", "neo", "34",
                     layout="transform", card_faces=[
                         {"name": "The Restoration of Eiganjo", "type_line": "Enchantment — Saga", "oracle_text": "I — Search your library.\nII — Discard a card.\nIII — Exile this Saga.", "flavor_text": "The city remembers the past."},
                         {"name": "Architect of Restoration", "type_line": "Enchantment Creature — Fox Monk", "oracle_text": "Vigilance", "flavor_text": "Rebuilding begins."}]),
            printing("digital-1", "Virtual Plain", "m21", "400", games=["arena"], digital=True, flavor_text="Digital story."),
        ]
        # The two test-only fields are intentionally overridden for one object.
        with gzip.open(self.source, "wt", encoding="utf-8") as fh:
            for obj in objects:
                fh.write(json.dumps(obj) + "\n")
        pli.build(self.source, self.db)

    def tearDown(self):
        self.tmp.cleanup()

    def command(self, *words):
        import argparse
        a = argparse.Namespace(action=words[0], set_code=None, name=None, phrase=None,
                               all=False, limit=50, all_languages=False, include_digital=False)
        if words[0] == "set":
            a.set_code = words[1]
        elif words[0] == "card":
            a.name = words[1]
        elif words[0] == "flavor":
            a.phrase = words[1]
        if len(words) > 2 and words[2] == "all-digital":
            a.include_digital = True
        with sqlite3.connect(self.db) as conn:
            conn.row_factory = sqlite3.Row
            return pli.query(conn, a)

    def test_alpha_printings_not_unique_cards(self):
        r = self.command("set", "lea")
        self.assertEqual(r["counts"], {"printings": 2, "distinct_names": 1, "oracle_cards": 1})
        self.assertEqual([x["collector_number"] for x in r["items"]], ["1", "2"])

    def test_flavor_search_keeps_specific_land_printing(self):
        r = self.command("flavor", "Mishra")
        self.assertEqual(len(r["items"]), 1)
        self.assertEqual(r["items"][0]["id"], "alpha-2")

    def test_saga_chapters_and_other_face_preserved(self):
        r = self.command("saga")
        self.assertEqual(len(r["items"]), 1)
        faces = r["items"][0]["faces"]
        self.assertIn("III — Exile", faces[0]["oracle_text"])
        self.assertEqual(faces[1]["flavor_text"], "Rebuilding begins.")

    def test_digital_excluded_by_default(self):
        r = self.command("set", "m21")
        self.assertEqual(r["counts"]["printings"], 1)
        r = self.command("set", "m21", "all-digital")
        self.assertEqual(r["counts"]["printings"], 2)

    def test_exact_name_returns_all_editions(self):
        r = self.command("card", "Plains")
        self.assertEqual(len(r["items"]), 3)
        self.assertTrue(all(x["faces"] for x in r["items"]))

    def test_back_face_name_resolves_fast_without_scan(self):
        r = self.command("card", "Architect of Restoration")
        self.assertEqual([x["id"] for x in r["items"]], ["saga-1"])

    def test_frozen_grixis_source_wins_over_newer_cache(self):
        base = Path(self.tmp.name)
        root = base / "mini-repo"
        (root / "data" / "grixis").mkdir(parents=True)
        (root / ".cache").mkdir()
        (root / ".cache" / "default-cards-20261015000000.jsonl.gz").touch()
        (root / ".cache" / "default-cards-20261028000000.jsonl.gz").touch()
        (root / "data" / "grixis" / "dev_snapshot_lock.json").write_text(
            json.dumps({"files": {"default-cards": "default-cards-20261015000000.jsonl.gz"}}), encoding="utf-8")
        with mock.patch.object(pli, "ROOT", root):
            self.assertEqual(pli.latest_source().name, "default-cards-20261015000000.jsonl.gz")


if __name__ == "__main__":
    unittest.main()
