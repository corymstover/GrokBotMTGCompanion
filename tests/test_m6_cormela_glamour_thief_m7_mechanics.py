"""Finite source-anchored rules/mana cases for the Cormela, Glamour Thief M7 candidate.

Seed 0, no randomness. A bounded rules model, NOT a game engine or win-rate measurement;
it supports no improvement claim by itself.
"""
from collections import Counter
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
D = "Cormela__Glamour_Thief"
SNAP = ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json"
CAND = ROOT / f"data/grixis/m7/candidate_lists/{D}.txt"
BASE = ROOT / f"data/grixis/m7/baseline_sources/{D}_approved_source_2026-10-14.txt"
SPELLBOOK = ROOT / f"data/grixis/m7/research_challengers/{D}_CommanderSpellbook_20261023.json"
CORMELA = "Cormela, Glamour Thief"
BIRGI = "Birgi, God of Storytelling // Harnfel, Horn of Bounty"
ADDS = ["Mistrise Village", "Underground River", "Frantic Search", "Twinflame", "Hexing Squelcher"]
CUTS = ["Undercity Sewers", "Exotic Orchard", "Faithless Looting", "Gitaxian Probe", "Red Elemental Blast"]
CORE = ["Saw in Half", "Molten Duplication", "Demonic Gifts", "Shallow Grave", "Goryo's Vengeance", "Ashnod's Altar",
        "Phyrexian Altar", "Dualcaster Mage", BIRGI, "Dark Ritual", "Cabal Ritual", "Seething Song", "Culling the Weak",
        "Tendrils of Agony", "Brain Freeze", "Thassa's Oracle", "Demonic Consultation", "Tainted Pact",
        "Underworld Breach", "Lion's Eye Diamond", "Lotus Petal", "Pyroblast"]
GAME_CHANGERS = ["Ad Nauseam", "Ancient Tomb", "Chrome Mox", "Demonic Tutor", "Fierce Guardianship", "Force of Will",
                 "Gamble", "Imperial Seal", "Intuition", "Jeska's Will", "Lion's Eye Diamond", "Mana Vault",
                 "Mox Diamond", "Mystical Tutor", "Necropotence", "Orcish Bowmasters", "Rhystic Study",
                 "Thassa's Oracle", "Underworld Breach", "Vampiric Tutor"]
FETCH = {"Bloodstained Mire": ("Swamp", "Mountain"), "Flooded Strand": ("Plains", "Island"),
         "Marsh Flats": ("Plains", "Swamp"), "Misty Rainforest": ("Forest", "Island"),
         "Polluted Delta": ("Island", "Swamp"), "Scalding Tarn": ("Island", "Mountain"),
         "Wooded Foothills": ("Mountain", "Forest")}


def names(path):
    out = Counter()
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            q, raw = line.split(" ", 1)
            out[raw.removesuffix(" [Commander]")] += int(q.rstrip("x"))
    return out


def frantic_with_cormela(tapped_lands):
    """Pay Cormela's {1} activation with one land, cast Frantic Search ({2}{U}) entirely with her restricted
    {U}{B}{R}, then untap up to three lands. Returns (net unrestricted land mana, restricted mana left). Finite."""
    tapped = tapped_lands + 1          # activation cost {1}
    restricted = 3 - 3                 # {U}{B}{R} pays {2}{U}
    untapped = min(3, tapped)
    return untapped - 1, restricted


def saw_loop_net(converter):
    """One Cormela + Saw in Half iteration (Spellbook 500-xxxx-4867). Two deaths return Saw and the converter.
    The surviving hasty token pays {1} for {U}{B}{R}; Saw costs 3. Net total mana per iteration."""
    cost, produce = {"Dark Ritual": (1, 3), "Seething Song": (3, 5), "Cabal Ritual (threshold)": (2, 5),
                     "Frantic Search": (3, 3)}[converter]
    return 3 - 1 - 3 - cost + produce


def twinflame_loop(unrestricted, birgi, cap=50):
    """Twinflame on the untapped Cormela copy: the legend rule kills the old copy, its death trigger returns Twinflame,
    and the new hasty copy pays {1} (unrestricted only) for {U}{B}{R}, which pays Twinflame's {1}{R}. Birgi adds an
    unrestricted {R} per spell cast. Returns iterations (capped at `cap`)."""
    restricted, n = 0, 0
    while n < cap and unrestricted >= 1:
        unrestricted -= 1
        restricted += 3 - 2
        unrestricted += 1 if birgi else 0
        n += 1
    return n


