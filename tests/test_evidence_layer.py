"""Bot cycle 57 (M3): evidence layer (EDHREC aggregation, classes/confidence, lift identity, snapshot keys, items)."""
import copy
import json

from _helpers import ga, skip

import grixis_evidence as ge


def view(n, pd, syn, lift, tz=0.0, name="X"):
    return {"name": name, "num_decks": n, "potential_decks": pd, "synergy": syn, "lift": lift, "trend_zscore": tz}


def test_single_page_row_and_identity():
    # inclusion 0.5, baseline 0.1 -> synergy 0.4, lift 5.0: the identity holds
    r = ge.edh_dict(ge.edh_row([view(500, 1000, 0.4, 5.0)], "single_page"))
    assert r["inclusion"] == 0.5 and r["confidence"] == "moderate" and r["flags"] == []
    assert ge.lift_identity(r["lift"], r["synergy"], r["inclusion"]) < 1e-9


def test_inconsistent_lift_is_flagged_low():
    r = ge.edh_dict(ge.edh_row([view(500, 1000, 0.4, 3.0)], "single_page"))
    assert "lift_synergy_inconsistent" in r["flags"] and r["confidence"] == "low"


def test_small_sample_and_trend_flags():
    r = ge.edh_dict(ge.edh_row([view(10, 40, 0.15, 1.6, tz=2.5)], "single_page"))
    assert "small_sample" in r["flags"] and "rising" in r["flags"] and r["confidence"] == "low"
    r = ge.edh_dict(ge.edh_row([view(400, 1000, 0.1, 4 / 3, tz=-2.0)], "single_page"))
    assert "falling" in r["flags"]


def test_pooling_sums_counts_and_weights_rates():
    r = ge.edh_dict(ge.edh_row([view(100, 1000, 0.05, 1.5, 1.0), view(300, 3000, 0.09, 2.0, -1.0)], "pooled"))
    assert r["num_decks"] == 400 and r["potential_decks"] == 4000 and abs(r["inclusion"] - 0.1) < 1e-9
    assert abs(r["synergy"] - 0.08) < 1e-9 and abs(r["lift"] - 1.875) < 1e-9 and abs(r["trend_zscore"] + 0.5) < 1e-9
    assert "pooled" in r["flags"] and r["confidence"] == "low"  # different populations: never above low
    one = ge.edh_dict(ge.edh_row([view(500, 1000, 0.4, 5.0)], "pooled"))
    assert "one_page_of_pool" in one["flags"] and one["confidence"] == "low"


def test_edhrec_never_above_moderate():
    for n, pd in ((5000, 6000), (100, 100), (1, 60)):
        r = ge.edh_dict(ge.edh_row([view(n, pd, 0.1, 1.2)], "single_page"))
        assert r["confidence"] in ("moderate", "low")


def _doc():
    files = sorted(ge.OUT.glob("*.json"))
    if not files:
        skip("no evidence files built")
    return json.loads(files[0].read_text(encoding="utf-8"))


def test_items_validate_against_evidence_schema():
    doc = _doc()
    n = 0
    for r in doc["vectors"][:80]:
        for it in ge.items(doc, r):
            assert not ga.validate_file(it, "evidence.schema.json"), it
            assert it["class"] in ("fact", "derived_metric", "heuristic", "strategic_judgment")
            n += 1
    assert n > 0


def test_derived_and_heuristic_items_alone_do_not_decide():
    doc = _doc()
    its = [it for r in doc["vectors"] for it in ge.items(doc, r) if it["class"] in ("derived_metric", "heuristic")][:5]
    if not its:
        skip("no derived/heuristic items")
    ok, why = ga.decision_support_ok(its)
    assert not ok and any("diagnostics cannot decide" in w for w in why)


def test_vector_schema_rejects_bad_rows():
    doc = _doc()
    assert not ga.validate_file(doc, "evidence_vector.schema.json")
    bad = copy.deepcopy(doc)
    bad["vectors"][0]["edhrec"] = [1.0, 0.1]
    assert ga.validate_file(bad, "evidence_vector.schema.json")
    bad = copy.deepcopy(doc)
    bad["edhrec"]["class"] = "fact"
    assert ga.validate_file(bad, "evidence_vector.schema.json")


def test_snapshot_id_changes_with_inputs():
    a = ge.sha_text(json.dumps({"x": "sha256:1"}, sort_keys=True) + ge.VERSION)
    b = ge.sha_text(json.dumps({"x": "sha256:2"}, sort_keys=True) + ge.VERSION)
    assert a != b
