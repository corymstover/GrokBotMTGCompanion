"""Batch 9: faction/guild short-name aliases and leader answers with era context.

Aliases are derived from the graph's own Faction nodes, so they never point outside the graph.
Leader answers are ordered by the publication date of the citing official page; the most recent
cited leader is labelled as such, not as present-day canon."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import mv_ask as A  # noqa: E402

ALIASES = {"Izzet": "faction:izzet_league", "the Izzet": "faction:izzet_league", "Izzet guild": "faction:izzet_league",
           "Golgari": "faction:golgari", "Orzhov": "faction:orzhov_syndicate", "Azorius": "faction:azorius_senate",
           "Boros": "faction:boros_legion", "Gruul": "faction:gruul_clans", "Lorehold": "faction:lorehold_college",
           "Witherbloom": "faction:witherbloom_college", "Tuskeri": "faction:tuskeri", "Coppercoats": "faction:coppercoats"}


class FactionAliases(unittest.TestCase):
    def test_short_names_resolve(self):
        for term, nid in ALIASES.items():
            with self.subTest(term=term):
                self.assertEqual(A._find(term), nid)

    def test_aliases_only_point_at_faction_nodes(self):
        g = A.graph()
        for k, nid in A.faction_aliases().items():
            self.assertEqual(g.nodes[nid]["type"], "Faction", k)

    def test_no_generic_word_aliases(self):
        for bad in ("sun", "brazen", "reverent", "kav memorial", "zendikari", "league", "college", ""):
            self.assertNotIn(bad, A.faction_aliases())

    def test_exact_names_win_over_aliases(self):
        self.assertEqual(A._find("Golgari Swarm"), "faction:golgari")
        self.assertEqual(A._find("Sun Empire"), "faction:sun_empire")
        self.assertNotIn("MATCHED_BY_FACTION_ALIAS", A.ask("Who leads the Izzet League?")["flags"])

    def test_alias_match_is_flagged_and_answers(self):
        env = A.ask("Who leads the Izzet?")
        self.assertIn("MATCHED_BY_FACTION_ALIAS", env["flags"])
        self.assertEqual(env["confidence"], "VERIFIED")
        self.assertEqual(env["result"]["leadership"]["most_recent_cited"]["node"], "character:ral_zarek")

    def test_unknown_short_name_not_found(self):
        self.assertEqual(A.ask("Who leads the Zzyzx?")["confidence"], "NOT_FOUND")
        self.assertIsNone(A._alias("Zzyzx"))


class LeaderEraContext(unittest.TestCase):
    def lead(self, q):
        env = A.ask(q)
        self.assertNotEqual(env["confidence"], "NOT_FOUND", q)
        return env, env["result"]["leadership"]

    def test_orzhov_most_recent_is_teysa_with_kaya_as_earlier_era(self):
        env, l = self.lead("Who leads the Orzhov?")
        self.assertEqual(l["most_recent_cited"]["node"], "character:teysa_karlov")  # MK009, MKM 2023-12
        self.assertIn("character:kaya", [x["node"] for x in l["timeline"]])  # WR016, WAR 2019
        self.assertIn("MULTIPLE_LEADERS_ACROSS_ERAS", env["flags"])

    def test_former_leaders_are_kept_but_not_named_most_recent(self):
        _, l = self.lead("Who is the leader of the Golgari?")
        jarad = [x for x in l["timeline"] if x["node"] == "character:jarad_vod_savo"][0]
        self.assertTrue(jarad["described_as_former"])
        self.assertEqual(l["most_recent_cited"]["node"], "character:vraska")
        _, l = self.lead("Who leads the Azorius?")
        self.assertTrue([x for x in l["timeline"] if x["node"] == "character:isperia"][0]["described_as_former"])
        self.assertEqual(l["most_recent_cited"]["node"], "character:lavinia")

    def test_timeline_is_date_ordered_and_note_is_honest(self):
        _, l = self.lead("Who leads the Azorius Senate?")
        dates = [x["source_date"] or "" for x in l["timeline"]]
        self.assertEqual(dates, sorted(dates))
        self.assertIn("not proof of the leader in present-day canon", l["note"])

    def test_single_leader_has_no_multi_era_flag(self):
        env, l = self.lead("Who leads the Boros?")
        self.assertEqual(l["most_recent_cited"]["node"], "character:aurelia")
        self.assertNotIn("MULTIPLE_LEADERS_ACROSS_ERAS", env["flags"])

    def test_implied_leader_stays_qualified(self):
        env, _ = self.lead("Who leads the Gruul?")
        self.assertEqual(env["confidence"], "QUALIFIED")


if __name__ == "__main__":
    unittest.main()
