"""Batch 9: the reviewed-no-claim register (data/lore_research/reviewed_no_claim.json).

A listed page was read and holds no quotable story relation. It is counted apart from cited pages,
never as an approval, and the coverage builder rejects bad entries."""
import copy
import json
import sys
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import build_story_coverage_inventory as S  # noqa: E402


class ReviewedNoClaim(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.reg = json.loads(S.REVIEWED.read_text(encoding="utf-8"))
        cls.inv = json.loads(S.OUT.read_text(encoding="utf-8"))

    def test_register_is_labelled_not_an_approval(self):
        self.assertEqual(self.reg["schema"], "reviewed-no-claim/v1")
        self.assertIn("NOT an owner approval", self.reg["meaning"])
        for e in self.reg["entries"]:
            self.assertEqual(e["reviewer"], "GrokBot")
            self.assertIn(e["reason"], self.reg["reasons"])
            self.assertTrue(e["url"].startswith("https://magic.wizards.com/"))
            for k in ("approved", "approval", "certified", "locked"):
                self.assertNotIn(k, e)

    def test_reviewed_pages_are_not_counted_as_cited(self):
        for a in self.inv["arcs"]:
            self.assertEqual(a["pages"] - a["cited_pages"], len(a["uncited_urls"]))
            self.assertEqual(a["pages"] - a["cited_pages"] - a["reviewed_no_claim_pages"], len(a["unreviewed_urls"]))
            want = "NOT_STARTED" if not a["cited_pages"] + a["reviewed_no_claim_pages"] else (
                "ALL_PAGES_CITED_OR_REVIEWED" if a["cited_pages"] + a["reviewed_no_claim_pages"] == a["pages"] else "PARTIAL")
            self.assertEqual(a["review_status"], want, a["arc"])
        self.assertEqual(self.inv["totals"]["reviewed_no_claim_pages"], len(self.reg["entries"]))

    def test_iko_is_reviewed_but_still_not_all_cited(self):
        iko = next(a for a in self.inv["arcs"] if a["arc"] == "IKO")
        self.assertEqual(iko["status"], "PARTIAL")  # honest: only 1 of 3 pages is cited
        self.assertEqual(iko["review_status"], "ALL_PAGES_CITED_OR_REVIEWED")
        self.assertEqual(iko["reviewed_no_claim_pages"], 2)

    def _build_with(self, reg):
        with mock.patch.object(S, "REVIEWED") as p:
            p.exists.return_value = True
            p.read_text.return_value = json.dumps(reg)
            p.name = "reviewed_no_claim.json"
            p.relative_to.return_value = Path("data/lore_research/reviewed_no_claim.json")
            return S.build()

    def test_bad_entries_are_rejected(self):
        cited_url = "https://magic.wizards.com/en/news/feature/planeswalkers-guide-ikoria-2020-04-02"
        cases = {
            "cited": dict(url=cited_url, page_key="planeswalkers-guide-ikoria-2020-04-02"),
            "unknown reason": dict(reason="LOOKS_BORING"),
            "wrong arc": dict(arc="KHM"),
            "outside inventory": dict(url="https://magic.wizards.com/en/news/feature/zzz", page_key="zzz"),
            "missing note": dict(note=""),
            "bad duplicate": dict(reason="DUPLICATE_PAGE", duplicate_of="https://magic.wizards.com/en/zzz"),
        }
        for name, change in cases.items():
            with self.subTest(name):
                reg = copy.deepcopy(self.reg)
                reg["entries"][0].update(change)
                with self.assertRaises(ValueError):
                    self._build_with(reg)
        reg = copy.deepcopy(self.reg)
        reg["entries"].append(copy.deepcopy(reg["entries"][0]))
        with self.assertRaises(ValueError):
            self._build_with(reg)

    def test_valid_register_builds(self):
        self.assertEqual(self._build_with(self.reg), self.inv)


if __name__ == "__main__":
    unittest.main()
