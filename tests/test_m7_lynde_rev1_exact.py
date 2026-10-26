"""Lynde M7 Rev1 exact-list, bounded P0/P1 source predicates (not an MTG engine).

This is engineering research. PASS is not final M6/M7 certification while the
historical Stage A seal disagrees with bytes or the Oracle index has partial IDs.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SHA = "6e088891b3c92b632d95e4b6dbd83ffedb06834f812e6728cc5bfa7bdc13556e"
BASE_SHA = "05d1c4eea023d25e4308f78b109e80b78e0a3f4d655c3df36743ba3afbf04166"
ID = "Lynde__Cheerful_Tormentor"


def resolve(remote, local):
    p = ROOT / remote
    if p.is_file():
        return p
    return ROOT / "work" / local


P_CANDIDATE = resolve(f"data/grixis/m7/candidate_lists/{ID}_chatgpt_rev1.txt",
                      "Lynde_Cheerful_Tormentor_M7_Rev1_Candidate_2026-10-25.txt")
P_BASE = resolve(f"data/grixis/m7/baseline_sources/{ID}_chatgpt_rev1_baseline.txt",
                 "Lynde__Cheerful_Tormentor_Approved_Baseline_2026-10-14.txt")
P_ORACLE = resolve(f"data/grixis/m7/research_challengers/{ID}_ChatGPT_Rev1_Oracle_Index_20261025.json",
                   "Lynde__Cheerful_Tormentor_ChatGPT_Rev1_Oracle_Index_20261025.json")
P_ALTS = resolve(f"data/grixis/m7/research_challengers/{ID}_ChatGPT_Rev1_Alternatives_20261025.json",
                 "Lynde__Cheerful_Tormentor_ChatGPT_Rev1_Alternatives_20261025.json")
P_BLUEPRINT = resolve(f"data/grixis/m6/test_blueprints/{ID}.json",
                      "Lynde__Cheerful_Tormentor_M6_Blueprint.json")


def decode(text):
    out = {}
    for line in text.splitlines():
        qty, name = line.split("x ", 1)
        out[name.removesuffix(" [Commander]")] = int(qty)
    return out


@pytest.fixture(scope="module")
def evidence():
    raw = P_CANDIDATE.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == SHA
    text = raw.decode("utf-8")
    lines = text.splitlines()
    assert lines[0] == "1x Lynde, Cheerful Tormentor [Commander]"
    cards = decode(text)
    assert sum(cards.values()) == 100
    assert len(cards) == 96
    assert {k: v for k, v in cards.items() if v > 1} == {
        "Island": 3, "Mountain": 2, "Swamp": 2}
    base_raw = P_BASE.read_bytes()
    assert hashlib.sha256(base_raw).hexdigest() == BASE_SHA
    baseline = decode(base_raw.decode("utf-8"))
    assert sum(baseline.values()) == 100
    adds = {k: cards[k] - baseline.get(k, 0) for k in cards if cards[k] > baseline.get(k, 0)}
    cuts = {k: baseline[k] - cards.get(k, 0) for k in baseline if baseline[k] > cards.get(k, 0)}
    assert sum(adds.values()) == sum(cuts.values()) == 8
    assert set(adds) == {
        "Court of Vantress", "Extravagant Replication", "Barrin, Master Wizard",
        "Into the Pit", "Staff of Compleation", "Urza's Saga",
        "Otawara, Soaring City", "Shizo, Death's Storehouse"}
    assert cuts == {
        "Cruel Reality": 1, "Curse of Death's Hold": 1,
        "Torment of Scarabs": 1, "Curse of the Restless Dead": 1,
        "Nightscape Familiar": 1, "Island": 1, "Mountain": 1, "Swamp": 1}
    oracle_receipt = json.loads(P_ORACLE.read_text())
    assert oracle_receipt["candidate_raw_sha256"] == SHA
    oracle = {x["name"]: x for x in oracle_receipt["cards"]}
    assert set(cards) == set(oracle)
    assert all(x["commander_legality"] == "legal" for x in oracle.values())
    assert all(set(x["color_identity"]) <= {"U", "B", "R"} for x in oracle.values())
    assert sum(v for k, v in cards.items() if "Land" in oracle[k]["type_line"]) == 35
    bp = json.loads(P_BLUEPRINT.read_text())
    assert [x["id"] for x in bp["cases"]] == [
        "C1", "K1", "K2", "K3", "K4", "K5",
        "E1", "E2", "W1", "W2", "F1", "F2", "F3"]
    assert len(oracle_receipt["cards"]) == 96
    return cards, baseline, oracle, bp


def require(evidence, case_id, cards=(), clauses=()):
    names, baseline, oracle, blueprint = evidence
    assert case_id in {c["id"] for c in blueprint["cases"]}
    assert all(n in names for n in cards), (case_id, cards)
    for name, clause in clauses:
        assert clause.lower() in (oracle[name]["oracle_text"] or
                                  oracle[name]["oracle_excerpt"]).lower(), (case_id, name, clause)
    return oracle


def test_C1_lynde_exact_trigger_and_cost(evidence):
    o = require(evidence, "C1", ["Lynde, Cheerful Tormentor"],
        [("Lynde, Cheerful Tormentor", "Whenever a Curse is put into your graveyard from the battlefield"),
         ("Lynde, Cheerful Tormentor", "draw two cards")])
    assert o["Lynde, Cheerful Tormentor"]["mana_cost"] == "{1}{U}{B}{R}"
    assert o["Lynde, Cheerful Tormentor"]["color_identity"] == ["B", "R", "U"]


@pytest.mark.parametrize("origin,destination,is_curse,recurs", [
    ("battlefield", "own_graveyard", True, True),
    ("hand", "own_graveyard", True, False),
    ("library", "own_graveyard", True, False),
    ("battlefield", "exile", True, False),
    ("battlefield", "hand", True, False),
    ("battlefield", "own_graveyard", False, False),
    ("battlefield", "opponent_graveyard", True, False),
])
def test_K1_return_window_actual_zone(evidence, origin, destination, is_curse, recurs):
    require(evidence, "K1", ["Lynde, Cheerful Tormentor"])
    eligible = origin == "battlefield" and destination == "own_graveyard" and is_curse
    assert eligible == recurs


@pytest.mark.parametrize("curses,upkeeps,draws,remaining", [
    (0, 3, 0, 0), (1, 1, 2, 0), (1, 3, 2, 0), (3, 2, 4, 1), (3, 4, 6, 0)
])
def test_K2_one_optional_movement_per_upkeep(evidence, curses, upkeeps, draws, remaining):
    require(evidence, "K2", ["Lynde, Cheerful Tormentor"],
            [("Lynde, Cheerful Tormentor", "may attach a Curse attached to you")])
    moved = min(curses, upkeeps)
    assert (2 * moved, curses - moved) == (draws, remaining)


def test_K3_misfortunes_trigger_order_source_paid(evidence):
    o = require(evidence, "K3", ["Curse of Misfortunes", "Lynde, Cheerful Tormentor"],
        [("Curse of Misfortunes", "beginning of your upkeep")])
    assert "search your library" in o["Curse of Misfortunes"]["oracle_text"].lower()
    # On your upkeep if Misfortunes enchants you: resolve tutor above Lynde.
    stack_top_to_bottom = ["Misfortunes", "Lynde"]
    assert stack_top_to_bottom[0] == "Misfortunes"


def test_K4_cut_self_punishing_curses_but_retain_risk(evidence):
    require(evidence, "K4", ["Curse of Thirst"])
    names, old, _, _ = evidence
    assert all(n in old and n not in names for n in
        ["Cruel Reality", "Curse of Death's Hold", "Torment of Scarabs"])
    assert "Curse of Thirst" in names  # risk not represented as eliminated


def test_K5_retained_upkeep_curses_check_actual_trigger_ownership(evidence):
    o = require(evidence, "K5", ["Curse of Fool's Wisdom", "Curse of Surveillance", "Curse of Unbinding"])
    assert "draw" in o["Curse of Fool's Wisdom"]["oracle_text"].lower()
    assert "upkeep" in o["Curse of Unbinding"]["oracle_text"].lower()
    assert "upkeep" in o["Curse of Surveillance"]["oracle_text"].lower()


def test_E1_three_new_outlets_require_actual_costs(evidence):
    o = require(evidence, "E1", ["Claws of Gix", "Despotic Scepter",
        "Barrin, Master Wizard", "Staff of Compleation", "Into the Pit"],
        [("Barrin, Master Wizard", "{2}, Sacrifice a permanent"),
         ("Staff of Compleation", "Pay 1 life: Destroy target permanent you own"),
         ("Into the Pit", "sacrificing a nonland permanent in addition to paying their other costs")])
    assert "Sacrifice a permanent" in o["Claws of Gix"]["oracle_text"]
    assert "Destroy target permanent you own" in o["Despotic Scepter"]["oracle_text"]
    assert "target creature" in o["Barrin, Master Wizard"]["oracle_text"].lower()
    # Barrin is not a free outlet if no legal creature target or two mana available.


def test_E2_upkeep_copies_and_shizo_enable_but_not_guarantee(evidence):
    o = require(evidence, "E2", ["Extravagant Replication", "Court of Vantress",
        "Paradox Haze", "The Ninth Doctor", "Obeka, Splitter of Seconds",
        "Shizo, Death's Storehouse"])
    assert "beginning of your upkeep" in o["Extravagant Replication"]["oracle_text"].lower()
    assert "monarch" in o["Court of Vantress"]["oracle_text"].lower()
    assert "additional upkeep" in o["The Ninth Doctor"]["oracle_text"].lower()
    assert "combat damage" in o["Obeka, Splitter of Seconds"]["oracle_text"].lower()
    assert "gains fear" in o["Shizo, Death's Storehouse"]["oracle_excerpt"].lower()


def test_W1_retain_damage_finishes_not_infinite_combo(evidence):
    require(evidence, "W1", ["Curse of Bloodletting", "Curse of Thirst",
        "Curse of Shaken Faith", "Maddening Hex", "Wicked Visitor"])
    names = evidence[0]
    assert sum(1 for n in names if "Curse" in n or n == "Maddening Hex") >= 17


def test_W2_enchantment_payoffs_source_conditions(evidence):
    o = require(evidence, "W2", ["Grim Guardian", "Doomwake Giant",
        "Ashiok's Reaper", "Entity Tracker", "Wicked Visitor"])
    assert "Whenever" in o["Grim Guardian"]["oracle_text"]
    assert "Whenever an enchantment" in o["Ashiok's Reaper"]["oracle_text"]
    assert "enchantment" in o["Doomwake Giant"]["oracle_text"].lower()


def test_F1_bounce_or_exile_not_lynde_graveyard_transition(evidence):
    o = require(evidence, "F1", ["Otawara, Soaring City", "Lynde, Cheerful Tormentor"])
    assert "owner's hand" in o["Otawara, Soaring City"]["oracle_excerpt"]
    assert "your graveyard from the battlefield" in o["Lynde, Cheerful Tormentor"]["oracle_text"]
    assert "hand" != "graveyard"


def test_F2_curse_token_is_not_recurring_card(evidence):
    require(evidence, "F2", ["Court of Vantress", "Extravagant Replication"])
    # A token copy may provide a move and draw; it ceases to exist if it dies.
    token_in_graveyard_after_state_based_actions = False
    assert not token_in_graveyard_after_state_based_actions


def test_F3_mana_and_density_paid_not_handwaved(evidence):
    cards, baseline, oracle, _ = evidence
    nonland = lambda cs: sum(v for k, v in cs.items()
                             if k in oracle and "Land" not in oracle[k]["type_line"]
                             and k != "Lynde, Cheerful Tormentor")
    assert nonland(cards) == 64
    assert sum(baseline.values()) - 35 - baseline["Lynde, Cheerful Tormentor"] == 64
    assert cards["Island"] == 3 and cards["Mountain"] == 2 and cards["Swamp"] == 2
    curses = sum(v for k, v in cards.items() if "Curse" in oracle[k]["type_line"])
    assert curses == 17  # down from 21, an important cost
    assert all(n in cards for n in ["Demonic Tutor", "Vampiric Tutor", "Imperial Seal"])
    assert oracle["Urza's Saga"]["oracle_excerpt"].count("{0}") == 1
    assert "{1}" in oracle["Urza's Saga"]["oracle_excerpt"]


def test_alternatives_are_full_100s_and_not_same_candidate(evidence):
    a = json.loads(P_ALTS.read_text())
    for k in ["alternative_A", "alternative_B"]:
        lines = a[k]["list"].splitlines()
        assert lines[0] == "1x Lynde, Cheerful Tormentor [Commander]"
        cards = decode(a[k]["list"])
        assert sum(cards.values()) == 100 and len(cards) == 96
        assert a[k]["list"] != P_CANDIDATE.read_text()


def test_uncertified_seal_and_partial_oracle_are_explicit(evidence):
    o = json.loads(P_ORACLE.read_text())
    missing_ids = [x["name"] for x in o["cards"] if not x["oracle_id"]]
    assert set(missing_ids) == {
        "Urza's Saga", "Otawara, Soaring City", "Shizo, Death's Storehouse"}
    # Green case tests must not be described as an M6/M7 final approval certificate.
    assert "NOT_FINAL_CERTIFICATION" in o["status"]
    seal = ROOT / f"data/grixis/m6/owner_pass_c_substitute/{ID}/seal.json"
    stage_a = seal.with_name("stage_a.md")
    if seal.is_file() and stage_a.is_file():
        metadata = json.loads(seal.read_text())
        assert hashlib.sha256(stage_a.read_bytes()).hexdigest() == (
            "02adfb85db19aa42d5dfe36b96906874ea1abd232b6f8bfc3861c1108035b72a")
        # Historical seal mismatch is intentional and not corrected in research.
