"""Finite source-anchored rules/mana cases for the Cult of Skaro M7 candidate.

Seed 0, no randomness. Exact fractions over Cult of Skaro's four equally likely random modes and an enumerated
connect-rate grid. This is a bounded rules/trigger-count model, NOT a game engine, simulation or win-rate
measurement; it supports no improvement claim by itself.

It includes the bounded finite version of the M6 Pass C requested tests (Kindred Discovery vs Research Thief /
Thopter Spy Network / Canoptek Spyder; Karlach vs Biotransference / Canoptek Spyder; Hexplate Wallbreaker): actual
Dalek subtype mix of the 100, attack-declaration vs combat-damage draw triggers over fixed board states, attack-trigger
counts per turn, red-source access and the token/draw opportunity cost of each cut. It does not model opponents'
removal, blocks, wipes or matchups; those remain an explicit limitation.
"""
from collections import Counter
from fractions import Fraction as F
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
D = "Cult_of_Skaro"
SNAP = ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json"
CAND = ROOT / f"data/grixis/m7/candidate_lists/{D}.txt"
BASE = ROOT / f"data/grixis/m7/baseline_sources/{D}_approved_source_2026-10-14.txt"
SPELLBOOK = ROOT / f"data/grixis/m7/research_challengers/{D}_CommanderSpellbook_20261023.json"
CULT = "Cult of Skaro"
ADDS = ["Karlach, Fury of Avernus", "Kindred Discovery", "Hammer of Purphoros", "Shaun, Father of Synths",
        "Quantum Misalignment", "Skorpekh Lord"]
CUTS = ["Cybermen Squadron", "Canoptek Spyder", "Adaptive Omnitool", "The Master, Multiplied",
        "Anrakyr the Traveller", "Etherium Sculptor"]
CORE = ["Strionic Resonator", "Roaming Throne", "Scientist Supreme of A.I.M.", "Helm of the Host", "Spark Double",
        "Sakashima of a Thousand Faces", "Phyrexian Metamorph", "Auton Soldier", "Irenicus's Vile Duplication",
        "The Dalek Emperor", "Davros, Dalek Creator", "Genesis of the Daleks", "Dalek Squadron", "Dalek Drone",
        "Research Thief", "Thopter Spy Network", "Biotransference", "Sword of Feast and Famine",
        "Aggravated Assault", "Full Throttle", "Lightning Greaves", "Swiftfoot Boots", "Padeem, Consul of Innovation"]
GAME_CHANGERS = ["Cyclonic Rift", "Fierce Guardianship", "Mana Vault"]
# Lands whose own Oracle (or fetchable typed duals) can produce red; conditional ones flagged.
RED_LANDS = {"Badlands": 1, "Blood Crypt": 1, "Bloodstained Mire": 1, "Command Tower": 1, "Exotic Orchard": 1,
             "Mountain": 3, "Polluted Delta": 1, "Scalding Tarn": 1, "Spire of Industry": 1, "Steam Vents": 1,
             "Arena of Glory": 1, "Volcanic Island": 1, "Xander's Lounge": 1, "Plaza of Heroes": 1,
             "Luxury Suite": 1, "Training Center": 1, "Great Furnace": 1}
CONDITIONAL_RED = {"Exotic Orchard", "Spire of Industry", "Plaza of Heroes"}
MODES = ("Thay", "Caan", "Sec", "Jast")  # one chosen at random on the stack (CR 603.3c); each 1/4


def names(path):
    out = Counter()
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            q, raw = line.split(" ", 1)
            out[raw.removesuffix(" [Commander]")] += int(q.rstrip("x"))
    return out


def cult_trigger_expectation():
    """Expected value of one Cult attack trigger (uniform random mode): cards drawn, Dalek tokens made, life lost
    per opponent. Copies made by Strionic Resonator / Scientist Supreme keep the already chosen mode (707.10);
    Roaming Throne (Dalek) makes a separate trigger with its own roll."""
    q = F(1, 4)
    return {"draw": 2 * q, "dalek_tokens": q, "drain_each_opp": 4 * q}


