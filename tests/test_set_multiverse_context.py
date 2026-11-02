"""Set context is a source-local navigation tool, never synthetic set canon."""
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_set_multiverse_context as S


class SetContextTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = S.build()

    def corrupt(self, path, mutate, message):
        source = json.loads(path.read_text(encoding="utf-8"))
        mutate(source)
        with tempfile.TemporaryDirectory() as folder:
            bad = Path(folder) / path.name
            bad.write_text(json.dumps(source), encoding="utf-8")
            kw = ({S.BRIDGE: "bridge_path", S.CATALOG: "catalog_path", S.GRAPH: "graph_path",
                   S.SOURCES: "sources_path"})[path]
            with self.assertRaisesRegex(ValueError, message):
                S.build(**{kw: bad})

    def test_first_party_bounded_counts(self):
        c = self.data["counts"]
        self.assertEqual(c["all_scryfall_codes_queryable"], 1062)
        self.assertEqual(c["official_story_series_sets"], 12)
        self.assertEqual(c["official_story_sample_pages"], 35)
        self.assertEqual(c["typed_claim_entity_associations"], {"Character": 117, "Faction": 11, "Plane": 8})
        self.assertEqual(c["sets_with_verified_mechanics_feature"], 3)
        self.assertEqual(c["official_related_commander_product_links"], 1)

    def test_named_set_story_and_mechanic_are_separate_evidence(self):
        tdm = S.query("TDM", self.data)
        self.assertFalse(tdm["inferred_canon"])
        self.assertEqual(tdm["evidence_status"], "SOURCE_GRADED_PARTIAL_CONTEXT")
        info = tdm["context"]
        self.assertEqual(info["mechanics_official_feature"]["source_title"], "Tarkir: Dragonstorm Mechanics")
        self.assertIn("Harmonize", info["mechanics_official_feature"]["mechanic_labels"])
        self.assertEqual(info["related_commander_product"]["commander_set_code"], "tdc")
        self.assertTrue(any(a["entity_id"] == "character:narset" and a["claim_id"] == "claim:TD010"
                            and a["claim_grade"] == "CANON_CONFIRMED"
                            and a["association_not_set_card_canon"]
                            for a in info["source_claim_entity_associations"]))

    def test_unresearched_sets_remain_unknown_even_if_parent_or_commander(self):
        tdc = S.query("tdc", self.data)
        self.assertEqual(tdc["parent_set_code"], "tdm")
        self.assertEqual(tdc["category"], "commander")
        self.assertEqual(tdc["evidence_status"], "NO_VERIFIED_STORY_CONTEXT_IN_THIS_SNAPSHOT")
        self.assertIsNone(tdc["context"])
        self.assertIsNone(S.query("lea", self.data)["context"])
        with self.assertRaises(KeyError):
            S.query("not_a_set", self.data)

    def test_official_mechanic_article_cannot_be_substituted(self):
        self.corrupt(S.SOURCES, lambda s: s["mechanics"][0].update(source_url="https://example.invalid/feature"),
                     "unverified or inflated mechanics")

    def test_mechanic_claim_cannot_be_inflated(self):
        self.corrupt(S.SOURCES, lambda s: s["mechanics"][0]["mechanic_labels"].append("Unproved"),
                     "unverified or inflated mechanics")

    def test_commander_cross_set_parent_must_be_real(self):
        self.corrupt(S.CATALOG, lambda c: c["sets"]["tdc"].update(parent_set_code="blb"),
                     "unverified Commander source")

    def test_unregistered_story_page_cannot_add_lore(self):
        self.corrupt(S.BRIDGE, lambda b: b["wizards_story_series_set_links"]["tdm"]
                     ["sample_first_party_story_sources"][0].update(url="https://magic.wizards.com/en/news/magic-story/nonexistent"),
                     "missing, duplicated or nonofficial story")

    def test_nonofficial_source_class_rejected(self):
        self.corrupt(S.GRAPH, lambda g: next(n for n in g["nodes"] if n["id"] == "source:tdm_ep1")
                     .update(source_class="NON_WIZARDS_LABELLED"), "not first-party graded")

    def test_stale_report_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "stale.json"
            path.write_text("{}\n", encoding="utf-8")
            with patch.object(S, "OUT", path):
                with self.assertRaisesRegex(ValueError, "stale"):
                    S.main(["--check"])


if __name__ == "__main__":
    unittest.main()
