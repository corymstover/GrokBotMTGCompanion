import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_story_art_captions as S  # noqa: E402
import build_multiverse_graph as G  # noqa: E402


class StoryArtCaptionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.atlas = json.loads(S.OUT.read_text(encoding="utf-8"))
        cls.graph = json.loads((ROOT / "data/multiverse_graph/multiverse_graph.json").read_text(encoding="utf-8"))

    def test_self_hash_and_check(self):
        self.assertTrue(S.self_hash_ok(self.atlas))
        self.assertEqual(S.main(["--check"]), 0)

    def test_only_official_pages_and_counts_consistent(self):
        for p in self.atlas["pages"]:
            self.assertRegex(p["url"], S.OFFICIAL)
            self.assertTrue(p["captions"])
        self.assertEqual(self.atlas["captions"], sum(len(p["captions"]) for p in self.atlas["pages"]))
        self.assertEqual(self.atlas["pages_scanned_missing"], 0)

    def test_navigation_tier_not_canon(self):
        self.assertEqual(self.atlas["tier"], "ART_CAPTIONED_IN_OFFICIAL_STORY")
        self.assertIn("not a claim", self.atlas["meaning"])
        for e in self.graph["edges"]:
            if e["relation"] == "art_captioned_in_story":
                self.assertTrue(e["from"].startswith("source:"))
                self.assertTrue(e["to"].startswith("card:"))
                self.assertNotIn("claim", e)

    def test_known_caption_present(self):
        rtd1 = next(p for p in self.atlas["pages"] if p["url"].endswith("return-dominaria-episode-1-2018-03-21"))
        self.assertIn("Dark Dabbling", [c["card"] for c in rtd1["captions"]])

    def test_scan_rejects_typo_artist_and_unknown_name(self):
        names = {"Crux of Fate": {"name": "Crux of Fate", "oracle_id": "x", "artists": {"Michael Komarck"}}}
        rej = {}
        self.assertEqual(S.scan("Crux of Fate | Art by Michael Kormarck text", names, 3, rej), [])
        self.assertEqual(S.scan("Not A Card | Art by Michael Komarck text", names, 3, rej), [])
        self.assertEqual(rej, {"artist_not_credited_in_snapshot": 1, "no_exact_card_name": 1})
        hit = S.scan("He fell. Crux of Fate | Art by Michael Komarck text", names, 3)
        self.assertEqual([h["card"] for h in hit], ["Crux of Fate"])

    def test_diacritics_fold_for_artist_only(self):
        names = {"The Chain Veil": {"name": "The Chain Veil", "oracle_id": "y", "artists": {"Volkan Ba\u01f5a"}}}
        self.assertEqual(len(S.scan("The Chain Veil | Art by Volkan Baga", names, 3)), 1)

    def test_graph_ingests_only_registered_sources(self):
        m = json.loads(G.MANIFEST.read_text(encoding="utf-8"))
        self.assertIn("data/story_atlas/story_art_captions_2026-10-30.json", m["story_caption_packs"])
        built = G.build()
        self.assertEqual(built["problems"], [])
        srcs = {n["id"] for n in built["nodes"] if n["type"] == "Source"}
        cap = [e for e in built["edges"] if e["relation"] == "art_captioned_in_story"]
        self.assertTrue(cap)
        self.assertTrue(all(e["from"] in srcs for e in cap))

    def test_unresolved_snapshot_card_identity_is_not_promoted_by_art_caption(self):
        # The official page genuinely credits this art, but the historical
        # caption matching snapshot did not provide an Oracle UUID. The atlas
        # is retained and the graph must not silently invent a card identity.
        unknown = [(p["url"], c) for p in self.atlas["pages"]
                   for c in p["captions"] if not c.get("oracle_id")]
        self.assertEqual(len(unknown), 1)
        self.assertEqual(unknown[0][1]["caption_name"], "Anointed Procession")
        built = G.build()
        info = built["inputs"]["story_caption_packs"][0]
        self.assertEqual(info["unresolved_card_identities"], [{
            "url": unknown[0][0], "card": unknown[0][1]["card"],
            "caption_name": "Anointed Procession", "reason": "NO_SNAPSHOT_ORACLE_ID"}])
        self.assertFalse(any(n["type"] == "Card" and not n.get("oracle_id") for n in built["nodes"]))
        self.assertNotIn("card:anointed_procession_anointed_procession", {n["id"] for n in built["nodes"]})


if __name__ == "__main__":
    unittest.main()
