"""M6 I must remain *blocked* until all P0 and qualitative gaps resolved."""
from __future__ import annotations
import copy
import unittest
from scripts.grixis_m6_abaddon_i_blocked import (
    BlockedCertificateFailure, build, check
)

class M6AbaddonBlockedReceiptTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example=build()

    def test_blocked_exact_two_100_card_pool_and_four_new_open(self):
        d=self.example
        self.assertEqual(d["certificate_status"],"blocked")
        self.assertEqual(d["candidate_pool"]["tested_pool_size"],2)
        self.assertFalse(d["local_optimum_for_tested_pool"])
        self.assertFalse(d["phase_b"]["all_required_tests_pass"])
        self.assertEqual(len(d["unresolved_requires_human_judgment"]),5)
        self.assertTrue(check(d))

    def test_adversarial_forged_local_optimum_rejected(self):
        for name in ("fake_pass","fake_optimal","fake_phaseb","fake_finished_reconciliation",
                     "fake_pool_sha","fake_p0_invent","fake_owner_authority",
                     "omit_open_gap","fake_pool_size"):
            with self.subTest(name=name):
                x=copy.deepcopy(self.example)
                if name=="fake_pass": x["certificate_status"]="pass"
                elif name=="fake_optimal":x["local_optimum_for_tested_pool"]=True
                elif name=="fake_phaseb":x["phase_b"]["all_required_tests_pass"]=True
                elif name=="fake_finished_reconciliation":x["reconciliation_complete"]=True
                elif name=="fake_pool_sha":x["candidate_pool"]["source_sha256"]="sha256:"+"0"*64
                elif name=="fake_p0_invent":x["phase_b"]["test_refs"].pop()
                elif name=="fake_owner_authority":x["authority"]["can_decide"]=True
                elif name=="omit_open_gap":x["unresolved_requires_human_judgment"].pop()
                elif name=="fake_pool_size":x["candidate_pool"]["tested_pool_size"]=0
                with self.assertRaises(BlockedCertificateFailure):
                    check(x)

if __name__=="__main__":
    unittest.main()
