"""Cycle 99: tutor origin, restrictions, exact zone movement and real stack tests."""
import sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_m6_abaddon_tutor_state as m

def md(name,mv,types,land=False):
 return {"mv":mv,"types":list(types),"land":land,"front":name}

class TutorTests(unittest.TestCase):
 def state(self,library,metadata,slot="Bituminous Blast"):
  t=m.TutorCascade(library,metadata,slot,[40,39,31],{"U":2,"B":4,"R":3,"C":6},6)
  return t

 def test_mystical_tutor_restricts_instant_or_sorcery(self):
  lib=["Sol Ring","Kessig Flamebreather","Ponder","Test Land"]
  meta={"Sol Ring":md("Sol Ring",1,["artifact"]),
        "Kessig Flamebreather":md("Kessig Flamebreather",2,["creature"]),
        "Ponder":md("Ponder",1,["sorcery"]),
        "Test Land":md("Test Land",0,["land"],True)}
  t=self.state(lib,meta)
  self.assertEqual(t.find_tutor_target("Mystical Tutor"),"Ponder")
  t.resolve_tutor("Mystical Tutor")
  self.assertEqual(t.library[0],"Ponder")
  self.assertEqual(len(t.library),4)
  self.assertEqual(t.lost,0)
  self.assertEqual(t.pilot,40)

 def test_demonic_tutor_to_hand_conserves_one_physical_card(self):
  l=["Sol Ring","Ponder","Test Land"]
  types={"Sol Ring":md("Sol Ring",1,["artifact"]), "Ponder":md("Ponder",1,["sorcery"]),
         "Test Land":md("Test Land",0,["land"],True)}
  t=self.state(l,types)
  h0=len(t.hand)
  chosen=t.resolve_tutor("Demonic Tutor")
  self.assertEqual(chosen,"Ponder")
  self.assertEqual(len(t.hand),h0+1)
  self.assertEqual(len(t.library),2)
  self.assertEqual(t.hand.count("Ponder"),1)
  self.assertNotIn("Ponder",t.library)

 def test_imperial_and_vampiric_loss_is_self_only(self):
  types={"Test Land":md("Test Land",0,["land"],True)}
  t=self.state(["Test Land"],types)
  t.resolve_tutor("Imperial Seal")
  self.assertEqual(t.pilot,38)
  t.resolve_tutor("Vampiric Tutor")
  self.assertEqual(t.pilot,36)
  self.assertEqual(t.lost,0)
  self.assertEqual(t.opponents,[40,39,31])

 def test_mystical_search_can_fail_with_no_eligible_targets(self):
  types={"Test Land":md("Test Land",0,["land"],True),
         "Sol Ring":md("Sol Ring",1,["artifact"])}
  t=self.state(["Sol Ring","Test Land"],types)
  self.assertIsNone(t.resolve_tutor("Mystical Tutor"))
  self.assertEqual(len(t.library),2)
  self.assertEqual(len(t.hand),3)
  self.assertEqual(t.events[-1]["selected"],None)

 def test_real_cascade_second_trigger_sees_new_top_card(self):
  types={"Mystical Tutor":md("Mystical Tutor",1,["instant"]),
         "Ponder":md("Ponder",1,["sorcery"]),
         "Test Land":md("Test Land",0,["land"],True)}
  t=self.state(["Mystical Tutor","Ponder","Test Land","Test Land"],types)
  t.place("Abaddon the Despoiler",entered=5)
  t.lost=5
  self.assertEqual(t.cast("Bituminous Blast"),2)
  t.resolve_all(100)
  offers=[e["name"] for e in t.events if e["event"]=="real_cascade_offer"]
  self.assertEqual(offers,["Mystical Tutor","Ponder"])
  self.assertTrue(any(e["event"]=="oracle_tutor_resolved" and e["selected"]=="Ponder" for e in t.events))
  self.assertTrue(any(e["event"]=="expanded_ponder" for e in t.events))
  free_casts=[e for e in t.events if e["event"]=="cast" and e["origin"]=="cascade_exile"]
  self.assertEqual(len(free_casts),2)
  self.assertTrue(all(e["granted_cascade"]==0 for e in free_casts))

 def test_real_sorcery_from_hand_timing_and_mana(self):
  l=["Test Land"]
  t=self.state(l,{"Test Land":md("Test Land",0,["land"],True)})
  t.hand=["Demonic Tutor"]
  t.mana={"B":1,"C":1,"U":0,"R":0}
  t.main_phase=False
  with self.assertRaises(ValueError):t.cast("Demonic Tutor")
  t.main_phase=True
  self.assertEqual(t.cast("Demonic Tutor"),0)
  self.assertEqual(t.mana["B"],0)
  t.resolve_all()
  self.assertIn("Demonic Tutor",t.graveyard)
  self.assertIn("Test Land",t.hand)

 def test_authority_and_scope(self):
  p=m.read(m.PLAN)
  self.assertEqual(p["status"],"registered_before_execution")
  self.assertEqual(len(p["oracle_assertions"]),4)
  self.assertEqual(p["seed"],97017)
  self.assertFalse(any(p["authority"].values()))
  self.assertEqual(set(p["effects"]),set(m.TUTOR_SPECS))

if __name__=="__main__":unittest.main()
