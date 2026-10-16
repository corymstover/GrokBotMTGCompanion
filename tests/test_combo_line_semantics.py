from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import grixis_combo_steps_quality as cs


def test_action_counts_are_transparent_text_counts():
    steps = "Cast A by paying {1}.\nActivate B by sacrificing C.\nC dies, triggering D.\nResolve D.\nRepeat from step 1."
    n, a = cs.action_counts(steps)
    assert n == 5
    assert a == {"cast": 1, "activate": 1, "sacrifice": 1, "trigger": 1, "resolve": 1, "repeat": 1}


def test_declared_mana_preserves_symbols_and_colors():
    syms, colors = cs.declared_mana("{1}{U}{B} plus {R/R}")
    assert syms == ["1", "U", "B", "R/R"]
    assert colors == ["B", "R", "U"]


def test_zone_mentions_are_counts_not_normalized_requirements():
    z = cs.zone_mentions("A is in your graveyard. B is in your hand. Return A from your graveyard to the battlefield.")
    assert z["graveyard"] == 2
    assert z["hand"] == 1
    assert z["battlefield"] == 1
    assert z["exile"] == 0


def test_endpoint_hints_do_not_turn_infinite_into_automatic_win():
    assert cs.endpoint_hints(["Infinite colorless mana", "Infinite storm count"]) == ["mana", "storm"]
    got = cs.endpoint_hints(["Infinite damage"])
    assert got == ["damage"]
    assert "win" not in got


def test_missing_step_record_is_explicit_low_confidence():
    combo = {"id": "missing", "cards": ["A", "B"]}
    out = cs.line_record(combo, {})
    assert out["record_found"] is False
    assert out["confidence"] == "low"
    assert out["derived"]["interaction_window_proxy"]["stack_action_count_proxy"] == 0


def test_present_step_record_preserves_raw_source_and_derives_only_simple_metrics():
    combo = {"id": "x", "cards": ["A", "B"]}
    cache = {"x": {"status": "OK", "mana_needed": "{2}{U}", "easy_prerequisites": "A in your graveyard",
                   "notable_prerequisites": "", "notes": "", "produces": ["Infinite mill"],
                   "steps": "Cast B.\nResolve B.\nRepeat."}}
    out = cs.line_record(combo, cache)
    assert out["record_found"] is True and out["confidence"] == "moderate"
    assert out["raw"]["mana_needed"] == "{2}{U}"
    assert out["derived"]["colored_symbols_declared"] == ["U"]
    assert out["derived"]["zone_mentions"]["graveyard"] == 1
    assert out["derived"]["interaction_window_proxy"]["stack_action_count_proxy"] == 2
    assert out["derived"]["endpoint_hints"] == ["mill"]
    assert any("not an official" in x for x in out["limitations"])
