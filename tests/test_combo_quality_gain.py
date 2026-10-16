from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import grixis_combo_quality_gain as gain


def test_gain_record_preserves_zero_auto_decisions():
    d = gain.build_record()
    assert d["measured_deltas"]["strategic_priority_auto_decisions"] == 0
    assert "unresolved strategic judgment" in d["after"]["governance_guards"][1]


def test_gain_record_has_commander_native_and_power_core_examples():
    d = gain.build_record()
    kinds = {x["kind"] for x in d["worked_examples"]}
    assert "commander_native" in kinds
    assert "commander_independent_external_payoff" in kinds
    assert "power_core_review" in kinds


def test_gain_is_more_than_volume():
    d = gain.build_record()
    m = d["measured_deltas"]
    assert m["spellbook_lines"] > 0
    assert m["direct_commander_piece_lines"] > 0
    assert m["commander_independent_win_hints"] > 0
    assert m["power_core_review_candidates"] > 0
    assert m["step_records"] > 0
    assert m["declared_mana_records"] > 0
    assert m["zone_mentions"] > 0


def test_before_after_models_are_not_same_representation():
    d = gain.build_record()
    assert d["before"]["model"] != d["after"]["model"]
    assert len(d["after"]["available_dimensions"]) > len(d["before"]["available_fields"])
