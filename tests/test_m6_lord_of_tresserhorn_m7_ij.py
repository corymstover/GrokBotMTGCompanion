"""Candidate-specific M6 I / J evidence for the Lord_of_Tresserhorn (Lord of Tresserhorn) M7 review candidate.

Recomputes bound byte and logical hashes (zones commander / main), runs the authoritative J bundle checker, asserts the
I certificate stays tested-pool-local with no approval/lock claim, and pins the fail-closed deck-bound preserved Pass C
non-independence wording (`technically_independent=false`) and the schema 1.0 Stage A seal mapping for this deck.
The candidate is a five-swap review candidate (READY_FOR_EXACT_OWNER_APPROVAL_NOT_YET_APPROVED); nothing here is owner
approval. Lord's actual Oracle text is used; there is no opponent-regeneration clause.
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

D = "Lord_of_Tresserhorn"
S = "lord-of-tresserhorn"
CERT = ROOT / f"data/grixis/m6/ij/certificates/{S}-m7.json"
BUNDLE = ROOT / f"data/grixis/m6/ij/revision_bundles/{S}-m7.json"
POOL = ROOT / f"data/grixis/m6/ij/tested_pools/{D}_M7_tested_configurations_20261023.json"
SNAP = ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json"
MEMO = ROOT / f"data/grixis/m6/certification_preflight/{D}_M6_I_local_best_20261023.md"
PACKET = ROOT / f"data/grixis/m7/decision_reviews/{D}.json"
CANON_RAW = "95863276f38beff6b0cf7609041006a6f1de94d5e62c73d76551d6793ffa5b8e"
CAND_RAW = "fd09cb267660206b834257e5c455259985b0e53316743835f679760b11200f85"
FINAL = f"data/grixis/m6/owner_pass_c_substitute/{D}/final_disposition.md"
SEAL = f"data/grixis/m6/owner_pass_c_substitute/{D}/seal.json"
PRESERVED = "`technically_independent=false`"
COMMANDERS = ["Lord of Tresserhorn"]
BMC, CON, FG, ORN, SKC = ("Black Market Connections", "Consign to Memory", "Fierce Guardianship",
                          "Ornithopter of Paradise", "Skullclamp")
COV, FTS, FEL, SHE, SDN = ("Cover of Darkness", "Feed the Swarm", "Fellwar Stone", "Sheoldred's Edict", "Stubborn Denial")
ADDS = [BMC, CON, FG, ORN, SKC]
CUTS = [COV, FTS, FEL, SHE, SDN]
CAND = (ADDS, CUTS)
EXPECTED_DELTAS = {
    "BASELINE": ([], []),
    "CANONICAL_EXPORT": ([], []),
    "REVIEW_CANDIDATE_FIVE_SWAP": CAND,
    "ALT_A_FOUR_SWAPS_KEEP_SHEOLDREDS_EDICT": ([BMC, CON, FG, ORN], [COV, FTS, FEL, SDN]),
    "ALT_B_SKULLCLAMP_OVER_MUDDLE_KEEP_EDICT": (ADDS, [COV, FTS, FEL, "Muddle the Mixture", SDN]),
    "ALT_C_SKULLCLAMP_OVER_NIGHTSCAPE_FAMILIAR": (ADDS, [COV, FTS, FEL, "Nightscape Familiar", SDN]),
    "PASS_C_SOULS_FIRE_OVER_SHEOLDREDS_EDICT": ([BMC, CON, FG, ORN, "Soul's Fire"], CUTS),
    "PASS_C_FIERCE_GUARDIANSHIP_OVER_NIGHTSCAPE_FAMILIAR": (ADDS, [COV, FTS, FEL, "Nightscape Familiar", SHE]),
    "PASS_C_DISTORTION_STRIKE_OVER_ROGUES_PASSAGE": (ADDS + ["Distortion Strike"], CUTS + ["Rogue's Passage"]),
    "REJECT_AQUEOUS_FORM_OVER_MUDDLE": (ADDS + ["Aqueous Form"], CUTS + ["Muddle the Mixture"]),
    "REJECT_PRIOR_DRAFT_TEMUR_BATTLE_RAGE_OVER_PAIN_FOR_ALL": ([BMC, FG, ORN, SKC, "Temur Battle Rage"],
                                                              [COV, FEL, "Pain for All", SHE, SDN]),
    "REJECT_ORIGINAL_TENTATIVE_PLAN": (["Aqueous Form", FG, SKC, "Soul's Fire", "Temur Battle Rage"],
                                       [COV, FEL, "Nightscape Familiar", "Pain for All", SHE]),
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


class LordOfTresserhornM7IJ(unittest.TestCase):
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
        self.assertEqual(ids["REVIEW_CANDIDATE_FIVE_SWAP"]["raw_sha256"], CAND_RAW)
        self.assertEqual(self.c["list_hash"], ids["REVIEW_CANDIDATE_FIVE_SWAP"]["logical_hash"])
        self.assertNotEqual(ids["REVIEW_CANDIDATE_FIVE_SWAP"]["logical_hash"], self.reg["current_canonical_hash"])
        for alt in ("ALT_A_FOUR_SWAPS_KEEP_SHEOLDREDS_EDICT", "ALT_B_SKULLCLAMP_OVER_MUDDLE_KEEP_EDICT"):
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
        self.assertIn(".github/workflows/m7-lord-of-tresserhorn.yml", paths)
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
        self.assertEqual(pk["readiness"], "READY_FOR_EXACT_OWNER_APPROVAL_NOT_YET_APPROVED")
        audit = pk["low_swap_heightened_audit"]
        weak = {x["card"]: x for x in audit["weakest_slot_challenge"]}
        self.assertGreaterEqual(len(weak), 10)
        for card in CUTS + ["Muddle the Mixture", "Nightscape Familiar", "Rogue's Passage", "Pain for All", "Terminate"]:
            self.assertIn(card, weak)
        pk_sets = [(sorted(p["adds"]), sorted(p["cuts"])) for p in audit["multi_slot_packages"]]
        self.assertEqual(pk_sets[0], (sorted(ADDS), sorted(CUTS)))
        judged = {c["card"]: c["judgment"] for c in pk["material_candidates"]}
        self.assertEqual(len(judged), 15)
        for card in ADDS:
            self.assertEqual(judged[card], "SELECT_ADD", card)
        for card in ("Soul's Fire", "Distortion Strike"):
            self.assertEqual(judged[card], "RETAIN_ALTERNATIVE", card)
        for card in ("Temur Battle Rage", "Aqueous Form", "Embercleave", "Psychotic Fury", "Glistening Oil"):
            self.assertEqual(judged[card], "REJECT", card)
        memo = MEMO.read_text()
        for s in ("Five is a floor, not a target", "Owner direction", "**All five cuts are flagged**",
                  "No owner-removed card is re-added", "no provenance exception is used",
                  "There is **no opponent-regeneration clause**", "NON-INDEPENDENT owner-equivalent review (ChatGPT/OpenAI GPT-6",
                  "Not run", "Dress Down layer-6 truth table", "staged",
                  "READY_FOR_EXACT_OWNER_APPROVAL_NOT_YET_APPROVED", "CR 903.3d"):
            self.assertIn(s, memo)


class LordOfTresserhornPassCFailsClosed(unittest.TestCase):
    """This deck's receipt is accepted only through the checker's deck-bound preserved non-independence wording
    ('`technically_independent=false`'); it is neither the explicit 'technically independent **false**' form nor the
    parenthetical form, and an explicit independence TRUE/YES statement anywhere vetoes it."""

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
        self.assertFalse(standard.pass_c_preserved_nonindependence(t, "Loki__the_Deceiver"))
        self.assertIn("NEEDS TESTING", t)
        self.assertIn("ChatGPT/OpenAI GPT-6", t)
        return t

    def test_preserved_wording_accepted(self):
        self.assertTrue(self.run_with(FINAL, self.receipt()))

    def test_true_missing_or_contradictory_rejected(self):
        t = self.receipt()
        bad = [
            t.replace(PRESERVED, "`technically_independent=true`"),
            t.replace(PRESERVED, "`technically_independent`"),
            t + "\nCorrection: technical independence TRUE.\n",
            t + "\nCorrection: technically independent: yes\n",
            t.replace("ChatGPT/OpenAI GPT-6", "another model"),
        ]
        for text in bad:
            with self.assertRaises(ValueError):
                self.run_with(FINAL, text)

    def test_schema_1_0_seal_maps_to_canonical_fields_and_seal_not_rewritten(self):
        raw = (ROOT / SEAL).read_text()
        seal = json.loads(raw)
        self.assertEqual(seal["schema_version"], "1.0")
        self.assertEqual(seal["sealed_on"], "2026-10-21")
        self.assertIs(seal["cannot_claim_technical_independence"], True)
        n = standard.normalize_stage_a_seal_aliases(seal, D)
        self.assertEqual(n["canonical_input_sha256"], CANON_RAW)
        self.assertIs(n["technically_independent"], False)
        self.assertEqual(n["review_class_after_final"], "FORMAL_PASS_C_OWNER_EQUIVALENT")
        self.assertEqual(n["actual_evaluator"], "ChatGPT/OpenAI GPT-6")
        self.assertEqual(n["git_first_stage_commit_sha"], "f6d930bfa97c59fb39a04e3ed6223fbaea6ccb19")
        self.assertEqual(n["stage_a_json_sha256"], "ee6c5c80260cc21768a3889a74766ef6517a0bf4a0e76b5ac19b1d55208c07e6")
        self.assertEqual(n["stage_a_md_sha256"], "02ca73a0c891a418377a17ab61bccd0dfcebfb221d9748bece2f8baa8421043f")
        self.assertEqual(n["stage_a_md_sha256"], sha(f"data/grixis/m6/owner_pass_c_substitute/{D}/stage_a.md"))
        self.assertEqual(n["stage_a_json_sha256"], sha(f"data/grixis/m6/owner_pass_c_substitute/{D}/stage_a.json"))
        self.assertEqual(seal["independence_requirement"], "OWNER_WAIVED_FOR_FORMAL_PASS_C")
        self.assertEqual((ROOT / SEAL).read_text(), raw)
        wrong_sha = copy.deepcopy(seal)
        wrong_sha["immutable_stage_a_files"]["stage_a.json"]["sha256"] = "0" * 64
        for bad in (dict(seal, technically_independent=True), wrong_sha,
                    dict(seal, independence_requirement="INDEPENDENT"), dict(seal, stage="B_SEAL")):
            with self.assertRaises(ValueError):
                self.run_with(SEAL, json.dumps(bad))


if __name__ == "__main__":
    unittest.main()
