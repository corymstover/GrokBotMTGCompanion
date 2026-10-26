"""Lynde Deck #31 exact approved SHA M6 J source binding and M7 provenance.
Finite source-paid predicates are complementary to tests/test_m7_lynde_rev1_exact.py;
neither claims a complete Magic rules engine or measured multiplayer win rate.
"""
import hashlib
import json
from pathlib import Path
import sys
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import grixis_m6_bundle_check as m6
import grixis_m7_decision_gate as m7

D = "Lynde__Cheerful_Tormentor"
BASE = "05d1c4eea023d25e4308f78b109e80b78e0a3f4d655c3df36743ba3afbf04166"
APPROVED = "6e088891b3c92b632d95e4b6dbd83ffedb06834f812e6728cc5bfa7bdc13556e"
CORRECTION = "f7ffaef0d8e5181e959de30b061fcf56a8fd09a854d18b745691c60a9ec7087c"


def sha(name):
    return hashlib.sha256((ROOT / name).read_bytes()).hexdigest()


def test_exact_owner_selected_source_and_full_m7_gate():
    p = "data/grixis/m7/candidate_lists/Lynde__Cheerful_Tormentor_chatgpt_rev1.txt"
    assert sha(p) == APPROVED
    result = m7.verify_packet(json.loads((ROOT / (
        "data/grixis/m7/decision_reviews/Lynde__Cheerful_Tormentor_rev1.json")).read_text()))
    assert result["deck_id"] == D
    assert result["new_swaps"] == 8
    assert result["owner_presentable"]


def test_preserved_historical_seal_and_stage_files():
    root = "data/grixis/m6/owner_pass_c_substitute/" + D + "/"
    assert sha(root + "seal.json") == "ed5a1c20af6bdf0e999499fd1e07ad8652796051438ec59ec802b6f619e51a98"
    assert sha(root + "stage_a.md") == "02adfb85db19aa42d5dfe36b96906874ea1abd232b6f8bfc3861c1108035b72a"
    assert sha(root + "stage_a.json") == "d2b968bb9990d57920f983e9a5a40cf3fefe849d567b925b48bfc085ee7407eb"
    assert sha(root + "stage_a_seal_correction_v2_20261025.json") == CORRECTION


def test_lynde_exception_is_exact_one_deck_one_md_and_fails_closed():
    root = "data/grixis/m6/owner_pass_c_substitute/" + D + "/"
    original = m6.load(ROOT / (root + "seal.json"))
    seal = m6.normalize_stage_a_seal_aliases(m6.normalize_legacy_stage_a_seal(original), D)
    assert m6.verify_lynde_versioned_stage_a_correction(D, seal, "md")
    assert not m6.verify_lynde_versioned_stage_a_correction(D, seal, "json")
    assert not m6.verify_lynde_versioned_stage_a_correction("Lord_Xander__the_Collector", seal, "md")
    seal["stage_a_md_sha256"] = "0" * 64
    assert not m6.verify_lynde_versioned_stage_a_correction(D, seal, "md")


def test_m6_j_exact_revision_bundle_binds_evidence_no_approval_authority():
    bundle = m6.load(ROOT / "data/grixis/m6/ij/revision_bundles/lynde-cheerful-tormentor-m7-rev1.json")
    assert bundle["result_hash"] == "lh1:421bcaea277b8542c3b158089794036155aecb7949bd243514578ec20d054cb7"
    assert bundle["authority"]["can_approve_or_lock"] is False
    assert bundle["authority"]["can_decide"] is False
    assert m6.validate_bundle(bundle, m6.load(m6.REGISTRY), m6.load(m6.SEALS)) is True


def test_legacy_two_swap_bundle_not_falsely_transferred():
    path = ROOT / "data/grixis/m6/ij/revision_bundles/lynde-cheerful-tormentor-m7-rev1.json"
    bundle = m6.load(path)
    assert len(bundle["phase_b"]["tests"]) >= 1
    assert all(t["supports_improvement_claim"] is False for t in bundle["phase_b"]["tests"])
    assert any(t["harness_version"].startswith("lynde_rev1_") for t in bundle["phase_b"]["tests"])
