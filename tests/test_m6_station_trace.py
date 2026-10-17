"""Bounded Grinding Station/Underworld Breach/Lotus Petal test invariants."""
import sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_m6_abaddon_station_trace as b
class TestStationTrace(unittest.TestCase):
 def test_existing_baseline_cards(self): b.check_list()
 def test_90_card_loop_no_win(self):
    x=b.trace(90)
    self.assertEqual((x["cycles"],x["self_milled"],x["escape_casts"]),(30,90,30))
    self.assertFalse(x["win_proven"])
    self.assertEqual(x["net_mana"],0)
 def test_requires_escape_fuel_if_petal_in_grave(self):
    self.assertEqual(b.trace(90,petal_field=False)["cycles"],0)
    self.assertEqual(b.trace(90,grave_other=3,petal_field=False)["cycles"],30)
 def test_replacement_prevents_fuel(self):
    self.assertEqual(b.trace(90,exile_mill=True)["cycles"],1)
 def test_all_scenarios_are_not_phase_b(self):
    d=b.data()
    self.assertFalse(d["phase_b_complete"])
    self.assertFalse(d["supports_improvement_claim"])
    self.assertFalse(any(d["authority"].values()))
 def test_no_breach(self):
    self.assertEqual(b.trace(90,breach=False)["cycles"],0)
if __name__=="__main__": unittest.main()
