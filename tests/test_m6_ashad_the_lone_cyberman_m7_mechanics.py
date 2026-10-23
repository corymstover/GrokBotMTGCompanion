"""Finite source-anchored rules/mana cases for the Ashad, the Lone Cyberman M7 candidate.

Seed 0, no randomness. Bounded rules model, NOT a game engine or win-rate measurement;
supports no improvement claim by itself.
"""
from collections import Counter
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SNAP = ROOT / "data/grixis/m6/oracle_snapshots/Ashad__the_Lone_Cyberman_M7_Scryfall_20261023.json"
CAND = ROOT / "data/grixis/m7/candidate_lists/Ashad__the_Lone_Cyberman.txt"
BASE = ROOT / "data/grixis/m7/baseline_sources/Ashad_the_Lone_Cyberman_approved_source_2026-10-13.txt"
SPELLBOOK = ROOT / "data/grixis/m7/research_challengers/Ashad__the_Lone_Cyberman_CommanderSpellbook_20261023.json"
ADDS = ["Skullclamp", "Piggy Bank", "Razorlash Transmogrant", "Necron Deathmark", "Royal Warden"]
CUTS = ["Fellwar Stone", "Reckless Fireweaver", "Thoughtcast", "Marionette Master", "Thopter Spy Network"]
ROCKS = {"Sol Ring", "Arcane Signet", "Fellwar Stone", "Rakdos Signet", "Talisman of Creativity",
         "Talisman of Dominance", "Talisman of Indulgence", "Mox Opal", "Cursed Mirror"}
CORE = ["Twinning Staff", "Shimmer Myr", "Biotransference", "Esoteric Duplicator", "Urza, Lord High Artificer",
        "Worldwalker Helm", "Artificer Class", "Krark-Clan Ironworks", "Ashnod's Altar", "Phyrexian Altar",
        "Pitiless Plunderer", "Mayhem Devil", "Disciple of the Vault", "Wurmcoil Engine", "Portal to Phyrexia"]


def names(path):
    out = Counter()
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            q, raw = line.split("x ", 1)
            out[raw.removesuffix(" [Commander]")] += int(q)
    return out


def ashad_turn(spells, board):
    """Model Ashad: only the FIRST nonlegendary artifact spell CAST this turn has casualty 2.

    spells: list of (name, is_nonlegendary_artifact, bodies_on_etb). board: creature powers.
    Copies are not cast; the copy also makes its ETB bodies. Returns (copies, sacrifices, board).
    """
    copies = sacs = 0
    used = False
    board = list(board)
    for _, artifact, bodies in spells:
        mult = 1
        if artifact and not used:
            used = True
            eligible = [p for p in board if p >= 2]
            if eligible:
                board.remove(min(eligible))
                copies += 1
                sacs += 1
                mult = 2
        board.extend(bodies * mult)
    return copies, sacs, board


