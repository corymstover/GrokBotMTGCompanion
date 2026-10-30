import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_claim_card_anchors as A  # noqa: E402


class ClaimCardAnchorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d = json.loads(A.OUT.read_text(encoding="utf-8"))

    def test_check_passes(self):
        self.assertEqual(A.main(["--check"]), 0)

    def test_research_status_and_disclaimer(self):
        self.assertTrue(self.d["status"].startswith("PRELIMINARY_RESEARCH"))
        self.assertIn("never asserts that the card depicts", self.d["rule"])

    def test_every_claim_counted_and_episode_packs_anchored(self):
        n = sum(len(json.loads((ROOT / p).read_text(encoding="utf-8"))["claims"])
                for p in json.loads(A.N.MANIFEST.read_text(encoding="utf-8"))["claim_packs"])
        self.assertEqual(self.d["counts"]["claims"], n)
        for pack in A.STORY_SETS:
            self.assertGreater(self.d["by_pack"][pack]["claims_anchored"], 0, pack)
            self.assertGreater(self.d["by_pack"][pack]["PRINTED_IN_STORY_SET"], 0, pack)

    def test_art_tier_only_for_cited_official_pages(self):
        packs = {}
        for p in json.loads(A.N.MANIFEST.read_text(encoding="utf-8"))["claim_packs"]:
            d = json.loads((ROOT / p).read_text(encoding="utf-8"))
            packs[Path(p).name] = d
        atlas = json.loads(A.ATLAS.read_text(encoding="utf-8"))
        art = {p["url"]: {x["oracle_id"] for x in p["captions"]} for p in atlas["pages"]}
        art_rows = [r for r in self.d["anchors"] if r["tier"] == "ART_IN_CITED_SOURCE"]
        self.assertGreaterEqual(len(art_rows), 20)
        for r in art_rows:
            d = packs[r["pack"]]
            c = next(x for x in d["claims"] if x["id"] == r["claim"])
            cited = {d["source_register"][s]["url"] for s in c["source_ids"]}
            for u in r["cited_pages_crediting_art"]:
                self.assertIn(u, cited)
                self.assertTrue(u.startswith("https://magic.wizards.com/"))
                self.assertIn(r["oracle_id"], art[u])

    def test_set_tier_only_for_mapped_packs(self):
        for r in self.d["anchors"]:
            if r["tier"] == "PRINTED_IN_STORY_SET":
                self.assertIn(r["pack"], A.STORY_SETS)
                self.assertTrue(set(r["story_set_printings"]) <= set(A.STORY_SETS[r["pack"]]))

    def test_mutation_foreign_card_caught(self):
        cur = copy.deepcopy(self.d)
        cur["anchors"][0]["oracle_id"] = "00000000-0000-0000-0000-000000000000"
        self.assertTrue(A.structural_problems(cur))

    def test_snapshot_free_append_is_source_limited(self):
        pack = 'pack_c5_phyrexian_invasion_outcome_2026-10-30.json'
        self.assertEqual(self.d['by_pack'][pack]['claims'], 2)
        self.assertEqual(self.d['by_pack'][pack]['claims_anchored'], 1)
        rows = [r for r in self.d['anchors'] if r['pack'] == pack]
        self.assertEqual([(r['claim'], r['card'], r['tier']) for r in rows],
                         [('C501', 'Yawgmoth, Thran Physician', 'NAMED_PARTICIPANT')])
        self.assertEqual(A.coverage_problems(self.d), [])
        missing = copy.deepcopy(self.d)
        del missing['by_pack'][pack]
        self.assertTrue(A.coverage_problems(missing))


if __name__ == "__main__":
    unittest.main()
