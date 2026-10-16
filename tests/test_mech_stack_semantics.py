"""ChatGPT cycle 66.6: semantic tests for counterspell/protection readiness modules."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from grixis_mech import stack  # noqa: E402


def _games(rows):
    return [(None, rows)]


def test_counter_parser_supported_scopes_and_commander_free_text():
    r, why = stack.counter_parse("Counterspell", "Counter target spell.", "Instant")
    assert why is None and r["mode"] == "spell" and r["scope"] == ("spell",)

    r, why = stack.counter_parse("Negate", "Counter target noncreature spell.", "Instant")
    assert why is None and r["scope"] == ("noncreature_spell",)

    r, why = stack.counter_parse("Stifle", "Counter target activated or triggered ability.", "Instant")
    assert why is None and set(r["scope"]) == {"activated_ability", "triggered_ability"}

    text = "If you control a commander, you may cast Fierce Guardianship without paying its mana cost.\nCounter target noncreature spell."
    r, why = stack.counter_parse("Fierce Guardianship", text, "Instant")
    assert why is None and r["free_with_commander"]


def test_counter_parser_refuses_soft_and_qualified_counters():
    cases = (
        ("Counter target spell unless its controller pays {2}.", "soft counter"),
        ("Counter target spell with mana value 2 or less.", "qualified"),
        ("Whenever X enters, counter target spell.", "not a supported activated"),
    )
    for text, frag in cases:
        r, why = stack.counter_parse("X", text, "Enchantment")
        assert r is None and why and frag in why, (text, r, why)


def test_counter_readiness_uses_hand_unspent_mana_and_commander_free_line():
    rows = [
        {"turn": 1, "battlefield": [], "hand": ["C"], "graveyard": [], "mana": 1, "spent": 1},
        {"turn": 2, "battlefield": [], "hand": ["C"], "graveyard": [], "mana": 2, "spent": 0},
        {"turn": 3, "battlefield": [], "hand": ["C"], "graveyard": [], "mana": 3, "spent": 2},
    ]
    ctx = {"cards": {"C": {"text": "Counter target spell.", "type_line": "Instant"}},
           "models": {"C": {"mv": 2}}, "commanders": set()}
    assert stack.counter_ready(_games(rows), "C", ctx, 3) == 1.0  # only T2 leaves >=2 mana

    ctx = {"cards": {"C": {"text": "If you control a commander, you may cast C without paying its mana cost.\nCounter target spell.", "type_line": "Instant"}},
           "models": {"C": {"mv": 3}}, "commanders": {"Cmdr"}}
    rows[2]["battlefield"] = ["Cmdr"]
    assert stack.counter_ready(_games(rows), "C", ctx, 3) == 1.0  # free on T3 despite only 1 unspent


def test_protection_parser_distinguishes_reactive_and_static_modes():
    r, why = stack.protection_parse("Slip", "Target creature you control gains hexproof until end of turn.", "Instant")
    assert why is None and r == {"mode": "spell", "scope": "target"}

    r, why = stack.protection_parse("Banner", "Spells you control can't be countered.", "Enchantment")
    assert why is None and r == {"mode": "static_team", "scope": "team"}

    r, why = stack.protection_parse("Shell", "Indestructible", "Artifact Creature")
    assert why is None and r == {"mode": "static_self", "scope": "self"}

    r, why = stack.protection_parse("Wardling", "Ward {2}", "Creature")
    assert why is None and r["mode"] == "static_self"


def test_protection_parser_refuses_conditional_or_other_unmodelled_wording():
    r, why = stack.protection_parse("X", "When X enters, if you control an artifact, X gains hexproof until end of turn.", "Creature")
    assert r is None and "conditional" in why

    r, why = stack.protection_parse("X", "Creatures your opponents control lose hexproof.", "Enchantment")
    assert r is None and why and "not modelled" in why


def test_protection_readiness_spell_vs_static():
    rows = [
        {"turn": 1, "battlefield": [], "hand": ["P"], "graveyard": [], "mana": 1, "spent": 0},
        {"turn": 2, "battlefield": [], "hand": ["P"], "graveyard": [], "mana": 2, "spent": 2},
        {"turn": 3, "battlefield": [], "hand": ["P"], "graveyard": [], "mana": 3, "spent": 1},
    ]
    ctx = {"cards": {"P": {"text": "Target creature you control gains hexproof until end of turn.", "type_line": "Instant"}},
           "models": {"P": {"mv": 1}}, "commanders": set()}
    assert stack.protection_ready(_games(rows), "P", ctx, 3) == 2.0  # T1 and T3

    rows2 = [
        {"turn": 1, "battlefield": [], "hand": [], "graveyard": [], "mana": 1, "spent": 1},
        {"turn": 2, "battlefield": ["P"], "hand": [], "graveyard": [], "mana": 2, "spent": 2},
        {"turn": 3, "battlefield": ["P"], "hand": [], "graveyard": [], "mana": 3, "spent": 3},
    ]
    ctx = {"cards": {"P": {"text": "Spells you control can't be countered.", "type_line": "Enchantment"}},
           "models": {"P": {"mv": 2}}, "commanders": set()}
    assert stack.protection_ready(_games(rows2), "P", ctx, 3) == 2.0


def test_stack_specs_are_test_results_and_never_claim_win_rates():
    for m in (stack.Counterspells, stack.StackProtection):
        assert m.SPEC["evidence_class"] == "test_result"
        assert any("win rates" in x for x in m.SPEC["does_not_model"])
