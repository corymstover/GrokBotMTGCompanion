"""Five formerly isolated character/faction IDs receive cited but non-exhaustive history."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_p5_isolated_entity_history as audit  # noqa: E402
import mv_ask  # noqa: E402


class IsolatedEntityHistoryTests(unittest.TestCase):
    def test_all_registered_characters_and_factions_have_direct_source_claims(self):
        r = audit.audit()
        self.assertEqual(r["status"], "PASS")
        self.assertEqual(r["verified_claims"], 5)
        self.assertEqual(r["registered_character_faction_entities"], 629)
        self.assertEqual(r["entities_with_direct_cited_claims"], 629)
        self.assertEqual(r["uncovered"], [])
        self.assertFalse(r["complete_histories"])
        self.assertFalse(r["owner_approved"])
        self.assertFalse(r["live_source_quote_check"])
        self.assertTrue(all(len(s["quote_sha256"]) == 64 for s in r["quote_hashes"]))

    def test_all_five_originally_missing_entities_now_answer_with_cited_history(self):
        examples = ["Eric Kenrith", "Hazel Kenrith", "Lyra Dawnbringer", "Valentin", "the Cabaretti"]
        for entity in examples:
            with self.subTest(entity=entity):
                answer = mv_ask.ask(f"What is the history of {entity}?")
                self.assertEqual(answer["route"], "ask->entity_history")
                self.assertEqual(answer["confidence"], "QUALIFIED")
                self.assertTrue(any(url.startswith("https://magic.wizards.com/")
                                    for url in answer["sources"]))
                self.assertIn("PARTIAL_CITED_ENTITY_HISTORY", answer["flags"])
                self.assertFalse(answer["result"]["complete_history"])

    def test_eric_spelling_and_current_leadership_are_not_assumed(self):
        pack = __import__("json").loads(audit.PACK.read_text(encoding="utf-8"))
        eric = next(c for c in pack["claims"] if c["id"] == "IEH002")
        self.assertIn("Eric", eric["source_excerpt"])
        self.assertIn("Erec", eric["limitation"])
        self.assertNotIn("Erec Kenrith", {n["name"] for n in mv_ask.graph().nodes.values()
                                          if n["type"] == "Character"})
        leader = mv_ask.ask("Who currently leads the Cabaretti?")
        self.assertEqual(leader["confidence"], "QUALIFIED")
        self.assertIn("CURRENT_LEADER_NOT_ESTABLISHED", leader["flags"])


if __name__ == "__main__":
    unittest.main()
