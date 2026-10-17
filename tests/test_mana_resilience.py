import json
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))

import grixis_mana_resilience as mr


def test_failure_complement_is_bounded():
    assert mr.fail(1.0)==0.0
    assert mr.fail(0.0)==1.0
    assert mr.fail(0.375)==0.625
    assert mr.fail(2.0)==0.0
    assert mr.fail(-1.0)==1.0


def test_one_source_unavailable_is_structural_delta_not_library_shrink():
    masks=["U","B","R",""]*3
    labels=[f"c{i}" for i in range(len(masks))]
    r=mr.one_source_sensitivity(masks,labels,7,{"U":1,"B":1,"R":1})
    assert 0<=r["baseline"]<=1
    assert 0<=r["mean_delta"]<=r["worst_delta"]<=1
    assert r["sources_tested"]==9
    assert r["worst_sources"]


def test_redundant_sources_reduce_one_source_fragility():
    sparse=["U","B","R"]+[""]*9
    dense=["U","U","B","B","R","R"]+[""]*6
    labels=[str(i) for i in range(12)]
    a=mr.one_source_sensitivity(sparse,labels,7,{"U":1,"B":1,"R":1})
    b=mr.one_source_sensitivity(dense,labels,7,{"U":1,"B":1,"R":1})
    assert b["worst_delta"] < a["worst_delta"]


def test_fetch_resilience_marks_single_color_target_points():
    timing={"fetch_validation":[{
        "card":"F","target_count":3,"actual_target_colors":"UBR",
        "targets_by_color":{"U":["A","B"],"B":["B"],"R":["C","D"]}
    }]}
    r=mr.fetch_resilience(timing)[0]
    assert r["single_target"] is False
    assert r["colors_with_only_one_target"]=={"B":["B"]}
    assert r["all_supported_colors_have_redundant_targets"] is False


def test_real_kess_build_is_non_deciding_and_bounded():
    reg=json.loads((ROOT/"data/grixis/registry.json").read_text())
    did,e=next((did,e) for did,e in reg["decks"].items() if e["slug"]=="kess-dissident-mage")
    d=mr.build_one(did,e)
    assert d["authority"]["can_decide"] is False
    assert d["canonical_hash"]==e["canonical_project_list"]["hash"]
    assert d["commander_colored_failure"]
    for row in d["turn_failure"].values():
        for k,v in row.items():
            if k.endswith("failure") and isinstance(v,(int,float)):
                assert 0<=v<=1
        s=row["one_strict_source_unavailable_UBR"]
        assert 0<=s["mean_delta"]<=s["worst_delta"]<=1
