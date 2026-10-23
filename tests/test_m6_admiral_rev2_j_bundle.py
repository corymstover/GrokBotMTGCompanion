"""Admiral exact revised M6.9 J result bundle; preserve historical D J.

Runs the repository's actual M6 final schema/byte checker ON THIS NEW
candidate-specific sidecar, then additionally verifies the revised physical
and logical 100-card result. The normal 62-roster root J scanner is untouched;
M6.10 and M7 owner acceptance are not granted.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_m6_bundle_check as standard

BUNDLE=ROOT/"data/grixis/m6/ij/revision_bundles/admiral-beckett-brass-rev2.json"
OLD_BUNDLE=ROOT/"data/grixis/m6/bundles/admiral-beckett-brass.json"
NEW_I=ROOT/"data/grixis/m6/ij/certificates/admiral-beckett-brass-rev2.json"
OLD_I=ROOT/"data/grixis/m6/ij/certificates/admiral-beckett-brass.json"
SNAPSHOT=ROOT/"data/grixis/m6/oracle_snapshots/Admiral_Beckett_Brass_rev2_97_Scryfall_20261022.json"
CAND=ROOT/"data/grixis/m7/research_challengers/Admiral_Beckett_Brass_six_Wave_Palisade_draw_resilient_20261022.txt"
BASE=ROOT/"data/grixis/m6/authority_snapshots/Admiral_Beckett_Brass_Canonical_Approved_20261022.txt"

def physical(path):
    cards=Counter()
    zone={}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line:
            continue
        q,raw=line.split("x ",1)
        name=raw.removesuffix(" [Commander]")
        if name in cards:
            raise ValueError("duplicate "+name)
        cards[name]=int(q)
        zone[name]="commander" if raw.endswith(" [Commander]") else "main"
    return cards,zone

def logical(cards,zones,oracle):
    rows=sorted(f'{zones[n]}|{oracle[n]["oracle_id"]}|{v}' for n,v in cards.items())
    return "lh1:"+hashlib.sha256("".join(s+"\n" for s in rows).encode()).hexdigest()

class AdmiralRev2JBound(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.b=json.loads(BUNDLE.read_text())
        cls.i=json.loads(NEW_I.read_text())
        cls.o=json.loads(SNAPSHOT.read_text())
        cls.oracle={x["name"]:x for x in cls.o["cards"]}

    def test_actual_authoritative_j_schema_byte_checker_passes_sidecar(self):
        registry=standard.load(standard.REGISTRY)
        seals=standard.load(standard.SEALS)
        self.assertTrue(standard.validate_bundle(self.b,registry,seals))
        self.assertEqual(self.b["bundle_status"],"complete_evidence_not_approval")
        self.assertFalse(self.b["authority"]["can_decide"])
        self.assertFalse(self.b["authority"]["can_apply_swap"])
        self.assertFalse(self.b["authority"]["can_approve_or_lock"])

    def test_new_j_result_is_new_exact_100_raw_and_logical_not_old_D(self):
        b=self.b
        cards,zones=physical(CAND)
        base,bzones=physical(BASE)
        self.assertEqual(sum(cards.values()),100)
        self.assertEqual(len(cards),97)
        self.assertEqual(hashlib.sha256(CAND.read_bytes()).hexdigest(),
                         "ff5f54f9f608ab0facd62fd3b79df16a0255b4dbbc12d39154a127f27bb8c000")
        self.assertEqual(logical(cards,zones,self.oracle),b["result_hash"])
        self.assertEqual(b["result_hash"],self.i["list_hash"])
        self.assertEqual(sum((cards-base).values()),6)
        self.assertEqual(sum((base-cards).values()),6)
        full={x["name"]:x for x in json.loads((ROOT/"data/grixis/m7/research_challengers/Admiral_Beckett_Brass_Full_Source_Oracle_20261022.json").read_text())["cards"]}
        self.assertEqual(b["baseline_hash"],logical(base,bzones,full))
        self.assertNotEqual(b["result_hash"],json.loads(OLD_BUNDLE.read_text())["result_hash"])
        self.assertNotEqual(self.i["list_hash"],json.loads(OLD_I.read_text())["list_hash"])

    def test_exact_full_oracle_sources_legality_and_pirate_color(self):
        self.assertEqual(self.o["unique_names"],97)
        self.assertEqual(self.o["candidate_raw_sha256"],hashlib.sha256(CAND.read_bytes()).hexdigest())
        self.assertEqual(self.o["candidate_logical_hash"],self.b["result_hash"])
        self.assertEqual(self.o["project_exceptions"],[])
        self.assertTrue(self.o["all_commander_legal"])
        self.assertTrue(self.o["grixis_identity_all"])
        self.assertEqual(set(physical(CAND)[0]),set(self.oracle))
        for x in self.oracle.values():
            self.assertEqual(x["commander_legality"],"legal")
            self.assertTrue(set(x["color_identity"])<={"B","R","U"})
            self.assertIn(x["source_ref"],self.o["sources"])

    def test_required_phase_b_and_new_i_sources_are_byte_bound(self):
        b=self.b
        self.assertEqual(self.i["certificate_status"],"pass")
        self.assertEqual(self.i["candidate_pool"]["tested_pool_size"],7)
        paths={p["path"] for p in b["inputs"]}
        self.assertIn(str(NEW_I.relative_to(ROOT)),paths)
        self.assertIn(str(CAND.relative_to(ROOT)),paths)
        self.assertIn(str(SNAPSHOT.relative_to(ROOT)),paths)
        self.assertIn("data/grixis/m6/ij/tested_pools/Admiral_Beckett_Brass_rev2_seven_configurations_20261022.json",paths)
        tests={x["test_ref"] for x in b["phase_b"]["tests"]}
        for required in ("tests/test_m7_admiral_stage8_wave_palisade_paid_combat.py",
                         "tests/test_m6_admiral_rev2_candidate_source_bind.py",
                         "tests/test_m6_admiral_rev2_seven_configuration_pool.py",
                         "tests/test_m6_admiral_rev2_i_local_best.py"):
            self.assertIn(required,tests)
        self.assertTrue(all(x["verdict"]=="pass" for x in b["phase_b"]["tests"]))
        self.assertTrue(all(x["effect_coverage"]=="bounded_partial" and not x["supports_improvement_claim"] for x in b["phase_b"]["tests"]))

    def test_waived_pass_c_is_explicitly_nonindependent_and_no_approval(self):
        p=self.b["pass_c"]
        self.assertEqual(p["reviewer"],"ChatGPT/OpenAI GPT-6")
        self.assertEqual(p["review_class"],"FORMAL_PASS_C_OWNER_EQUIVALENT")
        self.assertIs(p["technically_independent"],False)
        self.assertIn("pass_c_owner_waiver_20261021.json",p["waiver_receipt_path"])
        # Sidecar deliberately kept outside root 62-bundle final index, so no
        # duplicate slug silently replaces the historical D or owner approval.
        self.assertNotEqual(BUNDLE.parent,standard.BUNDLES)
        self.assertEqual(json.loads(OLD_BUNDLE.read_text())["result_hash"],
                         "lh1:1f6ae6fa721c3bd7e8b888c4a216edca7cdb25c587d5ce812282662cb0118d58")

if __name__=="__main__":
    unittest.main()
