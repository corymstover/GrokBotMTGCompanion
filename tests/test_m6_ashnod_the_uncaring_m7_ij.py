"""Candidate-specific M6 I / J evidence for the Ashnod the Uncaring M7 candidate.

Recomputes bound byte and logical hashes, runs the authoritative J bundle checker,
asserts the I certificate stays tested-pool-local with no approval/lock claim, and
pins the narrow fail-closed Pass C non-independence wording check.
"""
import glob
import hashlib
import inspect
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

D = "Ashnod_the_Uncaring"
CERT = ROOT / "data/grixis/m6/ij/certificates/ashnod-the-uncaring-m7.json"
BUNDLE = ROOT / "data/grixis/m6/ij/revision_bundles/ashnod-the-uncaring-m7.json"
POOL = ROOT / "data/grixis/m6/ij/tested_pools/Ashnod_the_Uncaring_M7_tested_configurations_20261023.json"
SNAP = ROOT / "data/grixis/m6/oracle_snapshots/Ashnod_the_Uncaring_M7_Scryfall_20261023.json"
MEMO = ROOT / "data/grixis/m6/certification_preflight/Ashnod_the_Uncaring_M6_I_local_best_20261023.md"
PACKET = ROOT / "data/grixis/m7/decision_reviews/Ashnod_the_Uncaring.json"
CANON_RAW = "f574e4fad4749603294f53d2fe5536a159f884a8f1a8a7b6b1a22b3a637cf1cf"
CAND_RAW = "b1078f084c2fa53426910edb66f0a036978e06bd9c9a2061f460af397503143d"
FINAL = "data/grixis/m6/owner_pass_c_substitute/Ashnod_the_Uncaring/final_disposition.md"
PRESERVED = "independent=FALSE"
LEGACY = ("Technically independent third model", "**actual technical independence:** false",
          "**Technically independent:** NO.", "**Technically independent:** FALSE.")


def sha(p):
    return hashlib.sha256((ROOT / p).read_bytes()).hexdigest()


class AshnodTheUncaringM7IJ(unittest.TestCase):
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
            self.assertEqual(cfg["physical_cards"], 100, cfg["id"])
        ids = {x["id"]: x for x in self.pool["configurations"]}
        self.assertEqual(ids["BASELINE"]["raw_sha256"], CANON_RAW)
        self.assertEqual("sha256:" + ids["BASELINE"]["raw_sha256"], self.reg["source"]["raw_sha256"])
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

    def test_canonical_registry_untouched_no_provenance_exception_and_no_approval(self):
        self.assertIs(self.reg["source"]["recorded_matches_raw"], True)
        self.assertEqual("sha256:" + self.reg["source"]["recorded_sha256"].removeprefix("sha256:"),
                         self.reg["source"]["raw_sha256"])
        for p in (CERT, BUNDLE, POOL, MEMO):
            t = p.read_text()
            self.assertNotIn('"APPROVED"', t)
            self.assertNotIn("CANONICAL_LOCKED", t)
        self.assertFalse(self.pool["owner_m7_approved"])

    def test_self_challenge_recorded_in_packet_and_memo(self):
        pk = json.loads(PACKET.read_text())
        chal = {x["challenger"]: x["disposition"] for x in pk["open_ended_optimization_audit"]["post_floor_challenges"]}
        self.assertEqual(chal["Sage of Lat-Nam"], "RETAIN_ALTERNATIVE")
        self.assertEqual(chal["Spire of Industry"], "RETAIN_ALTERNATIVE")
        self.assertGreaterEqual(len(chal), 2)
        memo = MEMO.read_text()
        self.assertIn("Self-challenge", memo)
        self.assertIn("Krark-Clan Shaman", memo)


