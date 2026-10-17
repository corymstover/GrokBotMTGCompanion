"""Scope-restricted Abaddon corrected static mana audit tests."""
import sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_m6_abaddon_mox_static_delta as a
class TestAbaddonStatic(unittest.TestCase):
 def test_known_static_omission_is_corrected(self):
    d=a.derive(); m=d["metrics"]
    self.assertEqual(m["fast_mana_inventory"]["corrected"]-m["fast_mana_inventory"]["frozen"],1)
    self.assertEqual(m["repeatable_nonland_sources"]["corrected"]-m["repeatable_nonland_sources"]["frozen"],1)
 def test_conditional_cannot_claim_cast_rate(self):
    d=a.derive()
    self.assertFalse(d["color_probability_claim"])
    self.assertFalse(d["commander_cast_probability_recomputed"])
    self.assertFalse(d["legacy_commander_mana_report_recomputed"])
    self.assertFalse(any(d["authority"].values()))
 def test_land_count_not_silently_changed(self):
    d=a.derive(); self.assertEqual(d["metrics"]["lands"]["frozen"],d["metrics"]["lands"]["corrected"])
if __name__=="__main__": unittest.main()
