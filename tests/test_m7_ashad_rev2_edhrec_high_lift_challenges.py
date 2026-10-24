"""Focused primary-Oracle, hash, and no-padding checks for two high-lift Ashad M7 challengers.
These lists are *alternatives* only. They cannot be approved/locked by this test.
"""
import hashlib
import json
import unittest
from collections import Counter
from pathlib import Path

R=Path(__file__).resolve().parents[1]
NINE=R/"data/grixis/m7/candidate_lists/Ashad__the_Lone_Cyberman_ChatGPT_Rev2_Nine_Research.txt"
LIB=R/"data/grixis/m7/research_challengers/Ashad__the_Lone_Cyberman_ChatGPT_Liberator_Over_Kappa_Challenge.txt"
TECH=R/"data/grixis/m7/research_challengers/Ashad__the_Lone_Cyberman_ChatGPT_Technomancer_Over_Kappa_Challenge.txt"
SNAP=R/"data/grixis/m6/oracle_snapshots/Ashad__the_Lone_Cyberman_M7_Rev2_Scryfall_20261023.json"
EXTRA=R/"data/grixis/m7/research_challengers/Ashad__the_Lone_Cyberman_ChatGPT_high_lift_direct_sources.json"
H={
    "NINE":"1a9e875a06971734d7bd7211b3338cb888a3f8135c88530bab7e9e8544402704",
    "LIB":"352911498345e78bd55773f4c9d1c49d05599610d5fc806f7b779c85eb5f6267",
    "TECH":"afdd6678f2d3e58555bdf67287a040e240057ab488de82fb1625a7dc62593515",
}
BASICS={"Island","Mountain","Swamp"}

def parsed(path):
    lines=path.read_text(encoding="utf-8").splitlines()
    names=Counter()
    for line in lines:
        number,raw=line.split("x ",1)
        names[raw.removesuffix(" [Commander]")]+=int(number)
    return lines,names

class AshadHighLiftAlternatives(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        original=json.loads(SNAP.read_text(encoding="utf-8"))
        extra=json.loads(EXTRA.read_text(encoding="utf-8"))
        cls.sourced={x["name"]:x for x in original["cards"]+extra["cards"]}
        cls.extra={x["name"]:x for x in extra["cards"]}

    def test_exact_100_full_lists_singleton_and_no_pool_illegality(self):
        for key,path in (("NINE",NINE),("LIB",LIB),("TECH",TECH)):
            with self.subTest(key=key):
                self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(),H[key])
                lines,cards=parsed(path)
                self.assertEqual(lines[0],"1x Ashad, the Lone Cyberman [Commander]")
                self.assertEqual((len(lines),len(cards),sum(cards.values())),(95,95,100))
                self.assertEqual({n:q for n,q in cards.items() if q>1},
                                 {"Island":3,"Swamp":3,"Mountain":2})
                self.assertTrue(all(q==1 or n in BASICS for n,q in cards.items()))
                for n in cards:
                    self.assertIn(n,self.sourced)
                    c=self.sourced[n]
                    self.assertEqual(c["commander_legality"],"legal")
                    self.assertTrue(set(c["color_identity"]) <= {"U","B","R"})

    def test_one_for_one_challenges_not_falsely_selected(self):
        _,base=parsed(NINE)
        for path,replacement in ((LIB,"Liberator, Urza's Battlethopter"),
                                 (TECH,"Technomancer")):
            _,candidate=parsed(path)
            self.assertEqual(set((candidate-base).elements()),{replacement})
            self.assertEqual(set((base-candidate).elements()),{"Kappa Cannoneer"})
            self.assertIn("Ichor Wellspring",candidate)
            self.assertIn("Unwinding Clock",candidate)
            self.assertIn("Marionette Master",candidate)

    def test_direct_oracle_and_real_tradeoff(self):
        self.assertEqual(set(self.extra),{"Liberator, Urza's Battlethopter","Technomancer"})
        lib=self.extra["Liberator, Urza's Battlethopter"]
        tech=self.extra["Technomancer"]
        self.assertEqual(lib["oracle_id"],"798a4a6f-7443-4e8e-afcb-0a694fdfcbb3")
        self.assertEqual(tech["oracle_id"],"3f97541e-34f3-4f7f-8ac2-7167b2ec9b33")
        self.assertIn("Legendary Artifact Creature",lib["type_line"])
        self.assertIn("as though they had flash",lib["oracle_text"])
        self.assertIn("When this creature enters, mill three cards",tech["oracle_text"])
        self.assertEqual(tech["mana_cost"],"{5}{B}{B}")
        self.assertEqual({n for n,c in self.sourced.items()
                          if n in parsed(NINE)[1] and c["game_changer"]},
                         {"Cyclonic Rift","Demonic Tutor","Fierce Guardianship",
                          "Ancient Tomb","Mishra's Workshop"})
        for n in self.extra:
            self.assertEqual(self.extra[n]["commander_legality"],"legal")
            self.assertTrue(self.extra[n]["source_api"].startswith("https://api.scryfall.com/cards/named?exact="))

if __name__=="__main__":
    unittest.main()
