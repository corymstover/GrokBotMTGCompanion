"""Focused NON-APPROVAL structural/source and mana checks for Ashad ChatGPT M7 Rev2 research options."""
import hashlib
import json
import math
import unittest
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"data/grixis/m7/baseline_sources/Ashad_the_Lone_Cyberman_approved_source_2026-10-13.txt"
GROK=ROOT/"data/grixis/m7/candidate_lists/Ashad__the_Lone_Cyberman.txt"
NINE=ROOT/"data/grixis/m7/candidate_lists/Ashad__the_Lone_Cyberman_ChatGPT_Rev2_Nine_Research.txt"
TEN=ROOT/"data/grixis/m7/research_challengers/Ashad__the_Lone_Cyberman_ChatGPT_Rev2_Ten_Patrol_Alternative.txt"
SOURCES=ROOT/"data/grixis/m7/research_challengers/Ashad__the_Lone_Cyberman_ChatGPT_Rev2_new_lands_primary_sources.json"
ORIGINAL_SNAPSHOT=ROOT/"data/grixis/m6/oracle_snapshots/Ashad__the_Lone_Cyberman_M7_Scryfall_20261023.json"
SNAPSHOT=ROOT/"data/grixis/m6/oracle_snapshots/Ashad__the_Lone_Cyberman_M7_Rev2_Scryfall_20261023.json"
EXPECTED={"BASE":"087e34c2127859111fc08f8d9ec7d66cd3495537cc571d88e829fd27d2823e25","GROK":"dfd1158c79668c2dcd85137219bd00bdc75cd855697cf31dfb9b5ff93552597d","NINE":"1a9e875a06971734d7bd7211b3338cb888a3f8135c88530bab7e9e8544402704","TEN":"daf54f692a508db867d84ef9c047897cfc3669f54c841b23a273af4de925558b"}
ADDS_NINE=["Skullclamp","Piggy Bank","Razorlash Transmogrant","Necron Deathmark","Royal Warden","Mishra's Workshop","Ancient Tomb","City of Brass","Mana Confluence"]
CUTS_NINE=["Fellwar Stone","Reckless Fireweaver","Thoughtcast","Noxious Gearhulk","Thopter Spy Network","Tezzeret, Master of the Bridge","Delete","Crumbling Necropolis","Shipwreck Marsh"]
BASICS={"Island","Mountain","Swamp"}
NEW={"Mishra's Workshop","Ancient Tomb","City of Brass","Mana Confluence"}

def count(path):
    lines=path.read_text(encoding="utf-8").splitlines()
    d=Counter()
    for line in lines:
        number,name=line.split("x ",1)
        assert number.isdecimal() and int(number)>0, line
        d[name.removesuffix(" [Commander]")]+=int(number)
    return lines,d

def p4(source_count):
    return sum(math.comb(source_count,i)*math.comb(99-source_count,10-i)
               for i in range(4,11))/math.comb(99,10)

