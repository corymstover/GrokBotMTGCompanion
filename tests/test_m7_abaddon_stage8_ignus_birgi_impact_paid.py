"""Abaddon Stage8: newly sourced off-ranking Ignus/Birgi/Impact Tremors loop.

Finite payable line and complete research 100-card comparisons only.
Not a claim of owner readiness or gameplay dominance.
"""
from collections import Counter
from pathlib import Path
import hashlib
import json
import unittest

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"data/grixis/m7/candidate_lists/Abaddon_the_Despoiler_rev2.txt"
REPORT=ROOT/"data/grixis/m7/research_challengers/Abaddon_the_Despoiler_stage8_impact_tremors_ignus_payable_review_20261022.json"
NEW_ORACLE=ROOT/"data/grixis/m7/research_challengers/Abaddon_the_Despoiler_stage8_nine_offranking_Scryfall_20261022.json"
BASE_ORACLE=ROOT/"data/grixis/m6/oracle_snapshots/Abaddon_the_Despoiler_Rev2_Scryfall_20261022.json"
BASICS={"Island","Mountain","Swamp"}


def physical(path):
    contents=path.read_bytes()
    lines=contents.decode().splitlines()
    cards=Counter()
    for line in lines:
        number,name=line.split("x ",1)
        assert number.isdigit()
        cards[name.removesuffix(" [Commander]")]+=int(number)
    return contents, lines, cards


def paid_ignus_birgi_impact(cycles, starting_red=1, opponents=3):
    """Source-paid (uninterrupted) finite trace; other resources identical.

    Ignus activation: R + return it to own hand for CC R on resolution.
    Ignus recast: CC R, Birgi trigger: R, Impact ETB: 1 each opponent.
    """
    red=starting_red
    colorless=0
    ignus_on_battlefield=True
    damage_per_opponent=[0]*opponents
    cast_events=0
    for _ in range(cycles):
        if red<1 or not ignus_on_battlefield:
            raise AssertionError("Cannot pay an Ignus bounce")
        red-=1
        ignus_on_battlefield=False
        colorless+=2
        red+=1
        if colorless<2 or red<1:
            raise AssertionError("Cannot pay {2}{R} for Ignus")
        colorless-=2
        red-=1
        # Birgi's real spell CAST trigger, before Ignus resolves.
        red+=1
        cast_events+=1
        ignus_on_battlefield=True
        # When Ignus enters, Impact Tremors' ETB trigger resolves.
        damage_per_opponent=[d+1 for d in damage_per_opponent]
    return {"red_float":red,"colorless_float":colorless,
            "ignus_on_battlefield":ignus_on_battlefield,
            "cast_events":cast_events,"damage_per_opponent":damage_per_opponent}


