"""Batch 14 Phase 7: leader questions phrased with titles ('guildmaster', 'khan', 'commander'), "who's",
'in charge of', 'commands', and a trailing 'now' route to the stored leader relations; factions with no
cited leader stay NOT_FOUND rather than guessing."""
import re
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import mv_ask as A  # noqa: E402

FORMS = ["Who leads the {}?", "Who leads the {} now?", "Who is the guildmaster of the {}?", "Who's the leader of {}?",
         "Who is in charge of the {}?", "Who's in charge of the {}?", "Who commands the {}?",
         "Who is the current leader of the {}?", "Who is in command of the {}?"]


def lead_factions():
    g = A.graph()
    out = set()
    for e in g.g["edges"]:
        if e["relation"] in A.LEADER_RELATIONS and e.get("claim") and g.nodes.get(e["to"], {}).get("type") == "Faction":
            out.add(e["to"])
    return sorted(out)


class LeaderPhrasingTests(unittest.TestCase):
    def test_izzet_variants(self):
        for f in FORMS:
            env = A.ask(f.format("Izzet"))
            self.assertNotEqual(env["confidence"], "NOT_FOUND", f)
            self.assertEqual(env["result"]["entity"], "faction:izzet_league", f)
            self.assertIn("leadership", env["result"], f)

    def test_every_led_faction_answers_every_form(self):
        g = A.graph()
        for nid in lead_factions():
            name = re.sub(r"\s*\(.*?\)", "", g.nodes[nid]["name"]).strip()
            name = re.sub(r"^the ", "", name, flags=re.I)
            for f in FORMS:
                env = A.ask(f.format(name))
                self.assertEqual(env["result"].get("entity"), nid, f.format(name))
                self.assertIn("leadership", env["result"], f.format(name))

    def test_faction_without_cited_leader_is_not_invented(self):
        env = A.ask("Who is the guildmaster of the Elves of Eldraine?")
        self.assertEqual(env["confidence"], "NOT_FOUND")
        self.assertEqual(env["route"], "ask->lore:" + A.LEADER_UNION)

    def test_title_question_about_character_still_routes(self):
        env = A.ask("Who is the khan of the Abzan?")
        self.assertEqual(env["result"]["entity"], "faction:abzan")


if __name__ == "__main__":
    unittest.main()
