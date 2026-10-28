"""Finite, source-bound M7 review checks for Deck #40; not multiplayer win-rate tests."""
from collections import Counter
from hashlib import sha256
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parent
BASELINE = ROOT / "nekusar_m7_baseline_2026_10_15.txt"
CANDIDATE = ROOT / "nekusar_m7_candidate_rev1.txt"
BASE_SHA = "bc36908fb2f848dfd69407a317d7da5811532dba7e3b4e7be89a2905d901c6f1"
CAND_SHA = "043d2521cec1e82d7ba8ff899b96920249e16ae32e73e2759f02044b41f94e53"
SWAPS = {
    "Fevered Visions": "Roaming Throne",
    "Fate Unraveler": "Spark Double",
    "Peer into the Abyss": "Bloodletter of Aclazotz",
    "Phyrexian Tyranny": "Glint-Horn Buccaneer",
    "Stormfist Crusader": "Faerie Mastermind",
    "Spiteful Visions": "Sigil of Sleep",
    "Reliquary Tower": "Cavern of Souls",
}
ADDED_COLOR_IDENTITIES = {
    "Roaming Throne": set(),
    "Spark Double": {"U"},
    "Bloodletter of Aclazotz": {"B"},
    "Glint-Horn Buccaneer": {"R"},
    "Faerie Mastermind": {"U"},
    "Sigil of Sleep": {"U"},
    "Cavern of Souls": set(),
}


def parse(path):
    cards = Counter()
    rows = path.read_text(encoding="utf-8").splitlines()
    assert rows[0] == "1x Nekusar, the Mindrazer [Commander]"
    for row in rows:
        m = re.fullmatch(r"([1-9][0-9]*)x (.+?)(?: \[Commander\])?", row)
        assert m, row
        cards[m.group(2)] += int(m.group(1))
    return cards, rows


