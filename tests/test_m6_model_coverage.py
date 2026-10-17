"""Negative-case M6 proxy evidence truthfulness gates."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_m6_model_coverage as mod
import grixis_authority as ga


class TestProxyCoverage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.p=mod.PACKETS/"abaddon-the-despoiler.json"
        cls.packet=mod.load(cls.p)

    def test_real_unmodeled_positive(self):
        item=self.packet["items"][0]
        res=mod.inspect_item(item)
        self.assertTrue(res["has_positive_proxy_verdict"])
        self.assertTrue(res["swapped_effects_unmodeled"])
        self.assertFalse(res["supports_improvement_claim"])
        self.assertEqual(res["reason"],"M5_goldfish_unmodeled_effects")

    def test_positive_known_partial_also_blocked(self):
        item=copy.deepcopy(self.packet["items"][0])
        item["test_evidence"]["tests"][0]["limitations"]=["bounds exclude opponent responses"]
        res=mod.inspect_item(item)
        self.assertEqual(res["reason"],"M5_goldfish_incomplete_or_unknown_coverage")
        self.assertFalse(res["supports_improvement_claim"])

    def test_no_positive_test(self):
        item=copy.deepcopy(self.packet["items"][0])
        item["test_evidence"]["tests"][0]["verdict"]="no_detectable_difference"
        self.assertEqual(mod.inspect_item(item)["reason"],"M5_exploratory_no_positive_verdict")

    def test_schema_rejects_upgrade_claim(self):
        doc=mod.derive(self.packet,self.p)
        doc["items"][0]["supports_improvement_claim"]=True
        self.assertTrue(ga.validate_file(doc,"m6_model_coverage.schema.json"))

    def test_schema_rejects_claim_count(self):
        doc=mod.derive(self.packet,self.p)
        doc["counts"]["claim_eligible_from_M5"]=1
        self.assertTrue(ga.validate_file(doc,"m6_model_coverage.schema.json"))

    def test_packet_identity_checked(self):
        doc=mod.derive(self.packet,self.p)
        self.assertEqual(doc["counts"]["hypotheses"],98)
        self.assertEqual(doc["authority"]["can_approve_or_lock"],False)


if __name__=="__main__":
    unittest.main()
