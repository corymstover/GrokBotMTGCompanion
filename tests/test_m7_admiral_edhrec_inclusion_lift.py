"""Research-only EDHREC inclusion/high-lift discovery and permanent owner contract.

Validates a captured 2026-10-22 discovery crosswalk, not live fluctuating
EDHREC metrics, a game engine, M6 certification or owner-ready M7 list.
"""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
F = ROOT / "data/grixis/m7/research_challengers/Admiral_Beckett_Brass_EDHREC_inclusion_lift_discovery_20261022.json"
BASE = ROOT / "data/grixis/m6/authority_snapshots/Admiral_Beckett_Brass_Canonical_Approved_20261022.txt"
LEDGER = ROOT / "data/grixis/m7/research_challengers/Admiral_Beckett_Brass_current_continuation_20261022.json"
CONTRACT = ROOT / "grixis/Commander-First Decisive Optimization and Test Economy Standard.md"
AGENTS = ROOT / "AGENTS.md"
NOVEL = {
    "Storm Fleet Aerialist", "Kitesail Corsair", "Dreamcaller Siren",
    "Kukemssa Pirates", "Deadeye Brawler", "Prying Blade",
}

class AdmiralEDHRECDiscoveryContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d = json.loads(F.read_text(encoding="utf-8"))
        cls.baseline = {line.split("x ", 1)[1].replace(" [Commander]", "")
                        for line in BASE.read_text(encoding="utf-8").splitlines() if line.strip()}

    def test_newly_observed_six_genuinely_outside_canonical(self):
        self.assertEqual(self.d["status"], "RESEARCH_ONLY_DISCOVERY_NOT_OWNER_READY")
        self.assertEqual(len(self.d["top_inclusion_observed"]), 10)
        self.assertEqual(len(self.d["high_lift_observed"]), 10)
        self.assertEqual({x["name"] for x in self.d["scryfall_new_discovery_oracle"]}, NOVEL)
        self.assertTrue(NOVEL.isdisjoint(self.baseline))
        self.assertTrue(all(x["name"] in self.baseline for x in self.d["top_inclusion_observed"]))

    def test_sources_metrics_and_distinct_lift_semantics(self):
        src = self.d["source"]
        self.assertIn("edhrec.com/commanders/admiral-beckett-brass", src["edhrec_commander_url"])
        self.assertEqual(src["retrieved_date"], "2026-10-22")
        self.assertIn("lift", src["associated_metric"])
        self.assertIn("not historical synergy", src["associated_metric"])
        for item in self.d["top_inclusion_observed"] + self.d["high_lift_observed"]:
            self.assertGreaterEqual(item["inclusion_percent"], 0)
            self.assertGreater(item["lift_times"], 0)

    def test_scryfall_source_grixis_and_reasoned_judgments(self):
        for rec in self.d["scryfall_new_discovery_oracle"]:
            self.assertTrue(rec["oracle_id"], rec["name"])
            self.assertTrue(rec["oracle_text"], rec["name"])
            self.assertTrue(rec["scryfall_uri"].startswith("https://scryfall.com/card/"))
            self.assertEqual(rec["commander_legality"], "legal")
            self.assertTrue(set(rec["color_identity"]) <= {"B", "R", "U"})
            self.assertIn(rec["judgment"], {"SELECT_ADD", "REJECT", "RETAIN_ALTERNATIVE", "EXCLUDE_INVALID"})
            self.assertTrue(rec["challenged_slots"])
            self.assertGreater(len(rec["qualitative_analysis"]), 55)

    def test_no_unsupported_three_pirate_hit_from_kukemssa_or_raid(self):
        records = {x["name"]: x for x in self.d["scryfall_new_discovery_oracle"]}
        self.assertIn("assigns no combat damage", records["Kukemssa Pirates"]["oracle_text"])
        self.assertIn("if you attacked this turn", records["Storm Fleet Aerialist"]["oracle_text"])
        self.assertIn("if you control another Pirate", records["Dreamcaller Siren"]["oracle_text"])
        self.assertIn("up to two target nonland permanents", records["Dreamcaller Siren"]["oracle_text"])

    def test_permanent_rule_and_owner_hold(self):
        rules = CONTRACT.read_text(encoding="utf-8")
        agents = AGENTS.read_text(encoding="utf-8")
        self.assertIn("Mandatory EDHREC candidate-discovery expansion", rules)
        self.assertIn("Top Cards / inclusion", rules)
        self.assertIn("High Lift", rules)
        self.assertIn("Mandatory EDHREC inclusion and high-lift discovery", agents)
        ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
        self.assertFalse(ledger["canonical_authority"]["new_m7_owner_approval"])
        # The captured EDHREC discovery remains research provenance, while
        # a separately verified revised M7 candidate may advance to owner
        # presentation without changing the canonical approved deck.
        self.assertIn(ledger["m7_status"], {
            "RESEARCH_ONLY_REOPENED_OWNER_APPROVAL_WITHHELD",
            "REVISED_M7_SIX_SWAP_OWNER_CANDIDATE_IN_PR616_AWAITING_LATEST_EXACT_HEAD_CI_NO_OWNER_APPROVAL",
        })
        if ledger["m7_status"].startswith("REVISED_M7_"):
            rev2 = ledger["m7_rev2_decision_packet"]
            self.assertFalse(rev2["owner_approval"])
            self.assertFalse(rev2["canonical_changed"])
            self.assertTrue(rev2["edhrec_inclusion_and_high_lift"])
            self.assertEqual(rev2["genuine_swaps"], 6)

if __name__ == "__main__":
    unittest.main()
