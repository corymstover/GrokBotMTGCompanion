"""Candidate-specific M6 I / J evidence for the Admiral Brass, Unsinkable M7 candidate.

Recomputes every bound byte hash and logical hash, runs the authoritative J
bundle checker, and asserts the I certificate stays tested-pool-local with no
approval, lock, CI or global-optimality claim. Canonical decklist untouched.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import grixis_authority as ga  # noqa: E402
import grixis_m6_bundle_check as standard  # noqa: E402

CERT = ROOT / "data/grixis/m6/ij/certificates/admiral-brass-unsinkable-m7.json"
BUNDLE = ROOT / "data/grixis/m6/ij/revision_bundles/admiral-brass-unsinkable-m7.json"
POOL = ROOT / "data/grixis/m6/ij/tested_pools/Admiral_Brass__Unsinkable_M7_five_configurations_20261023.json"
SNAP = ROOT / "data/grixis/m6/oracle_snapshots/Admiral_Brass__Unsinkable_M7_109_Scryfall_20261023.json"
MEMO = ROOT / "data/grixis/m6/certification_preflight/Admiral_Brass__Unsinkable_M6_I_local_best_20261023.md"
PACKET = ROOT / "data/grixis/m7/decision_reviews/Admiral_Brass__Unsinkable.json"
CANON_RAW = "056f0369bc4b11967365eef65d15a806b2d0f673ecf8097b028ffcdfd472f5cc"
CAND_RAW = "953a1f8c147239f450ec78704537a2f45c6dde3891d38e7c5f48d178780d2475"


def sha(p):
    return hashlib.sha256((ROOT / p).read_bytes()).hexdigest()


class AdmiralBrassUnsinkableM7IJ(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.c = json.loads(CERT.read_text())
        cls.b = json.loads(BUNDLE.read_text())
        cls.pool = json.loads(POOL.read_text())
        s = json.loads(SNAP.read_text())
        cls.o = {x["name"]: x for x in s["cards"]}
        cls.o.update({n.split(" // ")[0]: x for n, x in list(cls.o.items()) if " // " in n})
        cls.reg = json.loads((ROOT / "data/grixis/registry.json").read_text())["decks"]["Admiral_Brass__Unsinkable"]

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
        self.assertFalse(any("actions/runs" in r for r in self.c["receipt_refs"]))  # no CI claimed
        for t in self.c["phase_b"]["test_refs"]:
            self.assertTrue((ROOT / t).is_file(), t)

    def test_pool_every_configuration_raw_and_logical_hash(self):
        self.assertEqual("sha256:" + sha(self.c["candidate_pool"]["source_ref"]), self.c["candidate_pool"]["source_sha256"])
        self.assertEqual(self.c["candidate_pool"]["tested_pool_size"], 5)
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
        self.assertIs(self.reg["source"]["recorded_matches_raw"], False)
        for p in (CERT, BUNDLE, POOL, MEMO):
            t = p.read_text()
            self.assertNotIn('"APPROVED"', t)
            self.assertNotIn("CANONICAL_LOCKED", t)
        self.assertFalse(self.pool["owner_m7_approved"])

    def test_self_challenge_recorded_in_packet_and_memo(self):
        pk = json.loads(PACKET.read_text())
        stop = pk["open_ended_optimization_audit"]["quality_based_stop_reason"]
        self.assertIn("self-challenge", stop)
        for n in ("Nesting Grounds", "Ashnod's Altar"):
            self.assertIn(n, stop)
        self.assertIn("Self-challenge", MEMO.read_text())
        chal = {x["challenger"]: x["disposition"] for x in pk["open_ended_optimization_audit"]["post_floor_challenges"]}
        self.assertEqual(chal["Nesting Grounds"], "RETAIN_ALTERNATIVE")
        self.assertEqual(chal["Ashnod's Altar"], "REJECT")


class RegistryBoundDigestDiscrepancyFailsClosed(unittest.TestCase):
    """Adversarial checks for the narrow Pass C ledger-vs-seal reconciliation."""
    HIST = "e66e3a59719401f41830e9938997a87a45a1b0dcaa0663b0ec7b44e10077dd39"
    D = "Admiral_Brass__Unsinkable"

    def test_exact_registry_pair_accepted(self):
        self.assertTrue(standard.registry_bound_digest_discrepancy(
            {"canonical_approved_sha256": self.HIST}, {"canonical_input_sha256": CANON_RAW}, self.D))

    def test_fabricated_or_swapped_digests_rejected(self):
        f = standard.registry_bound_digest_discrepancy
        self.assertFalse(f({"canonical_approved_sha256": "0" * 64}, {"canonical_input_sha256": CANON_RAW}, self.D))
        self.assertFalse(f({"canonical_approved_sha256": self.HIST}, {"canonical_input_sha256": "1" * 64}, self.D))
        self.assertFalse(f({"canonical_approved_sha256": CANON_RAW}, {"canonical_input_sha256": self.HIST}, self.D))

    def test_other_deck_without_registry_discrepancy_rejected(self):
        self.assertFalse(standard.registry_bound_digest_discrepancy(
            {"canonical_approved_sha256": self.HIST}, {"canonical_input_sha256": CANON_RAW}, "Admiral_Beckett_Brass"))


if __name__ == "__main__":
    unittest.main()
