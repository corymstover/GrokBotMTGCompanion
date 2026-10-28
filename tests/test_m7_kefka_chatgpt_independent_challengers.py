"""Kefka independent 44 whole-100 research variants; no canonical owner approval."""
import hashlib
import json
import re
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIR = ROOT / "data/grixis/m7/independent_candidates"
INDEX = ROOT / "data/grixis/m7/independent_reviews/Kefka__Court_Mage_M7_Independent_Oracle_Index_20261024.json"
REPORT = ROOT / "data/grixis/m7/independent_reviews/Kefka__Court_Mage_ChatGPT_New_Challenger_Checkpoint_20261024.md"
BASE_SHA = "cd36192fedda7a4f54570fb8b8e4605147b40f9254e6985729097fc998f17b03"
STEM = "Kefka__Court_Mage_M7_"
PAIRS = {
    "Baseline": [],
    "Dualcaster_Over_Culling": [("Dualcaster Mage", "Culling the Weak")],
    "Chameleon_Over_DemonicCounsel": [("Chameleon, Master of Disguise", "Demonic Counsel")],
    "FleshDuplicate_Over_DemonicCounsel": [("Flesh Duplicate", "Demonic Counsel")],
    "GeneratorServant_Over_Culling": [("Generator Servant", "Culling the Weak")],
    "FireCovenant_Over_ToxicDeluge": [("Fire Covenant", "Toxic Deluge")],
    "Dualcaster_Chameleon_TwoSwap": [
        ("Dualcaster Mage", "Culling the Weak"), ("Chameleon, Master of Disguise", "Demonic Counsel")],
    "Dualcaster_FleshDuplicate_TwoSwap": [
        ("Dualcaster Mage", "Culling the Weak"), ("Flesh Duplicate", "Demonic Counsel")],
    "Generator_Chameleon_TwoSwap": [
        ("Generator Servant", "Culling the Weak"), ("Chameleon, Master of Disguise", "Demonic Counsel")],
    "Triple_With_FireCovenant_Stress": [
        ("Dualcaster Mage", "Culling the Weak"), ("Chameleon, Master of Disguise", "Demonic Counsel"),
        ("Fire Covenant", "Toxic Deluge")],
    "GlasspoolMimic_Over_DemonicCounsel": [
        ("Glasspool Mimic // Glasspool Shore", "Demonic Counsel")],
    "Naban_Over_DemonicCounsel": [("Naban, Dean of Iteration", "Demonic Counsel")],
    "Dualcaster_Glasspool_TwoSwap": [
        ("Dualcaster Mage", "Culling the Weak"), ("Glasspool Mimic // Glasspool Shore", "Demonic Counsel")],
    "Chameleon_Glasspool_TwoSwap": [
        ("Chameleon, Master of Disguise", "Culling the Weak"),
        ("Glasspool Mimic // Glasspool Shore", "Demonic Counsel")],
    "StepThrough_Over_DemonicCounsel": [("Step Through", "Demonic Counsel")],
    "Spellseeker_Over_DemonicCounsel": [("Spellseeker", "Demonic Counsel")],
    "StepThrough_Over_DiabolicIntent": [("Step Through", "Diabolic Intent")],
    "Spellseeker_Over_DiabolicIntent": [("Spellseeker", "Diabolic Intent")],
    "Dualcaster_StepThrough_TwoSwap": [
        ("Dualcaster Mage", "Culling the Weak"), ("Step Through", "Demonic Counsel")],
    "Dualcaster_Spellseeker_TwoSwap": [
        ("Dualcaster Mage", "Culling the Weak"), ("Spellseeker", "Demonic Counsel")],
    "Chameleon_StepThrough_TwoSwap": [
        ("Chameleon, Master of Disguise", "Culling the Weak"),
        ("Step Through", "Demonic Counsel")],
    "Dualcaster_StepThrough_FireCovenant_Triple": [
        ("Dualcaster Mage", "Culling the Weak"), ("Step Through", "Demonic Counsel"),
        ("Fire Covenant", "Toxic Deluge")],
    "Irma_Over_DemonicCounsel": [("Irma, Part-Time Mutant", "Demonic Counsel")],
    "Irma_Over_Culling": [("Irma, Part-Time Mutant", "Culling the Weak")],
    "Irma_Over_PhantasmalImage": [("Irma, Part-Time Mutant", "Phantasmal Image")],
    "Irma_Over_PhyrexianMetamorph": [("Irma, Part-Time Mutant", "Phyrexian Metamorph")],
    "Irma_StepThrough_TwoSwap": [
        ("Irma, Part-Time Mutant", "Culling the Weak"), ("Step Through", "Demonic Counsel")],
    "Irma_Dualcaster_TwoSwap": [
        ("Irma, Part-Time Mutant", "Demonic Counsel"), ("Dualcaster Mage", "Culling the Weak")],
    "Irma_Spellseeker_TwoSwap": [
        ("Irma, Part-Time Mutant", "Culling the Weak"), ("Spellseeker", "Demonic Counsel")],
    "Irma_StepThrough_Dualcaster_Triple": [
        ("Irma, Part-Time Mutant", "Phantasmal Image"), ("Dualcaster Mage", "Culling the Weak"),
        ("Step Through", "Demonic Counsel")],
    "Irma_Chameleon_StepThrough_Triple": [
        ("Irma, Part-Time Mutant", "Phantasmal Image"),
        ("Chameleon, Master of Disguise", "Culling the Weak"),
        ("Step Through", "Demonic Counsel")],
    "Irma_StepThrough_FireCovenant_Triple": [
        ("Irma, Part-Time Mutant", "Culling the Weak"),
        ("Step Through", "Demonic Counsel"), ("Fire Covenant", "Toxic Deluge")],
    "Irma_GeneratorServant_TwoSwap": [
        ("Irma, Part-Time Mutant", "Demonic Counsel"),
        ("Generator Servant", "Culling the Weak")],
    "GeneratorServant_StepThrough_TwoSwap": [
        ("Generator Servant", "Culling the Weak"),
        ("Step Through", "Demonic Counsel")],
    "Sakashima_Over_PhyrexianMetamorph": [
        ("Sakashima of a Thousand Faces", "Phyrexian Metamorph")],
    "Sakashima_Over_Culling": [
        ("Sakashima of a Thousand Faces", "Culling the Weak")],
    "Sakashima_Over_DemonicCounsel": [
        ("Sakashima of a Thousand Faces", "Demonic Counsel")],
    "FleshDuplicate_Over_PhyrexianMetamorph": [
        ("Flesh Duplicate", "Phyrexian Metamorph")],
    "Chameleon_Over_PhyrexianMetamorph": [
        ("Chameleon, Master of Disguise", "Phyrexian Metamorph")],
    "SparkDouble_Over_PhyrexianMetamorph": [
        ("Spark Double", "Phyrexian Metamorph")],
    "Sakashima_StepThrough_TwoSwap": [
        ("Sakashima of a Thousand Faces", "Phyrexian Metamorph"),
        ("Step Through", "Demonic Counsel")],
    "Sakashima_Generator_StepThrough_Triple": [
        ("Sakashima of a Thousand Faces", "Phyrexian Metamorph"),
        ("Generator Servant", "Culling the Weak"),
        ("Step Through", "Demonic Counsel")],
    "Sakashima_Chameleon_TwoSwap": [
        ("Sakashima of a Thousand Faces", "Phyrexian Metamorph"),
        ("Chameleon, Master of Disguise", "Culling the Weak")],
    "Sakashima_Irma_TwoSwap": [
        ("Sakashima of a Thousand Faces", "Phyrexian Metamorph"),
        ("Irma, Part-Time Mutant", "Culling the Weak")],
}


