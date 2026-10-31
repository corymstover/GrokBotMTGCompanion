"""Source integrity, continuity isolation, graph/Q&A, and foundation hold for v2.68."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_p5_last_four_thin_planes as A  # noqa: E402
import build_foundation_acceptance_packet as P  # noqa: E402
import mv_ask  # noqa: E402


class LastFourPlaneTests(unittest.TestCase):
    def test_quoted_graph_incidence_and_continuity(self):
        result = A.audit()
        self.assertEqual((result["claims"], result["official_pages"], result["registered_thin_planes"]),
                         (13, 8, 0))
        self.assertTrue(result["bablovia_unset_isolated"])
        self.assertFalse(result["complete_histories"])

    def test_missing_quote_and_unset_boundary_are_detected(self):
        pack = json.loads(A.PACK.read_text(encoding="utf-8"))
        pages = {sid: "" for sid in pack["source_register"]}
        for c in pack["claims"]:
            pages[c["source_ids"][0]] += "<p>" + c["source_excerpt"] + "</p>"
        pages["lf_unset_boundary"] = "<p>" + pack["continuity_boundary_excerpt"] + "</p>"
        self.assertTrue(A.audit(pages)["live_quote_checked"])
        pages["lf_unset_boundary"] = "<p>Missing continuity provenance</p>"
        with self.assertRaisesRegex(ValueError, "Un-set continuity boundary"):
            A.audit(pages)
        pages["lf_unset_boundary"] = pack["continuity_boundary_excerpt"]
        pages["lf_muraganda_guide"] = ""
        with self.assertRaisesRegex(ValueError, "excerpt absent"):
            A.audit(pages)

    def test_representative_histories_remain_qualified(self):
        for plane in A.EXPECTED:
            with self.subTest(plane=plane):
                response = mv_ask.ask(f"What is the history of {plane}?")
                self.assertEqual((response["route"], response["confidence"]),
                                 ("ask->plane_history", "QUALIFIED"))
                self.assertEqual(response["result"]["direct_claims"], 5)
                self.assertFalse(response["result"]["complete_history"])
                self.assertFalse(response["result"]["verified_total_chronology"])
                self.assertIn("NO_VERIFIED_TOTAL_CHRONOLOGY", response["flags"])

    def test_foundation_packet_and_deck_hold(self):
        self.assertEqual(len(P.QA_CASES), 42)
        self.assertEqual(len({c[0] for c in P.QA_CASES}), 42)
        packet = P.build()
        self.assertEqual(len(packet["representative_questions"]), 42)
        self.assertEqual(packet["coverage"]["thin_plane_dossiers"], 0)
        self.assertTrue(packet["phase6_deckbuilding_deferred"])
        self.assertFalse(packet["owner_accepted"])
        self.assertFalse(packet["release_certified"])


if __name__ == "__main__":
    unittest.main()