class PassCDisclosureWordingFailsClosed(unittest.TestCase):
    """Narrow fix: explicit FALSE/NO technical-independence statements pass; TRUE, ambiguous,
    missing or contradictory statements fail; every previously accepted receipt still passes."""

    def run_with_final_text(self, text):
        b = json.loads(BUNDLE.read_text())
        real = standard.safe_repo_file
        with tempfile.TemporaryDirectory() as d:
            fake = Path(d) / "final_disposition.md"
            fake.write_text(text, encoding="utf-8")
            with mock.patch.object(standard, "safe_repo_file",
                                   lambda p: fake if str(p).endswith(FINAL) else real(p)):
                return standard.validate_pass_c(b["pass_c"], D)

    def preserved(self):
        t = (ROOT / FINAL).read_text(encoding="utf-8")
        self.assertEqual(t.count(PRESERVED), 1)
        self.assertFalse(any(s in t for s in LEGACY))  # legacy substrings do not accept it
        self.assertFalse(standard.pass_c_explicit_false_disclosure(t))  # nor does the PR #653 pattern
        self.assertTrue(standard.pass_c_parenthetical_false_disclosure(t))  # the new strict pattern does
        return t

    def test_preserved_wording_accepted(self):
        self.assertTrue(self.run_with_final_text(self.preserved()))

    def test_true_ambiguous_missing_or_contradictory_rejected(self):
        t = self.preserved()
        bad = [
            t.replace(PRESERVED, "independent=TRUE"),
            t.replace(PRESERVED, "independent = yes"),
            t.replace(PRESERVED, "independent=UNKNOWN"),
            t.replace(PRESERVED, "independent=not assessed"),
            t.replace(PRESERVED, "independent=NOT FALSE"),
            t.replace(PRESERVED, "independent"),
            t.replace(PRESERVED, "FALSE"),
            t.replace(PRESERVED, ""),
            t.replace("technical third-model independence (", "third-model review ("),
            t + "\nCorrection: independent=TRUE.\n",
            t + "\nCorrection: technical independence TRUE.\n",
        ]
        for text in bad:
            with self.assertRaises(ValueError):
                self.run_with_final_text(text)

    def test_pattern_unit_cases(self):
        f = standard.pass_c_explicit_false_disclosure
        for ok in ("technical independence FALSE, existing exposure shared.",
                   "**Technically independent:** FALSE.", "**Technically independent:** NO.",
                   "**actual technical independence:** false.", "technically independent **false**,",
                   "technical independence `false`, waiver", "**Technically independent: false.**"):
            self.assertTrue(f(ok), ok)
        for bad in ("", "technical independence TRUE", "technically independent: yes",
                    "technical independence pending", "technical independence no longer applies",
                    "technical independence: NOT FALSE", "technical independence: none",
                    "technical independence false; technical independence true"):
            self.assertFalse(f(bad), bad)

    def test_parenthetical_pattern_unit_cases(self):
        f = standard.pass_c_parenthetical_false_disclosure
        for ok in ("technical third-model independence (actual evaluator X; independent=FALSE, owner-waived)",
                   "technical third-model independence (independent = false)"):
            self.assertTrue(f(ok), ok)
        for bad in ("", "independent=FALSE", "third-model independence (independent=FALSE)",
                    "technical third-model independence (independent=TRUE)",
                    "technical third-model independence (independent=NOT FALSE)",
                    "technical third-model independence (independent=FALSE) and later independent=TRUE",
                    "technical third-model independence (independent=FALSE); technical independence: yes",
                    "technical third-model independence (actual evaluator X) independent=FALSE"):
            self.assertFalse(f(bad), bad)

    def test_new_pattern_accepts_only_ashnod_among_previously_rejected_receipts(self):
        files = sorted(glob.glob(str(ROOT / "data/grixis/m6/owner_pass_c_substitute/*/final_disposition.md")))
        newly = []
        for p in files:
            t = Path(p).read_text(encoding="utf-8")
            before = any(s in t for s in LEGACY) or standard.pass_c_explicit_false_disclosure(t)
            if not before and standard.pass_c_parenthetical_false_disclosure(t):
                newly.append(Path(p).parent.name)
        self.assertEqual(newly, [D])
        src = inspect.getsource(standard.validate_pass_c)
        self.assertIn("pass_c_explicit_false_disclosure(final)", src)  # PR #653 path retained

    def test_superset_of_previously_accepted_receipts(self):
        files = sorted(glob.glob(str(ROOT / "data/grixis/m6/owner_pass_c_substitute/*/final_disposition.md")))
        self.assertEqual(len(files), 62)
        src = inspect.getsource(standard.validate_pass_c)
        for s in LEGACY:  # legacy accepted substrings are retained verbatim
            self.assertIn('"%s" in final' % s, src)
        legacy_accepted = [p for p in files if any(s in Path(p).read_text(encoding="utf-8") for s in LEGACY)]
        self.assertGreaterEqual(len(legacy_accepted), 5)
        anhelo = (ROOT / "data/grixis/m6/owner_pass_c_substitute/Anhelo__the_Painter/final_disposition.md").read_text()
        self.assertIn("**Technically independent:** FALSE.", anhelo)
        self.assertFalse(standard.pass_c_explicit_false_disclosure(
            anhelo.replace("**Technically independent:** FALSE.", "**Technically independent:** TRUE.")))
        self.assertFalse(standard.pass_c_explicit_false_disclosure(
            anhelo.replace("**Technically independent:** FALSE.", "")))


