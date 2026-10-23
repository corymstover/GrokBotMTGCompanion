"""Finite source-anchored rules/mana cases for the Davros, Dalek Creator M7 candidate.

Seed 0, no randomness. Davros's end-step trigger is modelled exactly as printed (current Oracle in the M7 snapshot):
"At the beginning of your end step, create a 3/3 black Dalek artifact creature token with menace if an opponent lost
3 or more life this turn. Then each opponent who lost 3 or more life this turn faces a villainous choice -- You draw a
card, or that player discards a card." The condition is checked on resolution (it is not an intervening-if, CR 603.4),
so other end-step triggers ordered first (Wound Reflection, Missy, Perforating Artist) count.

This is a bounded rules/qualification-count model over fixed, enumerated board states, NOT a game engine, simulation
or win-rate measurement; it supports no improvement claim by itself. It includes the bounded finite version of the
three M6 Pass C requested tests (Unlicensed Disintegration variants; Ingenious Artillerist variants; Fiery Confluence
vs the current enablers). It does not model opponents' removal choices beyond the listed response cases, blocks, hand
contents, wipes or matchups; those remain explicit limitations.
"""
from collections import Counter
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
D = "Davros__Dalek_Creator"
SNAP = ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json"
CAND = ROOT / f"data/grixis/m7/candidate_lists/{D}.txt"
BASE = ROOT / f"data/grixis/m7/baseline_sources/{D}_approved_source_2026-10-14.txt"
SPELLBOOK = ROOT / f"data/grixis/m7/research_challengers/{D}_CommanderSpellbook_20261023.json"
DAVROS = "Davros, Dalek Creator"
ADDS = ["Bloodletter of Aclazotz", "Unlicensed Disintegration", "Tergrid, God of Fright",
        "Purphoros, God of the Forge", "Fiery Confluence", "Tectonic Giant"]
CUTS = ["Death in Heaven", "Weeping Angel", "The Cyber-Controller", "Blasphemous Act", "Vandalblast", "Swan Song"]
CORE = ["Boltwave", "Maestros Charm", "Loyal Subordinate", "Court of Ambition", "Perforating Artist",
        "Torment of Hailfire", "Wound Reflection", "Sygg, River Cutthroat", "Tinybones, Trinket Thief",
        "Geth's Grimoire", "Waste Not", "Entropic Battlecruiser", "The Valeyard", "Missy", "Sycorax Commander",
        "Ensnared by the Mara", "This Is How It Ends", "Roaming Throne", "Strionic Resonator",
        "Scientist Supreme of A.I.M.", "Cyberman Patrol", "Labyrinth Raptor", "Dalek Squadron",
        "Cybermen Squadron", "Auton Soldier", "Tezzeret, Master of the Bridge", "Delete"]
GAME_CHANGERS_BASE = ["Ancient Tomb", "Cyclonic Rift", "Demonic Tutor", "Fierce Guardianship", "Jeska's Will"]
GAME_CHANGERS_CAND = sorted(GAME_CHANGERS_BASE + ["Tergrid, God of Fright"])
OPPS = ("A", "B", "C")  # a four-player pod: three opponents


def names(path):
    out = Counter()
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            q, raw = line.split(" ", 1)
            out[raw.removesuffix(" [Commander]")] += int(q.rstrip("x"))
    return out


def oracle():
    return {c["name"].split(" // ")[0]: c for c in json.loads(SNAP.read_text())["cards"]}


def lose(lost, opp, amount, our_turn=True, bloodletter=False):
    """Apply life loss; Bloodletter of Aclazotz doubles opponents' life loss during our turn (replacement)."""
    if amount <= 0:
        return
    lost[opp] = lost.get(opp, 0) + amount * (2 if (bloodletter and our_turn) else 1)