def cult_attack_triggers(cult_bodies_first, karlach=False, shaun=False, throne_dalek=False, synth_haste=False):
    """Number of Cult attack triggers in one turn. cult_bodies_first = Cult plus legal untapped nonlegendary Cult
    copies able to attack in combat 1. Karlach: 'whenever you attack, if it's the first combat phase, untap all
    attacking creatures ... additional combat phase' -> the same bodies attack again (declared attack -> trigger).
    Shaun: 'whenever you attack' -> a tapped-and-attacking non-legendary Synth copy of attacking legendary Cult;
    it enters attacking so it does NOT trigger 'attacks' in that combat (508.3a/508.4), but if Shaun's trigger
    resolves before Karlach's, Karlach untaps it. The Synth came under our control this turn, so it can be declared
    as an attacker in the extra combat only with haste (302.6): Hammer of Purphoros, or The Dalek Emperor (other
    Daleks; the Synth is a Dalek copy). synth_haste models that condition.
    Roaming Throne naming Dalek doubles each trigger of another Dalek."""
    first = cult_bodies_first
    second = 0
    if karlach:
        second = cult_bodies_first + (1 if (shaun and synth_haste) else 0)
    total = first + second
    return total * (2 if throne_dalek else 1)


def kindred_draws(dalek_entries, dalek_attack_declarations):
    """Kindred Discovery naming Dalek: mandatory draw per Dalek entering or attacking (pre-damage)."""
    return dalek_entries + dalek_attack_declarations


def research_thief_draws(artifact_attackers, hit_rate):
    """Research Thief: one draw per artifact creature that deals combat damage to a player (post-damage)."""
    return artifact_attackers * hit_rate


def tsn_draws(combats_with_any_hit_probability):
    """Thopter Spy Network: one draw per combat-damage step in which one or more artifact creatures connect."""
    return sum(combats_with_any_hit_probability)


def spyder_draws(nontoken_artifact_creature_entries):
    """Canoptek Spyder: one draw per other nontoken artifact creature or Vehicle entering."""
    return nontoken_artifact_creature_entries


