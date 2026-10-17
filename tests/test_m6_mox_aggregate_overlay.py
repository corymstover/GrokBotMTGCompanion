"""Aggregate overlay must be exactly +25 conditional fast-mana cards and nothing else."""
import unittest,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_m6_mox_aggregate_overlay as a
class TestAggregate(unittest.TestCase):
    def test_25_card_overlay(self):
        r=a.derive()
        self.assertEqual(len(r["deck_rows"]),62)
        self.assertEqual(r["corrected_totals"]["fast_mana"]-r["original_totals"]["fast_mana"],25)
        self.assertEqual(sum(d["chrome_mox_conditional_inventory_delta"] for d in r["deck_rows"]),25)
    def test_original_land_totals_and_approval(self):
        r=a.derive()
        self.assertEqual(r["original_totals"]["lands"],r["corrected_totals"]["lands"])
        self.assertFalse(r["historical_evidence_overwritten"])
        self.assertTrue(all(not v for v in r["authority"].values()))
if __name__=="__main__":unittest.main()
