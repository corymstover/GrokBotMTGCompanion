#!/usr/bin/env python3
"""Small offline regression tests for edition-aware lore discovery."""

import json
import tempfile
import unittest
from pathlib import Path

import lore_deep_research as D


class LoreDeepResearchTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.archive = self.root / "archive"
        self.archive.mkdir()
        self.profiles = self.root / "profiles"
        self.profiles.mkdir()
        (self.archive / "manifest.json").write_text(json.dumps({
            "shards": {"a-000.jsonl": {}}, "source": "synthetic-v1", "coverage": "synthetic English paper"}), encoding="utf-8")
        rows = [
            self.row("Corrupt", "usg", "124", "Yawgmoth brushed Urza's mind."),
            self.row("Corrupt", "m11", "89", "No Yawgmoth in this printing.".replace("Yawgmoth", "subject")),
            self.row("Phyrexian Tyranny", "pls", "118", "Yawgmoth rewarded Crovax with Ertai."),
            self.row("Phyrexian Broodlings", "ulg", "58", "Kerrick assembled beasts from parts."),
            self.row("Phyrexian Reclamation", "ulg", "63", "The dead return to serve."),
            self.row("Phyrexian Slayer", "inv", "118", "Tsabo Tavoc's ravagers devoured Benalia."),
            self.row("Other Phyrexian Scheme", "inv", "155", "Made for Phyrexia."),
            self.row("Unnamed", "m11", "1", "Not relevant."),
            self.row("Parody of Yawgmoth", "unh", "5", "And you thought Yawgmoth drove a hard bargain."),
        ]
        (self.archive / "a-000.jsonl").write_text("\n".join(json.dumps(r) for r in rows) + "\n", encoding="utf-8")
        profile = {"subject": "Yawgmoth", "signals": [
            {"term": "Yawgmoth", "relation": "subject", "phase": "I"},
            {"term": "Kerrick", "relation": "associated_character", "phase": "II"},
            {"term": "Tsabo Tavoc", "relation": "associated_character", "phase": "III"},
            {"term": "Phyrexia", "relation": "theme", "phase": "IV"},
        ], "pinned_printings": [
            {"card": "Phyrexian Tyranny", "set": "pls", "collector": "118", "phase": "III", "reason": "Verified invasion context"},
            {"card": "Phyrexian Reclamation", "set": "ulg", "collector": "63", "phase": "I", "reason": "Thematic link only"}
        ], "reading_sources": []}
        (self.profiles / "yawgmoth.json").write_text(json.dumps(profile), encoding="utf-8")

    def tearDown(self):
        self.temp.cleanup()

    @staticmethod
    def row(name, edition, collector, flavor):
        return {"n": name, "s": edition, "c": collector, "l": "en", "p": 1,
                "r": "2000-01-01", "id": edition + collector, "url": "https://example.org/" + edition,
                "faces": [{"n": name, "f": flavor}]}

    def test_variants_preserve_exact_printing_quotes(self):
        result = D.variants("Corrupt", self.archive)
        self.assertEqual(result["total_english_paper_printing_faces"], 2)
        self.assertEqual(result["distinct_flavor_variants_including_blank"], 2)
        earliest = next(v for v in result["flavor_variants"] if "Yawgmoth" in v["flavor_text"])
        self.assertEqual([(ed["set"], ed["collector"]) for ed in earliest["exact_printings"]], [("usg", "124")])

    def test_direct_alias_and_pinned_cards_are_found(self):
        result = D.deep_research("Yawgmoth", self.archive, profile_dir=self.profiles, limit=1)
        self.assertTrue(result["profile_used"])
        self.assertEqual(result["total_evidence_candidates"], 6)
        self.assertEqual(result["shown"], 1)
        all_cards = D.deep_research("Yawgmoth", self.archive, profile_dir=self.profiles, limit=30)
        by_name = {c["card"]: c for c in all_cards["candidates"]}
        self.assertEqual(by_name["Phyrexian Tyranny"]["score"], 125)
        self.assertEqual(by_name["Phyrexian Broodlings"]["score"], 90)
        self.assertEqual(by_name["Phyrexian Reclamation"]["score"], 85)
        self.assertEqual(by_name["Corrupt"]["flavor_variant_count_including_blank"], 2)
        one_flavor = D.deep_research("Yawgmoth", self.archive, profile_dir=self.profiles,
                                     max_variants=1, limit=20)
        relevant = next(c for c in one_flavor["candidates"] if c["card"] == "Corrupt")
        self.assertIn("Yawgmoth", relevant["flavor_variants"][0]["text"])
        self.assertIn("literal textual match", by_name["Phyrexian Slayer"]["evidence"][0]["qualification"])
        self.assertEqual(by_name["Phyrexian Tyranny"]["phase"], "III")

    def test_parody_can_be_opted_into_but_is_not_canon_by_default(self):
        regular = D.deep_research("Yawgmoth", self.archive, profile_dir=self.profiles, limit=20)
        self.assertNotIn("Parody of Yawgmoth", [r["card"] for r in regular["candidates"]])
        opt_in = D.deep_research("Yawgmoth", self.archive, profile_dir=self.profiles,
                                 limit=20, include_parody=True)
        self.assertIn("Parody of Yawgmoth", [r["card"] for r in opt_in["candidates"]])

    def test_gap_audit_excludes_present_cards(self):
        deck = self.root / "story.txt"
        deck.write_text("1x Ramos, Dragon Engine [Commander]\n1x Phyrexian Tyranny\n2x Swamp\n", encoding="utf-8")
        result = D.deep_research("Yawgmoth", self.archive, profile_dir=self.profiles,
                                 decklist=deck, limit=20)
        self.assertEqual(result["decklist_slots"], 4)
        self.assertEqual(result["total_not_in_deck"], 5)
        self.assertNotIn("Phyrexian Tyranny", [r["card"] for r in result["candidates"]])
        self.assertTrue(D._deck_has_card("Mishra, Claimed by Gix // Mishra, Lost to Phyrexia",
                                         {"mishra, claimed by gix"}))
        self.assertFalse(D._deck_has_card("Mishra, Claimed by Gix // Mishra, Lost to Phyrexia",
                                          {"urza, prince of kroog"}))

    def test_generic_subject_fallback_is_labeled(self):
        result = D.deep_research("Karn", self.archive, profile_dir=self.profiles, limit=10)
        self.assertFalse(result["profile_used"])
        self.assertEqual(result["total_evidence_candidates"], 0)

    def test_existing_lore_index_enrichments_are_discovered_but_labeled_editorial(self):
        index = self.root / "index.json"
        index.write_text(json.dumps({"items": [{"kind": "character", "name": "Yawgmoth",
            "page": "Characters Index.md", "anchor": "yawgmoth", "enriched_cards": ["Unnamed"],
            "links": {"arcs": ["Conflicts & Arcs.md#the-legacy"]}}]}), encoding="utf-8")
        result = D.deep_research("Yawgmoth", self.archive, profile_dir=self.profiles,
                                 index_path=index, limit=20)
        self.assertEqual(result["total_evidence_candidates"], 7)
        card = next(c for c in result["candidates"] if c["card"] == "Unnamed")
        self.assertEqual(card["score"], 70)
        self.assertEqual(card["evidence"][0]["qualification"],
                         "editorial link; neither literal quote nor direct event proof")
        self.assertEqual(result["linked_lore_entries"][0]["related_lore_links"]["arcs"],
                         ["Conflicts & Arcs.md#the-legacy"])


if __name__ == "__main__":
    unittest.main()
