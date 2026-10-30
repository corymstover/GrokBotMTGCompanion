import json
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_lore_pilot as A  # noqa: E402
import commander_rules as CR  # noqa: E402

SPEC = ROOT / "data/lore_decks/specs/pilot3_ugins_allies_and_heroes.json"
EV = ROOT / "data/lore_decks/drafts/ugins_allies_and_heroes_printing_evidence.json"
ATLAS = ROOT / "data/story_atlas/story_art_captions_2026-10-30.json"
CAP = re.compile(r"Its art \(by (.+?)\) is embedded with an 'Art by' caption in the official story \"(.+?)\"")


class Pilot3Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.spec = json.loads(SPEC.read_text(encoding="utf-8"))
        cls.ev = json.loads(EV.read_text(encoding="utf-8"))
        cls.pack = json.loads((ROOT / cls.spec["claim_packs"][0]).read_text(encoding="utf-8"))

    def test_audit_passes_and_stays_unapproved(self):
        r = A.audit(SPEC)
        self.assertEqual(r["result"], "PASS")
        self.assertEqual(r["total"], 100)
        self.assertTrue(r["status"].startswith("UNAPPROVED"))

    def test_commander_is_eligible_by_rules(self):
        out = CR.commander(["Jace, Multiverse Architect"])
        self.assertEqual(out["confidence"], "VERIFIED")
        self.assertTrue(out["result"]["allowed"])
        self.assertIn("903.3a", [x["rule"] for x in out["rules"]])

    def test_every_caption_statement_is_in_the_atlas(self):
        titles = {v["title"]: v["url"] for v in self.pack["source_register"].values()}
        atlas = {(p["url"], c["card"], c["artist"]) for p in json.loads(ATLAS.read_text(encoding="utf-8"))["pages"]
                 for c in p["captions"]}
        n = 0
        for c in self.ev["cards"]:
            m = CAP.search(c["why"])
            if not m:
                continue
            n += 1
            self.assertIn((titles[m[2]], c["name"], m[1]), atlas, c["name"])
            self.assertEqual(c["printing"]["artist"], m[1], c["name"])
        self.assertGreaterEqual(n, 30)

    def test_implied_claim_never_cited(self):
        implied = {c["id"] for c in self.pack["claims"] if c["grade"] != "CANON_CONFIRMED"}
        self.assertEqual(implied, {"U016"})
        for c in self.ev["cards"]:
            self.assertFalse(set(c.get("claims", [])) & implied, c["name"])

    def test_lore_inspired_cards_cite_no_claims(self):
        for c in self.ev["cards"]:
            if c["tier"] == "LORE_INSPIRED":
                self.assertEqual(c["claims"], [], c["name"])
            if c["tier"] == "CANON_REFERENCE":
                self.assertTrue(c["claims"], c["name"])


if __name__ == "__main__":
    unittest.main()
