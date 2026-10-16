"""Logical (lh1) vs raw list hashes (brief §19)."""
from _helpers import FakeR, ga, load, resolver, ROOT


def test_logical_hash_ignores_order_tags_and_layout():
    a = "1x Alpha [Commander{top}]\n1x Beta [Draw]\n2 Island\n"
    b = "2x Island [Land]\n1 Beta\n1x Alpha [Commander]\n"
    assert ga.text_hash(a, FakeR()) == ga.text_hash(b, FakeR())
    assert ga.text_hash(a, FakeR()).startswith("lh1:")


def test_raw_hash_sees_bytes_logical_does_not():
    a, b = "1x Alpha [Commander]\n1x Beta\n", "1x Alpha [Commander]\n1x Beta  \n"
    assert ga.raw_hash(a) != ga.raw_hash(b)
    assert ga.raw_hash(a).startswith("sha256:")
    assert ga.text_hash(a, FakeR()) == ga.text_hash(b, FakeR())


def test_quantities_are_summed_and_zone_matters():
    split = ga.logical_hash([("main", "x", 1), ("main", "x", 1)])
    assert split == ga.logical_hash([("main", "x", 2)])
    assert ga.logical_hash([("main", "x", 1)]) != ga.logical_hash([("companion", "x", 1)])
    assert ga.logical_hash([("main", "x", 1)]) != ga.logical_hash([("main", "x", 2)])


def test_bad_zone_and_unresolved_cards_raise():
    for bad in ([("sideboard", "x", 1)], [("main", None, 1)]):
        try:
            ga.logical_hash(bad)
        except ValueError:
            continue
        raise AssertionError(f"accepted {bad}")
    try:
        ga.text_hash("1x Unknown Card\n", FakeR())
    except ValueError:
        pass
    else:
        raise AssertionError("unresolved card hashed")


def test_hash_definition_documents_both():
    reg = load("data/grixis/registry.json")
    hd = reg["hash_definition"]
    assert "lh1" in hd["logical"] and "SHA-256 of the file bytes" in hd["raw"] and "mixed" in hd["note"]


def test_registry_hashes_match_deck_pages_and_exports():
    """Integration: every canonical hash recomputes from its deck page; index.json hashes match the files."""
    R = resolver()
    reg = load("data/grixis/registry.json")
    for did, e in reg["decks"].items():
        assert e["current_canonical_hash"] == ga.text_hash(ga.deck_block_text(e["slug"]), R), did
        exp = ROOT / e["canonical_project_list"]["export"]
        assert ga.text_hash(exp.read_text(encoding="utf-8"), R) == e["current_canonical_hash"], did
    man = load("exports/grixis-archidekt/index.json")
    for x in man["files"]:
        data = (ROOT / "exports" / "grixis-archidekt" / x["file"]).read_bytes()
        assert ga.raw_hash(data) == x["raw_sha256"], x["file"]
        assert ga.text_hash(data.decode("utf-8"), R) == x["list_hash"], x["file"]


def test_source_recorded_hash_mismatch_is_recorded_not_hidden():
    reg = load("data/grixis/registry.json")
    mism = [d for d, e in reg["decks"].items() if e["source"]["recorded_matches_raw"] is False]
    assert len(mism) >= 2  # the source's logical-vs-raw confusion (see hash_definition.note)
