"""Candidate-specific M6 I / J evidence for the Anhelo, the Painter M7 candidate.

Recomputes bound byte and logical hashes, runs the authoritative J bundle checker,
and asserts the I certificate stays tested-pool-local with no approval/lock claim.
"""
import hashlib
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import grixis_authority as ga  # noqa: E402
import grixis_m6_bundle_check as standard  # noqa: E402

D = "Anhelo__the_Painter"
CERT = ROOT / "data/grixis/m6/ij/certificates/anhelo-the-painter-m7.json"
BUNDLE = ROOT / "data/grixis/m6/ij/revision_bundles/anhelo-the-painter-m7.json"
POOL = ROOT / "data/grixis/m6/ij/tested_pools/Anhelo__the_Painter_M7_tested_configurations_20261023.json"
SNAP = ROOT / "data/grixis/m6/oracle_snapshots/Anhelo__the_Painter_M7_Scryfall_20261023.json"
MEMO = ROOT / "data/grixis/m6/certification_preflight/Anhelo__the_Painter_M6_I_local_best_20261023.md"
PACKET = ROOT / "data/grixis/m7/decision_reviews/Anhelo__the_Painter.json"
CANON_RAW = "8d5f8a9bd4fcdcd164aab63150c14dc69a814a4d9fd764876de3214d3adf9972"
HIST = "d19d94b8a96fb27a760c7b7d9181221f74bd61642d1d1dd7644fc1c59c09839e"
CAND_RAW = "2c696db8013b90459b23495f8c6a94426ca86ba180a163a8a941d5c285950a58"


def sha(p):
    return hashlib.sha256((ROOT / p).read_bytes()).hexdigest()


