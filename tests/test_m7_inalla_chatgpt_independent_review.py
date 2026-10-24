"""Focused, source-bound independent Inalla M7 challenge: RESEARCH ONLY."""
import hashlib
import json
import re
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "data/grixis/m7/baseline_sources/Inalla__Archmage_Ritualist_approved_source_2026-10-14.txt"
TWO = ROOT / "data/grixis/m7/independent_candidates/Inalla__Archmage_Ritualist_M7_Two_Swap_Dualcaster_Pyroblast_20261024.txt"
THREE = ROOT / "data/grixis/m7/independent_candidates/Inalla__Archmage_Ritualist_M7_Three_Swap_Probe_Stress_20261024.txt"
REVIEW = ROOT / "data/grixis/m7/independent_reviews/Inalla__Archmage_Ritualist_M7_Adversarial_20261024.json"
MD = ROOT / "data/grixis/m7/independent_reviews/Inalla__Archmage_Ritualist_ChatGPT_Independent_20261024.md"
SNAP = ROOT / "data/grixis/m6/oracle_snapshots/Inalla__Archmage_Ritualist_M7_Scryfall_20261023.json"
SPELL = ROOT / "data/grixis/m7/research_challengers/Inalla__Archmage_Ritualist_CommanderSpellbook_20261023.json"
OLD = "81333ac71d483b667af968bf2ab221e1fa0de6edd7c2395170d15786e5b15fa3"
TWO_SHA = "5d182d9b9814fde5e04ec0687d7245bf3cd29c31d200c70a13f76e72bb932aef"
THREE_SHA = "b3ce0a3f6943889dd2bdfb0221a6daed4e07b338e5c3c5026bf1da0bc4e0ca26"


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def parsed(p):
    out=Counter()
    for line in p.read_text(encoding="utf-8").splitlines():
        m=re.fullmatch(r"(\d+)x (.+?)( \[Commander\])?",line)
        assert m, (p,line)
        out[m[2]]+=int(m[1])
    return out


