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
        self.assertEqual(arcs["KLD/AER"]["status"], "NOT_STARTED")

    def test_claim_total_matches_graph_packs(self):
        self.assertEqual(self.d["totals"]["claims"], sum(self.d["claims_per_pack"].values()))


if __name__ == "__main__":
    unittest.main()
