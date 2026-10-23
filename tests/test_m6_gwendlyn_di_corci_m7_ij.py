"""Candidate-specific M6 I / J evidence for the Gwendlyn Di Corci M7 research candidate.

Recomputes bound byte and logical hashes (zones commander / main), runs the authoritative J bundle checker, asserts the
I certificate stays tested-pool-local with no approval/lock claim, and pins the fail-closed Pass C explicit-false non-independence
wording and the Stage A seal mapping (canonical field names) for this deck. The candidate is RESEARCH_ONLY (one genuine
swap, below the five-swap floor); nothing here is owner approval.
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

D = "Gwendlyn_Di_Corci"
S = "gwendlyn-di-corci"
CERT = ROOT / f"data/grixis/m6/ij/certificates/{S}-m7.json"
BUNDLE = ROOT / f"data/grixis/m6/ij/revision_bundles/{S}-m7.json"
POOL = ROOT / f"data/grixis/m6/ij/tested_pools/{D}_M7_tested_configurations_20261023.json"
SNAP = ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json"
MEMO = ROOT / f"data/grixis/m6/certification_preflight/{D}_M6_I_local_best_20261023.md"
PACKET = ROOT / f"data/grixis/m7/decision_reviews/{D}.json"
CANON_RAW = "9a393cb7edf40f9bfb388d37dd657839cad851dc6a021440c7d1b239c1fd20a9"
CAND_RAW = "f5f26b78a09f9247be2e311dd76b6e1ff3ed012cd2eaa66692cb33b68fc38197"
FINAL = f"data/grixis/m6/owner_pass_c_substitute/{D}/final_disposition.md"
SEAL = f"data/grixis/m6/owner_pass_c_substitute/{D}/seal.json"
EXPLICIT = "technical independence **false**"
ADDS = ["Hymn to Tourach"]
CUTS = ["Dauthi Voidwalker"]
APH, STONE = "Aphetto Alchemist", "Magewright's Stone"
RINGS = "Rings of Brighthearth"
EXPECTED_DELTAS = {
    "BASELINE": ([], []),
    "CANONICAL_EXPORT": ([], []),
    "RESEARCH_ONE": (ADDS, CUTS),
    "PASS_C_EXACT_APHETTO_MINUS_STONE_ON_BASELINE": ([APH], [STONE]),
    "CANDIDATE_PLUS_APHETTO_MINUS_STONE": (ADDS + [APH], CUTS + [STONE]),
    "PASS_C_FALLBACK_RINGS_MINUS_MIND_TWIST": ([RINGS], ["Mind Twist"]),
    "ONE_RINGS_OVER_DAUTHI": ([RINGS], CUTS),
    "TWO_WHISPERING_MADNESS_OVER_REFORGE": (ADDS + ["Whispering Madness"], CUTS + ["Reforge the Soul"]),
    "CHALLENGE_SULFUROUS_SPRINGS_OVER_NECROPOLIS": (["Sulfurous Springs"], ["Crumbling Necropolis"]),
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


class GwendlynDiCorciM7IJ(unittest.TestCase):
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
            self.assertEqual([n for z, n, _ in r if z == "commander"], ["Gwendlyn Di Corci"], cfg["id"])
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
        self.assertEqual(ids["RESEARCH_ONE"]["raw_sha256"], CAND_RAW)
        self.assertEqual(self.c["list_hash"], ids["RESEARCH_ONE"]["logical_hash"])
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
        self.assertEqual(pk["readiness"], "RESEARCH_ONLY_WITHDRAWN_NOT_OWNER_PRESENTABLE")
        audit = pk["low_swap_heightened_audit"]
        weak = {x["card"]: x for x in audit["weakest_slot_challenge"]}
        self.assertGreaterEqual(len(weak), 8)
        for card in CUTS + [STONE, "Dream Salvage", "Anvil of Bogardan", "Reforge the Soul", "Underworld Dreams",
                            "Crumbling Necropolis", "Mind Twist"]:
            self.assertIn(card, weak)
        pk_sets = [(sorted(p["adds"]), sorted(p["cuts"])) for p in audit["multi_slot_packages"]]
        self.assertEqual(len(pk_sets), 2)
        for add, cut in ((APH, STONE), ("Whispering Madness", "Reforge the Soul")):
            self.assertIn((sorted(ADDS + [add]), sorted(CUTS + [cut])), pk_sets)
        judged = {c["card"]: c["judgment"] for c in pk["material_candidates"]}
        for card in ("Whispering Madness", "Swiftfoot Boots", "Drown in the Loch", "Kederekt Parasite", "Lavaborn Muse",
                     "Rankle, Master of Pranks", "Tinybones, the Pickpocket", "Davriel, Rogue Shadowmage",
                     "Vizier of Tumbling Sands", "Retreat to Coralhelm", "Sulfurous Springs", "Mana Vault"):
            self.assertEqual(judged[card], "REJECT", card)
        self.assertEqual(judged[APH], "RETAIN_ALTERNATIVE")
        self.assertEqual(judged[RINGS], "RETAIN_ALTERNATIVE")
        self.assertEqual(judged["Hymn to Tourach"], "SELECT_ADD")
        memo = MEMO.read_text()
        for s in ("Self-challenge", "Only one genuine improvement was found, so the deck is RESEARCH_ONLY",
                  "Five is a floor, not a target", "Pass C exact (+Aphetto Alchemist \u2212Magewright's Stone)",
                  "Pass C fallback (+Rings of Brighthearth \u2212Mind Twist)", "Owner direction",
                  "Flagged owner-blueprint override", "Owner-removed cards are not re-added", "RETAIN_ALTERNATIVE",
                  "NON-INDEPENDENT owner-equivalent", "Not done, stated plainly"):
            self.assertIn(s, memo)


class GwendlynDiCorciPassCFailsClosed(unittest.TestCase):
    """This deck's receipt is accepted only through the checker's generic strict explicit-false disclosure
    ('technical independence **false**'); it matches neither the parenthetical pattern nor any deck-bound preserved
    wording, and an explicit technical-independence TRUE/YES statement anywhere vetoes it."""

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
        self.assertEqual(t.count(EXPLICIT), 1)
        self.assertTrue(standard.pass_c_explicit_false_disclosure(t))
        self.assertFalse(standard.pass_c_parenthetical_false_disclosure(t))
        self.assertFalse(standard.pass_c_preserved_nonindependence(t, D))
        for legacy in ("Technically independent third model", "**actual technical independence:** false",
                       "**Technically independent:** NO.", "**Technically independent:** FALSE."):
            self.assertNotIn(legacy, t)
        return t

    def test_explicit_false_wording_accepted(self):
        self.assertTrue(self.run_with(FINAL, self.receipt()))

    def test_true_missing_or_contradictory_rejected(self):
        t = self.receipt()
        bad = [
            t.replace(EXPLICIT, "technical independence **true**"),
            t.replace(EXPLICIT, "technical independence TRUE"),
            t.replace(EXPLICIT, "technically independent: yes"),
            t.replace(EXPLICIT, ""),
            t.replace(EXPLICIT, "technical independence **unknown**"),
            t + "\nCorrection: technical independence TRUE.\n",
            t + "\nCorrection: technically independent: yes\n",
            t.replace("ChatGPT/OpenAI GPT-6", "another model"),
        ]
        for text in bad:
            with self.assertRaises(ValueError):
                self.run_with(FINAL, text)

    def test_seal_aliases_map_to_canonical_fields_and_seal_not_rewritten(self):
        seal = json.loads((ROOT / SEAL).read_text())
        n = standard.normalize_stage_a_seal_aliases(seal, D)
        self.assertEqual(n["canonical_input_sha256"], CANON_RAW)
        self.assertIs(n["technically_independent"], False)
        self.assertEqual(n["review_class_after_final"], "FORMAL_PASS_C_OWNER_EQUIVALENT")
        self.assertEqual(n["stage_a_json_sha256"], seal["artifacts"]["stage_a.json"]["sha256"])
        self.assertEqual(seal["artifacts"]["stage_a.md"]["sha256"],
                         "fce722dd3021dd25e7a7aa6d0ee69d41fa16f04d1f9e146ab92d6bd830dfc668")
        self.assertIs(seal["technical_model_independence"], False)
        self.assertIs(seal["owner_independence_waiver"], True)
        self.assertEqual(seal, json.loads((ROOT / SEAL).read_text()))
        import copy
        no_json_sha = copy.deepcopy(seal)
        del no_json_sha["artifacts"]["stage_a.json"]["sha256"]
        wrong_sha = copy.deepcopy(seal)
        wrong_sha["artifacts"]["stage_a.json"]["sha256"] = "0" * 64
        for bad in (dict(seal, technical_model_independence=True), no_json_sha, wrong_sha,
                    dict(seal, formal_pass_c_classification="INDEPENDENT")):
            with self.assertRaises(ValueError):
                self.run_with(SEAL, json.dumps(bad))


if __name__ == "__main__":
    unittest.main()
