"""Bot cycle 58 (M1): machine-readable interaction edges (M4 input) and source-attestation coverage."""
import copy
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import grixis_authority as ga  # noqa: E402
import grixis_interactions as gi  # noqa: E402

REVIEWS = gi.load_reviews()
EDGES = {p.stem: json.loads(p.read_text(encoding="utf-8")) for p in sorted(gi.EDGES.glob("*.json"))}
GRAPH = json.loads((ROOT / "data" / "grixis" / "schemas" / "graph.schema.json").read_text(encoding="utf-8"))
GRAPH_EDGE_KINDS = set(GRAPH["properties"]["edges"]["items"]["properties"]["kind"]["enum"])


def test_every_review_has_a_current_schema_valid_edge_file():
    assert set(EDGES) == set(REVIEWS) and len(EDGES) == 62
    schema = ga.load_schema(gi.EDGE_SCHEMA)
    for slug, doc in EDGES.items():
        assert ga.validate(doc, schema, gi.EDGE_SCHEMA) == [], slug
        fresh = gi.build_edges(slug, REVIEWS[slug], (gi.DATA / f"{slug}.json").read_bytes())
        assert gi.edges_text(fresh) == gi.edges_text(doc), f"{slug}: edges stale"
        assert doc["deck_sha256"] == REVIEWS[slug]["deck_sha256"]


def test_every_ruling_has_a_hub_and_membership_for_each_card():
    for slug, doc in EDGES.items():
        hubs = {n["interaction"]: n for n in doc["nodes"] if n["kind"] in ("combo", "interaction")}
        assert set(hubs) == {x["id"] for x in REVIEWS[slug]["interactions"]}
        for x in REVIEWS[slug]["interactions"]:
            mem = [e for e in doc["edges"] if e["interaction"] == x["id"] and e["layer"] == "membership"]
            assert len(mem) == len(dict.fromkeys(x["cards"])), (slug, x["id"])
            assert all(e["to"] == hubs[x["id"]]["id"] for e in mem)


def test_pair_edges_point_at_the_anchor_and_carry_rule_citations():
    n = 0
    for slug, doc in EDGES.items():
        assert doc["counts"]["pair_edges"] >= 1, slug
        by = {x["id"]: x for x in REVIEWS[slug]["interactions"]}
        for e in doc["edges"]:
            x = by[e["interaction"]]
            assert e["cr"] == x.get("cr", [])
            assert e["evidence"][0] == f"review:data/grixis_interactions/{slug}.json#{x['id']}"
            if e["layer"] == "pair":
                n += 1
                assert e["evidence_class"] == "derived_metric" and e["symmetric"]
                if any(c in REVIEWS[slug]["commanders"] for c in x["cards"]):
                    assert e["to"].startswith("commander:")
    assert n > 1000


def test_membership_kinds_are_graph_native_for_m4():
    for doc in EDGES.values():
        for e in doc["edges"]:
            if e["graph_kind"] is not None:
                assert e["graph_kind"] == e["kind"] and e["kind"] in GRAPH_EDGE_KINDS
            else:
                assert e["kind"] in gi.REVIEW_KINDS
            if e["layer"] == "membership":
                assert e["graph_kind"] in ("piece_of", "member_of")


def test_anti_synergy_flags_become_conflicts_with():
    for slug, doc in EDGES.items():
        for x in REVIEWS[slug]["interactions"]:
            if (x.get("flag") or {}).get("kind") == "anti-synergy" and len(set(x["cards"])) > 1:
                ks = {e["kind"] for e in doc["edges"] if e["interaction"] == x["id"] and e["layer"] == "pair"}
                assert ks == {"conflicts_with"}, (slug, x["id"])


def test_authored_edges_replace_pair_edges_and_are_checked():
    slug = "wick-the-whorled-mind"
    d = copy.deepcopy(REVIEWS[slug])
    x = d["interactions"][0]
    x["edges"] = [{"from": x["cards"][1], "to": x["cards"][0], "kind": "fuels"}]
    doc = gi.build_edges(slug, d, b"x")
    mine = [e for e in doc["edges"] if e["interaction"] == x["id"] and e["layer"] != "membership"]
    assert [(e["kind"], e["graph_kind"], e["layer"]) for e in mine] == [("fuels", "fuels", "authored")]
    assert gi.validate_edges(slug, d, doc) == []
    x["edges"] = [{"from": "Black Lotus", "to": x["cards"][0], "kind": "bogus"}]
    bad = gi.validate_edges(slug, d, gi.build_edges(slug, d, b"x"))
    assert any("kind 'bogus'" in b for b in bad) and any("Black Lotus" in b for b in bad)


def test_front_face_names_map_to_the_list_entry():
    doc = EDGES["inalla-archmage-ritualist"]
    ids = {n["id"] for n in doc["nodes"]}
    assert "card:Kefka, Court Mage // Kefka, Ruler of Ruin" in ids and "card:Kefka, Court Mage" not in ids


def test_all_518_source_attestation_items_are_folded_in_or_dispositioned():
    cov, bad = gi.attestation_coverage(REVIEWS)
    assert bad == []
    assert cov["items"] == 518 and cov["missing"] == 0
    assert cov["cited"] + cov["dispositioned"] == 518 and cov["dispositioned"] == 3


def test_disposition_rules_are_enforced(tmp_path, monkeypatch):
    disp = json.loads(gi.DISPOSITIONS.read_text(encoding="utf-8"))
    disp["dispositions"][0]["reason"] = ""
    disp["dispositions"].append({"path": "x.json", "item": "nope", "disposition": "covered_elsewhere", "reason": "r"})
    p = tmp_path / "d.json"
    p.write_text(json.dumps(disp), encoding="utf-8")
    monkeypatch.setattr(gi, "DISPOSITIONS", p)
    _, bad = gi.attestation_coverage(REVIEWS)
    assert any("needs disposition" in b for b in bad) and any("unknown item" in b for b in bad)
    monkeypatch.setattr(gi, "DISPOSITIONS", tmp_path / "missing.json")
    cov, bad = gi.attestation_coverage(REVIEWS)
    assert cov["missing"] == 3 and len(bad) == 3