class InallaIndependentM7Research(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.baseline=parsed(BASE);cls.two=parsed(TWO);cls.three=parsed(THREE)
        cls.review=json.loads(REVIEW.read_text(encoding="utf-8"))
        cls.oracle={c["name"]:c for c in json.loads(SNAP.read_text(encoding="utf-8"))["cards"]}
        cls.spell=json.loads(SPELL.read_text(encoding="utf-8"))

    def test_baseline_exact_historical_bytes_and_research_only_status(self):
        self.assertEqual(digest(BASE),OLD)
        self.assertFalse(BASE.read_bytes().endswith(b"\n"))
        self.assertFalse(self.review["owner_approved"])
        self.assertFalse(self.review["canonical_changed"])
        self.assertIn("RESEARCH_ONLY",self.review["status"])
        self.assertIn("RESEARCH_ONLY",MD.read_text(encoding="utf-8"))
        self.assertIn(OLD,MD.read_text(encoding="utf-8"))

    def test_two_exact_100_and_two_physical_swaps(self):
        self.assertEqual(digest(TWO),TWO_SHA)
        self.assertTrue(TWO.read_bytes().endswith(b"\n"))
        self.assertEqual(sum(self.two.values()),100)
        self.assertEqual(len(self.two),100)
        self.assertEqual(self.two["Inalla, Archmage Ritualist"],1)
        self.assertEqual(self.two-self.baseline,Counter({"Dualcaster Mage":1,"Pyroblast":1}))
        self.assertEqual(self.baseline-self.two,Counter({
            "Kefka, Court Mage // Kefka, Ruler of Ruin":1,"Red Elemental Blast":1}))

    def test_three_exact_100_and_three_physical_swaps(self):
        self.assertEqual(digest(THREE),THREE_SHA)
        self.assertTrue(THREE.read_bytes().endswith(b"\n"))
        self.assertEqual(sum(self.three.values()),100)
        self.assertEqual(len(self.three),100)
        self.assertEqual(self.three["Inalla, Archmage Ritualist"],1)
        self.assertEqual(self.three-self.baseline,
                         Counter({"Dualcaster Mage":1,"Pyroblast":1,"Gitaxian Probe":1}))
        self.assertEqual(self.baseline-self.three,
                         Counter({"Kefka, Court Mage // Kefka, Ruler of Ruin":1,
                                  "Red Elemental Blast":1,"Ragavan, Nimble Pilferer":1}))

    def test_all_cards_archived_legal_grixis_and_27_lands(self):
        for deck in (self.baseline,self.two,self.three):
            self.assertEqual(set(deck)-set(self.oracle),set())
            lands=0;gc=set()
            for n,q in deck.items():
                c=self.oracle[n]
                self.assertEqual(c["commander_legality"],"legal",n)
                self.assertTrue(set(c["color_identity"])<=set("UBR"),n)
                self.assertTrue(c["oracle_text"],n)
                if "Land" in c["type_line"]:lands+=q
                if c["game_changer"]:gc.add(n)
            self.assertEqual(lands,27)
            self.assertEqual(len(gc),18)
            self.assertEqual(deck["Spellseeker"],1)
            self.assertEqual(deck["Scholar of the Ages"],1)
            self.assertEqual(deck["Finale of Promise"],1)
            self.assertEqual(deck["Ruthless Technomancer"],1)
            self.assertEqual(deck["Bloodline Necromancer"],1)
            self.assertEqual(deck["Tainted Pact"],1)
            self.assertEqual(deck["Underworld Breach"],1)

    def test_dualcaster_real_spellcopy_and_source_combo_delta(self):
        self.assertIn("Flash",self.oracle["Dualcaster Mage"]["oracle_text"])
        self.assertIn("copy target instant or sorcery",
                      self.oracle["Dualcaster Mage"]["oracle_text"])
        self.assertIn("Saw in Half",self.two)
        self.assertIn("Essence Flux",self.two)
        alt=self.spell["alternatives"][
            "Inalla__Archmage_Ritualist_PassC_plus_DualcasterMage_minus_Kefka_20261023.txt"]
        before={c["id"] for c in self.spell["baseline"]["included"]}
        after={c["id"] for c in alt["included"]}
        self.assertEqual((len(before),len(after)),(16,18))
        self.assertEqual(after-before,{"147-500","147-4598"})

    def test_pyro_and_probe_qualifications_not_claimed_strict(self):
        pyro=self.oracle["Pyroblast"]["oracle_text"]
        reb=self.oracle["Red Elemental Blast"]["oracle_text"]
        probe=self.oracle["Gitaxian Probe"]["oracle_text"]
        self.assertIn("Counter target spell if it's blue",pyro)
        self.assertIn("Counter target blue spell",reb)
        self.assertIn("Draw a card.",probe)
        self.assertEqual(self.oracle["Gitaxian Probe"]["mana_cost"],"{U/P}")
        self.assertIn("2 life",probe)
        self.assertIn("create a Treasure token",
                      self.oracle["Ragavan, Nimble Pilferer"]["oracle_text"])

    def test_owner_gate_and_under_five_honest_swap_disposition(self):
        statuses={f["id"]:f["status"] for f in self.review["findings"]}
        self.assertIn("OWNER",statuses["dual"])
        self.assertIn("BORDERLINE",statuses["pyro"])
        self.assertIn("NOT_QUALITY_POSITIVE_PROVEN",statuses["probe"])
        self.assertTrue(all(not v["owner_presentable"] for v in self.review["alternatives"]))
        self.assertEqual({v["raw_sha256"] for v in self.review["alternatives"]},
                         {TWO_SHA,THREE_SHA})
        self.assertIn("five",self.review["constraints"].lower())

if __name__=="__main__":
    unittest.main()
