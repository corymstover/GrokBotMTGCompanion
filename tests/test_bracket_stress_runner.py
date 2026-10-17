import json
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_bracket_stress_runner as br


def entry(slug):
    r=json.loads((ROOT/"data/grixis/registry.json").read_text())
    return next((did,e) for did,e in r["decks"].items() if e["slug"]==slug)


def test_kess_routes_b5_to_existing_stress_goldfish_and_real_modules():
    did,e=entry("kess-dissident-mage"); d=br.build_one(did,e)
    by={x["id"]:x for x in d["items"]}
    assert d["suite_family"]=="B5_competitive"
    assert by["first_key_spell_countered"]["evidence"]["status"]=="reused_existing_test_result"
    assert by["turbo_clock"]["evidence"]["status"]=="reused_goldfish_readiness"
    assert by["stack_protection"]["evidence"]["resolved_module_ids"]==["counterspell_density","stack_protection"]
    assert by["stack_protection"]["evidence"]["status"]=="pending_deck_level_module_execution"
    assert by["stax_tax"]["evidence"]["resolved_module_ids"]==["stax_tax"]
    assert by["protected_win_red_team"]["evidence"]["status"]=="judgment_required"


def test_no_weighted_or_aggregate_outcome_score_is_emitted():
    did,e=entry("kess-dissident-mage"); d=br.build_one(did,e)
    assert d["aggregate_score"] is None
    assert d["weight_semantics"]=="review_priority_only_not_outcome_score"
    assert d["authority"]["can_decide"] is False
    assert not any(x["decision_authority"] for x in d["items"])
    txt=json.dumps(d).lower()
    assert 'weighted_score' not in txt and 'win_rate' not in txt


def test_b4_judgment_prompts_remain_unanswered():
    r=json.loads((ROOT/"data/grixis/registry.json").read_text())
    did,e=next((did,e) for did,e in r["decks"].items() if int((e.get("ceiling",{}).get("grok_estimated_ceiling",{}) or {}).get("value") or (e.get("ceiling",{}).get("source_ceiling",{}) or {}).get("value") or 4)==4)
    d=br.build_one(did,e)
    assert d["suite_family"]=="B4_resilience"
    for x in d["items"]:
        if x["kind"]=="judgment_prompt":
            assert x["evidence"]["status"]=="judgment_required"
            assert x["evidence"]["automated_verdict"] is None


def test_legacy_stress_reuse_preserves_original_prereg_and_verdict():
    did,e=entry("kess-dissident-mage"); d=br.build_one(did,e)
    x=next(x for x in d["items"] if x["id"]=="commander_disruption")
    ev=x["evidence"]
    assert ev["status"]=="reused_existing_test_result"
    assert ev["legacy_preregistered"]["metric"]
    assert ev["legacy_verdict"] in {"pass","fail","inconclusive","no_detectable_difference"}
    assert ev["source"].startswith("data/grixis/stress/")
