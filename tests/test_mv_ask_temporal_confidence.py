"""Temporal confidence regressions: a cited historical event is not current-world certainty."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import mv_ask as A  # noqa: E402


class TemporalConfidence(unittest.TestCase):
    def test_ugin_original_timeline_death_is_qualified(self):
        env = A.ask("Who killed Ugin?")
        self.assertEqual(env["confidence"], "QUALIFIED")
        self.assertIn("TIMELINE_CONTEXT_REQUIRED", env["flags"])
        self.assertTrue(any(row["node"] == "character:nicol_bolas"
                            for rows in env["result"]["relations_by_status"].values() for row in rows))

    def test_current_leader_claim_does_not_imply_current_office(self):
        env = A.ask("Who is the current guildmaster of the Izzet?")
        self.assertEqual(env["confidence"], "QUALIFIED")
        self.assertIn("CURRENT_LEADER_NOT_ESTABLISHED", env["flags"])
        self.assertIsNone(env["result"]["leadership"]["verified_current_leader"])
        self.assertEqual(env["result"]["leadership"]["most_recent_cited"]["node"],
                         "character:ral_zarek")

    def test_deceased_latest_cited_leader_does_not_get_verified(self):
        env = A.ask("Who leads the Orzhov?")
        self.assertEqual(env["confidence"], "QUALIFIED")
        self.assertIn("LATEST_CITED_LEADER_DEATH_RECORDED", env["flags"])
        leader = env["result"]["leadership"]
        self.assertEqual(leader["most_recent_cited"]["node"], "character:teysa_karlov")
        self.assertIn("MK001", [r["claim"] for r in leader["latest_leader_death_evidence"]])

    def test_nonpresent_leader_without_contradiction_stays_supported(self):
        env = A.ask("Who leads the Izzet?")
        self.assertEqual(env["confidence"], "VERIFIED")
        self.assertNotIn("CURRENT_LEADER_NOT_ESTABLISHED", env["flags"])

    def test_unsupported_hypothetical_still_not_found(self):
        env = A.ask("Who killed Zorblax the Unreal?")
        self.assertEqual(env["confidence"], "NOT_FOUND")


if __name__ == "__main__":
    unittest.main()
