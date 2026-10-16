"""Bot cycle 59.1 (M4): per-deck dependency graph (schema, structure metrics, Spellbook substitution, M1 edges ingest)."""
import json
import hashlib

from _helpers import ga, skip  # noqa: F401

import grixis_graph as gg


def load(slug):
    f = gg.OUT / f"{slug}.json"
    if not f.exists():
        skip("graphs not built")
    return json.loads(f.read_text(encoding="utf-8"))


def test_every_deck_has_a_valid_graph_covering_its_list():
    summ = ga.summary()
    reg = ga.load_json(ga.REGISTRY)["decks"]
    assert {f.stem for f in gg.OUT.glob("*.json")} == {v["slug"] for v in summ.values()}
    for did, v in sorted(summ.items())[:6]:
        d = load(v["slug"])
        assert ga.validate_file(d, "graph.schema.json") == []
        assert d["list_hash"] == reg[ga.registry_id(did)]["canonical_project_list"]["hash"]
        names = {x["name"] for x in d["nodes"] if x["kind"] in ("card", "commander")}
        assert set(d["metrics"]) == names
        ids = {x["id"] for x in d["nodes"]}
        assert all(e["from"] in ids and e["to"] in ids and e["evidence"] for e in d["edges"])


def test_combo_pieces_break_their_combos_and_substitutes_are_detected():
    d = load("wick-the-whorled-mind")
    combos = {x["name"]: x for x in d["nodes"] if x["kind"] == "combo" and ":" not in x["name"]}
    pieces = {}
    for e in d["edges"]:
        if e["layer"] == "spellbook" and e["kind"] == "piece_of":
            pieces.setdefault(e["to"], set()).add(e["from"].split(":", 1)[1])
    assert len(pieces) == len(combos) == 13
    for cid, ps in pieces.items():
        for n in ps:
            assert cid in d["metrics"][n]["breaks_if_removed"]
    # Arcane Adaptation and Leyline of Transformation are interchangeable in Spellbook combos (same other pieces)
    assert "Leyline of Transformation" in d["metrics"]["Arcane Adaptation"]["interchangeable_with"]
    assert any(e["kind"] == "redundant_with" and {e["from"], e["to"]} == {"card:Arcane Adaptation", "card:Leyline of Transformation"} for e in d["edges"])


def test_necessity_rules():
    d = load("wick-the-whorled-mind")
    m = d["metrics"]
    assert m["Wick, the Whorled Mind"]["structural_necessity"] == "necessary"
    for n, x in m.items():
        assert x["structural_necessity"] in gg.NECESSITY
        if x["necessity_reasons"]:
            assert x["structural_necessity"] == "necessary"
        if x["breaks_if_removed"] and x["structural_necessity"] not in ("necessary", "important"):
            raise AssertionError(f"{n} breaks {x['breaks_if_removed']} but is {x['structural_necessity']}")
        assert isinstance(x["redundancy"], int) and x["redundancy"] >= 0
    assert d["metrics"]["Swamp"]["structural_necessity"] == "redundant"


def test_edges_carry_classes_by_layer():
    d = load("wick-the-whorled-mind")
    for e in d["edges"]:
        if e["layer"] == "role":
            assert e["evidence_class"] in ("heuristic", "derived_metric")
        if e["layer"] == "spellbook" and e["kind"] == "piece_of":
            assert e["evidence_class"] == "fact" and e["evidence"][0].startswith("spellbook:")
        if e["layer"] == "blueprint":
            assert any(r.startswith("blueprint:") for r in e["evidence"])


def test_m1_ingest_is_read_only_and_degrades_gracefully(tmp_path=None):
    import tempfile
    from pathlib import Path
    tmp = Path(tmp_path or tempfile.mkdtemp())
    old = gg.EDGES
    try:
        gg.EDGES = tmp / "edges"
        reg = ga.load_json(ga.REGISTRY)["decks"]
        e = next(v for v in reg.values() if v["slug"] == "wick-the-whorled-mind")
        export = gg.ROOT / e["canonical_project_list"]["export"]
        review = gg.INTER / "wick-the-whorled-mind.json"
        d, st, _ = gg.m1_status("wick-the-whorled-mind", export, review)
        assert d is None and st == "absent"
        gg.EDGES.mkdir()
        fake = {"schema_version": 1, "deck_sha256": "0" * 64, "review_sha256": hashlib.sha256(review.read_bytes()).hexdigest(), "nodes": [], "edges": []}
        (gg.EDGES / "wick-the-whorled-mind.json").write_text(json.dumps(fake), encoding="utf-8")
        d, st, _ = gg.m1_status("wick-the-whorled-mind", export, review)
        assert d is None and st in ("stale_list", "invalid")  # invalid once interaction_edges.schema.json is on main
    finally:
        gg.EDGES = old


def test_check_passes():
    if not (gg.ROOT / ".cache").exists():
        skip("no .cache")
    assert gg.check(verbose=False, rebuild=False) == []
