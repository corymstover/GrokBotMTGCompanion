"""Bot cycle 50 (M2): commander blueprint validation (schema v2, Oracle facts, card refs, evidence, class rules, ceilings)."""
import copy
import json
import tempfile
from pathlib import Path

from _helpers import ROOT, ga, skip

import grixis_blueprints as gb

SLUG = "abaddon-the-despoiler"
_CTX = []


def ctx():
    if not _CTX:
        if not (gb.BP / f"{SLUG}.json").exists():
            skip("no blueprint for the fixture deck")
        crs = sorted((ROOT / ".cache").glob("MagicCompRules-*.txt"))
        if not crs:
            skip("no cached Comprehensive Rules")
        try:
            gb.R()
        except Exception as e:  # noqa: BLE001
            skip(f"no Scryfall cache: {e}")
        _CTX.append((ga.summary(), ga.load_json(ga.REGISTRY), crs[-1].read_text(encoding="utf-8", errors="ignore")))
    return _CTX[0]


def base():
    return json.loads((gb.BP / f"{SLUG}.json").read_text(encoding="utf-8"))


def problems(bp):
    summ, reg, cr = ctx()
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / f"{bp.get('slug', SLUG)}.json"
        p.write_text(json.dumps(bp), encoding="utf-8")
        return gb.check_one(p, summ, reg, cr)[0]


def has(probs, text):
    return any(text in x for x in probs)


def test_all_written_blueprints_pass():
    summ, reg, cr = ctx()
    bad = {}
    for p in sorted(gb.BP.glob("*.json")):
        pr = gb.check_one(p, summ, reg, cr)[0]
        if pr:
            bad[p.name] = pr[:3]
    assert not bad, bad


def test_fixture_is_clean():
    assert problems(base()) == []


def test_every_field_needs_evidence():
    bp = base()
    bp["plan"]["evidence"] = []
    assert has(problems(bp), "schema")
    bp = base()
    del bp["win_conditions"][0]["evidence_class"]
    assert has(problems(bp), "schema")
    bp = base()
    del bp["requirements"]
    assert has(problems(bp), "schema")


def test_oracle_text_must_match_cache():
    bp = base()
    bp["commanders"]["value"][0]["oracle_text"] += " (once each turn)"
    assert has(problems(bp), "Oracle text/type/sha differs")


def test_commander_facts_must_be_verified_oracle():
    bp = base()
    bp["commanders"]["confidence"] = "high"
    assert has(problems(bp), "must cite oracle: refs with confidence verified")


def test_card_refs_in_list_or_declared_candidates():
    bp = base()
    bp["identity_core"][1]["card"] = "Aurora Phoenix"
    assert has(problems(bp), "is not in the canonical list")
    bp = base()
    bp["packages"][0]["candidates"] = ["Boltwave"]
    assert has(problems(bp), "already in the list")
    bp = base()
    bp["packages"][0]["candidates"] = ["Llanowar Elves"]
    assert has(problems(bp), "not Commander-legal inside the color identity")
    bp = base()
    bp["packages"][0]["candidates"] = ["Not A Real Card Name Zzz"]
    assert has(problems(bp), "does not resolve exactly")


def test_required_package_min_count():
    bp = base()
    bp["packages"][0]["min_count"] = 99
    assert has(problems(bp), "required min_count 99")


def test_evidence_class_rules():
    bp = base()
    bp["plan"]["evidence_class"] = "fact"
    assert has(problems(bp), "plan: evidence_class fact not allowed")
    bp = base()
    bp["power"]["grok_estimated_ceiling"]["evidence_class"] = "derived_metric"
    assert has(problems(bp), "power.grok_estimated_ceiling: evidence_class")
    bp = base()
    bp["power"]["edhrec"]["evidence_class"] = "strategic_judgment"
    assert has(problems(bp), "power.edhrec: evidence_class")
    bp = base()
    bp["supporting_features"]["evidence_class"] = "fact"
    assert has(problems(bp), "supporting_features: evidence_class")


