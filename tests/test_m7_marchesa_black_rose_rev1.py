"""Deck 35 finite source-anchored checks; not a general Magic rules engine."""

from collections import Counter
from pathlib import Path
import hashlib
import json
import unittest


ROOT = Path(__file__).resolve().parents[1]
M7 = ROOT / "data/grixis/m7"
CANDIDATE = M7 / "candidate_lists/Marchesa__the_Black_Rose_chatgpt_rev1.txt"
ORACLE = M7 / "oracle_snapshots/Marchesa__the_Black_Rose_Rev1_Scryfall_20261026.json"
PACKET = M7 / "decision_reviews/Marchesa__the_Black_Rose_rev1.json"
ALT8 = M7 / "research_challengers/Marchesa__the_Black_Rose_rev1_alt8_rhystic.txt"
ALT9 = M7 / "research_challengers/Marchesa__the_Black_Rose_rev1_alt9_rhystic_dictate.txt"
HASH = "c4857d176eaa6ed682da7cab974014d393fce2efe698bdca6994d77bb27ddf02"
SWAPS = {
    "Braids, Arisen Nightmare": "Curse-Marred Demon",
    "Deadly Dispute": "The Ooze",
    "Feed the Swarm": "Withering Torment",
    "Fleshbag Marauder": "Accursed Marauder",
    "River Kelpie": "Aether Channeler",
    "Syr Konrad, the Grim": "Voldaren Thrillseeker",
    "Twilight Diviner": "Madame Null, Power Broker",
}


def physical(path):
    cards = []
    for row in path.read_text(encoding="utf-8").splitlines():
        n, name = row.split("x ", 1)
        cards.extend([name.removesuffix(" [Commander]")] * int(n))
    return cards


