"""Finite source-anchored rules/mana cases for the Ashnod the Uncaring M7 candidate.

Seed 0, no randomness. Bounded rules model, NOT a game engine or win-rate measurement;
supports no improvement claim by itself.
"""
from collections import Counter
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SNAP = ROOT / "data/grixis/m6/oracle_snapshots/Ashnod_the_Uncaring_M7_Scryfall_20261023.json"
CAND = ROOT / "data/grixis/m7/candidate_lists/Ashnod_the_Uncaring.txt"
BASE = ROOT / "data/grixis/m7/baseline_sources/Ashnod_the_Uncaring_approved_source_2026-10-13.txt"
SPELLBOOK = ROOT / "data/grixis/m7/research_challengers/Ashnod_the_Uncaring_CommanderSpellbook_20261023.json"
ADDS = ["Corridor Monitor", "Aether Spellbomb", "Audacious Reshapers", "Priest of Forgotten Gods", "Thopter Squadron"]
CUTS = ["Foundry Inspector", "Fellwar Stone", "Talisman of Indulgence", "Walking Ballista", "Esoteric Duplicator"]
ROCKS = {"Sol Ring", "Arcane Signet", "Fellwar Stone", "Mind Stone", "Talisman of Creativity",
         "Talisman of Dominance", "Talisman of Indulgence", "Mox Opal", "Lotus Petal"}
CORE = ["Clan Crafter", "Bolas's Citadel", "Time Sieve", "Kuldotha Forgemaster", "Repurposing Bay", "Trading Post",
        "Goblin Engineer", "Scrap Welder", "Retrofitter Foundry", "Scrap Trawler", "Myr Retriever",
        "Krark-Clan Ironworks", "Ashnod's Altar", "Crime Novelist", "Disciple of the Vault", "Marionette Apprentice",
        "Mayhem Devil", "Nim Deathmantle", "Urza, Lord High Artificer", "Lotus Petal", "Krark-Clan Shaman"]


def names(path):
    out = Counter()
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            q, raw = line.split("x ", 1)
            out[raw.removesuffix(" [Commander]")] += int(q)
    return out


def ashnod_copies(source_type, is_mana_ability, sacrificed_in_cost):
    """Ashnod: copy if the source is an artifact or creature, the ability is not a mana ability,
    and one or more permanents were sacrificed to activate it (cost, not resolution)."""
    return (("Artifact" in source_type or "Creature" in source_type)
            and not is_mana_ability and sacrificed_in_cost)


def monitor_loop(loops, novelist=False):
    """Engineer + Corridor Monitor + Lotus Petal with Ashnod. Returns (net_mana, artifact_sacs, etbs, engineer_untapped)."""
    mana = 0
    sacs = etbs = 0
    engineer_untapped = True
    petal_in_gy = True
    for _ in range(loops):
        assert engineer_untapped and petal_in_gy
        # Petal returned last loop (or start: tap+sac Petal first) -> R
        mana += 1          # Lotus Petal: {T}, sacrifice: one mana (mana ability, not copied)
        sacs += 1
        mana -= 1          # Engineer {R}
        engineer_untapped = False
        sacs += 1          # sacrifice Monitor as cost -> Ashnod copy, new target Monitor
        if novelist:
            mana += 2      # Crime Novelist: R for each artifact sacrificed (Petal + Monitor)
        etbs += 1          # copy resolves first: Monitor returns
        engineer_untapped = True  # Monitor ETB untaps Engineer
        etbs += 1          # original resolves: Petal returns
    return mana, sacs, etbs, engineer_untapped


def squadron_cycle(counters, altar=True, novelist=True):
    """One cycle: make Thopter A, feed it to Squadron (copied), make Thopter B, sacrifice B for mana."""
    mana = 0
    mana -= 1; counters -= 1                  # {1}, remove counter: Thopter A
    mana -= 1; counters += 2                  # {1}, sacrifice A: +1 counter, Ashnod copy +1
    mana += 1 if novelist else 0
    mana -= 1; counters -= 1                  # {1}, remove counter: Thopter B
    mana += (2 if altar else 0) + (1 if novelist else 0)  # Altar/KCI CC + Novelist R
    return mana, counters