class AshadRev2ResearchOnly(unittest.TestCase):
    def test_original_grok_and_two_options_exact_hashes_and_structure(self):
        for key,path in [("BASE",BASE),("GROK",GROK),("NINE",NINE),("TEN",TEN)]:
            with self.subTest(key=key):
                self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(),EXPECTED[key])
                lines,d=count(path)
                self.assertEqual(lines[0],"1x Ashad, the Lone Cyberman [Commander]")
                self.assertEqual((len(lines),len(d),sum(d.values())),(95,95,100))
                self.assertEqual(sum("[Commander]" in x for x in lines),1)
                self.assertEqual({k:v for k,v in d.items() if v>1},
                                 {"Island":3,"Mountain":2,"Swamp":3})
                self.assertTrue(all(v==1 or k in BASICS for k,v in d.items()))

    def test_exact_nine_and_ten_nonpadding_alternatives(self):
        _,before=count(BASE)
        for path,n in ((NINE,9),(TEN,10)):
            _,after=count(path)
            self.assertEqual(set((after-before).elements()),
                             set(ADDS_NINE)|({"Cyberman Patrol"} if n==10 else set()))
            self.assertEqual(set((before-after).elements()),
                             set(CUTS_NINE)|({"Ichor Wellspring"} if n==10 else set()))
            self.assertEqual(sum((after-before).values()),n)
            self.assertEqual(sum((before-after).values()),n)
            self.assertIn("Marionette Master",after)
            self.assertIn("Unwinding Clock",after)
            if n==9: self.assertIn("Ichor Wellspring",after)
            else: self.assertNotIn("Ichor Wellspring",after)

    def test_live_four_card_oracle_ids_and_116_source_pool_provenance(self):
        original=json.loads(ORIGINAL_SNAPSHOT.read_text(encoding="utf-8"))
        snap=json.loads(SNAPSHOT.read_text(encoding="utf-8"))
        sources=json.loads(SOURCES.read_text(encoding="utf-8"))
        self.assertEqual(original["candidate_raw_sha256"],EXPECTED["GROK"])
        self.assertEqual(snap["candidate_raw_sha256"],EXPECTED["NINE"])
        self.assertEqual(len(original["cards"]),112)
        self.assertEqual((snap["unique_names"],snap["cards_count"],len(snap["cards"])),(116,116,116))
        original_cards={c["name"]:c for c in original["cards"]}
        pool={c["name"]:c for c in snap["cards"]}
        supplement={c["name"]:c for c in sources["cards"]}
        self.assertEqual(set(pool)-set(original_cards),NEW)
        self.assertTrue(all(pool[k]==v for k,v in original_cards.items()),
                        "Historical 112-name source is preserved byte-for-byte by value")
        self.assertEqual(set(supplement),NEW)
        self.assertEqual({x for x in NEW if supplement[x]["game_changer"]},
                         {"Ancient Tomb","Mishra's Workshop"})
        expected_oracle_ids={
            "Mishra's Workshop":"ba284fe6-bb29-455c-8321-9714a0cdc05e",
            "Ancient Tomb":"23467047-6dba-4498-b783-1ebc4f74b8c2",
            "City of Brass":"f25351e3-539b-4bbc-b92d-6480acf4d722",
            "Mana Confluence":"d0ee5bdc-2b69-4b73-9a20-ffcc18783b29",
        }
        self.assertEqual(sources["status"],"LIVE_DIRECT_SCRYFALL_VERIFIED_RESEARCH_NOT_OWNER_APPROVAL")
        for name in NEW:
            with self.subTest(direct_scryfall=name):
                self.assertEqual(supplement[name]["oracle_id"],expected_oracle_ids[name])
                self.assertEqual(pool[name]["oracle_id"],expected_oracle_ids[name])
                self.assertEqual(pool[name]["oracle_text"],supplement[name]["oracle_text"])
                self.assertEqual(supplement[name]["color_identity"],[])
                self.assertEqual(supplement[name]["commander_legality"],"legal")
                self.assertTrue(supplement[name]["source"].startswith("https://scryfall.com/card/"))
                self.assertTrue(supplement[name]["source_api"].startswith("https://api.scryfall.com/cards/named?exact="))
        self.assertIn("only to cast artifact spells",pool["Mishra's Workshop"]["oracle_text"])
        self.assertIn("deals 2 damage to you",pool["Ancient Tomb"]["oracle_text"])
        self.assertIn("Whenever this land becomes tapped",pool["City of Brass"]["oracle_text"])
        self.assertIn("Pay 1 life",pool["Mana Confluence"]["oracle_text"])
        self.assertFalse(snap["all_commander_legal"])
        self.assertFalse(snap["grixis_identity_all"])
        self.assertTrue(snap["candidate_all_commander_legal"])
        self.assertTrue(snap["candidate_grixis_identity_all"])
        self.assertEqual(set(snap["pool_contains_ineligible_rejected_names"]),
                         {"Bio-Asset Allocator","Golos, Tireless Pilgrim"})
        self.assertEqual({name for name,c in pool.items() if c["commander_legality"]!="legal"},
                         {"Bio-Asset Allocator","Golos, Tireless Pilgrim"})
        review=(ROOT/"data/grixis/m7/decision_reviews/Ashad__the_Lone_Cyberman_ChatGPT_Rev2_mana_and_identity_review.md").read_text(encoding="utf-8")
        self.assertIn("direct live Scryfall JSON",review)
        for path in [NINE,TEN]:
            _,d=count(path)
            self.assertTrue(all(x not in d for x in snap["pool_contains_ineligible_rejected_names"]))
            for name in d:
                with self.subTest(candidate=path.name,card=name):
                    self.assertIn(name,pool)
                    self.assertEqual(pool[name]["commander_legality"],"legal")
                    self.assertTrue(set(pool[name]["color_identity"])<={"U","B","R"})
        self.assertEqual({n for n in count(NINE)[1] if pool[n]["game_changer"]},
                         {"Cyclonic Rift","Demonic Tutor","Fierce Guardianship",
                          "Ancient Tomb","Mishra's Workshop"})

    def test_bounded_static_source_mana_improvement_not_color_claim(self):
        full=json.loads(SNAPSHOT.read_text(encoding="utf-8"))
        direct={c["name"]:c for c in full["cards"]}
        supplement={c["name"]:c for c in json.loads(SOURCES.read_text(encoding="utf-8"))["cards"]}
        mana_rocks={"Arcane Signet","Rakdos Signet","Sol Ring","Talisman of Creativity",
                    "Talisman of Dominance","Talisman of Indulgence","Mox Opal",
                    "Cursed Mirror","Fellwar Stone"}
        expected=[(BASE,30,9,39),(GROK,30,8,38),(NINE,32,8,40),(TEN,32,8,40)]
        for path,land,rock,total in expected:
            _,d=count(path)
            landcount=sum(q for name,q in d.items() if "Land" in
                          (direct.get(name) or supplement.get(name))["type_line"])
            rockcount=sum(d[x] for x in mana_rocks)
            self.assertEqual((landcount,rockcount,landcount+rockcount),
                             (land,rock,total))
        self.assertAlmostEqual(p4(38),0.5828,places=4)
        self.assertAlmostEqual(p4(39),0.6099,places=4)
        self.assertAlmostEqual(p4(40),0.6363,places=4)

if __name__=="__main__":
    unittest.main()
