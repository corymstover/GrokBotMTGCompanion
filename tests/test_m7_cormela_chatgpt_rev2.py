"""Cormela independent M7 Rev2 six-swap exact-source owner-review candidate; no canonical approval."""
import hashlib,json,unittest
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"data/grixis/m7/baseline_sources/Cormela__Glamour_Thief_approved_source_2026-10-14.txt"
GROK=ROOT/"data/grixis/m7/candidate_lists/Cormela__Glamour_Thief.txt"
REV2=ROOT/"data/grixis/m7/candidate_lists/Cormela__Glamour_Thief_ChatGPT_M7_Rev2_Six_Approval_Candidate.txt"
ORACLE=ROOT/"data/grixis/m6/oracle_snapshots/Cormela__Glamour_Thief_ChatGPT_M7_Rev2_Selected_20261023.json"
REVIEW=ROOT/"data/grixis/m7/decision_reviews/Cormela__Glamour_Thief_ChatGPT_M7_Rev2_Independent.md"
SPELLBOOK=ROOT/"data/grixis/m7/research_challengers/Cormela__Glamour_Thief_CommanderSpellbook_20261023.json"
RAW="d91ac1ab1dc543ee9fe93c69978c33966a8e9578bc46935e65d5d3b7139c46fd"
BASE_RAW="80f4bdef2b8b140aeae23775cfdf87fda81e7215038b8db9b1746c806f366e0b"
GROK_RAW="1cb098f4d1089f6989dfdb79b4abcd149000dfa5f90b923bda72ffa36aa2c8b1"
SWAPS=(
 ("Undercity Sewers","Mistrise Village"),
 ("Exotic Orchard","Underground River"),
 ("Faithless Looting","Frantic Search"),
 ("Gitaxian Probe","Twinflame"),
 ("Red Elemental Blast","Hexing Squelcher"),
 ("Preordain","Into the Flood Maw"),
)
ROCKS={"Arcane Signet","Ashnod's Altar","Chrome Mox","Lion's Eye Diamond","Lotus Petal",
       "Mana Vault","Mox Diamond","Mox Opal","Phyrexian Altar","Sol Ring",
       "Talisman of Creativity","Talisman of Dominance","Talisman of Indulgence"}
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def parse(path):
    lines=path.read_text(encoding="utf-8").splitlines()
    rows=[]
    for line in lines:
        q,n=line.split("x ",1)
        assert q.isdecimal() and int(q)>0,line
        if n.endswith(" [Commander]"): n=n.removesuffix(" [Commander]")
        rows.append((int(q),n))
    return rows

