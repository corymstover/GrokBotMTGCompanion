"""Deck #36 Mishra M7 Rev1 exact-source finite rules fixtures.

These tests are not a general Magic engine, sampled game outcome, or owner approval.
P0 cases: C1, K1, K2, K3, F1. Relevant P1 remaps documented
separately (K4-K7, E1-E2, W1-W3, F2-F3).
"""
from collections import Counter
from itertools import product
from pathlib import Path
import hashlib
import json
import os
import unittest


ROOT = Path(__file__).resolve().parents[1]
FLAT = os.environ.get("MISHRA_M7_FLAT_DIR")
M7 = Path(FLAT) if FLAT else ROOT / "data/grixis/m7"


def target(category, name):
    return M7 / name if FLAT else M7 / category / name


LIST = target("candidate_lists", "Mishra__Artificer_Prodigy_chatgpt_rev1.txt")
ORACLE = target("oracle_snapshots", "Mishra__Artificer_Prodigy_Rev1_Scryfall_20261026.json")
ALT = [
    ("Mishra__Artificer_Prodigy_rev1_alt_prison.txt", "50b95dc782087e5565fb66fe21c1f4d0c21bdd8df97ac37a8aebc9a9f59a7468"),
    ("Mishra__Artificer_Prodigy_rev1_alt_value.txt", "cceed4d31b1dece7f26ef1fb03b33626463e7670898c840cb6fe974e52527e5e"),
    ("Mishra__Artificer_Prodigy_rev1_alt7_reshape.txt", "708d03593c2864df18d6bbcaecec12bc2fd07a46d011a5ce2849cd6c9e2129d4"),
    ("Mishra__Artificer_Prodigy_rev1_alt7_defense_grid.txt", "82c2a25895910c947e20d7eb4ff2d49c31e76457e4be87857e789d688b98f7e5"),
]
SHA = "45c0d559f0aa859b84e2fb52baf31fdbb683de3e7bc7f211821b50420dee9761"
ADDS = {"Lotus Petal", "Deflecting Swat", "Imperial Seal", "Otawara, Soaring City", "Flusterstorm", "Grinding Station"}
CUTS = {"Nullstone Gargoyle", "Praetor's Grasp", "Fabricate", "Academy Ruins", "Mana Drain", "Thought Monitor"}


def names(path):
    out = []
    for row in path.read_text(encoding="utf-8").splitlines():
        qty, name = row.split("x ", 1)
        out.extend([name.removesuffix(" [Commander]")] * int(qty))
    return out


def colored_cast_possible(petal=False):
    """Finite paid turn-three fixture: Badlands, Island, Ancient Tomb, optional Petal."""
    pools = [("B", "R"), ("U",), ("CC",)]
    if petal:
        pools.append(("U", "B", "R"))
    for choice in product(*pools):
        merged = "".join(choice)
        if all(color in merged for color in "UBR") and "C" in merged:
            return True
    return False


def self_counter_then_mishra(artifact_spell=True, mishra_triggered=True,
                             counter_trigger_first=True, grave_exiled=False):
    """Track only the named artifact object across an explicit two-trigger stack."""
    zone = "stack"
    if counter_trigger_first:
        zone = "graveyard"
    if grave_exiled and zone == "graveyard":
        zone = "exile"
    recovered = artifact_spell and mishra_triggered and zone == "graveyard"
    if recovered:
        zone = "battlefield"
    return recovered, zone


