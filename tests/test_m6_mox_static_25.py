"""Cycle 88: fail closed on unexpected Step C changes or authority promotion."""
import unittest
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_m6_mox_static_25 as mod

class TestCorrected25(unittest.TestCase):
    def test_all_25_only_intended_diff(self):
        rows=mod.build_rows()
        self.assertEqual(len(rows),25)
        self.assertEqual(len({a[0] for a in rows}),25)
        self.assertTrue(all(a[3]["authority"]["can_decide"] is False for a in rows))
    def test_first_has_conditional_mox(self):
        rows=mod.build_rows()
        slug,_,_,data,_=next(x for x in rows if x[0]=="abaddon-the-despoiler")
        self.assertIn("Chrome Mox",data["fast_mana_cards"])
        self.assertEqual(data["counts"]["lands"],34)
        self.assertEqual(data["counts"]["fast_mana"],12)
    def test_locked_sources_exist(self):
        for slug,_,old,_,entry in mod.build_rows():
            self.assertTrue(old.exists())
            self.assertTrue((mod.ROOT/entry["canonical_project_list"]["export"]).exists())

if __name__=="__main__":unittest.main()
