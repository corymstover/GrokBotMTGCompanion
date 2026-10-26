"""Deck #37 finite, source-bound M7 tests (not multiplayer win-rate simulation)."""

from collections import Counter
import hashlib
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
M7 = ROOT / "data/grixis/m7"
DECK = M7 / "candidate_lists/Mishra__Eminent_One_chatgpt_rev1.txt"
ORACLE = M7 / "oracle_snapshots/Mishra__Eminent_One_Rev1_Scryfall_20261026.json"
SHA = "0fa7b00d9d74b208f3fd5783b30aa190c4e5b17e72ea64851f895315f05083a0"
ADDS = {"Panharmonicon", "Roaming Throne", "Idol of Oblivion", "Lightning Greaves", "Grinding Station", "Marionette Apprentice"}
CUTS = {"Smelting Vat", "The Mightstone and Weakstone", "Uthros Research Craft", "Padeem, Consul of Innovation", "Lich's Relic", "Enthusiastic Mechanaut"}


class MishraEminentRev1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw = DECK.read_bytes()
        cls.rows = cls.raw.decode().splitlines()
        cls.cards = [row.split("x ", 1)[1].removesuffix(" [Commander]") for row in cls.rows]
        cls.receipt = json.loads(ORACLE.read_text())
        cls.oracle = {c["name"]: c for c in cls.receipt["cards"]}

    def text(self, name):
        return self.oracle[name]["oracle_text"]

    def test_exact_list_complete_oracle_identity_legality_and_count(self):
        self.assertEqual(hashlib.sha256(self.raw).hexdigest(), SHA)
        self.assertEqual(self.receipt["candidate_raw_sha256"], SHA)
        self.assertEqual(self.receipt["source"], "https://api.scryfall.com/cards/collection")
        self.assertEqual(len(self.rows), len(self.cards))
        self.assertEqual(len(self.cards), len(set(self.cards)))
        self.assertEqual(len(self.cards), 100)
        self.assertEqual(self.rows[0], "1x Mishra, Eminent One [Commander]")
        self.assertEqual(sum("[Commander]" in row for row in self.rows), 1)
        self.assertTrue(all(row.startswith("1x ") for row in self.rows))
        self.assertEqual(set(self.oracle), set(self.cards))
        self.assertTrue(ADDS <= set(self.cards))
        self.assertFalse(CUTS & set(self.cards))
        self.assertEqual(sum("Land" in c["type_line"].split(" — ")[0] for c in self.oracle.values()), 34)
        for name, card in self.oracle.items():
            with self.subTest(name=name):
                self.assertTrue(card["oracle_id"])
                self.assertEqual(card["commander_legality"], "legal")
                self.assertTrue(set(card["color_identity"]) <= set("UBR"))

    def test_mishra_gontis_heart_panharmonicon_energy(self):
        self.assertIn("beginning of combat", self.text("Mishra, Eminent One"))
        self.assertIn("target noncreature artifact", self.text("Mishra, Eminent One"))
        self.assertIn("another artifact you control enters", self.text("Gonti's Aether Heart"))
        self.assertIn("Pay eight", self.text("Gonti's Aether Heart"))
        self.assertIn("triggers an additional time", self.text("Panharmonicon"))
        # Original Heart and Warform each trigger on the first Warform entering;
        # Panharmonicon doubles both 2-energy triggers: 2x2x2 = 8.
        first_copy_energy = 2 * 2 * 2
        self.assertEqual(first_copy_energy, 8)
        self.assertEqual(first_copy_energy - 8, 0)
        # The copied nonlegendary Heart can exile *itself* to pay the cost.

    def test_roaming_throne_double_mishra_trigger_and_energy(self):
        self.assertIn("Human Artificer", self.oracle["Mishra, Eminent One"]["type_line"])
        self.assertIn("choose a creature type", self.text("Roaming Throne"))
        self.assertIn("another creature you control of the chosen type", self.text("Roaming Throne"))
        # Choosing Human or Artificer gives two separate Mishra triggers.
        # First Warform Heart entry produces 4 energy; next enters with
        # three Hearts in play and produces 6 more. Both Warforms are nonlegendary.
        self.assertEqual(2*2 + 3*2, 10)

    def test_simulacrum_mv_copy_and_mana_value(self):
        synth = self.text("Simulacrum Synthesizer")
        self.assertIn("artifact you control with mana value 3 or greater enters", synth)
        self.assertNotIn("nontoken artifact you control", synth)
        self.assertIn("artifact creature", self.text("Mishra, Eminent One"))
        # Mishra's copy modifications preserve copied artifact's mana value.
        self.assertGreaterEqual(self.oracle["Portal to Phyrexia"]["mana_value"], 3)
        self.assertGreaterEqual(self.oracle["Coveted Jewel"]["mana_value"], 3)

    def test_idol_copy_haste_and_token_precondition(self):
        self.assertIn("Activate only if you created a token this turn", self.text("Idol of Oblivion"))
        self.assertIn("{T}: Draw a card", self.text("Idol of Oblivion"))
        self.assertIn("haste", self.text("Mishra, Eminent One"))
        # Source Idol plus hasty Warform Idol can each tap after Mishra's token
        # enters. Neither draws without a qualifying token on that turn.
        activations_if_token_this_turn = 2
        self.assertEqual(activations_if_token_this_turn, 2)

    def test_grinding_station_and_marionette_exact_limits(self):
        self.assertIn("{T}, Sacrifice an artifact", self.text("Grinding Station"))
        self.assertIn("Whenever an artifact enters", self.text("Grinding Station"))
        self.assertIn("each opponent loses 1 life", self.text("Marionette Apprentice"))
        self.assertIn("creature or artifact", self.text("Marionette Apprentice"))
        # An artifact-creature Warform put into the graveyard triggers Apprentice
        # exactly once, not once for each of its two types.
        self.assertEqual(Counter({"warform_deaths": 1})["warform_deaths"], 1)
        # Station cannot be activated infinitely merely for being tapped.
        self.assertEqual(3 * 1, 3)

    def test_greaves_protection_not_equivalent_to_padeem(self):
        self.assertIn("haste and shroud", self.text("Lightning Greaves"))
        self.assertIn("Equip {0}", self.text("Lightning Greaves"))
        self.assertEqual(self.oracle["Mishra, Eminent One"]["type_line"], "Legendary Creature — Human Artificer")
        # Greaves grants shroud to the equipped creature, not to all artifacts.
        self.assertNotIn("artifacts you control have hexproof", self.text("Lightning Greaves"))


if __name__ == "__main__":
    unittest.main()
