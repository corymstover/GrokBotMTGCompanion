"""Phase 2 L213: the card lore-link overlay stays conservative, cited and consistent with committed data."""
import csv
import json
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data/lore_research/card_lore_links_2026-10-30.json"
TEXT_TIERS = {"CLAIM_ANCHORED", "OFFICIAL_TEXT_NAMES_CARD", "SHORT_NAME_IN_SET_STORY"}


class CardLoreLinksTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d = json.loads(OUT.read_text(encoding="utf-8"))
        cls.urls = {r["url"] for r in csv.DictReader((ROOT / "data/primary_sources.csv").open(encoding="utf-8"))}
        cls.urls |= {r["url"] for r in csv.DictReader((ROOT / "data/story_extra_sources.csv").open(encoding="utf-8"))}

    def test_pool_matches_enrichment_no_lore_cards(self):
        cards = json.loads((ROOT / "data/card_enrichment.json").read_text(encoding="utf-8"))["cards"]
        pool = {k for k, v in cards.items()
                if any(l.startswith("- **Lore:**") and "❓ No lore entry" in l for l in v["lines"])}
        self.assertEqual(pool, {c["oracle_id"] for c in self.d["cards"]})
        self.assertEqual(self.d["pool"], len(pool))

    def test_status_follows_evidence(self):
        for c in self.d["cards"]:
            tiers = {e["tier"] for e in c["evidence"]}
            want = "LINKED" if tiers & TEXT_TIERS else "ART_ONLY" if tiers else "NO_LORE_YET"
            self.assertEqual(c["status"], want, c["name"])
            self.assertEqual(c["no_lore_reason"] is None, want == "LINKED", c["name"])

    def test_universes_beyond_never_text_matched(self):
        for c in self.d["cards"]:
            if c["universes_beyond"]:
                tiers = {e["tier"] for e in c["evidence"]}
                self.assertFalse(tiers & {"OFFICIAL_TEXT_NAMES_CARD", "SHORT_NAME_IN_SET_STORY"}, c["name"])

    def test_quotes_are_verbatim_and_contain_the_name(self):
        for c in self.d["cards"]:
            front = c["name"].split(" // ")[0]
            for e in c["evidence"]:
                if e["tier"] in {"OFFICIAL_TEXT_NAMES_CARD", "SHORT_NAME_IN_SET_STORY"}:
                    name = front if e["tier"] == "OFFICIAL_TEXT_NAMES_CARD" else e["short_name"]
                    self.assertTrue(front.startswith(name))
                    for p in e["pages"]:
                        self.assertIn(p["url"], self.urls)
                        self.assertGreaterEqual(len(p["quote"]), 25)
                        self.assertLessEqual(len(p["quote"]), 400)
                        self.assertRegex(p["quote"], r"(?<![A-Za-z0-9])" + re.escape(name) + r"(?![A-Za-z0-9])")
                        self.assertNotRegex(p["quote"], re.escape(name) + r"\s*\|\s*Art by$")

    def test_implied_tier_is_labelled_and_same_set(self):
        for c in self.d["cards"]:
            for e in c["evidence"]:
                if e["tier"] == "SHORT_NAME_IN_SET_STORY":
                    self.assertEqual(e["grade"], "IMPLIED_SAME_SET_NAME")
                    self.assertIn("inferred", e["limitation"])
                    for p in e["pages"]:
                        self.assertTrue(p["arc"], c["name"])

    def test_claim_anchors_resolve_to_real_claims_with_sources(self):
        packs = {}
        for c in self.d["cards"]:
            for e in c["evidence"]:
                if e["tier"] != "CLAIM_ANCHORED":
                    continue
                for x in e["claims"]:
                    if x["pack"] not in packs:
                        packs[x["pack"]] = {k["id"] for k in json.loads(
                            (ROOT / "data/lore_research" / x["pack"]).read_text(encoding="utf-8"))["claims"]}
                    self.assertIn(x["claim"], packs[x["pack"]])
                    self.assertTrue(x["source_urls"], (c["name"], x["claim"]))

    def test_counts_and_status_label(self):
        from collections import Counter
        n = Counter(c["status"] for c in self.d["cards"])
        for k in ("LINKED", "ART_ONLY", "NO_LORE_YET"):
            self.assertEqual(self.d["counts"].get(k, 0), n[k])
        self.assertIn("not owner approved", self.d["status"])

    @unittest.skipUnless((ROOT / ".cache/story/text22").is_dir() and any((ROOT / ".cache/multiverse").glob(
        "oracle-cards-*.jsonl.gz")), "story cache / Scryfall snapshot not present")
    def test_builder_check_is_current(self):
        r = subprocess.run([sys.executable, "scripts/build_card_lore_links.py", "--check"], cwd=ROOT,
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)


if __name__ == "__main__":
    unittest.main()
