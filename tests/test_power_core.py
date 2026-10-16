from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import grixis_power_core as pc


def combo(structural="commander_independent_power_package", n=3, outcome="blueprint_designated_win_line", payoff=None):
    cards = [chr(ord("A") + i) for i in range(n)]
    return {
        "id": "c1", "cards": cards,
        "classification": {"structural_hint": structural, "outcome_hint": outcome,
                           "evidence": ["spellbook:c1"]},
        "axes": {
            "card_count": {"value": n},
            "required_payoff": {"value": {"blueprint_external_payoffs_or_enablers": payoff or []}},
            "commander_contribution": {"evidence": ["blueprint:test#commander_role"]},
        },
    }


def test_commander_independent_blueprint_win_becomes_review_candidate_not_decision():
    c = pc.candidate(combo())
    assert c["classification"] == "power_core_review_candidate"
    assert c["commander_independent"] is True
    assert c["compactness"] == "compact_3"
    assert c["materiality"]["current_overlay_changes_blueprint"] is False
    assert c["materiality"]["proposed_blueprint_changes"] == []


def test_commander_native_combo_is_not_power_core_review_candidate():
    assert pc.candidate(combo(structural="commander_native_combo")) is None


def test_extended_package_still_flagged_but_not_called_compact():
    c = pc.candidate(combo(n=5))
    assert c["compactness"] == "extended_4_plus"
    assert c["classification"] == "power_core_review_candidate"


def test_external_payoff_is_preserved_as_caution():
    c = pc.candidate(combo(payoff=["Payoff"]))
    assert any("external payoff" in x for x in c["why_flagged"])


def test_materiality_gate_catches_every_governance_field():
    for field in pc.MATERIAL_FIELDS:
        assert pc.material_fields_touched([{"path": f"/{field}/x"}]) == [field]


def test_overlay_only_metadata_does_not_reopen_m2():
    assert pc.material_fields_touched([{"path": "/overlay_label"}, {"path": "/review_note"}]) == []
