"""Ashad M7 Rev3: exact source-bound M6 I/J reproducibility checks, NO owner authority."""
import hashlib
import json
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_authority as ga
import grixis_m6_bundle_check as j

CERT=ROOT/"data/grixis/m6/ij/certificates/ashad-the-lone-cyberman-m7-rev3.json"
BUNDLE=ROOT/"data/grixis/m6/ij/revision_bundles/ashad-the-lone-cyberman-m7-rev3.json"
POOL=ROOT/"data/grixis/m6/ij/tested_pools/Ashad__the_Lone_Cyberman_M7_Rev3_tested_configurations_20261023.json"
ORACLE=ROOT/"data/grixis/m6/oracle_snapshots/Ashad__the_Lone_Cyberman_M7_Rev3_118_Scryfall_20261023.json"
PREFERRED="data/grixis/m7/candidate_lists/Ashad__the_Lone_Cyberman_ChatGPT_M7_Rev3_Ten_Approval_Candidate.txt"
RAW="352911498345e78bd55773f4c9d1c49d05599610d5fc806f7b779c85eb5f6267"
LOGICAL="lh1:9ebaa891f2ff0e7af81ff2856b54a012c915f8d5cb1936a8ca579579aa8cb8c9"
BASE="087e34c2127859111fc08f8d9ec7d66cd3495537cc571d88e829fd27d2823e25"

def sha(path):
    return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()

class AshadRev3IJ(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.c=json.loads(CERT.read_text(encoding="utf-8"))
        cls.b=json.loads(BUNDLE.read_text(encoding="utf-8"))
        cls.pool=json.loads(POOL.read_text(encoding="utf-8"))
        cls.oracle={c["name"]:c for c in json.loads(ORACLE.read_text(encoding="utf-8"))["cards"]}
        cls.registry=json.loads((ROOT/"data/grixis/registry.json").read_text(encoding="utf-8"))

    def logical(self,path):
        rows=[]
        for line in (ROOT/path).read_text(encoding="utf-8").splitlines():
            q,raw=line.split("x ",1)
            zone="commander" if raw.endswith(" [Commander]") else "main"
            name=raw.removesuffix(" [Commander]")
            rows.append((zone,self.oracle[name]["oracle_id"],int(q)))
        return ga.logical_hash(rows)

    def test_certificate_source_schema_and_scope(self):
        self.assertEqual(ga.validate_file(self.c,"zero_improvement_certificate.schema.json"),[])
        self.assertEqual(self.c["candidate_pool"]["tested_pool_size"],5)
        self.assertEqual(self.c["candidate_pool"]["source_sha256"],
                         "sha256:"+sha(self.c["candidate_pool"]["source_ref"]))
        self.assertEqual(self.c["list_hash"],LOGICAL)
        self.assertEqual(self.c["certificate_status"],"pass")
        self.assertTrue(self.c["local_optimum_for_tested_pool"])
        self.assertFalse(self.c["improving_substitution_found"])
        self.assertFalse(self.c["authority"]["can_approve_or_lock"])
        self.assertFalse(self.c["authority"]["can_decide"])
        self.assertEqual(self.c["scope_caveat"],
                         "Local optimum over the explicitly tested candidate pool only; not a mathematical or global proof of optimality.")
        self.assertNotIn("global proof",self.c["authority"]["note"])

    def test_all_five_full_configs_byte_and_logical_hash(self):
        self.assertEqual(self.pool["explicit_pool_size"],5)
        self.assertFalse(self.pool["owner_m7_approved"])
        self.assertEqual(self.pool["candidate_raw_sha256"],RAW)
        self.assertEqual(self.pool["candidate_logical_hash"],LOGICAL)
        for cfg in self.pool["configurations"]:
            with self.subTest(cfg=cfg["id"]):
                self.assertEqual(sha(cfg["path"]),cfg["raw_sha256"])
                self.assertEqual(self.logical(cfg["path"]),cfg["logical_hash"])
                self.assertEqual(cfg["physical_cards"],100)
        self.assertEqual(self.pool["configurations"][0]["raw_sha256"],BASE)
        self.assertEqual(self.pool["configurations"][3]["raw_sha256"],RAW)

    def test_strict_j_checker_validates_actual_exact_bytes(self):
        self.assertTrue(j.validate_bundle(self.b,j.load(j.REGISTRY),j.load(j.SEALS)))
        self.assertEqual(self.b["result_hash"],LOGICAL)
        self.assertEqual(self.b["baseline_hash"],self.registry["decks"]["Ashad__the_Lone_Cyberman"]["current_canonical_hash"])
        self.assertEqual(self.b["snapshot"]["oracle_ref"],str(ORACLE.relative_to(ROOT)))
        self.assertFalse(self.b["pass_c"]["technically_independent"])
        self.assertFalse(self.b["authority"]["can_approve_or_lock"])
        self.assertFalse(self.b["authority"]["can_decide"])
        inp={i["path"]:i["sha256"] for i in self.b["inputs"]}
        for cfg in self.pool["configurations"]:
            self.assertEqual(inp[cfg["path"]],"sha256:"+sha(cfg["path"]))
        for important in (str(CERT.relative_to(ROOT)),str(POOL.relative_to(ROOT)),
                          str(ORACLE.relative_to(ROOT)),PREFERRED):
            self.assertEqual(inp[important],"sha256:"+sha(important))
        self.assertTrue(all(not t["supports_improvement_claim"] for t in self.b["phase_b"]["tests"]))
        self.assertEqual(self.b["bundle_status"],"complete_evidence_not_approval")

    def test_bad_digest_denied_and_preserved_first_pass_bundle(self):
        historical=ROOT/"data/grixis/m6/ij/revision_bundles/ashad-the-lone-cyberman-m7.json"
        h=json.loads(historical.read_text(encoding="utf-8"))
        self.assertEqual(h["result_hash"],"lh1:672c3945d8fd2f44a7d03dce4672b9d4aa25391a26b8c1607b5242ca05cc946f")
        self.assertTrue(j.validate_bundle(h,j.load(j.REGISTRY),j.load(j.SEALS)))
        fake=json.loads(BUNDLE.read_text(encoding="utf-8"))
        fake["inputs"][0]["sha256"]="sha256:"+"0"*64
        with self.assertRaises(ValueError):
            j.validate_bundle(fake,j.load(j.REGISTRY),j.load(j.SEALS))

if __name__=="__main__":
    unittest.main()
