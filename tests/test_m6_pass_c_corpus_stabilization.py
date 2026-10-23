"""Full 62-receipt owner-equivalent Pass C corpus test for the stabilized shared checker.

Added with M7 Deck #7 (Be_lakor__the_Dark_Master). Proves exactly which preserved receipts pass the
stabilized scripts/grixis_m6_bundle_check.py, that every receipt accepted before (decks #1-#6 under PR #654)
is still accepted, and that TRUE/YES, ambiguous, missing, contradictory, partial and tampered inputs fail.
"""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("bundle_check_corpus", ROOT / "scripts/grixis_m6_bundle_check.py")
bc = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(bc)

PROGRESS = json.loads((ROOT / bc.OWNER_PROGRESS).read_text(encoding="utf-8"))
DECKS = [row["deck_id"] for row in PROGRESS["decks"]]
# Preserved seals whose recorded stage_a.md SHA-256 does not match the committed bytes (their git_blob_sha does
# match). The stabilized checker deliberately keeps rejecting these; they need an owner decision, not a rename.
EXPECTED_FAIL = {
    "Lord_Xander__the_Collector": "diverged from separately sealed byte commitment",
    "Lynde__Cheerful_Tormentor": "diverged from separately sealed byte commitment",
}
PREVIOUSLY_ACCEPTED = DECKS[:6]  # accepted by the PR #654 checker (cd0be27a...)


def _h(path):
    return "sha256:" + hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def judgment(deck_id):
    base = f"data/grixis/m6/owner_pass_c_substitute/{deck_id}"
    j = {"reviewer": "ChatGPT/OpenAI GPT-6", "review_class": bc.OWNER_EQUIVALENT, "technically_independent": False,
         "judgment_receipt_path": base + "/final_disposition.md", "waiver_receipt_path": bc.OWNER_WAIVER,
         "progress_receipt_path": bc.OWNER_PROGRESS, "stage_a_seal_path": base + "/seal.json"}
    for k in ("judgment_receipt", "waiver_receipt", "progress_receipt", "stage_a_seal"):
        j[k + "_sha256"] = _h(j[k + "_path"])
    return j


def test_corpus_is_the_full_62():
    assert len(DECKS) == 62 and len(set(DECKS)) == 62
    assert DECKS[6] == "Be_lakor__the_Dark_Master"


@pytest.mark.parametrize("deck_id", DECKS)
def test_full_corpus_exact_outcome(deck_id):
    if deck_id in EXPECTED_FAIL:
        with pytest.raises(ValueError, match=EXPECTED_FAIL[deck_id]):
            bc.validate_pass_c(judgment(deck_id), deck_id)
    else:
        assert bc.validate_pass_c(judgment(deck_id), deck_id) is True


def test_nothing_previously_accepted_is_rejected_and_counts():
    passed = [d for d in DECKS if d not in EXPECTED_FAIL]
    assert set(PREVIOUSLY_ACCEPTED) <= set(passed)
    assert len(passed) == 60


@pytest.mark.parametrize("deck_id", PREVIOUSLY_ACCEPTED)
def test_previously_accepted_canonical_seals_unchanged_by_new_layer(deck_id):
    seal = bc.normalize_legacy_stage_a_seal(bc.load(ROOT / f"data/grixis/m6/owner_pass_c_substitute/{deck_id}/seal.json"))
    assert bc.normalize_stage_a_seal_aliases(seal, deck_id) is seal


def _seal(deck_id):
    return json.loads((ROOT / f"data/grixis/m6/owner_pass_c_substitute/{deck_id}/seal.json").read_text(encoding="utf-8"))


def _validate_with_seal(monkeypatch, deck_id, seal, final_text=None):
    real_load, real_bind, real_safe = bc.load, bc.bind, bc.safe_repo_file

    def fake_load(path):
        if str(path).endswith(f"{deck_id}/seal.json"):
            return copy.deepcopy(seal)
        return real_load(path)

    monkeypatch.setattr(bc, "load", fake_load)
    monkeypatch.setattr(bc, "bind", lambda name, h: None)
    if final_text is not None:
        tmp = ROOT / ".pytest_tmp_final.md"

        def fake_safe(name):
            if str(name).endswith(f"{deck_id}/final_disposition.md"):
                tmp.write_text(final_text, encoding="utf-8")
                return tmp
            return real_safe(name)

        monkeypatch.setattr(bc, "safe_repo_file", fake_safe)
    try:
        return bc.validate_pass_c(judgment(deck_id), deck_id)
    finally:
        (ROOT / ".pytest_tmp_final.md").unlink(missing_ok=True)


BELAKOR = "Be_lakor__the_Dark_Master"


def test_belakor_seal_maps_one_to_one_without_rewriting():
    seal = _seal(BELAKOR)
    out = bc.normalize_stage_a_seal_aliases(seal, BELAKOR)
    assert out["canonical_input_sha256"] == seal["canonical_sha256"]
    assert out["git_first_stage_commit_sha"] == seal["first_stage_git_commit_sha"]
    assert out["review_class_after_final"] == seal["formal_class"]
    assert out["technically_independent"] is seal["technical_independence"] is False
    assert out["actual_evaluator"] == seal["actual_evaluator"]
    for k, v in seal.items():
        assert out[k] == v


@pytest.mark.parametrize("value", [True, "TRUE", "YES", "false", None, 0])
def test_independence_true_yes_or_ambiguous_fails(monkeypatch, value):
    seal = _seal(BELAKOR)
    seal["technical_independence"] = value
    with pytest.raises(ValueError):
        _validate_with_seal(monkeypatch, BELAKOR, seal)


def test_missing_independence_fails(monkeypatch):
    seal = _seal(BELAKOR)
    del seal["technical_independence"]
    with pytest.raises(ValueError, match="missing required field"):
        _validate_with_seal(monkeypatch, BELAKOR, seal)