class AnheloThePainterM7IJ(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.c = json.loads(CERT.read_text())
        cls.b = json.loads(BUNDLE.read_text())
        cls.pool = json.loads(POOL.read_text())
        cls.o = {x["name"].split(" // ")[0]: x for x in json.loads(SNAP.read_text())["cards"]}
        cls.reg = json.loads((ROOT / "data/grixis/registry.json").read_text())["decks"][D]

    def lh(self, path):
        rows = []
        for line in (ROOT / path).read_text(encoding="utf-8").splitlines():
            if line.strip():
                q, raw = line.split("x ", 1)
                z = "commander" if raw.endswith(" [Commander]") else "main"
                rows.append((z, self.o[raw.removesuffix(" [Commander]").split(" // ")[0]]["oracle_id"], int(q)))
        return ga.logical_hash(rows)

    def test_certificate_schema_and_local_only_scope(self):
        self.assertEqual(ga.validate_file(self.c, "zero_improvement_certificate.schema.json"), [])
        self.assertEqual(self.c["certificate_status"], "pass")
        self.assertFalse(self.c["improving_substitution_found"])
        self.assertIs(self.c["authority"]["can_decide"], False)
        self.assertIs(self.c["authority"]["can_approve_or_lock"], False)
        self.assertIn("not a mathematical or global proof", self.c["scope_caveat"])
        self.assertFalse(any("actions/runs" in r for r in self.c["receipt_refs"]))
        for t in self.c["phase_b"]["test_refs"]:
            self.assertTrue((ROOT / t).is_file(), t)

    def test_pool_every_configuration_raw_and_logical_hash(self):
        self.assertEqual("sha256:" + sha(self.c["candidate_pool"]["source_ref"]), self.c["candidate_pool"]["source_sha256"])
        self.assertEqual(self.c["candidate_pool"]["tested_pool_size"], len(self.pool["configurations"]))
        for cfg in self.pool["configurations"]:
            self.assertEqual(sha(cfg["path"]), cfg["raw_sha256"], cfg["id"])
            self.assertEqual(self.lh(cfg["path"]), cfg["logical_hash"], cfg["id"])
        ids = {x["id"]: x for x in self.pool["configurations"]}
        self.assertEqual(ids["BASELINE"]["raw_sha256"], CANON_RAW)
        self.assertEqual(ids["BASELINE"]["logical_hash"], self.reg["current_canonical_hash"])
        self.assertEqual(ids["PREFERRED_FIVE"]["raw_sha256"], CAND_RAW)
        self.assertEqual(self.c["list_hash"], ids["PREFERRED_FIVE"]["logical_hash"])

    def test_authoritative_j_checker_passes_and_binds_result(self):
        self.assertTrue(standard.validate_bundle(self.b, standard.load(standard.REGISTRY), standard.load(standard.SEALS)))
        self.assertEqual(self.b["result_hash"], self.c["list_hash"])
        self.assertEqual(self.b["baseline_hash"], self.reg["current_canonical_hash"])
        paths = {i["path"] for i in self.b["inputs"]}
        for cfg in self.pool["configurations"]:
            self.assertIn(cfg["path"], paths)
        self.assertIn(str(CERT.relative_to(ROOT)), paths)
        self.assertFalse(self.b["pass_c"]["technically_independent"])
        self.assertTrue(all(not t["supports_improvement_claim"] for t in self.b["phase_b"]["tests"]))

    def test_canonical_registry_untouched_and_no_approval(self):
        self.assertEqual(self.reg["source"]["raw_sha256"], "sha256:" + CANON_RAW)
        self.assertEqual(self.reg["source"]["recorded_sha256"], HIST)
        self.assertIs(self.reg["source"]["recorded_matches_raw"], False)
        for p in (CERT, BUNDLE, POOL, MEMO):
            t = p.read_text()
            self.assertNotIn('"APPROVED"', t)
            self.assertNotIn("CANONICAL_LOCKED", t)
        self.assertFalse(self.pool["owner_m7_approved"])

    def test_self_challenge_recorded_in_packet_and_memo(self):
        pk = json.loads(PACKET.read_text())
        chal = {x["challenger"]: x["disposition"] for x in pk["open_ended_optimization_audit"]["post_floor_challenges"]}
        self.assertEqual(chal["Wizards of Thay"], "RETAIN_ALTERNATIVE")
        self.assertEqual(chal["Mystic Sanctuary"], "REJECT")
        self.assertGreaterEqual(len(chal), 2)
        memo = MEMO.read_text()
        self.assertIn("Self-challenge", memo)
        self.assertIn("Primal Amulet", memo)


class RegistryBoundDigestDiscrepancyFailsClosed(unittest.TestCase):
    def test_exact_registry_pair_accepted(self):
        self.assertTrue(standard.registry_bound_digest_discrepancy(
            {"canonical_approved_sha256": HIST}, {"canonical_input_sha256": CANON_RAW}, D))

    def test_fabricated_or_swapped_digests_rejected(self):
        f = standard.registry_bound_digest_discrepancy
        self.assertFalse(f({"canonical_approved_sha256": "0" * 64}, {"canonical_input_sha256": CANON_RAW}, D))
        self.assertFalse(f({"canonical_approved_sha256": HIST}, {"canonical_input_sha256": "1" * 64}, D))
        self.assertFalse(f({"canonical_approved_sha256": CANON_RAW}, {"canonical_input_sha256": HIST}, D))


class PassCDisclosureWordingFailsClosed(unittest.TestCase):
    """The checker accepts Anhelo's preserved '**Technically independent:** FALSE.' wording only."""
    FINAL = "data/grixis/m6/owner_pass_c_substitute/Anhelo__the_Painter/final_disposition.md"

    def run_with_final_text(self, text):
        import tempfile
        from unittest import mock
        b = json.loads(BUNDLE.read_text())
        real = standard.safe_repo_file
        with tempfile.TemporaryDirectory() as d:
            fake = Path(d) / "final_disposition.md"
            fake.write_text(text, encoding="utf-8")
            with mock.patch.object(standard, "safe_repo_file",
                                   lambda p: fake if str(p).endswith(self.FINAL) else real(p)):
                return standard.validate_pass_c(b["pass_c"], D)

    def test_preserved_wording_accepted(self):
        self.assertTrue(self.run_with_final_text((ROOT / self.FINAL).read_text(encoding="utf-8")))

    def test_affirmative_or_missing_disclosure_rejected(self):
        t = (ROOT / self.FINAL).read_text(encoding="utf-8")
        self.assertIn("**Technically independent:** FALSE.", t)
        for bad in (t.replace("**Technically independent:** FALSE.", "**Technically independent:** TRUE."),
                    t.replace("**Technically independent:** FALSE.", "")):
            with self.assertRaises(ValueError):
                self.run_with_final_text(bad)


if __name__ == "__main__":
    unittest.main()
