"""Cycle 97: real-library metadata, deterministic cascade reveal, and fail-closed tests."""
import sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_m6_abaddon_real_library_replay as m

def meta(**cards):return {n:{"mv":c[0],"land":c[1],"front":n} for n,c in cards.items()}

class RealLibraryTests(unittest.TestCase):
 def test_forced_hand_is_exactly_three_distinct_canonical_cards(self):
  ordered=[{"name":n} for n in ["Boltwave","Flame Rift","Bituminous Blast"]+[f"Filler{i}" for i in range(96)]]
  names=m.stripped_library(ordered,"Bituminous Blast")
  self.assertEqual(len(names),96)
  self.assertNotIn("Flame Rift",names)
  ordered[5]["name"]="Boltwave"
  with self.assertRaises(ValueError):m.stripped_library(ordered,"Bituminous Blast")

 def test_unsupported_first_eligible_hit_is_declined_and_logged(self):
  md=meta(**{"Fake Land":(0,True),"Fake Spell":(1,False),"Test Spark":(1,False)})
  t=m.RealCascade(["Fake Land","Fake Spell","Test Spark"],md,"Bituminous Blast",[40,39,31],
                  {"B":2,"R":3,"C":4},6)
  t.place("Abaddon the Despoiler",entered=5)
  t.lost=5
  self.assertEqual(t.cast("Bituminous Blast"),2)
  t.resolve_all()
  offers=[x for x in t.events if x["event"]=="real_cascade_offer"]
  self.assertTrue(any(x["name"]=="Fake Spell" and x["outcome"]=="declined_unmodeled" for x in offers))
  self.assertFalse(any(x.get("name")=="Fake Spell" and x["event"]=="cast" for x in t.events))

 def test_strictly_lower_mv_and_land_skips(self):
  md=meta(**{"Fake Land":(0,True),"Fake Equal":(5,False),"Fake Lower":(4,False)})
  t=m.RealCascade(["Fake Land","Fake Equal","Fake Lower"],md,"Bituminous Blast",[40,39,31],
                  {"B":2,"R":3,"C":4},6)
  t.cast("Bituminous Blast")
  t.resolve_all()
  offers=[x for x in t.events if x["event"]=="real_cascade_offer"]
  self.assertEqual([e["name"] for e in offers],["Fake Lower"])

 def test_support_cast_and_no_new_granted_from_exile(self):
  md=meta(**{"Test Land":(0,True),"Kessig Flamebreather":(2,False)})
  t=m.RealCascade(["Test Land","Kessig Flamebreather"],md,"Bituminous Blast",[40,39,31],
                  {"B":2,"R":3,"C":4},6)
  t.place("Abaddon the Despoiler",entered=5);t.lost=5
  t.cast("Bituminous Blast");t.resolve_all()
  offers=[x for x in t.events if x["event"]=="real_cascade_offer"]
  self.assertEqual(offers[0]["outcome"],"cast_supported")
  casts=[x for x in t.events if x["event"]=="cast" and x["origin"]=="cascade_exile"]
  self.assertEqual(len(casts),1)
  self.assertEqual(casts[0]["granted_cascade"],0)

 def test_alias_resolves_only_front_face(self):
  name="Birgi, God of Storytelling // Harnfel, Horn of Bounty"
  self.assertEqual(m.FRONTS[name],"Birgi, God of Storytelling")
  self.assertNotIn(name,m.CARDS)

 def test_reject_false_improvement_and_missing_coverage(self):
  p=m.read(m.PLAN)
  self.assertEqual(p["sample_count_per_swap"],240)
  self.assertEqual(p["seed"],97017)
  self.assertEqual(len(p["swap_hypotheses"]),2)
  self.assertFalse(any(p["authority"].values()))
  self.assertIn("declined_unmodeled",p["cascade_policy"])
  totals=m.basic_stats([{"hand_casts":3,"granted_cast_triggers":1,"printed_cast_triggers":0,
    "cascade_offers":2,"supported_casts":0,"declined_unmodeled":2,"declined_legal_constraint":0,
    "first_hit_names":["Unknown","Unknown"]}])
  self.assertEqual(totals["effect_coverage"]["modeled_casts"],0)
  self.assertEqual(totals["effect_coverage"]["unmodeled_offers"],2)

if __name__=="__main__":unittest.main()
