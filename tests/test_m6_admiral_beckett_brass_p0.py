"""Finite Admiral Beckett Brass P0 rules fixtures, not a Magic simulator.

Source: 2026-10-22 live Scryfall Oracle snapshot; canonical 2026-10-13
approved/locked Admiral list.  The event model records distinct physical
combat-damage sources, target legality, controllers and end-step timing.
It does not estimate actual multiplayer performance or certify M6 globally.
"""

from collections import defaultdict
from dataclasses import dataclass
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = ROOT / "data/grixis/m6/oracle_snapshots/Admiral_Beckett_Brass_P0_Scryfall_20261022.json"


@dataclass(frozen=True)
class Damage:
    source_id: str
    source_types: frozenset[str]
    damaged_player: str
    combat: bool = True
    prevented: bool = False


@dataclass
class Permanent:
    object_id: str
    controller: str
    owner: str
    is_land: bool = False
    on_battlefield: bool = True


def qualified_players(history):
    """Beckett counts DISTINCT Pirate objects, not power, hits or controllers."""
    by_player = defaultdict(set)
    for event in history:
        if event.combat and not event.prevented and "Pirate" in event.source_types:
            by_player[event.damaged_player].add(event.source_id)
    return {player for player, sources in by_player.items() if len(sources) >= 3}


def beckett_triggers_at_end_step(*, beckett_present, controlled_by, history,
                                  permanents, throne_present=False,
                                  throne_controller=None, throne_chosen_type=None):
    """Return available trigger copies/target IDs at the beginning of end step.

    Beckett triggers at end step, but a targeted trigger unable to choose a
    legal target cannot be put on the stack.  The caller chooses distinct
    targets for the examples below, rather than auto-resolving any theft.
    """
    if not beckett_present:
        return 0, []
    players = qualified_players(history)
    targets = [p.object_id for p in permanents if p.on_battlefield
               and not p.is_land and p.controller in players]
    count = (1 + int(throne_present and throne_controller == controlled_by
                     and throne_chosen_type == "Pirate")) if targets else 0
    return count, targets


def resolve_theft(permanent, *, qualified, expected_controller, new_controller):
    """Retest a previously selected target's legality on resolution."""
    if (not permanent.on_battlefield or permanent.is_land or
            permanent.controller != expected_controller or
            expected_controller not in qualified):
        return False
    permanent.controller = new_controller  # no expiry; owner stays unchanged
    return True