class LegacyStageASealFieldNamesFailClosed(unittest.TestCase):
    """Narrow fix: the exact legacy A_SEAL field names map one-to-one; conflicts, partial forms and
    tampered values fail; seals already in canonical form are returned unchanged."""
    SEAL = "data/grixis/m6/owner_pass_c_substitute/Ashnod_the_Uncaring/seal.json"

    def seal(self):
        return json.loads((ROOT / self.SEAL).read_text())

    def run_with_seal(self, seal):
        b = json.loads(BUNDLE.read_text())
        real_safe, real_bind = standard.safe_repo_file, standard.bind
        with tempfile.TemporaryDirectory() as d:
            fake = Path(d) / "seal.json"
            fake.write_text(json.dumps(seal), encoding="utf-8")
            with mock.patch.object(standard, "safe_repo_file",
                                   lambda p: fake if str(p).endswith(self.SEAL) else real_safe(p)), \
                 mock.patch.object(standard, "bind",
                                   lambda n, h: None if str(n).endswith(self.SEAL) else real_bind(n, h)):
                return standard.validate_pass_c(b["pass_c"], D)

    def test_preserved_legacy_seal_normalizes_and_passes(self):
        s = self.seal()
        n = standard.normalize_legacy_stage_a_seal(s)
        self.assertEqual(n["canonical_input_sha256"], CANON_RAW)
        self.assertIs(n["technically_independent"], False)
        self.assertEqual(n["review_class_after_final"], standard.OWNER_EQUIVALENT)
        self.assertEqual(n["actual_evaluator"], "ChatGPT/OpenAI GPT-6")
        self.assertTrue(self.run_with_seal(s))

    def test_conflicting_partial_or_tampered_legacy_seals_rejected(self):
        s = self.seal()
        both = dict(s, technically_independent=False)
        with self.assertRaises(ValueError):
            standard.normalize_legacy_stage_a_seal(both)
        bad = [dict(s, technical_independence=True), dict(s, technical_independence=None),
               dict(s, formal_pass_c_classification="INDEPENDENT"), dict(s, actual_model="Other"),
               dict(s, canonical_approved_sha256="0" * 64), dict(s, first_stage_git_commit_sha="0" * 40),
               dict(s, deck_id="Ashad__the_Lone_Cyberman"), dict(s, stage="B_SEAL"),
               dict(s, owner_independence_waiver=False), dict(s, stage_a_md_sha256="0" * 64),
               {k: v for k, v in s.items() if k != "technical_independence"}, both]
        for seal in bad:
            with self.assertRaises(ValueError):
                self.run_with_seal(seal)

    def test_canonical_and_other_seals_unchanged(self):
        for p in sorted(glob.glob(str(ROOT / "data/grixis/m6/owner_pass_c_substitute/*/seal.json"))):
            seal = json.loads(Path(p).read_text())
            if Path(p).parent.name == D:
                continue
            self.assertEqual(standard.normalize_legacy_stage_a_seal(seal), seal, p)


if __name__ == "__main__":
    unittest.main()
