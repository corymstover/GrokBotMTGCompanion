import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import build_story_coverage_inventory as S  # noqa: E402


class StoryCoverageInventory(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d = json.loads(S.OUT.read_text(encoding="utf-8"))

    def test_up_to_date(self):
        self.assertEqual(S.build(), self.d)

    def test_every_inventoried_page_counted_once(self):
        self.assertEqual(sum(a["pages"] for a in self.d["arcs"]), self.d["totals"]["pages"])
        for a in self.d["arcs"]:
            self.assertEqual(a["pages"] - a["cited_pages"], len(a["uncited_urls"]))

    def test_status_matches_counts(self):
        for a in self.d["arcs"]:
            want = "NOT_STARTED" if a["cited_pages"] == 0 else (
                "ALL_PAGES_CITED" if a["cited_pages"] == a["pages"] else "PARTIAL")
            self.assertEqual(a["status"], want, a["arc"])
            self.assertEqual(bool(a["citing_packs"]), a["cited_pages"] > 0)

    def test_known_coverage(self):
        arcs = {a["arc"]: a for a in self.d["arcs"]}
        self.assertEqual(arcs["MOM"]["cited_pages"], 10)  # Pack C4 cites all 10 main-story episodes
        self.assertEqual(arcs["ONE"]["status"], "ALL_PAGES_CITED")
        # Phase 5 bulk pipeline packs (batch 5): KLD/AER, XLN/RIX and AKH/HOU are started
        self.assertEqual(arcs["KLD/AER"]["cited_pages"], 14)
        self.assertEqual(arcs["XLN/RIX"]["cited_pages"], 10)
        # Batch 6: MID/VOW, SNC and EOE packs
        self.assertEqual(arcs["MID/VOW"]["cited_pages"], 8)
        self.assertEqual(arcs["SNC"]["status"], "ALL_PAGES_CITED")
        # Batch 6b: RF, WOE and MKM packs
        self.assertEqual(arcs["WOE"]["status"], "ALL_PAGES_CITED")
        self.assertEqual(arcs["MKM"]["cited_pages"], 10)
        # Batch 6c: BLB and DSK packs
        self.assertEqual(arcs["BLB"]["cited_pages"], 6)
        self.assertEqual(arcs["DSK"]["cited_pages"], 6)
        self.assertEqual(arcs["OTJ"]["status"], "ALL_PAGES_CITED")
        self.assertEqual(arcs["LCI"]["cited_pages"], 7)
        self.assertEqual(arcs["DFT"]["cited_pages"], 6)
        self.assertEqual(arcs["KHM"]["cited_pages"], 6)
        self.assertEqual(arcs["STX"]["cited_pages"], 5)
        self.assertEqual(arcs["IKO"]["cited_pages"], 1)
        # Batch 7a: THB, THS (Planeswalker's Guides), MAT, ELD guide
        self.assertEqual(arcs["THB"]["cited_pages"], 1)
        self.assertEqual(arcs["THS"]["cited_pages"], 5)
        self.assertEqual(arcs["MAT"]["status"], "ALL_PAGES_CITED")
        self.assertEqual(arcs["ELD"]["status"], "ALL_PAGES_CITED")
        # Batch 7b: SOS (legends, guide, episode 6), SOI/EMN
        # Batch 7 (overnight run batch 7): bulk fills; SOI/EMN, BFZ/OGW and EOE now cite every page
        self.assertEqual(arcs["SOI/EMN"]["status"], "ALL_PAGES_CITED")
        self.assertEqual(arcs["BFZ/OGW"]["status"], "ALL_PAGES_CITED")
        self.assertEqual(arcs["EOE"]["status"], "ALL_PAGES_CITED")
        self.assertEqual(arcs["AKH/HOU"]["status"], "ALL_PAGES_CITED")
        self.assertEqual(arcs["TDM"]["status"], "ALL_PAGES_CITED")
        for arc in ("SOS", "ECL", "RF", "BRO"):
            self.assertEqual(arcs[arc]["status"], "ALL_PAGES_CITED", arc)

    def test_claim_total_matches_graph_packs(self):
        self.assertEqual(self.d["totals"]["claims"], sum(self.d["claims_per_pack"].values()))


if __name__ == "__main__":
    unittest.main()
