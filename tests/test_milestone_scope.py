"""Bot cycle 62: Cory's M1/M3 acceptance and its scope (M3 results never decide on their own)."""
import copy

from _helpers import ga  # noqa: F401


def test_m1_m3_accepted_with_verbatim_scope_others_not():
    reg = ga.load_json(ga.REGISTRY)
    ms = reg["program"]["milestones"]
    for m in ("M1", "M3"):
        x = ms[m]
        assert x["status"] == "accepted" and x["accepted_by"] == "corymstover" and x["accepted_date"] == "2026-10-16"
        assert x["accepted_at"] == "2026-10-16T17:39Z" and "t48u" in x["acceptance_evidence"]
        assert x["scope_verbatim"] == ga.MILESTONE_SCOPE_VERBATIM
    for m in ("M2", "M4", "M5", "M6", "M7", "M8"):
        assert ms[m]["status"] != "accepted" and not ms[m]["accepted_by"]
    assert "Wick" in ms["M2"]["pending_note"] and "Mairsil" in ms["M2"]["pending_note"]
    assert ga.milestone_problems(ms, set(reg["human_approvers"])) == []
    bad = copy.deepcopy(ms)
    bad["M3"]["scope_verbatim"] = "M3 accepted"
    assert ga.milestone_problems(bad, set(reg["human_approvers"]))


def test_m3_test_results_never_decide_alone():
    t = [{"id": "test:x:goldfish:1", "class": "test_result", "confidence": "high"}]
    ok, why = ga.decision_support_ok(t)
    assert not ok and any("M3 results do not independently decide" in w for w in why)
    ok, _ = ga.decision_support_ok(t + [{"id": "oracle:Sol Ring", "class": "fact", "confidence": "verified"}])
    assert ok
    # a judgment review resting on test results alone cannot support a decision either
    c = {"card": "X", "judgment_review": {"kind": "judgment_review", "method": "human", "by": "corymstover", "date": "2026-10-16",
                                          "swaps": ["swap:x"], "verdict": "accept", "reasoning": "r", "evidence_items": t}}
    assert ga.decision_review_problems(c, "swap:x")
    # and a screening review never does
    assert ga.decision_review_problems({"card": "X", "review": {"kind": "screening_review"}})
