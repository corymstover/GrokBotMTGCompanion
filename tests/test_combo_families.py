import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts import grixis_combo_families as cf


def row(cid, cards):
    return {"id": cid, "cards": cards}


def test_near_variant_relation():
    assert cf.near(["A", "B", "C"], ["A", "B", "D"])
    assert cf.near(["A", "B"], ["A", "C"])
    assert not cf.near(["A", "B", "C"], ["A", "D", "E"])
    assert not cf.near([], ["A"])


def test_components_are_transitive_and_deterministic():
    # A-B-C forms a connected family even though the endpoints are not direct near-variants.
    a = row("3", ["A", "B", "C"])
    b = row("1", ["A", "B", "D"])
    c = row("2", ["A", "D", "E"])
    d = row("4", ["X", "Y", "Z"])
    comps = cf.components([a, b, c, d])
    assert [[x["id"] for x in g] for g in comps] == [["1", "2", "3"], ["4"]]


def test_family_common_union_and_authority():
    lines = [
        {
            "id": "c1", "cards": ["A", "B", "C"], "spellbook": {"infinite": True},
            "classification": {"structural_hint": "commander_independent_power_package", "outcome_hint": "blueprint_designated_win_line"},
            "axes": {
                "commander_requirement": {"value": {"direct_commander_pieces": []}},
                "required_payoff": {"value": {"status": "none_declared_but_not_proven_unnecessary"}},
                "dead_card_burden": {"value": {"low_independent_signal_pieces": ["C"]}},
            },
        },
        {
            "id": "c2", "cards": ["A", "B", "D"], "spellbook": {"infinite": True},
            "classification": {"structural_hint": "commander_native_combo", "outcome_hint": "blueprint_designated_win_line"},
            "axes": {
                "commander_requirement": {"value": {"direct_commander_pieces": ["A"]}},
                "required_payoff": {"value": {"status": "known_external_enabler"}},
                "dead_card_burden": {"value": {"low_independent_signal_pieces": []}},
            },
        },
    ]
    sem = {
        "c1": {"record_found": True, "raw": {"mana_needed": "{1}{U}"}, "derived": {"endpoint_hints": ["mill"], "interaction_window_proxy": {"stack_action_count_proxy": 3}}},
        "c2": {"record_found": True, "raw": {"mana_needed": ""}, "derived": {"endpoint_hints": ["mana"], "interaction_window_proxy": {"stack_action_count_proxy": 2}}},
    }
    f = cf.build_family("deck", 1, lines, sem, {"c1"})
    assert f["pieces"]["common_to_every_line"] == ["A", "B"]
    assert f["pieces"]["alternative_or_bridge_pieces"] == ["C", "D"]
    assert f["line_characteristics"]["power_core_review_line_count"] == 1
    assert f["line_characteristics"]["direct_endpoint_hint_line_count"] == 1
    assert "commander_participation_varies_within_family" in f["review_flags"]
    assert f["authority"]["can_decide"] is False
    assert f["authority"]["classification_status"] == "unresolved_requires_judgment"


def test_family_never_turns_infinite_into_win_claim():
    line = {
        "id": "loop", "cards": ["A", "B"], "spellbook": {"infinite": True},
        "classification": {"structural_hint": "unlinked_spellbook_combo", "outcome_hint": "incidental_infinite_or_value_loop_requires_judgment"},
        "axes": {
            "commander_requirement": {"value": {"direct_commander_pieces": []}},
            "required_payoff": {"value": {"status": "none_declared_but_not_proven_unnecessary"}},
            "dead_card_burden": {"value": {"low_independent_signal_pieces": []}},
        },
    }
    f = cf.build_family("deck", 1, [line], {}, set())
    assert f["line_characteristics"]["infinite_line_count"] == 1
    assert f["authority"]["classification_status"] == "unresolved_requires_judgment"
    assert "win" not in f["authority"]["classification_status"]
