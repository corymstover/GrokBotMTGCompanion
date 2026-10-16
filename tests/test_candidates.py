"""Bot cycle 60 (M5): candidate universes, triage, escalations, full reviews, exploratory swaps and paired tests."""
import json

from _helpers import ga, skip  # noqa: F401

import grixis_candidates as gc
import grixis_paired as gp


def files():
    fs = [f for f in gc.OUT.glob("*.json") if f.stem != "spellbook_almost"]
    if not fs:
        skip("candidate files not built")
    return fs


def load(slug):
    f = gc.OUT / f"{slug}.json"
    if not f.exists():
        skip("candidate files not built")
    return json.loads(f.read_text(encoding="utf-8"))


def test_every_deck_has_a_bounded_recorded_universe():
    summ = ga.summary()
    assert {f.stem for f in files()} == {v["slug"] for v in summ.values()}
    for f in files():
        d = json.loads(f.read_text(encoding="utf-8"))
        u = d["universe"]
        assert gc.UNIVERSE_MIN <= u["size"] == len(d["candidates"]) <= gc.UNIVERSE_MAX
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
    assert d["triage"]["full_reviews"] > d["triage"]["default_full_reviews"]
    assert any(c["rank"] > 40 for c in esc)


def test_full_reviews_compare_blueprint_role_graph_and_incumbent():
    d = load("wick-the-whorled-mind")
    lst = {s["card"]: s for s in json.loads((gc.AUDIT / "wick-the-whorled-mind.json").read_text(encoding="utf-8"))["slots"]}
    for c in d["candidates"]:
        if not c["full_review"]:
            continue
        r = c["review"]
        assert {"role", "blueprint", "graph", "best_incumbent", "assessment", "evidence_classes"} <= set(r)
        if r["cut"]:
            assert lst[r["cut"]]["disposition"] not in gc.PROTECTED   # core / strong retain / project requirements are never the cut
            assert r["cut"] not in r["graph"]["with_incumbents"]       # the cut is not a piece of the combo the add completes


def test_swaps_stay_exploratory_and_unregistered():
    reg = ga.load_json(ga.REGISTRY)
    for f in files():
        d = json.loads(f.read_text(encoding="utf-8"))
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
        d = json.loads(f.read_text(encoding="utf-8"))
        bp = json.loads((gc.BPS / f"{d['slug']}.json").read_text(encoding="utf-8"))
        ce = bp["power"]["grok_estimated_ceiling"]["value"]["value"]
        assert d["tournament"]["applicable"] == (str(ce) == "5")
        if not d["tournament"]["applicable"]:
            assert not any("tournament" in (c.get("review") or {}) for c in d["candidates"])
