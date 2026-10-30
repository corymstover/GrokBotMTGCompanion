"""Protect source-preserving graph cleanups from the October 30 overnight audit."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class GraphIntegrityCorrections(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.g = json.loads((ROOT / "data/multiverse_graph/multiverse_graph.json").read_text())
        cls.audit = json.loads((ROOT / "data/multiverse_audits/entity_structure_audit_2026-10-30.json").read_text())

    def test_c023_both_brothers_are_subjects_not_a_literal(self):
        edges = [e for e in self.g["edges"] if e.get("claim") == "C023"]
        self.assertEqual({e["from"] for e in edges}, {"character:urza", "character:mishra"})
        self.assertEqual({e["to"] for e in edges}, {"concept:powerstones"})
        self.assertNotIn("literal:urza_mishra", {n["id"] for n in self.g["nodes"]})

    def test_legacy_artifact_bridges_are_exact_normalized_matches(self):
        misses = [r for r in self.audit["legacy_crosswalk"]["rows"]
                  if r["status"] == "NORMALISED_MATCH_NOT_BRIDGED"]
        self.assertEqual(misses, [])
        edges = [e for e in self.g["edges"] if e["relation"] == "see_also_curated_entry"
                 and e.get("name_match_basis") == "unique_normalized_item_name"]
        self.assertEqual(len(edges), 5)
        self.assertTrue(all(e["from"].startswith("artifact:") for e in edges))

    def test_no_unresolved_compound_subjects_or_builder_problems(self):
        self.assertEqual(self.g["problems"], [])
        self.assertFalse(any(";" in r["token"]
                             for r in self.audit["claim_pack_consistency"]["claims_with_undeclared_subject"]))


if __name__ == "__main__":
    unittest.main()
