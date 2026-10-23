"""Finite source-anchored rules/mana cases for the Be'lakor, the Dark Master M7 candidate.

Seed 0, no randomness. Bounded rules model, NOT a game engine or win-rate measurement;
supports no improvement claim by itself.
"""
from collections import Counter
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
D = "Be_lakor__the_Dark_Master"
SNAP = ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json"
CAND = ROOT / f"data/grixis/m7/candidate_lists/{D}.txt"
BASE = ROOT / "data/grixis/m7/baseline_sources/Be_lakor_the_Dark_Master_approved_source_2026-10-13.txt"
SPELLBOOK = ROOT / f"data/grixis/m7/research_challengers/{D}_CommanderSpellbook_20261023.json"
CMDR = "Be'lakor, the Dark Master"
ADDS = ["Desecration Demon", "Kindred Dominance", "Demonlord Belzenlok", "Reaper from the Abyss", "Herald's Horn"]
CUTS = ["Dream Devourer", "Blasphemous Act", "Rakdos, Patron of Chaos", "Bloodthirster", "Fellwar Stone"]
ROCKS = {"Sol Ring", "Arcane Signet", "Fellwar Stone", "Rakdos Signet", "Talisman of Creativity",
         "Talisman of Dominance", "Talisman of Indulgence"}
CORE = ["Liliana's Contract", "Rite of Replication", "Molten Echoes", "Spark Double", "Herald of Slaanesh",
        "Urza's Incubator", "Heartless Summoning", "Roaming Throne", "Bloodletter of Aclazotz", "Kardur, Doomscourge",
        "Sneak Attack", "Reanimate", "Toxic Deluge", "Warstorm Surge", "Lord of Change", "Panharmonicon"]


def names(path):
    out = Counter()
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            q, raw = line.split("x ", 1)
            out[raw.removesuffix(" [Commander]")] += int(q)
    return out


def lord_damage(power, heartless=False):
    """Lord of Torment: the entering Demon deals damage equal to its (current) power; never negative."""
    return max(0, power - (1 if heartless else 0))


def rite_kicked_lord_triggers(roaming_throne=False):
    """Kicked Rite of Replication on Be'lakor: five token copies enter simultaneously (CR 603.6a).
    The original sees five other Demons; each token sees the other four (not itself). Legend rule
    (704.5j) removes copies afterward but triggers are already on the stack. Finite."""
    triggers = 5 + 5 * 4
    return triggers * (2 if roaming_throne else 1)