class AshnodM7Mechanics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cards = {c["name"]: c for c in json.loads(SNAP.read_text())["cards"]}
        cls.cand, cls.base = names(CAND), names(BASE)

    def test_commander_oracle_copy_rule_without_turn_limit(self):
        t = self.cards["Ashnod the Uncaring"]["oracle_text"]
        self.assertIn("Whenever you activate an ability of an artifact or creature that isn't a mana ability", t)
        self.assertIn("if one or more permanents were sacrificed to activate it, you may copy that ability", t)
        self.assertNotIn("once each turn", t.lower())
        self.assertNotIn("only once", t.lower())

    def test_copy_eligibility_model(self):
        self.assertTrue(ashnod_copies("Artifact Creature — Construct", False, True))
        self.assertFalse(ashnod_copies("Artifact", True, True))      # KCI / Petal / Treasure
        self.assertFalse(ashnod_copies("Land", False, True))         # Buried Ruin, Inventors' Fair
        self.assertTrue(ashnod_copies("Artifact Land", False, True))  # Treasure Vault
        self.assertFalse(ashnod_copies("Creature — Goblin Artificer", False, False))  # Goblin Welder

    def test_every_add_has_a_sacrifice_cost_ability_or_is_a_combo_piece(self):
        self.assertIn("Sacrifice this artifact: Return target creature", self.cards["Aether Spellbomb"]["oracle_text"])
        self.assertIn("{1}, Sacrifice this artifact: Draw a card", self.cards["Aether Spellbomb"]["oracle_text"])
        self.assertIn("{T}, Sacrifice an artifact: Reveal cards", self.cards["Audacious Reshapers"]["oracle_text"])
        self.assertIn("{T}, Sacrifice two other creatures: Any number of target players each lose 2 life",
                      self.cards["Priest of Forgotten Gods"]["oracle_text"])
        self.assertIn("{1}, Sacrifice another Thopter: Put a +1/+1 counter", self.cards["Thopter Squadron"]["oracle_text"])
        self.assertIn("When this creature enters, untap target artifact or creature you control",
                      self.cards["Corridor Monitor"]["oracle_text"])
        self.assertIn("Artifact", self.cards["Corridor Monitor"]["type_line"])
        self.assertEqual(self.cards["Corridor Monitor"]["cmc"], 2.0)

    def test_cuts_have_no_ashnod_copyable_sacrifice_ability_except_duplicator(self):
        for n in ["Foundry Inspector", "Fellwar Stone", "Talisman of Indulgence", "Walking Ballista"]:
            self.assertNotIn("Sacrifice", self.cards[n]["oracle_text"], n)
        self.assertIn("{2}, Sacrifice this artifact: Draw a card", self.cards["Esoteric Duplicator"]["oracle_text"])

    def test_priest_copy_doubles_drain_edict_mana_draw(self):
        once = {"life_per_opp": 2, "edicts_per_opp": 1, "black": 2, "cards": 1}
        doubled = {k: v * 2 for k, v in once.items()}
        self.assertEqual(doubled, {"life_per_opp": 4, "edicts_per_opp": 2, "black": 4, "cards": 2})

    def test_engineer_monitor_petal_loop_is_mana_neutral_and_repeatable(self):
        self.assertIn("{R}, {T}, Sacrifice an artifact: Return target artifact card with mana value 3 or less",
                      self.cards["Goblin Engineer"]["oracle_text"])
        self.assertIn("{T}, Sacrifice this artifact: Add one mana of any color", self.cards["Lotus Petal"]["oracle_text"])
        mana, sacs, etbs, untapped = monitor_loop(25)
        self.assertEqual(mana, 0)
        self.assertEqual((sacs, etbs), (50, 50))
        self.assertTrue(untapped)
        self.assertEqual(monitor_loop(10, novelist=True)[0], 20)

    def test_squadron_loop_needs_novelist_and_altar(self):
        m, c = squadron_cycle(3)
        self.assertEqual((m, c), (1, 3))
        self.assertLess(squadron_cycle(3, novelist=False)[0], 0)
        self.assertLess(squadron_cycle(3, altar=False)[0], 0)
        self.assertIn("Whenever you sacrifice an artifact, put a +1/+1 counter on this creature and add {R}",
                      self.cards["Crime Novelist"]["oracle_text"])

    def test_spellbook_delta_and_no_two_card_infinite(self):
        sb = json.loads(SPELLBOOK.read_text())
        base_ids = {x[0] for x in sb["baseline"]["included"]}
        cand_ids = {x[0] for x in sb["candidate"]["included"]}
        self.assertEqual(len(base_ids), 15)
        self.assertEqual(cand_ids - base_ids, {"1414-1649-2068-4404", "2034-2068-2762-5346", "2068-2762-4659-5346"})
        self.assertEqual(base_ids - cand_ids, {"777-1020-2866-4659", "777-1020-2034-2866"})
        for x in sb["baseline"]["included"]:
            self.assertNotIn("Ashnod the Uncaring", x[1])
        for x in sb["candidate"]["included"]:
            self.assertGreaterEqual(len(x[1]), 3)

    def test_exact_swaps_and_core_preserved(self):
        self.assertEqual(sorted((self.cand - self.base).elements()), sorted(ADDS))
        self.assertEqual(sorted((self.base - self.cand).elements()), sorted(CUTS))
        for n in CORE:
            self.assertEqual(self.cand[n], 1, n)

    def test_quantity_counted_lands_rocks_artifacts_creatures(self):
        tl = lambda n: self.cards[n]["type_line"]
        land = lambda d: sum(q for n, q in d.items() if "Land" in tl(n))
        self.assertEqual((land(self.base), land(self.cand)), (33, 33))
        self.assertEqual(sum(q for n, q in self.base.items() if n in ROCKS), 9)
        self.assertEqual(sum(q for n, q in self.cand.items() if n in ROCKS), 7)
        self.assertEqual((self.base["Island"], self.base["Mountain"], self.base["Swamp"]), (3, 2, 3))
        art = lambda d: sum(q for n, q in d.items() if "Artifact" in tl(n))
        cre = lambda d: sum(q for n, q in d.items() if "Creature" in tl(n) and n != "Ashnod the Uncaring")
        self.assertEqual((art(self.base), art(self.cand)), (43, 41))
        self.assertEqual((cre(self.base), cre(self.cand)), (25, 27))
        self.assertEqual(sum(self.cand.values()), 100)

    def test_legality_identity_singleton_game_changers(self):
        for n, q in self.cand.items():
            c = self.cards[n]
            self.assertEqual(c["commander_legality"], "legal", n)
            self.assertTrue(set(c["color_identity"]) <= {"U", "B", "R"}, n)
            if n not in {"Island", "Swamp", "Mountain"}:
                self.assertEqual(q, 1, n)
        gc = lambda d: sorted(n for n in d if self.cards[n]["game_changer"])
        self.assertEqual(gc(self.cand), gc(self.base))
        self.assertEqual(gc(self.cand), ["Ancient Tomb", "Bolas's Citadel", "Cyclonic Rift", "Demonic Tutor",
                                         "Fierce Guardianship", "Vampiric Tutor"])


if __name__ == "__main__":
    unittest.main()
