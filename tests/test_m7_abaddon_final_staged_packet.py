"""Abaddon-only exact-source M7 candidate structural and authority regressions.

M7 decision packet passing does NOT declare M6 I/J PASS nor owner approval.
"""
from __future__ import annotations
from collections import Counter
import hashlib
import json
from pathlib import Path
import unittest
from scripts.grixis_m7_decision_gate import verify_packet,parse_list,canonical_source

ROOT=Path(__file__).resolve().parents[1]
PATH=ROOT/"data/grixis/m7/decision_reviews/Abaddon_the_Despoiler.json"
REG=ROOT/"data/grixis/registry.json"
ALT=ROOT/"data/grixis/m7/research_challengers/Abaddon_the_Despoiler_v2_engine_answer_keeper.txt"
P0=ROOT/"data/grixis/m6/phase_b_plans/abaddon_p0_case_inventory_20261022.json"
FORBIDDEN="Admiral_Beckett_Brass"

class AbaddonFinalStagedM7(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.packet=json.loads(PATH.read_text(encoding="utf-8"))
        cls.registry=json.loads(REG.read_text(encoding="utf-8"))

    def test_complete_exact_source_structural_gate(self):
        result=verify_packet(self.packet,root=ROOT,registry=self.registry)
        self.assertEqual(result["deck_id"],"Abaddon_the_Despoiler")
        self.assertEqual(result["new_swaps"],2)
        self.assertTrue(result["canonical_unchanged"])
        self.assertTrue(result["m6_certification_not_inferred"])

    def test_researched_pinned_candidate_hash_and_physical_two_swap(self):
        chosen=ROOT/self.packet["final_candidate"]["path"]
        research=ROOT/"data/grixis/m7/research_challengers/Abaddon_the_Despoiler_v2_engine_answer_betrayal.txt"
        self.assertEqual(chosen.read_bytes(),research.read_bytes())
        self.assertEqual(hashlib.sha256(chosen.read_bytes()).hexdigest(),
                         self.packet["final_candidate"]["sha256"])
        reg=self.registry["decks"]["Abaddon_the_Despoiler"]
        baseline,md=canonical_source(ROOT,reg)
        base_cards,_,_=parse_list(baseline,source_markdown=md)
        candidate_cards,commands,companions=parse_list(chosen)
        self.assertEqual(len(candidate_cards),100)
        self.assertEqual(commands,["Abaddon the Despoiler"])
        self.assertEqual(companions,[])
        self.assertEqual(Counter(candidate_cards)-Counter(base_cards),
                         Counter({"Grinning Ignus":1,"Chaos Warp":1}))
        self.assertEqual(Counter(base_cards)-Counter(candidate_cards),
                         Counter({"Rakdos, Lord of Riots":1,"Inevitable Betrayal":1}))

    def test_competing_keeper_alternative_not_selected_or_silenced(self):
        alt,_,_=parse_list(ALT)
        chosen,_,_=parse_list(ROOT/self.packet["final_candidate"]["path"])
        self.assertIn("Inevitable Betrayal",alt)
        self.assertNotIn("Inevitable Betrayal",chosen)
        self.assertIn("Keeper of Secrets",chosen)
        self.assertNotIn("Keeper of Secrets",alt)
        self.assertEqual(Counter(chosen)-Counter(alt),Counter({"Keeper of Secrets":1}))
        self.assertEqual(Counter(alt)-Counter(chosen),Counter({"Inevitable Betrayal":1}))

    def test_mechanics_known_cases_no_false_complete_m6_or_m7_approval(self):
        p=self.packet
        self.assertTrue(p["whole_deck_audit"]["all_noncommand_cards_reviewed"])
        self.assertEqual(p["verification"]["known_hard_blockers"],[])
        self.assertEqual(p["verification"]["power_bracket"],4)
        self.assertEqual(len(p["verification"]["archidekt_tags"]),3)
        self.assertEqual(p["owner_authority"]["exact_candidate_owner_approved"],False)
        self.assertEqual(p["owner_authority"]["canonical_deck_changed"],False)
        self.assertEqual(p["owner_authority"]["owner_approval_question"],
                         "This deck is complete. Do you approve it?")
        self.assertNotIn(FORBIDDEN,json.dumps(p))
        cases=json.loads(P0.read_text())
        self.assertEqual(len(cases["replay_cases"]),95)
        self.assertEqual(cases["required_open"],[])
        self.assertFalse(cases["authority"]["formal_m6_certified"])
        self.assertEqual(cases["authority"]["m6_6"],"PARTIAL")
        self.assertEqual(cases["authority"]["m6_7"],"PARTIAL")

if __name__=="__main__":
    unittest.main()
