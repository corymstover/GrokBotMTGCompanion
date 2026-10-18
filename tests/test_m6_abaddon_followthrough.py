"""Cycle 94: independent failure-oriented Abaddon threshold/follow-through checks."""
import sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_m6_abaddon_followthrough as m

class TestFollowthrough(unittest.TestCase):
    def test_generic_payment_enumerates_colored_options(self):
        pay=m.legal_payments({"U":1,"B":2,"R":2,"C":3},{"U":1,"B":1,"R":1,"generic":2})
        self.assertTrue(any(m.legal_payments(p,{"B":1,"R":1,"generic":1}) for p in pay))
        self.assertEqual(m.legal_payments({"U":0,"B":1,"R":1,"C":1},{"U":1,"generic":1}),[])
    def test_colored_mana_after_commander(self):
        command={"U":1,"B":1,"R":1,"generic":2}
        spell={"B":1,"R":1,"generic":1}
        self.assertFalse(m.followup_after_commander({"U":1,"B":2,"R":2,"C":2},False,command,spell))
        self.assertTrue(m.followup_after_commander({"U":1,"B":2,"R":2,"C":3},False,command,spell))
        self.assertFalse(m.followup_after_commander({"U":1,"B":1,"R":1,"C":3},False,command,spell))
        self.assertTrue(m.followup_after_commander({"U":0,"B":1,"R":1,"C":1},True,command,spell))
    def test_printed_remains_without_abaddon(self):
        self.assertEqual(m.cascade_triggers("Bituminous Blast",0)["total_on_cast"],1)
        self.assertEqual(m.cascade_triggers("Bituminous Blast",5)["total_on_cast"],2)
        self.assertEqual(m.cascade_triggers("Bituminous Blast",54,origin="exile")["total_on_cast"],1)
        self.assertEqual(m.cascade_triggers("Bituminous Blast",54,own_turn=False)["total_on_cast"],1)
        self.assertEqual(m.cascade_triggers("Bituminous Blast",54,commander=False)["total_on_cast"],1)
        self.assertEqual(m.cascade_triggers("followup_mv3",3)["total_on_cast"],1)
        self.assertEqual(m.cascade_triggers("followup_mv3",2)["total_on_cast"],0)
    def test_tapped_source_destroyed_response_difference(self):
        base={"turn_cast":5,"activation_turn":6,"haste":False,"source_survives":True,
              "source":"Heartless Hidetsugu","response_remove_source":True}
        self.assertEqual(m.board_result(base,[40,39,31],40)["total_opponent_life_lost"],54)
        self.assertEqual(m.board_result({**base,"source":"Tree of Perdition"},[40,39,31],40)["total_opponent_life_lost"],0)
        self.assertEqual(m.board_result({**base,"source_survives":False},[40,39,31],40)["total_opponent_life_lost"],0)
        self.assertEqual(m.board_result({**base,"activation_turn":5},[40,39,31],40)["total_opponent_life_lost"],0)
    def test_data_rerun_and_no_promotion(self):
        d=m.run()
        self.assertEqual(len(d["board_results"]),8)
        self.assertEqual(len(d["printed_cascade_cases"]),24)
        self.assertFalse(d["effect_aware_deckwide_paired_test_executed"])
        self.assertFalse(d["full_phase_b_complete"])
        self.assertFalse(d["supports_improvement_claim"])
        self.assertFalse(any(d["authority"].values()))
        self.assertEqual(d["retained_engine_witnesses"]["Kessig Flamebreather"]["threshold_at_each_mv3_cast"],[0,3])
        self.assertTrue(d["retained_engine_witnesses"]["Birgi, God of Storytelling"]["available_to_pay_subsequent_spells_while_unspent"])
if __name__=="__main__":unittest.main()
