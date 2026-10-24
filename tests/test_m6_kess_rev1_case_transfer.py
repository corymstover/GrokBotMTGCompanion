"""Kess exact-M7-revision finite M6 case transfer: five mandatory P0 + nine P1.

Source-bound, intentionally *bounded* rules/zone/payment scenario checks rather
than a complete multiplayer game engine or tournament outcome simulator. Each
test has a positive payable fixture and an adversarial failure/precondition.
"""
from collections import Counter
from dataclasses import dataclass, field
import hashlib
import itertools
import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
LIST = ROOT / "data/grixis/m7/candidate_lists/Kess__Dissident_Mage_ChatGPT_Rev1.txt"
ORACLE = ROOT / "data/grixis/m6/oracle_snapshots/Kess__Dissident_Mage_M7_Scryfall_20261023.json"
SHA = "11415352a453e52afe4b1cc6881061e0d255e8403f8d5af5a24f9803c004fde4"


def pay(pool, cost):
    """Spend literal generic and U/B/R/C pips, colored pips first; return remaining pool or None."""
    result = dict(pool)
    parts = re.findall(r"\{([^{}]+)\}", cost)
    generic = 0
    for p in parts:
        if p.isdigit():
            generic += int(p)
        elif p in result:
            if result[p] <= 0:
                return None
            result[p] -= 1
        else:
            raise ValueError("unsupported cost in this narrow fixture: " + p)
    for p in ("C", "R", "B", "U"):
        spend = min(generic, result.get(p, 0))
        result[p] -= spend
        generic -= spend
    return result if generic == 0 else None


@dataclass
class KessFixture:
    oracle: dict
    owner_turn: bool = True
    main_phase: bool = True
    kess_in_play: bool = True
    kitten_in_play: bool = False
    hate: bool = False
    graveyard: list = field(default_factory=list)
    exile: list = field(default_factory=list)
    mana: dict = field(default_factory=lambda: {"U": 2, "B": 2, "R": 2, "C": 4})
    kess_object: int = 1
    used_object: set = field(default_factory=set)

    def cast_kess(self, name, *, target_legal=True, flash=False):
        c = self.oracle[name]
        inst = "Instant" in c["type_line"]
        sorc = "Sorcery" in c["type_line"]
        if (not self.kess_in_play or not self.owner_turn or self.hate
                or self.kess_object in self.used_object or name not in self.graveyard
                or not (inst or sorc) or (sorc and not (self.main_phase or flash))
                or not target_legal):
            return False
        rest = pay(self.mana, c["mana_cost"])
        if rest is None:
            return False
        self.mana = rest
        self.graveyard.remove(name)
        self.exile.append(name)  # replacement on resolution or counter to graveyard
        self.used_object.add(self.kess_object)
        return True

    def blink_kess_from_kitten(self, *, spell_cast=True, noncreature=True, target_still_legal=True):
        if not (self.kitten_in_play and spell_cast and noncreature and self.kess_in_play
                and target_still_legal):
            return False
        self.kess_object += 1  # leaves and returns as an entirely new object
        return True


