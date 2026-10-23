"""Research-only source tests for Abaddon reopen after Admiral owner approval.

These assertions prevent research hypotheticals from being mistaken for an
approved replacement, an Oracle rules pass, or a new M6/M7 milestone.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
REOPEN=ROOT/"data/grixis/m7/research_challengers/Abaddon_the_Despoiler_post_Admiral_EDHREC_20261022.json"
BASE=ROOT/"data/grixis/m7/candidate_lists/Abaddon_the_Despoiler_rev2.txt"
APPROVED_SHA="0d9f6df80cafc2a380199b7aec8112e4e54ccfec70024679607032cdf10f5790"
BASICS={"Island","Mountain","Swamp"}


def cards(p):
    lines=p.read_text(encoding="utf-8").splitlines()
    count=Counter()
    for line in lines:
        qty,name=line.split("x ",1)
        count[name.removesuffix(" [Commander]")]+=int(qty)
    return lines,count


class AbaddonPostAdmiralResearch(unittest.TestCase):
    def test_new_edhrec_discovery_not_mistaken_for_approval(self):
        research=json.loads(REOPEN.read_text(encoding="utf-8"))
        self.assertEqual(research["status"],"RESEARCH_ONLY_NOT_OWNER_PRESENTABLE")
        self.assertEqual(research["canonical_approved_sha256"],APPROVED_SHA)
        self.assertEqual(research["canonical_approval_status"],"APPROVED_LOCKED_PRESERVE")
        self.assertFalse(research["hard_gate"]["owner_ready"])
        self.assertTrue(research["hard_gate"]["genuine_improvements_not_yet_established"])
        self.assertEqual(research["hard_gate"]["against_current_locked_baseline_new_swaps_in_each_trial"],2)
        self.assertEqual(research["crosswalk"]["summary"]["top_cards_present"],9)
        self.assertEqual(research["crosswalk"]["summary"]["high_lift_present"],1)
        self.assertEqual(len(research["crosswalk"]["summary"]["new_distinct_absent_cards_to_triage"]),12)
        self.assertIn("Blood for the Blood God!",research["crosswalk"]["summary"]["new_distinct_absent_cards_to_triage"])
        self.assertIn("Spear Spewer",research["crosswalk"]["summary"]["new_distinct_absent_cards_to_triage"])
        self.assertIn("Aurora Phoenix",research["crosswalk"]["summary"]["new_distinct_absent_cards_to_triage"])
        self.assertGreaterEqual(len(research["preliminary_judgments"]),10)
        self.assertTrue(all("SELECT_ADD" != x["status"] for x in research["preliminary_judgments"]))

    def test_two_exact_full_100_source_trials_not_owner_presentable(self):
        research=json.loads(REOPEN.read_text(encoding="utf-8"))
        self.assertEqual(hashlib.sha256(BASE.read_bytes()).hexdigest(),APPROVED_SHA)
        base_lines,base=cards(BASE)
        self.assertEqual(base_lines[0],"1x Abaddon the Despoiler [Commander]")
        self.assertEqual(sum(base.values()),100)
        self.assertEqual(len(base),94)
        self.assertEqual(sum(base[k] for k in BASICS),9)
        for candidate in research["complete_100_research_variants"]:
            with self.subTest(candidate=candidate["name"]):
                p=ROOT/candidate["path"]
                lines,now=cards(p)
                self.assertEqual(hashlib.sha256(p.read_bytes()).hexdigest(),candidate["raw_sha256"])
                self.assertEqual(lines[0],base_lines[0])
                self.assertEqual(sum(now.values()),100)
                self.assertEqual(len(now),94)
                self.assertTrue(all(n==1 or k in BASICS for k,n in now.items()))
                self.assertEqual(set((now-base).elements()),set(candidate["adds"]))
                self.assertEqual(set((base-now).elements()),set(candidate["cuts"]))
                self.assertEqual(sum((now-base).values()),2)
                self.assertEqual(sum((base-now).values()),2)
                self.assertTrue(candidate["status"].startswith("RESEARCH_ONLY"))

    def test_approved_abaddon_receipt_preserved_after_owner_requested_reopening(self):
        r=json.loads((ROOT/"data/grixis/m7/owner_approvals/Abaddon_the_Despoiler_M7_20261022.json").read_text(encoding="utf-8"))
        self.assertEqual(r["approved_raw_sha256"],APPROVED_SHA)
        self.assertEqual(r["owner_decision"],"APPROVE_EXACT_CANDIDATE")
        self.assertTrue(r["canonical_verified"])


if __name__=="__main__":
    unittest.main()
