"""Source-bound independent Be'lakor M7 Rev2 eight-swap review; never owner approval."""
import hashlib
import json
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "data/grixis/m7/baseline_sources/Be_lakor_the_Dark_Master_approved_source_2026-10-13.txt"
GROK = ROOT / "data/grixis/m7/candidate_lists/Be_lakor__the_Dark_Master.txt"
FINAL = ROOT / "data/grixis/m7/candidate_lists/Be_lakor__the_Dark_Master_ChatGPT_M7_Rev2_Eight_Approval_Candidate.txt"
ORACLE = ROOT / "data/grixis/m6/oracle_snapshots/Be_lakor__the_Dark_Master_ChatGPT_M7_Rev2_Selected_20261023.json"
REVIEW = ROOT / "data/grixis/m7/decision_reviews/Be_lakor__the_Dark_Master_ChatGPT_M7_Rev2_Independent.md"
RAW = "2107f02e7a5303eef15b6720565d08dfe974b3d6fa57ea449440042cec1b4dd4"
BASE_SHA = "3abc951606a6db2b17ea2aceb471fc2ef4c55e2ef082d49d9140a83b2491155e"
GROK_SHA = "62a96b4f39584fa38947843bea352de923b29d7b266b57fce5918802a79b57bf"
SWAPS = (
    ("Dream Devourer", "Desecration Demon"),
    ("Blasphemous Act", "Kindred Dominance"),
    ("Rakdos, Patron of Chaos", "Demonlord Belzenlok"),
    ("Bloodthirster", "Shadowgrange Archfiend"),
    ("Fellwar Stone", "Cursed Mirror"),
    ("Balor", "Curse-Marred Demon"),
    ("Crumbling Necropolis", "City of Brass"),
    ("Foreboding Ruins", "Mana Confluence"),
)
ROCKS = {"Sol Ring", "Arcane Signet", "Rakdos Signet", "Talisman of Creativity",
         "Talisman of Dominance", "Talisman of Indulgence", "Cursed Mirror"}
GCS = {"Ancient Tomb", "Cyclonic Rift", "Demonic Tutor", "Fierce Guardianship", "Vampiric Tutor"}

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def parse(path):
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line: continue
        quantity, name = line.split("x ", 1)
        rows.append((int(quantity), name.removesuffix(" [Commander]")))
    return rows

class BeLakorChatGPTRev2Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.baseline = parse(BASE)
        cls.original = parse(GROK)
        cls.final = parse(FINAL)
        cls.oracle = json.loads(ORACLE.read_text())
        cls.cards = {c["name"]: c for c in cls.oracle["cards"]}
        cls.final_counts = Counter({n:q for q,n in cls.final})

    def test_immutable_baseline_and_first_pass_hashes(self):
        self.assertEqual(sha(BASE), BASE_SHA)
        self.assertEqual(sha(GROK), GROK_SHA)
        self.assertEqual(sum(q for q,n in self.baseline), 100)
        self.assertEqual(sum(q for q,n in self.original), 100)

    def test_exact_new_candidate_hash_and_shape(self):
        self.assertEqual(sha(FINAL), RAW)
        self.assertTrue(FINAL.read_bytes().endswith(b"\n"))
        self.assertEqual(len(self.final), 94)
        self.assertEqual(sum(q for q,n in self.final), 100)
        self.assertEqual(len(self.final_counts), 94)
        self.assertEqual(self.final[0], (1, "Be'lakor, the Dark Master"))
        self.assertEqual(self.final_counts["Island"], 3)
        self.assertEqual(self.final_counts["Mountain"], 2)
        self.assertEqual(self.final_counts["Swamp"], 4)
        for q,n in self.final:
            if q>1: self.assertIn(n, {"Island","Mountain","Swamp"})

    def test_exact_eight_not_floor_cap_or_padding(self):
        old=Counter({n:q for q,n in self.baseline})
        new=self.final_counts
        added=Counter(new-old)
        removed=Counter(old-new)
        self.assertEqual(added,Counter({add:1 for cut,add in SWAPS}))
        self.assertEqual(removed,Counter({cut:1 for cut,add in SWAPS}))
        self.assertEqual(len(added),8)
        self.assertEqual(new["Rakdos, the Showstopper"],1)
        self.assertEqual(new["Lord of Change"],1)

    def test_current_oracle_legal_color_and_source_provenance(self):
        self.assertEqual(self.oracle["candidate_raw_sha256"],RAW)
        self.assertEqual(self.oracle["physical_cards"],100)
        self.assertEqual(self.oracle["unique_card_names"],94)
        self.assertEqual(len(self.cards),94)
        self.assertEqual(set(self.cards),set(self.final_counts))
        self.assertEqual(self.oracle["exceptions"],[])
        self.assertTrue(self.oracle["status"].endswith("NOT_OWNER_APPROVED"))
        for n,q in self.final_counts.items():
            c=self.cards[n]
            self.assertEqual(c["quantity"],q)
            self.assertEqual(c["commander_legality"],"legal",n)
            self.assertLessEqual(set(c["color_identity"]),{"U","B","R"},n)
            self.assertTrue(c.get("oracle_id"),n)
            self.assertTrue(c.get("source"),n)

    def test_land_rock_demon_gc(self):
        self.assertEqual(sum(c["quantity"] for c in self.cards.values() if "Land" in c["type_line"]),36)
        self.assertEqual(sum(c["quantity"] for c in self.cards.values() if "Demon" in c["type_line"]),25)
        self.assertEqual(ROCKS & set(self.final_counts),ROCKS)
        self.assertEqual(self.oracle["static_mana_rocks"],7)
        self.assertEqual({n for n in self.final_counts if self.cards[n]["game_changer"]},GCS)
        self.assertEqual(set(self.oracle["game_changers"]),GCS)

    def test_niche_rules_oracle_not_overclaimed(self):
        curse=self.cards["Curse-Marred Demon"]["oracle_text"]
        self.assertIn("discard a card at random",curse)
        self.assertIn("search your library for a card",curse)
        shadow=self.cards["Shadowgrange Archfiend"]["oracle_text"]
        self.assertIn("greatest power among creatures sacrificed",shadow)
        mirror=self.cards["Cursed Mirror"]["oracle_text"]
        self.assertIn("As this artifact enters",mirror)
        self.assertIn("copy of any creature",mirror)
        self.assertIn("Add {R}",mirror)
        review=REVIEW.read_text(encoding="utf-8")
        self.assertIn("25 finite Lord triggers",review)
        self.assertIn("legend rule",review)
        self.assertIn("random",review)
        self.assertIn("No refreshed Spellbook",review)
        self.assertIn("non-independent",review)

    def test_no_auto_approval(self):
        review=REVIEW.read_text(encoding="utf-8")
        self.assertIn("NOT CORY-APPROVED",review)
        self.assertIn("NOT CANONICAL",review)
        self.assertIn(RAW,review)
        self.assertIn("eight",review.lower())

if __name__ == "__main__":
    unittest.main()
