"""Candidate-specific M6 I / J evidence for the Lynde__Cheerful_Tormentor (Lynde, Cheerful Tormentor) M7 research candidate.

Recomputes bound byte and logical hashes (zones commander / main) for all 13 tested configurations, asserts that the I
certificate is BLOCKED (not pass) and stays tested-pool-local with no approval/lock claim, and asserts that the UNCHANGED
authoritative J bundle checker REJECTS this deck's bundle on the existing Pass C Stage A seal mismatch: the committed
seal.json (commit c4c5fa5d) records stage_a.md SHA-256 59f2dc10... while the committed stage_a.md hashes to 02adfb85...
(59f2dc10... is the SHA-256 of the file without its final newline byte; the committed file ends in a blank line).
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

D = "Lynde__Cheerful_Tormentor"
S = "lynde-cheerful-tormentor"
CERT = ROOT / f"data/grixis/m6/ij/certificates/{S}-m7.json"
BUNDLE = ROOT / f"data/grixis/m6/ij/revision_bundles/{S}-m7.json"
POOL = ROOT / f"data/grixis/m6/ij/tested_pools/{D}_M7_tested_configurations_20261023.json"
SNAP = ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json"
MEMO = ROOT / f"data/grixis/m6/certification_preflight/{D}_M6_I_local_best_20261023.md"
PACKET = ROOT / f"data/grixis/m7/decision_reviews/{D}.json"
PC = f"data/grixis/m6/owner_pass_c_substitute/{D}"
FINAL, SEAL, STAGE_MD, STAGE_JSON = (f"{PC}/final_disposition.md", f"{PC}/seal.json", f"{PC}/stage_a.md",
                                     f"{PC}/stage_a.json")
CANON_RAW = "05d1c4eea023d25e4308f78b109e80b78e0a3f4d655c3df36743ba3afbf04166"
CAND_RAW = "435717e03dc60e874f638b0daf8ebc9ce2e898d00207985daebe789acf47fb77"
SEALED_MD = "59f2dc10eedec5797f3f5dcfdb0a206b380a037e9b17a29e740d6ca94829c12e"
ACTUAL_MD = "02adfb85db19aa42d5dfe36b96906874ea1abd232b6f8bfc3861c1108035b72a"
SEALED_JSON = "d2b968bb9990d57920f983e9a5a40cf3fefe849d567b925b48bfc085ee7407eb"
DIVERGED = "Stage A source diverged from separately sealed byte commitment"
PRESERVED = "`technically_independent=false`"
COMMANDERS = ["Lynde, Cheerful Tormentor"]
COURT, REPL = "Court of Vantress", "Extravagant Replication"
CRUEL, DEATH, NIGHT = "Cruel Reality", "Curse of Death's Hold", "Nightscape Familiar"
A2, C2 = [COURT, REPL], [CRUEL, DEATH]
EXPECTED_DELTAS = {
    "BASELINE": ([], []),
    "CANONICAL_EXPORT": ([], []),
    "RESEARCH_TWO_SWAP": (A2, C2),
    "ALT_A_COURT_ONLY": ([COURT], [CRUEL]),
    "ALT_B_REPLICATION_ONLY": ([REPL], [DEATH]),
    "STAGED_STAFF_OF_COMPLEATION_OVER_NIGHTSCAPE": (A2 + ["Staff of Compleation"], C2 + [NIGHT]),
    "PASS_C_CURSE_OF_CHAOS_OVER_ECHOES": (A2 + ["Curse of Chaos"], C2 + ["Curse of Echoes"]),
    "PASS_C_STRIONIC_RESONATOR_OVER_NIGHTSCAPE": (A2 + ["Strionic Resonator"], C2 + [NIGHT]),
    "PASS_C_BESEECH_THE_MIRROR_OVER_RESTLESS_DEAD": (A2 + ["Beseech the Mirror"], C2 + ["Curse of the Restless Dead"]),
    "REJECT_DISTURBING_MIRTH_OVER_TRESPASSERS": (A2 + ["Disturbing Mirth"], C2 + ["Trespasser's Curse"]),
    "REJECT_TEFERIS_AGELESS_INSIGHT_OVER_UNBINDING": (A2 + ["Teferi's Ageless Insight"], C2 + ["Curse of Unbinding"]),
    "REJECT_THOUGHTRENDER_LAMIA_OVER_BITTERHEART": (A2 + ["Thoughtrender Lamia"], C2 + ["Bitterheart Witch"]),
    "REJECT_CURSE_OF_THE_BLOODY_TOME_OVER_MADDENING_HEX": (A2 + ["Curse of the Bloody Tome"], C2 + ["Maddening Hex"]),
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


class LyndeCheerfulTormentorM7IJ(unittest.TestCase):
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
        self.assertIn("c4c5fa5df5d55114c5f7e773d103d8490e60b67b", self.c["blockers"][0])
        self.assertIn("Only two genuine swaps", self.c["blockers"][1])
        self.assertEqual(len(self.c["unresolved_requires_human_judgment"]), 2)
        self.assertIs(self.c["authority"]["can_decide"], False)
        self.assertIs(self.c["authority"]["can_approve_or_lock"], False)
        self.assertIn("not a mathematical or global proof", self.c["scope_caveat"])
        self.assertIn("13 complete configurations", self.c["authority"]["note"])
        self.assertIn("BLOCKED, not PASS", self.c["authority"]["note"])
        self.assertIn(SEAL, self.c["receipt_refs"])
        self.assertFalse(any("actions/runs" in r for r in self.c["receipt_refs"]))
        for t in self.c["phase_b"]["test_refs"]:
            self.assertTrue((ROOT / t).is_file(), t)

    def test_pool_every_configuration_raw_logical_hash_and_exact_delta(self):
        self.assertEqual("sha256:" + sha(self.c["candidate_pool"]["source_ref"]), self.c["candidate_pool"]["source_sha256"])
        self.assertEqual(self.c["candidate_pool"]["tested_pool_size"], len(self.pool["configurations"]))
        self.assertEqual(len(self.pool["configurations"]), 13)
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
        self.assertEqual(ids["RESEARCH_TWO_SWAP"]["raw_sha256"], CAND_RAW)
        self.assertEqual(self.c["list_hash"], ids["RESEARCH_TWO_SWAP"]["logical_hash"])
        self.assertNotEqual(ids["RESEARCH_TWO_SWAP"]["logical_hash"], self.reg["current_canonical_hash"])
        self.assertEqual(len({x["logical_hash"] for x in self.pool["configurations"]}), 12)  # baseline == export
        self.assertFalse(self.pool["owner_m7_approved"])

    def test_bundle_bindings_schema_and_checker_pin(self):
        self.assertEqual(ga.validate_file(self.b, "m6_reproducibility_bundle.schema.json"), [])
        self.assertEqual(self.b["result_hash"], self.c["list_hash"])
        self.assertEqual(self.b["baseline_hash"], self.reg["current_canonical_hash"])
        paths = {i["path"]: i["sha256"] for i in self.b["inputs"]}
        for cfg in self.pool["configurations"]:
            self.assertIn(cfg["path"], paths)
        self.assertIn(str(CERT.relative_to(ROOT)), paths)
        self.assertIn(".github/workflows/m7-lynde-cheerful-tormentor.yml", paths)
        self.assertEqual(sha("scripts/grixis_m6_bundle_check.py"),
                         "2962a64053b6ea302924fd74dcc646c5fc6eb318016c0aa57026012ba9b3bf3b")
        for p, h in paths.items():
            self.assertEqual(h, "sha256:" + sha(p), p)
        self.assertEqual(self.b["pass_c"]["stage_a_seal_sha256"], "sha256:" + sha(SEAL))
        self.assertFalse(self.b["pass_c"]["technically_independent"])
        self.assertEqual(self.b["pass_c"]["review_class"], "FORMAL_PASS_C_OWNER_EQUIVALENT")
        self.assertTrue(all(not t["supports_improvement_claim"] for t in self.b["phase_b"]["tests"]))
        for t in self.b["phase_b"]["tests"]:
            self.assertEqual(t["source_sha256"], "sha256:" + sha(t["test_ref"]), t["test_ref"])
        self.assertFalse((ROOT / f"data/grixis/m6/bundles/{S}.json").exists())  # never placed where --check scans

    def test_unchanged_j_checker_rejects_on_stage_a_seal_mismatch(self):
        with self.assertRaisesRegex(ValueError, DIVERGED):
            validate(self.b)
        with self.assertRaisesRegex(ValueError, DIVERGED):
            standard.validate_pass_c(dict(self.b["pass_c"]), D)
        seal = json.loads((ROOT / SEAL).read_text())
        self.assertEqual(seal["stage_a_files"]["stage_a.md"]["sha256"], SEALED_MD)
        self.assertEqual(sha(STAGE_MD), ACTUAL_MD)
        self.assertNotEqual(SEALED_MD, ACTUAL_MD)
        self.assertEqual(seal["stage_a_files"]["stage_a.json"]["sha256"], SEALED_JSON)
        self.assertEqual(sha(STAGE_JSON), SEALED_JSON)  # the JSON half of the seal does match

    def test_exact_cause_sealed_hash_is_file_without_final_newline(self):
        raw = (ROOT / STAGE_MD).read_bytes()
        self.assertEqual(len(raw), 13276)
        self.assertTrue(raw.endswith(b".\n\n"))
        self.assertEqual(hashlib.sha256(raw[:-1]).hexdigest(), SEALED_MD)
        blob = hashlib.sha1(b"blob %d\0" % len(raw) + raw).hexdigest()
        seal = json.loads((ROOT / SEAL).read_text())
        self.assertEqual(seal["stage_a_files"]["stage_a.md"]["git_blob_sha"], blob)  # the recorded blob is the committed file

    def test_seal_is_the_only_failure(self):
        real = standard.content_hash

        def sealed_md(name):
            return "sha256:" + SEALED_MD if str(name) == STAGE_MD else real(name)
        with mock.patch.object(standard, "content_hash", sealed_md):
            self.assertTrue(validate(self.b))
            self.assertTrue(standard.validate_pass_c(dict(self.b["pass_c"]), D))
        with self.assertRaisesRegex(ValueError, DIVERGED):  # and the real hash still fails afterwards
            validate(self.b)

    def test_jlk_neutral_seal_maps_and_bytes_unchanged(self):
        raw = (ROOT / SEAL).read_bytes()
        seal = json.loads(raw)
        self.assertEqual(seal["schema_version"], "jlk-neutral-seal-1")
        self.assertEqual((seal["deck_index"], seal["tracker_index"], seal["reviewer_alias"]), (31, 30, "Josh-Lee-Kwai"))
        self.assertEqual(seal["independence_requirement"], "OWNER_WAIVED_FOR_FORMAL_PASS_C")
        self.assertEqual(seal["stage_a_commit_sha"], "b4c985688c4bee3db76d18bb0c3ada940ec79c98")
        n = standard.normalize_stage_a_seal_aliases(seal, D)
        self.assertEqual(n["canonical_input_sha256"], CANON_RAW)
        self.assertIs(n["technically_independent"], False)
        self.assertEqual(n["review_class_after_final"], "FORMAL_PASS_C_OWNER_EQUIVALENT")
        self.assertEqual(n["git_first_stage_commit_sha"], "b4c985688c4bee3db76d18bb0c3ada940ec79c98")
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
        self.assertIn("ChatGPT/OpenAI GPT-6", t)
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
        for s in ("RESEARCH_ONLY_WITHDRAWN_NOT_OWNER_PRESENTABLE", SEALED_MD[:8], ACTUAL_MD[:8], "c4c5fa5d",
                  "certificate in this PR is `blocked`, not `pass`", "No owner keep or owner add is cut", "final newline"):
            self.assertIn(s, memo)


if __name__ == "__main__":
    unittest.main()
