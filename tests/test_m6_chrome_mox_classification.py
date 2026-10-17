"""Regression tests: conditional Chrome Mox is fast mana but not guaranteed color."""
import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_mana_base as mana


class TestConditionalChromeMox(unittest.TestCase):
    @staticmethod
    def sample(name="Chrome Mox",oracle=None):
        return {"name":name,"mana_cost":"{0}","mv":0,"type_line":"Artifact",
                "oracle":oracle or
                "Imprint — When this artifact enters, you may exile a nonartifact, nonland card from your hand.\n"
                "{T}: Add one mana of any of the exiled card's colors.",
                "color_identity":"C"}

    def test_chrome_mox_potential_mana_with_dependency(self):
        c=mana.classify(self.sample(),set("UBR"))
        self.assertTrue(c["fast_mana"])
        self.assertTrue(c["repeatable_nonland_source"])
        self.assertTrue(c["imprint_dependent_mana"])
        self.assertTrue(c["conditional_source"])
        self.assertEqual(c["source_colors"],"UBR")
        self.assertNotIn("C",c["source_colors"])
        self.assertEqual(c["source_amount_proxy"],1)

    def test_deck_identity_restricts_potential_color(self):
        c=mana.classify(self.sample(),set("UR"))
        self.assertEqual(c["source_colors"],"UR")
        self.assertTrue(c["conditional_source"])

    def test_imprint_text_required(self):
        c=mana.classify(self.sample(oracle="{T}: Add one mana of any of the exiled card's colors."),set("UBR"))
        self.assertFalse(c["imprint_dependent_mana"])
        self.assertFalse(c["fast_mana"])

    def test_not_any_other_card_with_same_text(self):
        c=mana.classify(self.sample(name="Invented Card"),set("UBR"))
        self.assertFalse(c["imprint_dependent_mana"])

    def test_real_frozen_card_text(self):
        card=mana.CardDB().get("Chrome Mox")
        c=mana.classify(card,set("UBR"))
        self.assertTrue(c["fast_mana"])
        self.assertTrue(c["imprint_dependent_mana"])
        self.assertTrue(c["conditional_source"])

    def test_unrelated_fast_mana_not_reclassified(self):
        for name in ("Sol Ring","Arcane Signet","Lotus Petal","Mox Diamond","Mox Opal"):
            try:
                card=mana.CardDB().get(name)
            except KeyError:
                continue
            c=mana.classify(card,set("UBR"))
            self.assertFalse(c["imprint_dependent_mana"])


if __name__=="__main__":
    unittest.main()
