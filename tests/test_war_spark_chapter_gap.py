"""The two previously unused official story chapters give bounded chronology, not a total war timeline."""
import json
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_war_spark_chapter_gap as C


class WarSparkChapterGapTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.current = C.build()

    def test_report_exactly_matches_registered_first_party_sources(self):
        self.assertEqual(json.loads(C.OUT.read_text()), self.current)
        self.assertEqual(self.current["counts"], {"new_strands": 2, "new_events": 10,
                                                 "new_strict_edges": 8, "new_source_local_pairs": 20,
                                                 "official_pages": 2, "live_verifiable_quotes": 8})
        self.assertTrue(self.current["excluded_from_certified_v300_graph_and_packet"])
        self.assertEqual({e["source_id"] for e in self.current["edges"]},
                         {"wr_path_opulent", "wr_desperate"})

    def test_source_local_paths_and_unproven_cross_strand_order(self):
        a = C.proof(self.current, "PO:hekara_mourned", "PO:simic_izzet_arrive")
        self.assertEqual((a["result"], len(a["proof"])), ("BEFORE", 4))
        b = C.proof(self.current, "DO:kaya_commissioned", "DO:golgari_rescue")
        self.assertEqual((b["result"], len(b["proof"])), ("BEFORE", 4))
        self.assertEqual(C.proof(self.current, "PO:simic_izzet_arrive",
                                 "DO:kaya_commissioned")["result"], "UNKNOWN")
        self.assertEqual(C.proof(self.current, "DO:vraska_returns",
                                 "Y:blackblade_shatters")["result"], "UNKNOWN")
        self.assertEqual(C.proof(self.current, "DO:golgari_rescue",
                                 "W:bolas_imprisoned")["result"], "UNKNOWN")
        with self.assertRaises(ValueError):
            C.proof(self.current, "DO:vraska_returns", "Y:made_up")

    def test_live_quote_checker_rejects_missing_excerpts(self):
        pages = {s["url"]: " ".join(e["quote"] for e in self.current["edges"] if e["source_id"] == id)
                 for id, s in self.current["sources"].items()}
        self.assertEqual(C.live_check(self.current, lambda url: pages[url])["quotes"], 8)
        with self.assertRaisesRegex(ValueError, "official live quotation absent"):
            C.live_check(self.current, lambda url: "unrelated official story page")

    def test_tampered_cross_strand_order_rejected(self):
        original = C.SPEC
        doc = json.loads(original.read_text())
        doc["strands"][0]["edges"][0]["later"] = "DO:kaya_commissioned"
        with patch.object(C, "SPEC", type("PretendFile", (), {"read_bytes": lambda self: json.dumps(doc).encode()})()):
            with self.assertRaisesRegex(ValueError, "unsupported cross-strand"):
                C.build()


if __name__ == "__main__":
    unittest.main()