class AbaddonImpactStage8(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report=json.loads(REPORT.read_text(encoding="utf-8"))
        cls.source=json.loads(NEW_ORACLE.read_text(encoding="utf-8"))
        cls.base_oracle=json.loads(BASE_ORACLE.read_text(encoding="utf-8"))["oracle_snapshot"]
        cls.cards=cls.source["oracle_cards"]

    def test_all_nine_offranking_source_cards_legal_and_real(self):
        self.assertEqual(self.source["not_found"],[])
        self.assertEqual(len(self.cards),9)
        for name, card in self.cards.items():
            self.assertEqual(name,card["name"])
            self.assertEqual(card["commander_legality"],"legal")
            self.assertTrue(set(card["color_identity"]) <= set("UBR"))
            self.assertTrue(card["oracle_text"])
        self.assertIn("Whenever a creature you control enters",
                      self.cards["Impact Tremors"]["oracle_text"])
        self.assertEqual(self.cards["Impact Tremors"]["mana_cost"],"{1}{R}")
        self.assertIn("At the beginning of your first main phase",
                      self.cards["Sanctum of Stone Fangs"]["oracle_text"])
        self.assertIn("At the beginning of your upkeep",
                      self.cards["Creeping Bloodsucker"]["oracle_text"])
        self.assertIn("Whenever an artifact you control enters",
                      self.cards["Reckless Fireweaver"]["oracle_text"])
        self.assertIn("Whenever you create or sacrifice a token",
                      self.cards["Mirkwood Bats"]["oracle_text"])

    def test_exact_current_source_and_finite_paid_combo(self):
        a=self.base_oracle
        self.assertIn("Whenever you cast a spell, add {R}",
                      a["Birgi, God of Storytelling // Harnfel, Horn of Bounty"]["oracle_text"])
        ignus=a["Grinning Ignus"]["oracle_text"]
        self.assertIn("{R}, Return this creature to its owner's hand",ignus)
        self.assertIn("Add {C}{C}{R}",ignus)
        self.assertIn("Activate only as a sorcery",ignus)
        one=paid_ignus_birgi_impact(1)
        self.assertEqual(one["red_float"],1)
        self.assertEqual(one["colorless_float"],0)
        self.assertEqual(one["damage_per_opponent"],[1,1,1])
        three=paid_ignus_birgi_impact(3)
        self.assertEqual(three["cast_events"],3)
        self.assertEqual(three["red_float"],1)
        self.assertEqual(three["damage_per_opponent"],[3,3,3])
        # Forty iterations are only possible if all required cards survive and
        # no opponent stops the sequence: no measured game win rate.
        self.assertEqual(paid_ignus_birgi_impact(40)["damage_per_opponent"],[40,40,40])

    def test_whole_100_research_only_and_named_cut_cost(self):
        r=self.report
        self.assertFalse(r["owner_ready"])
        self.assertTrue(r["not_m6_certified"])
        self.assertTrue(r["deck3_on_hold"])
        self.assertTrue(r["status"].startswith("RESEARCH_ONLY"))
        basebytes,baselines,base=physical(BASE)
        self.assertEqual(hashlib.sha256(basebytes).hexdigest(),r["canonical"]["raw_sha256"])
        self.assertEqual(sum(base.values()),100)
        self.assertEqual(len(r["complete_100_research_variants"]),3)
        for p in r["complete_100_research_variants"]:
            raw,lines,cards=physical(ROOT/p["path"])
            self.assertEqual(hashlib.sha256(raw).hexdigest(),p["sha256"])
            self.assertEqual(lines[0],baselines[0])
            self.assertEqual(sum(cards.values()),100)
            self.assertTrue(all(n in BASICS or q==1 for n,q in cards.items()))
            self.assertEqual(sorted((cards-base).elements()),sorted(p["adds"]))
            self.assertEqual(sorted((base-cards).elements()),sorted(p["cuts"]))
            self.assertIn("Call Forth the Tempest",cards)
            self.assertIn("Pact of Negation",cards)
            self.assertIn("Pyroblast",cards)
            for name in cards:
                item=self.base_oracle.get(name,self.cards.get(name))
                self.assertIsNotNone(item,name)
                self.assertEqual(item["commander_legality"],"legal",name)
                self.assertTrue(set(item["color_identity"])<=set("UBR"),name)
        self.assertIn("Aggravated Assault",
                      r["baseline_impact_assault_competition"]["cut"])
        self.assertIn("The Ruinous Powers",
                      r["baseline_impact_ruinous_competition"]["cut"])
        self.assertTrue(r["governance"]["minimum_five_owner_floor_unmet"])

    def test_trigger_timing_not_assumed_immediate_or_immune(self):
        self.assertTrue(all(x["disposition"] in {
            "SELECT_ADD","REJECT","RETAIN_ALTERNATIVE","EXCLUDE_INVALID"
        } for x in self.report["nine_source_judgments"]))
        self.assertEqual(len(self.report["nine_source_judgments"]),9)
        intro=self.report["exact_payable_ignus_tremors_loop"]
        self.assertTrue(any("empty stack" in x.lower()
                            for x in intro["prerequisites"]))
        self.assertTrue(any("Rule of Law" in x
                            for x in intro["interaction_notes"]))
        self.assertTrue(any("Abaddon X" in x
                            for x in intro["interaction_notes"]))


if __name__=="__main__":
    unittest.main()
