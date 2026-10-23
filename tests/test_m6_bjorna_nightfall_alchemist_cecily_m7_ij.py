"""Candidate-specific M6 I / J evidence for the Cecily/Bjorna (companion Lutri) M7 candidate.

Recomputes bound byte and logical hashes (zones commander / companion / main), runs the authoritative J bundle
checker, asserts the I certificate stays tested-pool-local with no approval/lock claim, and pins the fail-closed
Pass C non-independence wording and legacy seal-alias mapping for this deck.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import grixis_authority as ga  # noqa: E402
import grixis_m6_bundle_check as standard  # noqa: E402

D = "Cecily__Bjorna__Lutri"
CERT = ROOT / "data/grixis/m6/ij/certificates/bjorna-nightfall-alchemist-cecily-m7.json"
BUNDLE = ROOT / "data/grixis/m6/ij/revision_bundles/bjorna-nightfall-alchemist-cecily-m7.json"
POOL = ROOT / "data/grixis/m6/ij/tested_pools/Cecily__Bjorna__Lutri_M7_tested_configurations_20261023.json"
SNAP = ROOT / "data/grixis/m6/oracle_snapshots/Cecily__Bjorna__Lutri_M7_Scryfall_20261023.json"
MEMO = ROOT / "data/grixis/m6/certification_preflight/Cecily__Bjorna__Lutri_M6_I_local_best_20261023.md"
PACKET = ROOT / "data/grixis/m7/decision_reviews/Cecily__Bjorna__Lutri.json"
CANON_RAW = "553838da88fe00974e74664633be5051c4f1a0879baa71de81ca9f880e5a6d28"
CAND_RAW = "2cc7227f954e728e0b37949b74f9575128b2c82250f53e211289aa60e4fa1717"
FINAL = "data/grixis/m6/owner_pass_c_substitute/Cecily__Bjorna__Lutri/final_disposition.md"
SEAL = "data/grixis/m6/owner_pass_c_substitute/Cecily__Bjorna__Lutri/seal.json"
PRESERVED = "Technical independent model FALSE"
LUTRI = "Lutri, the Spellchaser"
ADDS = ["Strionic Resonator", "Echo, Perceptive Prodigy", "Twenty-Toed Toad",
        "Sea Gate Restoration // Sea Gate, Reborn", "Deflecting Swat", "Mana Drain"]
CUTS = ["Emry, Lurker of the Loch", "Goblin Engineer", "Sai, Master Thopterist", "Dark Deal", "Mana Geyser", "Seething Song"]
EXPECTED_DELTAS = {
    "BASELINE": ([], []),
    "CANONICAL_WITH_COMPANION": ([], []),
    "PREFERRED_SIX": (ADDS, CUTS),
    "FIVE_FLOOR_WITHOUT_MANA_DRAIN": (ADDS[:5], CUTS[:5]),
    "SIX_PASS_C_RESONATOR_OVER_WAKE": (ADDS, ["In Garruk's Wake"] + CUTS[1:]),
    "SEVEN_ENTER_THE_INFINITE": (ADDS + ["Enter the Infinite"], CUTS + ["Wheel of Misfortune"]),
    "SEVEN_PETER_PARKERS_CAMERA": (ADDS + ["Peter Parker's Camera"], CUTS + ["Lightning Greaves"]),
}


def sha(p):
    return hashlib.sha256((ROOT / p).read_bytes()).hexdigest()


def rows(path):
    out = []
    for line in (ROOT / path).read_text(encoding="utf-8").splitlines():
        if line.strip():
            q, raw = line.split(" ", 1)
            z = "commander" if raw.endswith(" [Commander]") else "companion" if raw.endswith(" [Companion]") else "main"
            out.append((z, raw.removesuffix(" [Commander]").removesuffix(" [Companion]"), int(q.rstrip("x"))))
    return out


class CecilyBjornaLutriM7IJ(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.c = json.loads(CERT.read_text())
        cls.b = json.loads(BUNDLE.read_text())
        cls.pool = json.loads(POOL.read_text())
        cls.o = {x["name"].split(" // ")[0]: x for x in json.loads(SNAP.read_text())["cards"]}
        cls.reg = json.loads((ROOT / "data/grixis/registry.json").read_text())["decks"][D]

    def lh(self, path):
        return ga.logical_hash([(z, self.o[n.split(" // ")[0]]["oracle_id"], q) for z, n, q in rows(path)])

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

    def test_pool_every_configuration_raw_logical_hash_and_exact_delta(self):
        self.assertEqual("sha256:" + sha(self.c["candidate_pool"]["source_ref"]), self.c["candidate_pool"]["source_sha256"])
        self.assertEqual(self.c["candidate_pool"]["tested_pool_size"], len(self.pool["configurations"]))
        base = Counter({n: q for z, n, q in rows(self.pool["configurations"][0]["path"]) if z != "companion"})
        for cfg in self.pool["configurations"]:
            self.assertEqual(sha(cfg["path"]), cfg["raw_sha256"], cfg["id"])
            self.assertEqual(self.lh(cfg["path"]), cfg["logical_hash"], cfg["id"])
            self.assertEqual(cfg["physical_cards"], 100, cfg["id"])
            r = rows(cfg["path"])
            self.assertEqual(sum(q for z, _, q in r if z != "companion"), 100, cfg["id"])
            comp = [n for z, n, _ in r if z == "companion"]
            self.assertEqual(comp, [LUTRI] if cfg["companion_outside_100"] else [], cfg["id"])
            main = Counter({n: q for z, n, q in r if z != "companion"})
            adds, cuts = EXPECTED_DELTAS[cfg["id"]]
            self.assertEqual(sorted((main - base).elements()), sorted(adds), cfg["id"])
            self.assertEqual(sorted((base - main).elements()), sorted(cuts), cfg["id"])
        ids = {x["id"]: x for x in self.pool["configurations"]}
        self.assertEqual(set(ids), set(EXPECTED_DELTAS))
        self.assertEqual(ids["BASELINE"]["raw_sha256"], CANON_RAW)
        self.assertEqual("sha256:" + ids["BASELINE"]["raw_sha256"], self.reg["source"]["raw_sha256"])
        self.assertEqual(ids["BASELINE"]["logical_hash"], self.reg["baseline_hash"])
        self.assertEqual(ids["CANONICAL_WITH_COMPANION"]["logical_hash"], self.reg["current_canonical_hash"])
        self.assertEqual(ids["CANONICAL_WITH_COMPANION"]["path"], self.reg["canonical_project_list"]["export"])
        self.assertEqual(ids["PREFERRED_SIX"]["raw_sha256"], CAND_RAW)
        self.assertEqual(self.c["list_hash"], ids["PREFERRED_SIX"]["logical_hash"])
        self.assertFalse(self.pool["owner_m7_approved"])

    def test_authoritative_j_checker_passes_and_binds_result(self):
        self.assertTrue(standard.validate_bundle(self.b, standard.load(standard.REGISTRY), standard.load(standard.SEALS)))
        self.assertEqual(self.b["result_hash"], self.c["list_hash"])
        self.assertEqual(self.b["baseline_hash"], self.reg["current_canonical_hash"])
        paths = {i["path"]: i["sha256"] for i in self.b["inputs"]}
        for cfg in self.pool["configurations"]:
            self.assertIn(cfg["path"], paths)
        self.assertIn(str(CERT.relative_to(ROOT)), paths)
        self.assertEqual(paths["scripts/grixis_m6_bundle_check.py"], "sha256:" + sha("scripts/grixis_m6_bundle_check.py"))
        self.assertEqual(sha("scripts/grixis_m6_bundle_check.py"),
                         "2962a64053b6ea302924fd74dcc646c5fc6eb318016c0aa57026012ba9b3bf3b")
        self.assertFalse(self.b["pass_c"]["technically_independent"])
        self.assertEqual(self.b["pass_c"]["review_class"], "FORMAL_PASS_C_OWNER_EQUIVALENT")
        self.assertTrue(all(not t["supports_improvement_claim"] for t in self.b["phase_b"]["tests"]))

    def test_canonical_registry_untouched_no_provenance_exception_and_no_approval(self):
        self.assertIs(self.reg["source"]["recorded_matches_raw"], True)
        self.assertEqual("sha256:" + self.reg["source"]["recorded_sha256"], self.reg["source"]["raw_sha256"])
        self.assertEqual(sorted(self.reg["official_commander_compliance"]["cards"]),
                         [LUTRI, "Trade Secrets", "Yawgmoth's Bargain"])
        for p in (CERT, BUNDLE, POOL, MEMO):
            t = p.read_text()
            self.assertNotIn('"APPROVED"', t)
            self.assertNotIn("CANONICAL_LOCKED", t)
            self.assertNotIn("officially legal", t.replace("never officially legal", "").replace("not officially legal", ""))
        self.assertNotIn("baseline_provenance_exception", json.loads(PACKET.read_text()))

    def test_self_challenge_recorded_in_packet_and_memo(self):
        pk = json.loads(PACKET.read_text())
        pf = pk["open_ended_optimization_audit"]["post_floor_challenges"]
        chal = {x["challenger"]: x["disposition"] for x in pf}
        self.assertGreaterEqual(len({x["incumbent"] for x in pf}), 2)
        self.assertEqual(chal["Enter the Infinite"], "RETAIN_ALTERNATIVE")
        self.assertEqual(chal["Peter Parker's Camera"], "RETAIN_ALTERNATIVE")
        memo = MEMO.read_text()
        self.assertIn("Self-challenge", memo)
        self.assertIn("In Garruk's Wake", memo)
        self.assertIn("Seething Song kept", memo)


class CecilyPassCFailsClosed(unittest.TestCase):
    """The preserved FALSE wording is accepted only for this deck and only without any TRUE/YES claim."""

    def run_with_final_text(self, text):
        b = json.loads(BUNDLE.read_text())
        real_safe, real_bind = standard.safe_repo_file, standard.bind
        with tempfile.TemporaryDirectory() as d:
            fake = Path(d) / "final_disposition.md"
            fake.write_text(text, encoding="utf-8")
            with mock.patch.object(standard, "safe_repo_file",
                                   lambda p: fake if str(p).endswith(FINAL) else real_safe(p)), \
                 mock.patch.object(standard, "bind",
                                   lambda n, h: None if str(n).endswith(FINAL) else real_bind(n, h)):
                return standard.validate_pass_c(dict(b["pass_c"]), D)

    def preserved(self):
        t = (ROOT / FINAL).read_text(encoding="utf-8")
        self.assertEqual(t.count(PRESERVED), 1)
        self.assertTrue(standard.pass_c_preserved_nonindependence(t, D))
        self.assertFalse(standard.pass_c_preserved_nonindependence(t, "Be_lakor__the_Dark_Master"))
        return t

    def test_preserved_wording_accepted(self):
        self.assertTrue(self.run_with_final_text(self.preserved()))

    def test_true_missing_or_contradictory_rejected(self):
        t = self.preserved()
        bad = [
            t.replace(PRESERVED, "Technical independent model TRUE"),
            t.replace(PRESERVED, "Technical independent model YES"),
            t.replace(PRESERVED, ""),
            t + "\nCorrection: technical independence TRUE.\n",
            t + "\nCorrection: technically independent: yes\n",
        ]
        for text in bad:
            with self.assertRaises(ValueError):
                self.run_with_final_text(text)

    def test_legacy_seal_aliases_map_without_rewriting(self):
        seal = json.loads((ROOT / SEAL).read_text())
        n = standard.normalize_stage_a_seal_aliases(seal, D)
        self.assertEqual(n["canonical_input_sha256"], CANON_RAW)
        self.assertIs(n["technically_independent"], False)
        self.assertEqual(n["review_class_after_final"], "FORMAL_PASS_C_OWNER_EQUIVALENT")
        self.assertEqual(seal, json.loads((ROOT / SEAL).read_text()))
        for bad in (dict(seal, technical_independence=True), dict(seal, technically_independent=True),
                    {k: v for k, v in seal.items() if k != "technical_independence"},
                    dict(seal, formal_class="INDEPENDENT")):
            with self.assertRaises(ValueError):
                b = json.loads(BUNDLE.read_text())
                real_safe, real_bind = standard.safe_repo_file, standard.bind
                with tempfile.TemporaryDirectory() as d:
                    fake = Path(d) / "seal.json"
                    fake.write_text(json.dumps(bad), encoding="utf-8")
                    with mock.patch.object(standard, "safe_repo_file",
                                           lambda p: fake if str(p).endswith(SEAL) else real_safe(p)), \
                         mock.patch.object(standard, "bind",
                                           lambda n, h: None if str(n).endswith(SEAL) else real_bind(n, h)):
                        standard.validate_pass_c(b["pass_c"], D)


if __name__ == "__main__":
    unittest.main()