def test_contradictory_aliases_fail(monkeypatch):
    seal = _seal(BELAKOR)
    seal["canonical_raw_sha256"] = "0" * 64
    with pytest.raises(ValueError, match="contradictory"):
        _validate_with_seal(monkeypatch, BELAKOR, seal)
    seal = _seal(BELAKOR)
    seal["technically_independent"] = True  # canonical key contradicting its legacy alias
    with pytest.raises(ValueError, match="contradictory|both canonical and legacy"):
        _validate_with_seal(monkeypatch, BELAKOR, seal)


def test_partial_and_tampered_seal_fail(monkeypatch):
    seal = _seal(BELAKOR)
    del seal["stage_a_md_sha256"]
    with pytest.raises(ValueError, match="missing required field"):
        _validate_with_seal(monkeypatch, BELAKOR, seal)
    seal = _seal(BELAKOR)
    seal["stage_a_md_sha256"] = "f" * 64
    with pytest.raises(ValueError, match="diverged"):
        _validate_with_seal(monkeypatch, BELAKOR, seal)
    seal = _seal(BELAKOR)
    seal["stage_a_md_path"] = "data/grixis/m6/owner_pass_c_substitute/Cecily__Bjorna__Lutri/stage_a.md"
    with pytest.raises(ValueError, match="fixed deck Stage A location"):
        _validate_with_seal(monkeypatch, BELAKOR, seal)
    seal = _seal(BELAKOR)
    seal["first_stage_git_commit_sha"] = "1" * 40
    with pytest.raises(ValueError, match="provenance mismatch"):
        _validate_with_seal(monkeypatch, BELAKOR, seal)


def test_wrong_class_or_evaluator_fail(monkeypatch):
    seal = _seal(BELAKOR)
    seal["formal_class"] = "BLIND_INDEPENDENT_REVIEW"
    with pytest.raises(ValueError, match="provenance mismatch"):
        _validate_with_seal(monkeypatch, BELAKOR, seal)
    seal = _seal(BELAKOR)
    seal["actual_evaluator"] = "ChatGPT GPT-6"
    with pytest.raises(ValueError, match="provenance mismatch"):
        _validate_with_seal(monkeypatch, BELAKOR, seal)


def test_unknown_alias_is_not_accepted(monkeypatch):
    seal = _seal(BELAKOR)
    seal["formal_review_label"] = seal.pop("formal_class")
    with pytest.raises(ValueError, match="missing required field"):
        _validate_with_seal(monkeypatch, BELAKOR, seal)


def test_sealed_stage_a_json_fallback_requires_binding(monkeypatch):
    deck = "Cormela__Glamour_Thief"
    seal = _seal(deck)
    seal["stage_a_json_sha256"] = "e" * 64
    with pytest.raises(ValueError, match="not bound by its seal"):
        _validate_with_seal(monkeypatch, deck, seal)
    deck = "Jeleva__Nephalia_s_Scourge"
    seal = _seal(deck)
    seal["review_class"] = "SOMETHING_ELSE"  # direct seal value contradicts the sealed Stage A JSON value
    with pytest.raises(ValueError, match="contradictory|provenance mismatch"):
        _validate_with_seal(monkeypatch, deck, seal)


def _final(deck_id):
    return (ROOT / f"data/grixis/m6/owner_pass_c_substitute/{deck_id}/final_disposition.md").read_text(encoding="utf-8")


@pytest.mark.parametrize("veto", ["Technically independent: TRUE.", "technical independence **YES**",
                                  "independent third model: yes", "technically_independent=true",
                                  "independent model YES"])
def test_receipt_true_yes_statement_vetoes(monkeypatch, veto):
    text = _final(BELAKOR) + "\n" + veto + "\n"
    assert not bc.pass_c_preserved_nonindependence(text, BELAKOR)
    with pytest.raises(ValueError):
        _validate_with_seal(monkeypatch, BELAKOR, _seal(BELAKOR), final_text=text)


def test_receipt_phrase_removed_or_moved_fails(monkeypatch):
    phrase = bc._PASS_C_PRESERVED_NONINDEPENDENCE[BELAKOR]
    text = _final(BELAKOR).replace(phrase, "technical third-model independence disclosed")
    with pytest.raises(ValueError, match="missing provenance"):
        _validate_with_seal(monkeypatch, BELAKOR, _seal(BELAKOR), final_text=text)
    # another deck's phrase is not accepted for this deck
    other = bc._PASS_C_PRESERVED_NONINDEPENDENCE["Cecily__Bjorna__Lutri"]
    assert not bc.pass_c_preserved_nonindependence(other, BELAKOR)


def test_receipt_missing_evaluator_or_disposition_fails(monkeypatch):
    text = _final(BELAKOR).replace("ChatGPT/OpenAI GPT-6", "an evaluator")
    with pytest.raises(ValueError, match="missing provenance"):
        _validate_with_seal(monkeypatch, BELAKOR, _seal(BELAKOR), final_text=text)
    text = _final(BELAKOR).replace("KEEP", "K E E P")
    with pytest.raises(ValueError, match="missing provenance"):
        _validate_with_seal(monkeypatch, BELAKOR, _seal(BELAKOR), final_text=text)


def test_enumerated_phrases_are_verbatim_and_unique_per_deck():
    for deck, phrase in bc._PASS_C_PRESERVED_NONINDEPENDENCE.items():
        assert deck in DECKS
        assert _final(deck).count(phrase) >= 1
    for deck, spelling in bc._PASS_C_PRESERVED_EVALUATOR_SPELLING.items():
        assert deck in DECKS and spelling in _final(deck) and "ChatGPT/OpenAI GPT-6" not in _final(deck)
