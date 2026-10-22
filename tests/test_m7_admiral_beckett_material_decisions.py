"""Fail-closed final research judgment roster; DOES NOT satisfy owner-ready M7 gate."""

import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
DIR = ROOT / "data/grixis/m7/research_challengers"
JUDGMENTS = DIR / "Admiral_Beckett_Brass_material_decisions_20261022.json"
ORACLE = DIR / "Admiral_Beckett_Brass_Full_Source_Oracle_20261022.json"
CANON = ROOT / "data/grixis/m6/authority_snapshots/Admiral_Beckett_Brass_Canonical_Approved_20261022.txt"
D = DIR / "Admiral_Beckett_Brass_evasive_pirate_density_package.txt"
SCHEMA_REQUIRED_CANDIDATE_FIELDS = {
    "card", "source", "role", "named_cuts", "incumbent_opportunity_cost", "commander_synergy",
    "adversarial_downside", "judgment", "reason", "confidence", "evidence_refs",
}


def names(path):
    return {
        line.split("x ", 1)[1].removesuffix(" [Commander]")
        for line in path.read_text(encoding="utf-8").splitlines()
    }


class AdmiralM7MaterialJudgmentsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(JUDGMENTS.read_text(encoding="utf-8"))
        cls.oracle = {c["name"]: c for c in json.loads(ORACLE.read_text(encoding="utf-8"))["cards"]}
        cls.before = names(CANON)
        cls.after = names(D)

    def test_24_unique_substantive_candidate_dispositions_all_source_bound(self):
        rows = self.data["material_candidates"]
        self.assertEqual(len(rows), 24)
        self.assertEqual(self.data["material_candidate_count"], 24)
        self.assertEqual(len({x["card"] for x in rows}), 24)
        for row in rows:
            with self.subTest(card=row["card"]):
                self.assertEqual(set(row), SCHEMA_REQUIRED_CANDIDATE_FIELDS)
                self.assertIn(row["card"], self.oracle)
                self.assertEqual(self.oracle[row["card"]]["legalities"]["commander"], "legal")
                self.assertTrue(set(self.oracle[row["card"]]["color_identity"]) <= {"U", "B", "R"})
                self.assertTrue(all(len(row[f]) >= 30 for f in
                    ("source", "role", "incumbent_opportunity_cost", "commander_synergy", "adversarial_downside", "reason")))
                self.assertTrue(row["evidence_refs"])
                self.assertTrue(all(x in self.before for x in row["named_cuts"]))
                self.assertIn(row["judgment"], {"SELECT_ADD", "REJECT", "RETAIN_ALTERNATIVE", "EXCLUDE_INVALID"})
                self.assertIn(row["confidence"], {"HIGH", "MODERATE", "LOW_WITH_DISCLOSED_LIMITS"})

    def test_exactly_five_selected_actual_replacements_correspond_to_research_D(self):
        selected = [x for x in self.data["material_candidates"] if x["judgment"] == "SELECT_ADD"]
        self.assertEqual(len(selected), 5)
        self.assertEqual(self.data["selected_add_count"], 5)
        self.assertEqual({x["card"] for x in selected}, self.after - self.before)
        self.assertEqual({x["named_cuts"][0] for x in selected}, self.before - self.after)
        self.assertEqual(len(self.after), len(self.before))
        self.assertEqual(len(self.before), 97)

    def test_alternative_cuts_and_dispositions_are_real_and_nontrivial(self):
        self.assertGreaterEqual(self.data["challenged_incumbent_slots"], 8)
        self.assertGreaterEqual(self.data["source_bound_alternative_package_count"], 2)
        observed = {x["judgment"] for x in self.data["material_candidates"]}
        self.assertIn("SELECT_ADD", observed)
        self.assertIn("REJECT", observed)
        self.assertIn("RETAIN_ALTERNATIVE", observed)
        # No EXCLUDE_INVALID because this sampled set contains no illegal card.
        self.assertNotIn("EXCLUDE_INVALID", observed)

    def test_canonical_approval_and_M6_certification_are_not_claimed(self):
        self.assertTrue(self.data["status"].startswith("RESEARCH_ONLY"))
        self.assertTrue(self.data["owner_authority"]["canonical_unchanged"])
        self.assertFalse(self.data["owner_authority"]["exact_M7_owner_approval"])
        self.assertFalse(self.data["owner_authority"]["owner_approval_requested"])
        self.assertTrue(any("M6.8" in note and "M6.9" in note for note in self.data["limitations"]))


if __name__ == "__main__":
    unittest.main()
