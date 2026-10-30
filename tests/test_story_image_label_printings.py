"""Story image-label art-to-printing links (Batch 5). Runs with or without the caches."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_story_image_label_printings as L  # noqa: E402

D = json.loads(L.OUT.read_text(encoding="utf-8"))


class StoryImageLabelPrintings(unittest.TestCase):
    def test_structure_and_self_hash(self):
        self.assertEqual(L.structural_problems(D), [])

    def test_tamper_is_detected(self):
        bad = json.loads(json.dumps(D))
        bad["labels"][0]["collector_number"] = "99999"
        self.assertIn("self-hash", L.structural_problems(bad))

    def test_reality_fracture_coverage(self):
        fra = D["by_set"]["fra"]
        self.assertGreaterEqual(fra["MATCHED"], 150)
        rows = [r for r in D["labels"] if r["set"] == "fra" and r["status"] == "MATCHED"]
        self.assertTrue(all(r["printing"]["set"] in ("fra", "frc") for r in rows))

    def test_agrees_with_koth_printing_leads(self):
        koth = json.loads((ROOT / "data/lore_research/koth_wrenn_printing_leads_2026-10-30.json").read_text(encoding="utf-8"))
        want = {l["quote"].split(":")[0]: l["matched_printings"][0]["scryfall_id"]
                for l in koth["leads"] if l["kind"] == "COLLECTOR_NUMBER_IN_IMAGE_LABEL"}
        got = {r["label"]: r["printing"]["scryfall_id"] for r in D["labels"] if r["label"] in want}
        self.assertEqual(got, want)

    def test_matched_rows_agree_on_number_and_name(self):
        for r in D["labels"]:
            if r["status"] == "MATCHED":
                with self.subTest(label=r["label"]):
                    self.assertEqual(r["printing"]["collector_number"], r["collector_number"])
                    self.assertTrue(r["caption_name"] == r["printing"]["name"]
                                    or r["caption_name"] in r["printing"]["name"].split(" // "))

    def test_mismatches_are_kept_not_forced(self):
        mism = [r for r in D["labels"] if r["status"] == "NAME_MISMATCH"]
        self.assertTrue(mism)
        for r in mism:
            self.assertNotIn(r["caption_name"], r["printing"]["name"].split(" // "))

    def test_label_regex(self):
        m = L.LABEL.match("0248_MTGFRA_MainPair: Koth, the Geomancer")
        self.assertEqual((m["num"], m["set"], m["kind"], m["name"]), ("0248", "FRA", "MainPair", "Koth, the Geomancer"))
        self.assertIsNone(L.LABEL.match("Koth, the Geomancer | Art by: Kieran Yanner"))


if __name__ == "__main__":
    unittest.main()
