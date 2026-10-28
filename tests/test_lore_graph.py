import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from build_lore_graph import build, search


class LoreGraphTests(unittest.TestCase):
    def test_evidence_is_not_canon_proof(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "entries.json"
            path.write_text(json.dumps({"items": [
                {"page": "Lore.md", "anchor": "urza", "name": "Urza", "kind": "character", "links": {"cards": ["cards/U/urz.md#urza"]}, "flags": {"retcon": 1}, "citations": 2},
            ]}), encoding="utf-8")
            graph = build(path)
            self.assertEqual(graph["stats"]["card_references"], 1)
            self.assertEqual(graph["edges"][0]["evidence"]["tier"], "contextual_pointer")
            self.assertEqual(graph["nodes"][0]["flags"], {"retcon": 1})
            self.assertEqual(search(graph, "Urza", 10)[0]["connection_count"], 1)

    def test_duplicate_entry_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "entries.json"
            row = {"page": "Lore.md", "anchor": "same", "name": "A", "kind": "arc"}
            path.write_text(json.dumps({"items": [row, row]}), encoding="utf-8")
            with self.assertRaises(ValueError):
                build(path)


if __name__ == "__main__":
    unittest.main()
