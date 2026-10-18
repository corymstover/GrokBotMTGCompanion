"""Cycle 95 negative control and access-bound tests (not a multiplayer rules engine)."""
import sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_m6_abaddon_deckwide_access as m

def rec(seen,commander=4,mana=None):
    return {"first_seen":seen,"commander_turn":commander,
            "mana":mana or [1,2,3,4,5,6,7,8],"spent":[0]*8,"mulligans":0}

class AccessBounds(unittest.TestCase):
    def test_access_is_not_cast(self):
        r=rec({"Heartless Hidetsugu":5,"Ponder":0})
        self.assertEqual(m.early_seen_gross(r,"Heartless Hidetsugu",5,5),5)
        self.assertIsNone(m.early_seen_gross(r,"Heartless Hidetsugu",5,4))
        self.assertIsNone(m.early_seen_gross(r,"never seen",0,8))
    def test_delayed_ability_and_followup_required(self):
        r=rec({"Heartless Hidetsugu":5,"Ponder":1},commander=3)
        d=m.conditional_candidate(r,"Heartless Hidetsugu",5,8,["Ponder"])
        self.assertEqual(d["source_gross_castable_by_t6"],1)
        self.assertEqual(d["conditional_next_turn_activation_by_t8"],1)
        self.assertEqual(d["conditional_commander_prior_and_seen_1mv_followup_by_t8"],1)
        r2=rec({"Heartless Hidetsugu":8,"Ponder":1},commander=2)
        self.assertEqual(m.conditional_candidate(r2,"Heartless Hidetsugu",5,8,["Ponder"])["conditional_next_turn_activation_by_t8"],0)
        r3=rec({"Heartless Hidetsugu":5,"Ponder":1},commander=None)
        self.assertEqual(m.conditional_candidate(r3,"Heartless Hidetsugu",5,8,["Ponder"])["conditional_commander_prior_and_seen_1mv_followup_by_t8"],0)
    def test_blast_legal_target_and_fixed_X(self):
        r=rec({"Bituminous Blast":5},commander=4)
        self.assertEqual(m.blast_opportunity(r,8,5,False),{"printed":False,"double":False})
        self.assertEqual(m.blast_opportunity(r,8,0,True),{"printed":True,"double":False})
        self.assertEqual(m.blast_opportunity(r,8,5,True),{"printed":True,"double":True})
        r2=rec({"Bituminous Blast":5},commander=None)
        self.assertEqual(m.blast_opportunity(r2,8,5,True),{"printed":True,"double":False})
    def test_distinct_development_and_effects(self):
        a=m.diff_stats([0,1,1,0],[1,1,0,0])
        self.assertEqual(a["paired_diff"],0)
        self.assertEqual(a["baseline"],a["challenger"])
        self.assertEqual(m.summary([0,1,0,1])["successes"],2)
    def test_strict_no_authority(self):
        p=m.read(m.PLAN)
        self.assertEqual(p["status"],"registered_before_test")
        self.assertFalse(any(p["authority"].values()))
        self.assertEqual(len(p["hypotheses"]),2)
        self.assertTrue(all(h["cut"]=="Bituminous Blast" for h in p["hypotheses"]))

if __name__=="__main__":unittest.main()
