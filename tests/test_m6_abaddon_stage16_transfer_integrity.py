"""Fail-closed integrity audit of Abaddon legacy M6 case transfer.

A successful test DOES NOT make historical fixtures current-candidate evidence:
case relevance and original physical source conservation still need authored
adjudication. Preserve the distinction between prior executions and new ones.
"""
import hashlib
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "data/grixis/m6/phase_b_plans"
EVIDENCE = PLAN / "Abaddon_stage16_legacy_candidate_transfer_20261023.json"
LEGACY = PLAN / "abaddon_p0_case_inventory_20261022.json"
STAGE15 = PLAN / "Abaddon_stage15_new_six_changed_effects_20261023.json"
CAND = ROOT / "data/grixis/m7/research_challengers/Abaddon_the_Despoiler_stage13_protected_wheel_six_research_20261023.txt"
CUT_REFERENCES = {
    "Ruinous": "The Ruinous Powers",
    "Keeper": "Keeper of Secrets",
    "Kessig": "Kessig Flamebreather",
    "Thermo-Alchemist": "Thermo-Alchemist",
    "Betrayal": "Inevitable Betrayal",
}


class AbaddonCandidateTransferIntegrity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.plan = json.loads(EVIDENCE.read_text(encoding="utf-8"))
        cls.legacy = json.loads(LEGACY.read_text(encoding="utf-8"))
        cls.stage15 = json.loads(STAGE15.read_text(encoding="utf-8"))
        cls.raw = CAND.read_bytes()
        cls.cards = [m for m in (re.fullmatch(r"(\d+)x (.+?)(?: \[Commander\])?", line) for line in cls.raw.decode("utf-8").splitlines()) if m]
        assert len(cls.cards) == len(cls.raw.decode("utf-8").splitlines())

    def test_candidate_exact_physical_and_authority(self):
        p = self.plan
        self.assertEqual(hashlib.sha256(self.raw).hexdigest(), p["provisional_new_candidate_raw_sha256"])
        self.assertEqual(sum(int(m.group(1)) for m in self.cards), 100)
        self.assertEqual(self.cards[0].group(2), "Abaddon the Despoiler")
        names = {m.group(2) for m in self.cards}
        self.assertTrue(all(c not in names for c in CUT_REFERENCES.values()))
        self.assertTrue(all(p["mechanic_reconciliation_gate"][g] is False
                            for g in ("transfer_done", "all_required_m6_p0_and_p1_satisfied",
                                      "m6_8_candidate_specific_complete", "m6_9_candidate_specific_complete",
                                      "m6_10_owner_accepted", "owner_m7_ready")))

    def test_104_historical_p0_no_false_current_binding(self):
        p = self.plan
        self.assertEqual(self.legacy["source_sha256"], p["legacy_source_baseline_raw_sha256"])
        old = self.legacy["replay_cases"]
        rows = p["old_p0_cases"]
        self.assertEqual(len(old), len(rows))
        self.assertEqual(len({r["id"] for r in rows}), 104)
        nontransfer = 0
        for case, row in zip(old, rows):
            self.assertEqual(case["id"], row["id"])
            self.assertEqual(case["mechanic"], row["topic"])
            self.assertEqual(case["test_file"], row["legacy_test_file"])
            refs = sorted({full for short, full in CUT_REFERENCES.items() if short in case["mechanic"]})
            self.assertEqual(sorted(row["cut_or_preexisting_absent_refs"]), refs)
            flag = bool(refs)
            nontransfer += int(flag)
            self.assertEqual(row["current_candidate_transfer"],
                "HISTORICAL_COUNTERFACTUAL_DO_NOT_COUNT_AS_CURRENT_APPLICABLE_P0"
                if flag else "POTENTIALLY_REUSABLE_UNCHANGED_CORE_REQUIRES_SCOPE_REVIEW")
            self.assertEqual(row["old_execution"], "HISTORICAL_PASS_NOT_NEW_CANDIDATE_EXECUTION")
        self.assertEqual(nontransfer, 20)
        self.assertEqual(p["counts"]["historical_p0_without_named_cut"], 84)

    def test_all_fourteen_new_executed_cases_have_exact_receipt(self):
        p = self.plan
        receipt = self.stage15["execution_receipt"]
        self.assertEqual(receipt["pr_head_sha"], "7d4c079d0f7420753608254ddb33f63e6b8a4fd5")
        self.assertEqual(receipt["workflow_run_id"], 39906969961)
        self.assertEqual(receipt["exact_step_conclusion"], "success")
        self.assertEqual(len(self.stage15["cases"]), 14)
        self.assertEqual(len(p["new_stage15_cases"]), 14)
        for old, new in zip(self.stage15["cases"], p["new_stage15_cases"]):
            self.assertEqual((old["case_id"], old["method"], old["actual_result"]),
                (new["case_id"], new["method"], new["actual_result"]))
            self.assertEqual(new["actual_result"], "PASS_EXACT_HEAD_CI")
        self.assertEqual(p["counts"]["new_stage15_source_bound_p0_pass"], 14)

    def test_fourteen_legacy_p1_are_not_falsely_recertified(self):
        p = self.plan
        rows = p["old_p1_methods"]
        self.assertEqual(len(rows), 14)
        self.assertEqual(len({r["method"] for r in rows}), 14)
        self.assertEqual(sum(r["current_candidate_transfer"].startswith("HISTORICAL_COUNTERFACTUAL") for r in rows), 3)
        for file in sorted({r["test_file"] for r in rows}):
            methods = set(re.findall(r"^\s+def (test_[^(]+)\(", (ROOT / file).read_text(encoding="utf-8"), re.M))
            self.assertEqual({r["method"] for r in rows if r["test_file"] == file}, methods)
        self.assertEqual(p["mechanic_reconciliation_gate"]["transfer_done"], False)


if __name__ == "__main__":
    unittest.main()
