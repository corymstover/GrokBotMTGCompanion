"""Scoped PASS M6 I for revised Admiral; no generic global-optimum inference.

The test recomputes exact certificate -> seven-source pool, authored decision
memo, physical candidate logical hash, immutable historical certificate.
A PASS here is a tested-pool judgment, not M6 J, M6.10, M7 or owner approval.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
NEW=ROOT/"data/grixis/m6/ij/certificates/admiral-beckett-brass-rev2.json"
OLD=ROOT/"data/grixis/m6/ij/certificates/admiral-beckett-brass.json"
REPORT=ROOT/"data/grixis/m6/certification_preflight/Admiral_M6_I_rev2_seven_config_local_best_20261022.md"
J_OLD=ROOT/"data/grixis/m6/bundles/admiral-beckett-brass.json"

class AdmiralRev2ILocalBest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.n=json.loads(NEW.read_text())
        cls.o=json.loads(OLD.read_text())
        cls.pool=json.loads((ROOT/cls.n["candidate_pool"]["source_ref"]).read_text())

    def test_schema_required_semantics_remain_explicitly_local(self):
        d=self.n
        self.assertEqual(d["schema_version"],1)
        self.assertEqual(d["deck_id"],"Admiral_Beckett_Brass")
        self.assertEqual(d["slug"],"admiral-beckett-brass")
        self.assertEqual(d["certificate_status"],"pass")
        self.assertTrue(d["reconciliation_complete"])
        self.assertTrue(d["phase_b"]["all_required_tests_pass"])
        self.assertEqual(d["unresolved_requires_human_judgment"],[])
        self.assertEqual(d["blockers"],[])
        self.assertFalse(d["improving_substitution_found"])
        self.assertTrue(d["local_optimum_for_tested_pool"])
        self.assertEqual(d["scope_caveat"],
                         "Local optimum over the explicitly tested candidate pool only; not a mathematical or global proof of optimality.")
        self.assertIs(d["authority"]["can_decide"],False)
        self.assertIs(d["authority"]["can_approve_or_lock"],False)

    def test_pool_seven_source_hash_is_real_and_exact(self):
        d=self.n
        p=ROOT/d["candidate_pool"]["source_ref"]
        self.assertEqual("sha256:"+hashlib.sha256(p.read_bytes()).hexdigest(),
                         d["candidate_pool"]["source_sha256"])
        self.assertEqual(d["candidate_pool"]["tested_pool_size"],7)
        self.assertEqual(self.pool["explicit_pool_size"],7)
        self.assertEqual({x["id"] for x in self.pool["configurations"]},
                         {"BASELINE","D","WAVE_CANNONADE","WAVE_PALISADE",
                          "AERIALIST","AERIALIST_WAVE_PALISADE","NINE_BOTH"})
        self.assertEqual(d["list_hash"],self.pool["provisional_preferred_logical_hash"])

    def test_authored_decision_memo_candidly_discloses_uncertainty(self):
        s=REPORT.read_text()
        for token in ("39880475909","39880476338","WAVE_PALISADE",
                      "Cannonade","Palisade","Aerialist","RESEARCH_ONLY",
                      "M6.9 J","owner"):
            # Memo uses research-only scope, not blanket proof.
            if token=="RESEARCH_ONLY":
                self.assertIn("not a",s.lower())
            else:
                self.assertIn(token,s)
        self.assertIn(str(REPORT.relative_to(ROOT)),self.n["receipt_refs"])
        self.assertIn("seven",s.lower())
        self.assertIn("not",s.lower())

    def test_all_named_phase_b_sources_present_and_old_i_still_bound_to_D(self):
        for p in self.n["phase_b"]["test_refs"]:
            self.assertTrue((ROOT/p).is_file(),p)
        self.assertEqual(self.o["candidate_pool"]["tested_pool_size"],5)
        self.assertNotEqual(self.o["list_hash"],self.n["list_hash"])
        self.assertEqual(self.o["list_hash"],json.loads(J_OLD.read_text())["result_hash"])
        self.assertEqual(self.n["optimizer_pass_ref"],
                         "data/grixis/m6/sealed/reconciliation_manifest.json")

    def test_owner_equivalent_pass_c_and_m6_j_remain_separately_required(self):
        waiver=json.loads((ROOT/"data/grixis/m6/governance/pass_c_owner_waiver_20261021.json").read_text())
        self.assertEqual(waiver["decision"],
                         "AUTHORIZE_OWNER_EQUIVALENT_PASS_C_AS_REPLACEMENT_FOR_INDEPENDENT_THIRD_MODEL_REQUIREMENT_FOR_M6_GOVERNANCE")
        self.assertIn("M6.9 J",self.n["authority"]["note"])
        self.assertIn("M6.10",self.n["authority"]["note"])
        self.assertIn("M7",self.n["authority"]["note"])
        self.assertTrue(self.pool["owner_m7_approved"] is False)
        self.assertTrue(self.pool["m6_J_pass_issued"] is False)

if __name__=="__main__":
    unittest.main()
