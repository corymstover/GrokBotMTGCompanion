"""Tests for scripts/story_claim_pipeline.py (Phase 5 bulk claim packs).

Runs without the story cache (CI): committed packs must equal a fresh spec build and the audit
hashes must hold. Gate tests use a temporary cache so the verbatim check itself is exercised.
"""
import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import story_claim_pipeline as P  # noqa: E402


def specs():
    return [json.loads(f.read_text(encoding="utf-8")) for f in P.spec_files()]


class CommittedPacks(unittest.TestCase):
    def test_check_passes(self):
        self.assertEqual(P.cmd_check(), 0)

    def test_at_least_three_phase5_packs(self):
        ids = {s["pack_id"] for s in specs()}
        for pid in ("pack_p5_kaladesh_aether_revolt", "pack_p5_ixalan_rivals",
                    "pack_p5_amonkhet_hour_of_devastation"):
            self.assertIn(pid, ids)

    def test_packs_are_preliminary_and_official(self):
        man = json.loads(P.MANIFEST.read_text(encoding="utf-8"))
        for s in specs():
            p, a = P.pack_paths(s["pack_id"])
            pack = json.loads(p.read_text(encoding="utf-8"))
            self.assertEqual(pack["status"], P.STATUS)
            self.assertIn("PRELIMINARY_RESEARCH", pack["status"])
            self.assertIn(f"data/lore_research/{p.name}", man["claim_packs"])
            for src in pack["source_register"].values():
                self.assertTrue(src["url"].startswith("https://magic.wizards.com/"))
            audit = json.loads(a.read_text(encoding="utf-8"))
            self.assertEqual(audit["quotes_verbatim"], audit["quotes"])
            self.assertEqual(audit["problems"], [])

    def test_non_confirmed_claims_carry_limitations(self):
        for s in specs():
            for c in s["claims"]:
                if c["grade"] != "CANON_CONFIRMED":
                    self.assertTrue(c.get("limitation"), c["id"])

    def test_claim_ids_globally_unique(self):
        ids = [c["id"] for s in specs() for c in s["claims"]]
        self.assertEqual(len(ids), len(set(ids)))


    def test_page_keys_globally_unique(self):
        # Page keys become graph source ids; a reused key naming another page breaks the graph build.
        self.assertEqual(P.page_key_collisions(), [])

    def test_page_key_collision_detected(self):
        with tempfile.TemporaryDirectory() as d:
            a, b = Path(d) / "a.spec.json", Path(d) / "b.spec.json"
            a.write_text(json.dumps({"pack_id": "a", "pages": {"guide": "page-one"}}), encoding="utf-8")
            b.write_text(json.dumps({"pack_id": "b", "pages": {"guide": "page-two"}}), encoding="utf-8")
            self.assertEqual(len(P.page_key_collisions([a, b])), 1)
            b.write_text(json.dumps({"pack_id": "b", "pages": {"guide": "page-one"}}), encoding="utf-8")
            self.assertEqual(P.page_key_collisions([a, b]), [])


class Gates(unittest.TestCase):
    def setUp(self):
        self.rows = P.primary_rows()
        self.spec = specs()[0]
        self.tmp = tempfile.TemporaryDirectory()
        self.cache = Path(self.tmp.name)
        for slug in self.spec["pages"].values():
            text = " ".join(q["quote"] for s in specs() for c in s["claims"] for q in c["quotes"]
                            if s["pages"].get(q["page"]) == slug)
            (self.cache / f"{slug}.txt").write_text(text, encoding="utf-8")

    def tearDown(self):
        self.tmp.cleanup()

    def build(self, spec):
        return P.build_pack(spec, self.rows, self.cache, set())[2]

    def test_clean_spec_has_no_problems(self):
        self.assertEqual(self.build(self.spec), [])

    def test_altered_quote_is_rejected(self):
        s = copy.deepcopy(self.spec)
        q = s["claims"][0]["quotes"][0]
        q["quote"] = q["quote"].replace(" ", "  ", 1) + " (invented)"
        self.assertTrue(any("not found verbatim" in p for p in self.build(s)))

    def test_whitespace_only_difference_is_accepted(self):
        s = copy.deepcopy(self.spec)
        q = s["claims"][0]["quotes"][0]
        q["quote"] = q["quote"].replace(" ", "\n ", 1)
        self.assertEqual(self.build(s), [])

    def test_implied_without_limitation_is_rejected(self):
        s = copy.deepcopy(self.spec)
        s["claims"][0]["grade"] = "CANON_IMPLIED"
        s["claims"][0].pop("limitation", None)
        self.assertTrue(any("needs a limitation" in p for p in self.build(s)))

    def test_unknown_grade_and_short_quote_rejected(self):
        s = copy.deepcopy(self.spec)
        s["claims"][0]["grade"] = "APPROVED"
        s["claims"][0]["quotes"].append({"page": s["claims"][0]["quotes"][0]["page"], "quote": "short"})
        probs = self.build(s)
        self.assertTrue(any("unknown grade" in p for p in probs))
        self.assertTrue(any("shorter than" in p for p in probs))

    def test_wrong_arc_page_rejected(self):
        s = copy.deepcopy(self.spec)
        s["arc"] = "NOT_AN_ARC"
        self.assertTrue(any("is tagged" in p for p in self.build(s)))

    def test_undeclared_subject_and_duplicate_id_rejected(self):
        s = copy.deepcopy(self.spec)
        s["claims"][1]["id"] = s["claims"][0]["id"]
        s["claims"][0]["subject"] = "nobody_declared"
        probs = self.build(s)
        self.assertTrue(any("duplicate claim id" in p for p in probs))
        self.assertTrue(any("not a declared entity" in p for p in probs))


if __name__ == "__main__":
    unittest.main()

    def test_entity_ids_unique_per_name(self):
        # Same type + name under two ids splits the graph and breaks mv_ask name lookups (Batch 6c lesson).
        self.assertEqual(P.entity_alias_collisions(), [])

    def test_entity_alias_collision_detected(self):
        with tempfile.TemporaryDirectory() as d:
            a, b = Path(d) / "a.spec.json", Path(d) / "b.spec.json"
            ent = lambda i: {"id": i, "type": "Character", "name": "Kaito Shizuki"}
            a.write_text(json.dumps({"pack_id": "a", "entities": [ent("kaito")]}), encoding="utf-8")
            b.write_text(json.dumps({"pack_id": "b", "entities": [ent("kaito_shizuki")]}), encoding="utf-8")
            self.assertEqual(len(P.entity_alias_collisions([a, b])), 1)
            b.write_text(json.dumps({"pack_id": "b", "entities": [ent("kaito")]}), encoding="utf-8")
            self.assertEqual(P.entity_alias_collisions([a, b]), [])
