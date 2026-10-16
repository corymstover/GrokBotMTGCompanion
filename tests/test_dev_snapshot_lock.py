"""Bot cycle 66.3b: the frozen dev snapshot lock refuses bulk fetches and validate_all detects a drifted cache."""
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import ingest_scryfall as ing  # noqa: E402
import check_dev_snapshot_lock as chk  # noqa: E402


def _setup(tmp_path, monkeypatch, present=True):
    cache = tmp_path / "cache"
    cache.mkdir()
    if present:
        (cache / "oracle-cards-20261016090200.jsonl").write_text('{"name": "Island"}\n')
    lock = tmp_path / "lock.json"
    import hashlib
    sha = "sha256:" + hashlib.sha256((cache / "oracle-cards-20261016090200.jsonl").read_bytes()).hexdigest() if present else "x"
    lock.write_text(json.dumps({"files": {"oracle-cards": "oracle-cards-20261016090200.jsonl"}, "sha256": {"oracle-cards": sha}}))
    monkeypatch.setattr(ing, "LOCK_FILE", lock)
    monkeypatch.delenv("SCRYFALL_OFFLINE", raising=False)
    monkeypatch.delenv("SCRYFALL_BIRTHDAY_SNAPSHOT", raising=False)

    def no_net(url):
        raise AssertionError(f"network fetch attempted under the lock: {url}")
    monkeypatch.setattr(ing, "http_get", no_net)
    return cache, lock


def test_locked_read_never_fetches(tmp_path, monkeypatch):
    cache, _ = _setup(tmp_path, monkeypatch)
    cards, _ = ing.get_bulk(cache, None)
    assert cards == [{"name": "Island"}]
    (cache / "oracle-cards-20261017090000.jsonl").write_text('{"name": "Newer"}\n')  # a newer bulk appears anyway
    assert ing.get_bulk(cache, None)[0] == [{"name": "Island"}]                  # still the locked one


def test_missing_locked_file_refuses_instead_of_downloading(tmp_path, monkeypatch):
    cache, _ = _setup(tmp_path, monkeypatch, present=False)
    with pytest.raises(SystemExit, match="refusing"):
        ing.get_bulk(cache, None)
    with pytest.raises(SystemExit, match="refusing"):
        ing.get_bulk(cache, None, kind="rulings")  # a kind the lock does not name is never fetched either


def test_birthday_override_lifts_the_lock(tmp_path, monkeypatch):
    _setup(tmp_path, monkeypatch)
    monkeypatch.setenv("SCRYFALL_BIRTHDAY_SNAPSHOT", "1")
    assert ing.snapshot_lock() is None


def test_checker_flags_drift(tmp_path, monkeypatch):
    cache, lock = _setup(tmp_path, monkeypatch)
    assert chk.problems(lock, cache) == []
    (cache / "oracle-cards-20261017090000.jsonl").write_text("{}\n")
    assert any("not the locked" in p for p in chk.problems(lock, cache))
    (cache / "oracle-cards-20261017090000.jsonl").unlink()
    (cache / "oracle-cards-20261016090200.jsonl").write_text("changed\n")
    assert any("sha256" in p for p in chk.problems(lock, cache))


def test_repo_lock_matches_the_shared_cache():
    if (ROOT / ".cache").exists():
        assert chk.problems(hashes=False) == []
