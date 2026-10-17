"""Adversarial redaction tests for M6 independent runner projections."""
import copy
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_m6_blind_replay as m
import grixis_m6_sealed as sealed

class TestM6BlindReplay(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.doc=sealed.load_document("abaddon-the-despoiler")

    def test_project_a_does_not_depend_on_test_verdicts(self):
        doc=copy.deepcopy(self.doc)
        pa=m.sanitized("A",doc)
        for t in doc.get("tests",[]):
            t["verdict"]="fail"
            t["limitations"]=["canary secret"]
        self.assertEqual(pa,m.sanitized("A",doc))

    def test_project_b_does_not_depend_on_blueprints(self):
        doc=copy.deepcopy(self.doc)
        pb=m.sanitized("B",doc)
        for c in doc.get("candidates",[]):
            rv=c.get("review")
            if rv:
                rv["blueprint"]={"anti_goal":True,"fit":"weak","named_by":[]}
        self.assertEqual(pb,m.sanitized("B",doc))

    def test_side_a_stable_under_repeat_projection(self):
        doc=m.sanitized("A",self.doc)
        self.assertEqual(sealed.pass_output("A",self.doc),sealed.pass_output("A",doc))

    def test_side_b_stable_under_repeat_projection(self):
        doc=m.sanitized("B",self.doc)
        self.assertEqual(sealed.pass_output("B",self.doc),sealed.pass_output("B",doc))

    def test_m5_source_does_not_have_approval_authority(self):
        for side in ("A","B"):
            p=m.sanitized(side,self.doc)
            self.assertNotIn("approval",p)
            self.assertNotIn("accepted_by",p)
            self.assertNotIn("reconciliation",p)


if __name__=="__main__":
    unittest.main()
