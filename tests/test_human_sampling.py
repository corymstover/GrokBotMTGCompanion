import json
import random
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import grixis_human_sampling as hs


def test_static_manifest_uses_frozen_policy_and_keeps_dynamic_empty():
    d=hs.build_manifest(); f=json.loads((ROOT/'data/grixis/human_sampling_freeze.json').read_text())
    assert d['policy_sha256']==f['policy_sha256']
    by={x['id']:x for x in d['strata']}
    assert set(by)==set(hs.STATIC+hs.DYNAMIC)
    assert all(by[x]['status']=='awaiting_future_inputs' and by[x]['selected']==[] for x in hs.DYNAMIC)
    assert d['authority']['can_decide'] is False


def test_exception_and_pending_release_select_every_eligible_deck():
    d=hs.build_manifest(); by={x['id']:x for x in d['strata']}
    for sid in ('exception','pending_release'):
        assert by[sid]['quota']=='all'
        assert by[sid]['selected_count']==by[sid]['eligible_count']


def test_static_sampling_is_deterministic_and_quota_bounded():
    d1=hs.build_manifest(); d2=hs.build_manifest(); assert d1==d2
    by={x['id']:x for x in d1['strata']}
    for sid in ('random','anomaly','cedh','low_commander_dependence','rules_sensitive'):
        assert by[sid]['selected_count']<=8
        assert len({x['slug'] for x in by[sid]['selected']})==by[sid]['selected_count']


def opt_records():
    return [
      {'slug':'a','pass_a_hash':'ha1','pass_b_hash':'hb1','pass_a_challenger_hash':'x','pass_b_challenger_hash':'y','pass_a_swaps':['A=>B','C=>D'],'pass_b_swaps':['A=>B','E=>F']},
      {'slug':'b','pass_a_hash':'ha2','pass_b_hash':'hb2','pass_a_challenger_hash':'z','pass_b_challenger_hash':'z','pass_a_swaps':['A=>B'],'pass_b_swaps':['C=>D','E=>F','G=>H']},
      {'slug':'c','pass_a_hash':'ha3','pass_b_hash':'hb3','pass_a_challenger_hash':'m','pass_b_challenger_hash':'n','pass_a_swaps':[],'pass_b_swaps':[]},
    ]


def test_optimizer_disagreement_formula_is_order_independent_and_hash_disagreement_first():
    seed='seed'; a=hs.optimizer_disagreement_selection(opt_records(),seed,8)
    r=opt_records(); random.Random(7).shuffle(r); b=hs.optimizer_disagreement_selection(r,seed,8)
    assert a==b
    assert a[0]['slug']=='a'  # hash disagreement + swap conflict beats c's hash disagreement with no swap conflict
    assert a[-1]['slug']=='b' # matching challenger hashes rank behind disagreements


def test_major_change_formula_is_order_independent_and_excludes_small_nonstructural_change():
    rows=[
      {'slug':'plain','total_swaps':4,'win_route_changed':False,'required_package_change_count':0,'mana_base_change_count':2},
      {'slug':'five','total_swaps':5,'win_route_changed':False,'required_package_change_count':0,'mana_base_change_count':0},
      {'slug':'mana','total_swaps':2,'win_route_changed':False,'required_package_change_count':0,'mana_base_change_count':3},
      {'slug':'package','total_swaps':1,'win_route_changed':False,'required_package_change_count':2,'mana_base_change_count':0},
      {'slug':'win','total_swaps':1,'win_route_changed':True,'required_package_change_count':0,'mana_base_change_count':0},
    ]
    a=hs.major_change_selection(rows,'seed',8); b=hs.major_change_selection(list(reversed(rows)),'seed',8)
    assert a==b
    assert [x['slug'] for x in a]==['win','package','five','mana']
    assert 'plain' not in {x['slug'] for x in a}


def test_dynamic_optimizer_records_require_committed_hash_fields():
    bad=opt_records()[0].copy(); bad['pass_a_hash']=''
    try: hs.optimizer_disagreement_selection([bad],'seed',8)
    except ValueError: pass
    else: raise AssertionError('missing committed pass hash must fail')