class CultOfSkaroOracle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.o = {c["name"]: c for c in json.loads(SNAP.read_text())["cards"]}
        cls.cand, cls.base = names(CAND), names(BASE)

    def test_commander_oracle_random_mode_and_no_haste(self):
        t = self.o[CULT]["oracle_text"]
        self.assertIn("Whenever Cult of Skaro attacks, choose one at random", t)
        for m in MODES:
            self.assertIn(m + " \u2014", t)
        self.assertNotIn("Haste", t)
        self.assertEqual(self.o[CULT]["mana_cost"], "{1}{U}{B}{R}")
        self.assertIn("Dalek", self.o[CULT]["type_line"])
        e = cult_trigger_expectation()
        self.assertEqual(e, {"draw": F(1, 2), "dalek_tokens": F(1, 4), "drain_each_opp": F(1)})

    def test_add_oracle_anchors(self):
        o = self.o
        self.assertIn("Whenever you attack, if it's the first combat phase of the turn, untap all attacking creatures",
                      o["Karlach, Fury of Avernus"]["oracle_text"])
        self.assertIn("Whenever a creature you control of the chosen type enters or attacks, draw a card",
                      o["Kindred Discovery"]["oracle_text"])
        self.assertIn("Creatures you control have haste", o["Hammer of Purphoros"]["oracle_text"])
        self.assertIn("Artifact", o["Hammer of Purphoros"]["type_line"])
        self.assertIn("tapped and attacking token that's a copy of target attacking legendary creature",
                      o["Shaun, Father of Synths"]["oracle_text"])
        self.assertIn("When Shaun leaves the battlefield, exile all Synth tokens", o["Shaun, Father of Synths"]["oracle_text"])
        self.assertIn("except it isn't legendary", o["Quantum Misalignment"]["oracle_text"])
        self.assertIn("Rebound", o["Quantum Misalignment"]["oracle_text"])
        self.assertIn("Other artifact creatures you control get +1/+0 and have menace", o["Skorpekh Lord"]["oracle_text"])
        self.assertIn("Artifact Creature", o["Skorpekh Lord"]["type_line"])

    def test_attack_trigger_counts_per_turn(self):
        # Cult alone, no extra combat: 1 trigger. Karlach: 2. Karlach+Shaun (Shaun resolves first): 3 only if the new
        # Synth has haste (Hammer of Purphoros / The Dalek Emperor); otherwise it is summoning sick (302.6): still 2.
        self.assertEqual(cult_attack_triggers(1), 1)
        self.assertEqual(cult_attack_triggers(1, karlach=True), 2)
        self.assertEqual(cult_attack_triggers(1, karlach=True, shaun=True), 2)
        self.assertEqual(cult_attack_triggers(1, karlach=True, shaun=True, synth_haste=True), 3)
        self.assertIn("Creatures you control have haste", self.o["Hammer of Purphoros"]["oracle_text"])
        self.assertIn("haste", self.o["The Dalek Emperor"]["oracle_text"])
        self.assertEqual(cult_attack_triggers(1, shaun=True), 1)  # Synth enters attacking: no trigger this combat
        # Next turn the persistent Synth copy attacks too (it is not exiled at end of combat, only if Shaun leaves).
        self.assertEqual(cult_attack_triggers(2, karlach=True, shaun=True, synth_haste=True), 5)
        self.assertEqual(cult_attack_triggers(2, karlach=True, shaun=True), 4)
        self.assertEqual(cult_attack_triggers(1, karlach=True, throne_dalek=True), 4)
        exp = cult_trigger_expectation()
        self.assertEqual(3 * exp["draw"], F(3, 2))
        self.assertEqual(3 * exp["drain_each_opp"], 3)
        # Baseline extra-combat sources were sorcery/once-per-turn spells only; Karlach adds a permanent one.
        for c in ("Full Throttle", "Aggravated Assault", "Great Train Heist"):
            self.assertIn(c, self.cand)

    def test_myriad_and_entering_attacking_tokens_do_not_trigger_cult(self):
        # Cybermen Squadron (cut) / Dalek Squadron / Auton Soldier myriad tokens enter tapped and attacking.
        self.assertIn("token copy that's tapped and attacking", self.o["Cybermen Squadron"]["oracle_text"])
        self.assertIn("Exile the tokens at end of combat", self.o["Cybermen Squadron"]["oracle_text"])
        self.assertIn("legend rule", self.o["The Master, Multiplied"]["oracle_text"])
        # Helm of the Host token gains haste and is declared as an attacker -> it triggers.
        self.assertIn("That token gains haste", self.o["Helm of the Host"]["oracle_text"])
        # Hammer gives haste to Cult (no native haste) and to every clone the turn it lands.
        clones = ["Spark Double", "Sakashima of a Thousand Faces", "Phyrexian Metamorph", "Auton Soldier",
                  "Irenicus's Vile Duplication", "Quantum Misalignment", "Helm of the Host"]
        self.assertTrue(all(self.cand[c] == 1 for c in clones))


