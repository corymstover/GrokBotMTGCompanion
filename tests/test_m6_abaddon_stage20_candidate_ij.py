"""Source-bound new Abaddon M6 I local-pool and J candidate-only evidence.

This can pass without M6.10 owner milestone acceptance and without M7 owner
approval. The old official receipt files are preserved, not overwritten.
"""
import hashlib
import json
from pathlib import Path
import re
import sys
import unittest
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import grixis_authority as ga
import grixis_m6_bundle_check as jcheck

I = ROOT / "data/grixis/m6/ij/candidate_certificates/Abaddon_protected_six_stage20_20261023.json"
J = ROOT / "data/grixis/m6/bundles/candidate_exact/Abaddon_protected_six_stage20_20261023.json"
D = ROOT / "data/grixis/m6/ij/adjudications/Abaddon_protected_six_stage20_20261023.json"
OLD = ROOT / "data/grixis/m7/candidate_lists/Abaddon_the_Despoiler_rev2.txt"
NEW = ROOT / "data/grixis/m7/research_challengers/Abaddon_the_Despoiler_stage13_protected_wheel_six_research_20261023.txt"
ORACLE = ROOT / "data/grixis/m6/oracle_snapshots/Abaddon_the_Despoiler_Stage17_95_Source_Reconciled_20261023.json"
ROW = re.compile(r"^(\d+)x (.+?)(?: \[Commander\])?$")


def parse(path):
    result = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = ROW.fullmatch(line)
        if not m:
            raise ValueError("Malformed physical card " + repr(line))
        result.append((int(m.group(1)), m.group(2), line.endswith("[Commander]")))
    return result


class AbaddonStage20CandidateIJ(unittest.TestCase):
    def test_physical_exact_and_logical_sha_bindings(self):
        ad = json.loads(D.read_text(encoding="utf-8"))
        cert = json.loads(I.read_text(encoding="utf-8"))
        bundle = json.loads(J.read_text(encoding="utf-8"))
        o = json.loads(ORACLE.read_text(encoding="utf-8"))
        self.assertEqual(hashlib.sha256(NEW.read_bytes()).hexdigest(), ad["proposed_raw_sha256"])
        self.assertEqual(hashlib.sha256(OLD.read_bytes()).hexdigest(), ad["canonical_locked_raw_sha256"])
        self.assertEqual(ad["proposed_raw_sha256"], o["candidate_sha256"])
        new = parse(NEW)
        old = parse(OLD)
        self.assertEqual(sum(x[0] for x in new), sum(x[0] for x in old))
        self.assertEqual(sum(x[0] for x in new), 100)
        self.assertEqual(new[0], (1, "Abaddon the Despoiler", True))
        entries = [("commander" if cmd else "main", o["oracle_cards"][n]["oracle_id"], q)
                   for q, n, cmd in new]
        logical = ga.logical_hash(entries)
        self.assertEqual(logical, ad["proposed_lh1"])
        self.assertEqual(logical, cert["list_hash"])
        self.assertEqual(logical, bundle["result_hash"])
        oc = Counter({n:q for q,n,_ in old})
        nc = Counter({n:q for q,n,_ in new})
        adds = nc - oc
        cuts = oc - nc
        self.assertEqual(sum(adds.values()), 6)
        self.assertEqual(sum(cuts.values()), 6)
        self.assertEqual(dict(adds), {n:1 for n in ("Impact Tremors","Sanctum of Stone Fangs",
            "Coruscation Mage","Sakashima of a Thousand Faces","Mount Doom",
            "Sheoldred, the Apocalypse")})
        self.assertEqual(dict(cuts), {n:1 for n in ("Thermo-Alchemist","The Ruinous Powers",
            "Kessig Flamebreather","Keeper of Secrets","Mountain","Ponder")})

    def test_schema_and_actual_J_hash_refs(self):
        cert = json.loads(I.read_text(encoding="utf-8"))
        bundle = json.loads(J.read_text(encoding="utf-8"))
        self.assertEqual(ga.validate_file(cert, "zero_improvement_certificate.schema.json"), [])
        reg = json.loads((ROOT / "data/grixis/registry.json").read_text(encoding="utf-8"))
        sealed = json.loads((ROOT / "data/grixis/m6/sealed/reconciliation_manifest.json").read_text(encoding="utf-8"))
        self.assertTrue(jcheck.validate_bundle(bundle, reg, sealed))
        self.assertEqual(cert["candidate_pool"]["tested_pool_size"], 4)
        self.assertEqual(cert["certificate_status"], "pass")
        self.assertTrue(all(not test["supports_improvement_claim"] for test in bundle["phase_b"]["tests"]))
        self.assertTrue(all(test["effect_coverage"] == "bounded_partial" for test in bundle["phase_b"]["tests"]))

    def test_reproducible_scope_is_not_owner_approval(self):
        ad = json.loads(D.read_text(encoding="utf-8"))
        cert = json.loads(I.read_text(encoding="utf-8"))
        bundle = json.loads(J.read_text(encoding="utf-8"))
        self.assertFalse(ad["owner_m7_approval"])
        self.assertFalse(ad["formal_m6_10_owner_acceptance"])
        self.assertFalse(ad["canonical_writes"])
        self.assertTrue(ad["deck3_hold"])
        self.assertEqual(len(ad["tested_pool"]), 4)
        self.assertEqual(sum(x["disposition"].startswith("SELECT") for x in ad["tested_pool"]), 1)
        e = ad["effect_coverage"]
        self.assertEqual(e["historical_named_p0_executed_success"], 104)
        self.assertEqual(e["historical_p0_not_applicable_to_new_candidate"], 27)
        self.assertEqual(e["historical_core_p0_reused_mechanic_facts"], 77)
        self.assertEqual(e["new_candidate_changed_p0_actual_executed_success"], 14)
        self.assertEqual(e["historical_p1_counterfactual"], 3)
        self.assertFalse(cert["authority"]["can_approve_or_lock"])
        self.assertFalse(bundle["authority"]["can_approve_or_lock"])
        self.assertFalse(bundle["authority"]["can_apply_swap"])


if __name__ == "__main__":
    unittest.main()
