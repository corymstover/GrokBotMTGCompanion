"""Bot cycle 62: Cory's 8-blueprint review (t50u) and its corrections; M2/M4 stay unaccepted."""
import copy

import _helpers  # noqa: F401  (sys.path)
from _helpers import ga
import grixis_blueprints as gb

EIGHT = {"parnesse-the-subtle-brush", "solkanar-the-swamp-king", "bjorna-nightfall-alchemist-cecily", "thraximundar",
         "tresserhorns-lord-returned", "the-madcap-jester", "wick-the-whorled-mind", "mairsil-the-pretender"}


def test_exactly_the_eight_are_cory_reviewed_and_m2_m4_not_accepted():
    bps = gb.load_all()
    assert {s for s, b in bps.items() if b["status"] == "cory_reviewed"} == EIGHT
    reg = ga.load_json(ga.REGISTRY)
    for s in EIGHT:
        assert gb.review_problems(bps[s], reg) == [] and bps[s]["provenance"]["reviewed_by"] == "corymstover"
    ms = reg["program"]["milestones"]
    assert all(ms[m]["status"] != "accepted" for m in ("M2", "M4", "M5"))
    bad = copy.deepcopy(bps["wick-the-whorled-mind"]); bad["cory_review"]["ceiling"] = "5"
    assert gb.review_problems(bad, reg)


def test_corrections_applied():
    bps = gb.load_all()
    th = bps["thraximundar"]
    assert not any(k["id"] == "mana-value-six" for k in th["key_interactions"]) and "Source error" not in th["commander_role"]["value"]["honest_note"]
    pk = {k["id"]: k for k in bps["parnesse-the-subtle-brush"]["key_interactions"]}["retargeted-copy-tax"]
    assert pk["confidence"] == "verified" and pk["evidence_class"] == "approved_decision"
    assert "hasty" not in {w["id"]: w for w in bps["parnesse-the-subtle-brush"]["win_conditions"]}["dualcaster-tech"]["description"].replace("not inherently hasty", "")
    mk = {k["id"]: k for k in bps["mairsil-the-pretender"]["key_interactions"]}["marvin"]
    assert mk["confidence"] != "test_required" and "cr:113.10a" in mk["evidence"]
    sol = bps["solkanar-the-swamp-king"]
    assert "Aetherflux Reservoir" not in {w["id"]: w for w in sol["win_conditions"]}["life-loops"]["cards"]
    bj = bps["bjorna-nightfall-alchemist-cecily"]
    assert "clearing Cecily" not in bj["plan"]["value"]["secondary"]
    for s in ("tresserhorns-lord-returned", "the-madcap-jester"):
        assert bps[s]["project_exceptions"]["future_release"]
    mj = bps["the-madcap-jester"]
    assert {"Thassa's Oracle", "Underworld Breach"} <= {c["card"] for c in mj["power_core"]}
    assert not {"Thassa's Oracle", "Underworld Breach"} & {c["card"] for c in mj["identity_core"]}
    assert {"graveyard-hate", "oracle-line-hate"} <= {f["id"] for f in mj["failure_modes"]}


def test_no_generic_compact_win_in_identity_core():
    for s, b in gb.load_all().items():
        cw = [c["name"].split(",")[0].split(" ")[0] for c in b["commanders"]["value"]]
        assert not [x for x in b["identity_core"] if x["card"] in gb.GENERIC_COMPACT_WINS and not any(w in x["why"] for w in cw)], s


def test_m1_corrections_overlay():
    c = gb.m1_corrections()
    assert c["parnesse-10"]["corrected_status"] == "verified" and c["parnesse-10"]["source"] == "Cory review + derivation"
    assert c["mairsil-10"]["corrected_status"] == "resolved_hypothesis_incorrect"
    assert any(d["cr"] == "113.10a" and "become part of the ability" in d["quote"] for d in c["mairsil-10"]["derivation"])
