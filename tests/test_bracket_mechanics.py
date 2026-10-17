import json
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import grixis_bracket_mechanics as bm


def docs():
    return [json.loads(p.read_text()) for p in sorted((ROOT/'data/grixis/bracket_stress_mechanics').glob('*.json')) if p.name!='summary.json']


def test_b5_mechanic_artifacts_cover_exact_b5_population_and_frozen_snapshot():
    rows=bm.b5_entries()
    ds=docs()
    assert len(ds)==len(rows)>0
    assert {d['slug'] for d in ds}=={e['slug'] for _,e,_ in rows}
    assert all(d['provenance']['development_snapshot']=='snap-20261016' for d in ds)
    assert all(d['authority']['can_decide'] is False and d['aggregate_score'] is None for d in ds)


def test_every_preregistered_b5_module_has_executed_result():
    for d in docs():
        assert d['required_module_ids']==['counterspell_density','stack_protection','stax_tax']
        assert [x['module_id'] for x in d['module_results']]==d['required_module_ids']
        assert all(x['status']=='executed_deck_level_test_result' for x in d['module_results'])


def test_deck_level_mechanic_artifacts_never_emit_forbidden_outcome_metrics():
    for d in docs():
        text=json.dumps(d).lower()
        assert '"win_rate"' not in text
        assert '"multiplayer_win_rate"' not in text
        assert '"win_probability"' not in text
        assert '"weighted_score"' not in text
