"""Evidence classes, provisional dispositions, escalation, independent optimizer passes, v2 exploratory gating."""
from _helpers import ga, load


def ev(cls, conf="high", i="e"):
    return {"id": i, "class": cls, "confidence": conf}


def test_seven_classes_and_confidence_levels():
    assert len(ga.EVIDENCE_CLASSES) == 7 and "approved_decision" in ga.EVIDENCE_CLASSES
    assert ga.CONFIDENCE == ("verified", "high", "moderate", "low", "test_required", "blocked")


def test_heuristics_alone_cannot_decide():
    ok, why = ga.decision_support_ok([ev("heuristic"), ev("derived_metric"), ev("hypothesis")])
    assert not ok and any("diagnostics cannot decide" in w for w in why)
    assert ga.decision_support_ok([ev("heuristic"), ev("fact", "verified")])[0]
    assert not ga.decision_support_ok([])[0]


def test_unresolved_evidence_blocks():
    ok, why = ga.decision_support_ok([ev("fact"), ev("test_result", "test_required", "t1")])
    assert not ok and any("t1" in w for w in why)
    assert not ga.decision_support_ok([ev("rumor")])[0]


def test_disposition_without_refs_is_provisional():
    slot = {"card": "X", "roles": ["draw"], "blueprint_refs": ["bp:1"], "graph_refs": ["g:1"], "alternatives": ["Y"], "redundancy": 2, "reason": "core draw"}
    assert ga.disposition_status(slot) == "complete"
    for k in ("blueprint_refs", "graph_refs", "alternatives", "reason"):
        assert ga.disposition_status({**slot, k: [] if k != "reason" else ""}) == "provisional", k
    assert ga.disposition_status({**slot, "redundancy": None}) == "provisional"
    audit = {"deck_id": "D", "slots": [{**slot, "graph_refs": [], "review_status": "complete"}]}
    assert ga.audit_problems(audit)


def test_escalation_needs_reasons_evidence_and_full_review():
    good = {"card": "X", "full_review": True, "escalation": {"escalated": True, "reasons": ["package_gap"], "evidence_refs": ["oracle:X"]}}
    assert ga.candidate_problems(good) == []
    assert ga.candidate_problems({**good, "full_review": False})
    assert ga.candidate_problems({**good, "escalation": {"escalated": True, "reasons": [], "evidence_refs": ["x:y"]}})
    assert ga.candidate_problems({**good, "escalation": {"escalated": True, "reasons": ["new_card"], "evidence_refs": []}})
    assert set(ga.ESCALATION_REASONS) >= {"dependency_analysis", "new_card", "unusual_oracle_interaction", "package_gap", "reviewer_evidence"}


def _pass(pid, opt, fam, inputs, formula, informed=()):
    return {"pass_id": pid, "optimizer": opt, "objective_function": {"id": pid, "family": fam, "inputs": list(inputs), "formula_sha256": formula},
            "informed_by": list(informed)}


def test_optimizer_passes_must_be_independent():
    a = _pass("A", "commander_first", "blueprint_fidelity", ["blueprint", "oracle_hooks"], "f1")
    b = _pass("B", "performance", "measured_performance", ["goldfish", "stress"], "f2")
    assert ga.check_reconciliation(a, b) == []
    assert ga.check_reconciliation(a, {**b, "objective_function": {**b["objective_function"], "formula_sha256": "f1"}})
    assert ga.check_reconciliation(a, {**b, "objective_function": {**b["objective_function"], "family": "blueprint_fidelity"}})
    assert ga.check_reconciliation(a, {**b, "informed_by": ["A"]})
    assert ga.check_reconciliation(_pass("A", "commander_first", "blueprint_fidelity", ["blueprint", "edhrec_inclusion"], "f1"), b)
    assert ga.check_reconciliation(a, _pass("B", "performance", "measured_performance", ["goldfish", "blueprint"], "f2"))


def test_v2_output_is_exploratory_and_never_final():
    d = load("data/grixis_refine_v2.json")
    ms = load("data/grixis/registry.json")["program"]["milestones"]
    gate = ms["M2"]["status"] == "accepted" and ms["M4"]["status"] == "accepted"
    assert d["exploratory"] is (not gate) and d["m6_gate"]["open"] is gate
    assert len(d["decks"]) == 62  # no ceiling shortcut: every deck analyzed
    for did, x in d["decks"].items():
        assert x["state"] == "CHALLENGER" and "unapproved" in x["label"]
        v = x["verdict"].lower()
        assert "final list" not in v.replace("not a final list", "") and "at its ceiling" not in v.replace("not evidence that the list is at its ceiling", ""), did
        for r in x["recommendations"]:
            assert isinstance(r["diagnostics"]["power_guard"]["pass"], bool)  # gates are diagnostics, recorded either way
            assert r["evidence"] and all(":" in e for e in r["evidence"])
    lc = d["lift_check"]
    assert lc["cardviews"] > 0 and lc["with_lift"] == lc["cardviews"] and lc["with_trend"] == lc["cardviews"]


def test_v2_never_cuts_a_project_exception():
    d = load("data/grixis_refine_v2.json")["decks"]["Cecily__Bjorna__Lutri"]
    cut = {r["cut"] for r in d["recommendations"]} | {s["card"] for s in d["weakest_slots"]}
    assert not cut & {"Trade Secrets", "Yawgmoth's Bargain", "Lutri, the Spellchaser"}
