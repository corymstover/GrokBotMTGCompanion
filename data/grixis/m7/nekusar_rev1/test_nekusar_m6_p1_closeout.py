"""Bounded positive/adversarial Nekusar P1 state traces for exact M7 Rev1.

Pair with PR #721/#722 live Oracle verification. These small effect-specific
models are NOT a Comprehensive Rules engine, opponent playtest, or formal M6 I/J
seal. K5 and W1 are obsolete in the approved 100: never report them as PASSED.
"""

import unittest
from dataclasses import dataclass
from test_nekusar_m7_rev1 import CANDIDATE, CAND_SHA, parse, sha256


@dataclass(frozen=True)
class DrawResolution:
    damage_events: int
    nekusar_damage: int
    ghyrson_damage: int
    curiosity_draws: int


def resolve_opponent_draws(draws, *, nekusar=True, krang=False,
                           ghyrson=False, curiosity_on_nekusar=False):
    """Resolve only Nekusar's draw triggers and damage consequences."""
    if draws < 0:
        raise ValueError("draw count cannot be negative")
    hits = draws * (1 + int(krang)) if nekusar else 0
    return DrawResolution(hits, hits, 2 * hits if ghyrson else 0,
                          hits if curiosity_on_nekusar else 0)


def resolve_wheel(hand_cards, *, discard, metalcraft_artifacts=0, molten=False,
                  prior_draws=0):
    """Per-opponent wheel scenario: discard differs from shuffle."""
    discarded = hand_cards if discard else 0
    return {"discard_events": discarded, "draw_events": hand_cards,
            "caress_loss": discarded * 2, "waste_not_triggers": discarded,
            "molten_damage": prior_draws + hand_cards if molten and metalcraft_artifacts >= 3 else 0}


def resolve_multiplayer_wheel_draws(players, *, each_draws=7,
                                   narset_controller=None, notion_thief_controller=None):
    """Model owner-relative Narset restriction or Thief redirection for a wheel.

    Assume nobody drew earlier this turn and the wheel resolves outside any
    player's draw step. Do not combine two replacement/static effects here.
    """
    if narset_controller and notion_thief_controller:
        raise ValueError("combined effect ordering is outside this fixture")
    draws = {p: 0 for p in players}
    for p in players:
        events = each_draws
        if narset_controller and p != narset_controller:
            events = min(events, 1)  # Narset does NOT restrict its controller
        if notion_thief_controller and p != notion_thief_controller:
            draws[notion_thief_controller] += events
        else:
            draws[p] += events
    return draws


def can_escape_wheel_and_will(*, other_graveyard_cards, initial_mana,
                              opponent_hand_size):
    """Bounded two-spell gate; intentionally NOT an infinite-loop solver."""
    return (other_graveyard_cards >= 6 and initial_mana >= 3
            and initial_mana - 3 + opponent_hand_size >= 3)


def niv_curiosity_damage_chain(*, first_niv_hit_to_opponent, choose_draw,
                               library_size, opponent_life):
    """Count finite Niv->Curiosity->draw->Niv iterations, ignoring responses."""
    if not first_niv_hit_to_opponent or not choose_draw:
        return 0
    draws = 0
    life = opponent_life - 1  # seed damage already happened
    while library_size > 0 and life > 0:
        draws += 1
        library_size -= 1
        life -= 1
    return draws


