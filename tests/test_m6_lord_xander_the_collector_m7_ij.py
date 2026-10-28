"""Candidate-specific M6 I / J evidence for the Lord_Xander__the_Collector (Lord Xander, the Collector) M7 research candidate.

Recomputes bound byte and logical hashes (zones commander / main) for all 11 tested configurations, asserts that the I
certificate is BLOCKED (not pass) and stays tested-pool-local with no approval/lock claim, and asserts that the UNCHANGED
authoritative J bundle checker REJECTS this deck's bundle on the existing Pass C Stage A seal mismatch: the committed
seal.json (commit bca97b98) records stage_a.md SHA-256 89a78d80... while the committed stage_a.md hashes to 826f0770....
A mock that substitutes only the sealed value for that one hash makes validate_bundle pass, showing the seal is the
only failure. Neither the sealed evidence nor the checker is edited. Nothing here is owner approval.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path
import sys
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import grixis_authority as ga  # noqa: E402
import grixis_m6_bundle_check as standard  # noqa: E402

D = "Lord_Xander__the_Collector"
S = "lord-xander-the-collector"
CERT = ROOT / f"data/grixis/m6/ij/certificates/{S}-m7.json"
BUNDLE = ROOT / f"data/grixis/m6/ij/revision_bundles/{S}-m7.json"
POOL = ROOT / f"data/grixis/m6/ij/tested_pools/{D}_M7_tested_configurations_20261023.json"
SNAP = ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json"
MEMO = ROOT / f"data/grixis/m6/certification_preflight/{D}_M6_I_local_best_20261023.md"
PACKET = ROOT / f"data/grixis/m7/decision_reviews/{D}.json"
PC = f"data/grixis/m6/owner_pass_c_substitute/{D}"
FINAL, SEAL, STAGE_MD, STAGE_JSON = (f"{PC}/final_disposition.md", f"{PC}/seal.json", f"{PC}/stage_a.md",
                                     f"{PC}/stage_a.json")
CANON_RAW = "92cdc2f9c1a3583ccf6a311679db66bef825dac2902761859e929f268b6b4787"
CAND_RAW = "8dc209682c00608e1d903b41988ac7bcec540005624ef7938593ee520f1a28c8"
SEALED_MD = "89a78d803b5cb5ea886b2402828aaff00b78497db0b3c0fe569c6c0ee5a879d1"
ACTUAL_MD = "826f07707a6fdd1583b815ba6b80ad99bd8a71d57d03ac05766ed2a0a4cd0322"
SEALED_JSON = "aff5f64c0a59ede5b77eb3a58d39fc5cf04bc8eebdc791c238a94898a25181ca"
DIVERGED = "Stage A source diverged from separately sealed byte commitment"
PRESERVED = "`technically_independent=false`"
COMMANDERS = ["Lord Xander, the Collector"]
NEC, BOOTS, MAL = "Necromancy", "Swiftfoot Boots", "Malakir Rebirth // Malakir Mire"
PER, GRE, BOG = "Persist", "Lightning Greaves", "Bojuka Bog"
KAR, OFFER = "Karlach, Fury of Avernus", "An Offer You Can't Refuse"
A3, C3 = [NEC, BOOTS, MAL], [PER, GRE, BOG]
EXPECTED_DELTAS = {
    "BASELINE": ([], []),
    "CANONICAL_EXPORT": ([], []),
    "RESEARCH_THREE_SWAP": (A3, C3),
    "ALT_A_OWNER_KEEPS_NECROMANCY_OVER_KARLACH": (A3, [KAR, GRE, BOG]),
    "ALT_B_OWNER_KEEPS_NECROMANCY_OVER_AN_OFFER": (A3, [OFFER, GRE, BOG]),
    "PASS_C_GORYOS_VENGEANCE_OVER_PERSIST": (["Goryo's Vengeance", BOOTS, MAL], C3),
    "PASS_C_SEIZE_THE_DAY_OVER_KARLACH": (A3 + ["Seize the Day"], C3 + [KAR]),
    "STAGED_KIKI_JIKI_OVER_KARLACH": (A3 + ["Kiki-Jiki, Mirror Breaker"], C3 + [KAR]),
    "REJECT_GLASSPOOL_MIMIC_OVER_TRAINING_CENTER": (A3 + ["Glasspool Mimic // Glasspool Shore"], C3 + ["Training Center"]),
    "REJECT_CHROME_MOX_OVER_TALISMAN": (A3 + ["Chrome Mox"], C3 + ["Talisman of Creativity"]),
    "REJECT_COMMAND_BEACON_OVER_XANDERS_LOUNGE": (A3 + ["Command Beacon"], C3 + ["Xander's Lounge"]),
}


def sha(p):
    return hashlib.sha256((ROOT / p).read_bytes()).hexdigest()


def rows(path):
    out = []
    for line in (ROOT / path).read_text(encoding="utf-8").splitlines():
        if line.strip():
            q, raw = line.split(" ", 1)
            z = "commander" if raw.endswith(" [Commander]") else "main"
            out.append((z, raw.removesuffix(" [Commander]"), int(q.rstrip("x"))))
    return out


def validate(b):
    return standard.validate_bundle(b, standard.load(standard.REGISTRY), standard.load(standard.SEALS))


class LordXanderM7IJ(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.c = json.loads(CERT.read_text())
        cls.b = json.loads(BUNDLE.read_text())
        cls.pool = json.loads(POOL.read_text())
        cls.o = {x["name"].split(" // ")[0]: x for x in json.loads(SNAP.read_text())["cards"]}
        cls.reg = json.loads((ROOT / "data/grixis/registry.json").read_text())["decks"][D]

    def lh(self, path):
        return ga.logical_hash([(z, self.o[n.split(" // ")[0]]["oracle_id"], q) for z, n, q in rows(path)])

    def test_certificate_schema_blocked_and_local_only_scope(self):
        self.assertEqual(ga.validate_file(self.c, "zero_improvement_certificate.schema.json"), [])
        self.assertEqual(self.c["certificate_status"], "blocked")
        self.assertFalse(self.c["improving_substitution_found"])
        self.assertFalse(self.c["local_optimum_for_tested_pool"])
        self.assertEqual(len(self.c["blockers"]), 2)
        self.assertIn(SEALED_MD, self.c["blockers"][0])
        self.assertIn(ACTUAL_MD, self.c["blockers"][0])
        self.assertIn("bca97b98980869974388134e0b133d75e5782a55", self.c["blockers"][0])
        self.assertIn("Only three genuine swaps", self.c["blockers"][1])
        self.assertEqual(len(self.c["unresolved_requires_human_judgment"]), 2)
        self.assertIs(self.c["authority"]["can_decide"], False)
        self.assertIs(self.c["authority"]["can_approve_or_lock"], False)
        self.assertIn("not a mathematical or global proof", self.c["scope_caveat"])
        self.assertIn("11 complete configurations", self.c["authority"]["note"])
        self.assertIn("BLOCKED, not PASS", self.c["authority"]["note"])
        self.assertIn(SEAL, self.c["receipt_refs"])
        self.assertFalse(any("actions/runs" in r for r in self.c["receipt_refs"]))
        for t in self.c["phase_b"]["test_refs"]:
            self.assertTrue((ROOT / t).is_file(), t)

    def test_pool_every_configuration_raw_logical_hash_and_exact_delta(self):
        self.assertEqual("sha256:" + sha(self.c["candidate_pool"]["source_ref"]), self.c["candidate_pool"]["source_sha256"])
        self.assertEqual(self.c["candidate_pool"]["tested_pool_size"], len(self.pool["configurations"]))
        self.assertEqual(len(self.pool["configurations"]), 11)
        base = Counter({n: q for z, n, q in rows(self.pool["configurations"][0]["path"])})
        for cfg in self.pool["configurations"]:
            self.assertEqual(sha(cfg["path"]), cfg["raw_sha256"], cfg["id"])
            self.assertEqual(self.lh(cfg["path"]), cfg["logical_hash"], cfg["id"])
            self.assertEqual(cfg["physical_cards"], 100, cfg["id"])
            r = rows(cfg["path"])
            self.assertEqual(sum(q for _, _, q in r), 100, cfg["id"])
            self.assertEqual([n for z, n, _ in r if z == "commander"], COMMANDERS, cfg["id"])
            self.assertIsNone(cfg["companion_outside_100"], cfg["id"])
            main = Counter({n: q for z, n, q in r})
            adds, cuts = EXPECTED_DELTAS[cfg["id"]]
            self.assertEqual(sorted((main - base).elements()), sorted(adds), cfg["id"])
            self.assertEqual(sorted((base - main).elements()), sorted(cuts), cfg["id"])
        ids = {x["id"]: x for x in self.pool["configurations"]}
        self.assertEqual(set(ids), set(EXPECTED_DELTAS))
        self.assertEqual(ids["BASELINE"]["raw_sha256"], CANON_RAW)
        self.assertEqual("sha256:" + ids["BASELINE"]["raw_sha256"], self.reg["source"]["raw_sha256"])
        self.assertEqual(ids["BASELINE"]["logical_hash"], self.reg["baseline_hash"])
        self.assertEqual(ids["CANONICAL_EXPORT"]["logical_hash"], self.reg["current_canonical_hash"])
        self.assertEqual(ids["CANONICAL_EXPORT"]["path"], self.reg["canonical_project_list"]["export"])
        self.assertEqual(ids["RESEARCH_THREE_SWAP"]["raw_sha256"], CAND_RAW)
        self.assertEqual(self.c["list_hash"], ids["RESEARCH_THREE_SWAP"]["logical_hash"])
        self.assertNotEqual(ids["RESEARCH_THREE_SWAP"]["logical_hash"], self.reg["current_canonical_hash"])
        self.assertEqual(len({x["logical_hash"] for x in self.pool["configurations"]}), 10)  # baseline == export
        self.assertFalse(self.pool["owner_m7_approved"])

    def test_bundle_bindings_schema_and_checker_pin(self):
        self.assertEqual(ga.validate_file(self.b, "m6_reproducibility_bundle.schema.json"), [])
        self.assertEqual(self.b["result_hash"], self.c["list_hash"])
        self.assertEqual(self.b["baseline_hash"], self.reg["current_canonical_hash"])
        paths = {i["path"]: i["sha256"] for i in self.b["inputs"]}
        for cfg in self.pool["configurations"]:
            self.assertIn(cfg["path"], paths)
        self.assertIn(str(CERT.relative_to(ROOT)), paths)
        self.assertIn(".github/workflows/m7-lord-xander-the-collector.yml", paths)
        # The old research J bundle deliberately pins the ORIGINAL checker. Its receipt is
        # preserved while the authorized source-only v2 correction updates the live checker.
        self.assertNotEqual(sha("scripts/grixis_m6_bundle_check.py"),
                            "2962a64053b6ea302924fd74dcc646c5fc6eb318016c0aa57026012ba9b3bf3b")
        for p, h in paths.items():
            if p == "scripts/grixis_m6_bundle_check.py":
                self.assertEqual(h, "sha256:2962a64053b6ea302924fd74dcc646c5fc6eb318016c0aa57026012ba9b3bf3b")
            elif p == "data/grixis/schemas/m7_decisive_optimization.schema.json":
                # The frozen research J bundle pins its original schema bytes.
                # The later live schema revision is independently SHA-bound;
                # never rewrite the historical bundle or claim it passes now.
                self.assertEqual(h, "sha256:9ae2161f427051ec78d38198968ff7ff0880a4e6a91986356b86fee076ad9376")
                self.assertEqual(sha(p), "babc54a313fc54ec41f8b6b21ad303f1dc2c6706d225216bbe0ae577c07cc7b1")
            else:
                self.assertEqual(h, "sha256:" + sha(p), p)
        self.assertEqual(self.b["pass_c"]["stage_a_seal_sha256"], "sha256:" + sha(SEAL))
        self.assertFalse(self.b["pass_c"]["technically_independent"])
        self.assertEqual(self.b["pass_c"]["review_class"], "FORMAL_PASS_C_OWNER_EQUIVALENT")
        self.assertTrue(all(not t["supports_improvement_claim"] for t in self.b["phase_b"]["tests"]))
        for t in self.b["phase_b"]["tests"]:
            if t["test_ref"] == "tests/test_m6_lord_xander_the_collector_m7_ij.py":
                # Historic receipt still names the pre-correction regression test.
                self.assertNotEqual(t["source_sha256"], "sha256:" + sha(t["test_ref"]))
            else:
                self.assertEqual(t["source_sha256"], "sha256:" + sha(t["test_ref"]), t["test_ref"])
        self.assertFalse((ROOT / f"data/grixis/m6/bundles/{S}.json").exists())  # never placed where --check scans

    def test_old_j_bundle_remains_historic_and_v2_source_correction_is_scoped(self):
        with self.assertRaisesRegex(ValueError, "SHA-256 drift"):
            validate(self.b)
        self.assertTrue(standard.validate_pass_c(dict(self.b["pass_c"]), D))
        seal = json.loads((ROOT / SEAL).read_text())
        self.assertEqual(seal["stage_a_files"]["stage_a.md"]["sha256"], SEALED_MD)
        self.assertEqual(sha(STAGE_MD), ACTUAL_MD)
        self.assertNotEqual(SEALED_MD, ACTUAL_MD)
        self.assertEqual(seal["stage_a_files"]["stage_a.json"]["sha256"], SEALED_JSON)
        self.assertEqual(sha(STAGE_JSON), SEALED_JSON)  # the JSON half of the seal does match

    def test_authorized_v2_correction_does_not_rewrite_original_seal(self):
        self.assertTrue(standard.validate_pass_c(dict(self.b["pass_c"]), D))
        self.assertTrue(standard.verify_xander_versioned_stage_a_correction(D,
                        standard.normalize_stage_a_seal_aliases(json.loads((ROOT / SEAL).read_text()), D), "md"))
        with mock.patch.object(standard, "verify_xander_versioned_stage_a_correction", return_value=False):
            with self.assertRaisesRegex(ValueError, DIVERGED):
                standard.validate_pass_c(dict(self.b["pass_c"]), D)

    def test_jlk_neutral_seal_maps_and_bytes_unchanged(self):
        raw = (ROOT / SEAL).read_bytes()
        seal = json.loads(raw)
        self.assertEqual(seal["schema_version"], "jlk-neutral-seal-1")
        self.assertEqual((seal["deck_index"], seal["tracker_index"], seal["reviewer_alias"]), (30, 29, "Josh-Lee-Kwai"))
        self.assertEqual(seal["independence_requirement"], "OWNER_WAIVED_FOR_FORMAL_PASS_C")
        self.assertEqual(seal["stage_a_commit_sha"], "6ebb511e4b1bc4d6d0b9f0103cf1f95519f7eaae")
        n = standard.normalize_stage_a_seal_aliases(seal, D)
        self.assertEqual(n["canonical_input_sha256"], CANON_RAW)
        self.assertIs(n["technically_independent"], False)
        self.assertEqual(n["review_class_after_final"], "FORMAL_PASS_C_OWNER_EQUIVALENT")
        self.assertEqual(n["git_first_stage_commit_sha"], "6ebb511e4b1bc4d6d0b9f0103cf1f95519f7eaae")
        self.assertEqual(n["stage_a_md_sha256"], SEALED_MD)
        self.assertEqual(n["stage_a_json_sha256"], SEALED_JSON)
        self.assertEqual((ROOT / SEAL).read_bytes(), raw)
        self.assertEqual("sha256:" + hashlib.sha256(raw).hexdigest(), self.b["pass_c"]["stage_a_seal_sha256"])

    def test_preserved_pass_c_wording_bound_to_this_deck(self):
        t = (ROOT / FINAL).read_text(encoding="utf-8")
        self.assertIn(PRESERVED, t)
        self.assertTrue(standard.pass_c_preserved_nonindependence(t, D))
        self.assertFalse(standard.pass_c_preserved_nonindependence(t, "The_Rani"))  # wording is deck-bound
        self.assertFalse(standard.pass_c_preserved_nonindependence(t, "Not_A_Deck"))
        self.assertFalse(standard.pass_c_preserved_nonindependence(t + "\ntechnically independent: yes\n", D))
        self.assertFalse(standard.pass_c_preserved_nonindependence(t.replace(PRESERVED, "`technically_independent=true`"), D))
        self.assertIn("ChatGPT GPT-6", t)
        self.assertNotIn("ChatGPT/OpenAI GPT-6", t)
        self.assertIn("NEEDS TESTING", t)
        self.assertIn(SEALED_MD[:8], (ROOT / FINAL).read_text())  # the disposition repeats the sealed (wrong) hash

    def test_canonical_registry_untouched_memo_and_no_approval(self):
        self.assertIs(self.reg["source"]["recorded_matches_raw"], True)
        self.assertEqual("sha256:" + self.reg["source"]["recorded_sha256"], self.reg["source"]["raw_sha256"])
        self.assertEqual(self.reg["commanders"], COMMANDERS)
        for p in (CERT, BUNDLE, POOL, MEMO):
            t = p.read_text()
            self.assertNotIn('"APPROVED"', t)
            self.assertNotIn("CANONICAL_LOCKED", t)
        pk = json.loads(PACKET.read_text())
        self.assertNotIn("baseline_provenance_exception", pk)
        self.assertEqual(pk["readiness"], "RESEARCH_ONLY_WITHDRAWN_NOT_OWNER_PRESENTABLE")
        memo = MEMO.read_text()
        for s in ("RESEARCH_ONLY_WITHDRAWN_NOT_OWNER_PRESENTABLE", SEALED_MD[:8], ACTUAL_MD[:8], "bca97b98",
                  "certificate in this PR is `blocked`, not `pass`", "FLAGGED"):
            self.assertIn(s, memo)


if __name__ == "__main__":
    unittest.main()
