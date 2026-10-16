"""Bot cycle 60 (M5): candidate universes, triage, escalations, full reviews, exploratory swaps and paired tests."""
import json

from _helpers import ga, skip  # noqa: F401

import grixis_candidates as gc
import grixis_paired as gp


def files():
    fs = sorted(gc.deck_files())
    if not fs:
        skip("candidate files not built")
    return fs


def load(slug):
    if not gc.path_of(slug).exists():
        skip("candidate files not built")
    return gc.load(slug)


def test_every_deck_has_a_recorded_universe():
    """Stored files are capped legacy (Bot cycle 61), checked against the bound each recorded; superseded at M5 regeneration."""
    summ = ga.summary()
    assert set(files()) == {v["slug"] for v in summ.values()}
    for f in files():
        d = load(f)
        u = d["universe"]
        lo, hi = u["bounds"]
        assert lo <= u["size"] == len(d["candidates"]) <= hi
        assert not hasattr(gc, "UNIVERSE_MIN") and not hasattr(gc, "UNIVERSE_MAX")  # no bound in the builder (step A)
        assert u["definition"] and u["sources"] and u["sources_kept"] and d["snapshot"]["id"].startswith("sha256:")
        assert [c["rank"] for c in d["candidates"]] == list(range(1, len(d["candidates"]) + 1))


def test_candidate_records_are_schema_valid_and_escalations_get_full_review():
    d = load("wick-the-whorled-mind")
    for c in d["candidates"]:
        assert ga.validate_file(c, "candidate.schema.json") == []
        assert ga.candidate_problems(c) == []
        assert c["workload"] == {"default_full_review_range": [15, 40], "is_gate": False}
    esc = [c for c in d["candidates"] if c["escalation"]["escalated"]]
    assert esc and all(c["full_review"] and c["escalation"]["evidence_refs"] for c in esc)
    # escalation goes beyond the default range (constraint 3: 15-40 is not a gate)
    assert d["triage"]["screening_reviews"] > d["triage"]["default_full_reviews"]
    assert d["triage"]["escalation_cap"] is None and "escalation_overflow" not in d["triage"]   # Bot cycle 61: no cap
    assert any(c["rank"] > 40 for c in esc)


def test_full_reviews_compare_blueprint_role_graph_and_incumbent():
    d = load("wick-the-whorled-mind")
    lst = {s["card"]: s for s in json.loads((gc.AUDIT / "wick-the-whorled-mind.json").read_text(encoding="utf-8"))["slots"]}
    for c in d["candidates"]:
        if not c["full_review"]:
            continue
        r = c["review"]
        assert {"role", "blueprint", "graph", "best_incumbent", "assessment", "evidence_classes"} <= set(r)
        assert r["kind"] == "screening_review" and r["method"] == "scripted" and r["decision_support"]["can_decide"] is False
        if r["cut"]:
            assert r["cut"] not in r["graph"]["with_incumbents"]       # the cut is not a piece of the combo the add completes
            if r["cut_level"] == "standard":
                assert lst[r["cut"]]["disposition"] not in gc.ELEVATED | {"project_requirement"}


def test_swaps_stay_exploratory_and_unregistered():
    reg = ga.load_json(ga.REGISTRY)
    for f in files():
        d = load(f)
        assert d["authority"]["status"] == "provisional" and d["authority"]["exploratory"] is True
        ch = {x.get("hash") for x in reg["decks"][d["deck_id"]].get("challengers") or []}
        flagged = {c["review"]["swap"] for c in d["candidates"] if c.get("review", {}).get("matches_registered_challenger")}
        for s in d["swaps"]:
            assert s["state"] == "CHALLENGER" and s["exploratory"] and s["decision"]["verdict"] is None
            assert s["base_hash"] == reg["decks"][d["deck_id"]]["canonical_project_list"]["hash"]
            assert s["result_hash"] not in ch or s["id"] in flagged   # a rediscovered registered challenger is flagged, never merged


def test_paired_tests_follow_prereg_and_note_model_limits():
    d = load("wick-the-whorled-mind")
    assert d["tests"]
    for t in d["tests"]:
        assert ga.validate_file(t, "test.schema.json") == []
        assert t["verdict"] == gp.verdict(t["results"])
        assert t["simulator"]["version"] == "1.1" and t["samples"] == gc.SAMPLES
        assert any("cannot see" in x for x in t["limitations"])
    nm = [c["review"]["goldfish"] for c in d["candidates"] if c["full_review"] and c["review"].get("goldfish") and not c["review"]["goldfish"]["test"]]
    assert all(g["not_modelable"].startswith("Not modelable") for g in nm)


def test_tournament_evidence_only_for_cedh_ceiling():
    for f in files():
        d = load(f)
        bp = json.loads((gc.BPS / f"{d['slug']}.json").read_text(encoding="utf-8"))
        ce = bp["power"]["grok_estimated_ceiling"]["value"]["value"]
        assert d["tournament"]["applicable"] == (str(ce) == "5")
        if not d["tournament"]["applicable"]:
            assert not any("tournament" in (c.get("review") or {}) for c in d["candidates"])


def test_no_absolute_protection_but_a_recorded_burden():
    lv = {}
    for slug in files():
        d = load(slug)
        for sw in d["swaps"]:
            lv[sw["burden"]["level"]] = lv.get(sw["burden"]["level"], 0) + 1
            if sw["burden"]["level"] != "standard":
                b = sw["burden"]
                assert b["cleared"] and not b["uncompensated"] and b["tests"]["B1_evidence"] and b["tests"]["B2_compensation"]
                assert "compensated by" in sw["expected_cost"] or not b["breaks"]
    assert lv.get("elevated", 0) > 0   # core / strong-retain / combo pieces can be cut when the burden clears


def test_project_requirements_are_evaluated_and_labeled():
    d = load("bjorna-nightfall-alchemist-cecily")
    pr = {x["card"]: x for x in d["project_requirements"]}
    assert {"Lutri, the Spellchaser"} <= set(pr)
    assert all(x["authorization"].startswith("AUTHORIZED") and "not immune" in x["note"] for x in pr.values())
    assert "Companion" in pr["Lutri, the Spellchaser"]["note"]
    assert sum(x["evaluated_in_reviews"] for x in pr.values() if x["zone"] == "main") > 0


def test_screening_review_never_satisfies_a_decision():
    d = load("wick-the-whorled-mind")
    c = next(x for x in d["candidates"] if x["full_review"])
    assert ga.decision_review_problems(c)                                    # screening only: cannot decide
    sw = dict(next(x for x in d["swaps"] if x["adds"] == [c["card"]]), state="APPROVAL_READY")
    assert ga.swap_decision_problems(sw, {c["card"]: c})                     # a decided swap needs a judgment_review
    fake = dict(c, judgment_review={"kind": "judgment_review", "method": "agent_judgment", "by": "script:grixis_candidates.py",
                                    "date": "2026-10-16", "swaps": [sw["id"]], "verdict": "accept", "reasoning": "x",
                                    "evidence_items": [{"id": "oracle:x", "class": "fact", "confidence": "verified"}]})
    assert ga.decision_review_problems(fake, sw["id"])                       # a script cannot author a judgment review
    ok = dict(fake, judgment_review=dict(fake["judgment_review"], by="Cory", method="human"))
    assert ga.decision_review_problems(ok, sw["id"]) == []
    assert ga.validate_file(ok, "candidate.schema.json") == []
