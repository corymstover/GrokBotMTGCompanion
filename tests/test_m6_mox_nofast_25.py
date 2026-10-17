"""Cycle 89: target manifests must preserve frozen Step C authority."""
import unittest,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_m6_mox_nofast_25 as m

class TestMoxNoFastGate(unittest.TestCase):
    def test_25_source_snapshots_and_no_authority(self):
        static=m.load(m.STATIC)
        self.assertEqual(static["count"],25)
        self.assertEqual(len({r["slug"] for r in static["rows"]}),25)
        self.assertTrue(all(not v for v in m.AUTH.values()))
    def test_frozen_stepc_present(self):
        for row in m.load(m.STATIC)["rows"]:
            self.assertTrue((m.BASE/(row["slug"]+".json")).is_file())
            self.assertTrue((m.NEWSTATIC/(row["slug"]+".json")).is_file())
    def test_mox_added_to_only_target_fast_inventory(self):
        for row in m.load(m.STATIC)["rows"]:
            old=m.load(m.BASE/(row["slug"]+".json"))
            corrected=m.load(m.NEWSTATIC/(row["slug"]+".json"))
            for cmd in old["commanders"]:
                historical=set(cmd["fast_mana_inventory"])
                current=set(corrected["fast_mana_cards"])
                self.assertEqual(current-historical,{"Chrome Mox"})
                self.assertEqual(historical-current,set())

if __name__=="__main__":unittest.main()
