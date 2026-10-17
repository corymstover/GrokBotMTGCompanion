import json
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import grixis_human_sampling_policy as hp


def policy(): return json.loads((ROOT/'data/grixis/human_sampling_policy.json').read_text())


def test_all_nine_required_strata_are_frozen_before_results():
    p=policy(); ids={x['id'] for x in p['strata']}
    assert ids==hp.IDS
    assert p['status']=='frozen_before_m6_outputs'
    assert p['authority']['can_decide'] is False
    assert p['review_output_requirement']['script_may_author_judgment'] is False


def test_dynamic_strata_formula_is_predeclared_not_selectable_now():
    p=policy(); d={x['id']:x for x in p['strata']}
    assert d['high_optimizer_disagreement']['timing']=='after_pass_a_b_commit_before_reveal_reconciliation'
    assert d['major_change']['timing']=='after_reconciliation_before_approval_ready'
    assert d['high_optimizer_disagreement']['quota']==8
    assert d['major_change']['quota']==8
    assert 'symmetric-difference' in d['high_optimizer_disagreement']['ranking_rule']
    assert 'total swaps' in d['major_change']['ranking_rule']


def test_exception_and_pending_release_are_all_not_sampled_away():
    p=policy(); d={x['id']:x for x in p['strata']}
    assert d['exception']['quota']=='all'
    assert d['pending_release']['quota']=='all'


def test_policy_digest_is_byte_level_and_stable_for_same_file():
    assert hp.digest().startswith('sha256:')
    assert hp.digest()==hp.digest()
    assert len(hp.digest())==71
