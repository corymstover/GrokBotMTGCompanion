"""Progress sub-tracker: fail closed on unsupported promotion, not a new milestone authority."""
from pathlib import Path
import json,unittest
ROOT=Path(__file__).resolve().parents[1]
TRACKER=ROOT/"data/grixis/milestone_m6_m7_subtracker.json"
REG=ROOT/"data/grixis/registry.json"
PREF=ROOT/"data/grixis/m6/preflight.json"
SEAL=ROOT/"data/grixis/m6/sealed/reconciliation_manifest.json"

def validate(t,r,p,s):
 assert t["schema_version"]==1
 assert len(r["decks"])==62 and t["accounting"]["canonical_total"]==62
 assert t["accounting"]["canonical_approved_locked"]==62
 assert t["accounting"]["m8_certified"]==0
 assert r["program"]["milestones"]["M6"]["status"]==t["m6"]["status"]=="in_progress"
 assert r["program"]["milestones"]["M7"]["status"]==t["m7"]["status"]=="not_started"
 assert r["program"]["milestones"]["M6"]["accepted_by"] is None
 assert r["program"]["milestones"]["M7"]["accepted_by"] is None
 assert len(t["m6"]["gates"])==10 and len(t["m7"]["gates"])==6
 assert len({a["id"] for a in t["m6"]["gates"]})==10
 assert len({a["id"] for a in t["m7"]["gates"]})==6
 assert t["display"]["m6_total_gates"]==10 and t["display"]["m7_total_gates"]==6
 assert t["display"]["m6_completed_gates"]==sum(a["status"]=="COMPLETE" for a in t["m6"]["gates"])
 assert t["display"]["m7_completed_gates"]==sum(a["status"]=="COMPLETE" for a in t["m7"]["gates"])
 assert t["display"]["m6_gate_completion_percent"]==100*t["display"]["m6_completed_gates"]/10
 assert t["display"]["m7_gate_completion_percent"]==100*t["display"]["m7_completed_gates"]/6
 assert t["display"]["m6_partial_gates"]==sum(a["status"]=="PARTIAL" for a in t["m6"]["gates"])
 assert t["display"]["m6_unfulfilled_gates"]==10-t["display"]["m6_completed_gates"]
 assert p["counts"]["accepted_m5_input_complete"]==62
 assert s["counts"]["decks"]==62
 assert s["counts"]["deep_review"]==8848
 assert s["pass_c"]["complete"] is False
 assert t["m6"]["gates"][3]["completed"]==27
 assert t["m6"]["gates"][3]["status"]=="PARTIAL"
 case=json.loads((ROOT/"data/grixis/m6/author_reviews/cycle128_six_commander_authored_judgments_01.json").read_text())
 assert case["review_count"]==6 and len(case["rows"])==6 and case["historical_authored_count_before"]==15
 assert case["authored_count_after_if_verified"]==21
 r129=json.loads((ROOT/"data/grixis/m6/author_reviews/cycle129_six_detailed_01.json").read_text())
 assert r129["review_count"]==len(r129["rows"])==6 and r129["authored_if_verified"]==27
 assert len({x["deck_id"] for x in r129["rows"]})==6
 assert all(x["approved_swaps"]==0 and not x["independent_pass_c"] and not x["complete_phase_b"] for x in r129["rows"])
 assert len({x["deck_id"] for x in case["rows"]})==6
 assert all(x["disposition"]=="HOLD_EXISTING_LIST_NO_SWAP" and x["independent_pass_c_completed"] is False and x["approved_swaps"]==0 for x in case["rows"])
 assert t["m6"]["formal_m6_certified_decks"]==0
 assert t["m7"]["formal_m7_review_decisions"]==0
 assert t["m6"]["gates"][4]["status"]=="BLOCKED" and t["m6"]["gates"][4]["completed"]==0
 assert t["m6"]["gates"][5]["status"]=="PARTIAL" and t["m6"]["gates"][5]["completed"]==0
 assert t["m6"]["gates"][7]["completed"]==0 and t["m6"]["gates"][8]["completed"]==0
 assert t["m7"]["gates"][1]["completed"]==0
 assert t["update_contract"]["prefer_live_registry_and_evidence_over_this_snapshot"]
 assert t["update_contract"]["never_accept_a_milestone_or_modify_canonical_decks_from_tracker_update"]
 for milestone in ("m6","m7"):
  for gate in t[milestone]["gates"]:
   assert gate["status"] in ("COMPLETE","PARTIAL","BLOCKED","NOT_STARTED")
   assert isinstance(gate["title"],str) and gate["title"].strip()
   assert gate["evidence"]
   assert gate["completed"]>=0
   if gate["total"] is not None:assert gate["completed"]<=gate["total"]

class TestMilestoneSubtracker(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.t=json.loads(TRACKER.read_text())
  cls.r=json.loads(REG.read_text())
  cls.p=json.loads(PREF.read_text())
  cls.s=json.loads(SEAL.read_text())
 def test_snapshot_matches_current_engineering_milestones(self):
  validate(self.t,self.r,self.p,self.s)
 def test_false_M6_acceptance_is_rejected(self):
  import copy
  d=copy.deepcopy(self.r)
  d["program"]["milestones"]["M6"]["status"]="accepted"
  with self.assertRaises(AssertionError):validate(self.t,d,self.p,self.s)
 def test_false_independent_pass_c_is_rejected(self):
  import copy
  d=copy.deepcopy(self.s);d["pass_c"]["complete"]=True
  with self.assertRaises(AssertionError):validate(self.t,self.r,self.p,d)
 def test_false_percentage_is_rejected(self):
  import copy
  t=copy.deepcopy(self.t);t["display"]["m6_gate_completion_percent"]=90
  with self.assertRaises(AssertionError):validate(t,self.r,self.p,self.s)
 def test_premature_cycle2_review_claim_is_rejected(self):
  import copy
  t=copy.deepcopy(self.t);t["m7"]["formal_m7_review_decisions"]=62
  with self.assertRaises(AssertionError):validate(t,self.r,self.p,self.s)
 def test_no_canonical_reapproval_claim(self):
  self.assertIn("do not count",self.t["accounting"]["warning"].lower())
  self.assertEqual(self.t["accounting"]["canonical_approved_locked"],62)
  self.assertEqual(self.t["m6"]["formal_m6_certified_decks"],0)
  self.assertEqual(self.t["m7"]["formal_m7_review_decisions"],0)
if __name__=="__main__":unittest.main()
