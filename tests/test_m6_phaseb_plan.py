"""M6 preregistration negative cases."""
import copy
import json
import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_m6_phaseb_plan as pp
import grixis_authority as ga

class TestPlan(unittest.TestCase):
    def test_plan_verifies(self):
        pp.validate()
    def test_schema_rejects_claimed_tests(self):
        d=json.loads(pp.PLAN.read_text())
        d["counts"]["phase_b_tests_completed"]=1
        self.assertTrue(ga.validate_file(d,"m6_phase_b_plan.schema.json"))
    def test_schema_rejects_swap_permission(self):
        d=json.loads(pp.PLAN.read_text())
        d["authority"]["can_apply_swap"]=True
        self.assertTrue(ga.validate_file(d,"m6_phase_b_plan.schema.json"))
    def test_each_preregistered_swap_is_in_packet(self):
        d=json.loads(pp.PLAN.read_text())
        p=json.loads(pp.PACKET.read_text())
        orig={r["swap_id"]:r["add"] for r in p["items"]}
        for g in d["groups"]:
            self.assertTrue(all(orig.get(i)==g["candidate"] for i in g["swap_ids"]))

if __name__=="__main__":
    unittest.main()
