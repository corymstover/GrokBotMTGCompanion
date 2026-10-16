from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import grixis_combo_quality as cq


def bp(commanders=("Commander",), win=None, tutors=None, recursion=None, packages=None):
    return {
        "commanders": {"value": [{"name": x} for x in commanders]},
        "win_conditions": win or [],
        "tutor_targets": tutors or [],
        "recursion": {"value": recursion or []},
        "packages": packages or [],
    }


def graph(cards):
    return {"nodes": [dict({"kind": "card", "roles": [], "packages": [], "identity_core": False,
                             "tutor_target": False, "recursion": False}, **x) for x in cards]}


def combo(cid="1", cards=None, infinite=True, produces=None, requires=None):
    return {"id": cid, "cards": cards or ["A", "B", "C"], "n": len(cards or ["A", "B", "C"]),
            "infinite": infinite, "produces": produces or ["Infinite mana"], "requires": requires or [],
            "csb_bracket_tag": "P"}


def test_direct_commander_piece_is_commander_native_hint():
    c = combo(cards=["Commander", "B"])
    g = graph([
        {"name": "Commander", "mv": 3, "type_line": "Legendary Creature", "identity_core": True},
        {"name": "B", "mv": 2, "type_line": "Artifact"},
    ])
    out = cq.analyze_combo("x", c, [c], bp(), g)
    assert out["classification"]["structural_hint"] == "commander_native_combo"
    assert out["axes"]["commander_requirement"]["value"]["mode"] == "direct_piece"
    assert out["classification"]["priority"] == "unresolved_requires_judgment"


def test_blueprint_linked_commander_independent_combo_stays_hint_not_decision():
    c = combo(cid="abc", cards=["A", "B", "C"])
    wins = [{"id": "win", "kind": "combo", "cards": ["A", "B", "C"], "enablers": [],
             "evidence": ["spellbook:abc"]}]
    g = graph([
        {"name": "A", "mv": 1, "type_line": "Instant"},
        {"name": "B", "mv": 2, "type_line": "Artifact"},
        {"name": "C", "mv": 3, "type_line": "Enchantment"},
    ])
    out = cq.analyze_combo("x", c, [c], bp(win=wins), g)
    assert out["classification"]["structural_hint"] == "commander_independent_power_package"
    assert out["classification"]["outcome_hint"] == "blueprint_designated_win_line"
    assert out["axes"]["immediate_win"]["value"]["status"] == "unverified"
    assert out["axes"]["immediate_win"]["confidence"] == "test_required"


def test_blueprint_external_enabler_is_required_payoff_signal():
    c = combo(cid="abc", cards=["A", "B", "C"])
    wins = [{"id": "win", "kind": "combo", "cards": ["A", "B", "C"], "enablers": ["Payoff"],
             "evidence": ["spellbook:abc"]}]
    out = cq.analyze_combo("x", c, [c], bp(win=wins), graph([
        {"name": "A", "mv": 1, "type_line": "Instant"},
        {"name": "B", "mv": 0, "type_line": "Artifact"},
        {"name": "C", "mv": 2, "type_line": "Enchantment"},
    ]))
    assert out["classification"]["outcome_hint"] == "blueprint_win_requires_external_payoff"
    assert out["axes"]["required_payoff"]["value"]["blueprint_external_payoffs_or_enablers"] == ["Payoff"]
    assert out["axes"]["immediate_win"]["value"]["status"] == "requires_external_payoff"


def test_mana_is_proxy_and_colored_mana_is_deferred():
    c = combo(cards=["A", "B"])
    out = cq.analyze_combo("x", c, [c], bp(), graph([
        {"name": "A", "mv": 0, "type_line": "Artifact"},
        {"name": "B", "mv": 3, "type_line": "Sorcery"},
    ]))
    m = out["axes"]["mana"]["value"]
    assert m["mv_sum_proxy"] == 3
    assert m["exact_startup_mana"] == "unresolved"
    assert m["colored_mana"] == "deferred_to_step_C"


def test_dead_card_burden_is_low_signal_proxy_not_literal_dead_claim():
    c = combo(cards=["A", "B"])
    b = bp(packages=[{"id": "pkg:combo", "role": "combo package"}, {"id": "pkg:value", "role": "value"}])
    g = graph([
        {"name": "A", "mv": 1, "type_line": "Sorcery", "packages": ["pkg:combo"]},
        {"name": "B", "mv": 2, "type_line": "Creature", "roles": ["draw"], "packages": ["pkg:value"]},
    ])
    out = cq.analyze_combo("x", c, [c], b, g)
    assert out["axes"]["dead_card_burden"]["value"]["low_independent_signal_pieces"] == ["A"]
    assert "not a claim that the card is literally dead" in out["axes"]["dead_card_burden"]["note"]


def test_near_variant_redundancy_is_descriptive_only():
    c1 = combo("1", ["A", "B", "C"])
    c2 = combo("2", ["A", "B", "D"])
    c3 = combo("3", ["X", "Y", "Z"])
    out = cq.analyze_combo("x", c1, [c1, c2, c3], bp(), graph([
        {"name": "A", "mv": 1, "type_line": "Artifact"},
        {"name": "B", "mv": 1, "type_line": "Artifact"},
        {"name": "C", "mv": 1, "type_line": "Artifact"},
    ]))
    assert out["axes"]["redundancy"]["value"]["near_variant_ids"] == ["2"]
    assert out["axes"]["resilience"]["evidence_class"] == "heuristic"


def test_infinite_without_blueprint_link_does_not_become_a_win_claim():
    c = combo(infinite=True)
    out = cq.analyze_combo("x", c, [c], bp(), graph([
        {"name": "A", "mv": 1, "type_line": "Artifact"},
        {"name": "B", "mv": 1, "type_line": "Artifact"},
        {"name": "C", "mv": 1, "type_line": "Artifact"},
    ]))
    assert out["classification"]["outcome_hint"] == "incidental_infinite_or_value_loop_requires_judgment"
    assert out["axes"]["immediate_win"]["value"]["blueprint_designated_win"] is False
