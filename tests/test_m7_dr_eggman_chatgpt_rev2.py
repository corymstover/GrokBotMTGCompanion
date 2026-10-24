"""Exact-file M7 Rev2 research-only checks for Dr. Eggman, independent of the Grok five-swap candidate.

These tests do not confer owner approval. Oracle/legality are checked against archived 2026-10-23
live-Scryfall sources and do not claim a new date-of-test API refresh.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "data/grixis/m7/baseline_sources/Dr__Eggman_approved_source_2026-10-14.txt"
CAND = ROOT / "data/grixis/m7/candidate_lists/Dr__Eggman_ChatGPT_M7_Rev2_20261023.txt"
EVID = ROOT / "data/grixis/m7/decision_reviews/Dr__Eggman_ChatGPT_M7_Rev2_Oracle_Selected_20261023.json"
REVIEW = ROOT / "data/grixis/m7/decision_reviews/Dr__Eggman_ChatGPT_M7_Rev2_Independent_20261023.md"
OLD_HASH = "ef34986253f71043e10c852b5f9f3ce79594fdfc1086b105f6744c3f639199c3"
NEW_HASH = "3ef9dc5bcda84834ccea2f13c1227b6bffda8f4bd914754894ae508adcc404ec"
ADDS = {"Possession Engine", "Skysovereign, Consul Flagship", "Interceptor Mechan",
        "Behemoth of Vault 0", "Gloomlake Verge"}
CUTS = {"Blasphemous Act", "Cybermen Squadron", "Cryptothrall",
        "Weapons Manufacturing", "Withering Torment"}
GCS = {"Ancient Tomb", "Cyclonic Rift", "Fierce Guardianship"}


def read_deck(path):
    result = Counter()
    lines = path.read_text(encoding="utf-8").splitlines()
    for index, line in enumerate(lines):
        m = re.fullmatch(r"(\d+)x (.+?)(?: \[Commander\])?", line)
        assert m, (index, line)
        if index == 0:
            assert line == "1x Dr. Eggman [Commander]"
        else:
            assert "[Commander]" not in line
        result[m.group(2)] += int(m.group(1))
    return result


class EggmanRev2Research(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = read_deck(BASE)
        cls.cand = read_deck(CAND)
        cls.evidence = json.loads(EVID.read_text(encoding="utf-8"))

    def test_source_preservation_and_candidate_exact_bytes(self):
        self.assertEqual(hashlib.sha256(BASE.read_bytes()).hexdigest(), OLD_HASH)
        self.assertEqual(hashlib.sha256(CAND.read_bytes()).hexdigest(), NEW_HASH)
        self.assertEqual(self.evidence["candidate_raw_sha256"], NEW_HASH)
        self.assertEqual(self.evidence["canonical_baseline_sha256"], OLD_HASH)
        self.assertIn("NOT_OWNER_APPROVED", self.evidence["status"])
        self.assertEqual(REVIEW.read_text(encoding="utf-8").count("No “Proceed”"), 1)

    def test_only_five_quality_positive_proposals_not_auto_approved(self):
        self.assertEqual(sum(self.base.values()), 100)
        self.assertEqual(sum(self.cand.values()), 100)
        self.assertEqual(len(self.base), 97)
        self.assertEqual(len(self.cand), 97)
        self.assertEqual(set(self.cand) - set(self.base), ADDS)
        self.assertEqual(set(self.base) - set(self.cand), CUTS)
        self.assertEqual(self.cand["Dr. Eggman"], 1)
        for basic in ("Island", "Mountain", "Swamp"):
            self.assertEqual(self.cand[basic], 2)
        self.assertTrue(all(q == 1 for n, q in self.cand.items() if n not in {"Island", "Mountain", "Swamp"}))
        self.assertIn("Blasphemous Act", REVIEW.read_text(encoding="utf-8"))
        self.assertIn("owner-retained", REVIEW.read_text(encoding="utf-8"))

    def test_oracle_and_legality_per_name(self):
        snap = self.evidence["cards"]
        self.assertEqual(len(snap), 97)
        self.assertEqual(set(row["name"] for row in snap), set(self.cand))
        self.assertEqual(sum(row["quantity"] for row in snap), 100)
        for row in snap:
            with self.subTest(card=row["name"]):
                self.assertEqual(row["quantity"], self.cand[row["name"]])
                self.assertEqual(row["commander_legality"], "legal")
                self.assertTrue(set(row["color_identity"]) <= {"U", "B", "R"})
                self.assertTrue(row["oracle_id"])
                self.assertTrue(row["type_line"])
        self.assertEqual({c["name"] for c in snap if c["game_changer"]}, GCS)
        self.assertEqual(self.evidence["project_exceptions"], [])

    def test_land_and_payload_numerics_and_gloomlake(self):
        snap = self.evidence["cards"]
        land_count = sum(c["quantity"] for c in snap if "Land" in c["type_line"].split(" — ")[0])
        eligible = sum(c["quantity"] for c in snap
                       if " — " in c["type_line"]
                       if re.search(r"\b(?:Robot|Construct|Vehicle)\b",
                                    c["type_line"].split(" — ", 1)[1].split(" // ")[0]))
        self.assertEqual(land_count, 32)
        self.assertEqual(eligible, 31)
        gloom = next(c for c in snap if c["name"] == "Gloomlake Verge")
        self.assertEqual(gloom["color_identity"], ["B", "U"])
        self.assertIn("{T}: Add {U}.", gloom["oracle_text"])
        self.assertIn("control an Island or a Swamp", gloom["oracle_text"])
        self.assertIn("canonical Don Andres", gloom["source"])

    def test_preserved_clock_and_inspector_are_real_artifact_engine(self):
        cards = {c["name"]: c for c in self.evidence["cards"]}
        for keep in ("Foundry Inspector", "Unwinding Clock", "Master Transmuter",
                     "Kuldotha Forgemaster", "Scrapyard Recombiner", "Padeem, Consul of Innovation"):
            self.assertIn(keep, self.cand)
        self.assertIn("artifact spells you cast cost", cards["Foundry Inspector"]["oracle_text"].lower())
        self.assertIn("each other player's untap step", cards["Unwinding Clock"]["oracle_text"])
        for n in ("Master Transmuter", "Kuldotha Forgemaster", "Scrapyard Recombiner"):
            self.assertIn("{T}", cards[n]["oracle_text"])
            self.assertIn("Artifact Creature", cards[n]["type_line"])
        self.assertIn("Cryptothrall is also a valid Construct payload", REVIEW.read_text(encoding="utf-8"))
        self.assertIn("Artifacts you control have hexproof", cards["Padeem, Consul of Innovation"]["oracle_text"])

    def test_color_union_is_not_automatically_three_separate_pips(self):
        # A common bug in simplified 31/32-land DP: one City of Brass is NOT simultaneously U+B+R.
        sources = ["UBR", "", ""]
        union = set().union(*(set(x) for x in sources))
        self.assertEqual(union, {"U", "B", "R"})
        def can_assign(colors):
            def visit(needed, used):
                if not needed:
                    return True
                return any(i not in used and needed[0] in cs and visit(needed[1:], used | {i})
                           for i, cs in enumerate(colors))
            return visit(("U", "B", "R"), set())
        self.assertFalse(can_assign(sources))
        self.assertTrue(can_assign(["UBR", "UB", "BR"]))


if __name__ == "__main__":
    unittest.main()