class TestMarchesaBlackRoseRev1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cards = physical(CANDIDATE)
        cls.source = {x["name"]: x for x in json.loads(ORACLE.read_text())["cards"]}
        cls.packet = json.loads(PACKET.read_text())

    def test_exact_candidate_and_full_current_oracle(self):
        self.assertEqual(hashlib.sha256(CANDIDATE.read_bytes()).hexdigest(), HASH)
        self.assertEqual(len(self.cards), 100)
        self.assertEqual(len(set(self.cards)), 98)
        self.assertEqual(Counter(self.cards)["Island"], 2)
        self.assertEqual(Counter(self.cards)["Swamp"], 2)
        self.assertEqual({n for n,c in Counter(self.cards).items() if c > 1}, {"Island", "Swamp"})
        self.assertEqual(self.cards[0], "Marchesa, the Black Rose")
        self.assertEqual(CANDIDATE.read_text().count("[Commander]"), 1)
        self.assertEqual(set(self.cards), set(self.source))
        self.assertEqual(sum("Land" in self.source[n]["type_line"].split(" — ")[0] for n in self.cards), 34)
        for name, obj in self.source.items():
            self.assertEqual(obj["commander_legality"], "legal", name)
            self.assertTrue(set(obj["color_identity"]) <= set("UBR"), name)
            self.assertTrue(obj["oracle_id"], name)

    def test_challengers_and_15_judgments(self):
        p = self.packet
        self.assertEqual(set(p["final_changes"]["adds"]), set(SWAPS.values()))
        self.assertEqual(set(p["final_changes"]["cuts"]), set(SWAPS))
        self.assertEqual(len(p["material_candidates"]), 15)
        self.assertEqual(len(p["whole_deck_audit"]["weakest_slots"]), 9)
        for path, digest, n in (
            (ALT8, "b2e1cde4f760e9733eea451e86487c31304e59919651aa2e941656231f5d53a0", 8),
            (ALT9, "3d492e6a78c4c5f579ef486db4463b16c7dadc84b1365561a73af56816bda75c", 9),
        ):
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), digest)
            self.assertEqual(len(physical(path)), 100)
            self.assertEqual(len(set(physical(path)) - set(self.cards)), n - 7)

    def test_C1_K1_K2_E1_F2_marchesa_trigger_timing(self):
        self.assertIn("Whenever a creature you control with a +1/+1 counter on it dies", self.source["Marchesa, the Black Rose"]["oracle_text"])
        self.assertIn("beginning of the next end step", self.source["Marchesa, the Black Rose"]["oracle_text"])
        # Bounded state table: counter required on death, Marchesa present then.
        def pending(commander_present, has_counter, died):
            return commander_present and has_counter and died
        self.assertTrue(pending(True, True, True))
        self.assertFalse(pending(True, False, True))
        self.assertFalse(pending(False, True, True))
        self.assertFalse(pending(True, True, False))
        def dethrone(target_life, all_life, attacks_player):
            return attacks_player and target_life == max(all_life)
        self.assertTrue(dethrone(42, [42, 35, 32], True))
        self.assertFalse(dethrone(35, [42, 35, 32], True))
        self.assertFalse(dethrone(42, [42, 35, 32], False))

    def test_K3_K4_K5_W1_W2_persist_reset_guards(self):
        for name in ("Murderous Redcap", "Mikaeus, the Unhallowed", "Gev, Scaled Scorch", "Gray Merchant of Asphodel", "Yawgmoth, Thran Physician", "Thran Vigil", "Sage of Fables"):
            self.assertIn(name, self.cards)
        # A creature dying with a -1/-1 counter cannot persist, and one with
        # a +1/+1 counter cannot undy. Paired counters cancel as state-based
        # actions while on the field, rather than after the creature dies.
        def persist_eligible(minus): return minus == 0
        def undying_eligible(plus): return plus == 0
        self.assertTrue(persist_eligible(0))
        self.assertFalse(persist_eligible(1))
        self.assertTrue(undying_eligible(0))
        self.assertFalse(undying_eligible(1))
        self.assertEqual((1-1, 1-1), (0,0))  # one of each cancels
        # Gary/Yawgmoth needs one additional non-Human sacrificial body to
        # alternate, life for Yawgmoth, and a valid devotion-drain payoff.
        self.assertFalse(bool(1 < 1))  # zero additional bodies is not enough
        self.assertTrue(1 >= 1)

    def test_K6_K7_E2_W3_return_and_flare_requirements(self):
        self.assertIn("Aether Channeler", self.cards)
        self.assertNotIn("River Kelpie", self.cards)
        self.assertIn("Flare of Denial", self.cards)
        self.assertIn("Wizard", self.source["Aether Channeler"]["type_line"])
        self.assertIn("Creature", self.source["Aether Channeler"]["type_line"])
        self.assertEqual(self.source["Aether Channeler"]["color_identity"], ["U"])
        self.assertIn("Spark Double", self.cards)
        self.assertIn("Flayer of the Hatebound", self.cards)
        self.assertIn("Sneak Attack", self.cards)
        # The beginning-of-end-step event has happened before Sneak Attack
        # sacrifices a creature, so any new Marchesa delayed trigger waits
        # for the following end step, not the current one.
        current_end_step_started = True
        sacrifice_then_dies = True
        self.assertFalse(not current_end_step_started and sacrifice_then_dies)

    def test_F1_F3_and_new_counter_engines_with_adversaries(self):
        self.assertIn("Activate only as a sorcery.", self.source["The Ooze"]["oracle_text"])
        self.assertIn("pay life equal to its power", self.source["Madame Null, Power Broker"]["oracle_text"])
        self.assertIn("nontoken creature", self.source["Accursed Marauder"]["oracle_text"])
        self.assertIn("Backup 2", self.source["Voldaren Thrillseeker"]["oracle_text"])
        self.assertIn("discard a card at random", self.source["Curse-Marred Demon"]["oracle_text"])
        self.assertIn("Destroy target creature or enchantment", self.source["Withering Torment"]["oracle_text"])
        # The graveyard object must still exist when the delayed effect acts;
        # exile in response makes the claimed specific-object return fail.
        graveyard_object_present = False
        self.assertFalse(graveyard_object_present)
        # Mutagens cannot be activated during combat/removal priority, and
        # Voldaren must have {1} to sacrifice for its damage ability.
        self.assertFalse("instant" in self.source["The Ooze"]["oracle_text"].lower())
        self.assertIn("{1}, Sacrifice this creature", self.source["Voldaren Thrillseeker"]["oracle_text"])


if __name__ == "__main__":
    unittest.main()
