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

    def test_brothers_war_set_links_only_official_publication_series(self):
        r = ask.ask("What official Magic stories are linked to The Brothers' War set?")
        self.assertEqual(r["route"], "ask->set_atlas:set_story")
        self.assertEqual(r["confidence"], "QUALIFIED")
        self.assertEqual(r["result"]["set"]["code"], "bro")
        self.assertEqual(r["result"]["set"]["scryfall_recorded_release_date"], "2022-11-18")
        series = r["result"]["official_story_series"]
        self.assertEqual(series["official_title"], "The Brothers' War")
        self.assertEqual(series["official_story_count_in_recovered_index"], 10)
        self.assertEqual(len(series["sampled_official_story_pages"]), 3)
        self.assertLess(series["sampled_official_story_pages"][0]["published_date"], "2022-11-18")
        self.assertFalse(series["sample_is_complete"])
        self.assertIn("ONLY_SAMPLE_OF_STORY_PAGES_SHOWN", r["flags"])
        self.assertIn("NO_IN_UNIVERSE_EVENT_ORDER_INFERRED", r["flags"])
        for page in series["sampled_official_story_pages"]:
            self.assertIn(page["url"], r["sources"])

    def test_named_release_date_and_series_are_separate_from_story_dates(self):
        r = ask.ask("Show the release date and official story series for Bloomburrow")
        self.assertEqual(r["result"]["set"]["code"], "blb")
        self.assertEqual(r["result"]["official_story_series"]["official_title"], "Bloomburrow")
        self.assertEqual(r["result"]["story_link_coverage"],
                         {"linked_series": 12, "total_catalogued_set_codes": 1062})
        self.assertIn("real-world dates, not dates of in-universe events", r["result"]["limitation"])

    def test_missing_wizards_title_link_does_not_mean_no_story_exists(self):
        r = ask.ask("Is War of the Spark linked to an official story series?")
        self.assertEqual(r["result"]["set"]["code"], "war")
        self.assertIsNone(r["result"]["official_story_series"])
        self.assertIn("NO_OFFICIAL_TITLE_STORY_LINK_IN_BOUNDED_INDEX", r["flags"])
        self.assertFalse(any("/magic-story/" in source for source in r["sources"]))
        self.assertIn("not no story exists", r["result"]["limitation"])

    def test_unknown_set_does_not_fabricate_a_story_series(self):
        r = ask.ask("What official stories are linked to Zorblax Time Rift set?")
        self.assertEqual(r["confidence"], "NOT_FOUND")
        self.assertIsNone(r["result"]["set"])
        self.assertIsNone(r["result"]["official_story_series"])
        self.assertIn("UNKNOWN_SET_IN_SNAPSHOT", r["flags"])
        self.assertFalse(any("magic.wizards.com" in source for source in r["sources"]))

    def test_story_route_does_not_steal_in_universe_history_questions(self):
        r = ask.ask("What happened on Innistrad?")
        self.assertNotEqual(r["route"], "ask->set_atlas:set_story")

    def test_brothers_war_two_timeline_join_uses_exact_official_page(self):
        r = ask.ask("Compare The Brothers' War set release chronology with cited in-universe events")
        self.assertEqual(r["route"], "ask->set_atlas:dual_timeline")
        self.assertEqual(r["confidence"], "QUALIFIED")
        both = r["result"]["two_chronology_axes"]
        self.assertEqual(both["real_world_set_release"], "2022-11-18")
        self.assertEqual(both["cited_in_universe_relations_total"], 3)
        self.assertEqual(both["omitted_in_universe_relations"], 0)
        self.assertIsNone(both["fictional_event_date_corresponding_to_set_release"])
        self.assertEqual(both["release_vs_fictional_event_order"],
                         "NOT_COMPARABLE_DIFFERENT_CHRONOLOGY_AXES")
        rels = both["in_universe_relations_on_exact_linked_pages"]
        self.assertIn("BEFORE", {edge["relation"] for edge in rels})
        self.assertIn("SAME_TIME_AS_LABEL", {edge["relation"] for edge in rels})
        self.assertIn("69 AR", " ".join(edge["later_event"] for edge in rels))
        source_pages = {page["url"] for page in r["result"]["official_story_series"]
                        ["sampled_official_story_pages"]}
        for edge in rels:
            self.assertIn(edge["source_url"], source_pages)
            self.assertIn(edge["source_url"], r["sources"])
            self.assertEqual(len(edge["quote_sha256"]), 64)
            self.assertTrue(edge["quote"])
        self.assertIn("IN_UNIVERSE_ORDER_ONLY_FROM_CITED_QUOTES", r["flags"])
        self.assertIn("NO_REAL_WORLD_TO_FICTIONAL_TIME_CONVERSION", r["flags"])

    def test_lore_timeline_route_never_infers_lore_from_a_title_only(self):
        r = ask.ask("Compare the release and lore timelines for Bloomburrow")
        self.assertEqual(r["result"]["set"]["code"], "blb")
        self.assertEqual(r["result"]["two_chronology_axes"]["in_universe_relations_on_exact_linked_pages"], [])
        self.assertIn("NO_CITED_IN_UNIVERSE_EVENT_ON_LINKED_SAMPLE_PAGES", r["flags"])
        self.assertIsNone(r["result"]["two_chronology_axes"]["fictional_event_date_corresponding_to_set_release"])

    def test_dual_timeline_known_unlinked_and_unknown_sets_fail_closed(self):
        known = ask.ask("Compare the release and lore timelines for War of the Spark")
        self.assertEqual(known["confidence"], "QUALIFIED")
        self.assertIsNone(known["result"]["official_story_series"])
        self.assertEqual(known["result"]["two_chronology_axes"]["cited_in_universe_relations_total"], 0)
        self.assertIn("NO_OFFICIAL_TITLE_STORY_LINK_IN_BOUNDED_INDEX", known["flags"])
        missing = ask.ask("Compare the release and lore timelines for Zorblax Time Rift")
        self.assertEqual(missing["confidence"], "NOT_FOUND")
        self.assertIsNone(missing["result"]["set"])
        self.assertFalse(any("magic.wizards.com" in url for url in missing["sources"]))


if __name__ == "__main__":
    unittest.main()