class CormelaChatGPTRev2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows=parse(REV2)
        cls.counts=Counter({n:q for q,n in cls.rows})
        cls.before=Counter({n:q for q,n in parse(BASE)})
        cls.grok=Counter({n:q for q,n in parse(GROK)})
        cls.o=json.loads(ORACLE.read_text(encoding="utf-8"))
        cls.cards={c["name"]:c for c in cls.o["cards"]}

    def test_three_immutable_raw_source_hashes(self):
        self.assertEqual(sha(BASE),BASE_RAW)
        self.assertEqual(sha(GROK),GROK_RAW)
        self.assertEqual(sha(REV2),RAW)
        self.assertTrue(REV2.read_bytes().endswith(bytes([10])))

    def test_exact_100_single_commander_and_singleton(self):
        self.assertEqual(len(self.rows),100)
        self.assertEqual(len(self.counts),100)
        self.assertEqual(sum(self.counts.values()),100)
        self.assertTrue(all(q==1 for q,n in self.rows))
        self.assertEqual(REV2.read_text(encoding="utf-8").splitlines()[0],
            "1x Cormela, Glamour Thief [Commander]")

    def test_six_swaps_vs_canonical_and_one_new_postfloor(self):
        self.assertEqual(self.counts-self.before,Counter({a:1 for c,a in SWAPS}))
        self.assertEqual(self.before-self.counts,Counter({c:1 for c,a in SWAPS}))
        self.assertEqual(len(SWAPS),6)
        self.assertEqual(self.counts-self.grok,Counter({"Into the Flood Maw":1}))
        self.assertEqual(self.grok-self.counts,Counter({"Preordain":1}))

    def test_full_selected_oracle_legal_color_identity(self):
        self.assertEqual(self.o["candidate_raw_sha256"],RAW)
        self.assertEqual(self.o["baseline_raw_sha256"],BASE_RAW)
        self.assertEqual(self.o["physical_cards"],100)
        self.assertEqual(self.o["distinct_names"],100)
        self.assertEqual(self.o["project_exceptions"],[])
        self.assertTrue(self.o["official_commander_legal_all"])
        self.assertTrue(self.o["grixis_color_identity_all"])
        self.assertEqual(len(self.o["cards"]),100)
        self.assertEqual(set(self.cards),set(self.counts))
        for n,c in self.cards.items():
            with self.subTest(name=n):
                self.assertEqual(c["quantity"],1)
                self.assertEqual(c["commander_legality"],"legal")
                self.assertLessEqual(set(c["color_identity"]),{"U","B","R"})
                self.assertTrue(c["oracle_id"])
                self.assertIsNotNone(c["oracle_text"])
                self.assertTrue(c["source"])

    def test_lands_rocks_gamechangers_bracket(self):
        self.assertEqual(self.o["normal_lands"],30)
        self.assertEqual(sum("Land" in c["type_line"] for c in self.cards.values()),30)
        self.assertEqual(len(ROCKS),13)
        self.assertEqual(ROCKS & set(self.counts),ROCKS)
        self.assertEqual(len(self.o["game_changers"]),20)
        self.assertEqual({n for n,c in self.cards.items() if c["game_changer"]},set(self.o["game_changers"]))

    def test_commander_restricted_mana_and_saved_combos(self):
        self.assertIn("Spend this mana only to cast instant and/or sorcery spells",
            self.cards["Cormela, Glamour Thief"]["oracle_text"])
        self.assertIn("When Cormela dies",self.cards["Cormela, Glamour Thief"]["oracle_text"])
        self.assertIn("Untap up to three lands",self.cards["Frantic Search"]["oracle_text"])
        self.assertIn("except it has haste",self.cards["Twinflame"]["oracle_text"])
        self.assertIn("Spells you control can't be countered",self.cards["Hexing Squelcher"]["oracle_text"])
        self.assertIn("next spell you cast this turn can't be countered",self.cards["Mistrise Village"]["oracle_text"])
        s=json.loads(SPELLBOOK.read_text(encoding="utf-8"))
        self.assertEqual((len(s["baseline"]["included"]),len(s["candidate"]["included"])),(23,25))
        self.assertNotIn("Preordain",json.dumps(s["candidate"]["included"]))

    def test_into_flood_maw_gift_opponent_only_and_one_mana(self):
        c=self.cards["Into the Flood Maw"]
        self.assertEqual(c["mana_cost"],"{U}")
        self.assertIn("Gift a tapped Fish",c["oracle_text"])
        self.assertIn("target nonland permanent an opponent controls",c["oracle_text"])
        self.assertIn("If the gift was promised",c["oracle_text"])
        self.assertNotIn("you control",c["oracle_text"])

    def test_nonapproval_review_tradeoffs_and_floor_not_cap(self):
        s=REVIEW.read_text(encoding="utf-8")
        self.assertIn("NOT OWNER APPROVED",s)
        self.assertIn("NOT CANONICAL",s)
        self.assertIn(RAW,s)
        for word in ("Snap","Abrade","Preordain","Burnt Offering","Dramatic Reversal","GrokBot"):
            self.assertIn(word,s)
        self.assertIn("not padding",s)
        self.assertIn("non-independent",s)
        self.assertIn("no new formal M6 J",s)

if __name__=="__main__": unittest.main()
