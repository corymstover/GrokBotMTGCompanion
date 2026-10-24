"""Independent owner-review-only Deck #26 Kess M7 Rev1, exact-source bounded tests.

No canonical approval or GitHub merge is authorized by passing these tests.
"""
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "data/grixis/m7/baseline_sources/Kess__Dissident_Mage_approved_source_2026-10-14.txt"
CAND = ROOT / "data/grixis/m7/independent_reviews/Kess__Dissident_Mage_ChatGPT_Rev1_candidate.txt"
MEMO = ROOT / "data/grixis/m7/independent_reviews/Kess__Dissident_Mage_ChatGPT_Rev1_review.md"
ORACLE = ROOT / "data/grixis/m6/oracle_snapshots/Kess__Dissident_Mage_M7_Scryfall_20261023.json"
REG = ROOT / "data/grixis/registry.json"
BASE_SHA = "93d27d605bbdf0737ebe32c911fafe3a002b06d7d90f00b7bfc402cb1d3faccb"
CAND_SHA = "11415352a453e52afe4b1cc6881061e0d255e8403f8d5af5a24f9803c004fde4"
SWAPS = (
    ("Mana Drain", "Personal Tutor"),
    ("Grim Tutor", "Demonic Counsel"),
    ("Jeska's Will", "Ledger Shredder"),
    ("Cyclonic Rift", "Into the Flood Maw"),
    ("Exotic Orchard", "Fiery Islet"),
)
KEEP = (
    "Kess, Dissident Mage", "Demonic Consultation", "Tainted Pact", "Thassa's Oracle",
    "Underworld Breach", "Lion's Eye Diamond", "Brain Freeze", "Grinding Station",
    "Gifts Ungiven", "Intuition", "Entomb", "Reanimate", "Displacer Kitten",
    "Snapcaster Mage", "Spellseeker", "Faithless Looting", "Dragon's Rage Channeler",
    "Valley Floodcaller", "Mindbreak Trap", "Deadly Rollick", "Final Fortune",
)


def names(path):
    data = path.read_bytes()
    rows = data.decode("utf-8").splitlines()
    assert all(row.startswith("1x ") for row in rows)
    assert rows[0] == "1x Kess, Dissident Mage [Commander]"
    assert all("[Commander]" not in r for r in rows[1:])
    return [r.removeprefix("1x ").removesuffix(" [Commander]") for r in rows]


