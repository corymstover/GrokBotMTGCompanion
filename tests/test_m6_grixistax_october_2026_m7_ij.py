"""Candidate-specific M6 I / J evidence for the Grixistax___October_2026 (Kraum, Ludevic's Opus + Tevesh Szat, Doom of
Fools) M7 research candidate.

Recomputes bound byte and logical hashes (zones commander / main), runs the authoritative J bundle checker, asserts the
I certificate stays tested-pool-local with no approval/lock claim, and pins the fail-closed deck-bound preserved Pass C
non-independence wording and the jlk-neutral-seal-1 Stage A seal mapping (canonical field names) for this deck.
The candidate is RESEARCH_ONLY (two genuine swaps, below the five-swap floor); nothing here is owner approval.
"""
from collections import Counter
import copy
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

D = "Grixistax___October_2026"
S = "grixistax-october-2026"
CERT = ROOT / f"data/grixis/m6/ij/certificates/{S}-m7.json"
BUNDLE = ROOT / f"data/grixis/m6/ij/revision_bundles/{S}-m7.json"
POOL = ROOT / f"data/grixis/m6/ij/tested_pools/{D}_M7_tested_configurations_20261023.json"
SNAP = ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json"
MEMO = ROOT / f"data/grixis/m6/certification_preflight/{D}_M6_I_local_best_20261023.md"
PACKET = ROOT / f"data/grixis/m7/decision_reviews/{D}.json"
CANON_RAW = "f36346d4ba965db1e098b0aa92d27a968ee3a14c74a2b9401c1a5357f83c025c"
CAND_RAW = "a04f16ba3a75bd53963866fd0b18c0390af54930b5526e6893ac6c6a6503b858"
FINAL = f"data/grixis/m6/owner_pass_c_substitute/{D}/final_disposition.md"
SEAL = f"data/grixis/m6/owner_pass_c_substitute/{D}/seal.json"
PRESERVED = "**Actual independent third model:** **NO**"
COMMANDERS = ["Kraum, Ludevic's Opus", "Tevesh Szat, Doom of Fools"]
CAND = (["Arcane Signet", "Bitterblossom"], ["Mox Amber", "Windfall"])
EXPECTED_DELTAS = {
    "BASELINE": ([], []),
    "CANONICAL_EXPORT": ([], []),
    "RESEARCH_TWO_SWAP": CAND,
    "PASS_C_TALISMAN_OF_INDULGENCE_OVER_MOX_AMBER": (["Bitterblossom", "Talisman of Indulgence"], ["Mox Amber", "Windfall"]),
    "PASS_C_ARCANE_SIGNET_OVER_OVERBURDEN_KEEP_AMBER": (["Arcane Signet", "Bitterblossom"], ["Overburden", "Windfall"]),
    "ARCANE_SIGNET_ONLY": (["Arcane Signet"], ["Mox Amber"]),
    "BITTERBLOSSOM_OVER_CYCLONIC_RIFT_KEEP_WINDFALL": (["Arcane Signet", "Bitterblossom"], ["Cyclonic Rift", "Mox Amber"]),
    "BITTERBLOSSOM_OVER_MAGUS_OF_THE_MOON_KEEP_WINDFALL": (["Arcane Signet", "Bitterblossom"], ["Magus of the Moon", "Mox Amber"]),
    "STAGED_OPPOSITION_OVER_STATIC_ORB": (["Arcane Signet", "Bitterblossom", "Opposition"], ["Mox Amber", "Static Orb", "Windfall"]),
    "STAGED_OPPOSITION_OVER_MAGUS_OF_THE_MOON": (["Arcane Signet", "Bitterblossom", "Opposition"],
                                                 ["Magus of the Moon", "Mox Amber", "Windfall"]),
    "REJECT_FROZEN_AETHER_OVER_STATIC_ORB": (["Arcane Signet", "Bitterblossom", "Frozen Aether"], ["Mox Amber", "Static Orb", "Windfall"]),
    "REJECT_STRIP_MINE_OVER_GEMSTONE_CAVERNS": (["Arcane Signet", "Bitterblossom", "Strip Mine"],
                                                ["Gemstone Caverns", "Mox Amber", "Windfall"]),
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


class GrixistaxOctober2026M7IJ(unittest.TestCase):
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
        self.assertIn("12 complete configurations", self.c["authority"]["note"])
        self.assertFalse(any("actions/runs" in r for r in self.c["receipt_refs"]))
        for t in self.c["phase_b"]["test_refs"]:
            self.assertTrue((ROOT / t).is_file(), t)

    def test_pool_every_configuration_raw_logical_hash_and_exact_delta(self):
        self.assertEqual("sha256:" + sha(self.c["candidate_pool"]["source_ref"]), self.c["candidate_pool"]["source_sha256"])
        self.assertEqual(self.c["candidate_pool"]["tested_pool_size"], len(self.pool["configurations"]))
        self.assertEqual(len(self.pool["configurations"]), 12)
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
        for alt in ("PASS_C_ARCANE_SIGNET_OVER_OVERBURDEN_KEEP_AMBER", "STAGED_OPPOSITION_OVER_STATIC_ORB"):
            self.assertNotEqual(ids[alt]["logical_hash"], self.c["list_hash"])
        self.assertFalse(self.pool["owner_m7_approved"])

    def test_authoritative_j_checker_passes_and_binds_result(self):
        self.assertTrue(standard.validate_bundle(self.b, standard.load(standard.REGISTRY), standard.load(standard.SEALS)))
        self.assertEqual(self.b["result_hash"], self.c["list_hash"])
        self.assertEqual(self.b["baseline_hash"], self.reg["current_canonical_hash"])
        paths = {i["path"]: i["sha256"] for i in self.b["inputs"]}
        for cfg in self.pool["configurations"]:
            self.assertIn(cfg["path"], paths)
        self.assertIn(str(CERT.relative_to(ROOT)), paths)
        self.assertIn(".github/workflows/m7-grixistax-october-2026.yml", paths)
        self.assertEqual(paths["scripts/grixis_m6_bundle_check.py"], "sha256:" + sha("scripts/grixis_m6_bundle_check.py"))
        self.assertEqual(sha("scripts/grixis_m6_bundle_check.py"),
                         "2962a64053b6ea302924fd74dcc646c5fc6eb318016c0aa57026012ba9b3bf3b")
        for p, h in paths.items():
            self.assertEqual(h, "sha256:" + sha(p), p)
        self.assertFalse(self.b["pass_c"]["technically_independent"])
        self.assertEqual(self.b["pass_c"]["review_class"], "FORMAL_PASS_C_OWNER_EQUIVALENT")
        self.assertTrue(all(not t["supports_improvement_claim"] for t in self.b["phase_b"]["tests"]))

    def test_canonical_registry_untouched_no_provenance_exception_and_no_approval(self):
        self.assertIs(self.reg["source"]["recorded_matches_raw"], True)
        self.assertEqual("sha256:" + self.reg["source"]["recorded_sha256"], self.reg["source"]["raw_sha256"])
        self.assertEqual(self.reg["commanders"], COMMANDERS)
        for p in (CERT, BUNDLE, POOL, MEMO):
            t = p.read_text()
            self.assertNotIn('"APPROVED"', t)
            self.assertNotIn("CANONICAL_LOCKED", t)
        self.assertNotIn("baseline_provenance_exception", json.loads(PACKET.read_text()))

    def test_self_challenge_recorded_in_packet_and_memo(self):
        pk = json.loads(PACKET.read_text())
        self.assertEqual(pk["readiness"], "RESEARCH_ONLY_WITHDRAWN_NOT_OWNER_PRESENTABLE")
        audit = pk["low_swap_heightened_audit"]
        weak = {x["card"]: x for x in audit["weakest_slot_challenge"]}
        self.assertGreaterEqual(len(weak), 10)
        for card in ("Mox Amber", "Windfall", "Static Orb", "Magus of the Moon", "Cyclonic Rift", "Cursed Totem",
                     "Torpor Orb", "Red Elemental Blast", "Mental Misstep", "Gemstone Caverns", "Chain of Vapor",
                     "Jeska's Will", "Gamble", "Wishclaw Talisman", "Overburden", "Karn, the Great Creator", "Tangle Wire"):
            self.assertIn(card, weak)
        pk_sets = [(sorted(p["adds"]), sorted(p["cuts"])) for p in audit["multi_slot_packages"]]
        self.assertEqual(pk_sets, [(["Arcane Signet", "Bitterblossom"], ["Mox Amber", "Windfall"]),
                                   (["Arcane Signet", "Bitterblossom", "Opposition"], ["Mox Amber", "Static Orb", "Windfall"])])
        judged = {c["card"]: c["judgment"] for c in pk["material_candidates"]}
        self.assertGreaterEqual(len(judged), 20)
        for card in ("Arcane Signet", "Bitterblossom"):
            self.assertEqual(judged[card], "SELECT_ADD", card)
        self.assertEqual(judged["Opposition"], "RETAIN_ALTERNATIVE")
        for card in ("Talisman of Indulgence", "Fellwar Stone", "Frozen Aether", "Braids, Cabal Minion", "Strip Mine",
                     "City of Traitors", "Sphere of Resistance", "Null Rod"):
            self.assertEqual(judged[card], "REJECT", card)
        self.assertEqual(judged["Archon of Emeria"], "EXCLUDE_INVALID")
        memo = MEMO.read_text()
        for s in ("Two genuine improvements were found, so the deck is RESEARCH_ONLY",
                  "Five is a floor, not a target", "Owner direction", "no owner card is overridden",
                  "Data caveat", "Owner-removed cards and classes are not re-added", "RETAIN_ALTERNATIVE",
                  "NON-INDEPENDENT owner-equivalent", "Not done, stated plainly", "NEEDS TESTING",
                  "not a commander name", "Torpor Orb ruling 2024-04-12"):
            self.assertIn(s, memo)


class GrixistaxOctober2026PassCFailsClosed(unittest.TestCase):
    """This deck's receipt is accepted only through the checker's deck-bound preserved non-independence wording
    ('**Actual independent third model:** **NO**'); it is neither the explicit 'technically independent **false**'
    form nor the parenthetical form, and an explicit independence TRUE/YES statement anywhere vetoes it."""

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

    def receipt(self):
        t = (ROOT / FINAL).read_text(encoding="utf-8")
        self.assertEqual(t.count(PRESERVED), 1)
        self.assertFalse(standard.pass_c_explicit_false_disclosure(t))
        self.assertFalse(standard.pass_c_parenthetical_false_disclosure(t))
        self.assertTrue(standard.pass_c_preserved_nonindependence(t, D))
        self.assertFalse(standard.pass_c_preserved_nonindependence(t, "Kess__Dissident_Mage"))
        self.assertIn("NEEDS TESTING", t)
        self.assertIn("ChatGPT/OpenAI GPT-6", t)
        return t

    def test_preserved_wording_accepted(self):
        self.assertTrue(self.run_with(FINAL, self.receipt()))

    def test_true_missing_or_contradictory_rejected(self):
        t = self.receipt()
        bad = [
            t.replace(PRESERVED, "**Actual independent third model:** **YES**"),
            t.replace(PRESERVED, "**Actual independent third model:**"),
            t + "\nCorrection: technical independence TRUE.\n",
            t + "\nCorrection: technically independent: yes\n",
            t.replace("ChatGPT/OpenAI GPT-6", "another model"),
        ]
        for text in bad:
            with self.assertRaises(ValueError):
                self.run_with(FINAL, text)

    def test_jlk_neutral_seal_maps_to_canonical_fields_and_seal_not_rewritten(self):
        raw = (ROOT / SEAL).read_text()
        seal = json.loads(raw)
        self.assertEqual(seal["schema_version"], "jlk-neutral-seal-1")
        n = standard.normalize_stage_a_seal_aliases(seal, D)
        self.assertEqual(n["canonical_input_sha256"], CANON_RAW)
        self.assertIs(n["technically_independent"], False)
        self.assertEqual(n["review_class_after_final"], "FORMAL_PASS_C_OWNER_EQUIVALENT")
        self.assertEqual(n["git_first_stage_commit_sha"], "b29a4f304a22e7fd82f07d292afba353dbc6f1e8")
        self.assertEqual(n["stage_a_json_sha256"], "415ba221b0a028053cbbaf564887a832d2a4ea8ab2f19d9d86677b249c37efc2")
        self.assertEqual(n["stage_a_md_sha256"], "ced8de7ff81ddba73c3aa11833d72292120008160c0e0d89b3948b52aceb7308")
        self.assertEqual(n["stage_a_md_sha256"], sha(f"data/grixis/m6/owner_pass_c_substitute/{D}/stage_a.md"))
        self.assertEqual(n["stage_a_json_sha256"], sha(f"data/grixis/m6/owner_pass_c_substitute/{D}/stage_a.json"))
        self.assertEqual(seal["independence_requirement"], "OWNER_WAIVED_FOR_FORMAL_PASS_C")
        self.assertEqual((ROOT / SEAL).read_text(), raw)
        wrong_sha = copy.deepcopy(seal)
        wrong_sha["stage_a_files"]["stage_a.json"]["sha256"] = "0" * 64
        for bad in (dict(seal, technically_independent=True), wrong_sha,
                    dict(seal, independence_requirement="INDEPENDENT"), dict(seal, stage="B_SEAL")):
            with self.assertRaises(ValueError):
                self.run_with(SEAL, json.dumps(bad))


if __name__ == "__main__":
    unittest.main()
