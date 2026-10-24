"""Jeleva independent research-only stress configurations; no card is owner approved here."""
import hashlib
from math import comb
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOLDER = ROOT / "data/grixis/m7/independent_candidates"
REPORT = ROOT / "data/grixis/m7/independent_reviews/Jeleva__Nephalia_s_Scourge_ChatGPT_Adversarial_20261024.md"
STEM = "Jeleva__Nephalia_s_Scourge_M7_"
FILES = {
    "baseline": "Baseline_Research_20261024.txt",
    "savage": "SavageBeating_Over_MindsDesire_Research_20261024.txt",
    "blast": "DelayedBlastFireball_Over_ToxicDeluge_Research_20261024.txt",
    "two": "Savage_Delayed_TwoSwap_Research_20261024.txt",
    "haste": "HasteMagic_Over_TorchCourier_Research_20261024.txt",
    "samut": "Samut_Over_TorchCourier_Research_20261024.txt",
    "tyrant": "SamutTyrant_Over_HexingSquelcher_Research_20261024.txt",
    "snap": "Snap_Over_Probe_Research_20261024.txt",
    "forbidden": "ForbiddenOrchard_Over_Exotic_Research_20261024.txt",
    "snap_forbidden": "Snap_Forbidden_TwoSwap_Research_20261024.txt",
    "flare": "Flare_Over_MnemonicBetrayal_Research_20261024.txt",
    "madcap": "Madcap_Over_HexingSquelcher_Research_20261024.txt",
    "riptide": "RiptideLab_Over_CityOfTraitors_Research_20261024.txt",
    "fire_covenant": "FireCovenant_Over_ToxicDeluge_Research_20261024.txt",
    "flame_anor": "FlameAnor_Over_MindbreakTrap_Research_20261024.txt",
    "spellseeker": "Spellseeker_Over_MnemonicBetrayal_Research_20261024.txt",
    "dramatic": "DramaticReversal_Over_CabalRitual_Research_20261024.txt",
    "gemstone": "GemstoneMine_Over_MorphicPool_Research_20261024.txt",
    "frantic": "FranticSearch_Over_GitaxianProbe_Research_20261024.txt",
    "five_stress": "FiveStress_NotApproved_Research_20261024.txt",
    "cavern_city": "Cavern_Over_CityOfTraitors_Research_20261024.txt",
    "cavern_morphic": "Cavern_Over_MorphicPool_Research_20261024.txt",
    "plaza_city": "PlazaOfHeroes_Over_CityOfTraitors_Research_20261024.txt",
}
EXPECTED = {
    "baseline": {},
    "savage": {"Savage Beating": "Mind's Desire"},
    "blast": {"Delayed Blast Fireball": "Toxic Deluge"},
    "two": {"Savage Beating": "Mind's Desire", "Delayed Blast Fireball": "Toxic Deluge"},
    "haste": {"Haste Magic": "Torch Courier"},
    "samut": {"Samut, Hazoret's Champion": "Torch Courier"},
    "tyrant": {"Samut, Tyrant of Naktamun": "Hexing Squelcher"},
    "snap": {"Snap": "Gitaxian Probe"},
    "forbidden": {"Forbidden Orchard": "Exotic Orchard"},
    "snap_forbidden": {"Snap": "Gitaxian Probe", "Forbidden Orchard": "Exotic Orchard"},
    "flare": {"Flare of Duplication": "Mnemonic Betrayal"},
    "madcap": {"The Madcap Jester": "Hexing Squelcher"},
    "riptide": {"Riptide Laboratory": "City of Traitors"},
    "fire_covenant": {"Fire Covenant": "Toxic Deluge"},
    "flame_anor": {"Flame of Anor": "Mindbreak Trap"},
    "spellseeker": {"Spellseeker": "Mnemonic Betrayal"},
    "dramatic": {"Dramatic Reversal": "Cabal Ritual"},
    "gemstone": {"Gemstone Mine": "Morphic Pool"},
    "frantic": {"Frantic Search": "Gitaxian Probe"},
    "five_stress": {"Fire Covenant": "Toxic Deluge", "Flame of Anor": "Mindbreak Trap",
                    "Spellseeker": "Mnemonic Betrayal", "Dramatic Reversal": "Cabal Ritual",
                    "Gemstone Mine": "Morphic Pool"},
    "cavern_city": {"Cavern of Souls": "City of Traitors"},
    "cavern_morphic": {"Cavern of Souls": "Morphic Pool"},
    "plaza_city": {"Plaza of Heroes": "City of Traitors"},
}
HISTORICAL_RAW_SHA256 = "00e3f52118f5944684ebc49a5398acf8184f7ca878e861221e4c99931191bc2f"
LANDS = {
    "Ancient Tomb", "Arena of Glory", "Arid Mesa", "Badlands", "Blood Crypt", "Bloodstained Mire",
    "City of Brass", "City of Traitors", "Command Tower", "Exotic Orchard", "Flooded Strand",
    "Gemstone Caverns", "Island", "Mana Confluence", "Marsh Flats", "Misty Rainforest",
    "Morphic Pool", "Otawara, Soaring City", "Polluted Delta", "Scalding Tarn", "Steam Vents",
    "Swamp", "Underground Sea", "Verdant Catacombs", "Volcanic Island", "Watery Grave", "Wooded Foothills",
}
TOP_STAGERS = {
    "Mystical Tutor", "Vampiric Tutor", "Imperial Seal", "Personal Tutor", "Scheming Symmetry",
    "Long-Term Plans", "Brainstorm", "Scroll Rack", "Sensei's Divining Top", "Ponder", "Preordain",
}
HASTE_ENABLERS = {"Torch Courier", "Lightning Greaves", "Arena of Glory", "Borne Upon a Wind"}
BASELINE_INSTANT_SORCERY_NAMES = {
    "Ad Nauseam", "An Offer You Can't Refuse", "Borne Upon a Wind", "Brain Freeze",
    "Brainstorm", "Cabal Ritual", "Chain of Vapor", "Dark Ritual",
    "Deflecting Swat", "Demonic Consultation", "Demonic Tutor", "Doomsday",
    "Fierce Guardianship", "Final Fortune", "Flusterstorm", "Force of Negation",
    "Force of Will", "Gamble", "Gitaxian Probe", "Imperial Seal",
    "Into the Flood Maw", "Jeska's Will", "Lim-Dûl's Vault", "Long-Term Plans",
    "Mental Misstep", "Mind's Desire", "Mindbreak Trap", "Mnemonic Betrayal",
    "Mystical Tutor", "Pact of Negation", "Peer into the Abyss", "Personal Tutor",
    "Ponder", "Preordain", "Pyroblast", "Red Elemental Blast",
    "Rite of Flame", "Scheming Symmetry", "Swan Song", "Tainted Pact",
    "Toxic Deluge", "Vampiric Tutor", "Wheel of Fortune", "Windfall",
    "Yawgmoth's Will",
}


