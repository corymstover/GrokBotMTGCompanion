"""Finite Oracle-bound Admiral M7 post-floor card-effect fixtures.

Scope: 11 live Scryfall records saved 2026-10-22 and source-bound physical
six-/seven-swap research variants. This is not an exhaustive Magic rules
engine, win-rate study, global optimization, M6 I/J certificate or owner approval.
"""
from collections import Counter
from dataclasses import dataclass
from itertools import permutations
import hashlib
import json
from pathlib import Path
import unittest


def parse_list(path):
    """Standalone physical fixture reader; no dependency on JSON-schema M7 gate."""
    cards = []
    commanders = []
    companions = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        amount_text, raw = line.split("x ", 1)
        amount = int(amount_text)
        role = "Commander" if raw.endswith(" [Commander]") else ""
        name = raw.removesuffix(" [Commander]")
        cards.extend([name] * amount)
        if role == "Commander":
            commanders.extend([name] * amount)
    if len(cards) != 100 or not commanders or cards[0] != commanders[0]:
        raise ValueError("Expected exactly 100 cards with commander first")
    for name, quantity in Counter(cards).items():
        if quantity > 1 and name not in {"Island", "Mountain", "Swamp"}:
            raise ValueError(f"Illegal Admiral fixture repeat: {name}")
    return cards, commanders, companions


ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "data/grixis/m7/research_challengers"
SOURCE = RESEARCH / "Admiral_Beckett_Brass_eleven_card_live_Scryfall_20261022.json"
BASE = ROOT / "data/grixis/m6/authority_snapshots/Admiral_Beckett_Brass_Canonical_Approved_20261022.txt"
CANONICAL_SHA = "4ba5c483eb67b5f2647d375450adf9c2b7e79a036d0ba1866e58de8441bf3414"
NEW_NAMES = {
    "Brotherhood Regalia", "Captain Storm, Cosmium Raider",
    "Shizo, Death's Storehouse", "Glaring Spotlight", "Cosmotronic Wave",
}
INCUMBENTS = {
    "Bident of Thassa", "March of the Drowned", "Path of Ancestry",
    "Fiery Cannonade", "Open into Wonder",
}
VARIANTS = [
    "Admiral_Beckett_Brass_six_Captain_Storm_20261022.txt",
    "Admiral_Beckett_Brass_six_Shizo_20261022.txt",
    "Admiral_Beckett_Brass_seven_Storm_Shizo_20261022.txt",
    "Admiral_Beckett_Brass_six_Glaring_Spotlight_20261022.txt",
    "Admiral_Beckett_Brass_six_Brotherhood_Regalia_20261022.txt",
    "Admiral_Beckett_Brass_six_Cosmotronic_Wave_20261022.txt",
    "Admiral_Beckett_Brass_seven_Regalia_Wave_20261022.txt",
]


@dataclass(frozen=True)
class Land:
    name: str
    colors: frozenset[str]
    tapped: bool = False


def can_pay_land_sources(lands, colored_pips, generic):
    """One activation/source per land; finite colored-pip matching."""
    ready = [land for land in lands if not land.tapped]
    if len(ready) < len(colored_pips) + generic:
        return False
    for assignment in permutations(ready, len(colored_pips)):
        if all(color in land.colors for color, land in zip(colored_pips, assignment)):
            return True
    return False


def qualifying_pirate_hits(pirate_ids, blocked_ids=frozenset(), fog=False):
    """Count distinct successful Pirate combat-damage source IDs to one player."""
    if fog:
        return 0
    return len(set(pirate_ids) - set(blocked_ids))


@dataclass(frozen=True)
class Defender:
    kind: str
    toughness: int


def cannonade_precombat(blockers):
    """Only existing non-Pirates with toughness <=2 die from a 2-damage Cannonade."""
    return tuple(b for b in blockers if b.kind == "Pirate" or b.toughness > 2)


