import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from story_deck_planner import assemble, plan, themes


TIME = """### Post-Mending (Gatewatch era)
| # | Arc | Source |
|---|---|---|
| 1 | [Conflux](Conflicts%20%26%20Arcs.md#conflux-of-alara) | [Story](https://magic.wizards.com/en/story/alara-plane) |
### Phyrexian Invasion
| Order | Phase | Source |
|---|---|---|
| 1 | [ONE](Conflicts%20%26%20Arcs.md#phyrexia-all-will-be-one-2023) | [Story](https://magic.wizards.com/en/story/phyrexia-plane) |
### Omenpath era (post-invasion)
| Relative marker | Arc | Source |
|---|---|---|
| unplaced ⚠️ | [RF](Conflicts%20%26%20Arcs.md#jaces-echoverse-reality-fracture) | [Story](https://magic.wizards.com/en/story/ravnica-plane) |
| after TDM | [TDM](Conflicts%20%26%20Arcs.md#tarkir-dragonstorm-2025) | Bolas and Ugin vanish; this is a curated row, not independent proof. |
"""


def entry(page, name, anchor, kind, links=None, enriched=()):
    return {"page": page, "name": name, "anchor": anchor, "kind": kind,
            "links": links or {}, "enriched_cards": list(enriched), "flags": {}}


class StoryDeckPlannerTests(unittest.TestCase):
    def test_short_summary_title_yields_real_arc_beats(self):
        index = {"items": [
            entry("Story Arc Summaries.md", "March of the Machine", "march-of-the-machine", "summary"),
            entry("Conflicts & Arcs.md", "March of the Machine (2023)", "march-of-the-machine-2023", "arc"),
        ]}
        result = plan("March of the Machine", index, TIME)
        self.assertEqual(result["beat_total"], 1)
        self.assertEqual(result["beats"][0]["title"], "March of the Machine (2023)")
        self.assertIn("summary_heading_name_match_contextual", result["beats"][0]["discovery_evidence"])

    def test_shipped_karn_example_is_complete_but_not_auto_approved(self):
        path = Path(__file__).resolve().parents[1] / "data/lore_decks/examples/karn_life_story_draft.json"
        spec = json.loads(path.read_text(encoding="utf-8"))
        result = assemble(spec)
        self.assertEqual(result["total"], 100)
        self.assertEqual(result["validation"]["status"], "not_run")
        names = result["decklist"].splitlines()
        self.assertFalse(any("Mycosynth Lattice" in row for row in names))
        self.assertEqual(result["basic_slots"], 19)
        self.assertEqual(len(result["reasons"]), 80)
        self.assertTrue(all(card.get("source", "").startswith("https://scryfall.com/card/")
                            for beat in spec["beats"] for card in beat["cards"]))

    def test_dual_subject_story_beats_have_distinct_evidence_and_order_caveats(self):
        index = {"items": [
            entry("Characters Index.md", "Nicol Bolas", "nicol-bolas", "character",
                  {"arcs": ["Conflicts & Arcs.md#conflux-of-alara", "Conflicts & Arcs.md#jaces-echoverse-reality-fracture"]},
                  ["Nicol Bolas, Dragon-God"]),
            entry("Characters Index.md", "Ugin", "ugin", "character",
                  {"arcs": ["Conflicts & Arcs.md#conflux-of-alara"]}, ["Ugin, the Spirit Dragon"]),
            entry("Conflicts & Arcs.md", "Conflux of Alara", "conflux-of-alara", "arc",
                  {"eras": ["Master Timeline.md#post-mending-gatewatch-era"]}),
            entry("Conflicts & Arcs.md", "Jace's Echoverse", "jaces-echoverse-reality-fracture", "arc",
                  {"eras": ["Master Timeline.md#omenpath-era-post-invasion"]}),
            entry("Conflicts & Arcs.md", "Tarkir: Dragonstorm (2025)", "tarkir-dragonstorm-2025", "arc",
                  {"eras": ["Master Timeline.md#omenpath-era-post-invasion"]}),
        ]}
        result = plan("Ugin vs Nicol Bolas", index, TIME)
        self.assertEqual(themes("Ugin/Nicol Bolas"), ["Ugin", "Nicol Bolas"])
        self.assertEqual(len(result["beats"]), 3)
        self.assertEqual(result["beats"][0]["title"], "Conflux of Alara")
        self.assertEqual(result["beats"][1]["timeline"]["ordering_rule"], "relative_markers_only_not_a_total_order")
        self.assertIn("same_timeline_row_mentions_requested_names_contextual_only", result["beats"][2]["discovery_evidence"])
        self.assertIn("not a globally proven", result["ordering_warning"])

    def test_assembly_can_be_complete_but_unverified(self):
        spec = {"theme": "Karn", "commander": "Karn, Legacy Reforged",
                "beats": [{"title": "Mirrodin", "lore_keys": ["Conflicts & Arcs.md#mirrodin"],
                           "cards": [{"name": "Karn, Silver Golem", "why": "the original golem",
                                      "evidence": "curated_entry", "source": "Characters Index.md#karn"}]}],
                "basics": {"Wastes": 98}}
        result = assemble(spec)
        self.assertEqual(result["total"], 100)
        self.assertEqual(result["validation"]["status"], "not_run")
        self.assertIn("[Commander]", result["decklist"])
        validated = assemble(spec, lambda text: {"total": 100, "ci": "", "issues": [], "hard_types": ["deck size"]})
        self.assertEqual(validated["validation"]["status"], "passed")
        bad = assemble({**spec, "basics": {"Wastes": 97}})
        self.assertEqual(bad["validation"]["status"], "incomplete")

    def test_no_unsupported_direct_source_or_implicit_duplicate(self):
        spec = {"commander": "Karn, Legacy Reforged", "beats": [{"title": "Karn", "lore_keys": ["X#karn"],
                "cards": [{"name": "Urza's Saga", "why": "echo", "evidence": "direct_official", "source": "made up"}]}]}
        with self.assertRaises(ValueError):
            assemble(spec)
        spec["beats"][0]["cards"][0]["evidence"] = "contextual_pointer"
        spec["playability"] = [{"name": "Urza's Saga", "why": "support"}]
        with self.assertRaises(ValueError):
            assemble(spec)


if __name__ == "__main__":
    unittest.main()