class BelakorM7Mechanics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cards = {c["name"]: c for c in json.loads(SNAP.read_text())["cards"]}
        cls.cand, cls.base = names(CAND), names(BASE)

    def test_commander_oracle(self):
        c = self.cards[CMDR]
        self.assertIn("Whenever another Demon you control enters, it deals damage equal to its power to any target",
                      c["oracle_text"])
        self.assertIn("you draw X cards and you lose X life, where X is the number of Demons you control", c["oracle_text"])
        self.assertEqual((c["power"], c["toughness"], c["cmc"]), ("6", "5", 6.0))
        self.assertIn("Demon", c["type_line"])

    def test_lord_damage_per_swap(self):
        self.assertEqual(lord_damage(int(self.cards["Dream Devourer"]["power"])), 0)
        for n in ["Desecration Demon", "Demonlord Belzenlok", "Reaper from the Abyss"]:
            self.assertIn("Demon", self.cards[n]["type_line"], n)
            self.assertEqual(lord_damage(int(self.cards[n]["power"])), 6, n)
        self.assertEqual(self.cards["Desecration Demon"]["cmc"], 4.0)
        self.assertEqual(lord_damage(6, heartless=True), 5)
        self.assertEqual(lord_damage(0, heartless=True), 0)

    def test_demon_power_sum_and_count(self):
        def stats(d):
            demons = [n for n in d if "Demon" in self.cards[n]["type_line"]]
            return len(demons), sum(int(self.cards[n]["power"]) for n in demons)
        self.assertEqual(stats(self.base), (25, 129))
        self.assertEqual(stats(self.cand), (25, 135))

    def test_kindred_dominance_one_sided_vs_blasphemous_act(self):
        self.assertIn("Destroy all creatures that aren't of the chosen type", self.cards["Kindred Dominance"]["oracle_text"])
        self.assertIn("deals 13 damage to each creature", self.cards["Blasphemous Act"]["oracle_text"])
        ours = [n for n in self.cand if "Creature" in self.cards[n]["type_line"]]
        survivors = [n for n in ours if "Demon" in self.cards[n]["type_line"] or n in {"Roaming Throne", "Spark Double"}]
        self.assertEqual(sorted(set(ours) - set(survivors)), ["Ancient Cellarspawn"])

    def test_reaper_morbid_and_herald_horn_text(self):
        self.assertIn("Morbid — At the beginning of each end step, if a creature died this turn, destroy target non-Demon creature",
                      self.cards["Reaper from the Abyss"]["oracle_text"])
        t = self.cards["Herald's Horn"]["oracle_text"]
        self.assertIn("Creature spells you cast of the chosen type cost {1} less", t)
        self.assertIn("If it's a creature card of the chosen type, you may reveal it and put it into your hand", t)

    def test_cut_rationale_text(self):
        self.assertIn("target opponent may sacrifice two nonland, nontoken permanents of their choice",
                      self.cards["Rakdos, Patron of Chaos"]["oracle_text"])
        self.assertIn("additional combat phase", self.cards["Bloodthirster"]["oracle_text"])
        self.assertIn("a land an opponent controls could produce", self.cards["Fellwar Stone"]["oracle_text"])
        self.assertEqual(self.cards["Dream Devourer"]["power"], "0")

    def test_rite_combo_is_finite(self):
        self.assertIn("If this spell was kicked, create five of those tokens instead",
                      self.cards["Rite of Replication"]["oracle_text"])
        self.assertEqual(rite_kicked_lord_triggers(), 25)
        self.assertEqual(rite_kicked_lord_triggers() * 6, 150)
        self.assertEqual(rite_kicked_lord_triggers(roaming_throne=True), 50)

    def test_spellbook_single_finite_combo_unchanged(self):
        sb = json.loads(SPELLBOOK.read_text())
        ids = lambda k: {x["id"] for x in sb[k]["included"]}
        self.assertEqual(ids("baseline"), {"1744-4071"})
        self.assertEqual(ids("candidate"), {"1744-4071"})
        self.assertEqual(sorted(sb["candidate"]["included"][0]["uses"]), [CMDR, "Rite of Replication"])

    def test_exact_swaps_and_core_preserved(self):
        self.assertEqual(sorted((self.cand - self.base).elements()), sorted(ADDS))
        self.assertEqual(sorted((self.base - self.cand).elements()), sorted(CUTS))
        for n in CORE:
            self.assertEqual(self.cand[n], 1, n)

    def test_quantity_counted_lands_rocks(self):
        land = lambda d: sum(q for n, q in d.items() if "Land" in self.cards[n]["type_line"].split("—")[0])
        self.assertEqual((land(self.base), land(self.cand)), (36, 36))
        self.assertEqual(sum(q for n, q in self.base.items() if n in ROCKS), 7)
        self.assertEqual(sum(q for n, q in self.cand.items() if n in ROCKS), 6)
        self.assertEqual((self.cand["Island"], self.cand["Mountain"], self.cand["Swamp"]), (3, 2, 4))
        self.assertEqual(sum(self.cand.values()), 100)
        self.assertEqual(sum(self.base.values()), 100)

    def test_legality_identity_singleton_game_changers(self):
        for n, q in self.cand.items():
            c = self.cards[n]
            self.assertEqual(c["commander_legality"], "legal", n)
            self.assertTrue(set(c["color_identity"]) <= {"U", "B", "R"}, n)
            if n not in {"Island", "Swamp", "Mountain"}:
                self.assertEqual(q, 1, n)
        gc = lambda d: sorted(n for n in d if self.cards[n]["game_changer"])
        self.assertEqual(gc(self.cand), gc(self.base))
        self.assertEqual(gc(self.cand), ["Ancient Tomb", "Cyclonic Rift", "Demonic Tutor", "Fierce Guardianship",
                                         "Vampiric Tutor"])


if __name__ == "__main__":
    unittest.main()
