"""JSON Schemas: the stdlib validator, the real data files, negative cases, and a jsonschema cross-check when installed."""
import copy
import json

from _helpers import ROOT, ga, load, skip

DATA_FILES = (("data/grixis/registry.json", "registry.schema.json"), ("data/grixis/exceptions.json", "exception.schema.json"),
              ("data/grixis/approvals.json", "approval.schema.json"), ("data/grixis_refine_v2.json", "refine_v2.schema.json"))


def test_every_schema_has_schema_and_id():
    files = sorted(ga.SCHEMAS.glob("*.schema.json"))
    assert len(files) >= 14
    for f in files:
        s = json.loads(f.read_text(encoding="utf-8"))
        assert s["$schema"].startswith("https://json-schema.org/") and s["$id"].endswith("/" + f.name), f.name


def test_data_files_validate():
    for rel, sch in DATA_FILES:
        assert ga.validate_file(load(rel), sch) == [], rel


def test_registry_negative_cases():
    reg = load("data/grixis/registry.json")
    bj = "Cecily__Bjorna__Lutri"
    bad = copy.deepcopy(reg)
    bad["decks"][bj]["official_legal_projection"]["canonical"] = True
    assert ga.validate_file(bad, "registry.schema.json")
    bad = copy.deepcopy(reg)
    bad["decks"][bj]["official_legal_projection"]["label"] = "official list"
    assert ga.validate_file(bad, "registry.schema.json")
    bad = copy.deepcopy(reg)
    d = next(e for e in bad["decks"].values() if e["challengers"])
    d["challengers"][0]["label"] = "GrokBot final"
    assert ga.validate_file(bad, "registry.schema.json")
    bad = copy.deepcopy(reg)
    next(iter(bad["decks"].values()))["state"] = "FINAL"
    assert ga.validate_file(bad, "registry.schema.json")
    bad = copy.deepcopy(reg)
    next(iter(bad["decks"].values()))["current_canonical_hash"] = "sha256:" + "0" * 64
    assert ga.validate_file(bad, "registry.schema.json")


def test_exception_negative_case():
    exc = load("data/grixis/exceptions.json")
    exc["exceptions"][0]["project_authorization_status"] = "LEGAL"
    assert ga.validate_file(exc, "exception.schema.json")


def test_workload_is_never_a_gate_and_dispositions_need_status():
    cand = {"schema_version": 1, "deck_id": "D", "card": "X", "oracle_id": "o", "rank": 50, "tier": "screened", "full_review": True,
            "escalation": {"escalated": True, "reasons": ["new_card"], "evidence_refs": ["oracle:X"], "by": "grokbot", "note": ""},
            "evidence": [], "workload": {"default_full_review_range": [15, 40], "is_gate": False}}
    base = ga.validate_file(cand, "candidate.schema.json")
    bad = copy.deepcopy(cand)
    bad["workload"]["is_gate"] = True
    assert len(ga.validate_file(bad, "candidate.schema.json")) > len(base)
    bad = copy.deepcopy(cand)
    bad["escalation"]["reasons"] = ["vibes"]
    assert len(ga.validate_file(bad, "candidate.schema.json")) > len(base)


def test_validator_core_keywords():
    s = {"type": "object", "required": ["a"], "additionalProperties": False,
         "properties": {"a": {"type": "integer", "minimum": 1}, "b": {"enum": ["x"]}, "c": {"type": "array", "items": {"type": "string"}, "minItems": 1}}}
    assert ga.validate({"a": 2, "b": "x", "c": ["q"]}, s) == []
    assert ga.validate({"a": 0}, s) and ga.validate({}, s) and ga.validate({"a": 1, "z": 1}, s)
    assert ga.validate({"a": True}, s)  # bool is not an integer
    assert ga.validate({"a": 1, "c": []}, s) and ga.validate({"a": 1, "b": "y"}, s)


def test_cross_check_with_jsonschema():
    try:
        import jsonschema
        from referencing import Registry, Resource
    except ImportError:
        skip("jsonschema/referencing not installed (the stdlib validator is authoritative)")
    res = []
    for f in ga.SCHEMAS.glob("*.schema.json"):
        s = json.loads(f.read_text(encoding="utf-8"))
        res.append((s["$id"], Resource.from_contents(s)))
    reg = Registry().with_resources(res)
    for rel, sch in DATA_FILES:
        s = json.loads((ga.SCHEMAS / sch).read_text(encoding="utf-8"))
        v = jsonschema.Draft202012Validator(s, registry=reg)
        errs = sorted(v.iter_errors(load(rel)), key=str)
        assert not errs, (rel, str(errs[0])[:300] if errs else "")
        jsonschema.Draft202012Validator.check_schema(s)
    bad = load("data/grixis/registry.json")
    next(iter(bad["decks"].values()))["state"] = "FINAL"
    s = json.loads((ga.SCHEMAS / "registry.schema.json").read_text(encoding="utf-8"))
    assert list(jsonschema.Draft202012Validator(s, registry=reg).iter_errors(bad))