def read_cards(key):
    raw = (FOLDER / (STEM + FILES[key])).read_bytes()
    if not raw.endswith(b"\n") or raw.endswith(b"\n\n"):
        raise AssertionError("research files are single-LF normalized; historic source has no LF")
    text = raw.decode("utf-8")
    lines = text.splitlines()
    if not lines or lines[0] != "1x Jeleva, Nephalia's Scourge [Commander]":
        raise AssertionError("wrong commander first line")
    if len(lines) != 100 or any(not re.fullmatch(r"1x [^\r\n]+", l) for l in lines[1:]):
        raise AssertionError("research alternative must have 100 one-per-line 1x cards")
    names = [line[3:] for line in lines[1:]]
    if len(names) != len(set(names)):
        raise AssertionError("singleton violation")
    return names, raw


class JelevaAdversarialStress(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base, cls.raw = read_cards("baseline")
        cls.report = REPORT.read_text(encoding="utf-8")

    def test_source_byte_provenance_and_100_distinct(self):
        # Canonical Oct14 TXT lacks terminal LF, unlike reserialized research-only files.
        self.assertEqual(hashlib.sha256(self.raw[:-1]).hexdigest(), HISTORICAL_RAW_SHA256)
        self.assertEqual(len(self.base), 99)
        self.assertEqual(len(set(self.base)), 99)
        self.assertEqual(len(LANDS.intersection(self.base)), 27)
        self.assertEqual(len(TOP_STAGERS.intersection(self.base)), 11)
        self.assertEqual(len(HASTE_ENABLERS.intersection(self.base)), 4)

    def test_all_research_alternatives_exact_swaps_and_mana_shell(self):
        base = set(self.base)
        for key, changes in EXPECTED.items():
            with self.subTest(candidate=key):
                cards, _ = read_cards(key)
                names = set(cards)
                if key in ("forbidden", "snap_forbidden"):
                    expected_lands = (LANDS - {"Exotic Orchard"}) | {"Forbidden Orchard"}
                elif key == "riptide":
                    expected_lands = (LANDS - {"City of Traitors"}) | {"Riptide Laboratory"}
                elif key in ("gemstone", "five_stress"):
                    expected_lands = (LANDS - {"Morphic Pool"}) | {"Gemstone Mine"}
                elif key in ("cavern_city", "plaza_city"):
                    expected_lands = (LANDS - {"City of Traitors"}) | {"Cavern of Souls" if key == "cavern_city" else "Plaza of Heroes"}
                elif key == "cavern_morphic":
                    expected_lands = (LANDS - {"Morphic Pool"}) | {"Cavern of Souls"}
                else:
                    expected_lands = LANDS
                self.assertEqual(len(names), 99)
                self.assertEqual(names - base, set(changes))
                self.assertEqual(base - names, set(changes.values()))
                self.assertEqual(len(expected_lands.intersection(names)), 27)
                self.assertEqual(expected_lands.intersection(names), expected_lands)
                self.assertEqual(TOP_STAGERS.intersection(names), TOP_STAGERS)
                if key not in ("haste", "samut"):
                    self.assertEqual(HASTE_ENABLERS.intersection(names), HASTE_ENABLERS)
                else:
                    self.assertEqual(len(HASTE_ENABLERS.intersection(names)), 3)

    def test_jeleva_combat_timing_and_exile_conditions_are_explicit(self):
        # Official WotC release notes are cited in the research report; these checks
        # validate that the *review* never upgrades conditional branches to guarantees.
        for text in ("declare-attackers", "additional combat", "after this phase",
                     "after a main phase", "extra combat", "needs Jeleva to survive"):
            if text == "needs Jeleva to survive":
                self.assertIn("needs Jeleva to survive", self.report)
            else:
                self.assertIn(text, self.report)
        self.assertIn("5", self.report)
        self.assertIn("cast from exile", self.report)
        self.assertIn("indestructibility", self.report)
        self.assertIn("Drannith Magistrate", self.report)
        self.assertIn("cannot be cast while Magistrate is present", self.report)
        self.assertIn("3 life", self.report)

    def test_savage_staged_remaining_own_spell_availability_is_conditional(self):
        """Exact card-type-only combinatorics, not simulation/castability/win rates."""
        self.assertEqual(len(BASELINE_INSTANT_SORCERY_NAMES), 45)
        self.assertEqual(BASELINE_INSTANT_SORCERY_NAMES.intersection(self.base), BASELINE_INSTANT_SORCERY_NAMES)
        savage_names, _ = read_cards("savage")
        research_spells = (BASELINE_INSTANT_SORCERY_NAMES - {"Mind's Desire"}) | {"Savage Beating"}
        self.assertEqual(len(research_spells), 45)
        self.assertEqual(len(set(savage_names).intersection(research_spells)), 45)
        for x, expected in ((4, 0.836919), (6, 0.953431), (8, 0.987199)):
            with self.subTest(mana_spent_to_cast_jeleva=x):
                # Top card staged as Savage, among other 98: 44 spells/54 nonspells.
                probability = 1 - comb(54, x - 1) / comb(98, x - 1)
                self.assertAlmostEqual(probability, expected, places=6)
        self.assertIn("not success rates", self.report)
        self.assertIn("additional cost or other condition", self.report)

    def test_snap_commander_tax_and_orchard_color_cost_tradeoffs_disclosed(self):
        self.assertIn("no commander tax", self.report.lower())
        self.assertIn("not an automatically larger tax-boosted pool", self.report.lower())
        self.assertIn("Drannith Magistrate", self.report)
        self.assertIn("no flying", self.report)
        self.assertIn("cannot block", self.report)
        self.assertIn("Pod-composition-dependent", self.report)
        # Oracle-text scenarios only, not a metagame-frequency or win-rate model.
        grixis = {"U", "B", "R"}
        for opponent_land_colors, expected_exotic in (
            ({"U", "B", "R"}, {"U", "B", "R"}),
            ({"U", "B"}, {"U", "B"}),
            ({"W", "G"}, set()),
        ):
            with self.subTest(opposing_lands=opponent_land_colors):
                exotic_grixis = grixis.intersection(opponent_land_colors)
                forbidden_grixis = grixis
                self.assertEqual(exotic_grixis, expected_exotic)
                self.assertEqual(forbidden_grixis, grixis)
        names, _ = read_cards("snap_forbidden")
        self.assertIn("Snap", names)
        self.assertIn("Forbidden Orchard", names)
        self.assertNotIn("Gitaxian Probe", names)
        self.assertNotIn("Exotic Orchard", names)

    def test_no_five_swap_claim_or_owner_approval(self):
        self.assertIn("RESEARCH_ONLY", self.report)
        self.assertIn("no owner-presentable proposal", self.report)
        self.assertIn("no canonical change", self.report)
        self.assertIn("no owner approval", self.report)
        self.assertIn("zero five-swap-ready proposals", self.report)
        self.assertIn("not a validated Magic rules engine", self.report)
        # FiveStress is an explicitly REJECTED negative control, not approval.
        self.assertLess(max(len(changes) for k, changes in EXPECTED.items() if k != "five_stress"), 5)
        self.assertEqual(len(EXPECTED["five_stress"]), 5)
        self.assertIn("negative control", self.report)
        self.assertIn("does not satisfy M7", self.report)

    def test_fresh_october_and_wizard_bounce_hypotheses_carry_explicit_limits(self):
        # This is source-bound review traceability, not a Magic stack simulator.
        for exact in (
            "Flare of Duplication", "Mnemonic Betrayal", "sacrifice Jeleva",
            "stack target", "The Madcap Jester", "four mana before Jeleva",
            "normal costs", "Riptide Laboratory", "City of Traitors",
            "{1}{U}", "colorless", "Mirror Universe Intrusion",
            "November 13, 2026", "Turbulent Wetlands", "eight or more lands",
        ):
            with self.subTest(exact=exact):
                self.assertIn(exact, self.report)
        for key, new_name in (
            ("flare", "Flare of Duplication"),
            ("madcap", "The Madcap Jester"),
            ("riptide", "Riptide Laboratory"),
        ):
            names, _ = read_cards(key)
            self.assertIn(new_name, names)
            self.assertEqual(len(names), 99)
        # No false claim that one new wizard yields five positive deck changes.
        self.assertIn("not a demonstrated improvement", self.report)

    def test_spellseeker_fire_flex_and_artifact_burst_have_falsifiable_limits(self):
        for exact in (
            "Fire Covenant", "Toxic Deluge", "additional cost", "Drannith Magistrate",
            "Flame of Anor", "Mindbreak Trap", "Wizard", "five damage",
            "Spellseeker", "Mnemonic Betrayal", "twice", "<=2",
            "Dramatic Reversal", "Cabal Ritual", "Mana Vault", "Grim Monolith",
            "Frantic Search", "Gitaxian Probe", "Gemstone Mine", "Morphic Pool",
            "1,975 of 2,925", "1,984 of 2,925", "~0.31 percentage points",
        ):
            with self.subTest(exact=exact):
                self.assertIn(exact, self.report)

    def test_exact_land_three_color_bounded_enumeration(self):
        from itertools import combinations, permutations

        land_names = sorted(LANDS)
        color_options = {}
        grouped = {
            "UBR": ["Arid Mesa", "Bloodstained Mire", "City of Brass", "Command Tower",
                    "Exotic Orchard", "Flooded Strand", "Mana Confluence", "Marsh Flats",
                    "Misty Rainforest", "Polluted Delta", "Scalding Tarn",
                    "Verdant Catacombs", "Wooded Foothills", "Gemstone Mine", "Starting Town",
                    "Forbidden Orchard"],
            "UB": ["Morphic Pool", "Underground Sea", "Watery Grave"],
            "UR": ["Steam Vents", "Volcanic Island"],
            "BR": ["Badlands", "Blood Crypt"],
            "U": ["Island", "Otawara, Soaring City"],
            "B": ["Swamp"],
            "R": ["Arena of Glory"],
            "": ["Ancient Tomb", "City of Traitors", "Gemstone Caverns"],
        }
        for colors, names in grouped.items():
            for name in names:
                self.assertNotIn(name, color_options)
                color_options[name] = colors
        self.assertEqual(set(LANDS), set(land_names))
        self.assertTrue(set(LANDS).issubset(color_options))

        def supports_ubr(chosen, options):
            return any(all(want in options[name] for name, want in zip(chosen, ordering))
                       for ordering in permutations("UBR"))

        def count_covered(lands, options=color_options):
            triples = list(combinations(sorted(lands), 3))
            self.assertEqual(len(triples), 2925)
            return sum(supports_ubr(triple, options) for triple in triples)

        self.assertEqual(count_covered(LANDS), 1975)
        for replacement, cut, expected in (
            ("Gemstone Mine", "Morphic Pool", 1984),
            ("Starting Town", "Morphic Pool", 1984),
            ("Forbidden Orchard", "Exotic Orchard", 1975),
        ):
            with self.subTest(replacement=replacement):
                new_lands = (LANDS - {cut}) | {replacement}
                self.assertEqual(count_covered(new_lands), expected)
        wizard_mana = {**color_options, "Cavern of Souls": "UBR", "Plaza of Heroes": "UBR"}
        spell_mana = {**color_options, "Cavern of Souls": "", "Plaza of Heroes": ""}
        for replacement in ("Cavern of Souls", "Plaza of Heroes"):
            with self.subTest(commander_land=replacement):
                alternative = (LANDS - {"City of Traitors"}) | {replacement}
                self.assertEqual(count_covered(alternative, wizard_mana), 2250)
                # Both the displaced City and Cavern/Plaza provide only colorless
                # toward ordinary noncreature spells in this simplified check.
                self.assertEqual(count_covered(alternative, spell_mana), 1975)
        morphic_replacement = (LANDS - {"Morphic Pool"}) | {"Cavern of Souls"}
        self.assertEqual(count_covered(morphic_replacement, wizard_mana), 1984)
        self.assertEqual(count_covered(morphic_replacement, spell_mana), 1732)
        self.assertIn("not** probability of casting the four-mana commander", self.report)

    def test_cavern_wizard_protection_and_generic_burst_loss_disclosed(self):
        for phrase in ("Cavern of Souls", "City of Traitors", "Plaza of Heroes",
                       "Thassa's Oracle", "Harmonic Prodigy", "Wizard", "Drannith Magistrate",
                       "2,250 / 2,925", "1,732 / 2,925", "9.40 percentage-point",
                       "City's additional generic mana", "not** probability"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.report)


if __name__ == "__main__":
    unittest.main()
