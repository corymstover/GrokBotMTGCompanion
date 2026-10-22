"""Source-bound fail-closed Abaddon M6.6/7 per-deck scope reconciliation.

This is a *contract test*, not a substitute for the 104 actual P0 and
14 actual P1 methods invoked separately by the CI workflow.
"""
from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
AUDIT = "data/grixis/m6/certification_preflight/abaddon_residual_70_decision_relevance_20261022.json"
LEDGER = "data/grixis/m6/phase_b_plans/abaddon_certification_gap_20261022.json"
TRACKER = "data/grixis/milestone_m6_m7_subtracker.json"
SOURCE = "data/grixis/m7/candidate_lists/Abaddon_the_Despoiler.txt"
REVIEW = "data/grixis/m6/certification_preflight/Abaddon_M6_6_7_Gate_Adjudication_20261022.md"
P0 = "data/grixis/m6/phase_b_plans/abaddon_p0_case_inventory_20261022.json"
SHA = "1fabe1251a7868838365144bf0cb1ee903d394ed90ac146b2dd9cdd45683b7dd"


def read_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


class AbaddonScopedM66M67(unittest.TestCase):
    def test_physical_source_and_p0_not_silently_recertified(self):
        self.assertEqual(hashlib.sha256((ROOT / SOURCE).read_bytes()).hexdigest(), SHA)
        p0 = read_json(P0)
        self.assertEqual(len(p0["replay_cases"]), 104)
        self.assertEqual(p0["required_open"], [])
        self.assertFalse(p0["completion_claim"])
        self.assertFalse(p0["authority"]["formal_m6_certified"])

    def test_actual_new_p1_methods_are_named_and_source_available(self):
        audit = read_json(AUDIT)
        self.assertEqual(audit["residual_p1_executed_cases"], 14)
        for part in ("new_p1_preregistered", "further_p1_preregistered"):
            plan = audit[part]
            self.assertTrue(plan["execution_status"].startswith("EXACT_HEAD_PASS_PR_"))
            self.assertEqual(len(plan["planned_methods"]), 7)
            tree = ast.parse((ROOT / plan["path"]).read_text(encoding="utf-8"))
            methods = {n.name for cls in tree.body if isinstance(cls, ast.ClassDef)
                       for n in cls.body if isinstance(n, ast.FunctionDef)}
            self.assertEqual(set(plan["planned_methods"]), methods.intersection(set(plan["planned_methods"])))
            self.assertEqual(len(set(plan["planned_methods"])), 7)
        self.assertNotEqual(audit["new_p1_preregistered"]["exact_head_sha"],
                            audit["further_p1_preregistered"]["exact_head_sha"])

    def test_all_70_residual_names_have_nonpending_status(self):
        audit = read_json(AUDIT)
        rows = audit["rows"]
        self.assertEqual(len(rows), 70)
        self.assertEqual(len({row["name"] for row in rows}), 70)
        self.assertFalse(any("PENDING" in row["disposition"] or "OPEN" in row["disposition"]
                             for row in rows))
        self.assertEqual(sum(r["disposition"].startswith("P1_EXECUTED_PASS_") for r in rows), 8)
        self.assertEqual(sum(audit["disposition_counts"].values()), 70)
        self.assertFalse(audit["canonical_modified"])

    def test_per_deck_gate_progress_not_m6_or_m7_acceptance(self):
        tracker = read_json(TRACKER)
        self.assertEqual(tracker["m6"]["formal_m6_certified_decks"], 0)
        self.assertEqual(tracker["m7"]["formal_m7_review_decisions"], 0)
        for gate_id in ("M6.6", "M6.7"):
            gate = next(g for g in tracker["m6"]["gates"] if g["id"] == gate_id)
            self.assertEqual(gate["status"], "PARTIAL")
            self.assertEqual(gate["completed"], 2)
            self.assertEqual(gate["total"], 62)
            self.assertEqual(gate["completed"], len(gate["per_deck_completion"]))
            self.assertFalse(gate["per_deck_completion"]["Abaddon_the_Despoiler"]["owner_m7_approved"])
            admiral = gate["per_deck_completion"]["Admiral_Beckett_Brass"]
            self.assertEqual(admiral["status"], "COMPLETE_DECISION_SCOPED_ONLY")
            self.assertFalse(admiral["owner_m7_approved"])
            self.assertTrue((ROOT / admiral["source"]).is_file())
        for gate_id in ("M6.8", "M6.9"):
            proof = next(g for g in tracker["m6"]["gates"] if g["id"] == gate_id)
            self.assertEqual((proof["status"], proof["completed"]), ("PARTIAL", 2))
            self.assertEqual(proof["completed"], len(proof["per_deck_completion"]))
            self.assertFalse(proof["per_deck_completion"]["Abaddon_the_Despoiler"]["owner_accepted"])
            admiral = proof["per_deck_completion"]["Admiral_Beckett_Brass"]
            self.assertEqual(admiral["status"], "SOURCE_BOUND_COMPLETE_EVIDENCE_NOT_OWNER_ACCEPTED")
            self.assertFalse(admiral["owner_accepted"])
            self.assertFalse(admiral["canonical_modified"])
            self.assertTrue((ROOT / admiral["source"]).is_file())
        gate = next(g for g in tracker["m6"]["gates"] if g["id"] == "M6.10")
        self.assertEqual((gate["status"], gate["completed"]), ("BLOCKED", 0))
        ledger = read_json(LEDGER)
        self.assertFalse(ledger["latest_gate_adjudication"]["formal_m6_certified"])
        self.assertFalse(ledger["latest_gate_adjudication"]["new_m7_owner_approved"])
        self.assertFalse(ledger["latest_gate_adjudication"]["all_99_effects_proven"])
        review = (ROOT / REVIEW).read_text(encoding="utf-8")
        self.assertIn("M6 I", review)
        self.assertIn("M6 J", review)
        self.assertIn("39819134570", review)
        self.assertIn("39819765932", review)


if __name__ == "__main__":
    unittest.main()