class PassCBoundedMeasuredTests(unittest.TestCase):
    """Bounded finite version of Pass C test 1/2/3/4: subtype mix + enumerated board states."""

    @classmethod
    def setUpClass(cls):
        cls.o = {c["name"]: c for c in json.loads(SNAP.read_text())["cards"]}
        cls.cand, cls.base = names(CAND), names(BASE)

    def mix(self, deck):
        dalek, other_ac = [], []
        for n, q in deck.items():
            tl = self.o[n]["type_line"]
            if "Creature" in tl and "Dalek" in tl:
                dalek.append(n)
            elif "Artifact Creature" in tl:
                other_ac.append(n)
        return sorted(dalek), sorted(other_ac)

    def test_actual_subtype_mix_of_the_100(self):
        dalek, other = self.mix(self.base)
        self.assertEqual(dalek, ["Cult of Skaro", "Dalek Drone", "Dalek Squadron", "The Dalek Emperor"])
        self.assertEqual(len(other), 18)  # Davros is an Alien Scientist, not a Dalek
        dalek_c, other_c = self.mix(self.cand)
        self.assertEqual(dalek_c, dalek)
        self.assertEqual(len(other_c), 15)  # -Squadron -Spyder -Anrakyr -Sculptor +Skorpekh Lord
        # Native Dalek-token makers (all "3/3 black Dalek artifact creature token with menace").
        makers = [n for n in self.cand if "Dalek artifact creature token" in self.o[n]["oracle_text"]]
        self.assertEqual(sorted(makers), ["Cult of Skaro", "Davros, Dalek Creator", "Doomsday Confluence",
                                          "Genesis of the Daleks", "The Dalek Emperor"])
        # Copy effects that can make additional Cult (Dalek) bodies in the candidate.
        copiers = ["Spark Double", "Sakashima of a Thousand Faces", "Phyrexian Metamorph", "Auton Soldier",
                   "Irenicus's Vile Duplication", "Helm of the Host", "Quantum Misalignment", "Shaun, Father of Synths"]
        self.assertTrue(all(self.cand[c] for c in copiers))
        self.assertIn("choose a creature type", self.o["Roaming Throne"]["oracle_text"])

    BOARDS = {
        # name: (dalek_entries, dalek_attackers, artifact_attackers, nontoken_artifact_creature_entries)
        "cult_alone_attacks": (0, 1, 1, 0),
        "genesis_chapter_III_then_cult_and_3_daleks_attack": (3, 4, 4, 0),
        "mixed_board_cult_2_daleks_2_necrons_1_thopter": (0, 3, 6, 0),
        "non_dalek_rebuild_after_wipe_2_thopters_1_cyberman": (0, 0, 3, 1),
        "dalek_drone_cast_then_cult_and_drone_attack": (1, 2, 2, 1),
    }
    GRID = (F(0), F(1, 4), F(1, 2), F(3, 4), F(1))

    def test_kindred_vs_thief_vs_tsn_vs_spyder_enumerated(self):
        rows = {}
        for b, (de, da, aa, nt) in self.BOARDS.items():
            sec = F(1, 4) if da else F(0)  # Cult's Sec mode makes a Dalek token on attack (Kindred draws on entry)
            k = kindred_draws(de, da) + sec
            thief = [research_thief_draws(aa, h) for h in self.GRID]
            tsn = [tsn_draws([1 - (1 - h) ** aa]) if aa else F(0) for h in self.GRID]
            rows[b] = (k, thief, tsn, spyder_draws(nt))
        k, thief, tsn, spy = rows["cult_alone_attacks"]
        self.assertEqual(k, F(5, 4))
        self.assertEqual(thief, [F(0), F(1, 4), F(1, 2), F(3, 4), F(1)])
        k, thief, tsn, spy = rows["genesis_chapter_III_then_cult_and_3_daleks_attack"]
        self.assertEqual(k, F(29, 4))
        self.assertEqual(thief[-1], 4)
        self.assertEqual(tsn[2], F(15, 16))
        k, thief, tsn, spy = rows["mixed_board_cult_2_daleks_2_necrons_1_thopter"]
        self.assertEqual(k, F(13, 4))
        self.assertEqual(thief[2], 3)
        self.assertGreater(thief[-1], k)  # Thief wins when a non-Dalek-heavy board connects fully
        k, thief, tsn, spy = rows["non_dalek_rebuild_after_wipe_2_thopters_1_cyberman"]
        self.assertEqual(k, 0)
        self.assertGreater(thief[2], k)
        self.assertEqual(spy, 1)
        k, thief, tsn, spy = rows["dalek_drone_cast_then_cult_and_drone_attack"]
        self.assertEqual(k, F(13, 4))
        self.assertEqual(spy, 1)
        # Over the five fixed boards Kindred's pre-damage draws beat Thief at every hit rate <= 1/2 and
        # beat Spyder on every board except the post-wipe non-Dalek rebuild.
        for b, (k, thief, tsn, spy) in rows.items():
            if b != "non_dalek_rebuild_after_wipe_2_thopters_1_cyberman":
                self.assertGreaterEqual(k, thief[2], b)
                self.assertGreater(k, spy, b)

    def test_karlach_vs_cut_opportunity_costs(self):
        # Karlach adds +1 full Cult trigger per turn (E = 1/2 card, 1/4 Dalek, 1 life per opponent).
        e = cult_trigger_expectation()
        gain = {k: v * (cult_attack_triggers(1, karlach=True) - cult_attack_triggers(1)) for k, v in e.items()}
        self.assertEqual(gain, {"draw": F(1, 2), "dalek_tokens": F(1, 4), "drain_each_opp": F(1)})
        # Biotransference (kept): one 2/2 Necron per artifact spell cast; Pass C alternative would lose these.
        self.assertIn("Whenever you cast an artifact spell, you lose 1 life and create a 2/2",
                      self.o["Biotransference"]["oracle_text"])
        # Cybermen Squadron (cut): in a 4-player pod, each nonlegendary artifact attacker gets 2 temporary copies
        # that enter attacking (extra damage only, no Cult trigger). With N attackers: 2N temporary bodies.
        self.assertEqual([2 * n for n in (1, 3, 5)], [2, 6, 10])
        # Red access for Karlach {4}{R}, Hammer {1}{R}{R}, Shaun {3}{U}{R}.
        red = sum(self.cand[n] for n in RED_LANDS)
        self.assertEqual(red, 19)
        self.assertEqual(red - sum(self.cand[n] for n in CONDITIONAL_RED), 16)
        for n in RED_LANDS:
            self.assertGreaterEqual(self.cand[n], 1, n)

    def test_hexplate_wallbreaker_tempo_vs_karlach(self):
        hx, ka = self.o["Hexplate Wallbreaker"], self.o["Karlach, Fury of Avernus"]
        self.assertIn("Whenever equipped creature attacks, if it's the first combat phase", hx["oracle_text"])
        self.assertIn("Equip {3}{R}", hx["oracle_text"])
        # Hexplate's germ-like Rebel is summoning sick on the cast turn; moving it to Cult costs 3R more.
        self.assertEqual((hx["cmc"], hx["cmc"] + 4), (5.0, 9.0))
        # Karlach works on the turn it lands if anything attacks (no equip, no attack by Karlach needed).
        self.assertEqual(ka["cmc"], 5.0)
        self.assertIn("Whenever you attack", ka["oracle_text"])


class CandidateDeckChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.o = {c["name"]: c for c in json.loads(SNAP.read_text())["cards"]}
        cls.cand, cls.base = names(CAND), names(BASE)

    def test_exact_swaps_core_preserved_and_quantities(self):
        self.assertEqual(sorted((self.cand - self.base).elements()), sorted(ADDS))
        self.assertEqual(sorted((self.base - self.cand).elements()), sorted(CUTS))
        for c in CORE:
            self.assertEqual(self.cand[c], 1, c)
        self.assertEqual(sum(self.cand.values()), 100)
        lands = sum(q for n, q in self.cand.items() if "Land" in self.o[n]["type_line"])
        self.assertEqual(lands, 34)
        self.assertEqual(lands, sum(q for n, q in self.base.items() if "Land" in self.o[n]["type_line"]))
        for basic in ("Island", "Mountain", "Swamp"):
            self.assertEqual(self.cand[basic], 3)

    def test_legality_identity_singleton_and_game_changers(self):
        for n, q in self.cand.items():
            c = self.o[n]
            self.assertEqual(c["commander_legality"], "legal", n)
            self.assertTrue(set(c["color_identity"]) <= {"U", "B", "R"}, n)
            if "Basic Land" not in c["type_line"]:
                self.assertEqual(q, 1, n)
        self.assertEqual(sorted(n for n in self.cand if self.o[n]["game_changer"]), GAME_CHANGERS)
        self.assertFalse(any(self.o[a]["game_changer"] for a in ADDS))

    def test_spellbook_combos_unchanged(self):
        sb = json.loads(SPELLBOOK.read_text())
        ids = lambda k: sorted(x["id"] for x in sb[k]["included"])
        self.assertEqual(ids("baseline"), ["900-3750"])
        self.assertEqual(ids("candidate"), ["900-3750"])
        self.assertEqual(sorted(sb["baseline"]["included"][0]["uses"]),
                         ["Aggravated Assault", "Sword of Feast and Famine"])


if __name__ == "__main__":
    unittest.main()