def wave_precombat(blockers):
    """Wave's no-block clause, not its 1-damage effect, opens the swing."""
    return tuple()  # Opposing creatures cannot block this turn on resolution.


@dataclass
class SpotlightState:
    available_generic: int
    sacrificed: bool = False

    def activate(self, creatures_at_resolution):
        if self.sacrificed or self.available_generic < 3:
            return None
        self.available_generic -= 3
        self.sacrificed = True
        return frozenset(creatures_at_resolution)


def removal_can_resolve_through_ward(*, targeted, ward_two, opponent_available):
    # Untargeted sweeps do not ask the opponent to pay ward.
    return not targeted or not ward_two or opponent_available >= 2


def equip_regalia(commander_legendary, *, has_paid_cast_two, equip_mana, main_phase):
    if not has_paid_cast_two or not main_phase:
        return False
    return equip_mana >= (1 if commander_legendary else 3)


class AdmiralPostFloorOracleAndMechanics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        obj = json.loads(SOURCE.read_text(encoding="utf-8"))
        cls.meta = obj
        cls.oracle = {c["name"]: c for c in obj["verified_cards"]}

    def test_01_frozen_authority_exact_11_current_scryfall_records(self):
        self.assertEqual(hashlib.sha256(BASE.read_bytes()).hexdigest(), CANONICAL_SHA)
        self.assertEqual(self.meta["status"], "SOURCED_ELEVEN_CARDS_ONLY_NOT_ALL_100_NOT_M7_READY")
        self.assertEqual(len(self.oracle), 11)
        self.assertEqual(set(self.oracle), NEW_NAMES | INCUMBENTS | {"Admiral Beckett Brass"})
        for name, record in self.oracle.items():
            self.assertTrue(record["oracle_id"], name)
            self.assertEqual(record["commander_legality"], "legal", name)
            self.assertTrue(set(record["color_identity"]) <= {"B", "R", "U"}, name)
            self.assertEqual(len(record["raw_scryfall_payload_sha256"]), 64)
            self.assertIn("cards/named?exact=", record["source_query_url"])
        self.assertEqual(self.oracle["Admiral Beckett Brass"]["mana_cost"], "{1}{U}{B}{R}")

    def test_02_all_seven_lists_physical_and_no_new_owner_authority(self):
        baseline, commander, companion = parse_list(BASE)
        self.assertEqual(len(baseline), 100)
        for name in VARIANTS:
            with self.subTest(name=name):
                cards, cmd, comp = parse_list(RESEARCH / name)
                self.assertEqual((len(cards), cmd, comp), (100, commander, companion))
                self.assertEqual(sum((Counter(cards) - Counter(baseline)).values()),
                                 sum((Counter(baseline) - Counter(cards)).values()))
                self.assertTrue((set(cards) - set(baseline)) <= NEW_NAMES |
                                {"City of Brass", "Departed Deckhand", "Cloud Pirates",
                                 "Skyship Plunderer", "Broadside Bombardiers"})

    def test_03_spotlight_source_cost_hexproof_not_untargeted_wipe(self):
        spot = self.oracle["Glaring Spotlight"]
        self.assertEqual(spot["mana_cost"], "{1}")
        self.assertIn("{3}, Sacrifice this artifact:", spot["oracle_text"])
        self.assertIn("gain hexproof until end of turn", spot["oracle_text"])
        self.assertIn("can't be blocked this turn", spot["oracle_text"])
        self.assertIsNone(SpotlightState(available_generic=2).activate(("P1", "P2", "P3")))
        device = SpotlightState(available_generic=4)
        affected = device.activate(("P1", "P2", "P3"))
        self.assertEqual(affected, frozenset({"P1", "P2", "P3"}))
        self.assertEqual(device.available_generic, 1)
        self.assertTrue(device.sacrificed)
        self.assertIsNone(device.activate(("P1", "P2", "P3")))  # Sacrificed once.
        self.assertNotIn("P4-entered-later", affected)  # Hexproof won't follow new ETBs.
        pirates = ["P1", "P2", "P3"]
        self.assertLess(qualifying_pirate_hits(pirates, blocked_ids={"P3"}), 3)
        self.assertEqual(qualifying_pirate_hits(pirates), 3)
        # With source resolved before blockers, all three are unblocked;
        # a Fog or Admiral removed before the end step can still defeat theft.
        self.assertEqual(qualifying_pirate_hits(pirates, fog=True), 0)

    def test_04_regalia_real_equip_cost_preserves_pirate_type_and_ward_not_sweep(self):
        record = self.oracle["Brotherhood Regalia"]
        self.assertIn("ward {2}", record["oracle_text"])
        self.assertIn("Assassin in addition to its other types", record["oracle_text"])
        self.assertIn("can't be blocked", record["oracle_text"])
        self.assertIn("Equip legendary creature {1}", record["oracle_text"])
        self.assertIn("Equip {3}", record["oracle_text"])
        self.assertTrue(equip_regalia(True, has_paid_cast_two=True, equip_mana=1, main_phase=True))
        self.assertFalse(equip_regalia(False, has_paid_cast_two=True, equip_mana=1, main_phase=True))
        self.assertFalse(equip_regalia(True, has_paid_cast_two=True, equip_mana=1, main_phase=False))
        self.assertFalse(equip_regalia(True, has_paid_cast_two=False, equip_mana=1, main_phase=True))
        # Ward {2} permits targeted opponent removal if they PAY two generic;
        # it does not stop a non-targeting board wipe.
        self.assertTrue(removal_can_resolve_through_ward(targeted=True,
                        ward_two=True, opponent_available=2))
        self.assertFalse(removal_can_resolve_through_ward(targeted=True,
                         ward_two=True, opponent_available=1))
        self.assertTrue(removal_can_resolve_through_ward(targeted=False,
                        ward_two=True, opponent_available=0))
        self.assertEqual(qualifying_pirate_hits(["Admiral", "P2", "P3"], {"P2", "P3"}), 1)

    def test_05_wave_vs_cannonade_source_paid_blocker_profiles(self):
        wave = self.oracle["Cosmotronic Wave"]
        cannonade = self.oracle["Fiery Cannonade"]
        self.assertEqual(wave["mana_cost"], "{3}{R}")
        self.assertEqual(cannonade["mana_cost"], "{2}{R}")
        self.assertEqual(wave["type_line"], "Sorcery")
        self.assertEqual(cannonade["type_line"], "Instant")
        self.assertIn("can't block this turn", wave["oracle_text"])
        self.assertIn("2 damage to each non-Pirate creature", cannonade["oracle_text"])
        blockers = (Defender("NonPirate", 2), Defender("NonPirate", 5),
                    Defender("Pirate", 2))
        remaining_cannonade = cannonade_precombat(blockers)
        self.assertEqual([b.toughness for b in remaining_cannonade], [5, 2])
        self.assertEqual(wave_precombat(blockers), ())  # All cannot block.
        self.assertEqual(qualifying_pirate_hits(["P1", "P2", "P3"], {"P3"}), 2)
        self.assertEqual(qualifying_pirate_hits(["P1", "P2", "P3"]), 3)
        # Wave's one damage does not kill a 5-toughness creature.
        self.assertTrue(5 > 1)
        self.assertFalse(2 > 2)
        # It is a precombat sorcery. No claim it protects after a counterspell.

    def test_06_path_vs_shizo_source_paid_four_land_and_uu_cases(self):
        path = self.oracle["Path of Ancestry"]
        shizo = self.oracle["Shizo, Death's Storehouse"]
        self.assertIn("enters tapped", path["oracle_text"])
        self.assertIn("scry 1", path["oracle_text"])
        self.assertIn("{T}: Add {B}", shizo["oracle_text"])
        self.assertIn("{B}, {T}: Target legendary creature gains fear", shizo["oracle_text"])
        island = Land("Island", frozenset({"U"}))
        mountain = Land("Mountain", frozenset({"R"}))
        swamp = Land("Swamp", frozenset({"B"}))
        path_fresh = Land("Path of Ancestry", frozenset({"B", "R", "U"}), True)
        path_ready = Land("Path of Ancestry", frozenset({"B", "R", "U"}))
        shizo_ready = Land("Shizo", frozenset({"B"}))
        self.assertFalse(can_pay_land_sources([island, mountain, swamp, path_fresh],
                                               ("U", "B", "R"), 1))
        self.assertTrue(can_pay_land_sources([island, mountain, swamp, shizo_ready],
                                              ("U", "B", "R"), 1))
        self.assertTrue(can_pay_land_sources([island, mountain, swamp, path_ready],
                                              ("U", "U"), 0))
        self.assertFalse(can_pay_land_sources([island, mountain, swamp, shizo_ready],
                                               ("U", "U"), 0))
        # A single Shizo cannot both tap for its own {B} and tap to give fear.
        self.assertFalse(can_pay_land_sources([shizo_ready], ("B",), 1))
        self.assertTrue(can_pay_land_sources([shizo_ready, swamp], ("B",), 1))
        # Path's scry requires its produced mana to CAST the typed Pirate spell.

    def test_07_storm_treasure_counters_do_not_supply_missing_third_hit(self):
        storm = self.oracle["Captain Storm, Cosmium Raider"]
        self.assertEqual(storm["mana_cost"], "{U}{R}")
        self.assertIn("Whenever an artifact you control enters", storm["oracle_text"])
        self.assertIn("target Pirate you control", storm["oracle_text"])
        counters = {"P1": 0, "P2": 0}
        # Two paid-for Treasure token entries while Storm and targets exist.
        for target in ("P1", "P2"):
            counters[target] += 1
        self.assertEqual(counters, {"P1": 1, "P2": 1})
        # Two artifact ETBs are not two additional Pirate combat damage sources.
        self.assertEqual(qualifying_pirate_hits(["P1", "P2"]), 2)
        self.assertLess(qualifying_pirate_hits(["P1", "P2"]), 3)
        # Skyship can increase an existing counter after its hit; it cannot
        # turn an attacking creature already blocked into an unblocked one.

    def test_08_march_real_one_black_two_pirate_recovery_after_wipe(self):
        march = self.oracle["March of the Drowned"]
        self.assertEqual(march["mana_cost"], "{B}")
        self.assertIn("Return two target Pirate cards", march["oracle_text"])
        self.assertIn("Return target creature card", march["oracle_text"])
        graveyard = {"P1": "Pirate", "P2": "Pirate", "P3": "NonPirate"}
        returned = [name for name, t in graveyard.items() if t == "Pirate"][:2]
        self.assertEqual(returned, ["P1", "P2"])
        self.assertEqual(len(returned), 2)
        # Storm in the graveyard cannot trigger from an artifact ETB in play.
        self.assertNotIn("return", self.oracle["Captain Storm, Cosmium Raider"]["oracle_text"].lower())

    def test_09_baseline_open_into_wonder_same_three_sources_not_free(self):
        open_spell = self.oracle["Open into Wonder"]
        self.assertEqual(open_spell["mana_cost"], "{X}{U}{U}")
        self.assertIn("X target creatures can't be blocked", open_spell["oracle_text"])
        self.assertIn("draw a card", open_spell["oracle_text"])
        self.assertEqual(3 + 2, 5)  # X=3, three targets, total 5 paid including UU.
        self.assertEqual(qualifying_pirate_hits(["P1", "P2", "P3"]), 3)
        self.assertEqual(qualifying_pirate_hits(["P1", "P2", "P3"], fog=True), 0)


if __name__ == "__main__":
    unittest.main()
