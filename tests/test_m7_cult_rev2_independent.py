"""Independent Cult of Skaro M7 Rev2 nine-swap source-bound finite checks; NOT owner approval."""
import hashlib
import json
from collections import Counter
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
D="Cult_of_Skaro"
BASE=ROOT/f"data/grixis/m7/baseline_sources/{D}_approved_source_2026-10-14.txt"
GROK=ROOT/f"data/grixis/m7/candidate_lists/{D}.txt"
CAND=ROOT/f"data/grixis/m7/chatgpt_final_candidates/{D}_M7_Rev2_Approval_Candidate_20261023.txt"
SOURCE=ROOT/f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json"
EXTRA=ROOT/f"data/grixis/m7/research_challengers/{D}_M7_Rev2_Addon_Scryfall_20261023.json"
HASH="e7c264409bd23bd6b3dc02548f555e3f64f2d2d11cc0430d61f49cbf452a1e3d"
BASE_HASH="4c221e5be0439338823ef621cd91706da8d405129cf6f5a41de36a83b875ef3b"
GROK_HASH="8b765d85649db64607c508bb3535466673593768ce729a9087a0260dc512624d"
ADDS=("Karlach, Fury of Avernus","Kindred Discovery","Hammer of Purphoros",
      "Shaun, Father of Synths","Quantum Misalignment","Skorpekh Lord",
      "Reverse the Polarity","Otawara, Soaring City","Takenuma, Abandoned Mire")
CUTS=("Cybermen Squadron","Canoptek Spyder","Adaptive Omnitool",
      "Thopter Spy Network","Anrakyr the Traveller","Baleful Strix",
      "Desynchronization","Island","Swamp")
BASICS={"Island","Mountain","Swamp"}
ROCKS=("Sol Ring","Mana Vault","Mox Opal","Arcane Signet","Dimir Signet",
       "Fellwar Stone","Talisman of Creativity","Talisman of Dominance",
       "Talisman of Indulgence")
REDUCERS=("Etherium Sculptor","Enthusiastic Mechanaut","Shuri, Wakandan Inventor")


def parse(path):
    out=Counter()
    lines=path.read_text(encoding="utf-8").splitlines()
    for i,line in enumerate(lines):
        q,name=line.split("x ",1)
        if i==0:
            assert name=="Cult of Skaro [Commander]"
            name=name.removesuffix(" [Commander]")
        else:
            assert "[Commander]" not in name
        out[name]+=int(q)
    return lines,out


