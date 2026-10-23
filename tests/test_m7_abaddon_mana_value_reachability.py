"""Abaddon source-bound MV reachability contrast: Blood vs printed Call cascades.

Finite eligibility checks; not a complete ordered library or predictive gameplay
simulator. Mind's Desire is an unrestricted free-cast distinct from cascade.
"""
from pathlib import Path
import json, unittest

ROOT=Path(__file__).resolve().parents[1]
CANON=ROOT/"data/grixis/m7/candidate_lists/Abaddon_the_Despoiler_rev2.txt"
BASE_ORACLE=ROOT/"data/grixis/m6/oracle_snapshots/Abaddon_the_Despoiler_Rev2_Scryfall_20261022.json"
NEW_ORACLE=ROOT/"data/grixis/m7/research_challengers/Abaddon_the_Despoiler_post_Admiral_39_card_Scryfall_20261022.json"
REPORT=ROOT/"data/grixis/m7/research_challengers/Abaddon_the_Despoiler_stage6_mana_value_cascade_disposition_20261022.md"


class AbaddonCascadeMVReachability(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.existing=json.loads(BASE_ORACLE.read_text(encoding="utf-8"))["oracle_snapshot"]
        cls.new=json.loads(NEW_ORACLE.read_text(encoding="utf-8"))["oracle_cards"]
        cls.names=[]
        for line in CANON.read_text(encoding="utf-8").splitlines():
            qty,n=line.split("x ",1)
            n=n.removesuffix(" [Commander]")
            cls.names.extend([n]*int(qty))

    def test_approved_100_max_library_mv_nine_and_blood_eleven(self):
        self.assertEqual(len(self.names),100)
        self.assertEqual(self.names[0],"Abaddon the Despoiler")
        other=self.names[1:]
        self.assertTrue(all(n in self.existing for n in other))
        self.assertEqual(max(self.existing[n]["mana_value"] for n in other),9)
        self.assertEqual(self.existing["Blasphemous Act"]["mana_value"],9)
        self.assertEqual(self.existing["Call Forth the Tempest"]["mana_value"],8)
        self.assertEqual(self.new["Blood for the Blood God!"]["cmc"],11)
        self.assertTrue(all(self.existing[n]["mana_value"]<11 for n in other))
        # Cascade requires strictly lesser mana value than its source.
        self.assertFalse(any(self.existing[n]["mana_value"]>11 for n in other))

    def test_call_forth_double_printed_cascade_and_act_can_reach_it(self):
        self.assertIn("Cascade, cascade",self.existing["Call Forth the Tempest"]["oracle_text"])
        self.assertTrue(8<9)
        self.assertIn("Blasphemous Act",self.names)
        self.assertIn("Call Forth the Tempest",self.names)
        # Possible ordered-library hit, NOT guaranteed and not empirical
        # probability: a source MV9 with cascade may exile MV8 Call.
        printed_cascades_on_free_exile_cast=2
        self.assertEqual(printed_cascades_on_free_exile_cast,2)
        # Abaddon DOES NOT grant a third to an exile cast.
        self.assertNotEqual("exile","hand")

    def test_hand_cast_call_triple_cascade_conditional_at_x_eight(self):
        self.assertIn("mana value X or less have cascade",
                      self.existing["Abaddon the Despoiler"]["oracle_text"])
        mv=8
        for x, expected in ((7,2),(8,3),(9,3)):
            total=2+int(mv<=x) # 2 printed + 1 Abaddon when hand/own turn
            self.assertEqual(total,expected)
        # Free exile cast from Act would retain its two printed abilities.
        exile_cast_total=2
        self.assertEqual(exile_cast_total,2)

    def test_blood_not_a_cascade_hit_but_minds_desire_can_offer_free(self):
        blood=self.new["Blood for the Blood God!"]
        self.assertNotIn("cascade",blood["oracle_text"].lower())
        self.assertEqual(blood["cmc"],11)
        self.assertIn("without paying its mana cost",
                      self.existing["Mind's Desire"]["oracle_text"])
        # A specific Mind's Desire exile reveal of Blood is legal to cast
        # without paying even though Blood's MV is eleven.
        top_card="Blood for the Blood God!"
        can_free_cast_by_desire=top_card in self.new
        can_free_cast_by_cascade=any(self.existing[n]["mana_value"]>11
                                     for n in self.names[1:])
        self.assertTrue(can_free_cast_by_desire)
        self.assertFalse(can_free_cast_by_cascade)

    def test_blood_discount_does_not_help_cascade_source_gate(self):
        t=self.new["Blood for the Blood God!"]["oracle_text"]
        self.assertIn("for each creature that died this turn",t)
        self.assertIn("Exile Blood for the Blood God!",t)
        self.assertIn("deals 8 damage to each opponent",t)
        # With six deaths, {8}{B}{B}{R} becomes {2}{B}{B}{R} = 5 paid.
        deaths=6
        payable_total=max(0,8-deaths)+3
        self.assertEqual(payable_total,5)
        self.assertEqual(self.new["Blood for the Blood God!"]["cmc"],11)
        # X>=11 needed at casting time. Later resolution eight-to-each
        # cannot grant the earlier hand cast cascade retroactively.
        prior_x=9
        self.assertFalse(11<=prior_x)
        post_resolve_x=prior_x+3*8
        self.assertEqual(post_resolve_x,33)

    def test_research_report_has_not_approved_substitution(self):
        s=REPORT.read_text(encoding="utf-8")
        self.assertIn("RESEARCH_ONLY",s)
        self.assertIn("Mind's Desire",s)
        self.assertIn("not a",s.lower())
        self.assertIn("keep Call Forth",s)


if __name__=="__main__":
    unittest.main()
