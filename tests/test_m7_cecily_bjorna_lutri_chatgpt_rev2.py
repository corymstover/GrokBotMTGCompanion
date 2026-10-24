"""Cecily/Bjorna/Lutri ChatGPT M7 Rev2 ten-swap source-bound research, not owner approval."""
import hashlib, json, unittest
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"data/grixis/m7/baseline_sources/Cecily__Bjorna__Lutri_approved_source_2026-10-13.txt"
GROK=ROOT/"data/grixis/m7/candidate_lists/Cecily__Bjorna__Lutri.txt"
REV2=ROOT/"data/grixis/m7/candidate_lists/Cecily__Bjorna__Lutri_ChatGPT_M7_Rev2_Ten_Approval_Candidate.txt"
ORACLE=ROOT/"data/grixis/m6/oracle_snapshots/Cecily__Bjorna__Lutri_ChatGPT_M7_Rev2_Selected_20261023.json"
REVIEW=ROOT/"data/grixis/m7/decision_reviews/Cecily__Bjorna__Lutri_ChatGPT_M7_Rev2_Independent.md"
RAW="e4028f06d2d928ad06fb8667ae4bba77c31b4f97c1d4fb5490f83b73eb6d6b5d"
BASE_SHA="553838da88fe00974e74664633be5051c4f1a0879baa71de81ca9f880e5a6d28"
GROK_SHA="2cc7227f954e728e0b37949b74f9575128b2c82250f53e211289aa60e4fa1717"
SWAPS=(
 ("Emry, Lurker of the Loch","Strionic Resonator"),
 ("Goblin Engineer","Echo, Perceptive Prodigy"),
 ("Sai, Master Thopterist","Twenty-Toed Toad"),
 ("Dark Deal","Sea Gate Restoration // Sea Gate, Reborn"),
 ("Mana Geyser","Deflecting Swat"),
 ("Seething Song","Mana Drain"),
 ("Cruel Ultimatum","Fevered Suspicion"),
 ("Wheel of Misfortune","Aminatou's Augury"),
 ("Crumbling Necropolis","City of Brass"),
 ("Fabled Passage","Mana Confluence"),
)
GCS={"Cyclonic Rift","Demonic Tutor","Fierce Guardianship","Jeska's Will","Mystical Tutor",
     "Notion Thief","Rhystic Study","The One Ring","Underworld Breach","Vampiric Tutor"}
ROCKS={"Sol Ring","Arcane Signet","Dimir Signet","Izzet Signet","Rakdos Signet",
       "Talisman of Creativity","Talisman of Dominance","Talisman of Indulgence","Thought Vessel"}
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def parse(path):
    lines=path.read_text(encoding="utf-8").splitlines()
    out=[]
    for line in lines:
        q,n=line.split("x ",1)
        zone="main"
        for label in ("Commander","Companion"):
            if n.endswith(" ["+label+"]"):
                n=n.removesuffix(" ["+label+"]");zone=label
        out.append((int(q),n,zone))
    return out

