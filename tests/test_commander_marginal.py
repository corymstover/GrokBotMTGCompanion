import json
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_commander_marginal as cm
import grixis_commander_marginal_gain as gain
import grixis_commander_step as step


def metric(key=0.5):
    return {"samples":100,"commander_cast_by_turn6":key,"commander_turn_mean_when_cast":3.0,"mana_spent_t1_6_mean":12.0,"mana_available_t1_6_mean":16.0,"extra_cards_drawn_mean":1.5,"tutors_resolved_mean":0.4,"fast_mana_uses_mean":0.3,"first_key_set_access_by_turn4":{"pkg:a":0.6,"pkg:b":0.2},"combo_assembled_by_turn6":0.25,"win_proxy_by_turn6":0.1,"note":"x"}


def test_mode_vector_keeps_dimensions_separate_without_scalar_score():
    v=cm.mode_vector(metric())
    assert v["mana_efficiency"]["spent_over_available_proxy"]==0.75
    assert v["package_access"]["expected_key_sets_first_accessed_by_turn4"]==0.8
    assert set(v["meaningful_progress_vector"])=={"commander_cast_by_turn6","extra_cards_drawn_mean","tutors_resolved_mean","expected_key_sets_first_accessed_by_turn4","combo_assembled_by_turn6"}
    assert "score" not in json.dumps(v).lower()


def test_vector_delta_is_normal_minus_counterfactual_componentwise():
    a=cm.mode_vector(metric(1.0)); b=cm.mode_vector(metric(0.25)); d=cm.vector_delta(a,b)
    assert d["meaningful_progress_vector"]["commander_cast_by_turn6"]==0.75
    assert d["mana_efficiency"]["spent_over_available_proxy"]==0.0


def test_gain_proof_uses_real_structural_decks_and_never_decides():
    d=gain.build_record()
    assert d["authority"]["can_decide"] is False
    assert d["measured"]["structural_decks"]==62
    assert d["measured"]["automatic_deck_decisions"]==0
    assert len(d["real_deck_examples"])>=2
    assert any(x["slug"]=="kess-dissident-mage" for x in d["real_deck_examples"])


def test_step_gate_accepts_only_zero_or_full_dynamic_populations():
    expected=len(json.loads((ROOT/"data/grixis/registry.json").read_text())["decks"])
    assert expected==62
    c=step.count(ROOT/"data/grixis/commander_counterfactual")
    m=step.count(ROOT/"data/grixis/commander_marginal")
    assert c in (0,62)
    assert m in (0,62)