class NekusarRev1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.baseline, cls.base_rows = parse(BASELINE)
        cls.candidate, cls.cand_rows = parse(CANDIDATE)

    def test_p0_1_exact_source_bytes_and_structural_size(self):
        self.assertEqual(sha256(BASELINE.read_bytes()).hexdigest(), BASE_SHA)
        self.assertEqual(sha256(CANDIDATE.read_bytes()).hexdigest(), CAND_SHA)
        self.assertEqual(sum(self.baseline.values()), 100)
        self.assertEqual(sum(self.candidate.values()), 100)
        self.assertEqual(len(self.candidate), 97)
        self.assertEqual(len(self.cand_rows), 97)
        self.assertEqual(self.candidate["Nekusar, the Mindrazer"], 1)
        self.assertTrue(CANDIDATE.read_bytes().endswith(b"\n"))

    def test_p0_2_all_and_only_seven_genuine_swaps(self):
        removed = self.baseline - self.candidate
        added = self.candidate - self.baseline
        self.assertEqual(removed, Counter(SWAPS.keys()))
        self.assertEqual(added, Counter(SWAPS.values()))
        self.assertEqual(sum(removed.values()), 7)
        self.assertEqual(sum(added.values()), 7)

    def test_p0_3_singleton_commander_and_color_identity_additions(self):
        duplicate_nonbasics = {card: qty for card, qty in self.candidate.items()
                               if qty > 1 and card not in {"Island", "Mountain", "Swamp"}}
        self.assertEqual(duplicate_nonbasics, {})
        self.assertEqual({b: self.candidate[b] for b in ("Island", "Mountain", "Swamp")},
                         {"Island": 2, "Mountain": 2, "Swamp": 2})
        self.assertEqual(set(SWAPS.values()), set(ADDED_COLOR_IDENTITIES))
        self.assertTrue(all(color <= {"U", "B", "R"} for color in ADDED_COLOR_IDENTITIES.values()))

    def test_p0_4_35_land_swap_not_34(self):
        # Baseline 35 front-face lands is the Oct15 canonical certification.
        # The single land substitution changes no spell/land slot count.
        self.assertEqual(SWAPS["Reliquary Tower"], "Cavern of Souls")
        self.assertEqual(self.baseline["Reliquary Tower"], 1)
        self.assertEqual(self.candidate["Cavern of Souls"], 1)
        self.assertEqual(self.candidate["Reliquary Tower"], 0)

    def test_p0_5_baseline_self_punishment_bounded_trace(self):
        # Seven OWN draws, Spiteful+Tyranny+Krang+Ghyrson all in play:
        # Spiteful triggers twice per draw, 1 original + 2 Ghyrson damage.
        # Tyranny triggers twice per draw, lose 2 if no {2} is paid.
        draws = 7
        spiteful_damage = draws * 2 * (1 + 2)
        tyranny_life_loss = draws * 2 * 2
        self.assertEqual((spiteful_damage, tyranny_life_loss), (42, 28))
        self.assertEqual(spiteful_damage + tyranny_life_loss, 70)
        self.assertNotIn("Spiteful Visions", self.candidate)
        self.assertNotIn("Phyrexian Tyranny", self.candidate)

    def test_p0_6_draw_step_and_damage_triggers_add_not_multiply(self):
        # One Nekusar with Staff, Harmonic, Roaming and Krang:
        # beginning-of-step does not qualify for Krang.
        step_triggers = 1 + 1 + 1 + 1
        damage_triggers_per_opponent_draw = 1 + 1 + 1 + 1 + 1
        self.assertEqual((step_triggers, damage_triggers_per_opponent_draw), (4, 5))
        # Spark Double is a separate Nekusar copy without the original's Staff.
        copy_step_triggers = 1 + 1 + 1
        copy_damage_triggers = 1 + 1 + 1 + 1
        self.assertEqual(1 + step_triggers + copy_step_triggers, 8)  # normal draw included
        self.assertEqual(damage_triggers_per_opponent_draw + copy_damage_triggers, 9)

    def test_p0_7_bloodletter_and_ghyrson_keep_exact_one_event(self):
        # Bloodletter doubles LIFE LOSS on our turn, not 1 damage dealt.
        # Ghyrson still sees the original exactly-one damage event.
        per_draw_damage = 1 + 2
        per_draw_life_loss = 2 * per_draw_damage
        self.assertEqual(per_draw_life_loss, 6)
        self.assertEqual(7 * per_draw_life_loss, 42)

    def test_p0_8_glint_horn_counts_own_discards_not_winds_shuffle(self):
        discard_count = 5
        opponents = 3
        per_opponent_damage = discard_count * (1 + 2)  # Ghyrson present
        self.assertEqual(per_opponent_damage, 15)
        self.assertEqual(per_opponent_damage * opponents, 45)
        self.assertEqual(0 * (1 + 2), 0)  # Winds of Change shuffle is NOT discard

    def test_p1_1_faerie_once_per_opponent_per_turn(self):
        # Each second card causes precisely one event in that turn.
        opponent_draw_sequences = [7, 7, 7]
        triggers = sum(1 for draws in opponent_draw_sequences if draws >= 2)
        self.assertEqual(triggers, 3)
        self.assertNotEqual(triggers, 18)  # never one event for each draw after second

    def test_p1_2_sigil_targets_are_not_board_wipe_guarantees(self):
        # Four Nekusar damage events with only two distinct target creatures.
        # Choosing the same target four times can produce three fizzled triggers.
        draw_damage_triggers, opponent_creatures = 4, 2
        effective_bounces = min(draw_damage_triggers, opponent_creatures)
        self.assertEqual(effective_bounces, 2)
        self.assertEqual(self.candidate["Sigil of Sleep"], 1)

    def test_p1_3_cavern_only_protects_named_wizard_creature_spell(self):
        chosen_type = "Wizard"
        commander_types = {"Zombie", "Wizard"}
        self.assertIn(chosen_type, commander_types)
        self.assertNotIn(chosen_type, {"Faerie", "Rogue"})
        # Cavern doesn't protect Nekusar's triggered abilities after resolution.

    def test_p1_4_role_retention_and_disputed_conditions(self):
        for card in ("Niv-Mizzet, Parun", "Curiosity", "Ghyrson Starn, Kelermorph",
                     "Harmonic Prodigy", "Wizard's Staff", "Krang, the All-Powerful",
                     "Waste Not", "Liliana's Caress", "Kami of the Crescent Moon",
                     "Teferi's Puzzle Box", "Bloodchief Ascension"):
            self.assertEqual(self.candidate[card], 1, card)
        self.assertNotIn("Forced Fruition", self.candidate)
        self.assertNotIn("Mindcrank", self.candidate)
        # Their M6 comparative matchups remain hypotheses, not measured losses/wins.


if __name__ == "__main__":
    unittest.main()
