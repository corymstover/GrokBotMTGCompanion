"""Exact-current Parnesse whole-99 role accounting; not strategic judgment automation."""

from collections import Counter
from hashlib import sha256
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data/grixis/m7/candidate_lists/Parnesse_the_Subtle_Brush_M7_Rev1_Approved_2026-10-27.txt"
REPORT = ROOT / "data/grixis/m7/decision_reviews/Parnesse_M7_Rev1_Exact_Current_Whole99_20261028.md"
CURRENT_SHA = "63b605a2c36ec81ab7a5a48770ac2b96b7994daf38546aba7b6bc6bd7597928c"


class ParnesseWhole99(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        raw = SOURCE.read_bytes()
        if sha256(raw).hexdigest() != CURRENT_SHA:
            raise AssertionError("exact owner-approved Parnesse raw source changed")
        lines = raw.decode("utf-8").splitlines()
        if not lines or lines[0] != "1x Parnesse, the Subtle Brush [Commander]":
            raise AssertionError("commander identity not source bound")
        cls.current = Counter()
        for line in lines:
            qty, name = line.split("x ", 1)
            cls.current[name.removesuffix(" [Commander]")] += int(qty)
        cls.spells = cls.current.copy()
        cls.spells.subtract({"Parnesse, the Subtle Brush": 1})
        cls.report = REPORT.read_text(encoding="utf-8")

    def test_each_current_noncommander_physical_copy_has_exactly_one_role(self):
        ledger = Counter()
        for qty, name in re.findall(r"^- (\d+)x (.+)$", self.report, re.MULTILINE):
            ledger[name] += int(qty)
        self.assertIn(CURRENT_SHA, self.report)
        self.assertEqual(sum(self.current.values()), 100)
        self.assertEqual(sum(ledger.values()), 99)
        self.assertEqual(ledger, self.spells)
        self.assertNotIn("Parnesse, the Subtle Brush", ledger)
        self.assertEqual({name: qty for name, qty in self.current.items() if qty > 1},
                         {"Island": 2, "Mountain": 3, "Swamp": 2})
        for heading, count in (
            ("35 lands", 35), ("15 mana/access", 15), ("25 substantive", 25),
            ("8 Parnesse", 8), ("8 conditional", 8), ("8 card-selection", 8),
        ):
            self.assertIn(heading, self.report)
            self.assertEqual(count, int(heading.split()[0]))

    def test_owner_approved_additions_and_cut_cards_not_silently_reused(self):
        adds = {"Mica, Reader of Ruins", "Spinerock Tyrant", "Tendrils of Agony",
                "Storm King's Thunder", "Fierce Guardianship", "Flusterstorm", "Loki Laufeyson"}
        cuts = {"Cormela, Glamour Thief", "Pyromancer's Goggles", "Sedgemoor Witch",
                "Replication Technique", "Counterspell", "An Offer You Can't Refuse", "Dark Ritual"}
        self.assertTrue(all(self.current[name] == 1 for name in adds))
        self.assertTrue(all(self.current[name] == 0 for name in cuts))
        self.assertEqual(len(adds), len(cuts))

    def test_complete_100_challenger_packages_preserve_count_and_singleton(self):
        candidates = [
            ({"Twincast"}, {"Display of Power"}),
            ({"Teach by Example", "Chandra, Hope's Beacon"},
             {"Galvanic Iteration", "Double Vision"}),
            ({"Counterspell", "Dark Ritual"}, {"Flusterstorm", "Loki Laufeyson"}),
            ({"See Double"}, {"Mica, Reader of Ruins"}),
        ]
        for additions, removals in candidates:
            with self.subTest(additions=additions, removals=removals):
                self.assertEqual(len(additions), len(removals))
                self.assertTrue(all(self.current[name] == 0 for name in additions))
                self.assertTrue(all(self.current[name] == 1 for name in removals))
                physical = self.current.copy()
                physical.subtract(removals)
                physical.update(additions)
                self.assertEqual(sum(physical.values()), 100)
                self.assertEqual(physical["Parnesse, the Subtle Brush"], 1)
                self.assertTrue(all(qty == 1 or name in {"Island", "Mountain", "Swamp"}
                                    for name, qty in physical.items() if qty > 0))


if __name__ == "__main__":
    unittest.main()
