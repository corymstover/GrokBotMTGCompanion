"""Exact 100-card Scryfall transaction and commander-effect regression checks.

Snapshot was retrieved 2026-10-26 UTC using Scryfall collection and exact
named endpoints. This is a source-bound historical snapshot, not an auto-
refreshing Magic rules engine or an independently reproduced game simulation.
"""
import hashlib
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DECK = ROOT / "data/grixis/m7/candidate_lists/Marchesa_Dealer_of_Death_chatgpt_rev1.txt"
ORACLE = ROOT / "data/grixis/m7/oracle_snapshots/Marchesa_Dealer_of_Death_Rev1_Scryfall_20261026.json"
SHA = "f6f68d204925ef3528166722d874cd4122e50755b30f8b9a9ac19d7eff9afd3e"


class TestMarchesaOracle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.snapshot = json.loads(ORACLE.read_text(encoding="utf-8"))
        cls.records = {c["decklist_name"]: c for c in cls.snapshot["records"]}

    def oracle(self, name):
        c = self.records[name]
        return c.get("oracle_text", "\n".join(f["oracle_text"] for f in c.get("faces", [])))

    def test_exact_sha_names_identity_commander_legality_and_oracle_id(self):
        self.assertEqual(hashlib.sha256(DECK.read_bytes()).hexdigest(), SHA)
        self.assertEqual(self.snapshot["candidate_raw_sha256"], SHA)
        names = [s.removeprefix("1x ").removesuffix(" [Commander]")
                 for s in DECK.read_text(encoding="utf-8").splitlines()]
        self.assertEqual(len(names), 100)
        self.assertEqual(len(set(names)), 100)
        self.assertEqual(set(names), set(self.records))
        self.assertEqual(self.snapshot["card_count"], 100)
        self.assertEqual(self.snapshot["commander_legal_count"], 100)
        self.assertEqual(self.snapshot["grixis_color_identity_count"], 100)
        self.assertEqual(self.snapshot["exceptions"], [])
        for name, record in self.records.items():
            self.assertEqual(record["commander_legality"], "legal", name)
            self.assertFalse(set(record["color_identity"]) - set("UBR"), name)
            self.assertTrue(record["oracle_id"], name)
            self.assertTrue(record["scryfall_id"], name)
            self.assertTrue(self.oracle(name).strip(), name)
        self.assertIn("Legendary Creature", self.records["Marchesa, Dealer of Death"]["type_line"])

    def test_p0_crime_trigger_cost_top_two_and_target_status(self):
        marchesa = self.oracle("Marchesa, Dealer of Death")
        self.assertIn("Whenever you commit a crime, you may pay {1}", marchesa)
        self.assertIn("top two cards", marchesa)
        self.assertIn("Put one of them into your hand and the other into your graveyard", marchesa)
        self.assertIn("Targeting opponents", marchesa)
        self.assertIn("Remove up to X counters from target permanent", self.oracle("Hex Parasite"))
        self.assertIn("Pay 1 life", self.oracle("Spatial Binding"))
        self.assertIn("target permanent can't phase out", self.oracle("Spatial Binding"))

    def test_p1_repeatable_crime_source_oracle_bound(self):
        self.assertIn("Whenever a player casts a blue spell", self.oracle("Lapis Lazuli Talisman"))
        self.assertIn("untap target permanent", self.oracle("Lapis Lazuli Talisman"))
        self.assertIn("Untap target artifact or creature", self.oracle("Tezzeret, Cruel Captain"))
        self.assertIn("Whenever you commit a crime, create a tapped Treasure", self.oracle("Magda, the Hoardmaster"))
        self.assertIn("triggers only once each turn", self.oracle("Magda, the Hoardmaster"))
        self.assertIn("target creature phases out", self.oracle("Talon Gates of Madara"))
        self.assertIn("Target creature loses first strike or swampwalk", self.oracle("Urborg"))
        self.assertIn("Target player exiles a card from their graveyard", self.oracle("Scrabbling Claws"))
        self.assertIn("Exile target card from a graveyard", self.oracle("Scrabbling Claws"))
        self.assertIn("a player sacrifices a permanent", self.oracle("Mayhem Devil"))
        self.assertIn("to any target", self.oracle("Mayhem Devil"))
        self.assertIn("target creature an opponent controls", self.oracle("Gilded Drake"))
        self.assertIn("target nonblack creature", self.oracle("Snuff Out"))
        self.assertIn("Return target spell or nonland permanent an opponent controls", self.oracle("Sink into Stupor // Soporific Springs"))

    def test_p1_three_win_family_oracle_and_adversarial_limitations(self):
        self.assertIn("your devotion to blue", self.oracle("Thassa's Oracle"))
        self.assertIn("Exile the top six cards", self.oracle("Demonic Consultation"))
        self.assertIn("Exile the top card of your library", self.oracle("Tainted Pact"))
        self.assertIn("Each nonland card in your graveyard has escape", self.oracle("Underworld Breach"))
        self.assertIn("exile three other cards from your graveyard", self.oracle("Underworld Breach"))
        self.assertIn("Discard your hand, Sacrifice this artifact", self.oracle("Lion's Eye Diamond"))
        self.assertIn("Target player mills three cards", self.oracle("Brain Freeze"))
        self.assertIn("Untap target artifact or creature", self.oracle("Aphetto Alchemist"))
        self.assertIn("Whenever equipped creature becomes tapped", self.oracle("Hawkeye's Bow"))
        self.assertIn("1 damage to each opponent", self.oracle("Hawkeye's Bow"))

    def test_p1_land_faces_and_new_card_oracle(self):
        self.assertEqual(self.records["Sink into Stupor // Soporific Springs"]["type_line"], "Instant // Land")
        self.assertEqual(len(self.records["Sink into Stupor // Soporific Springs"]["faces"]), 2)
        self.assertEqual(len(self.records["Birgi, God of Storytelling"]["faces"]), 2)
        self.assertIn("Search your library for a Plains or Swamp card", self.oracle("Marsh Flats"))
        self.assertIn("You control your opponents while they're searching their libraries", self.oracle("Opposition Agent"))


if __name__ == "__main__":
    unittest.main()
