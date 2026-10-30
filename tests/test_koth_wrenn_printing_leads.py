import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import build_koth_wrenn_printing_leads as K  # noqa: E402


class KothWrennPrintingLeads(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d = json.loads(K.OUT.read_text(encoding="utf-8"))

    def test_structure_and_hash(self):
        self.assertEqual(K.structural_problems(self.d), [])

    def test_tamper_detected(self):
        bad = copy.deepcopy(self.d)
        bad["leads"][0]["matched_printings"].append({"set": "xxx"})
        self.assertIn("self-hash", K.structural_problems(bad))

    def test_collector_number_labels_pick_one_printing(self):
        for r in self.d["leads"]:
            if r["kind"] == "COLLECTOR_NUMBER_IN_IMAGE_LABEL":
                self.assertEqual(len(r["matched_printings"]), 1)
                m = r["matched_printings"][0]
                self.assertIn("%04d_MTG%s" % (int(m["collector_number"]), m["set"].upper()), r["quote"])

    def test_prose_and_named_leads_assert_no_printing(self):
        for r in self.d["leads"]:
            if r["kind"] in ("CHARACTER_PROSE_ONLY", "NAMED_ON_OFFICIAL_PAGE"):
                self.assertFalse(r["printing_specific"])
                self.assertEqual(r["matched_printings"], [])

    def test_art_credit_printings_share_artist(self):
        for r in self.d["leads"]:
            if r["kind"] == "ART_CREDIT_NAME_AND_ARTIST":
                self.assertTrue({m["artist"] for m in r["matched_printings"]} == {r["selector"]["artist"]})
                self.assertIn(r["selector"]["artist"], r["quote"])

    def test_counts(self):
        self.assertEqual(self.d["printing_specific_leads"], 6)
        self.assertEqual(sum(self.d["counts"].values()), len(self.d["leads"]))

    @unittest.skipUnless(list(K.SNAP.glob("default-cards-*.jsonl.gz")) and K.STORY.exists(), "caches absent")
    def test_rebuild_matches(self):
        self.assertEqual(K.build(), self.d)


if __name__ == "__main__":
    unittest.main()
