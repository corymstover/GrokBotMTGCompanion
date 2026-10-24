"""Source-bound independent Edea M7 Rev2 research only; never confers owner approval."""
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import unittest

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"data/grixis/m7/baseline_sources/Edea__Possessed_Sorceress_approved_source_2026-10-14.txt"
CAND=ROOT/"data/grixis/m7/candidate_lists/Edea__Possessed_Sorceress_ChatGPT_M7_Rev2_20261023.txt"
ORACLE=ROOT/"data/grixis/m7/decision_reviews/Edea__Possessed_Sorceress_ChatGPT_M7_Rev2_Oracle_Selected_20261023.json"
REVIEW=ROOT/"data/grixis/m7/decision_reviews/Edea__Possessed_Sorceress_ChatGPT_M7_Rev2_Independent_20261023.md"
OLD="fd560a9b0777088b3ad1684ded030566c894faa206ddf6763b74d95d82c532e4"
EXACT="a039a79c6205c3dc61e0e237816d0d6b0168061b850cb8ca4a598483150b3f54"
COMMANDER="Edea, Possessed Sorceress"
SWAPS={
  "Aggravated Assault":"Mass Mutiny",
  "Kaya's Ghostform":"Zara, Renegade Recruiter",
  "Hall of Echoes":"Shipwreck Marsh",
  "Geyadrone Dihada":"Village Rites",
  "Combat Celebrant":"Seize the Spotlight",
}
REPEATABLE_KEEPS={
 "Evereth, Viceroy of Plunder",
 "High Market",
 "Ayara, Widow of the Realm // Ayara, Furnace Queen",
 "Ashnod's Altar",
 "Phyrexian Altar",
 "Phyrexian Tower",
 "Goblin Bombardment",
 "Illuminor Szeras",
 "Viscera Seer",
 "Warren Soultrader",
}
GC={"Ancient Tomb","Demonic Tutor","Fierce Guardianship"}
ROCKS={"Arcane Signet","Fellwar Stone","Sol Ring","Talisman of Creativity",
       "Talisman of Dominance","Talisman of Indulgence"}


def parse(path):
    count=Counter()
    lines=path.read_text(encoding="utf-8").splitlines()
    for i,line in enumerate(lines):
        m=re.fullmatch(r"(\d+)x (.+?)(?: \[Commander\])?",line)
        assert m is not None,(i,line)
        name=m.group(2)
        assert (i==0)==(name==COMMANDER),(i,name)
        if i==0:
            assert line=="1x Edea, Possessed Sorceress [Commander]"
        else:
            assert "[Commander]" not in line
        count[name]+=int(m.group(1))
    return count,lines


class EdeaRev2Research(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base,cls.old_lines=parse(BASE)
        cls.cand,cls.lines=parse(CAND)
        cls.oracle=json.loads(ORACLE.read_text(encoding="utf-8"))
        cls.cards={x["name"]:x for x in cls.oracle["cards"]}
        cls.review=REVIEW.read_text(encoding="utf-8")

    def test_exact_raw_sha_provenance_and_status(self):
        self.assertEqual(hashlib.sha256(BASE.read_bytes()).hexdigest(),OLD)
        self.assertEqual(hashlib.sha256(CAND.read_bytes()).hexdigest(),EXACT)
        self.assertEqual(self.oracle["baseline_raw_sha256"],OLD)
        self.assertEqual(self.oracle["candidate_raw_sha256"],EXACT)
        self.assertIn("NOT_OWNER_APPROVED",self.oracle["status"])
        self.assertIn("NOT CANONICAL",self.review)

    def test_100_physical_94_unique_and_basics(self):
        self.assertEqual(sum(self.cand.values()),100)
        self.assertEqual(len(self.cand),94)
        self.assertEqual(len(self.lines),94)
        self.assertEqual(self.cand[COMMANDER],1)
        self.assertEqual({n:q for n,q in self.cand.items() if q>1},
                         {"Island":3,"Mountain":3,"Swamp":3})
        self.assertEqual(self.oracle["physical_cards"],100)
        self.assertEqual(self.oracle["distinct_names"],94)

    def test_five_changes_owner_keeps_and_outlets(self):
        self.assertEqual(set(self.cand)-set(self.base),set(SWAPS))
        self.assertEqual(set(self.base)-set(self.cand),set(SWAPS.values()))
        for n in REPEATABLE_KEEPS:
            with self.subTest(keep=n):
                self.assertEqual(self.base[n],1)
                self.assertEqual(self.cand[n],1)
        self.assertIn("Evereth, Viceroy of Plunder",self.review)
        self.assertIn("High Market",self.review)
        self.assertIn("Ayara",self.review)
        self.assertIn("not owner approved",self.oracle["status"].replace("_"," ").lower())

    def test_archived_legal_oracle_identity_and_game_changers(self):
        self.assertEqual(set(self.cand),set(self.cards))
        self.assertEqual(len(self.cards),94)
        for n,q in self.cand.items():
            with self.subTest(card=n):
                v=self.cards[n]
                self.assertEqual(v["quantity"],q)
                self.assertEqual(v["commander_legality"],"legal")
                self.assertTrue(v["oracle_id"] and v["oracle_text"] and v["source"])
                self.assertTrue(set(v["color_identity"]) <= {"U","B","R"})
        self.assertEqual(self.oracle["project_exceptions"],[])
        self.assertEqual({n for n,c in self.cards.items() if c["game_changer"]},GC)
        self.assertEqual(set(self.oracle["game_changers"]),GC)

    def test_35_lands_and_six_rocks(self):
        land_count=sum(c["quantity"] for c in self.cards.values()
                       if "Land" in c["type_line"].split(" — ")[0])
        self.assertEqual(land_count,35)
        self.assertEqual(self.oracle["lands"],35)
        self.assertEqual(set(self.cand)&ROCKS,ROCKS)
        self.assertEqual(set(self.oracle["mana_rocks"]),ROCKS)
        self.assertNotIn("Shipwreck Marsh",self.cand)
        self.assertIn("Hall of Echoes",self.cand)

    def test_actual_extra_combat_ghostform_and_hall_text(self):
        text=lambda n:self.cards[n]["oracle_text"]
        self.assertIn("At the beginning of combat on your turn",text(COMMANDER))
        self.assertIn("Whenever a creature you control but don't own dies",text(COMMANDER))
        self.assertIn("Activate only as a sorcery",text("Aggravated Assault"))
        self.assertIn("there is an additional combat phase",text("Aggravated Assault"))
        self.assertIn("If this creature hasn't been exerted",text("Combat Celebrant"))
        self.assertIn("after this phase, there is an additional combat phase",text("Combat Celebrant"))
        self.assertIn("When enchanted permanent dies or is put into exile",text("Kaya's Ghostform"))
        self.assertIn("under your control",text("Kaya's Ghostform"))
        self.assertIn("The \"legend rule\" doesn't apply",text("Hall of Echoes"))
        self.assertIn("This land becomes a copy of target creature",text("Hall of Echoes"))
        self.assertIn("Gain control of target creature or planeswalker until end of turn",text("Geyadrone Dihada"))
        self.assertIn("Put a corruption counter",text("Geyadrone Dihada"))
        self.assertIn("Ghostform's death trigger",self.review)
        self.assertIn("win rate",self.review)

if __name__=="__main__":
    unittest.main()
