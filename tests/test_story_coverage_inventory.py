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
        self.assertGreaterEqual(arcs["MOM"]["cited_pages"], 10)  # Pack C4 cites all 10 main-story episodes
        self.assertEqual(arcs["ONE"]["status"], "ALL_PAGES_CITED")
        # Phase 5 bulk pipeline packs (batch 5): KLD/AER, XLN/RIX and AKH/HOU are started
        self.assertEqual(arcs["KLD/AER"]["status"], "ALL_PAGES_CITED")  # batch 8 closed the last 3 pages
        self.assertEqual(arcs["XLN/RIX"]["status"], "ALL_PAGES_CITED")  # batch 8 closed the last 7 pages
        # Batch 6: MID/VOW, SNC and EOE packs
        self.assertEqual(arcs["MID/VOW"]["status"], "ALL_PAGES_CITED")
        self.assertEqual(arcs["SNC"]["status"], "ALL_PAGES_CITED")
        # Batch 6b: RF, WOE and MKM packs
        self.assertEqual(arcs["WOE"]["status"], "ALL_PAGES_CITED")
        self.assertGreaterEqual(arcs["MKM"]["cited_pages"], 10)
        # Batch 6c: BLB and DSK packs
        self.assertEqual(arcs["BLB"]["status"], "ALL_PAGES_CITED")  # batch 8
        self.assertGreaterEqual(arcs["DSK"]["cited_pages"], 6)
        self.assertEqual(arcs["OTJ"]["status"], "ALL_PAGES_CITED")
        self.assertEqual(arcs["LCI"]["status"], "ALL_PAGES_CITED")  # batch 8
        self.assertEqual(arcs["DFT"]["status"], "ALL_PAGES_CITED")  # batch 8
        self.assertEqual(arcs["KHM"]["status"], "ALL_PAGES_CITED")
        self.assertEqual(arcs["STX"]["status"], "ALL_PAGES_CITED")
        self.assertEqual(arcs["IKO"]["cited_pages"], 1)
        # Batch 7a: THB, THS (Planeswalker's Guides), MAT, ELD guide
        self.assertEqual(arcs["THB"]["status"], "ALL_PAGES_CITED")  # batch 8
        self.assertEqual(arcs["THS"]["status"], "ALL_PAGES_CITED")
        self.assertEqual(arcs["MAT"]["status"], "ALL_PAGES_CITED")
        self.assertEqual(arcs["ELD"]["status"], "ALL_PAGES_CITED")
        # Batch 7b: SOS (legends, guide, episode 6), SOI/EMN
        # Batch 7 (overnight run batch 7): bulk fills; SOI/EMN, BFZ/OGW and EOE now cite every page
        self.assertEqual(arcs["SOI/EMN"]["status"], "ALL_PAGES_CITED")
        self.assertGreaterEqual(arcs["BFZ/OGW"]["cited_pages"], 19)
        self.assertEqual(arcs["EOE"]["status"], "ALL_PAGES_CITED")
        self.assertEqual(arcs["AKH/HOU"]["status"], "ALL_PAGES_CITED")
        self.assertEqual(arcs["TDM"]["status"], "ALL_PAGES_CITED")
        for arc in ("SOS", "ECL", "RF", "BRO"):
            self.assertEqual(arcs[arc]["status"], "ALL_PAGES_CITED", arc)
        # Batch 7 triage: 78 untagged pages tagged to arcs (BFZ/OGW gained 8 untagged 2015
        # Zendikar side stories, so it is honestly PARTIAL again until they are packed);
        # side-story packs bring ONE, OTJ and SNC back to every page cited.
        for arc in ("ONE", "OTJ", "SNC"):
            self.assertEqual(arcs[arc]["status"], "ALL_PAGES_CITED", arc)
        self.assertEqual(self.d["totals"]["pages"], 626)
        self.assertGreaterEqual(self.d["totals"]["cited_pages"], 330)
        # Batch 7c fill: BFZ 2015 stories, DMU main episodes, NEO side stories, DSK ep2,
        # MKM ep2 and the MOM Planeswalker's Guide close six more arcs (20 of 33 all cited).
        for arc in ("BFZ/OGW", "DMU", "NEO", "DSK", "MKM", "MOM"):
            self.assertEqual(arcs[arc]["status"], "ALL_PAGES_CITED", arc)
        self.assertGreaterEqual(self.d["totals"]["cited_pages"], 350)
        self.assertGreaterEqual(self.d["totals"]["arcs_all_cited"], 20)
        # Batch 8 (overnight run): LCI, BLB, THB, KLD/AER, DFT, XLN/RIX and DOM/WAR (new War of the
        # Spark: Ravnica pack) now cite every page: 27 of 33 arcs, 376 of 626 pages.
        self.assertEqual(arcs["DOM/WAR"]["status"], "ALL_PAGES_CITED")
        self.assertGreaterEqual(self.d["totals"]["cited_pages"], 376)
        self.assertGreaterEqual(self.d["totals"]["arcs_all_cited"], 27)
        # Batch 8 part 2: KHM and STX now cite every page: 29 of 33 arcs, 389 of 626 pages.
        self.assertGreaterEqual(self.d["totals"]["cited_pages"], 389)
        self.assertGreaterEqual(self.d["totals"]["arcs_all_cited"], 29)
        # Batch 8 part 3: MID/VOW and THS now cite every page: 31 of 33 arcs, 414 of 626 pages.
        self.assertGreaterEqual(self.d["totals"]["cited_pages"], 414)
        self.assertGreaterEqual(self.d["totals"]["arcs_all_cited"], 31)
        # Batch 9: reviewed-no-claim register; IKO's 2 non-narrative pages are reviewed, not cited
        self.assertEqual(arcs["IKO"]["review_status"], "ALL_PAGES_CITED_OR_REVIEWED")
        self.assertGreaterEqual(self.d["totals"]["arcs_all_cited_or_reviewed"], 32)

    def test_claim_total_matches_graph_packs(self):
        self.assertEqual(self.d["totals"]["claims"], sum(self.d["claims_per_pack"].values()))


if __name__ == "__main__":
    unittest.main()
