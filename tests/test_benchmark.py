"""Bot cycle 64.1 (G0): benchmark corpus checker: sealing, leak detection, source existence, holdout rule."""
import copy
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import grixis_benchmark as gb  # noqa: E402


def test_corpus_clean():
    assert gb.problems() == []


def test_prompts_carry_no_outcome_fields_and_every_item_is_sourced():
    c = gb.load(gb.B / "corpus.json")["items"]
    assert len(c) >= 40
    for it in c:
        assert "expected_outcome" not in it and it["sources"]
        assert it["contamination"]["level"] in ("yes", "partial", "no")


def test_leak_detected():
    it = {"id": "g0-x", "prompt": "Is Thraximundar seven mana?"}
    assert gb.leak_problems(it, {"leak_terms": ["seven"], "expected_outcome": "Mana value 7."})
    assert not gb.leak_problems(it, {"leak_terms": ["retract"], "expected_outcome": "Mana value 7."})


def test_source_checks_reject_missing_quote_and_file():
    assert gb.source_problems({"kind": "file", "path": "Update Log.md", "quote": "no such quote xyzzy", "commit": "6ccc5b0"})
    assert gb.source_problems({"kind": "file", "path": "nope.md", "quote": "abcd", "commit": "6ccc5b0"})
    assert gb.source_problems({"kind": "chat", "ref": "t99999u", "recorded_in": "data/grixis/blueprint_reviews.json"})
    assert gb.source_problems({"kind": "chat", "ref": "t50u", "recorded_in": "data/grixis/blueprint_reviews.json"}) == []


def test_historical_corpus_not_claimed_blind():
    c = gb.load(gb.B / "corpus.json")["items"]
    assert not any(i["contamination"]["level"] == "no" for i in c)  # Cory D2: never claim perfect blindness


def test_manifest_records_freeze_rule():
    m = gb.load(gb.B / "manifest.json")
    assert "immutable" in m["freeze_rule"] and m["immutable_from"] == "first commit of step A"
