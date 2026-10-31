"""Source-backed plane incidents, old/new era distinctions, and 34 QA IDs."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_p5_four_more_plane_histories as A  # noqa: E402
import build_foundation_acceptance_packet as P  # noqa: E402
import mv_ask  # noqa: E402


class FourMorePlaneHistoryTests(unittest.TestCase):
    def test_source_provenance_and_direct_incidence(self):
        result = A.audit()
        self.assertEqual((result["claims"], result["source_pages"], result["remaining_thin_planes"]), (12, 7, 4))
        self.assertFalse(result["complete_histories"])
        self.assertFalse(result["owner_approved"])

    def test_missing_source_quote_fails(self):
        pack = json.loads(A.PACK.read_text(encoding="utf-8"))
        pages = {sid: "" for sid in pack["source_register"]}
        for c in pack["claims"]:
            sid = c["source_ids"][0]
            pages[sid] += "<p>" + c["source_excerpt"] + "</p>"
        self.assertTrue(A.audit(pages)["live_quote_checked"])
        pages["fmp_kaldheim_2021"] = "<p>Quote removed.</p>"
        with self.assertRaisesRegex(ValueError, "Source excerpt absent"):
            A.audit(pages)

    def test_histories_are_qualified_and_nonexhaustive(self):
        for plane, count in A.EXPECTED.items():
            with self.subTest(plane=plane):
                r = mv_ask.ask(f"What is the history of {plane}?")
                self.assertEqual(r["route"], "ask->plane_history")
                self.assertEqual(r["confidence"], "QUALIFIED")
                self.assertEqual(r["result"]["direct_claims"], count)
                self.assertFalse(r["result"]["complete_history"])
                self.assertFalse(r["result"]["verified_total_chronology"])
                self.assertIn("NO_VERIFIED_TOTAL_CHRONOLOGY", r["flags"])

    def test_uncertainties_remain_visible(self):
        pack = json.loads(A.PACK.read_text(encoding="utf-8"))
        claims = {x["id"]: x for x in pack["claims"]}
        self.assertIn("unknown scheme", claims["FMP001"]["limitation"])
        self.assertIn("not the truth of every claim", claims["FMP003"]["limitation"])
        self.assertIn("not be treated as the current cycle", claims["FMP007"]["limitation"])
        self.assertIn("not evidence of a precise construction date", claims["FMP010"]["limitation"])

    def test_foundation_packet_has_34_distinct_questions_and_deck_hold(self):
        self.assertEqual(len(P.QA_CASES), 34)
        self.assertEqual(len({c[0] for c in P.QA_CASES}), 34)
        packet = P.build()
        self.assertEqual(len(packet["representative_questions"]), 34)
        self.assertEqual(packet["coverage"]["thin_plane_dossiers"], 4)
        self.assertTrue(packet["phase6_deckbuilding_deferred"])
        self.assertFalse(packet["owner_accepted"])
        self.assertFalse(packet["release_certified"])


if __name__ == "__main__":
    unittest.main()
