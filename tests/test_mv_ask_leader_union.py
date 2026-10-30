"""Batch 11: leader questions query led|leader_of|leads together (no fallback-only hiding)."""
import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import mv_ask as A


def rels(env):
    return {r["relation"].replace("inverse_of:", "") for rs in env["result"]["relations_by_status"].values() for r in rs}


def nodes(env):
    return {r["node"] for rs in env["result"]["relations_by_status"].values() for r in rs}


class LeaderUnion(unittest.TestCase):
    def test_former_led_edge_does_not_hide_leader_of(self):
        # GD010 stores Feather "led" the Boros; Aurelia is stored as leader_of (GD008, WR015)
        env = A.ask("Who leads the Boros?")
        self.assertEqual(env["route"], "ask->lore:" + A.LEADER_UNION)
        self.assertTrue({"led", "leader_of"} <= rels(env))
        self.assertEqual(env["result"]["leadership"]["most_recent_cited"]["node"], "character:aurelia")
        self.assertIn("character:feather", nodes(env))
        self.assertIn("MULTIPLE_LEADERS_ACROSS_ERAS", env["flags"])

    def test_dimir_keeps_szadek_as_former_and_lazav_most_recent(self):
        env = A.ask("Who was the leader of House Dimir?")
        self.assertTrue({"led", "leader_of"} <= rels(env))
        tl = env["result"]["leadership"]["timeline"]
        self.assertTrue(any(x["described_as_former"] for x in tl if x["node"] == "character:szadek"))
        self.assertEqual(env["result"]["leadership"]["most_recent_cited"]["node"], "character:lazav")

    def test_ruled_also_reads_leader_of(self):
        env = A.ask("Who ruled the Jeskai?")
        self.assertTrue({"character:ojutai", "character:narset"} <= nodes(env))

    def test_led_only_entities_still_answer(self):
        env = A.ask("Who led the Oriq?")
        self.assertEqual(nodes(env), {"character:extus"})

    def test_unknown_faction_still_not_found(self):
        self.assertEqual(A.ask("Who leads the Zzyzx Guild?")["confidence"], "NOT_FOUND")


if __name__ == "__main__":
    unittest.main()
