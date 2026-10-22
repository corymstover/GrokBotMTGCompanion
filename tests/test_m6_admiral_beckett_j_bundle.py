"""Additional fail-closed logical/raw binding for Admiral's J evidence bundle.

The repository's canonical grixis_m6_bundle_check.py verifies all on-repo
Pass-C, sealed A/B and input bytes at exact PR head; this suite independently
recomputes the *proposed 100-card result* and refuses owner authority.
"""

from collections import Counter
import hashlib
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
BUNDLE = ROOT / "data/grixis/m6/bundles/admiral-beckett-brass.json"
CERT = ROOT / "data/grixis/m6/ij/certificates/admiral-beckett-brass.json"
BASE = ROOT / "data/grixis/m6/authority_snapshots/Admiral_Beckett_Brass_Canonical_Approved_20261022.txt"
CAND = ROOT / "data/grixis/m7/research_challengers/Admiral_Beckett_Brass_evasive_pirate_density_package.txt"
ORACLE = ROOT / "data/grixis/m7/research_challengers/Admiral_Beckett_Brass_Full_Source_Oracle_20261022.json"
BASE_RAW = "4ba5c483eb67b5f2647d375450adf9c2b7e79a036d0ba1866e58de8441bf3414"
CAND_RAW = "201a1d5fc90e30d6aff9a565603fcf8caef69604dad2c07b4951be2b41cc92ee"


def deck_and_hash(path: Path, oracle: dict) -> tuple[Counter[str], str]:
    cards = Counter()
    zones = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        n, named = line.split("x ", 1)
        commander = named.endswith(" [Commander]")
        name = named.removesuffix(" [Commander]")
        assert name not in cards
        cards[name] = int(n)
        zones[name] = "commander" if commander else "main"
    rows = sorted(f'{zones[n]}|{oracle[n]["oracle_id"]}|{q}' for n, q in cards.items())
    logical = "lh1:" + hashlib.sha256("".join(r + "\n" for r in rows).encode()).hexdigest()
    return cards, logical


class AdmiralJBindingTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bundle = json.loads(BUNDLE.read_text(encoding="utf-8"))
        cls.i_certificate = json.loads(CERT.read_text(encoding="utf-8"))
        cls.oracle = {c["name"]: c for c in json.loads(ORACLE.read_text(encoding="utf-8"))["cards"]}

    def test_j_source_binds_current_approved_and_exact_proposed_100(self):
        b = self.bundle
        self.assertEqual(hashlib.sha256(BASE.read_bytes()).hexdigest(), BASE_RAW)
        self.assertEqual(hashlib.sha256(CAND.read_bytes()).hexdigest(), CAND_RAW)
        base, base_lh = deck_and_hash(BASE, self.oracle)
        candidate, candidate_lh = deck_and_hash(CAND, self.oracle)
        self.assertEqual(sum(base.values()), 100)
        self.assertEqual(sum(candidate.values()), 100)
        self.assertEqual(b["baseline_hash"], base_lh)
        self.assertEqual(b["result_hash"], candidate_lh)
        self.assertEqual(candidate_lh, self.i_certificate["list_hash"])
        self.assertEqual((candidate - base)["Broadside Bombardiers"], 1)
        self.assertEqual(sum((candidate - base).values()), 5)
        self.assertEqual(sum((base - candidate).values()), 5)

    def test_source_and_rules_references_have_real_bytes(self):
        b = self.bundle
        self.assertEqual(b["snapshot"]["birthday_id"], "birthday-20261017-6e5c604e1459")
        for key in ("oracle_ref", "rules_ref", "legality_ref"):
            self.assertTrue((ROOT / b["snapshot"][key]).is_file())
        for entry in b["inputs"]:
            p = ROOT / entry["path"]
            if p.is_file():
                self.assertEqual("sha256:" + hashlib.sha256(p.read_bytes()).hexdigest(), entry["sha256"])
        self.assertTrue(all(c["legalities"]["commander"] == "legal" for c in self.oracle.values()))
        self.assertTrue(all(set(c["color_identity"]) <= {"U", "B", "R"} for c in self.oracle.values()))

    def test_pass_c_waiver_and_phase_b_limit_never_claim_independent_games(self):
        b = self.bundle
        self.assertEqual(b["pass_c"]["review_class"], "FORMAL_PASS_C_OWNER_EQUIVALENT")
        self.assertEqual(b["pass_c"]["reviewer"], "ChatGPT/OpenAI GPT-6")
        self.assertIs(b["pass_c"]["technically_independent"], False)
        self.assertIs(b["phase_b"]["complete"], True)
        self.assertGreaterEqual(len(b["phase_b"]["tests"]), 7)
        for t in b["phase_b"]["tests"]:
            self.assertEqual(t["verdict"], "pass")
            self.assertEqual(t["effect_coverage"], "bounded_partial")
            self.assertFalse(t["supports_improvement_claim"])
            self.assertTrue(t["limitations"])
            p = ROOT / t["test_ref"]
            if p.is_file():
                self.assertEqual("sha256:" + hashlib.sha256(p.read_bytes()).hexdigest(), t["source_sha256"])

    def test_j_bundle_reports_no_owner_authority_and_only_i_local_best(self):
        b = self.bundle
        self.assertEqual(self.i_certificate["certificate_status"], "pass")
        self.assertEqual(self.i_certificate["candidate_pool"]["tested_pool_size"], 5)
        self.assertEqual(b["bundle_status"], "complete_evidence_not_approval")
        self.assertFalse(b["authority"]["can_decide"])
        self.assertFalse(b["authority"]["can_apply_swap"])
        self.assertFalse(b["authority"]["can_approve_or_lock"])
        self.assertEqual(b["unresolved_material_questions"], [])
        for k in ("mana_analysis", "red_team"):
            p = ROOT / b[k]["report_path"]
            self.assertEqual("sha256:" + hashlib.sha256(p.read_bytes()).hexdigest(), b[k]["sha256"])


if __name__ == "__main__":
    unittest.main()
