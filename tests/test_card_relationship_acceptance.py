"""Source-grade and historical time/caption evidence must fail closed."""
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_card_relationship_acceptance as A
from query_multiverse_graph import MG


class CardRelationshipAcceptanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graph = json.loads(A.GRAPH.read_text(encoding="utf-8"))

    def corrupt(self, modify, error):
        g = json.loads(json.dumps(self.graph))
        modify(g)
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "graph.json"
            path.write_text(json.dumps(g), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, error):
                A.build(path)

    def test_replays_claimed_bounded_evidence_only(self):
        r = A.build()
        c = r["counts"]
        self.assertEqual(c["official_image_file_labels_matched"], 570)
        self.assertEqual(c["distinct_exact_printings"], 560)
        self.assertEqual(c["unresolved_image_labels"], 7)
        self.assertEqual(c["direct_event_scene_caption_links"], 1)
        self.assertEqual(c["visually_reviewed_exact_art"], 6)
        self.assertEqual(c["dated_relationship_edges"], 36)
        self.assertGreater(c["undated_relationship_edges"], 1000)
        self.assertIn("UNRESOLVED", r["criteria"]["K064_card_story_art_flavor_links"])

    def test_query_does_not_conflate_a_relative_phrase_with_a_calendar_date(self):
        mg = MG()
        rows = mg.neighbors("Nicol Bolas", include_temporal=True)
        dated = next(r for r in rows if r["claim"] == "AKH017")
        self.assertEqual(dated["in_universe_date"]["value"], "Several decades ago")
        self.assertEqual(dated["time_qualification"], "QUOTED_SOURCE_LOCAL_SPAN")
        self.assertTrue(dated["source_urls"])
        self.assertTrue(any(r["claim"] and r["time_qualification"] == "SOURCE_NOT_DATED" for r in rows))
        self.assertTrue(any(r["time_qualification"] == "NOT_A_CANON_CHRONOLOGY_EDGE"
                            for r in mg.card("Crux of Fate", include_temporal=True)["relationships"]))

    def test_default_query_remains_byte_compatible_with_pinned_foundation_packet(self):
        import build_foundation_acceptance_packet as F
        prior = json.loads((ROOT / "data/release/foundation_acceptance_packet_2026-10-30.json").read_text())
        self.assertEqual(F.build(), prior)
        self.assertNotIn("time_qualification", MG().neighbors("Nicol Bolas")[0])

    def test_invented_date_quote_is_rejected(self):
        self.corrupt(lambda g: next(e for e in g["edges"] if e.get("in_universe_date"))
                     ["in_universe_date"].update(quote="exactly 12,345 AR"), "date phrase not verbatim")

    def test_unsupported_canon_upgrade_is_rejected(self):
        self.corrupt(lambda g: next(e for e in g["edges"] if e.get("claim") == "A003")
                     .update(grade="CANON_CONFIRMED"), "inflated claim grade")

    def test_art_label_cannot_be_promoted_to_narrative_scene(self):
        self.corrupt(lambda g: next(e for e in g["edges"] if e["relation"] == "art_file_used_on_official_page")
                     .update(limitation="This is the exact canon battlefield scene"),
                     "image label cannot certify")

    def test_unsupported_first_party_claim_source_rejected(self):
        def corrupt(g):
            source = next(e["sources"][0] for e in g["edges"] if e.get("claim"))
            next(n for n in g["nodes"] if n["id"] == "source:" + source).update(url="https://example.invalid/story")
        self.corrupt(corrupt, "nonofficial or unrelated claim citation")

    def test_check_rejects_stale_saved_report(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "report.json"
            path.write_text("{}\n", encoding="utf-8")
            with patch.object(A, "OUT", path):
                with self.assertRaisesRegex(ValueError, "stale"):
                    A.main(["--check"])


if __name__ == "__main__":
    unittest.main()
