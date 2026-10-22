"""Abaddon M6.7 interim author judgments: valid evidence, no deck authority."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_authority as ga

RECORD=ROOT/"data/grixis/m6/judgment_reviews/abaddon_phase_b_decisions_20261021.json"
MILESTONE=ROOT/"data/grixis/milestone_m6_m7_subtracker.json"
WAIVER=ROOT/"data/grixis/m6/governance/pass_c_owner_waiver_20261021.json"


class AbaddonJudgmentEvidence(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=json.loads(RECORD.read_text(encoding="utf-8"))
        cls.progress=json.loads(MILESTONE.read_text(encoding="utf-8"))
        cls.waiver=json.loads(WAIVER.read_text(encoding="utf-8"))

    def test_exact_locked_baseline_and_review_provenance(self):
        d=self.data
        self.assertEqual(d["deck_id"],"Abaddon_the_Despoiler")
        c=d["canonical"]
        self.assertEqual((c["card_total"],c["distinct_names"],c["lands"]),(100,94,34))
        self.assertEqual(c["raw_approved_sha256"],"2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf")
        self.assertEqual((c["approval_status"],c["lock_status"],c["changed"]),("APPROVED","LOCKED",False))
        self.assertFalse(d["independent_reviewer"])
        self.assertEqual(d["owner_pass_c_governance_waiver"],str(WAIVER.relative_to(ROOT)))
        self.assertEqual(self.waiver["applies_to"]["gate"],"M6.5")
        self.assertFalse(self.waiver["accepted_substitute"]["technically_independent"])

    def test_four_substantive_named_decision_class_reviews(self):
        cases=self.data["candidates"]
        self.assertEqual({x["card"] for x in cases},{"Aggravated Assault","Chaos Warp","The Ruinous Powers","Grinning Ignus"})
        for item in cases:
            with self.subTest(item=item["card"]):
                j=item["judgment_review"]
                self.assertEqual(j["kind"],"judgment_review")
                self.assertEqual(j["method"],"agent_judgment")
                self.assertIn("ChatGPT/OpenAI GPT-6",j["by"])
                self.assertEqual(j["date"],"2026-10-21")
                self.assertFalse(ga.decision_review_problems(item))
                self.assertGreaterEqual(len(j["evidence_items"]),3)
                self.assertIn("strategic_judgment",{x["class"] for x in j["evidence_items"]})
                self.assertIn("fact",{x["class"] for x in j["evidence_items"]})
                self.assertEqual(set(item["candidate_swap_ids"]),set(j["swaps"]))
                self.assertFalse(item["approved_swap"])

    def test_scripted_only_or_test_only_receipt_is_rejected(self):
        item=copy.deepcopy(self.data["candidates"][0])
        item["judgment_review"]["by"]="scripted output"
        self.assertTrue(ga.decision_review_problems(item))
        item=copy.deepcopy(self.data["candidates"][0])
        item["judgment_review"]["evidence_items"]=[x for x in item["judgment_review"]["evidence_items"] if x["class"]=="test_result"]
        self.assertTrue(ga.decision_review_problems(item))
        item=copy.deepcopy(self.data["candidates"][0])
        item["judgment_review"]["swaps"]=[]
        self.assertTrue(ga.decision_review_problems(item,"Abaddon-Assault-for-Rakdos"))

    def test_ruinous_powers_opponent_is_card_owner(self):
        item=next(x for x in self.data["candidates"] if x["card"]=="The Ruinous Powers")
        self.assertIn("the opponent whose library it came from",item["benefit"])
        self.assertIn("OWNER",item["benefit"])
        self.assertIn("warhammer-40000-commander-release-notes",str(item["judgment_review"]["evidence_items"]))

    def test_grinning_ignus_source_bound_matters_but_not_approved(self):
        item=next(x for x in self.data["candidates"] if x["card"]=="Grinning Ignus")
        self.assertEqual(item["interim_decision"],"HOLD_PRIORITY_TEST_CHALLENGER_NO_APPROVED_SWAP")
        self.assertEqual(item["source_inventory"]["m5_screened_swap_records"],98)
        self.assertEqual(item["source_inventory"]["distinct_candidate_adds"],63)
        r=item["rule_witness"]
        self.assertEqual(r["recasts_with_birgi"],5)
        self.assertEqual(r["cascade_triggers_if_opp_loss_at_least_three"],5)
        self.assertEqual(r["cascade_triggers_if_opp_loss_under_three"],0)
        self.assertEqual(r["recasts_with_rule_of_law"],1)
        self.assertFalse(r["actual_wins_measured"])
        self.assertFalse(item["approved_swap"])
        self.assertFalse(ga.decision_review_problems(item))

    def test_paid_ignus_access_is_genuine_but_not_net_improvement(self):
        item=next(x for x in self.data["candidates"] if x["card"]=="Grinning Ignus")
        r=item["paid_assembly_observation"]
        self.assertIn("physical",r["method"])
        self.assertEqual(r["engine_first_turn10"]["ignus_for_rakdos"]["ignus_cast"],333)
        self.assertEqual(r["engine_first_turn10"]["ignus_for_rakdos"]["five_paid_granted_cascades"],3)
        self.assertEqual(r["engine_first_turn10"]["ignus_for_nightscape"]["five_paid_granted_cascades"],1)
        self.assertEqual(r["engine_first_turn10"]["ignus_for_rite"]["five_paid_granted_cascades"],4)
        self.assertFalse(r["proves_challenger_superiority"])
        self.assertFalse(r["approved_swap"])
        self.assertIsNone(r["true_game_win_rate"])
        self.assertEqual(item["interim_decision"],"HOLD_PRIORITY_TEST_CHALLENGER_NO_APPROVED_SWAP")
        self.assertEqual(self.progress["m6"]["formal_m6_certified_decks"],0)
        self.assertEqual(self.progress["m7"]["formal_m7_review_decisions"],0)

    def test_no_false_m6_m7_or_canonical_promotion(self):
        d=self.data
        self.assertTrue(all(value is False for value in d["authority"].values()))
        self.assertEqual(self.progress["m6"]["gates"][4]["status"],"COMPLETE")
        self.assertEqual(self.progress["m6"]["gates"][4]["completion_basis"],"OWNER_AUTHORIZED_NONINDEPENDENT_PASS_C_SUBSTITUTE")
        self.assertEqual(self.progress["m6"]["gates"][5]["status"],"PARTIAL")
        self.assertEqual(self.progress["m6"]["gates"][6]["status"],"PARTIAL")
        self.assertEqual(self.progress["m6"]["formal_m6_certified_decks"],0)
        self.assertEqual(self.progress["m7"]["formal_m7_review_decisions"],0)
        self.assertEqual(self.progress["accounting"]["canonical_approved_locked"],62)


if __name__=="__main__":
    unittest.main()
