"""Batch 13: printed-flavor lore links stay conservative, distinct from story claims and consistent."""
import json
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data/lore_research/flavor_lore_links_2026-10-30.json"
LINKS = ROOT / "data/lore_research/card_lore_links_2026-10-30.json"
BULK = ROOT / ".cache/multiverse/default-cards-20261029090546.jsonl.gz"
STATUSES = {"FLAVOR_LINKED", "FLAVOR_SPEAKER_CHARACTER", "FLAVOR_NAME_ONLY", "NO_LORE_YET"}


class FlavorLoreLinksTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d = json.loads(OUT.read_text(encoding="utf-8"))
        cls.links = {c["oracle_id"]: c for c in json.loads(LINKS.read_text(encoding="utf-8"))["cards"]}
        g = json.loads((ROOT / "data/multiverse_graph/multiverse_graph.json").read_text(encoding="utf-8"))
        cls.nodes = {n["id"]: n for n in g["nodes"]}

    def test_pool_is_non_ub_no_lore_cards(self):
        pool = {o for o, c in self.links.items() if c["status"] == "NO_LORE_YET"}
        non_ub = {o for o in pool if not self.links[o]["universes_beyond"]}
        self.assertEqual(self.d["pool"]["cards"], len(pool))
        self.assertEqual({c["oracle_id"] for c in self.d["cards"]}, non_ub)
        self.assertEqual(self.d["counts"]["excluded_universes_beyond"], len(pool - non_ub))

    def test_status_follows_evidence(self):
        for c in self.d["cards"]:
            self.assertIn(c["status"], STATUSES)
            ev = c["evidence"]
            strong = [e for e in ev if e["kind"] != "SPEAKER_CARD_CHARACTER" and not e["grade"].endswith("_NAME_ONLY")]
            spk = [e for e in ev if e["kind"] == "SPEAKER_CARD_CHARACTER"]
            want = ("FLAVOR_LINKED" if strong else "FLAVOR_SPEAKER_CHARACTER" if spk else
                    "FLAVOR_NAME_ONLY" if ev else "NO_LORE_YET")
            self.assertEqual(c["status"], want, c["name"])
            if ev:
                self.assertTrue(c["has_english_flavor"], c["name"])

    def test_evidence_is_verbatim_and_cited(self):
        for c in self.d["cards"]:
            for e in c["evidence"]:
                self.assertTrue(e["printing"]["scryfall_uri"].startswith("https://scryfall.com/card/"), c["name"])
                self.assertTrue(e["grade"].startswith("PRINTED_FLAVOR_"), e["grade"])
                if e["kind"] == "SPEAKER_CARD_CHARACTER":
                    self.assertTrue(re.search(r"(?m)^\s*[—―]\s*" + re.escape(e["speaker"]), e["flavor_text"]))
                    self.assertTrue(e["speaker_cards"])
                    for s in e["speaker_cards"]:
                        self.assertNotEqual(s["oracle_id"], c["oracle_id"])
                    continue
                self.assertIn(e["entity"], self.nodes)
                self.assertEqual(self.nodes[e["entity"]]["name"], e["entity_name"])
                self.assertRegex(e["flavor_text"], r"(?<![A-Za-z0-9'])" + re.escape(e["entity_name"]))

    def test_attribution_means_the_speaker_is_the_entity(self):
        for c in self.d["cards"]:
            for e in c["evidence"]:
                if e["kind"] == "ATTRIBUTION":
                    heads = [m.group(1).split(",")[0].strip()
                             for m in re.finditer(r"(?m)^\s*[—―]\s*(.+?)\s*$", e["flavor_text"])]
                    self.assertTrue(any(h == e["entity_name"] or h.startswith(e["entity_name"] + " ") for h in heads),
                                    (c["name"], heads))

    def test_strong_grades_are_conservative(self):
        for c in self.d["cards"]:
            for e in c["evidence"]:
                if e["kind"] == "SPEAKER_CARD_CHARACTER":
                    continue
                strong = (e["multi_word_name"] or e["entity_type"] == "Plane" or e["set_consistent"]) \
                    and not e["ambiguous_name"]
                self.assertEqual(not e["grade"].endswith("_NAME_ONLY"), strong, (c["name"], e["entity_name"]))

    def test_marked_preliminary_not_story_claims(self):
        self.assertEqual(self.d["status"], "PRELIMINARY_RESEARCH")
        self.assertIn("distinct from story claims", self.d["not"])
        self.assertEqual(self.d["card_data_source"]["sha256_prefix"], "008434d5")

    @unittest.skipUnless(BULK.exists(), "pinned Scryfall bulk cache absent (CI); artifact checked structurally")
    def test_rebuild_is_current(self):
        r = subprocess.run([sys.executable, "scripts/build_flavor_lore_links.py", "--check"], cwd=ROOT,
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)


if __name__ == "__main__":
    unittest.main()
