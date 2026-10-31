"""Source-backed questions about keywords, published rulings and interactions."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import mv_ask  # noqa: E402


class RulesEvidenceQuestions(unittest.TestCase):
    def test_published_ruling_qualifies_interaction_without_simulating(self):
        answer = mv_ask.ask("How does Urza's Saga interact with Urza's Tower?")
        self.assertEqual(answer["route"], "ask->rules_evidence:interaction")
        self.assertEqual(answer["confidence"], "QUALIFIED")
        direct = answer["result"]["direct_rulings"]
        self.assertTrue(any("doesn't interact with Urza's Tower" in r["text"] for r in direct))
        self.assertEqual(answer["data_as_of"], "2026-10-15")
        self.assertEqual(answer["rules_effective"], "2026-09-25")
        self.assertIn("HISTORICAL_RULINGS_SHARD_NOT_LIVE", answer["flags"])
        self.assertIn("NO_RULES_SIMULATION", answer["flags"])
        self.assertIn("media.wizards.com", answer["sources"][0])

    def test_card_rulings_are_dated_and_complete_for_committed_shard(self):
        answer = mv_ask.ask("What are the rulings for Urza's Saga?")
        self.assertEqual(answer["route"], "ask->rules_evidence:card")
        detail = answer["result"]
        self.assertEqual(detail["card"], "Urza's Saga")
        self.assertEqual(detail["published_ruling_count"], len(detail["published_rulings"]))
        self.assertTrue(all(len(r["date"]) == 10 and r["text"] for r in detail["published_rulings"]))
        self.assertTrue(any("Urza's Tower" in r["text"] for r in detail["published_rulings"]))

    def test_keyword_mechanics_have_specific_official_rule_numbers(self):
        answer = mv_ask.ask("What mechanics does Serra Angel have?")
        self.assertEqual(answer["route"], "ask->rules_evidence:card")
        self.assertEqual(answer["result"]["keywords"], ["Flying", "Vigilance"])
        sections = {r["keyword"]: r["rule"] for r in answer["result"]["keyword_rules"]}
        self.assertEqual(sections, {"Flying": "702.9", "Vigilance": "702.20"})
        self.assertIn("not all card mechanics", answer["result"]["limitation"])

    def test_direct_keyword_explanation_uses_cr_excerpt(self):
        answer = mv_ask.ask("What does trample mean?")
        self.assertEqual(answer["route"], "ask->rules_evidence:keyword")
        self.assertEqual(answer["result"]["comprehensive_rules"]["rule"], "702.19")
        self.assertTrue(answer["result"]["comprehensive_rules"]["text"])
        self.assertIn("CR_KEYWORD_EXCERPT_ONLY", answer["flags"])

    def test_no_published_ruling_does_not_mean_no_interaction(self):
        answer = mv_ask.ask("How do Sol Ring and Serra Angel interact?")
        self.assertEqual(answer["route"], "ask->rules_evidence:interaction")
        self.assertEqual(answer["result"]["direct_rulings"], [])
        self.assertIn("NO_DIRECT_RULING", answer["flags"])
        self.assertIn("No ruling does not mean no interaction", answer["result"]["limitation"])

    def test_unknown_card_no_rule_guess(self):
        answer = mv_ask.ask("What are the rulings for Zorblax the Unreal?")
        self.assertEqual(answer["confidence"], "NOT_FOUND")
        self.assertIn("UNKNOWN_CARD_IN_INDEX", answer["flags"])
        unknown_pair = mv_ask.ask("How does Zorblax the Unreal interact with Sol Ring?")
        self.assertEqual(unknown_pair["confidence"], "NOT_FOUND")
        self.assertIn("UNKNOWN_CARD", unknown_pair["flags"])

    def test_existing_lore_set_and_commander_routes_not_stolen(self):
        self.assertEqual(mv_ask.ask("Who killed Elesh Norn?")["route"], "ask->lore:killed")
        self.assertEqual(mv_ask.ask("How many cards are in Alpha?")["route"], "ask->set_atlas:set")
        self.assertEqual(mv_ask.ask("Can Sol Ring be my commander?")["route"], "ask->rules:single")


if __name__ == "__main__":
    unittest.main()
