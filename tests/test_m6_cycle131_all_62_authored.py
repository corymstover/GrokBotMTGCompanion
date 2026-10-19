"""Cycle131 exhaustive 62-deck authored coverage, source integrity and fail-closed tests."""
from __future__ import annotations
import copy
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_m6_cycle131_all_62_authored as m

class CompleteAuthoredReviews(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.receipt=m.audit()
 def test_all_62_unique_source_bound_author_reviews(self):
  a=self.receipt
  self.assertEqual((a["previous_authored"],a["new_authored"],a["total_authored"]),(33,29,62))
  self.assertEqual(len(a["new_reviews"]),29)
  self.assertEqual(len(set(a["authored_deck_ids_in_triage_order"])),62)
  self.assertEqual(len(set(x["deck_id"] for x in a["new_reviews"])),29)
  self.assertEqual(set(a["authored_deck_ids_in_triage_order"]),set(m.read(m.REG)["decks"]))
 def test_all_exact_sources_and_real_100_card_zones(self):
  for r in self.receipt["new_reviews"]:
   self.assertEqual(r["source_cards_100"],100)
   self.assertEqual(r["commanders"],len(r["commander_names"]))
   self.assertEqual(set(r["candidate_and_commander_oracle_sha"]),set(r["commander_names"])|{r["add"],r["cut"]})
   self.assertTrue(all(len(z)==71 and z.startswith("sha256:") for z in r["candidate_and_commander_oracle_sha"].values()))
   self.assertTrue(r["m5_swap_id"].startswith("swap:"))
 def test_dual_commanders_and_companion_not_extra_cards(self):
  s={x["deck_id"]:x for x in self.receipt["new_reviews"]}
  self.assertEqual((s["Grixistax___October_2026"]["commanders"],s["Grixistax___October_2026"]["companion_outside_100"]),(2,0))
  self.assertEqual((s["Cecily__Bjorna__Lutri"]["commanders"],s["Cecily__Bjorna__Lutri"]["companion_outside_100"]),(2,1))
 def test_authorized_bans_future_release_not_official(self):
  s={x["deck_id"]:x for x in self.receipt["new_reviews"]}
  self.assertEqual(s["Cecily__Bjorna__Lutri"]["official_status_at_frozen_snapshot"],"not_compliant_project_exceptions")
  self.assertEqual(len(s["Cecily__Bjorna__Lutri"]["registered_project_exceptions"]),3)
  self.assertEqual(s["Tresserhorn_s_Lord__Returned"]["official_status_at_frozen_snapshot"],"pending_release")
  self.assertEqual(len(s["Tresserhorn_s_Lord__Returned"]["registered_project_exceptions"]),1)
 def test_two_documented_raw_sha_mismatches_not_silently_repaired(self):
  bad={x["deck_id"] for x in self.receipt["new_reviews"] if not x["recorded_raw_hash_matches_original_source"]}
  self.assertEqual(bad,m.KNOWN_RECORD_MISMATCH)
 def test_author_reviewer_not_formal_pass_c_or_real_phase_b(self):
  self.assertEqual(self.receipt["formal_independent_pass_c_completed"],0)
  self.assertEqual(self.receipt["complete_effect_aware_phase_b_certified"],0)
  self.assertEqual(self.receipt["canonical_deck_changes"],0)
  self.assertEqual(self.receipt["owner_approved_swaps"],0)
  self.assertFalse(self.receipt["m6_accepted"])
  self.assertFalse(self.receipt["current_full_100_card_legality_reverified"])
 def test_fail_closed_if_m6_tracker_falsely_promoted(self):
  original=m.read
  def tampered(path):
   x=original(path)
   if Path(path)==m.TRACK:
    x=copy.deepcopy(x);x["m6"]["gates"][3]["completed"]=62
   return x
  with patch.object(m,"read",side_effect=tampered):
   with self.assertRaises(ValueError):m.audit()
 def test_fail_closed_if_source_case_missing(self):
  original=m.read
  def tampered(path):
   x=original(path)
   if Path(path)==m.BATCHES["e"]:
    x=copy.deepcopy(x);x["rows"]=x["rows"][:-1];x["count"]=len(x["rows"])
   return x
  with patch.object(m,"read",side_effect=tampered):
   with self.assertRaises(ValueError):m.audit()
 def test_fail_closed_if_fake_independent_author_added(self):
  original=m.read
  def tampered(path):
   x=original(path)
   if Path(path)==m.BATCHES["a"]:
    x=copy.deepcopy(x);x["rows"][0]["authored_by"]="Independent Pass C expert"
   return x
  with patch.object(m,"read",side_effect=tampered):
   with self.assertRaises(ValueError):m.audit()
 def test_fail_closed_on_wrong_m5_swap(self):
  original=m.read
  def tampered(path):
   x=original(path)
   if Path(path)==m.BATCHES["a"]:
    x=copy.deepcopy(x);x["rows"][0]["add"]="Unregistered new candidate"
   return x
  with patch.object(m,"read",side_effect=tampered):
   with self.assertRaises(ValueError):m.audit()
 def test_no_writer_can_approve_deck_through_author_record(self):
  original=m.read
  def tampered(path):
   x=original(path)
   if Path(path)==m.BATCHES["b"]:
    x=copy.deepcopy(x);x["rows"][0]["approved_swaps"]=1
   return x
  with patch.object(m,"read",side_effect=tampered):
   with self.assertRaises(ValueError):m.audit()

if __name__=="__main__":unittest.main()