def read(key):
    suffix = "Baseline_Research_20261024.txt" if key == "Baseline" else key + "_Research_20261024.txt"
    raw = (DIR / (STEM + suffix)).read_bytes()
    assert raw.endswith(b"\n") and not raw.endswith(b"\n\n")
    lines = raw.decode("utf-8").splitlines()
    assert len(lines) == 100
    assert lines[0] == "1x Kefka, Court Mage // Kefka, Ruler of Ruin [Commander]"
    assert all(line.startswith("1x ") for line in lines)
    assert len(set(lines)) == 100
    return raw, [line.removeprefix("1x ").removesuffix(" [Commander]") for line in lines]


class KefkaIndependentChallengers(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.baseline_raw, cls.base = read("Baseline")
        cls.index = json.loads(INDEX.read_text(encoding="utf-8"))
        cls.report = REPORT.read_text(encoding="utf-8")

    def test_historical_baseline_raw_bytes_unchanged(self):
        self.assertEqual(hashlib.sha256(self.baseline_raw[:-1]).hexdigest(), BASE_SHA)
        self.assertEqual(len(self.base), 100)

    def test_all_forty_four_are_exact_full_100_with_only_staged_swaps(self):
        self.assertEqual(len(PAIRS), 44)
        base = Counter(self.base)
        for key, swaps in PAIRS.items():
            with self.subTest(configuration=key):
                raw, cards = read(key)
                self.assertEqual(len(cards), 100)
                expected = base.copy()
                for add, cut in swaps:
                    expected[cut] -= 1
                    expected[add] += 1
                    self.assertNotEqual(add, cut)
                self.assertEqual(Counter(cards), +expected)
                self.assertEqual(len(set(cards)), 100)
                self.assertEqual(cards.count("Kefka, Court Mage // Kefka, Ruler of Ruin"), 1)

    def test_source_bound_oracle_identity_and_legality(self):
        j = self.index
        self.assertEqual(j["source_date"], "2026-10-23")
        self.assertEqual(len(j["cards"]), 109)
        indexed = {c["name"]: c for c in j["cards"]}
        self.assertEqual(len(indexed), 109)
        external = j["external_card"]
        additional = j["additional_external_card"]
        third = j["third_external_card"]
        self.assertEqual(external["name"], "Chameleon, Master of Disguise")
        self.assertIn("gatherer.wizards.com", external["official_card_url"])
        self.assertEqual(additional["name"], "Irma, Part-Time Mutant")
        self.assertIn("magic.wizards.com", additional["official_rules_url"])
        self.assertEqual(third["name"], "Sakashima of a Thousand Faces")
        self.assertIn("magic.wizards.com", third["official_rules_url"])
        for key in PAIRS:
            _, names = read(key)
            with self.subTest(configuration=key):
                self.assertEqual(set(names) - set(indexed),
                                 {name for name in (external["name"], additional["name"],
                                                   third["name"]) if name in names})
        for card in j["cards"] + [external, additional, third]:
            with self.subTest(card=card["name"]):
                self.assertEqual(card["commander_legality"], "legal")
                self.assertTrue(set(card["color_identity"]) <= {"U", "B", "R"})
        _, base = read("Baseline")
        self.assertEqual(sum("Land" in indexed[n]["type_line"] for n in base), 28)
        self.assertEqual(sum(bool(indexed[n]["game_changer"]) for n in base), 20)

    def test_chameleon_mayhem_timing_and_name_caveat_reported(self):
        for term in ("Chameleon, Master of Disguise", "Mayhem", "eight mana", "own name",
                     "legend-rule", "regular creature casting timing", "not certified",
                     "no automatic acceptance", "only if discarded that turn"):
            with self.subTest(term=term):
                self.assertIn(term.lower(), self.report.lower())

    def test_other_risks_and_competing_cut_slots_disclosed(self):
        for term in ("Flesh Duplicate", "vanishing 3", "double blue", "Glasspool",
                     "tapped-only blue", "Generator Servant", "Culling the Weak",
                     "Demonic Counsel", "Fire Covenant", "Toxic Deluge",
                     "Naban", "Harmonic Prodigy", "owner-direction"):
            with self.subTest(term=term):
                self.assertIn(term.lower(), self.report.lower())

    def test_wizardcycling_and_spellseeker_exact_reachable_targets(self):
        j = {c["name"]: c for c in self.index["cards"]}
        step = j["Step Through"]
        self.assertEqual(step["mana_cost"], "{3}{U}{U}")
        self.assertIn("Wizardcycling {2}", step["oracle_text"])
        wizard_library = {name for name in self.base[1:] if "Wizard" in j[name]["type_line"]}
        self.assertEqual(wizard_library, {"Valley Floodcaller", "Gogo, Mysterious Mime",
                                          "Harmonic Prodigy", "Thassa's Oracle"})
        self.assertEqual(j["Demonic Counsel"]["mana_cost"], "{1}{B}")
        self.assertIn("four or more card types", j["Demonic Counsel"]["oracle_text"])
        self.assertIn("Demon card", j["Demonic Counsel"]["oracle_text"])
        seek = j["Spellseeker"]
        self.assertEqual(seek["mana_cost"], "{2}{U}")
        self.assertIn("mana value 2 or less", seek["oracle_text"])
        _, two = read("Dualcaster_StepThrough_TwoSwap")
        self.assertIn("Dualcaster Mage", two)
        self.assertIn("Step Through", two)
        self.assertNotIn("Culling the Weak", two)
        self.assertNotIn("Demonic Counsel", two)
        self.assertIn("does not", self.report.lower())

    def test_irma_exact_official_timing_limitations_stated(self):
        irma = self.index["additional_external_card"]
        self.assertEqual(irma["mana_cost"], "{2}{U}")
        self.assertIn("At the beginning of combat on your turn", irma["oracle_text"])
        self.assertIn("her name is Irma, Part-Time Mutant", irma["oracle_text"])
        self.assertIn("Then put a +1/+1 counter", irma["oracle_text"])
        for term in ("Irma, Part-Time Mutant", "already controlled", "no new ETB",
                     "Gogo", "not a commander", "attack trigger", "same-name legend rule",
                     "three mana", "RESEARCH_ONLY"):
            with self.subTest(term=term):
                self.assertIn(term.lower(), self.report.lower())

    def test_generator_step_through_pair_operational_boundaries(self):
        j = {c["name"]: c for c in self.index["cards"]}
        servant = j["Generator Servant"]
        self.assertEqual(servant["mana_cost"], "{1}{R}")
        self.assertIn("{T}, Sacrifice this creature: Add {C}{C}", servant["oracle_text"])
        self.assertIn("haste", servant["oracle_text"].lower())
        self.assertEqual(j["Kefka, Court Mage // Kefka, Ruler of Ruin"]["mana_cost"], "{2}{U}{B}{R}")
        _, cards = read("GeneratorServant_StepThrough_TwoSwap")
        self.assertIn("Generator Servant", cards)
        self.assertIn("Step Through", cards)
        self.assertNotIn("Culling the Weak", cards)
        self.assertNotIn("Demonic Counsel", cards)
        for term in ("turn two", "turn three", "U, B and R", "cannot normally tap",
                     "mulligan-free", "commander-first",
                     "conditional castability"):
            self.assertIn(term.lower(), self.report.lower())

    def test_ad_nauseam_curve_and_bargained_beseech_tradeoff(self):
        j = {c["name"]: c for c in self.index["cards"]}
        mana_values = {
            "Culling the Weak": 1,
            "Generator Servant": 2,
            "Demonic Counsel": 2,
            "Step Through": 5,
        }
        for name, mv in mana_values.items():
            with self.subTest(card=name):
                self.assertEqual(
                    sum(int(symbol) if symbol.isdigit() else 1
                        for symbol in re.findall(r"\{([^}]+)\}", j[name]["mana_cost"])),
                    mv)
        self.assertEqual(
            sum(mana_values[k] for k in ("Generator Servant", "Step Through"))
            - sum(mana_values[k] for k in ("Culling the Weak", "Demonic Counsel")),
            4)
        self.assertIn("mana value is 4 or less", j["Beseech the Mirror"]["oracle_text"])
        self.assertIn("You lose life equal to its mana value", j["Ad Nauseam"]["oracle_text"])
        self.assertEqual(j["Step Through"]["color_identity"], ["U"])
        for term in ("Ad Nauseam curve", "by four", "beseech the mirror",
                     "cannot free-cast", "twinflame", "cool but rude",
                     "both generator servant and culling the weak"):
            with self.subTest(term=term):
                self.assertIn(term.lower(), self.report.lower())

    def test_sakashima_suppresses_legend_rule_but_not_commander_identity(self):
        third = self.index["third_external_card"]
        self.assertEqual(third["mana_cost"], "{3}{U}")
        self.assertIn('The "legend rule" doesn\'t apply', third["oracle_text"])
        self.assertIn("except it has Sakashima of a Thousand Faces's other abilities",
                      third["oracle_text"])
        self.assertEqual(third["color_identity"], ["U"])
        _, cards = read("Sakashima_StepThrough_TwoSwap")
        self.assertEqual(cards.count("Kefka, Court Mage // Kefka, Ruler of Ruin"), 1)
        self.assertEqual(cards.count("Sakashima of a Thousand Faces"), 1)
        self.assertNotIn("Phyrexian Metamorph", cards)
        for term in ("Sakashima of a Thousand Faces", "same-name", "legend rule",
                     "Molten Duplication", "Saw in Half", "four mana",
                     "not a second commander", "not yet certified"):
            with self.subTest(term=term):
                self.assertIn(term.lower(), self.report.lower())

    def test_provisional_two_swap_raw_hash_and_full_100_source_gate(self):
        research_bytes, names = read("Sakashima_StepThrough_TwoSwap")
        raw = research_bytes[:-1]
        self.assertFalse(raw.endswith(b"\n"))
        self.assertEqual(
            hashlib.sha256(raw).hexdigest(),
            "14277f6e9774c5ef02b4f92332b52684794367007abf81bc2d84ef7ad7bcaa7d")
        self.assertIn("14277f6e9774c5ef02b4f92332b52684794367007abf81bc2d84ef7ad7bcaa7d",
                      self.report)
        oracle = {c["name"]: c for c in self.index["cards"]}
        for key in ("external_card", "additional_external_card", "third_external_card"):
            card = self.index[key]
            oracle[card["name"]] = card
        self.assertEqual(len(names), 100)
        self.assertEqual(len(set(names)), 100)
        self.assertEqual(sum("Land" in oracle[n]["type_line"] for n in names), 28)
        self.assertEqual(sum(bool(oracle[n]["game_changer"]) for n in names), 20)
        self.assertTrue(all(oracle[n]["commander_legality"] == "legal" for n in names))
        self.assertTrue(all(set(oracle[n]["color_identity"]) <= {"U", "B", "R"} for n in names))
        self.assertIn("No canonical PR", self.report)
        self.assertIn("not approval-ready", self.report)

    def test_floor_and_preservation(self):
        self.assertIn("RESEARCH_ONLY", self.report)
        self.assertIn("No owner-presentable M7 list", self.report)
        self.assertIn("five-swap minimum", self.report)
        self.assertIn("canonical change", self.report)
        self.assertLess(max(len(s) for s in PAIRS.values()), 5)


if __name__ == "__main__":
    unittest.main()
