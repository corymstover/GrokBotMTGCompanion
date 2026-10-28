import json
import sys
import tempfile
import types
import unittest
from pathlib import Path

from lore_evidence_work import printing_matches, lore_sources, graph_context, lookup


class LoreEvidenceTests(unittest.TestCase):
    def _archive(self, where):
        p = Path(where)
        (p / "manifest.json").write_text(json.dumps({"source": "fixture", "coverage": "test",
            "sets": {"atq": {"files": ["a-000.jsonl"]}, "bro": {"files": ["b-000.jsonl"]}},
            "shards": {"a-000.jsonl": {}, "b-000.jsonl": {}}}), encoding="utf-8")
        (p / "a-000.jsonl").write_text(json.dumps({"id": "p1", "o": "o1", "n": "Antiquity",
            "s": "atq", "c": "3", "l": "en", "p": 1, "url": "https://scryfall.com/card/atq/3",
            "faces": [{"n": "Antiquity", "f": "Urza's creation inspired the artificers."}]}) + "\n", encoding="utf-8")
        (p / "b-000.jsonl").write_text(json.dumps({"id": "p2", "n": "Saga",
            "s": "bro", "c": "12", "l": "en", "p": 1,
            "faces": [{"n": "Saga", "chapters": "I — Remember Urza"}]}) + "\n", encoding="utf-8")

    def test_literal_evidence_set_and_saga_distinction(self):
        with tempfile.TemporaryDirectory() as tmp:
            self._archive(tmp)
            result = printing_matches("Urza", Path(tmp))
            self.assertEqual(result["total_matches"], 2)
            self.assertEqual(result["matches_by_field"], {"printed_flavor": 1, "saga_chapter_oracle": 1})
            only = printing_matches("Urza", Path(tmp), ["atq"])
            self.assertEqual(only["total_matches"], 1)
            self.assertEqual(only["printings"][0]["evidence"], "literal_printing_text_match")
            self.assertEqual(printing_matches("ur", Path(tmp))["total_matches"], 0)

    def test_unknown_set_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            self._archive(tmp)
            with self.assertRaises(ValueError):
                printing_matches("Urza", Path(tmp), ["xyz"])

    def test_official_urls_not_promoted_to_card_proof(self):
        fake = types.ModuleType("lore_lib")
        fake.official_urls = lambda text: ["https://magic.wizards.com/en/story/urza"]
        fake.flags = lambda text: {"retcon": 1}
        original = sys.modules.get("lore_lib")
        sys.modules["lore_lib"] = fake
        try:
            result = lore_sources("Urza", [{"name": "Urza", "page": "Characters Index.md", "anchor": "urza",
                "kind": "character", "text": "Urza ⚠️"}])
            self.assertEqual(result[0]["official_citations"], ["https://magic.wizards.com/en/story/urza"])
            self.assertEqual(result[0]["interpretation"], "citations document the entry; not necessarily each linked card")
            with tempfile.TemporaryDirectory() as tmp:
                self._archive(tmp)
                linked = lookup("Urza", Path(tmp), [{"name": "Urza", "page": "Characters Index.md",
                    "anchor": "urza", "kind": "character", "text": "Urza"}], ["atq"], 5,
                    Path(tmp) / "missing_graph.json")
                self.assertEqual(linked["printing_lore_edges"][0]["to"], "Characters Index.md#urza")
                self.assertEqual(linked["printing_lore_edges"][0]["evidence"]["tier"], "literal_printing_text_match")
        finally:
            if original is None:
                del sys.modules["lore_lib"]
            else:
                sys.modules["lore_lib"] = original

    def test_graph_context_preserves_uncertainty(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "graph.json"
            p.write_text(json.dumps({"nodes": [
                {"id": "lore#urza", "name": "Urza"},
                {"id": "cards#urza", "name": "Urza's Tome"}],
                "edges": [{"from": "lore#urza", "to": "cards#urza",
                    "relation": "card_page_reference", "evidence": {"tier": "contextual_pointer"}}]}))
            result = graph_context("Urza", p)
            self.assertEqual(result[0]["connections"][0]["evidence"], "contextual_pointer")


if __name__ == "__main__":
    unittest.main()