def test_evidence_refs_must_resolve():
    bp = base()
    bp["plan"]["evidence"] = ["interaction:abaddon-the-despoiler#abaddon-999"]
    assert has(problems(bp), "no such M1 interaction")
    bp = base()
    bp["plan"]["evidence"] = ["source_archive:refinement/blueprints/Abaddon_the_Despoiler_v1.md#L99999"]
    assert has(problems(bp), "bad line anchor")
    bp = base()
    bp["plan"]["evidence"] = ["cr:999.9z"]
    assert has(problems(bp), "not in the cached CR")
    bp = base()
    bp["plan"]["evidence"] = ["spellbook:0-0-0"]
    assert has(problems(bp), "not in this deck's Spellbook results")
    bp = base()
    bp["plan"]["evidence"] = ["vibes:trust me"]
    assert has(problems(bp), "unknown evidence ref kind")
    bp = base()
    bp["key_interactions"][0]["m1_refs"] = ["abaddon-999"]
    assert has(problems(bp), "M1 id abaddon-999 not found")


def test_resolved_ceiling_stays_null_and_disagreement_consistent():
    bp = base()
    bp["power"]["resolved_ceiling"] = "4"
    assert has(problems(bp), "schema")
    bp = base()
    bp["power"]["grok_estimated_ceiling"]["value"]["value"] = "3"
    assert has(problems(bp), "power.disagreement must be True")
    bp["power"]["disagreement"] = True
    assert not has(problems(bp), "power.disagreement")


def test_source_ceiling_matches_registry_and_recovery_needs_line():
    bp = base()
    bp["power"]["source_ceiling"]["value"]["value"] = "3"
    assert has(problems(bp), "registry source ceiling")
    rec = json.loads((gb.BP / "ashnod-the-uncaring.json").read_text(encoding="utf-8")) if (gb.BP / "ashnod-the-uncaring.json").exists() else None
    if rec:
        rec["power"]["source_ceiling"]["evidence"] = ["source_archive:refinement/blueprints/Ashnod_the_Uncaring_v1.md"]
        assert has(problems(rec), "must cite source_archive:<file>#L<line>")


def test_review_status_needs_human():
    bp = base()
    bp["status"] = "cory_reviewed"
    assert has(problems(bp), "needs provenance.reviewed_by")
    bp["provenance"]["reviewed_by"] = "corymstover"
    assert not has(problems(bp), "reviewed_by")
    bp = base()
    bp["provenance"]["reviewed_by"] = "corymstover"
    assert has(problems(bp), "status is not cory_reviewed")


def test_boilerplate_reasons_flagged():
    bp = base()
    bp["identity_core"][2]["why"] = bp["identity_core"][1]["why"]
    assert has(problems(bp), "boilerplate reason repeated")


def test_project_exceptions_match_registry():
    bp = base()
    bp["project_exceptions"]["value"] = ["Sol Ring"]
    assert has(problems(bp), "exception registry")


def test_m2_status_is_not_met_until_cory():
    _, reg, _ = ctx()
    crit = gb.m2_status(gb.load_all(), reg)
    assert len(crit) == 5
    assert crit[3][1] and not crit[4][1]  # Bot cycle 62: Cory reviewed his 8-blueprint sample (t50u); M2 not accepted
    fake = copy.deepcopy(reg)
    fake["program"]["milestones"]["M2"].update(status="accepted", accepted_by="corymstover")
    assert gb.m2_status({}, fake)[4][1]


def test_milestone_acceptance_rules():
    ok = {"status": "accepted", "accepted_by": "corymstover", "accepted_date": "2026-10-16", "acceptance_evidence": "chat", "criteria_doc": "x"}
    assert ga.milestone_problems({"M0": ok}, {"corymstover"}) == []
    assert ga.milestone_problems({"M0": dict(ok, accepted_by="grokbot")}, {"corymstover"})
    assert ga.milestone_problems({"M0": dict(ok, acceptance_evidence=None)}, {"corymstover"})
    assert ga.milestone_problems({"M2": {"status": "in_progress", "accepted_by": "corymstover", "accepted_date": None, "criteria_doc": "x"}}, {"corymstover"})


def test_registry_records_m0_acceptance_and_approves_no_decks():
    reg = ga.load_json(ga.REGISTRY)
    m0 = reg["program"]["milestones"]["M0"]
    assert m0["status"] == "accepted" and m0["accepted_by"] == "corymstover" and m0["accepted_at"] == "2026-10-16T10:52Z"
    assert not any(e["state"] in ("APPROVED", "CANONICAL_LOCKED", "APPROVAL_READY") for e in reg["decks"].values())