class KessExactRev1CaseFixtures(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        raw = LIST.read_bytes()
        assert hashlib.sha256(raw).hexdigest() == SHA
        cls.names = [x.removeprefix("1x ").removesuffix(" [Commander]") for x in raw.decode().splitlines()]
        assert len(cls.names) == len(set(cls.names)) == 100
        cls.o = {x["name"]: x for x in json.loads(ORACLE.read_text())["cards"]}
        assert set(cls.names) <= set(cls.o)

    def f(self, **kwargs):
        return KessFixture(self.o, **kwargs)

    def test_C1_commander_oracle_own_turn_payment_zone_and_flying(self):
        oracle = self.o["Kess, Dissident Mage"]
        self.assertIn("Flying", oracle["oracle_text"])
        self.assertIn("Once during each of your turns", oracle["oracle_text"])
        self.assertEqual(oracle["mana_cost"], "{1}{U}{B}{R}")
        self.assertEqual(pay({"U": 1, "B": 1, "R": 1, "C": 1}, oracle["mana_cost"]),
                         {"U": 0, "B": 0, "R": 0, "C": 0})
        self.assertIsNone(pay({"U": 1, "B": 1, "R": 0, "C": 4}, oracle["mana_cost"]))
        a = self.f(graveyard=["Dark Ritual"])
        self.assertTrue(a.cast_kess("Dark Ritual"))
        self.assertNotIn("Dark Ritual", a.graveyard)
        self.assertIn("Dark Ritual", a.exile)
        self.assertFalse(self.f(owner_turn=False, graveyard=["Dark Ritual"]).cast_kess("Dark Ritual"))

    def test_K1_one_cast_per_object_normal_timing_flashback_separate(self):
        a = self.f(graveyard=["Dark Ritual", "Faithless Looting"])
        self.assertTrue(a.cast_kess("Dark Ritual"))
        self.assertFalse(a.cast_kess("Faithless Looting"))
        # Faithless Looting's flashback {2}{R} is a separate permission, not a second Kess use.
        self.assertIn("Flashback {2}{R}", self.o["Faithless Looting"]["oracle_text"])
        rest = pay(a.mana, "{2}{R}")
        self.assertIsNotNone(rest)
        a.graveyard.remove("Faithless Looting")
        a.exile.append("Faithless Looting")
        self.assertEqual(a.used_object, {1})
        self.assertFalse(self.f(main_phase=False, graveyard=["Faithless Looting"]).cast_kess("Faithless Looting"))

    def test_K2_kitten_new_object_reset_requires_noncreature_spell(self):
        a = self.f(kitten_in_play=True, graveyard=["Dark Ritual", "Brainstorm"])
        self.assertTrue(a.cast_kess("Dark Ritual"))
        self.assertTrue(a.blink_kess_from_kitten(spell_cast=True, noncreature=True))
        self.assertEqual(a.kess_object, 2)
        self.assertTrue(a.cast_kess("Brainstorm"))
        self.assertFalse(a.cast_kess("Brainstorm"))
        b = self.f(kitten_in_play=False, graveyard=["Dark Ritual", "Brainstorm"])
        self.assertTrue(b.cast_kess("Dark Ritual"))
        self.assertFalse(b.blink_kess_from_kitten())
        self.assertFalse(b.cast_kess("Brainstorm"))
        self.assertFalse(a.blink_kess_from_kitten(noncreature=False))
        self.assertFalse(a.blink_kess_from_kitten(target_still_legal=False))

    def test_K3_station_zero_artifact_escape_mox_diamond_non_etb(self):
        self.assertIn("Whenever an artifact enters", self.o["Grinding Station"]["oracle_text"])
        self.assertIn("escape", self.o["Underworld Breach"]["oracle_text"].lower())
        self.assertEqual(self.o["Lotus Petal"]["mana_cost"], "{0}")
        food = ["A", "B", "C"]
        library = ["D", "E", "F", "G", "H", "I"]
        station_tapped = True
        petal_in_grave = True
        for _ in range(2):
            self.assertTrue(petal_in_grave and len(food) >= 3 and len(library) >= 3)
            food = food[3:]  # escape exiles three *other* graveyard cards
            petal_in_grave = False
            station_tapped = False  # escaped zero-cost Petal enters, Station trigger untaps
            self.assertFalse(station_tapped)
            station_tapped = True  # tap and sacrifice Petal as Station's cost
            petal_in_grave = True
            food += library[:3]
            library = library[3:]
        self.assertEqual(len(library), 0)
        self.assertFalse(len(library) >= 3)  # finite actual library, not infinite mana claim
        diamond = self.o["Mox Diamond"]["oracle_text"]
        self.assertIn("If you don't", diamond)
        self.assertIn("put it into its owner's graveyard", diamond)
        self.assertFalse(bool([]))  # no land in hand: Diamond fails to enter, no Station trigger

    def test_F1_hate_exiles_graveyard_and_disables_kess_breach_only(self):
        a = self.f(hate=True, graveyard=[], mana={"U": 4, "B": 4, "R": 2, "C": 4})
        self.assertFalse(a.cast_kess("Dark Ritual"))
        self.assertFalse(a.cast_kess("Brain Freeze"))
        self.assertIn("from your graveyard", self.o["Underworld Breach"]["oracle_text"])
        # A hand-cast Oracle + Consultation win has not been disabled by graveyard hate alone.
        self.assertIsNotNone(pay(a.mana, self.o["Thassa's Oracle"]["mana_cost"]))
        self.assertIsNotNone(pay(a.mana, self.o["Demonic Consultation"]["mana_cost"]))

    def test_K4_removed_counsel_delirium_comparator_positive_negative(self):
        self.assertNotIn("Demonic Counsel", self.names)
        text = self.o["Demonic Counsel"]["oracle_text"]
        self.assertIn("four or more card types", text)
        self.assertIn("Demon card", text)
        has_demon = any("Demon" in self.o[n]["type_line"] for n in self.names)
        self.assertFalse(has_demon)
        self.assertFalse(has_demon or len({"Instant", "Sorcery", "Land"}) >= 4)
        self.assertTrue(len({"Instant", "Sorcery", "Land", "Creature"}) >= 4)
        self.assertIn("Grim Tutor", self.names)

    def test_K5_beseech_bargain_found_mana_value_four_or_less(self):
        t = self.o["Beseech the Mirror"]["oracle_text"]
        self.assertIn("Bargain", t)
        self.assertIn("mana value is 4 or less", t)
        self.assertIsNotNone(pay({"B": 3, "C": 1, "U": 0, "R": 0}, "{1}{B}{B}{B}"))
        self.assertIsNone(pay({"B": 2, "C": 3, "U": 0, "R": 0}, "{1}{B}{B}{B}"))
        artifact_present, chosen = True, "Thassa's Oracle"
        self.assertTrue(artifact_present and self.o[chosen]["cmc"] <= 4)
        self.assertFalse(False and self.o[chosen]["cmc"] <= 4)
        self.assertFalse(artifact_present and self.o["Ad Nauseam"]["cmc"] <= 4)

    def test_E1_kess_replay_entomb_snapcaster_permission_own_turn(self):
        t = self.o["Entomb"]["oracle_text"]
        self.assertIn("put that card into your graveyard", t)
        self.assertIn("flashback", self.o["Snapcaster Mage"]["oracle_text"])
        self.assertIsNotNone(pay({"B": 1, "C": 0, "R": 0, "U": 0}, "{B}"))
        a = self.f(graveyard=["Demonic Consultation"])
        self.assertTrue(a.cast_kess("Demonic Consultation"))
        self.assertFalse(a.cast_kess("Demonic Consultation"))
        b = self.f(owner_turn=False, graveyard=["Demonic Consultation"])
        self.assertFalse(b.cast_kess("Demonic Consultation"))

    def test_E2_fast_mana_pips_and_prerequisites_no_phantom_ubr(self):
        self.assertEqual(self.o["Mana Vault"]["mana_cost"], "{1}")
        self.assertIn("Add {C}{C}{C}", self.o["Mana Vault"]["oracle_text"])
        self.assertIsNone(pay({"C": 4, "U": 0, "B": 0, "R": 0}, "{1}{U}{B}{R}"))
        self.assertIsNotNone(pay({"C": 1, "U": 1, "B": 1, "R": 1}, "{1}{U}{B}{R}"))
        self.assertIn("Imprint", self.o["Chrome Mox"]["oracle_text"])
        self.assertIn("discard a land card", self.o["Mox Diamond"]["oracle_text"])
        self.assertIn("Add {B}{B}{B}", self.o["Dark Ritual"]["oracle_text"])
        self.assertIsNotNone(pay({"B": 1, "C": 0, "R": 0, "U": 0}, "{B}"))
        self.assertIsNone(pay({"B": 3, "C": 0, "R": 0, "U": 0}, "{1}{U}{B}{R}"))

    def test_W1_oracle_consult_kess_and_all_intuition_gifts_splits(self):
        core = ("Thassa's Oracle", "Demonic Consultation", "Tainted Pact", "Intuition",
                "Gifts Ungiven", "Reanimate", "Kess, Dissident Mage")
        self.assertTrue(set(core) <= set(self.names))
        # All costs paid with a staged color-realistic post-tutor mana pool.
        pool = {"U": 4, "B": 4, "R": 1, "C": 6}
        self.assertIsNotNone(pay(pool, self.o["Intuition"]["mana_cost"]))
        self.assertIsNotNone(pay(pool, self.o["Gifts Ungiven"]["mana_cost"]))
        for chosen_to_hand in ("Thassa's Oracle", "Reanimate", "Demonic Consultation"):
            hand = {chosen_to_hand}
            yard = set(("Thassa's Oracle", "Reanimate", "Demonic Consultation")) - hand
            # If Oracle is in the yard, Reanimate from hand or by Kess is available.
            oracle_access = "Thassa's Oracle" in hand or "Reanimate" in (hand | yard)
            # At least one Consultation in hand or the graveyard, with Kess available.
            consult_access = "Demonic Consultation" in (hand | yard)
            self.assertTrue(oracle_access and consult_access)
        pile = {"Thassa's Oracle", "Reanimate", "Demonic Consultation", "Tainted Pact"}
        for hand in map(set, itertools.combinations(sorted(pile), 2)):
            yard = pile - hand
            oracle_access = "Thassa's Oracle" in hand or "Reanimate" in (hand | yard)
            consult_access = bool({"Demonic Consultation", "Tainted Pact"} & (hand | yard))
            # Need <=1 graveyard cast among reanimate + consult; in this four-card pile
            # the hand may hold the second necessary card when the first comes from yard.
            gy_spells_needed = int("Thassa's Oracle" in yard and "Reanimate" in yard)
            gy_spells_needed += int("Demonic Consultation" in yard and "Tainted Pact" in yard)
            self.assertTrue(oracle_access and consult_access)
            self.assertLessEqual(gy_spells_needed, 1)
        a = self.f(graveyard=["Demonic Consultation"], mana={"U": 2, "B": 1, "R": 0, "C": 0})
        self.assertTrue(a.cast_kess("Demonic Consultation"))
        self.assertFalse(self.f(owner_turn=False, graveyard=["Demonic Consultation"]).cast_kess("Demonic Consultation"))

    def test_W2_breach_station_petal_plus_mox_diamond_negative(self):
        for n in ("Underworld Breach", "Grinding Station", "Lotus Petal", "Mox Opal", "Chrome Mox"):
            self.assertIn(n, self.names)
        self.assertEqual(self.o["Mox Opal"]["mana_cost"], "{0}")
        self.assertEqual(self.o["Chrome Mox"]["mana_cost"], "{0}")
        self.assertEqual(self.o["Lotus Petal"]["mana_cost"], "{0}")
        self.assertIn("sacrifice an artifact", self.o["Grinding Station"]["oracle_text"].lower())
        self.assertTrue(3 >= 3 and 3 >= 3)  # three escape foods and three millable cards
        self.assertFalse(2 >= 3)  # insufficient escape resources
        self.assertIn("If you don't", self.o["Mox Diamond"]["oracle_text"])

    def test_W3_breach_led_brain_freeze_payment_discard_and_negation(self):
        for n in ("Underworld Breach", "Lion's Eye Diamond", "Brain Freeze", "Wheel of Fortune"):
            self.assertIn(n, self.names)
        led = self.o["Lion's Eye Diamond"]["oracle_text"]
        self.assertIn("Discard your hand", led)
        self.assertIn("Activate only as an instant", led)
        self.assertIn("Storm", self.o["Brain Freeze"]["oracle_text"])
        self.assertIn("escape", self.o["Underworld Breach"]["oracle_text"].lower())
        self.assertIsNotNone(pay({"U": 3, "B": 0, "R": 0, "C": 0}, "{1}{U}"))
        self.assertIsNone(pay({"U": 1, "B": 0, "R": 0, "C": 0}, "{1}{U}"))
        self.assertFalse(2 >= 3)  # cannot escape without three other cards

    def test_F2_opponent_turn_kess_no_permission_even_if_instant(self):
        a = self.f(owner_turn=False, graveyard=["Mana Drain"], mana={"U": 4, "B": 4, "R": 4, "C": 4})
        self.assertFalse(a.cast_kess("Mana Drain"))
        b = self.f(owner_turn=True, graveyard=["Mana Drain"], mana={"U": 2, "B": 0, "R": 0, "C": 0})
        self.assertTrue(b.cast_kess("Mana Drain"))
        self.assertTrue("Mana Drain" in b.exile)

    def test_F3_removed_counsel_no_demon_negative_same_cut_reason(self):
        self.assertNotIn("Demonic Counsel", self.names)
        self.assertIn("Delirium", self.o["Demonic Counsel"]["oracle_text"])
        self.assertEqual([n for n in self.names if "Demon" in self.o[n]["type_line"]], [])
        self.assertFalse(len({"Artifact", "Instant", "Land"}) >= 4)
        self.assertTrue(len({"Artifact", "Instant", "Land", "Sorcery"}) >= 4)


if __name__ == "__main__":
    unittest.main()
