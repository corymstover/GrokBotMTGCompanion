"""Bot cycle 59.2 (M4): 99-slot audit (coverage, provisional authority, refs, lint, decision support, baseline)."""
import json

from _helpers import ga, skip  # noqa: F401

import grixis_audit as au


def load(slug):
    f = au.OUT / f"{slug}.json"
    if not f.exists():
        skip("audits not built")
    return json.loads(f.read_text(encoding="utf-8"))


def test_every_deck_audited_and_every_slot_covered():
    summ = ga.summary()
    assert {f.stem for f in au.OUT.glob("*.json")} == {v["slug"] for v in summ.values()}
    for did, v in sorted(summ.items())[:8]:
        d = load(v["slug"])
        assert ga.validate_file(d, "audit.schema.json") == []
        g = json.loads((au.GRAPH / f"{v['slug']}.json").read_text(encoding="utf-8"))
        main = {x["name"] for x in g["nodes"] if x["kind"] == "card" and x["zone"] == "main"}
        assert {s["card"] for s in d["slots"] if s["zone"] == "main"} == main
        assert d["slot_total"] == 100 - sum(1 for x in g["nodes"] if x["kind"] == "commander")


def test_nothing_is_authoritative_while_m2_is_not_accepted():
    reg = ga.load_json(ga.REGISTRY)
    assert reg["program"]["milestones"]["M2"]["status"] != "accepted"
    for f in au.OUT.glob("*.json"):
        d = json.loads(f.read_text(encoding="utf-8"))
        assert d["authority"]["status"] == "provisional"
        assert all(s["review_status"] == "provisional" and s["classifier"] == "script" for s in d["slots"])


def test_complete_eligibility_follows_disposition_status():
    d = load("wick-the-whorled-mind")
    for s in d["slots"]:
        assert s["complete_eligible"] == (ga.disposition_status(s) == "complete")
        if s["complete_eligible"]:
            assert s["blueprint_refs"] and s["graph_refs"] and s["alternatives"]
    # a slot with only heuristic support cannot decide
    s = next(x for x in d["slots"] if set(x["evidence_classes"]) <= {"fact", "heuristic", "derived_metric"} and not x["blueprint_refs"] and not any(r.startswith("spellbook:") for r in x["evidence"]))
    assert s["decision_support"]["ok"] is False


def test_rules_on_known_cards():
    d = load("wick-the-whorled-mind")
    by = {s["card"]: s for s in d["slots"]}
    assert by["Arcane Adaptation"]["disposition"] == "core"            # identity core, breaks the type-changer package
    assert by["Altar of Dementia"]["disposition"] == "strong_retain"   # Spellbook piece with interchangeable outlets
    assert by["Swamp"]["disposition"] == "flexible"
    b = load("bjorna-nightfall-alchemist-cecily")
    assert {s["card"] for s in b["slots"] if s["disposition"] == "project_requirement"} >= {"Lutri, the Spellchaser"}
    assert b["counts"]["companion"] == ["Lutri, the Spellchaser"]


def test_boilerplate_lint_and_baseline():
    for f in au.OUT.glob("*.json"):
        d = json.loads(f.read_text(encoding="utf-8"))
        assert d["lint"]["ok"] and d["lint"]["max_duplicate"] <= au.LINT_MAX_DUP
        assert au.lint_reasons(d["slots"]) == d["lint"]
        b = d["baseline_sim"]
        assert b["class"] == "test_result" and b["samples"] == au.BASE_SAMPLES and "win_rate" not in json.dumps(b["metrics"])


def test_lint_catches_duplicates():
    slots = [{"card": f"C{i}", "reason": "same text"} for i in range(au.LINT_MAX_DUP + 1)]
    assert au.lint_reasons(slots)["ok"] is False


def test_check_passes():
    if not (au.ROOT / ".cache").exists():
        skip("no .cache")
    assert au.check(verbose=False, rebuild=False) == []
