"""ChatGPT cycle 66.8: semantic tests for graveyard-setup and repeatable-tutor modules."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from grixis_mech import tutors  # noqa: E402


def _games(rows):
    return [(None, rows)]


def test_graveyard_setup_parses_selected_tutor_mill_and_surveil():
    r, why = tutors.graveyard_parse("Entomb", "Search your library for a card, put that card into your graveyard, then shuffle.", "Instant")
    assert why is None and r["kind"] == "selected_to_graveyard" and r["mode"] == "spell"
    assert r["target"]["kind"] == "any"

    r, why = tutors.graveyard_parse("Millstone", "{2}, {T}: Target player mills two cards.", "Artifact")
    assert why is None and r["kind"] == "mill" and r["mode"] == "activated" and r["amount"] == 2

    r, why = tutors.graveyard_parse("Spy", "When Spy enters, surveil 3.", "Creature")
    assert why is None and r["kind"] == "surveil" and r["mode"] == "etb" and r["amount"] == 3


def test_graveyard_setup_refuses_variable_and_unsupported_trigger_timing():
    cases = (
        ("Whenever Setup attacks, mill two cards.", "Creature", "trigger timing"),
        ("At the beginning of each end step, surveil 2.", "Enchantment", "trigger timing"),
        ("Mill X cards.", "Sorcery", "unsupported"),
        ("Target opponent mills three cards.", "Sorcery", "unsupported"),
    )
    for text, tl, frag in cases:
        r, why = tutors.graveyard_parse("Setup", text, tl)
        assert r is None and why and frag in why, (text, r, why)


def test_surveil_is_capacity_not_guaranteed_graveyard_cards():
    rows = [
        {"turn": 1, "battlefield": [], "graveyard": [], "hand": ["S"]},
        {"turn": 2, "battlefield": ["S"], "graveyard": [], "hand": []},
    ]
    ctx = {"cards": {"S": {"text": "When S enters, surveil 2.", "type_line": "Creature"}},
           "models": {"S": {"types": ["creature"], "land": False}}}
    m = tutors.graveyard_setup_metric(_games(rows), "S", ctx, 2)
    assert m == {"events": 1.0, "cards": 0.0, "surveil_capacity": 2.0}


def test_repeatable_tutor_parses_activated_and_upkeep_modes():
    r, why = tutors.repeatable_parse("Map", "{2}, {T}: Search your library for a card, put that card into your hand, then shuffle.", "Artifact")
    assert why is None and r["mode"] == "activated" and r["cost"] == {"mana": 2, "tap": True}
    assert r["destination"] == "hand" and r["target"]["kind"] == "any"

    r, why = tutors.repeatable_parse("Oracle", "At the beginning of your upkeep, search your library for a creature card, put that card into your hand, then shuffle.", "Enchantment")
    assert why is None and r["mode"] == "upkeep" and r["target"]["types"] == ["creature"]


def test_repeatable_tutor_refuses_nonmana_costs_and_qualified_targets():
    cases = (
        ("{T}, Sacrifice a creature: Search your library for a card, put that card into your hand, then shuffle.", "Artifact", "unsupported non-mana"),
        ("{1}, {T}: Search your library for a legendary creature card, put that card into your hand, then shuffle.", "Artifact", "unsupported qualifier"),
        ("Whenever X deals combat damage to a player, search your library for a card, put that card into your hand, then shuffle.", "Creature", "trigger other than"),
    )
    for text, tl, frag in cases:
        r, why = tutors.repeatable_parse("X", text, tl)
        assert r is None and why and frag in why, (text, r, why)


def test_repeatable_tutor_uses_unspent_mana_and_summoning_sickness():
    rows = [
        {"turn": 1, "battlefield": [], "graveyard": [], "hand": ["Seer"], "mana": 1, "spent": 0},
        {"turn": 2, "battlefield": ["Seer"], "graveyard": [], "hand": [], "mana": 3, "spent": 0},
        {"turn": 3, "battlefield": ["Seer"], "graveyard": [], "hand": [], "mana": 3, "spent": 1},
    ]
    ctx = {"cards": {"Seer": {"text": "{2}, {T}: Search your library for a card, put that card into your hand, then shuffle.", "type_line": "Creature"}},
           "models": {"Seer": {"types": ["creature"]}}}
    # T2 is arrival: {T} creature is sick. T3 has exactly two unspent mana and can activate once.
    assert tutors.repeatable_uses(_games(rows), "Seer", ctx, 3) == 1.0


def test_repeatable_tutor_reentry_resets_summoning_sickness_for_tap_creature():
    rows = [
        {"turn": 1, "battlefield": ["Seer"], "graveyard": [], "hand": [], "mana": 3, "spent": 0},
        {"turn": 2, "battlefield": ["Seer"], "graveyard": [], "hand": [], "mana": 3, "spent": 0},
        {"turn": 3, "battlefield": [], "graveyard": [], "hand": [], "mana": 3, "spent": 0},
        {"turn": 4, "battlefield": ["Seer"], "graveyard": [], "hand": [], "mana": 3, "spent": 0},
        {"turn": 5, "battlefield": ["Seer"], "graveyard": [], "hand": [], "mana": 3, "spent": 0},
    ]
    ctx = {"cards": {"Seer": {"text": "{2}, {T}: Search your library for a card, put that card into your hand, then shuffle.", "type_line": "Creature"}},
           "models": {"Seer": {"types": ["creature"]}}}
    # T1 and T4 are arrival/re-entry turns and cannot tap; T2/T5 can. T3 absent.
    assert tutors.repeatable_uses(_games(rows), "Seer", ctx, 5) == 2.0


def test_upkeep_tutor_starts_after_arrival_and_restarts_after_reentry():
    rows = [
        {"turn": 1, "battlefield": [], "graveyard": [], "hand": []},
        {"turn": 2, "battlefield": ["O"], "graveyard": [], "hand": []},
        {"turn": 3, "battlefield": ["O"], "graveyard": [], "hand": []},
        {"turn": 4, "battlefield": [], "graveyard": [], "hand": []},
        {"turn": 5, "battlefield": ["O"], "graveyard": [], "hand": []},
        {"turn": 6, "battlefield": ["O"], "graveyard": [], "hand": []},
    ]
    ctx = {"cards": {"O": {"text": "At the beginning of your upkeep, search your library for a card, put that card into your hand, then shuffle.", "type_line": "Enchantment"}},
           "models": {"O": {"types": ["enchantment"]}}}
    # End-step trace proxy: eligible on T3 and T6 only, not the arrival/re-entry turns T2/T5.
    assert tutors.repeatable_uses(_games(rows), "O", ctx, 6) == 2.0


def test_tutor_specs_remain_test_results_not_win_rates():
    for m in (tutors.GraveyardTutoring, tutors.RepeatableTutors):
        assert m.SPEC["evidence_class"] == "test_result"
        assert any("win rates" in x for x in m.SPEC["does_not_model"])
