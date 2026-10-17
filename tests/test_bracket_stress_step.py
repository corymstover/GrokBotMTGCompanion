import json
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import grixis_bracket_stress_gain as gain
import grixis_stress_step as step


def test_gain_proof_has_two_distinct_real_bracket_examples_and_no_score():
    d=gain.build_record()
    assert d['authority']['can_decide'] is False
    assert d['after']['decks']==62
    assert d['after']['routed_packets']==62 and d['after']['red_team_packets']==62
    assert d['after']['aggregate_outcome_scores']==0
    assert d['after']['module_items_executed_deck_level']>0
    fams={x['suite_family'] for x in d['real_deck_examples']}
    assert fams=={'B5_competitive','B4_resilience'}
    assert all(x['slug'] for x in d['real_deck_examples'])


def test_step_f_populations_are_complete_before_integration():
    assert step.count(ROOT/'data/grixis/bracket_stress')==62
    assert step.count(ROOT/'data/grixis/bracket_stress_packets')==62
    assert step.count(ROOT/'data/grixis/bracket_red_team')==62
    assert step.count(ROOT/'data/grixis/bracket_stress_mechanics')==step.expected_b5()


def test_module_items_are_executed_while_judgment_remains_unanswered():
    packets=[json.loads(p.read_text()) for p in (ROOT/'data/grixis/bracket_stress_packets').glob('*.json') if p.name!='summary.json']
    statuses=[x['evidence']['status'] for d in packets for x in d['items']]
    assert 'pending_deck_level_module_execution' not in statuses
    assert 'executed_deck_level_module_result' in statuses
    assert 'judgment_required' in statuses
    assert 'passed' not in statuses


def test_generic_before_and_bracket_after_are_materially_distinct():
    d=gain.build_record()
    assert d['before']['scenario_count']==9
    a,b=d['real_deck_examples']
    assert a['stress_ids'] != b['stress_ids']
    assert len(a['stress_ids']) != len(b['stress_ids'])
