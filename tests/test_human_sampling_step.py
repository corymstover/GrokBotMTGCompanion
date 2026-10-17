import json
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import grixis_human_review_manifest as hr
import grixis_human_sampling_gain as hg
import grixis_human_sampling_step as hs


def load(p): return json.loads((ROOT/p).read_text())


def test_review_queue_exactly_matches_deduped_static_selection():
    sample=load('data/grixis/human_sampling_manifest.json')
    review=hr.build_manifest()
    assert len(review['static_review_queue'])==len(sample['deduped_static_workload'])>0
    assert {x['slug'] for x in review['static_review_queue']}=={x['slug'] for x in sample['deduped_static_workload']}


def test_generated_review_items_are_pending_and_never_script_authored():
    review=hr.build_manifest()
    assert review['authority']['can_decide'] is False
    assert review['authority']['script_may_author_judgment'] is False
    for item in review['static_review_queue']:
        r=item['review_requirement']
        assert r['status']=='pending'
        assert r['script_may_author'] is False
        assert r['result_record'] is None
        assert r['requires_commander_first_context'] is True


def test_dynamic_review_queues_remain_empty_until_m6_inputs():
    review=hr.build_manifest(); sample=load('data/grixis/human_sampling_manifest.json')
    for sid in ('high_optimizer_disagreement','major_change'):
        q=review['dynamic_review_queues'][sid]
        assert q['status']=='awaiting_future_inputs' and q['entries']==[]
        assert q['selector_function']==sample['dynamic_hooks'][sid]['function']
        assert q['required_fields']==sample['dynamic_hooks'][sid]['required_fields']


def test_gain_proof_tracks_real_review_workload_without_decision_authority():
    review=hr.build_manifest(); gain=hg.build_gain(); sample=load('data/grixis/human_sampling_manifest.json')
    per={x['id']:x['selected_count'] for x in sample['strata']}
    assert gain['after']['unique_static_decks_selected']==len(review['static_review_queue'])
    assert gain['after']['review_queue_items_pending']==len(review['static_review_queue'])
    assert gain['after']['all_exception_eligible_selected']==per['exception']
    assert gain['after']['all_pending_release_eligible_selected']==per['pending_release']
    assert gain['after']['scripts_can_author_judgment'] is False
    assert gain['authority']['can_decide'] is False


def test_step_h_integration_check_passes_on_committed_artifacts():
    assert hs.check()==0
