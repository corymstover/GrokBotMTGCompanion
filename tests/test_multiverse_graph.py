"""Regression tests for the Phase 3 cited Multiverse claim graph."""
import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_multiverse_graph as B  # noqa: E402
from query_multiverse_graph import MG  # noqa: E402


class GraphBuildTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graph = B.build()
        cls.mg = MG()

    def test_committed_graph_is_current_and_clean(self):
        r = subprocess.run([sys.executable, str(ROOT / "scripts/build_multiverse_graph.py"), "--check"],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(self.graph["problems"], [])

    def test_every_pack_claim_present_with_valid_status_and_source(self):
        claims = [n for n in self.graph["nodes"] if n["type"] == "Claim"]
        expected = sum(len(B.load(r).get("claims", [])) for r in json.loads(B.MANIFEST.read_text())["claim_packs"])
        self.assertEqual(len(claims), expected)
        for c in claims:
            self.assertIn(c["grade"], B.CANON_STATUSES)
        cited = {e["to"] for e in self.graph["edges"] if e["relation"] == "cited_by"}
        self.assertEqual({c["id"] for c in claims} - cited, set())

    def test_disputed_and_open_claims_preserved(self):
        by_status = {}
        for n in self.graph["nodes"]:
            if n["type"] == "Claim":
                by_status.setdefault(n["grade"], set()).add(n["id"])
        self.assertEqual(by_status.get("CANON_DISPUTED"), {"claim:A003", "claim:A004", "claim:B012", "claim:C012", "claim:RTD006", "claim:RTD021", "claim:RTD033"})
        self.assertEqual(by_status.get("OPEN_QUESTION"), {"claim:A011", "claim:C010"})
        self.assertEqual(by_status.get("ALTERNATE_CONTINUITY"), {"claim:A012"})

    def test_no_broken_or_duplicate_edges(self):
        ids = {n["id"] for n in self.graph["nodes"]}
        for e in self.graph["edges"]:
            self.assertIn(e["from"], ids)
            self.assertIn(e["to"], ids)

    def test_relationship_edges_cite_only_wizards_sources(self):
        for e in self.graph["edges"]:
            if "claim" in e:
                for s in e["sources"]:
                    self.assertEqual(self.mg.nodes[f"source:{s}"]["source_class"], "WIZARDS_OFFICIAL", e)

    def test_cross_pack_entity_resolution(self):
        # A003 (Pack A) names survivors that Pack A2 defines as entities. They must resolve to those
        # entities and must not stay as free-text literals.
        survivors = {e["to"] for e in self.graph["edges"] if e.get("claim") == "A003"}
        self.assertIn("character:chromium_rhuell", survivors)
        self.assertNotIn("literal:chromium_rhuell", self.mg.nodes)

    def test_deck_edges_are_navigation_not_canon(self):
        for e in self.graph["edges"]:
            if e["relation"] in {"proposed_in", "see_also_curated_entry"}:
                self.assertNotIn("grade", e)
        deck = [n for n in self.graph["nodes"] if n["type"] == "DeckProposal"]
        self.assertTrue(deck and all("UNAPPROVED" in d["status"].upper() for d in deck))


class QueryTests(unittest.TestCase):
    mg = MG()

    def test_bidirectional_lookup(self):
        out = self.mg.neighbors("ugin")
        self.assertTrue(any(r["direction"] == "out" and r["relation"] == "jailed" for r in out))
        bolas_in = self.mg.neighbors("Nicol Bolas")
        self.assertTrue(any(r["direction"] == "in" and r["claim"] == "A007" for r in bolas_in))

    def test_character_preferred_over_same_name_card(self):
        self.assertEqual(self.mg.find("Nicol Bolas"), "character:nicol_bolas")
        self.assertEqual(self.mg.find("Nicol Bolas", prefer="Card"), "card:nicol_bolas")

    def test_path_uses_cited_claims(self):
        hops = self.mg.path("piru", "ugin")
        self.assertTrue(hops)
        self.assertTrue(all(h["claim"] and h["source_urls"] for h in hops))

    def test_card_story_art(self):
        res = self.mg.card("Crux of Fate")
        self.assertIn("e1d45374-a41b-4b3f-a7c8-3eb5ca767cf6", res["card"]["exact_story_art_printings"])

    def test_status_query(self):
        self.assertEqual([r["claim"] for r in self.mg.status("OPEN_QUESTION")], ["claim:A011", "claim:C010"])


    # --- Pack B (Thran / Yawgmoth / Brothers' War) ---
    def test_pack_b_brothers_and_sylex(self):
        out = self.mg.neighbors("Urza")
        rels = {(r["relation"], r.get("claim")) for r in out}
        self.assertIn(("sibling_of", "B001"), rels)
        self.assertIn(("activated", "B007"), rels)
        self.assertIn(("vendetta_against", "B013"), rels)

    def test_pack_b_path_mishra_to_yawgmoth(self):
        hops = self.mg.path("mishra", "yawgmoth")
        self.assertTrue(hops)
        self.assertTrue(all(h["claim"] and h["source_urls"] for h in hops))

    def test_pack_b_sylex_origin_stays_disputed(self):
        edges = [e for e in self.mg.g["edges"] if e.get("claim") == "B012"]
        self.assertTrue(edges)
        self.assertTrue(all(e["grade"] == "CANON_DISPUTED" for e in edges))

    def test_pack_b_bridges_to_curated_wiki(self):
        bridged = {e["from"] for e in self.mg.g["edges"] if e["relation"] == "see_also_curated_entry"}
        for nid in ("character:urza", "character:mishra", "character:yawgmoth", "artifact:golgothian_sylex"):
            self.assertIn(nid, bridged)

    def test_pack_c_yawgmoth_defeat_accounts_preserved(self):
        edges = [e for e in self.mg.g["edges"] if e.get("claim") == "C012"]
        targets = {e["to"] for e in edges}
        for nid in ("character:karn", "character:gerrard", "character:urza"):
            self.assertIn(nid, targets)
        self.assertTrue(all(e["grade"] == "CANON_DISPUTED" for e in edges))

    def test_pack_c_old_phyrexia_creator_is_open(self):
        edges = [e for e in self.mg.g["edges"] if e.get("claim") == "C010"]
        self.assertTrue(edges)
        self.assertTrue(all(e["grade"] == "OPEN_QUESTION" for e in edges))

    def test_pack_c_path_urza_to_mirrodin(self):
        hops = self.mg.path("urza", "mirrodin")
        self.assertTrue(hops)
        self.assertTrue(all(h["claim"] and h["source_urls"] for h in hops))

    def test_pack_c_sources_all_official(self):
        srcs = [n for n in self.mg.g["nodes"] if n["id"].startswith("source:c_")]
        self.assertEqual(len(srcs), 6)
        self.assertTrue(all(n.get("url", "").startswith("https://magic.wizards.com/") for n in srcs))

class MutationTests(unittest.TestCase):
    """Corrupt a temporary copy of the inputs and confirm the validator catches it."""

    def _build_with(self, mutate):
        man = json.loads(B.MANIFEST.read_text())
        with tempfile.TemporaryDirectory() as td:
            td = Path(td)
            pack = copy.deepcopy(B.load(man["claim_packs"][0]))
            mutate(pack)
            p = td / "pack.json"
            p.write_text(json.dumps(pack))
            man2 = dict(man, claim_packs=[str(p)] + man["claim_packs"][1:])
            m = td / "manifest.json"
            m.write_text(json.dumps(man2))
            return B.build(m)["problems"]

    def test_missing_source_detected(self):
        probs = self._build_with(lambda p: p["claims"][0].update(source_ids=[]))
        self.assertTrue(any("no source_ids" in x for x in probs))

    def test_unregistered_source_detected(self):
        probs = self._build_with(lambda p: p["claims"][0].update(source_ids=["made_up_source"]))
        self.assertTrue(any("unregistered source" in x for x in probs))

    def test_unknown_grade_detected(self):
        probs = self._build_with(lambda p: p["claims"][0].update(grade="PROBABLY_TRUE"))
        self.assertTrue(any("unknown grade" in x for x in probs))

    def test_entity_type_conflict_detected(self):
        probs = self._build_with(lambda p: p["entities"].append({"id": "ugin", "type": "Plane", "name": "Ugin"}))
        self.assertTrue(any("inconsistently" in x or "conflict" in x for x in probs))


if __name__ == "__main__":
    unittest.main()