class TestCultM7Rev2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lines,cls.cand=parse(CAND)
        _,cls.base=parse(BASE)
        _,cls.first=parse(GROK)
        a=json.loads(SOURCE.read_text(encoding="utf-8"))
        b=json.loads(EXTRA.read_text(encoding="utf-8"))
        cls.cards={c["name"]:c for c in a["cards"]+b["cards"]}
        cls.extra=b

    def test_raw_fingerprints_and_100(self):
        self.assertEqual(hashlib.sha256(CAND.read_bytes()).hexdigest(),HASH)
        self.assertEqual(hashlib.sha256(BASE.read_bytes()).hexdigest(),BASE_HASH)
        self.assertEqual(hashlib.sha256(GROK.read_bytes()).hexdigest(),GROK_HASH)
        self.assertTrue(CAND.read_bytes().endswith(b"\n"))
        self.assertEqual(self.lines[0],"1x Cult of Skaro [Commander]")
        self.assertEqual((len(self.lines),len(self.cand),sum(self.cand.values())),(96,96,100))
        self.assertEqual((self.cand["Island"],self.cand["Mountain"],self.cand["Swamp"]),(2,3,2))
        for n,q in self.cand.items():
            if n not in BASICS:
                self.assertEqual(q,1,n)

    def test_nine_exact_positive_delta_and_preserved_synergies(self):
        self.assertEqual(sorted((self.cand-self.base).elements()),sorted(ADDS))
        self.assertEqual(sorted((self.base-self.cand).elements()),sorted(CUTS))
        for n in ("Cult of Skaro","The Master, Multiplied","Etherium Sculptor",
                  "Shaun, Father of Synths","Auton Soldier","Dalek Squadron",
                  "Karlach, Fury of Avernus","Kindred Discovery","Hammer of Purphoros",
                  "Aggravated Assault","Sword of Feast and Famine","Brudiclad, Telchor Engineer",
                  "Roaming Throne","Scientist Supreme of A.I.M.","Strionic Resonator"):
            self.assertEqual(self.cand[n],1,n)
        self.assertEqual(self.cand["Thopter Spy Network"],0)
        self.assertEqual(self.cand["Baleful Strix"],0)

    def test_oct23_source_identity_legality_and_gc(self):
        self.assertEqual(self.extra["candidate_raw_sha256"],HASH)
        self.assertEqual(len(self.extra["cards"]),2)
        self.assertEqual(set(self.cand)-set(self.cards),set())
        for n in self.cand:
            c=self.cards[n]
            self.assertEqual(c["commander_legality"],"legal",n)
            self.assertTrue(set(c["color_identity"]) <= {"U","B","R"},n)
            self.assertTrue(c["oracle_id"],n)
            self.assertIsNotNone(c["oracle_text"],n)
        gcs={n for n in self.cand if self.cards[n]["game_changer"]}
        self.assertEqual(gcs,{"Cyclonic Rift","Fierce Guardianship","Mana Vault"})

    def test_lands_rocks_reducers_and_unmodified_sources(self):
        lands=sum(q for n,q in self.cand.items() if "Land" in self.cards[n]["type_line"])
        self.assertEqual(lands,34)
        self.assertEqual(sum(self.cand[n] for n in ROCKS),9)
        self.assertEqual(sum(self.cand[n] for n in REDUCERS),3)
        for n,c in (("Otawara, Soaring City","U"),("Takenuma, Abandoned Mire","B")):
            rec=self.cards[n]
            self.assertEqual(rec["color_identity"],[c])
            self.assertEqual(rec["type_line"],"Legendary Land")
            self.assertIn("{T}: Add {"+c+"}",rec["oracle_text"])
            self.assertIn("Channel —",rec["oracle_text"])
            self.assertIn("less to activate for each legendary creature",rec["oracle_text"])

    def test_master_synth_and_myriad_rules_no_false_entry_trigger(self):
        cult=self.cards["Cult of Skaro"]["oracle_text"]
        self.assertIn("Whenever Cult of Skaro attacks, choose one at random",cult)
        master=self.cards["The Master, Multiplied"]["oracle_text"]
        self.assertIn("Triggered abilities you control can't cause you to sacrifice or exile creature tokens you control",master)
        shaun=self.cards["Shaun, Father of Synths"]["oracle_text"]
        self.assertIn("tapped and attacking token",shaun)
        self.assertIn("except it's not legendary",shaun)
        self.assertIn("When Shaun leaves the battlefield, exile all Synth tokens you control",shaun)
        auton=self.cards["Auton Soldier"]["oracle_text"]
        self.assertIn("has myriad",auton)
        self.assertIn("Exile the tokens at end of combat",auton)
        k=self.cards["Karlach, Fury of Avernus"]["oracle_text"]
        self.assertIn("if it's the first combat phase",k)
        self.assertIn("additional combat phase",k)
        self.assertIn("Creatures you control have haste",self.cards["Hammer of Purphoros"]["oracle_text"])

    def test_rebound_trigger_daleks_and_optional_finisher(self):
        quantum=self.cards["Quantum Misalignment"]["oracle_text"]
        self.assertIn("except it isn't legendary",quantum)
        self.assertIn("Rebound",quantum)
        kindred=self.cards["Kindred Discovery"]["oracle_text"]
        self.assertIn("Whenever a creature you control of the chosen type enters or attacks",kindred)
        reverse=self.cards["Reverse the Polarity"]
        self.assertEqual(reverse["mana_cost"],"{1}{U}{U}")
        self.assertIn("Counter all other spells",reverse["oracle_text"])
        self.assertIn("Creatures can't be blocked this turn",reverse["oracle_text"])
        self.assertIn("Activate only as a sorcery",self.cards["Aggravated Assault"]["oracle_text"])

if __name__=="__main__":
    unittest.main()
