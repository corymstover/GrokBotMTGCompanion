from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import grixis_mech as gm
from grixis_mech import router


def card(text, type_line="Enchantment"):
    return {"text": text, "type_line": type_line, "mana_cost": ""}


def test_no_genuine_step_e_module_family_remains_unimplemented():
    assert [k for k in router.PLANNED if k not in gm.MODULES] == []


def test_variable_token_text_is_residual_not_a_fake_planned_module():
    cards = {
        "Variable Maker": card("When Variable Maker enters, create X 1/1 blue Creature tokens."),
        "Blank": card("Flying", "Creature — Bird"),
    }
    r = router.route_swap("Blank", "Variable Maker", cards)
    assert "tokens_other" in r["residual"]
    assert "tokens_other" not in r["planned"]
    assert r["status"] == "not_modelable"
    assert "intentionally require judgment" in r["reason"]


def test_unsupported_sacrifice_semantics_stay_residual():
    cards = {
        "Land Cost": card("As an additional cost to cast this spell, sacrifice a land.", "Sorcery"),
        "Blank": card("Flying", "Creature — Bird"),
    }
    r = router.route_swap("Blank", "Land Cost", cards)
    assert "sacrifice_other" in r["residual"]
    assert "sacrifice_other" not in r["planned"]
    assert r["status"] == "not_modelable"


def test_commander_specific_hook_escalates_to_judgment_not_planned_simulation():
    cards = {
        "Odd Card": card("Flying", "Creature — Wizard"),
        "Blank": card("Vigilance", "Creature — Soldier"),
    }
    r = router.route_swap("Blank", "Odd Card", cards,
                          hooks={"Odd Card": "commander_specific: unusual Oracle interaction"})
    assert r["planned"] == []
    assert r["status"] == "not_modelable"
    assert r["commander_specific"] == {"Odd Card": "commander_specific: unusual Oracle interaction"}
    assert "Commander-first judgment/Step D" in r["reason"]


def test_supported_module_wins_routing_but_residual_warning_is_preserved():
    cards = {
        "Death Watcher": card("Whenever another creature dies, draw a card.", "Creature — Human Wizard"),
        "Blank": card("Flying", "Creature — Bird"),
    }
    r = router.route_swap("Blank", "Death Watcher", cards)
    assert "death_triggers" in r["modules"]
    assert r["status"] == "routed"
    # Broad 'dies' text is retained as a diagnostic residual, not another module.
    assert "death_other" in r["residual"]


def test_registry_policy_has_residuals_but_zero_planned_families():
    # Avoid importing the cache-backed mechanics builder; test the same source-of-truth objects it serializes.
    assert set(router.RESIDUAL) == {"death_other", "sacrifice_other", "tokens_other"}
    assert not set(router.RESIDUAL) & set(gm.MODULES)