class CormelaM7Mechanics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cards = {c["name"]: c for c in json.loads(SNAP.read_text())["cards"]}
        cls.cand, cls.base = names(CAND), names(BASE)

    def test_commander_oracle(self):
        c = self.cards[CORMELA]
        self.assertIn("Haste", c["oracle_text"])
        self.assertIn("{1}, {T}: Add {U}{B}{R}. Spend this mana only to cast instant and/or sorcery spells.", c["oracle_text"])
        self.assertIn("When Cormela dies, return up to one target instant or sorcery card from your graveyard to your hand.",
                      c["oracle_text"])
        self.assertEqual((c["power"], c["toughness"], c["cmc"]), ("2", "4", 4.0))

    def test_frantic_search_converts_restricted_mana_finite(self):
        f = self.cards["Frantic Search"]
        self.assertEqual(f["mana_cost"], "{2}{U}")
        self.assertIn("Untap up to three lands.", f["oracle_text"])
        self.assertEqual(frantic_with_cormela(3), (2, 0))
        self.assertEqual(frantic_with_cormela(1), (1, 0))
        self.assertIn("Flashback", self.cards["Faithless Looting"]["oracle_text"])

    def test_saw_in_half_loop_converters_and_frantic_not_infinite(self):
        self.assertIn("creates two tokens that are copies", self.cards["Saw in Half"]["oracle_text"])
        self.assertEqual(saw_loop_net("Dark Ritual"), 1)
        self.assertEqual(saw_loop_net("Seething Song"), 1)
        self.assertEqual(saw_loop_net("Cabal Ritual (threshold)"), 2)
        self.assertEqual(saw_loop_net("Frantic Search"), -1)

    def test_twinflame_loop_finite_alone_infinite_only_with_birgi(self):
        t = self.cards["Twinflame"]["oracle_text"]
        self.assertIn("create a token that's a copy of that creature, except it has haste", t)
        self.assertIn("Whenever you cast a spell, add {R}.", self.cards[BIRGI]["oracle_text"])
        self.assertEqual(twinflame_loop(0, False), 0)
        self.assertEqual(twinflame_loop(3, False), 3)
        self.assertEqual(twinflame_loop(1, True, cap=50), 50)

    def test_protection_adds_and_cut_rationale_text(self):
        h = self.cards["Hexing Squelcher"]["oracle_text"]
        self.assertIn("Spells you control can't be countered.", h)
        self.assertIn("Ward—Pay 2 life.", h)
        self.assertIn("Creature", self.cards["Hexing Squelcher"]["type_line"])
        m = self.cards["Mistrise Village"]["oracle_text"]
        self.assertIn("enters tapped unless you control a Mountain or a Forest", m)
        self.assertIn("The next spell you cast this turn can't be countered.", m)
        self.assertIn("This land enters tapped.", self.cards["Undercity Sewers"]["oracle_text"])
        self.assertIn("an opponent controls could produce", self.cards["Exotic Orchard"]["oracle_text"])
        self.assertIn("Counter target blue spell", self.cards["Red Elemental Blast"]["oracle_text"])
        self.assertIn("Counter target spell if it's blue", self.cards["Pyroblast"]["oracle_text"])

    def test_spellbook_combos(self):
        sb = json.loads(SPELLBOOK.read_text())
        ids = lambda k: {x["id"] for x in sb[k]["included"]}
        self.assertEqual(len(ids("baseline")), 23)
        self.assertEqual(ids("candidate"), ids("baseline") | {"147-1235", "392-1235-4867"})
        for x in sb["candidate"]["included"]:
            for n in x["uses"]:
                self.assertEqual(self.cand[n], 1, (x["id"], n))

    def test_exact_swaps_and_core(self):
        self.assertEqual(sorted((self.cand - self.base).elements()), sorted(ADDS))
        self.assertEqual(sorted((self.base - self.cand).elements()), sorted(CUTS))
        for n in CORE + [CORMELA]:
            self.assertEqual(self.cand[n], 1, n)

    def test_quantity_counted_lands_and_mistrise_enablers(self):
        front = lambda n: self.cards[n]["type_line"].split("//")[0]
        land = lambda d: sum(q for n, q in d.items() if "Land" in front(n))
        self.assertEqual((land(self.base), land(self.cand)), (30, 30))
        self.assertEqual(sum(self.cand.values()), 100)
        self.assertEqual(sum(self.base.values()), 100)
        mountains = sorted(n for n in self.cand if "Mountain" in front(n))
        self.assertEqual(mountains, ["Badlands", "Blood Crypt", "Mountain", "Steam Vents", "Volcanic Island"])
        for f, types in FETCH.items():
            self.assertEqual(self.cand[f], 1, f)
            self.assertIn(f"{types[0]} or {types[1]}", self.cards[f]["oracle_text"].replace("an ", "a "))
            self.assertTrue(any(t in front(m) for m in mountains for t in types), f)
        always_tapped = [n for n in self.cand if "This land enters tapped." in self.cards[n]["oracle_text"]]
        self.assertEqual(always_tapped, [])

    def test_legality_identity_singleton_game_changers(self):
        for n, q in self.cand.items():
            c = self.cards[n]
            self.assertEqual(c["commander_legality"], "legal", n)
            self.assertTrue(set(c["color_identity"]) <= {"U", "B", "R"}, n)
            self.assertEqual(q, 1, n)
        gc = lambda d: sorted(n for n in d if self.cards[n]["game_changer"])
        self.assertEqual(gc(self.cand), gc(self.base))
        self.assertEqual(gc(self.cand), GAME_CHANGERS)
        self.assertFalse(any(self.cards[n]["game_changer"] for n in ADDS))

    def test_tainted_pact_unique_names_and_breach_finite(self):
        self.assertEqual(len(self.cand), 100)
        self.assertIn("exile two cards with the same name", self.cards["Tainted Pact"]["oracle_text"])
        self.assertIn("exile three other cards from your graveyard", self.cards["Underworld Breach"]["oracle_text"])


if __name__ == "__main__":
    unittest.main()
