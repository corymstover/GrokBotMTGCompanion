"""Final Abaddon M6 I/J integrity: one selected 100, non-independent Pass C,
bounded effect-aware Phase B, tested-pool only, zero canonical/owner authority.
"""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import unittest

from scripts import grixis_authority as ga
from scripts.grixis_m6_bundle_check import validate_bundle
from scripts.grixis_m6_abaddon_i_final_check import check as check_selected_i, ICompletedEvidenceError

ROOT = Path(__file__).resolve().parents[1]
I = ROOT / "data/grixis/m6/ij/certificates/abaddon-the-despoiler.json"
J = ROOT / "data/grixis/m6/bundles/abaddon-the-despoiler.json"
REG = ROOT / "data/grixis/registry.json"
SEALED = ROOT / "data/grixis/m6/sealed/reconciliation_manifest.json"
SNAP = ROOT / "data/grixis/m6/oracle_snapshots/Abaddon_the_Despoiler_Scryfall_20261022.json"
CAND = ROOT / "data/grixis/m7/candidate_lists/Abaddon_the_Despoiler.txt"
TRACK = ROOT / "data/grixis/milestone_m6_m7_subtracker.json"
SELECTED_LH = "lh1:4bb15eb5acc051871e7d818890f71705eb74f1281e933e73b0e77ff770be1efc"
BASE_LH = "lh1:5a1e5e5bb86ba35d7dbf712fbc3a7d29c3e05a17569c05e8a11976321699b793"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


class AbaddonFinalIJSourceBound(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.i, cls.j = load(I), load(J)
        cls.reg, cls.seals, cls.tracker = load(REG), load(SEALED), load(TRACK)

    def test_actual_pass_scoped_i_certificate_schema_and_source(self):
        i = self.i
        self.assertEqual(ga.validate_file(i, "zero_improvement_certificate.schema.json"), [])
        self.assertTrue(check_selected_i())
        self.assertEqual(i["certificate_status"], "pass")
        self.assertEqual(i["list_hash"], SELECTED_LH)
        self.assertEqual(i["candidate_pool"]["tested_pool_size"], 5)
        p = ROOT / i["candidate_pool"]["source_ref"]
        self.assertEqual("sha256:"+hashlib.sha256(p.read_bytes()).hexdigest(),
                         i["candidate_pool"]["source_sha256"])
        self.assertTrue(i["phase_b"]["all_required_tests_pass"])
        self.assertTrue(i["local_optimum_for_tested_pool"])
        self.assertFalse(i["improving_substitution_found"])
        self.assertEqual(i["unresolved_requires_human_judgment"], [])
        self.assertEqual(i["blockers"], [])
        self.assertFalse(i["authority"]["can_decide"])
        self.assertFalse(i["authority"]["can_approve_or_lock"])

    def test_full_m6_j_checker_validates_committed_bytes(self):
        self.assertEqual(ga.validate_file(self.j, "m6_reproducibility_bundle.schema.json"), [])
        self.assertTrue(validate_bundle(self.j, self.reg, self.seals))
        self.assertEqual(self.j["baseline_hash"], BASE_LH)
        self.assertEqual(self.j["result_hash"], SELECTED_LH)
        self.assertEqual(self.j["bundle_status"], "complete_evidence_not_approval")
        self.assertFalse(any(self.j["authority"].values()))
        self.assertFalse(self.j["pass_c"]["technically_independent"])
        self.assertEqual(self.j["pass_c"]["review_class"], "FORMAL_PASS_C_OWNER_EQUIVALENT")
        self.assertEqual(len(self.j["phase_b"]["tests"]), 3)
        self.assertTrue(self.j["phase_b"]["complete"])
        self.assertFalse(any(x["supports_improvement_claim"] for x in self.j["phase_b"]["tests"]))
        self.assertTrue(all(x["effect_coverage"] == "bounded_partial" for x in self.j["phase_b"]["tests"]))

    def test_dated_oracle_source_100_and_present_approval_protection(self):
        d = load(SNAP)
        self.assertEqual(d["card_identity_count"], 97)
        self.assertEqual(d["chosen_research_candidate_logical_hash"], self.i["list_hash"])
        self.assertEqual(hashlib.sha256(CAND.read_bytes()).hexdigest(),
                         d["chosen_research_candidate_raw_sha256"])
        self.assertEqual(self.tracker["m6"]["formal_m6_certified_decks"], 0)
        self.assertEqual(self.tracker["m7"]["formal_m7_review_decisions"], 0)
        self.assertEqual(self.reg["decks"]["Abaddon_the_Despoiler"]["current_canonical_hash"], BASE_LH)
        self.assertFalse(d["owner_m7_approval"])

    def test_forged_owner_or_oracle_or_pass_c_evidence_is_rejected(self):
        for transform in [
            lambda b: b["authority"].update(can_apply_swap=True),
            lambda b: b["pass_c"].update(technically_independent=True),
            lambda b: b["snapshot"].update(oracle_ref="data/grixis/m6/oracle_snapshots/absent.json"),
            lambda b: b["phase_b"]["tests"][0].update(supports_improvement_claim=True),
            lambda b: b["inputs"][0].update(sha256="sha256:"+"0"*64),
        ]:
            forged = copy.deepcopy(self.j)
            transform(forged)
            with self.assertRaises(ValueError):
                validate_bundle(forged, self.reg, self.seals)

    def test_forged_local_optimum_pass_is_rejected(self):
        for change in [
            {"local_optimum_for_tested_pool": False},
            {"improving_substitution_found": True},
            {"unresolved_requires_human_judgment":["unresolved mandatory gameplay rule"]},
            {"phase_b": {"all_required_tests_pass":False,"test_refs":["counterfeit"]}},
        ]:
            forged = copy.deepcopy(self.i)
            forged.update(change)
            with self.assertRaises(ICompletedEvidenceError):
                check_selected_i(forged)


if __name__ == "__main__":
    unittest.main()