class AshadM7Mechanics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cards = {c["name"]: c for c in json.loads(SNAP.read_text())["cards"]}
        cls.cand, cls.base = names(CAND), names(BASE)

    def test_commander_oracle_first_nonlegendary_artifact_casualty_2(self):
        t = self.cards["Ashad, the Lone Cyberman"]["oracle_text"]
        self.assertIn("The first nonlegendary artifact spell you cast each turn has casualty 2", t)
        self.assertIn("Whenever you sacrifice another creature, put a +1/+1 counter on Ashad", t)

    def test_slot_used_by_first_artifact_even_without_fodder(self):
        self.assertEqual(ashad_turn([("Sol Ring", True, []), ("Royal Warden", True, [3, 2, 2])], [])[0], 0)
        self.assertEqual(ashad_turn([("Royal Warden", True, [3, 2, 2]), ("Piggy Bank", True, [3])], [])[0], 0)
        c, s, board = ashad_turn([("Royal Warden", True, [3, 2, 2])], [3])
        self.assertEqual((c, s, len(board)), (1, 1, 6))

    def test_all_adds_are_nonlegendary_artifacts_and_bodies_pay_casualty(self):
        for n in ADDS:
            tl = self.cards[n]["type_line"]
            self.assertIn("Artifact", tl, n)
            self.assertNotIn("Legendary", tl, n)
        for n in ["Piggy Bank", "Razorlash Transmogrant", "Necron Deathmark", "Royal Warden"]:
            self.assertGreaterEqual(int(self.cards[n]["power"]), 2, n)
        self.assertIn("two tapped 2/2 black Necron Warrior artifact creature tokens", self.cards["Royal Warden"]["oracle_text"])
        self.assertIn("When this creature dies, create a Treasure token", self.cards["Piggy Bank"]["oracle_text"])

    def test_cut_noncasualty_bodies_and_nonartifact_engines(self):
        self.assertLess(int(self.cards["Reckless Fireweaver"]["power"]), 2)
        self.assertNotIn("Artifact", self.cards["Marionette Master"]["type_line"])
        self.assertEqual(self.cards["Thopter Spy Network"]["type_line"], "Enchantment")
        self.assertIn("1/1 colorless Thopter", self.cards["Thopter Spy Network"]["oracle_text"])
        self.assertEqual(self.cards["Thoughtcast"]["type_line"], "Sorcery")

    def test_skullclamp_lifts_toughness_two_one_power_bodies(self):
        t = self.cards["Skullclamp"]["oracle_text"]
        self.assertIn("Equipped creature gets +1/-1", t)
        self.assertIn("Whenever equipped creature dies, draw two cards", t)
        lifted = [n for n, q in self.cand.items() if "Creature" in self.cards[n]["type_line"]
                  and self.cards[n]["power"] == "1" and int(self.cards[n]["toughness"]) >= 2]
        self.assertEqual(sorted(lifted), sorted(["Emry, Lurker of the Loch", "Etherium Sculptor",
                                                 "Padeem, Consul of Innovation", "Pitiless Plunderer",
                                                 "Urza, Lord High Artificer"]))

    def test_necron_deathmark_flash_copy_kills_two(self):
        t = self.cards["Necron Deathmark"]["oracle_text"]
        self.assertTrue(t.startswith("Flash"))
        self.assertIn("destroy up to one target creature", t)
        copies, _, _ = ashad_turn([("Necron Deathmark", True, [5])], [3])
        self.assertEqual(1 + copies, 2)

    def test_razorlash_conditional_loop_is_mana_neutral_and_spellbook_listed(self):
        r = self.cards["Razorlash Transmogrant"]["oracle_text"]
        self.assertIn("{4}{B}{B}: Return this card from your graveyard to the battlefield", r)
        self.assertIn("costs {4} less to activate if an opponent controls four or more nonbasic lands", r)
        self.assertIn("Sacrifice a creature: Add one mana of any color", self.cards["Phyrexian Altar"]["oracle_text"])
        self.assertIn("Whenever another creature you control dies, create a Treasure token",
                      self.cards["Pitiless Plunderer"]["oracle_text"])
        produced = 1 + 1  # Altar + Treasure
        cost_discounted, cost_full = 2, 6
        self.assertEqual(produced - cost_discounted, 0)
        self.assertLess(produced - cost_full, 0)  # no loop without the nonbasic-land condition
        sb = json.loads(SPELLBOOK.read_text())
        cand_ids = {x[0] for x in sb["candidate"]["included"]}
        base_ids = {x[0] for x in sb["baseline"]["included"]}
        self.assertEqual(base_ids, {"66-457-5491"})
        self.assertEqual(cand_ids, {"66-457-5491", "4050-4871-6429"})
        for x in sb["candidate"]["included"]:
            self.assertGreaterEqual(len(x[1]), 3)  # no two-card infinite

    def test_exact_swaps_and_core_preserved(self):
        self.assertEqual(sorted((self.cand - self.base).elements()), sorted(ADDS))
        self.assertEqual(sorted((self.base - self.cand).elements()), sorted(CUTS))
        for n in CORE:
            self.assertEqual(self.cand[n], 1, n)

    def test_quantity_counted_lands_rocks_fodder(self):
        land = lambda d: sum(q for n, q in d.items() if "Land" in self.cards[n]["type_line"])
        self.assertEqual(land(self.base), 30)
        self.assertEqual(land(self.cand), 30)
        self.assertEqual(sum(q for n, q in self.base.items() if n in ROCKS), 9)
        self.assertEqual(sum(q for n, q in self.cand.items() if n in ROCKS), 8)
        self.assertEqual((self.base["Island"], self.base["Mountain"], self.base["Swamp"]), (3, 2, 3))
        fod = lambda d: sum(q for n, q in d.items() if n != "Ashad, the Lone Cyberman"
                            and "Creature" in self.cards[n]["type_line"]
                            and (self.cards[n]["power"] or "0").isdigit() and int(self.cards[n]["power"]) >= 2)
        self.assertEqual(fod(self.base), 17)
        self.assertEqual(fod(self.cand), 21)
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
        self.assertEqual(gc(self.cand), ["Cyclonic Rift", "Demonic Tutor", "Fierce Guardianship"])


if __name__ == "__main__":
    unittest.main()
