"""ChatGPT cycle 66.5a: adversarial tests for attack_trigger_proxy v2."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from grixis_mech import combat  # noqa: E402


def _trace(rows, turns=6):
    return [(None, [{"turn": t, "battlefield": list(rows.get(t, rows.get("default", []))), "graveyard": [], "hand": []}
                    for t in range(1, turns + 1)])]


def test_attack_parser_distinguishes_supported_scopes():
    assert combat.parse("X", "Whenever X attacks, draw a card.", "Creature — Rat") == ("self", None)
    assert combat.parse("X", "Whenever you attack, draw a card.", "Enchantment") == ("you_attack", None)
    assert combat.parse("X", "Whenever one or more creatures you control attack, draw a card.", "Artifact") == ("you_attack", None)
    assert combat.parse("X", "Whenever a creature you control attacks, scry 1.", "Enchantment") == ("creature_attacks", None)
    assert combat.parse("X", "Whenever another creature you control attacks, scry 1.", "Creature") == ("another_attacks", None)


def test_attack_parser_refuses_false_or_unsupported_semantics():
    # An attack requirement is not a triggered ability.
    assert combat.parse("X", "X attacks each combat if able.", "Creature") == (None, None)
    cases = (
        ("Whenever X attacks, if you control a Dragon, draw a card.", "intervening-if"),
        ("Whenever X attacks alone, draw two cards.", "conditional"),
        ("Whenever X attacks and isn't blocked, draw a card.", "conditional"),
        ("Whenever X attacks or blocks, scry 1.", "combined"),
        ("Whenever an opponent attacks, draw a card.", "opponent"),
        ("Whenever X attacks a player, draw a card.", "defender-specific"),
        ("Whenever a Pirate you control attacks, create a Treasure token.", "attack-trigger"),
    )
    for text, fragment in cases:
        sem, why = combat.parse("X", text, "Creature — Rat")
        assert sem is None and why and fragment in why, (text, sem, why)


def test_self_attack_summoning_sickness_haste_and_reentry():
    cards = {"Z": {"text": "Whenever Z attacks, draw a card.", "type_line": "Creature — Rat"}}
    games = _trace({1: [], 2: [], 3: ["Z"], 4: ["Z"], 5: [], 6: ["Z"]})
    # T3 arrival cannot attack; T4 can; T6 is a fresh re-entry and is summoning-sick again.
    assert combat.triggers(games, "Z", "self", 6, 1.0, 1.0, cards) == 1.0
    cards["Z"]["text"] = "Haste\nWhenever Z attacks, draw a card."
    # Haste permits both arrival/re-entry attacks: T3, T4, T6.
    assert combat.triggers(games, "Z", "self", 6, 1.0, 1.0, cards) == 3.0


def test_blockers_do_not_suppress_attack_triggers():
    # v2 deliberately has no blocker parameter: an attack trigger happens during declare attackers, before blockers.
    assert "block" not in combat.SPEC["parameters"]
    assert combat.SPEC["parameters"]["attack_rate"][0] == 1.0
    assert any("blockers" in x.lower() for x in combat.SPEC["does_not_model"])


def test_you_attack_counts_one_event_not_number_of_attackers():
    cards = {
        "E": {"text": "Whenever you attack, draw a card.", "type_line": "Enchantment"},
        "A": {"text": "", "type_line": "Creature"},
        "B": {"text": "", "type_line": "Creature"},
    }
    games = _trace({1: [], 2: ["E", "A", "B"], "default": ["E", "A", "B"]})
    # A and B become eligible on T3. Full declaration rate => one watcher trigger on each of T3-T6.
    assert combat.triggers(games, "E", "you_attack", 6, 1.0, 1.0, cards) == 4.0
    # At 50% independent declaration rate with two eligible attackers: P(any attacks)=.75 per combat.
    assert combat.triggers(games, "E", "you_attack", 6, 0.5, 1.0, cards) == 3.0


def test_per_attacker_and_another_semantics_are_distinct():
    cards = {
        "W": {"text": "Whenever a creature you control attacks, scry 1.", "type_line": "Creature"},
        "A": {"text": "", "type_line": "Creature"},
    }
    games = _trace({1: [], 2: ["W", "A"], "default": ["W", "A"]})
    # T3-T6: W and A each attack = 2 triggers per combat for 'a creature'.
    assert combat.triggers(games, "W", "creature_attacks", 6, 1.0, 1.0, cards) == 8.0
    # 'another creature' excludes W's own attacks.
    assert combat.triggers(games, "W", "another_attacks", 6, 1.0, 1.0, cards) == 4.0


def test_creature_watcher_survival_not_double_counted_on_own_attack():
    cards = {
        "W": {"text": "Whenever a creature you control attacks, scry 1.", "type_line": "Creature"},
        "A": {"text": "", "type_line": "Creature"},
    }
    games = _trace({1: [], 2: ["W", "A"], 3: ["W", "A"]}, turns=3)
    # On T3 with survive=.5: own attack contributes .5, A contributes .5*.5=.25. Total .75.
    assert combat.triggers(games, "W", "creature_attacks", 3, 1.0, 0.5, cards) == 0.75


def test_noncreature_you_attack_watcher_is_supported():
    cards = {
        "E": {"text": "Whenever one or more creatures you control attack, draw a card.", "type_line": "Enchantment"},
        "A": {"text": "", "type_line": "Creature"},
    }
    games = _trace({1: ["E", "A"], "default": ["E", "A"]}, turns=3)
    assert combat.matches("E", cards["E"]["text"], cards["E"]["type_line"])
    assert combat.triggers(games, "E", "you_attack", 3, 1.0, 1.0, cards) == 2.0