class KessChatGPTIndependentRev1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = names(SRC)
        cls.new = names(CAND)
        cls.oracle = {x["name"]: x for x in json.loads(ORACLE.read_text())["cards"]}
        cls.registry = json.loads(REG.read_text())["decks"]["Kess__Dissident_Mage"]

    def test_exact_raw_bytes_and_baseline_authority_preserved(self):
        self.assertEqual(sha256(SRC.read_bytes()).hexdigest(), BASE_SHA)
        self.assertEqual(sha256(CAND.read_bytes()).hexdigest(), CAND_SHA)
        self.assertTrue(CAND.read_bytes().endswith(b"\n"))
        self.assertEqual(self.registry["source"]["recorded_sha256"], BASE_SHA)
        self.assertEqual(self.registry["source"]["raw_sha256"], "sha256:" + BASE_SHA)
        self.assertTrue(self.registry["source"]["recorded_matches_raw"])

    def test_five_swaps_not_a_limit_and_protected_identity(self):
        self.assertEqual(len(self.source), 100)
        self.assertEqual(len(self.new), 100)
        self.assertEqual(len(set(self.new)), 100)
        self.assertEqual(self.new[1:], sorted(self.new[1:], key=str.lower))
        self.assertEqual(sorted((Counter(self.new) - Counter(self.source)).elements()),
                         sorted(a for a, _ in SWAPS))
        self.assertEqual(sorted((Counter(self.source) - Counter(self.new)).elements()),
                         sorted(c for _, c in SWAPS))
        for k in KEEP:
            self.assertEqual(self.new.count(k), 1, k)
        for banned_identity in ("Manamorphose", "Silence", "Dockside Extortionist"):
            self.assertNotIn(banned_identity, self.new)

    def test_archived_live_oracle_all_100_legality_identity_and_nonbasics(self):
        self.assertTrue(set(self.new) <= set(self.oracle))
        self.assertEqual(len(self.oracle), 187)
        for n in self.new:
            c = self.oracle[n]
            self.assertEqual(c["commander_legality"], "legal", n)
            self.assertTrue(set(c["color_identity"]) <= {"B", "R", "U"}, n)
        self.assertEqual(set(self.new) & {"Island", "Mountain", "Swamp"}, set())
        self.assertEqual(set(self.new) & {"Trade Secrets", "Yawgmoth's Bargain", "Lutri, the Spellchaser"}, set())
        self.assertEqual(sum("Land" in self.oracle[n]["type_line"] for n in self.new), 27)

    def test_bracket_and_measured_curve_consequences(self):
        def result(ns):
            library = [self.oracle[n] for n in ns[1:]]
            nonlands = [x for x in library if "Land" not in x["type_line"]]
            pitches = [x for x in nonlands if "{U}" in x["mana_cost"] or
                       (x["type_line"].startswith("Creature") and "U" in x["color_identity"])]
            return (len([x for x in library if "Land" in x["type_line"]]),
                    len([x for x in library if x["game_changer"]]) + int(self.oracle[ns[0]]["game_changer"]),
                    len(pitches), sum(x["cmc"] for x in nonlands) / len(nonlands))
        old, new = result(self.source), result(self.new)
        self.assertEqual(old[:3], (27, 21, 26))
        self.assertEqual(new[:3], (27, 23, 25))
        self.assertAlmostEqual(old[3], 1.8472222222, places=8)
        self.assertAlmostEqual(new[3], 1.9027777778, places=8)

    def test_selected_rules_and_no_unsupported_combo_claim(self):
        k = self.oracle["Kess, Dissident Mage"]["oracle_text"]
        self.assertIn("Once during each of your turns", k)
        self.assertIn("exile it instead", k)
        self.assertEqual(self.oracle["Mana Drain"]["mana_cost"], "{U}{U}")
        self.assertIn("your next main phase", self.oracle["Mana Drain"]["oracle_text"])
        self.assertIn("If you control a commander", self.oracle["Jeska's Will"]["oracle_text"])
        self.assertIn("Overload {6}{U}", self.oracle["Cyclonic Rift"]["oracle_text"])
        self.assertIn("land an opponent controls", self.oracle["Exotic Orchard"]["oracle_text"])
        self.assertIn("four or more card types", self.oracle["Demonic Counsel"]["oracle_text"])
        self.assertIn("Search your library for a card", self.oracle["Grim Tutor"]["oracle_text"])
        demons = [n for n in self.source if "Creature" in self.oracle[n]["type_line"] and
                  "Demon" in self.oracle[n]["type_line"].split("—")[-1]]
        self.assertFalse(demons, demons)
        for n in ("Kess, Dissident Mage", "Thassa's Oracle", "Demonic Consultation", "Tainted Pact",
                  "Underworld Breach", "Lion's Eye Diamond", "Brain Freeze", "Grinding Station",
                  "Reanimate", "Gifts Ungiven", "Intuition"):
            self.assertIn(n, self.new)

    def test_owner_approval_not_fabricated(self):
        memo = MEMO.read_text()
        for caveat in ("NOT APPROVED", "NOT CANONICAL", "Owner override", "Owner reversal",
                       "conditional", "not inherited", "never automatically"):
            self.assertIn(caveat.lower(), memo.lower())
        self.assertIn(CAND_SHA, memo)
        self.assertNotIn("CANONICAL_LOCKED", memo)


if __name__ == "__main__":
    unittest.main()