class NekusarP1Closeout(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cards, _ = parse(CANDIDATE)
        assert sha256(CANDIDATE.read_bytes()).hexdigest() == CAND_SHA

    def require_current(self, *names):
        for name in names:
            self.assertEqual(self.cards[name], 1, name)

    def test_K4_curiosity_on_nekusar_draws_but_is_not_self_infinite(self):
        self.require_current("Nekusar, the Mindrazer", "Curiosity")
        active = resolve_opponent_draws(5, curiosity_on_nekusar=True)
        self.assertEqual((active.nekusar_damage, active.curiosity_draws), (5, 5))
        self.assertEqual(resolve_opponent_draws(5).curiosity_draws, 0)
        self.assertEqual(resolve_opponent_draws(0, curiosity_on_nekusar=True).curiosity_draws, 0)
        # Owner draws from Curiosity do not qualify as opponent draws.

    def test_K5_old_krang_self_damage_fixture_removed_in_current_100(self):
        self.require_current("Krang, the All-Powerful")
        for removed in ("Spiteful Visions", "Phyrexian Tyranny"):
            self.assertEqual(self.cards[removed], 0)
        # DISPOSITION_NEEDED, not a passed current mechanic.

    def test_K6_discard_versus_shuffle_and_molten_metalcraft(self):
        self.require_current("Wheel of Fortune", "Winds of Change", "Waste Not",
                             "Liliana's Caress", "Molten Psyche")
        wheel = resolve_wheel(7, discard=True)
        winds = resolve_wheel(7, discard=False)
        self.assertEqual((wheel["caress_loss"], wheel["waste_not_triggers"]), (14, 7))
        self.assertEqual((winds["caress_loss"], winds["waste_not_triggers"]), (0, 0))
        self.assertEqual(resolve_wheel(7, discard=False, molten=True,
                                       metalcraft_artifacts=3, prior_draws=1)["molten_damage"], 8)
        self.assertEqual(resolve_wheel(7, discard=False, molten=True,
                                       metalcraft_artifacts=2)["molten_damage"], 0)

    def test_E1_E2_punisher_and_commander_must_preexist_draw(self):
        self.require_current("Nekusar, the Mindrazer", "Wheel of Fortune",
                             "Krang, the All-Powerful", "Ghyrson Starn, Kelermorph")
        live = resolve_opponent_draws(7, krang=True, ghyrson=True)
        self.assertEqual((live.damage_events, live.nekusar_damage, live.ghyrson_damage),
                         (14, 14, 28))
        self.assertEqual(resolve_opponent_draws(7, nekusar=False, krang=True,
                                                ghyrson=True).damage_events, 0)
        self.assertEqual(resolve_opponent_draws(0, krang=True, ghyrson=True).damage_events, 0)

    def test_W1_peer_line_absent_no_lethal_claim_about_current_100(self):
        self.assertEqual(self.cards["Peer into the Abyss"], 0)
        # DISPOSITION_NEEDED; historical finisher no longer available.

    def test_W2_breach_wheel_will_has_fuel_and_mana_limits(self):
        self.require_current("Underworld Breach", "Wheel of Fortune", "Jeska's Will")
        self.assertTrue(can_escape_wheel_and_will(other_graveyard_cards=6,
                                                 initial_mana=3, opponent_hand_size=7))
        self.assertFalse(can_escape_wheel_and_will(other_graveyard_cards=5,
                                                  initial_mana=3, opponent_hand_size=7))
        self.assertFalse(can_escape_wheel_and_will(other_graveyard_cards=6,
                                                  initial_mana=2, opponent_hand_size=7))
        self.assertFalse(can_escape_wheel_and_will(other_graveyard_cards=6,
                                                  initial_mana=3, opponent_hand_size=0))
        # W2 remains deferred for priority, actual loop, draw-out, counterplay.

    def test_W3_niv_curiosity_optional_chain_has_real_stop_conditions(self):
        self.require_current("Niv-Mizzet, Parun", "Curiosity")
        self.assertEqual(niv_curiosity_damage_chain(first_niv_hit_to_opponent=True,
                                                   choose_draw=True, library_size=15,
                                                   opponent_life=6), 5)
        self.assertEqual(niv_curiosity_damage_chain(first_niv_hit_to_opponent=True,
                                                   choose_draw=True, library_size=2,
                                                   opponent_life=6), 2)
        self.assertEqual(niv_curiosity_damage_chain(first_niv_hit_to_opponent=True,
                                                   choose_draw=False, library_size=15,
                                                   opponent_life=6), 0)
        self.assertEqual(niv_curiosity_damage_chain(first_niv_hit_to_opponent=False,
                                                   choose_draw=True, library_size=15,
                                                   opponent_life=6), 0)

    def test_F2_opposing_narset_and_notion_thief_are_owner_relative(self):
        self.require_current("Wheel of Fortune", "Nekusar, the Mindrazer")
        players = ("A_Nekusar", "B_hate", "C_other", "D_other")
        normal = resolve_multiplayer_wheel_draws(players)
        self.assertEqual(normal, dict.fromkeys(players, 7))
        narset = resolve_multiplayer_wheel_draws(players, narset_controller="B_hate")
        self.assertEqual(narset, {"A_Nekusar": 1, "B_hate": 7,
                                  "C_other": 1, "D_other": 1})
        self.assertEqual(sum(v for p, v in narset.items() if p != "A_Nekusar"), 9)
        # An OPPOSING Notion Thief steals our and the other opponents' draws,
        # but its controller B is still a Nekusar opponent and takes 28 pings!
        notion = resolve_multiplayer_wheel_draws(players, notion_thief_controller="B_hate")
        self.assertEqual(notion, {"A_Nekusar": 0, "B_hate": 28,
                                  "C_other": 0, "D_other": 0})
        self.assertEqual(sum(v for p, v in notion.items() if p != "A_Nekusar"), 28)

    def test_F3_lifegain_changes_what_is_lethal(self):
        self.require_current("Nekusar, the Mindrazer")
        wheel_damage = resolve_opponent_draws(7).nekusar_damage
        self.assertEqual(25 - wheel_damage + 10, 28)
        self.assertGreater(25 - wheel_damage + 10, 0)
        self.assertLessEqual(25 - resolve_opponent_draws(26).nekusar_damage, 0)


if __name__ == "__main__":
    unittest.main()
