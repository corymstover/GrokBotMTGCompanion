import json
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_bracket_stress as bs


def entry(slug):
    r=json.loads((ROOT/"data/grixis/registry.json").read_text())
    return next((did,e) for did,e in r["decks"].items() if e["slug"]==slug)


def test_kess_gets_b5_competitive_priorities():
    did,e=entry("kess-dissident-mage"); d=bs.build_one(did,e)
    assert d["bracket"]["value"]==5
    assert d["bracket"]["suite_family"]=="B5_competitive"
    ids={x["id"] for x in d["items"]}
    assert {"turbo_clock","stack_protection","stax_tax","protected_win_red_team"} <= ids
    assert "pillowfort" not in ids


def test_b4_and_b5_are_not_same_suite():
    assert [x[0] for x in bs.B4] != [x[0] for x in bs.B5]
    assert "board_wipe" in {x[0] for x in bs.B4}
    assert "turbo_clock" in {x[0] for x in bs.B5}


def test_weights_are_priority_only_and_sum_to_one():
    for rows in (bs.B4,bs.B5):
        assert abs(sum(x[2] for x in rows)-1.0)<1e-12
        assert all(x[2]>0 for x in rows)
    did,e=entry("kess-dissident-mage"); d=bs.build_one(did,e)
    assert d["weight_semantics"]=="review_priority_only_not_outcome_score"
    assert d["authority"]["can_decide"] is False
    assert not any(x["decision_authority"] for x in d["items"])


def test_judgment_only_stress_has_no_fake_executor():
    for rows in (bs.B4,bs.B5):
        for _,kind,_,_,executor in rows:
            if kind=="judgment_prompt":
                assert executor is None
