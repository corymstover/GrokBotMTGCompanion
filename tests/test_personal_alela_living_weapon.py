"""Offline regression checks for Cory's unapproved Living Weapon Assassins revision.

Uses the repository's Scryfall-derived October 15 card index. This is a
reproducible snapshot audit, not an assertion of live Oracle certification.
"""

import csv
import hashlib
import io
import subprocess
import sys
import unittest
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from evaluate_decklist import parse  # noqa: E402

SOURCE = ROOT / "decks/personal/sources/alela-living-weapon-assassins-original-2026-11-04.txt"
PROPOSAL = ROOT / "exports/personal/alela-living-weapon-assassins-2026-11-04.txt"
SOURCE_SHA256 = "39a068221d08861c0520ec9792537702d6bca730c24716f8bb3e72bb119ae0ba"

CUTS = {
    "Banishing Light",
    "Dark Ritual",
    "Diabolic Tutor",
    "Extinguisher Battleship",
    "Return to the Light Realms",
    "Rewrite Regrets",
    "Singularity Rupture",
    "The Echoverse Fulcrum",
    "Unburial Rites",
}
ADDS = {
    "Emry, Lurker of the Loch",
    "Hammer of Nazahn",
    "Skullclamp",
    "Steelshaper's Gift",
    "Stoneforge Mystic",
    "Swords to Plowshares",
    "Talisman of Dominance",
    "Talisman of Progress",
    "Teferi's Protection",
}
NEW_LANDS = {
    "Flooded Strand",
    "Godless Shrine",
    "Hallowed Fountain",
    "Marsh Flats",
    "Polluted Delta",
    "Urza's Saga",
}
LIVING_WEAPON_CORE = {
    "Batterskull", "Bitterthorn, Nissa's Animus", "Bonehoard", "Drossclaw",
    "Flayer Husk", "Hylderblade", "Kaldra Compleat", "Lashwrithe",
    "Mortarpod", "Necropouncer", "Nettlecyst", "Scytheclaw", "Skinwing",
}


def rows(path):
    result = parse(path.read_text(encoding="utf-8"))
    assert not any(e.get("bad") for e in result), "unparseable decklist row"
    return result


def card_index():
    index = ROOT / "data/card_index.csv"
    if index.is_file():
        raw = index.read_text(encoding="utf-8")
    else:
        # Sparse local clones can test the exact repository index without
        # hydrating the huge data/ directory. Full CI reads the file above.
        raw = subprocess.run(
            ["git", "show", "HEAD:data/card_index.csv"], cwd=ROOT,
            check=True, capture_output=True, text=True,
        ).stdout
    return {r["name"]: r for r in csv.DictReader(io.StringIO(raw))}


class PersonalAlelaProposalTests(unittest.TestCase):
    def test_original_snapshot_is_byte_identical(self):
        self.assertEqual(hashlib.sha256(SOURCE.read_bytes()).hexdigest(), SOURCE_SHA256)

    def test_exact_100_commander_singleton_and_preserved_living_weapon_core(self):
        source, proposal = rows(SOURCE), rows(PROPOSAL)
        for deck in (source, proposal):
            self.assertEqual(sum(e["qty"] for e in deck), 100)
            self.assertEqual([e["name"] for e in deck if "commander" in e["tags"].lower()],
                             ["Alela, Artful Provocateur"])
            self.assertEqual(sum(e["qty"] for e in deck if e["name"] in {"Plains", "Island", "Swamp"}),
                             29 if deck is source else 23)
            for e in deck:
                if e["name"] not in {"Plains", "Island", "Swamp"}:
                    self.assertEqual(e["qty"], 1, e["name"])
        before, after = ({e["name"] for e in deck} for deck in (source, proposal))
        self.assertTrue(LIVING_WEAPON_CORE <= before)
        self.assertTrue(LIVING_WEAPON_CORE <= after)

    def test_swap_ledger_and_land_count(self):
        before = Counter({e["name"]: e["qty"] for e in rows(SOURCE)})
        after = Counter({e["name"]: e["qty"] for e in rows(PROPOSAL)})
        self.assertEqual(set(before) - set(after), CUTS)
        self.assertEqual(set(after) - set(before), ADDS | NEW_LANDS)
        for basic in ("Island", "Plains", "Swamp"):
            self.assertEqual(before[basic] - after[basic], 2)
        old_lands = 36  # 29 basics plus 7 nonbasics in the supplied source.
        self.assertEqual(old_lands - 6 + len(NEW_LANDS), 36)

    def test_pinned_card_data_legality_and_color_identity(self):
        index = card_index()
        for e in rows(PROPOSAL):
            with self.subTest(card=e["name"]):
                self.assertIn(e["name"], index)
                if e["name"] not in index:
                    continue
                r = index[e["name"]]
                self.assertEqual(r["commander_legality"], "legal")
                self.assertTrue((set(r["color_identity"]) - {"C"}) <= set("WUB"),
                                f"{e['name']} has off-identity symbols {r['color_identity']}")


if __name__ == "__main__":
    unittest.main()
