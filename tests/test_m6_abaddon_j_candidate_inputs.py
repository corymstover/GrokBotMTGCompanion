"""Fail-closed Abaddon-only M6 J prebundle provenance and authority tests."""
from __future__ import annotations
from unittest import TestCase, mock
from scripts import grixis_m6_abaddon_j_candidate_inputs as j

class AbaddonM6JSelectedInputs(TestCase):
    def test_actual_source_hashes_and_four_authored_reviews(self):
        result=j.report()
        self.assertEqual(result["selected_candidate_sha256"],j.SHA_CHOSEN)
        self.assertEqual(result["baseline_source_sha256"],j.SHA_BASE)
        self.assertEqual(result["selected_land_count"],34)
        self.assertEqual(len(result["author_reviewed_red_team_prompt_ids"]),4)
        self.assertTrue(result["pass_c_provenance"]["waiver_and_deck_stage_a_validated"])
        self.assertFalse(result["pass_c_provenance"]["technically_independent"])
        self.assertEqual(result["mechanical_case_inventory"]["registered"],104)
        self.assertFalse(result["readiness"]["phase_b_complete"])
        self.assertEqual(result["readiness"]["m6_j"],"BLOCKED")
        self.assertFalse(result["readiness"]["m7_owner_approved"])

    def test_exact_candidate_sha_drift_fails(self):
        original=j.digest
        def altered(p):
            return "0"*64 if p==j.SELECTED else original(p)
        with mock.patch.object(j,"digest",side_effect=altered):
            with self.assertRaisesRegex(ValueError,"SHA drift"):
                j.report()

    def test_four_unanswered_source_questions_required(self):
        original=j.fetch
        def corrupted(p):
            val=original(p)
            if p=="data/grixis/bracket_red_team/abaddon-the-despoiler.json":
                val["reviews"][0]["analysis"]="pretend already answered"
            return val
        with mock.patch.object(j,"fetch",side_effect=corrupted):
            with self.assertRaisesRegex(ValueError,"unanswered"):
                j.report()

    def test_owner_approval_false_and_waiver_not_independent(self):
        original=j.fetch
        def approved(p):
            val=original(p)
            if p==j.M7:
                val["owner_authority"]["exact_candidate_owner_approved"]=True
            return val
        with mock.patch.object(j,"fetch",side_effect=approved):
            with self.assertRaisesRegex(ValueError,"Unauthorized"):
                j.report()
        def fake_independence(p):
            val=original(p)
            if p==j.PROGRESS:
                val["genuinely_independent_third_model_reviews"]=62
            return val
        with mock.patch.object(j,"fetch",side_effect=fake_independence):
            with self.assertRaisesRegex(ValueError,"independent"):
                j.report()

    def test_cannot_omit_real_selected_lands_or_reinterpret_old_mana(self):
        with mock.patch.object(j,"LANDS",j.LANDS-{"Xander's Lounge"}):
            with self.assertRaisesRegex(ValueError,"mana base"):
                j.report()
        original=j.fetch
        def changed_old_model(p):
            val=original(p)
            if p=="data/grixis/commander_mana/abaddon-the-despoiler.json":
                val["method"]["model"]="9.9"
            return val
        with mock.patch.object(j,"fetch",side_effect=changed_old_model):
            with self.assertRaisesRegex(ValueError,"baseline"):
                j.report()
