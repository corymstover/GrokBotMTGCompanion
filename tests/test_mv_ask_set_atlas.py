"""Natural-language Set & Printing Atlas answers retain scope and source qualifiers."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import mv_ask as ask  # noqa: E402


class SetAtlasAskTests(unittest.TestCase):
    def test_category_total_is_not_misrepresented_as_expansion_total(self):
        result = ask.ask("How many MTG sets have been released?")
        self.assertEqual(result["route"], "ask->set_atlas:categories")
        self.assertEqual(result["confidence"], "QUALIFIED")
        self.assertEqual(result["data_as_of"], "2026-10-29")
        counts = result["result"]["exclusive_set_code_scopes"]
        self.assertEqual(counts["historical_regular_mainline"], 136)
        self.assertEqual(sum(counts.values()), 1062)
        self.assertIn("NOT_A_UNIVERSAL_PREMIER_SET_TOTAL", result["flags"])
        self.assertIn("not an official universal expansion", result["result"]["question_scope"])
        self.assertIn("SOURCE_BULK_NOT_PRESENT", result["flags"])

    def test_alpha_distinguishes_card_identities_from_printing_records(self):
        result = ask.ask("How many cards are in Alpha?")
        self.assertEqual(result["route"], "ask->set_atlas:set")
        detail = result["result"]
        self.assertEqual(detail["set_code"], "lea")
        self.assertEqual(detail["distinct_identities_or_unresolved"], 290)
        self.assertEqual(detail["printing_records"], 295)
        self.assertEqual(detail["identity_classifications"]["debut"], 290)
        self.assertFalse(detail["card_list_complete"])
        self.assertNotIn("cards", detail)
        self.assertEqual(result["confidence"], "QUALIFIED")

    def test_complete_set_list_has_status_for_every_identity(self):
        result = ask.ask("List all cards in Limited Edition Alpha")
        detail = result["result"]
        self.assertTrue(detail["card_list_complete"])
        self.assertEqual(len(detail["cards"]), 290)
        self.assertEqual(sum(card["printings"] for card in detail["cards"]), 295)
        self.assertEqual({card["classification"] for card in detail["cards"]}, {"debut"})
        self.assertIn("Black Lotus", {card["name"] for card in detail["cards"]})

    def test_beta_reprints_and_alias_lookup(self):
        result = ask.ask("What cards are in Beta?")
        self.assertEqual(result["result"]["set_code"], "leb")
        self.assertIn("reprint", result["result"]["identity_classifications"])
        self.assertGreater(result["result"]["identity_classifications"]["reprint"], 0)
        self.assertEqual(ask.ask("How many cards are in Unlimited?")["result"]["set_code"], "2ed")

    def test_debut_and_reprint_lists_do_not_conflate_statuses(self):
        debut = ask.ask("Which cards debuted in Beta?")["result"]
        reprint = ask.ask("Which cards were reprints in Beta?")["result"]
        self.assertEqual(debut["card_list_scope"], "debut or tied debut")
        self.assertEqual(reprint["card_list_scope"], "reprint")
        self.assertTrue(all(c["classification"] in ("debut", "tied debut") for c in debut["cards"]))
        self.assertTrue(all(c["classification"] == "reprint" for c in reprint["cards"]))
        self.assertEqual(len(debut["cards"]) + len(reprint["cards"]),
                         debut["distinct_identities_or_unresolved"])

    def test_printing_history_keeps_distinct_print_ids_and_set_names(self):
        result = ask.ask("Which sets was Black Lotus printed in?")
        self.assertEqual(result["route"], "ask->set_atlas:card_printings")
        self.assertEqual(result["confidence"], "QUALIFIED")
        self.assertEqual(result["result"]["matched_oracle_identities"], 1)
        card = result["result"]["cards"][0]
        self.assertEqual(card["first_recorded_printing_date"], "1993-08-05")
        self.assertEqual(card["first_recorded_sets"],
                         [{"code": "lea", "name": "Limited Edition Alpha"}])
        self.assertEqual(card["printing_record_count"], 13)
        self.assertEqual(len({row["printing_id"] for row in card["printings"]}), 13)
        self.assertLess(len(card["distinct_set_codes"]), 13)
        self.assertTrue(result["result"]["first_recorded_date_is_not_in_universe_debut"])
        self.assertIn("PRINTING_DATE_NOT_IN_UNIVERSE_CHRONOLOGY", result["flags"])
        self.assertTrue(all(source.startswith("https://github.com/") for source in result["sources"]))

    def test_first_printing_question_same_answer_as_full_history(self):
        result = ask.ask("When was Black Lotus first printed?")
        self.assertEqual(result["result"]["cards"][0]["first_recorded_printing_date"], "1993-08-05")
        self.assertEqual(ask.ask("What set did Black Lotus debut in?")["route"],
                         "ask->set_atlas:card_printings")

    def test_unknowns_do_not_get_fabricated_set_or_card_histories(self):
        missing_set = ask.ask("List all cards in Made-Up Set Zorblax")
        self.assertEqual(missing_set["confidence"], "NOT_FOUND")
        self.assertIn("UNKNOWN_SET_IN_SNAPSHOT", missing_set["flags"])
        missing_card = ask.ask("Which sets was Zorblax the Nonexistent printed in?")
        self.assertEqual(missing_card["confidence"], "NOT_FOUND")
        self.assertEqual(missing_card["result"]["cards"], [])

    def test_existing_rules_and_lore_routing_unchanged(self):
        self.assertEqual(ask.ask("Who is Urza's brother?")["route"], "ask->lore:sibling_of|twin_sibling_of")
        self.assertEqual(ask.ask("Can Sol Ring be my commander?")["route"], "ask->rules:single")


if __name__ == "__main__":
    unittest.main()