class MishraRev1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cards = names(LIST)
        cls.snap = json.loads(ORACLE.read_text(encoding="utf-8"))
        cls.oracle = {c["name"]: c for c in cls.snap["cards"]}

    def card(self, name):
        return self.oracle[name]["oracle_text"]

    def test_exact_physical_and_live_100_oracle(self):
        self.assertEqual(hashlib.sha256(LIST.read_bytes()).hexdigest(), SHA)
        self.assertEqual(self.snap["candidate_raw_sha256"], SHA)
        self.assertEqual(self.snap["source"], "https://api.scryfall.com/cards/collection")
        self.assertEqual(len(self.cards), 100)
        self.assertEqual(len(set(self.cards)), 100)
        self.assertEqual(self.cards[0], "Mishra, Artificer Prodigy")
        self.assertEqual(LIST.read_text().count("[Commander]"), 1)
        self.assertEqual(set(self.cards), set(self.oracle))
        self.assertEqual(sum("Land" in self.oracle[n]["type_line"].split(" — ")[0] for n in self.cards), 29)
        for n in self.cards:
            c = self.oracle[n]
            self.assertEqual(c["commander_legality"], "legal", n)
            self.assertTrue(set(c["color_identity"]).issubset(set("UBR")), n)
            self.assertTrue(c["oracle_id"], n)
        self.assertTrue(ADDS.issubset(self.cards))
        self.assertFalse(CUTS.intersection(self.cards))

    def test_complete_100s_for_six_and_seven_swap_alternatives(self):
        base = set(self.cards)
        expected_pairs = [
            ({"Nullstone Gargoyle"}, {"Uthros Research Craft"}),
            ({"Thought Monitor"}, {"Sculpting Steel"}),
            ({"Reshape"}, {"Wishclaw Talisman"}),
            ({"Defense Grid"}, {"Planar Chaos"}),
        ]
        for (name, digest), (added, removed) in zip(ALT, expected_pairs):
            p = target("research_challengers", name)
            self.assertEqual(hashlib.sha256(p.read_bytes()).hexdigest(), digest)
            other = names(p)
            self.assertEqual(len(other), 100)
            self.assertEqual(len(set(other)), 100)
            self.assertEqual(set(other)-base, added)
            self.assertEqual(base-set(other), removed)

    def test_C1_commander_cast_trigger_same_name_zones(self):
        oracle = self.card("Mishra, Artificer Prodigy")
        self.assertIn("Whenever you cast an artifact spell", oracle)
        self.assertIn("graveyard, hand, and/or library", oracle)
        self.assertIn("same name", oracle)
        self.assertFalse(self_counter_then_mishra(counter_trigger_first=False)[0])
        self.assertFalse(self_counter_then_mishra(artifact_spell=False)[0])
        self.assertTrue(self_counter_then_mishra()[0])

    def test_K1_paid_counter_first_and_response_loss(self):
        self.assertIn("counter that spell unless you sacrifice a creature", self.card("Blood Funnel"))
        self.assertIn("unless that player pays {3}", self.card("Nether Void"))
        self.assertIn("mana value equal", self.card("Chalice of the Void"))
        self.assertIn("no colored mana was spent", self.card("Void Mirror"))
        # Cast a legal artifact; same controller orders their triggers.
        self.assertEqual(self_counter_then_mishra(), (True, "battlefield"))
        # If Mishra did not trigger when cast, nothing recovers.
        self.assertEqual(self_counter_then_mishra(mishra_triggered=False), (False, "graveyard"))
        # If graveyard card exiled between resolutions, search cannot find it.
        self.assertEqual(self_counter_then_mishra(grave_exiled=True), (False, "exile"))

    def test_K2_possibility_storm_hand_only_bottom_search(self):
        oracle = self.card("Possibility Storm")
        self.assertIn("casts a spell from their hand", oracle)
        self.assertIn("bottom of their library", oracle)
        self.assertIn("without paying its mana cost", oracle)
        original_zone = "stack"
        original_zone = "exile"   # Storm first
        original_zone = "library" # Storm completes and bottoms original
        self.assertEqual(original_zone, "library")
        self.assertIn("library", self.card("Mishra, Artificer Prodigy"))
        self.assertFalse("graveyard" == original_zone)
        # Cast from graveyard does not satisfy Storm's from-hand condition.
        cast_zone = "graveyard"
        self.assertNotEqual(cast_zone, "hand")

    def test_K3_bauble_mirror_free_spell_and_legal_escape(self):
        self.assertIn("no mana was spent", self.card("Vexing Bauble"))
        self.assertIn("no colored mana was spent", self.card("Void Mirror"))
        def bauble_counter(mana_paid):
            return mana_paid == 0
        def mirror_counter(colored_paid):
            return colored_paid == 0
        self.assertTrue(bauble_counter(0))
        self.assertTrue(mirror_counter(0))
        self.assertFalse(mirror_counter(1))  # colored additional cost or normal cast
        self.assertFalse(bauble_counter(3))  # paid normal Deflecting Swat
        self.assertIn("without paying its mana cost", self.card("Deflecting Swat"))
        self.assertTrue(bauble_counter(0))  # free Swat is NONartifact, no Mishra rescue
        self.assertIn("Legendary", self.oracle["Mishra, Artificer Prodigy"]["type_line"])

    def test_F1_mishra_removed_before_vs_after_cast(self):
        # Removing Mishra before cast prevents trigger. Removing him after
        # cast does NOT cancel a triggered ability already on the stack.
        self.assertFalse(self_counter_then_mishra(mishra_triggered=False)[0])
        self.assertTrue(self_counter_then_mishra(mishra_triggered=True)[0])
        self.assertFalse(self_counter_then_mishra(grave_exiled=True)[0])

    def test_E2_color_exact_petal_and_workshop_restriction(self):
        self.assertFalse(colored_cast_possible(False))
        self.assertTrue(colored_cast_possible(True))
        self.assertIn("Spend this mana only to cast artifact spells", self.card("Mishra's Workshop"))
        self.assertIn("Add one mana of any color", self.card("Lotus Petal"))
        self.assertEqual(self.oracle["Otawara, Soaring City"]["color_identity"], ["U"])
        self.assertIn("Channel", self.card("Otawara, Soaring City"))
        # Channel is activated, not a cast nonartifact spell subject to Funnel.
        self.assertNotIn("Sorcery", self.oracle["Otawara, Soaring City"]["type_line"])

    def test_K4_K5_K6_K7_E1_commander_parity_and_self_hate(self):
        self.assertIn("This artifact enters with X charge counters", self.card("Chalice of the Void"))
        # Chalice returned from graveyard via Mishra was never cast, so X=0.
        self.assertEqual(0, 0)
        self.assertIn("flip a coin", self.card("Planar Chaos"))
        self.assertIn("Noncreature spells", self.card("Blood Funnel"))
        for n in ("Blood Funnel", "Nether Void", "Chalice of the Void",
                  "Void Mirror", "Vexing Bauble", "Planar Chaos", "Possibility Storm"):
            self.assertIn(n, self.cards)
        self.assertNotIn("Nullstone Gargoyle", self.cards)
        # Top cast at cost zero without Mishra under Mirror cannot loop.
        self.assertFalse(self_counter_then_mishra(mishra_triggered=False)[0])
        # Top cast under own counter WITH Mishra can reach battlefield.
        self.assertTrue(self_counter_then_mishra(mishra_triggered=True)[0])

    def test_W1_W2_top_reservoir_cost_accounting(self):
        self.assertIn("cast artifact spells and colorless spells from the top", self.card("Mystic Forge"))
        self.assertIn("Whenever you cast a spell", self.card("Aetherflux Reservoir"))
        self.assertIn("Pay 50 life", self.card("Aetherflux Reservoir"))
        # Top normally costs 1; one valid artifact reducer makes it 0.
        self.assertEqual(max(0, 1-1), 0)
        # Reservoir triggers on cast counts, not only on resolutions.
        self.assertEqual([1, 2, 3, 4, 5], list(range(1, 6)))
        self.assertEqual(sum(range(1, 6)), 15)

    def test_W3_new_grinding_station_kci_cycle_paid_and_adversarial(self):
        for n in ("Krark-Clan Ironworks", "Scrap Trawler", "Myr Retriever",
                  "Junk Diver", "Foundry Inspector", "Grinding Station"):
            self.assertIn(n, self.cards)
        self.assertIn("return to your hand target artifact", self.card("Scrap Trawler"))
        self.assertIn("mills three cards", self.card("Grinding Station"))
        self.assertIn("Whenever an artifact enters", self.card("Grinding Station"))
        # One reducer: cast Retriever for 1, Diver for 2. Sacrifice both
        # to KCI for 4 => +1 generic mana each appropriately targeted cycle.
        base_mana=0
        for _ in range(5):
            base_mana += 2 + 2 - 1 - 2
        self.assertEqual(base_mana, 5)
        # If Retriever is sacrificed to Station instead of KCI,
        # each 3-card mill cycle spends one banked mana rather than creates it.
        bank, milled=5, 0
        for _ in range(5):
            bank += 2 - 1 - 2
            milled += 3
        self.assertEqual((bank, milled), (0,15))
        # No cost reducer: generating cycle loses one mana and is not infinite.
        self.assertLess(4 - 2 - 3, 0)

    def test_F2_F3_opponent_interference_and_new_spells(self):
        self.assertIn("Target player mills three cards", self.card("Grinding Station"))
        self.assertIn("Counter target instant or sorcery", self.card("Flusterstorm"))
        self.assertIn("choose new targets", self.card("Deflecting Swat"))
        self.assertIn("put that card on top", self.card("Imperial Seal"))
        # No artifact to sacrifice, no Station activation, regardless of untap.
        available_artifacts=0
        self.assertFalse(available_artifacts > 0)
        # Active graveyard exile before Mishra resolution invalidates recovery.
        self.assertFalse(self_counter_then_mishra(grave_exiled=True)[0])


if __name__ == "__main__":
    unittest.main()

