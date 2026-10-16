"""Deck state machine and human-approval enforcement (Cory constraints 6 and 8)."""
from _helpers import APPROVED_PATH, APPROVERS, H, MILESTONES_NOT, MILESTONES_OK, entry, ga, load, record


def test_every_state_has_transitions_and_targets_are_states():
    assert set(ga.TRANSITIONS) == set(ga.STATES)
    for a, bs in ga.TRANSITIONS.items():
        assert bs <= set(ga.STATES), a


def test_approved_and_locked_are_reachable_only_through_the_human_path():
    into = {b: {a for a, bs in ga.TRANSITIONS.items() if b in bs} for b in ga.STATES}
    assert into["APPROVED"] == {"APPROVAL_READY"}
    assert into["CANONICAL_LOCKED"] == {"APPROVED"}
    assert into["APPROVAL_READY"] <= {"TESTING", "REVIEW_REQUIRED"}
    assert not ga.allowed_transition("SOURCE_BASELINE", "APPROVED")
    assert not ga.allowed_transition("CHALLENGER", "APPROVAL_READY")
    assert ga.TRANSITIONS["CANONICAL_LOCKED"] == {"REOPEN_REQUIRED"}


def test_three_top_states_stay_distinct():
    assert len({"APPROVAL_READY", "APPROVED", "CANONICAL_LOCKED"} & set(ga.STATES)) == 3
    assert ga.HUMAN_STATES == {"APPROVED", "CANONICAL_LOCKED"}
    assert "APPROVAL_READY" not in ga.HUMAN_STATES


def test_illegal_history_is_flagged():
    e = entry("APPROVED", ["SOURCE_BASELINE", "APPROVED"])
    p = ga.approval_problems("D", e, [record()], APPROVERS, MILESTONES_OK)
    assert any("illegal transition" in x for x in p)


def test_approved_without_record_fails():
    e = entry("APPROVED", APPROVED_PATH, finalization_certificate="cert", approval={"state": "APPROVED", "cycle": 60, "date": "2026-12-01", "by": "corymstover", "record_id": "appr-1"})
    p = ga.approval_problems("D", e, [], APPROVERS, MILESTONES_OK)
    assert any("without a human approval record" in x for x in p)


def test_approved_by_non_human_fails():
    e = entry("APPROVED", APPROVED_PATH, approval={"state": "APPROVED", "cycle": 60, "date": "2026-12-01", "by": "grokbot", "record_id": "appr-1"})
    p = ga.approval_problems("D", e, [record(by="grokbot")], APPROVERS, MILESTONES_OK)
    assert any("not by a human approver" in x for x in p)


def test_approval_record_must_name_the_current_hash():
    e = entry("APPROVED", APPROVED_PATH, approval={"state": "APPROVED", "cycle": 60, "date": "2026-12-01", "by": "corymstover", "record_id": "appr-1"})
    p = ga.approval_problems("D", e, [record(list_hash="lh1:" + "b" * 64)], APPROVERS, MILESTONES_OK)
    assert any("without a human approval record" in x for x in p)


def test_valid_human_approval_passes():
    e = entry("APPROVED", APPROVED_PATH, approval={"state": "APPROVED", "cycle": 60, "date": "2026-12-01", "by": "corymstover", "record_id": "appr-1"})
    assert ga.approval_problems("D", e, [record()], APPROVERS, MILESTONES_OK) == []


def test_locked_needs_a_locking_record_not_just_approval():
    e = entry("CANONICAL_LOCKED", APPROVED_PATH + ["CANONICAL_LOCKED"], approval={"state": "CANONICAL_LOCKED", "cycle": 60, "date": "2026-12-01", "by": "corymstover", "record_id": "appr-1"})
    p = ga.approval_problems("D", e, [record("APPROVED")], APPROVERS, MILESTONES_OK)
    assert any("without a human approval record" in x for x in p)
    assert ga.approval_problems("D", e, [record("CANONICAL_LOCKED")], APPROVERS, MILESTONES_OK) == []


def test_gated_states_need_m2_and_m4_accepted():
    e = entry("APPROVAL_READY", APPROVED_PATH[:-1], finalization_certificate="cert")
    p = ga.approval_problems("D", e, [], APPROVERS, MILESTONES_NOT)
    assert sum("needs milestone" in x for x in p) == 2
    assert ga.approval_problems("D", e, [], APPROVERS, MILESTONES_OK) == []


def test_approval_ready_needs_certificate():
    e = entry("APPROVAL_READY", APPROVED_PATH[:-1])
    p = ga.approval_problems("D", e, [], APPROVERS, MILESTONES_OK)
    assert any("finalization certificate" in x for x in p)


def test_approval_fields_on_unapproved_state_fail():
    e = entry(approval={"state": None, "cycle": None, "date": None, "by": "corymstover", "record_id": "appr-1"})
    assert any("approval fields are set" in x for x in ga.approval_problems("D", e, [], APPROVERS, MILESTONES_NOT))


def test_resolved_ceiling_needs_a_human_and_disagreement_is_flagged_not_overridden():
    e = entry(ceiling={"source_ceiling": {"value": "4"}, "grok_estimated_ceiling": {"value": "5"},
                       "resolved_ceiling": {"value": "5", "resolved_by": "grokbot"}, "disagreement": True})
    p = ga.approval_problems("D", e, [], APPROVERS, MILESTONES_NOT)
    assert any("resolved_ceiling needs resolved_by" in x for x in p)
    e["ceiling"]["disagreement"] = False
    assert any("disagreement must be True" in x for x in ga.approval_problems("D", e, [], APPROVERS, MILESTONES_NOT))


def test_challenger_approval_without_promotion_fails():
    e = entry(challengers=[{"id": "chal:x", "hash": "lh1:" + "c" * 64}])
    p = ga.approval_problems("D", e, [record(list_hash="lh1:" + "c" * 64)], APPROVERS, MILESTONES_NOT)
    assert any("never promoted" in x for x in p)


def test_real_registry_m0_truth():
    reg, appr = load("data/grixis/registry.json"), load("data/grixis/approvals.json")
    states = [e["state"] for e in reg["decks"].values()]
    assert len(states) == 62 and states.count("PENDING_RELEASE") == 2 and states.count("SOURCE_BASELINE") == 60
    assert appr["records"] == []  # nothing approved without Cory
    assert reg["human_approvers"] == ["corymstover"]
    ms = reg["program"]["milestones"]
    for did, e in reg["decks"].items():
        assert ga.approval_problems(did, e, appr["records"], set(reg["human_approvers"]), ms) == [], did
        assert all(h["counts_as"] == "evidence" for h in e["historical_approvals"])
        assert e["ceiling"]["resolved_ceiling"]["value"] is None
        assert set(e["reopen_triggers"]) == set(ga.TRIGGER_KINDS)
        assert e["source_commit"] == "1836b97"
    assert ms["M0"]["status"] in ("complete_pending_acceptance", "accepted")
    assert ms["M0"]["accepted_by"] in (None, "corymstover")