class CecilyBjornaLutriChatGPTRev2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows=parse(REV2)
        cls.o=json.loads(ORACLE.read_text(encoding="utf-8"))
        cls.cards={c["name"]:c for c in cls.o["cards"]}
        cls.counts=Counter({n:q for q,n,z in cls.rows if z!="Companion"})
        cls.prior=Counter({n:q for q,n,z in parse(BASE)})

    def test_immutable_sources_exact_raw_hash(self):
        self.assertEqual(sha(BASE),BASE_SHA)
        self.assertEqual(sha(GROK),GROK_SHA)
        self.assertEqual(sha(REV2),RAW)
        self.assertTrue(REV2.read_bytes().endswith(bytes([10])))

    def test_companion_outside_100_two_commanders_singleton(self):
        self.assertEqual(len(self.rows),100)
        self.assertEqual(sum(q for q,n,z in self.rows if z!="Companion"),100)
        self.assertEqual(sum(q for q,n,z in self.rows),101)
        self.assertEqual(self.rows[:3],[
          (1,"Bjorna, Nightfall Alchemist","Commander"),
          (1,"Cecily, Haunted Mage","Commander"),
          (1,"Lutri, the Spellchaser","Companion")])
        self.assertEqual({n:q for n,q in self.counts.items() if q>1},{"Island":2})
        self.assertEqual(len(self.counts),99)

    def test_exact_ten_swaps_against_approved_baseline(self):
        self.assertEqual(self.counts-self.prior,Counter({a:1 for c,a in SWAPS}))
        self.assertEqual(self.prior-self.counts,Counter({c:1 for c,a in SWAPS}))
        self.assertEqual(len(SWAPS),10)
        self.assertIn("In Garruk's Wake",self.counts)
        self.assertIn("Wheel of Fortune",self.counts)

    def test_oracle_identity_exceptions_and_project_truth(self):
        self.assertEqual(self.o["candidate_raw_sha256"],RAW)
        self.assertEqual(self.o["physical_cards_in_100"],100)
        self.assertEqual(self.o["total_physical_including_companion"],101)
        self.assertEqual(len(self.cards),100)
        self.assertEqual(set(self.cards),{n for q,n,z in self.rows})
        self.assertEqual(set(self.o["official_commander_banned_cards_in_100"]),{"Trade Secrets","Yawgmoth's Bargain"})
        self.assertTrue(self.o["companion_officially_banned"])
        self.assertEqual(len(self.o["ban_exceptions"]),3)
        for q,n,z in self.rows:
            c=self.cards[n]
            self.assertEqual(c["quantity"],q,n)
            self.assertEqual(c["zone"],z,n)
            self.assertLessEqual(set(c["color_identity"]),{"U","B","R"},n)
            self.assertTrue(c["oracle_id"],n)
            self.assertTrue(c["source"],n)
            if n in {"Trade Secrets","Yawgmoth's Bargain"}:
                self.assertEqual(c["commander_legality"],"banned")
                self.assertIn("exception",c["project_exception"].lower())
            else:
                self.assertEqual(c["commander_legality"],"legal",n)
        self.assertIn("companion",self.cards["Lutri, the Spellchaser"]["project_exception"])

    def test_mana_land_pips_bracket(self):
        self.assertEqual(self.o["printed_land_slots"],33)
        self.assertEqual(self.o["modal_land_options"],1)
        self.assertEqual(len(ROCKS & set(self.counts)),9)
        self.assertEqual({n for n in self.counts if self.cards[n]["game_changer"]},GCS)
        self.assertEqual(self.o["static_rocks"],9)
        self.assertIn("Sea Gate Restoration // Sea Gate, Reborn",self.counts)

    def test_commander_new_freecast_and_trigger_interactions(self):
        ce=self.cards["Cecily, Haunted Mage"]["oracle_text"]
        self.assertIn("Then if you have eleven or more cards",ce)
        self.assertIn("without paying its mana cost",ce)
        self.assertIn("Copy target activated or triggered ability",self.cards["Echo, Perceptive Prodigy"]["oracle_text"])
        self.assertIn("Copy target triggered ability",self.cards["Strionic Resonator"]["oracle_text"])
        self.assertIn("you win the game",self.cards["Twenty-Toed Toad"]["oracle_text"])
        self.assertIn("Rebound",self.cards["Fevered Suspicion"]["oracle_text"])
        self.assertIn("Exile the top eight cards",self.cards["Aminatou's Augury"]["oracle_text"])
        self.assertIn("Companion",self.cards["Lutri, the Spellchaser"]["oracle_text"])

    def test_strategy_discloses_real_tradeoffs_not_owner_approval(self):
        s=REVIEW.read_text(encoding="utf-8")
        self.assertIn("NOT OWNER APPROVED",s)
        self.assertIn("NOT CANONICAL",s)
        self.assertIn(RAW,s)
        self.assertIn("two rituals",s)
        self.assertIn("Bjorna",s)
        self.assertIn("non-independent",s)
        self.assertIn("not officially legal",s.lower())

    def test_old_grok_six_and_new_four_delta(self):
        old=Counter({n:q for q,n,z in parse(GROK) if z!="Companion"})
        self.assertEqual(self.counts-old,Counter({"Fevered Suspicion":1,"Aminatou's Augury":1,"City of Brass":1,"Mana Confluence":1}))
        self.assertEqual(old-self.counts,Counter({"Cruel Ultimatum":1,"Wheel of Misfortune":1,"Crumbling Necropolis":1,"Fabled Passage":1}))

if __name__=="__main__":unittest.main()