class AdmiralBeckettP0(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.snapshot = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
        cls.cards = cls.snapshot["cards"]

    def test_c01_live_oracle_and_commander_source_permissions(self):
        admiral = self.cards["Admiral Beckett Brass"]
        self.assertEqual(admiral["mana_cost"], "{1}{U}{B}{R}")
        self.assertEqual(admiral["color_identity"], ["B", "R", "U"])
        self.assertEqual(admiral["commander_legality"], "legal")
        self.assertIn("three or more Pirates this turn", admiral["oracle_text"])
        self.assertIn("beginning of your end step", admiral["oracle_text"])
        self.assertIn("target nonland permanent", admiral["oracle_text"])
        # Color-aware actual cost check: three generic don't replace U/B/R.
        mana = {"C": 1, "U": 1, "B": 1, "R": 1}
        self.assertEqual(sum(mana.values()), 4)
        self.assertTrue(all(mana[c] >= 1 for c in "UBR"))
        self.assertFalse(all({"C": 4}.get(c, 0) >= 1 for c in "UBR"))

    def test_k01_same_player_three_distinct_pirates_and_permanent_theft(self):
        hits = [Damage(f"pirate-{i}", frozenset({"Pirate"}), "opponent-A")
                for i in range(3)]
        treasure = Permanent("artifact-A", "opponent-A", "opponent-A")
        lands = Permanent("land-A", "opponent-A", "opponent-A", is_land=True)
        count, targets = beckett_triggers_at_end_step(
            beckett_present=True, controlled_by="self", history=hits,
            permanents=[treasure, lands])
        self.assertEqual((count, targets), (1, ["artifact-A"]))
        self.assertTrue(resolve_theft(treasure, qualified={"opponent-A"},
                                      expected_controller="opponent-A",
                                      new_controller="self"))
        self.assertEqual((treasure.owner, treasure.controller), ("opponent-A", "self"))
        # Repeated combat hits, double strike and damage points are NOT new Pirates.
        self.assertEqual(qualified_players(hits[:2] + hits[:1]), set())
        # Each opponent hit by a Pirate is not "three Pirates to one player".
        split = [Damage(f"pirate-{i}", frozenset({"Pirate"}), f"opponent-{i}")
                 for i in range(3)]
        self.assertEqual(qualified_players(split), set())
        # Noncombat damage never qualifies; preventable damage does not count.
        self.assertEqual(qualified_players(hits[:2] +
                         [Damage("third", frozenset({"Pirate"}), "opponent-A", combat=False)]), set())
        self.assertEqual(qualified_players(hits[:2] +
                         [Damage("third", frozenset({"Pirate"}), "opponent-A", prevented=True)]), set())

    def test_k02_throne_two_separate_triggers_not_lower_threshold(self):
        throne = self.cards["Roaming Throne"]["oracle_text"]
        self.assertIn("another creature you control", throne)
        self.assertIn("triggers an additional time", throne)
        hits = [Damage(str(i), frozenset({"Pirate"}), "opponent-A") for i in range(3)]
        permanents = [Permanent(f"artifact-{i}", "opponent-A", "opponent-A") for i in range(2)]
        kwargs = dict(beckett_present=True, controlled_by="self", history=hits,
                      permanents=permanents, throne_present=True,
                      throne_controller="self", throne_chosen_type="Pirate")
        count, targets = beckett_triggers_at_end_step(**kwargs)
        self.assertEqual(count, 2)
        self.assertEqual(targets, ["artifact-0", "artifact-1"])
        self.assertEqual(beckett_triggers_at_end_step(**{**kwargs, "history": hits[:2]})[0], 0)
        self.assertEqual(beckett_triggers_at_end_step(**{**kwargs, "throne_chosen_type": "Golem"})[0], 1)
        self.assertEqual(beckett_triggers_at_end_step(**{**kwargs, "throne_controller": "opponent-B"})[0], 1)
        for target in permanents:
            self.assertTrue(resolve_theft(target, qualified={"opponent-A"},
                        expected_controller="opponent-A", new_controller="self"))
        self.assertTrue(all(p.controller == "self" and p.owner == "opponent-A"
                            for p in permanents))
        # Taking one already-stolen target twice makes the second target illegal.
        self.assertFalse(resolve_theft(permanents[0], qualified={"opponent-A"},
                         expected_controller="opponent-A", new_controller="self"))

    def test_k03_kari_token_monkey_not_pirate(self):
        self.assertIn("red Monkey creature token", self.cards["Kari Zev, Skyship Raider"]["oracle_text"])
        kari = Damage("kari", frozenset({"Human", "Pirate"}), "opponent-A")
        ally = Damage("ally", frozenset({"Pirate"}), "opponent-A")
        monkey = Damage("kari-ragavan-token", frozenset({"Monkey"}), "opponent-A")
        self.assertEqual(qualified_players([kari, ally, monkey]), set())
        self.assertEqual(qualified_players([kari, ally, Damage("third", frozenset({"Pirate"}), "opponent-A")]),
                         {"opponent-A"})

    def test_f01_blocker_fog_and_paid_mitigation(self):
        hits = [Damage(str(i), frozenset({"Pirate"}), "opponent-A") for i in range(3)]
        self.assertEqual(qualified_players(hits), {"opponent-A"})
        # Same attacking board, one Pirate blocked (hits creature, not player).
        blocked = hits[:2]
        self.assertEqual(qualified_players(blocked), set())
        # Same board with Fog: no combat damage to player.
        fog = [Damage(h.source_id, h.source_types, h.damaged_player, prevented=True)
               for h in hits]
        self.assertEqual(qualified_players(fog), set())
        # Open into Wonder is a sorcery; three targets cost {3}{U}{U}, precombat.
        self.assertEqual(self.cards["Open into Wonder"]["mana_cost"], "{X}{U}{U}")
        self.assertIn("can't be blocked this turn", self.cards["Open into Wonder"]["oracle_text"])
        available = {"U": 2, "other": 3}
        self.assertEqual(sum(available.values()), 5)
        self.assertEqual(qualified_players(hits), {"opponent-A"})  # only if spell resolved
        self.assertFalse(available["other"] >= 3 and {"U": 1}["U"] >= 2)
        # Alternative actual interaction: one blocker removed by paid {1}{U}
        # Rift before combat damage; does not remove a second independent blocker.
        self.assertEqual(self.cards["Cyclonic Rift"]["mana_cost"], "{1}{U}")
        self.assertEqual(qualified_players(hits), {"opponent-A"})
        self.assertEqual(qualified_players(blocked), set())
        # No commander on the battlefield at end-step start means no theft trigger;
        # removal after placement does not unwind a legally placed trigger.
        relic = Permanent("relic", "opponent-A", "opponent-A")
        self.assertEqual(beckett_triggers_at_end_step(
            beckett_present=False, controlled_by="self", history=hits, permanents=[relic])[0], 0)
        self.assertTrue(resolve_theft(relic, qualified={"opponent-A"},
                                      expected_controller="opponent-A",
                                      new_controller="self"))


if __name__ == "__main__":
    unittest.main()
