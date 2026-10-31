"""Source-graded direct plane history; no inferred total chronology or current state."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_p5_thin_plane_history as A  # noqa: E402
import mv_ask  # noqa: E402


class ThinPlaneHistoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pack = json.loads(A.PACK.read_text(encoding="utf-8"))

    def test_eleven_official_source_claims_and_direct_plane_coverage(self):
        result = A.audit()
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(result["claims"], 11)
        self.assertEqual(result["remaining_thin_planes"], 12)
        self.assertFalse(result["owner_approved"])

    def test_quotes_are_required_for_each_primary_page(self):
        pages = {sid: "" for sid in self.pack["source_register"]}
        for claim in self.pack["claims"]:
            first_source = claim["source_ids"][0]
            pages[first_source] += "<p>" + claim["source_excerpt"] + "</p>"
        self.assertTrue(A.audit(pages)["live_quote_checked"])
        pages["tph_eldraine_2019"] = "<p>No source text.</p>"
        with self.assertRaisesRegex(ValueError, "Source excerpt absent"):
            A.audit(pages)

    def test_all_four_plane_histories_are_cited_and_explicitly_incomplete(self):
        expected = {"Argentum": 5, "Eldraine": 5, "Ikoria": 6, "New Capenna": 5}
        for name, direct in expected.items():
            with self.subTest(plane=name):
                result = mv_ask.ask(f"What is the history of {name}?")
                self.assertEqual(result["route"], "ask->plane_history")
                self.assertEqual(result["confidence"], "QUALIFIED")
                self.assertEqual(result["result"]["direct_claims"], direct)
                self.assertFalse(result["result"]["complete_history"])
                self.assertFalse(result["result"]["verified_total_chronology"])
                self.assertIn("NO_VERIFIED_TOTAL_CHRONOLOGY", result["flags"])
                self.assertTrue(all(url.startswith("https://magic.wizards.com/")
                                    for url in result["sources"]))

    def test_unknown_invader_identity_and_historical_plane_naming_are_retained(self):
        capenna = mv_ask.ask("What is the history of New Capenna?")
        invasion = next(c for c in capenna["result"]["claims"] if c["claim_id"] == "TPH007")
        self.assertIn("NOT identify it as Phyrexia", invasion["limitation"])
        argentum = mv_ask.ask("What is the history of Argentum?")
        renaming = next(c for c in argentum["result"]["claims"] if c["claim_id"] == "TPH011")
        self.assertIn("not its current canonical name", renaming["limitation"])


if __name__ == "__main__":
    unittest.main()
