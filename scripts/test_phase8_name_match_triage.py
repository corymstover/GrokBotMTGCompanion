"""Small offline tests: research leads must never be labeled as canon approvals."""
import unittest

import lore_quotes as Q
import phase8_name_match_triage as T


def sample(card_name, person="Koth"):
    return {"cards": {"card-id": {"name": card_name, "lore": {"relations": [
        {"entry": "Characters Index.md#koth", "kind": "character", "name": person,
         "relation": "name-match", "sources": [], "via": "name", "line_flags": []}]}}}}


class NameMatchTriageTests(unittest.TestCase):
    def test_exact_card_title_on_official_page_is_candidate_only(self):
        data = sample("Koth of the Hammer")
        stories = {"https://magic.wizards.com/en/story/koth-planeswalker":
                   "koth of the hammer is a freedom fighter."}
        report = T.triage(data, stories, Q.norm)
        self.assertEqual(report["pending_links_examined"], 1)
        self.assertEqual(report["official_page_candidates"], 1)
        self.assertFalse(report["evidence_is_canon_approval"])

    def test_character_name_alone_is_not_a_card_confirmation(self):
        report = T.triage(sample("Koth of the Hammer"),
                          {"https://magic.wizards.com/en/story/koth-planeswalker":
                           "koth is a freedom fighter."}, Q.norm)
        self.assertEqual(report["official_page_candidates"], 0)
        self.assertEqual(report["links_without_new_page_candidate"], 1)


if __name__ == "__main__":
    unittest.main()
