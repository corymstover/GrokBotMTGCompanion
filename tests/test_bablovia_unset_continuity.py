"""The Unstable classroom story cannot be reclassified as ordinary canon."""
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


class BabloviaContinuityGate(unittest.TestCase):
    def test_legacy_classroom_claim_is_alt_continuity_at_every_claim_layer(self):
        spec = read("data/lore_research/claim_specs/pack_p5_untagged_side_stories_2015_2026.spec.json")
        pack = read("data/lore_research/pack_p5_untagged_side_stories_2015_2026_2026-10-30.json")
        graph = read("data/multiverse_graph/multiverse_graph.json")
        claims = [next(c for c in x["claims"] if c["id"] == "SSX020") for x in (spec, pack)]
        node = next(n for n in graph["nodes"] if n["id"] == "claim:SSX020")
        for x in (*claims, node):
            self.assertEqual(x["grade"], "ALTERNATE_CONTINUITY")
            self.assertIn("Unstable", x["limitation"])
            self.assertIn("not ordinary black-border Magic canon", x["limitation"])
        self.assertEqual(pack["status"], "PRELIMINARY_RESEARCH (not owner approved, not certified)")
        self.assertEqual(pack["claims"][19]["id"], "SSX020")
        self.assertEqual(pack["claims"][19]["source_ids"], ["wc"])
        self.assertTrue(pack["source_register"]["wc"]["url"].startswith("https://magic.wizards.com/"))
        relations = [e for e in graph["edges"] if e.get("claim") == "SSX020"
                     and e.get("relation") not in {"asserts", "cited_by"}]
        self.assertTrue(relations)
        self.assertTrue(all(e["grade"] == "ALTERNATE_CONTINUITY" for e in relations))

    def test_bablovia_plane_history_is_isolated(self):
        plane_pack = read("data/lore_research/pack_p5_last_four_thin_planes_2026-10-31.json")
        dossiers = read("data/lore_research/plane_history_dossiers_2026-10-30.json")
        bablovia = next(p for p in dossiers["planes"] if p["plane"] == "Bablovia")
        self.assertEqual(bablovia["distinct_claims"], 5)
        self.assertEqual({x["claim_id"] for x in bablovia["facts"]},
                         {"SSX020", "LFP001", "LFP002", "LFP003", "LFP004"})
        self.assertTrue(all(x["grade"] == "ALTERNATE_CONTINUITY" for x in bablovia["facts"]))
        self.assertIn("Unstable", plane_pack["source_register"]["lf_unset_boundary"]["title"])


if __name__ == "__main__":
    unittest.main()
