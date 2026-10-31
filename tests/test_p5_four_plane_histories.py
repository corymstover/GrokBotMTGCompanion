"""v2.66's four source-quoted histories within the current foundation packet."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_p5_four_plane_histories as A  # noqa: E402
import mv_ask  # noqa: E402
import build_foundation_acceptance_packet as P  # noqa: E402


class FourPlaneHistoryTests(unittest.TestCase):
    def test_direct_claims_sources_and_excluded_completeness(self):
        status = A.audit()
        self.assertEqual((status["claims"], status["source_pages"], status["remaining_thin_planes"]), (12, 5, 4))
        self.assertFalse(status["owner_approved"])
        self.assertFalse(status["complete_histories"])

    def test_source_quotes_missing_fail_closed(self):
        pack = json.loads(A.PACK.read_text(encoding="utf-8"))
        pages = {sid: "" for sid in pack["source_register"]}
        for claim in pack["claims"]:
            for sid in claim["source_ids"]:
                pages[sid] += "<p>" + claim["source_excerpt"] + "</p>"
        self.assertTrue(A.audit(pages)["live_quote_checked"])
        pages["fph_origins_2015"] = "<p>Missing source.</p>"
        with self.assertRaisesRegex(ValueError, "Source excerpt absent"):
            A.audit(pages)

    def test_history_q_and_a_remains_qualified(self):
        for plane in A.EXPECTED:
            with self.subTest(plane=plane):
                reply = mv_ask.ask(f"What is the history of {plane}?")
                self.assertEqual(reply["route"], "ask->plane_history")
                self.assertEqual(reply["confidence"], "QUALIFIED")
                self.assertEqual(reply["result"]["direct_claims"], 5)
                self.assertFalse(reply["result"]["complete_history"])
                self.assertFalse(reply["result"]["verified_total_chronology"])
                self.assertIn("NO_VERIFIED_TOTAL_CHRONOLOGY", reply["flags"])
                self.assertTrue(reply["sources"])
                self.assertTrue(all(url.startswith("https://magic.wizards.com/") for url in reply["sources"]))

    def test_foundation_review_has_unique_questions_and_no_deck_release(self):
        cases = P.QA_CASES
        self.assertEqual(len(cases), 34)
        self.assertEqual(len({c[0] for c in cases}), 34)
        packet = P.build()
        self.assertEqual(len(packet["representative_questions"]), 34)
        self.assertEqual(packet["coverage"]["thin_plane_dossiers"], 4)
        self.assertTrue(packet["phase6_deckbuilding_deferred"])
        self.assertFalse(packet["release_certified"])


if __name__ == "__main__":
    unittest.main()
