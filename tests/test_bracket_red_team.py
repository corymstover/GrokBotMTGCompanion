import json
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_bracket_red_team as rt


def entry(slug):
    r=json.loads((ROOT/"data/grixis/registry.json").read_text())
    return next((did,e) for did,e in r["decks"].items() if e["slug"]==slug)


def test_kess_b5_packet_has_only_pending_protected_win_review():
    did,e=entry("kess-dissident-mage"); d=rt.build_one(did,e)
    assert d["suite_family"]=="B5_competitive"
    assert [x["id"] for x in d["reviews"]]==["protected_win_red_team"]
    r=d["reviews"][0]
    assert r["review_status"]=="pending"
    assert r["reviewer"] is None and r["analysis"] is None and r["verdict"] is None
    assert r["can_decide"] is False and r["review_contract"]["may_decide_swap"] is False
    assert r["evidence_context"]["blueprint_failure_modes"]
    assert r["evidence_context"]["commander_structure"]["accepted_role"]["level"]=="central"


def test_b4_packet_contains_attrition_pillowfort_token_and_noncreature_prompts():
    reg=json.loads((ROOT/"data/grixis/registry.json").read_text())
    did,e=next((did,e) for did,e in reg["decks"].items() if int((e.get("ceiling",{}).get("grok_estimated_ceiling",{}) or {}).get("value") or (e.get("ceiling",{}).get("source_ceiling",{}) or {}).get("value") or 4)==4)
    d=rt.build_one(did,e); ids={x["id"] for x in d["reviews"]}
    assert d["suite_family"]=="B4_resilience"
    assert {"repeated_removal_attrition","pillowfort","token_stall","artifact_enchantment_interaction"} <= ids
    assert all(x["review_status"]=="pending" and x["verdict"] is None for x in d["reviews"])


def test_script_never_creates_judgment_review_or_decision():
    did,e=entry("kess-dissident-mage"); d=rt.build_one(did,e)
    txt=json.dumps(d).lower()
    assert d["authority"]["can_decide"] is False
    assert '"review_status": "complete"' not in txt
    assert '"verdict": "' not in txt
    assert all(x["review_contract"]["required_review_method"]=="human_or_agent_judgment_not_script" for x in d["reviews"])
    assert all(x["review_contract"]["heuristic_only_sufficient"] is False for x in d["reviews"])


def test_red_team_context_preserves_blueprint_and_audit_without_answering_question():
    did,e=entry("kess-dissident-mage"); d=rt.build_one(did,e); r=d["reviews"][0]
    ctx=r["evidence_context"]
    assert ctx["blueprint_win_conditions"]
    assert ctx["blueprint_anti_goals"]["value"]
    assert ctx["audit_focus"]
    assert ctx["supporting_test_refs"]
    assert r["analysis"] is None