def davros_end_step(lost, triggers=1, valeyard=False, wound_first=False, bloodletter=False,
                    on_token=None):
    """Resolve Davros's end-step trigger `triggers` times (Roaming Throne naming Alien/Scientist, Strionic Resonator
    or Scientist Supreme add resolutions). Wound Reflection, if ordered first, makes each opponent lose life equal
    to the life lost this turn. on_token(lost) applies an entering-token damage payoff (Purphoros / Artillerist).
    Returns (tokens, villainous_choices_faced)."""
    lost = dict(lost)
    if wound_first:
        for o in OPPS:
            lose(lost, o, lost.get(o, 0), bloodletter=bloodletter)
    tokens = choices = 0
    for _ in range(triggers):
        made = any(lost.get(o, 0) >= 3 for o in OPPS)
        tokens += made
        q = [o for o in OPPS if lost.get(o, 0) >= 3]
        choices += len(q) * (2 if valeyard else 1)
        # The token's ETB payoff triggers during resolution but goes on the stack only after Davros's trigger
        # finishes, so it resolves after this resolution's villainous choices and before the next copy.
        if made and on_token:
            on_token(lost)
    return tokens, choices, lost


class DavrosOracle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.o = oracle()
        cls.cand, cls.base = names(CAND), names(BASE)

    def test_commander_oracle_threshold_and_villainous_choice(self):
        c = self.o[DAVROS]
        t = c["oracle_text"]
        self.assertIn("At the beginning of your end step, create a 3/3 black Dalek artifact creature token with menace "
                      "if an opponent lost 3 or more life this turn", t)
        self.assertIn("each opponent who lost 3 or more life this turn faces a villainous choice", t)
        self.assertIn("You draw a card, or that player discards a card", t)
        self.assertEqual(c["mana_cost"], "{1}{U}{B}{R}")
        self.assertIn("Alien Scientist", c["type_line"])
        self.assertNotIn("Dalek", c["type_line"])  # Davros is not a Dalek (Pass C rules note)
        self.assertIn("Menace", t)

    def test_add_oracle_anchors(self):
        o = self.o
        self.assertIn("If an opponent would lose life during your turn, they lose twice that much life instead",
                      o["Bloodletter of Aclazotz"]["oracle_text"])
        self.assertIn("If you control an artifact, Unlicensed Disintegration deals 3 damage to that creature's controller",
                      o["Unlicensed Disintegration"]["oracle_text"])
        self.assertIn("Whenever an opponent sacrifices a nontoken permanent or discards a permanent card",
                      o["Tergrid, God of Fright"]["oracle_text"])
        self.assertIn("Whenever another creature you control enters, Purphoros deals 2 damage to each opponent",
                      o["Purphoros, God of the Forge"]["oracle_text"])
        self.assertIn("Indestructible", o["Purphoros, God of the Forge"]["oracle_text"])
        self.assertIn("Fiery Confluence deals 2 damage to each opponent", o["Fiery Confluence"]["oracle_text"])
        self.assertIn("Destroy target artifact", o["Fiery Confluence"]["oracle_text"])
        self.assertIn("This creature deals 3 damage to each opponent", o["Tectonic Giant"]["oracle_text"])
        self.assertIn("Whenever this creature attacks", o["Tectonic Giant"]["oracle_text"])

    def test_davros_resolution_counts(self):
        # Nobody qualified: no token, no choice. One opponent at 3: one token, one choice.
        self.assertEqual(davros_end_step({})[:2], (0, 0))
        self.assertEqual(davros_end_step({"A": 3})[:2], (1, 1))
        # Boltwave (3 to each opponent) qualifies the whole table: 1 token, 3 choices; Valeyard doubles the
        # choices, not the token (Pass C note); Roaming Throne naming Alien/Scientist doubles both.
        bw = {o: 3 for o in OPPS}
        self.assertEqual(davros_end_step(bw)[:2], (1, 3))
        self.assertEqual(davros_end_step(bw, valeyard=True)[:2], (1, 6))
        self.assertEqual(davros_end_step(bw, triggers=2)[:2], (2, 6))
        self.assertEqual(davros_end_step(bw, triggers=3, valeyard=True)[:2], (3, 18))
        # Wound Reflection ordered first turns an earlier 2-point loss into 4 (Pass C note).
        self.assertEqual(davros_end_step({"A": 2}, wound_first=True)[:2], (1, 1))
        self.assertEqual(davros_end_step({"A": 2})[:2], (0, 0))

    def test_bloodletter_halves_the_threshold_on_our_turn(self):
        # Any 2 points of loss on our turn become 4: Missy's ping with 2 artifact creatures, a Dalek token hit
        # of 3 becomes 6, Boltwave 6, Fiery Confluence 2-2-2 becomes 12 to each opponent.
        for amount, need in ((1, False), (2, True), (3, True)):
            lost = {}
            lose(lost, "A", amount, bloodletter=True)
            self.assertEqual(lost["A"] >= 3, need, amount)
        lost = {}
        lose(lost, "A", 2, our_turn=False, bloodletter=True)
        self.assertEqual(lost["A"], 2)  # not doubled on an opponent's turn
        lost = {}
        for o in OPPS:
            lose(lost, o, 6, bloodletter=True)
        self.assertEqual(lost, {o: 12 for o in OPPS})


