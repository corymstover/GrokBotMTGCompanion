import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "data" / "multiverse_audits" / "entity_structure_audit_2026-10-30.json"
sys.path.insert(0, str(ROOT / "scripts"))
import audit_entity_structures as aes  # noqa: E402


class EntityStructureAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d = json.loads(AUDIT.read_text(encoding="utf-8"))

    def test_committed_audit_is_current(self):
        r = subprocess.run([sys.executable, str(ROOT / "scripts" / "audit_entity_structures.py"), "--check"],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_graph_integrity_hard_invariants(self):
        i = self.d["graph_integrity"]
        self.assertEqual(i["duplicate_ids"], [])
        self.assertEqual(i["dangling_edges"], 0)
        self.assertEqual(i["prefix_type_mismatches"], [])
        self.assertEqual(i["builder_problems"], [])
        self.assertEqual(i["cards_without_oracle_id"], [])

    def test_no_pack_type_conflicts(self):
        self.assertEqual(self.d["claim_pack_consistency"]["type_conflicts"], [])

    def test_review_items_are_never_merged(self):
        self.assertIn("no merges", self.d["status"])
        for r in self.d["duplicate_candidates"]["character_alias_candidates"]:
            self.assertEqual(r["status"], "REVIEW_ONLY_NOT_MERGED")

    def test_crosswalk_covers_every_legacy_entity_node(self):
        lg = json.loads((ROOT / "data" / "lore_graph.json").read_text(encoding="utf-8"))
        n = sum(1 for x in lg["nodes"] if x["kind"] in aes.LEGACY_KIND_TO_TYPES)
        self.assertEqual(len(self.d["legacy_crosswalk"]["rows"]), n)
        self.assertEqual(sum(self.d["legacy_crosswalk"]["by_status"].values()), n)

    def test_pack_declared_variants_are_bridged_without_guessing_first_names(self):
        from build_multiverse_graph import Graph, bridge_curated
        graph = json.loads((ROOT / "data/multiverse_graph/multiverse_graph.json").read_text(encoding="utf-8"))
        edges = [e for e in graph["edges"] if e["relation"] == "see_also_curated_entry"
                 and e.get("name_match_basis") == "unique_pack_declared_name_variant"]
        self.assertEqual(len(edges), 10)
        pairs = {(e["from"], e["to"]) for e in edges}
        self.assertIn(("character:ajani", "curated:Characters Index.md#ajani-goldmane"), pairs)
        self.assertIn(("character:the_wanderer", "curated:Characters Index.md#the-wanderer"), pairs)
        self.assertEqual(self.d["legacy_crosswalk"]["by_status"].get("CANDIDATE_BY_FIRST_WORD"), 15)
        for row in self.d["legacy_crosswalk"]["rows"]:
            if row["status"] == "CANDIDATE_BY_FIRST_WORD":
                self.assertFalse(row["bridged_in_graph"])

        # A second typed entity with the same full name makes the proposed
        # pack-declared variant ambiguous; no navigation bridge may be made.
        g = Graph()
        g.add_node("character:ajani", "Character", "Ajani", "fixture")
        g.add_node("character:ajani", "Character", "Ajani Goldmane", "fixture")
        g.add_node("character:other", "Character", "Ajani Goldmane", "fixture")
        bridge_curated(g, "data/lore_graph.json")
        self.assertFalse(any(e["from"] == "character:ajani" and
                             e["to"] == "curated:Characters Index.md#ajani-goldmane" for e in g.edges))

    def test_norm(self):
        self.assertEqual(aes.norm("The Chain Veil"), "chain veil")
        self.assertEqual(aes.norm("Zendikar’s vampires"), aes.norm("Zendikars vampires"))

    def test_inventory_lists_both_graphs(self):
        roles = {r["role"] for r in self.d["inventory"]}
        self.assertIn("CANONICAL_RELATIONSHIP_GRAPH", roles)
        self.assertIn("LEGACY_CURATED_NAVIGATION_GRAPH", roles)
        self.assertTrue(all(r["exists"] for r in self.d["inventory"] if "*" not in r["path"]))


if __name__ == "__main__":
    unittest.main()
