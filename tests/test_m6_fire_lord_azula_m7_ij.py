"""Candidate-specific M6 I / J evidence for the Fire Lord Azula M7 candidate.

Recomputes bound byte and logical hashes (zones commander / main), runs the authoritative J bundle checker, asserts the
I certificate stays tested-pool-local with no approval/lock claim, and pins the fail-closed Pass C non-independence
wording and the Stage A seal mapping (canonical field names) for this deck.
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

D = "Fire_Lord_Azula"
S = "fire-lord-azula"
CERT = ROOT / f"data/grixis/m6/ij/certificates/{S}-m7.json"
BUNDLE = ROOT / f"data/grixis/m6/ij/revision_bundles/{S}-m7.json"
POOL = ROOT / f"data/grixis/m6/ij/tested_pools/{D}_M7_tested_configurations_20261023.json"
SNAP = ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json"
MEMO = ROOT / f"data/grixis/m6/certification_preflight/{D}_M6_I_local_best_20261023.md"
PACKET = ROOT / f"data/grixis/m7/decision_reviews/{D}.json"
CANON_RAW = "b6ef396641f2b5cfac0eb81fb494f21f3745e2a3fd47fa75d2eaadbdc34ddee5"
CAND_RAW = "f4136ea0028ee787dddad379e12a7e34ccdaa6578a52d1c63ae953734e5806f2"
FINAL = f"data/grixis/m6/owner_pass_c_substitute/{D}/final_disposition.md"
SEAL = f"data/grixis/m6/owner_pass_c_substitute/{D}/seal.json"
EXPLICIT_FALSE = "technical independence FALSE"
ADDS = ["Turnabout", "Sink into Stupor // Soporific Springs", "Unexpected Windfall", "Flashback", "Mistrise Village"]
CUTS = ["Samut, Tyrant of Naktamun", "Exotic Orchard", "Vivi Ornitier", "Swan Song", "Gemstone Caverns"]
EXPECTED_DELTAS = {
    "BASELINE": ([], []),
    "CANONICAL_EXPORT": ([], []),
    "PREFERRED_FIVE": (ADDS, CUTS),
    "FOUR_KEEP_SAMUT_NO_TURNABOUT": (ADDS[1:], CUTS[1:]),
    "FOUR_KEEP_SWAN_SONG_NO_FLASHBACK": (ADDS[:3] + ADDS[4:], CUTS[:3] + CUTS[4:]),
    "FIVE_KEEP_GEMSTONE_CAVERNS_CUT_WOODED_FOOTHILLS": (ADDS, CUTS[:4] + ["Wooded Foothills"]),
    "SIX_MOX_AMBER_OVER_FELLWAR_STONE": (ADDS + ["Mox Amber"], CUTS + ["Fellwar Stone"]),
    "PASS_C_SPELLSEEKER_OVER_SAMUT_BASELINE": (["Spellseeker"], ["Samut, Tyrant of Naktamun"]),
    "PASS_C_STORMKILN_OVER_BIGSCORE_BASELINE": (["Storm-Kiln Artist"], ["Big Score"]),
    "PASS_C_STORMKILN_OVER_WANSHITONG_BASELINE": (["Storm-Kiln Artist"], ["Wan Shi Tong, Librarian"]),
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


class FireLordAzulaM7IJ(unittest.TestCase):
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
        base = Counter({n: q for z, n, q in rows(self.pool["configurations"][0]["path"])})
        for cfg in self.pool["configurations"]:
            self.assertEqual(sha(cfg["path"]), cfg["raw_sha256"], cfg["id"])
            self.assertEqual(self.lh(cfg["path"]), cfg["logical_hash"], cfg["id"])
            self.assertEqual(cfg["physical_cards"], 100, cfg["id"])
            r = rows(cfg["path"])
            self.assertEqual(sum(q for _, _, q in r), 100, cfg["id"])
            self.assertEqual([n for z, n, _ in r if z == "commander"], ["Fire Lord Azula"], cfg["id"])
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
        self.assertEqual(ids["PREFERRED_FIVE"]["raw_sha256"], CAND_RAW)
        self.assertEqual(self.c["list_hash"], ids["PREFERRED_FIVE"]["logical_hash"])
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
        for p in (CERT, BUNDLE, POOL, MEMO):
            t = p.read_text()
            self.assertNotIn('"APPROVED"', t)
            self.assertNotIn("CANONICAL_LOCKED", t)
        self.assertNotIn("baseline_provenance_exception", json.loads(PACKET.read_text()))

    def test_self_challenge_recorded_in_packet_and_memo(self):
        pk = json.loads(PACKET.read_text())
        pf = pk["open_ended_optimization_audit"]["post_floor_challenges"]
        chal = {x["challenger"]: x["disposition"] for x in pf}
        self.assertGreaterEqual(len({x["incumbent"] for x in pf}), 2)
        for add in ADDS:
            self.assertNotIn(add, chal)  # selected adds may not be post-floor challengers
        for card in ("Culling the Weak", "Dramatic Reversal", "Mana Drain", "Stingcaster Mage", "City of Traitors",
                     "Reiterate", "Lightning Bolt"):
            self.assertEqual(chal[card], "REJECT", card)
        self.assertEqual(chal["Mox Amber"], "RETAIN_ALTERNATIVE")
        self.assertEqual(chal["Storm-Kiln Artist"], "RETAIN_ALTERNATIVE")
        self.assertEqual(len(pf), 10)
        memo = MEMO.read_text()
        self.assertIn("Self-challenge", memo)
        self.assertIn("+Spellseeker / \u2212Samut", memo)
        self.assertIn("Four-swap keeping Samut", memo)
        self.assertIn("Owner direction", memo)
        self.assertIn("One owner addition is overridden: Samut, Tyrant of Naktamun", memo)
        self.assertIn("Six-swap with Mox Amber over Fellwar Stone", memo)
        self.assertIn("Owner-removed cards are not re-added", memo)
        self.assertIn("RETAIN_ALTERNATIVE", memo)
        self.assertIn("NON-INDEPENDENT owner-equivalent", memo)
        self.assertIn("Not done, stated plainly", memo)


class FireLordAzulaPassCFailsClosed(unittest.TestCase):
    """This deck's receipt is accepted through the checker's explicit-false path (the receipt says '...leaves technical
    independence FALSE...', matched by the explicit-false pattern) and only without any TRUE/YES claim."""

    def run_with(self, target, text):
        b = json.loads(BUNDLE.read_text())
        real_safe, real_bind = standard.safe_repo_file, standard.bind
        with tempfile.TemporaryDirectory() as d:
            fake = Path(d) / Path(target).name
            fake.write_text(text, encoding="utf-8")
            with mock.patch.object(standard, "safe_repo_file",
                                   lambda p: fake if str(p).endswith(target) else real_safe(p)), \
                 mock.patch.object(standard, "bind",
                                   lambda n, h: None if str(n).endswith(target) else real_bind(n, h)):
                return standard.validate_pass_c(dict(b["pass_c"]), D)

    def explicit(self):
        t = (ROOT / FINAL).read_text(encoding="utf-8")
        self.assertEqual(t.count(EXPLICIT_FALSE), 1)
        self.assertTrue(standard.pass_c_explicit_false_disclosure(t))
        self.assertIn("Technically independent reviewer **FALSE**", t)
        return t

    def test_explicit_false_wording_accepted(self):
        self.assertTrue(self.run_with(FINAL, self.explicit()))

    def test_true_missing_or_contradictory_rejected(self):
        t = self.explicit()
        bad = [
            t.replace(EXPLICIT_FALSE, "technical independence TRUE"),
            t.replace(EXPLICIT_FALSE, "technical independence YES"),
            t.replace(EXPLICIT_FALSE, "technically independent: yes"),
            t.replace(EXPLICIT_FALSE, ""),
            t + "\nCorrection: technical independence TRUE.\n",
            t + "\nCorrection: technically independent: yes\n",
        ]
        for text in bad:
            with self.assertRaises(ValueError):
                self.run_with(FINAL, text)

    def test_seal_uses_canonical_fields_and_is_not_rewritten(self):
        seal = json.loads((ROOT / SEAL).read_text())
        n = standard.normalize_stage_a_seal_aliases(seal, D)
        self.assertEqual(n["canonical_input_sha256"], CANON_RAW)
        self.assertIs(n["technically_independent"], False)
        self.assertEqual(n["review_class_after_final"], "FORMAL_PASS_C_OWNER_EQUIVALENT")
        self.assertEqual(seal, json.loads((ROOT / SEAL).read_text()))
        for bad in (dict(seal, technically_independent=True),
                    {k: v for k, v in seal.items() if k != "stage_a_json_raw_sha256"},
                    dict(seal, stage_a_json_raw_sha256="0" * 64),
                    dict(seal, formal_pass_c_qualification="INDEPENDENT")):
            with self.assertRaises(ValueError):
                self.run_with(SEAL, json.dumps(bad))


if __name__ == "__main__":
    unittest.main()