class PassCBoundedMeasuredTests(unittest.TestCase):
    """Bounded finite versions of the three Pass C requested tests, over enumerated cases."""

    @classmethod
    def setUpClass(cls):
        cls.o = oracle()
        cls.cand, cls.base = names(CAND), names(BASE)

    def test_1_unlicensed_disintegration_variants(self):
        """Enumerate target legal/illegal on resolution x artifact controlled x our turn/other turn x the
        controller already qualified or not. 'Qualifies' = adds a Davros-qualified opponent at our end step."""
        rows = []
        for legal in (True, False):
            for artifact in (True, False):
                for our_turn in (True, False):
                    for pre in (0, 3):
                        # CR 608.2b: with its only target illegal the spell does not resolve: no destroy, no damage.
                        destroyed = legal
                        dmg = 3 if (legal and artifact) else 0
                        newly = (our_turn and pre < 3 and pre + dmg >= 3)
                        rows.append((legal, artifact, our_turn, pre, destroyed, dmg, newly))
        self.assertEqual(len(rows), 16)
        self.assertEqual(sum(r[4] for r in rows), 8)            # kills in every legal-target case
        self.assertEqual(sum(r[6] for r in rows), 1)            # newly qualifies only: legal, artifact, our turn, pre 0
        self.assertEqual(sum(1 for r in rows if r[5] == 3), 4)
        # It qualifies at most one opponent (the creature's controller), never all opponents.
        # Artifact density: the candidate keeps 23 artifacts incl. Davros (Pass C condition 'controls an artifact').
        arts = sum(q for n, q in self.cand.items() if "Artifact" in self.o[n]["type_line"].split(" // ")[0])
        self.assertEqual(arts, 23)  # 22 in the 99 plus Davros himself
        # Comparison with the cut Weeping Angel (never causes life loss) and kept This Is How It Ends
        # (opponent chooses: lose 5 or shuffle another creature; it qualifies only if they pick life or have no
        # other creature). Across the same 'legal target, our turn' cases:
        tihie = [(other_creatures, 1 if other_creatures == 0 else 0) for other_creatures in (0, 1, 3)]
        self.assertEqual([q for _, q in tihie], [1, 0, 0])      # worst-case qualification
        self.assertNotIn("life", self.o["Weeping Angel"]["oracle_text"])
        self.assertIn("They lose 5 life, or they shuffle another creature", self.o["This Is How It Ends"]["oracle_text"])

    def test_2_ingenious_artillerist_vs_purphoros_variants(self):
        """Artifact ETB events before Davros's end step (0, 1, one batch of 3, three separate 1s, a myriad batch of
        2 in a four-player pod), Artillerist removed in response, and Davros's own post-threshold token."""
        art = lambda events: sum(events)               # 'deals that much damage': one damage per artifact per event
        purph = lambda creature_entries: 2 * creature_entries   # 2 per other creature entering
        cases = {
            "none": ([], 0),
            "one_dalek_token": ([1], 1),
            "genesis_chapter_III_batch_of_3": ([3], 3),
            "three_separate_artifact_creatures": ([1, 1, 1], 3),
            "dalek_squadron_myriad_batch_of_2": ([2], 2),
        }
        got = {k: (art(ev), purph(n)) for k, (ev, n) in cases.items()}
        self.assertEqual(got, {"none": (0, 0), "one_dalek_token": (1, 2), "genesis_chapter_III_batch_of_3": (3, 6),
                               "three_separate_artifact_creatures": (3, 6), "dalek_squadron_myriad_batch_of_2": (2, 4)})
        # Each opponent qualified (>=3) from those events alone:
        self.assertEqual([k for k, (a, p) in got.items() if a >= 3],
                         ["genesis_chapter_III_batch_of_3", "three_separate_artifact_creatures"])
        self.assertEqual([k for k, (a, p) in got.items() if p >= 3],
                         ["genesis_chapter_III_batch_of_3", "three_separate_artifact_creatures",
                          "dalek_squadron_myriad_batch_of_2"])
        # Removal response: Artillerist (3/1 creature) destroyed in response -> 0; Purphoros is an indestructible
        # enchantment (a non-creature below devotion 5) and survives destroy effects; exile/bounce still answer it.
        self.assertIn("Indestructible", self.o["Purphoros, God of the Forge"]["oracle_text"])
        self.assertEqual(self.o["Ingenious Artillerist"]["toughness"], "1")
        # Davros's own token is created only after an opponent qualified; with a second Davros resolution
        # (Roaming Throne) the token's damage can qualify the OTHER opponents before the second check.
        base = {"A": 3, "B": 1, "C": 1}
        t, ch, _ = davros_end_step(base, triggers=2)
        self.assertEqual((t, ch), (2, 2))
        def purph_tok(lost):
            for o in OPPS:
                lose(lost, o, 2)
        def art_tok(lost):
            for o in OPPS:
                lose(lost, o, 1)
        self.assertEqual(davros_end_step(base, triggers=2, on_token=purph_tok)[:2], (2, 4))
        self.assertEqual(davros_end_step(base, triggers=2, on_token=art_tok)[:2], (2, 2))  # 1+1 < 3
        self.assertEqual(davros_end_step({"A": 1, "B": 1, "C": 1}, triggers=2, on_token=purph_tok)[:2], (0, 0))
        # With one resolution the post-threshold token never creates the original qualification (Pass C).
        self.assertEqual(davros_end_step(base, triggers=1, on_token=purph_tok)[:2], (1, 1))
        # Purphoros also counts nonartifact creature entries (Tectonic Giant, Tergrid, Bloodletter) and is an
        # enchantment, so artifact wipes do not hit it; Artillerist counts noncreature artifacts (rocks, Saga).
        self.assertIn("Whenever one or more artifacts you control enter", self.o["Ingenious Artillerist"]["oracle_text"])

    def test_3_fiery_confluence_vs_current_enablers(self):
        """Damage to each opponent, mana value and whole-table qualification from zero prior loss, with and
        without Bloodletter, plus the targeted-artifact-mode failure case."""
        o = self.o
        each = {"Boltwave": 3, "Maestros Charm": 3, "Fiery Confluence 2-2-2": 6, "Fiery Confluence 2-2-artifact": 4,
                "Flame Rift": 4, "Tectonic Giant attack": 3}
        mv = {"Boltwave": o["Boltwave"]["cmc"], "Maestros Charm": o["Maestros Charm"]["cmc"],
              "Fiery Confluence": o["Fiery Confluence"]["cmc"], "Flame Rift": o["Flame Rift"]["cmc"]}
        self.assertEqual(mv, {"Boltwave": 1.0, "Maestros Charm": 3.0, "Fiery Confluence": 4.0, "Flame Rift": 2.0})
        for k, v in each.items():
            self.assertGreaterEqual(v, 3, k)        # every listed enabler qualifies the whole table alone
        # From a prior 1-point loss (e.g. one Missy ping), all still qualify; with Bloodletter each doubles.
        self.assertEqual({k: 2 * v for k, v in each.items()}["Fiery Confluence 2-2-2"], 12)
        # Targeted-artifact-mode failure: if Fiery Confluence's only target (the artifact) is illegal on
        # resolution, the whole spell does not resolve (CR 608.2b), so its damage modes are lost too.
        def confluence(modes, target_legal):
            if "artifact" in modes and not target_legal:
                return 0
            return 2 * modes.count("burn")
        self.assertEqual(confluence(["burn", "burn", "artifact"], True), 4)
        self.assertEqual(confluence(["burn", "burn", "artifact"], False), 0)
        self.assertEqual(confluence(["burn", "burn", "burn"], False), 6)
        # Opportunity cost: it takes Vandalblast's slot (artifact removal stays: up to three targeted artifacts),
        # not Perforating Artist's (an end-step enabler that stays) or Weeping Angel's (taken by Disintegration).
        self.assertIn("Fiery Confluence", self.cand)
        self.assertIn("Perforating Artist", self.cand)
        self.assertNotIn("Vandalblast", self.cand)
        self.assertIn("Overload", o["Vandalblast"]["oracle_text"])   # the loss: one-sided artifact sweep

    def test_tectonic_giant_and_tergrid_lines(self):
        # Tectonic Giant: attack trigger resolves in declare attackers, before blocks: 3 to each opponent.
        lost = {}
        for opp in OPPS:
            lose(lost, opp, 3)
        self.assertEqual(davros_end_step(lost)[:2], (1, 3))
        # Tergrid: opponents choose sacrifice / discard / life in Court of Ambition, Torment of Hailfire and
        # Perforating Artist; Davros's discard option and Doomsday Confluence's discard feed Tergrid only when the
        # discarded card is a permanent card (the opponent chooses which card).
        for c in ("Court of Ambition", "Torment of Hailfire", "Perforating Artist"):
            self.assertIn("unless", self.o[c]["oracle_text"], c)
        # Anti-synergy disclosed: Dauthi Voidwalker exiles opponents' cards instead of the graveyard, so Tergrid
        # cannot return them while Voidwalker is out.
        self.assertIn("instead exile it with a void counter", self.o["Dauthi Voidwalker"]["oracle_text"])
        self.assertIn("from a graveyard onto the battlefield", self.o["Tergrid, God of Fright"]["oracle_text"])


class CandidateDeckChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.o = oracle()
        cls.cand, cls.base = names(CAND), names(BASE)

    def test_exact_swaps_core_preserved_and_quantities(self):
        self.assertEqual(sorted((self.cand - self.base).elements()), sorted(ADDS))
        self.assertEqual(sorted((self.base - self.cand).elements()), sorted(CUTS))
        for c in CORE:
            self.assertEqual(self.cand[c], 1, c)
        self.assertEqual(sum(self.cand.values()), 100)
        land = lambda n: "Land" in self.o[n]["type_line"].split(" // ")[0]
        lands = sum(q for n, q in self.cand.items() if land(n))
        self.assertEqual(lands, 34)
        self.assertEqual(lands, sum(q for n, q in self.base.items() if land(n)))
        self.assertEqual((self.cand["Island"], self.cand["Mountain"], self.cand["Swamp"]), (2, 3, 3))

    def test_legality_identity_singleton_and_game_changers(self):
        for n, q in self.cand.items():
            c = self.o[n]
            self.assertEqual(c["commander_legality"], "legal", n)
            self.assertTrue(set(c["color_identity"]) <= {"U", "B", "R"}, n)
            if "Basic Land" not in c["type_line"]:
                self.assertEqual(q, 1, n)
        self.assertEqual(sorted(n for n in self.base if self.o[n]["game_changer"]), GAME_CHANGERS_BASE)
        self.assertEqual(sorted(n for n in self.cand if self.o[n]["game_changer"]), GAME_CHANGERS_CAND)
        self.assertEqual([a for a in ADDS if self.o[a]["game_changer"]], ["Tergrid, God of Fright"])

    def test_spellbook_no_included_combos(self):
        sb = json.loads(SPELLBOOK.read_text())
        self.assertEqual(sb["baseline"]["included"], [])
        self.assertEqual(sb["candidate"]["included"], [])


if __name__ == "__main__":
    unittest.main()
