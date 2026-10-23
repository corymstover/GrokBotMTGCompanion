"""Abaddon stage17 immutable complete 95-name / 100-card source-bound Oracle gate.

The source facts were fetched on 2026-10-22/23. Stage14 live Scryfall
CI independently rechecked the 100-card candidate. Neither act certifies
M6 I/J or supplies owner approval; only official Commander legality here.
"""
import hashlib
import json
from pathlib import Path
import re
import unittest
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = ROOT / "data/grixis/m6/oracle_snapshots/Abaddon_the_Despoiler_Stage17_95_Source_Reconciled_20261023.json"
SPLIT = re.compile(r"^(\d+)x (.+?)(?: \[Commander\])?$")
BASICS = {"Plains", "Island", "Swamp", "Mountain", "Forest", "Wastes"}


class AbaddonStage17Oracle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
        cls.path = ROOT / cls.data["candidate_path"]
        cls.raw = cls.path.read_bytes()
        cls.entries = []
        for raw_line in cls.raw.decode("utf-8").splitlines():
            m = SPLIT.fullmatch(raw_line)
            if not m:
                raise AssertionError("Invalid 100-card physical decklist line: " + raw_line)
            cls.entries.append((int(m.group(1)), m.group(2)))

    def test_exact_list_owner_lock_distinct_and_color(self):
        d = self.data
        self.assertEqual(hashlib.sha256(self.raw).hexdigest(), d["candidate_sha256"])
        self.assertEqual(sum(q for q, _ in self.entries), 100)
        self.assertEqual(self.entries[0], (1, "Abaddon the Despoiler"))
        physical = Counter()
        for qty, name in self.entries:
            physical[name] += qty
        self.assertEqual(set(physical), set(d["oracle_cards"]))
        self.assertEqual(len(physical), 95)
        self.assertEqual(d["physical_cards"], 100)
        self.assertEqual(d["distinct_names"], 95)
        self.assertEqual({k: v for k, v in physical.items() if v > 1}, {"Island": 3, "Mountain": 2, "Swamp": 3})
        self.assertTrue(d["research_only"])
        self.assertFalse(d["owner_ready"])
        self.assertFalse(d["formal_m6_certified"])
        self.assertEqual(d["base_sha256"], "0d9f6df80cafc2a380199b7aec8112e4e54ccfec70024679607032cdf10f5790")

    def test_all_95_oracle_name_identity_live_source_bindings(self):
        d = self.data
        expected_sources = d["sources"]
        self.assertEqual(len(expected_sources), 5)
        counts = {}
        for name, row in d["oracle_cards"].items():
            self.assertIn(row["source_ref"], expected_sources)
            origin_index = expected_sources.index(row["source_ref"])
            counts[str(origin_index)] = counts.get(str(origin_index), 0) + 1
            source = json.loads((ROOT / row["source_ref"]).read_text(encoding="utf-8"))
            v = (source["oracle_snapshot"] if origin_index == 0 else source["oracle_cards"])[name]
            self.assertEqual(row["oracle_id"], v["oracle_id"])
            self.assertEqual(row["card_id"], v.get("card_id", v.get("id")))
            self.assertEqual(row["mana_value"], v.get("mana_value", v.get("cmc")))
            self.assertEqual(row["commander_legality"], v["commander_legality"])
            self.assertEqual(row["color_identity"], v["color_identity"])
            oracle = v.get("oracle_text") or "\n//\n".join(face["name"] + ": " + face["oracle_text"] for face in v.get("card_faces", []))
            self.assertEqual(row["oracle_text"], oracle)
            self.assertEqual(row["scryfall_uri"], v["scryfall_uri"])
            self.assertEqual(row["commander_legality"], "legal", name)
            self.assertLessEqual(set(row["color_identity"]), set("UBR"), name)
        self.assertEqual(counts, {str(k): v for k, v in d["source_name_count_by_index"].items()})
        self.assertEqual(d["official_commander_illegal_names"], [])

    def test_added_sources_are_mechanically_real(self):
        cards = self.data["oracle_cards"]
        self.assertIn("Offspring {2}", cards["Coruscation Mage"]["oracle_text"])
        self.assertIn("first main phase", cards["Sanctum of Stone Fangs"]["oracle_text"])
        self.assertIn("Whenever a creature", cards["Impact Tremors"]["oracle_text"])
        self.assertIn("legend rule", cards["Sakashima of a Thousand Faces"]["oracle_text"])
        self.assertIn("each opponent", cards["Sheoldred, the Apocalypse"]["oracle_text"])
        self.assertIn("{B}{R}", cards["Mount Doom"]["oracle_text"])
        self.assertEqual(self.data["exact_head_live_full100_ci"]["checked_status"], "SUCCESS")


if __name__ == "__main__":
    unittest.main()
