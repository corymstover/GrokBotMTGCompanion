"""ChatGPT cycle 66.9: semantic tests for opponent-dependent draw bounded proxy."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from grixis_mech import opponents  # noqa: E402


def _games(name="R", turns=3):
    return [(None, [{"turn": t, "battlefield": ([name] if t >= 2 else []), "graveyard": [], "hand": []}
                    for t in range(1, turns + 1)])]


def test_rhystic_and_mystic_style_parsing_is_explicit():
    r, why = opponents.parse("Rhystic Study",
                             "Whenever an opponent casts a spell, you may draw a card unless that player pays {1}.",
                             "Enchantment")
    assert why is None and r == {"source": "opponent_cast", "scope": "any", "cards": 1, "tax": "{1}"}

    r, why = opponents.parse("Mystic Remora",
                             "Whenever an opponent casts a noncreature spell, you may draw a card unless that player pays {4}.",
                             "Enchantment")
    assert why is None and r["scope"] == "noncreature" and r["tax"] == "{4}"


def test_opponent_draw_semantics_second_and_each_card():
    r, why = opponents.parse("Watcher", "Whenever an opponent draws their second card each turn, you draw a card.", "Creature")
    assert why is None and r["source"] == "opponent_draw" and r["scope"] == "second_card"
    r, why = opponents.parse("Watcher", "Whenever an opponent draws a card, you draw two cards.", "Creature")
    assert why is None and r["scope"] == "each_card" and r["cards"] == 2


def test_not_every_sentence_about_opponents_drawing_is_your_draw_engine():
    cases = (
        "At the beginning of each player's draw step, that player draws an additional card.",
        "Each opponent draws a card.",
        "Whenever an opponent casts a spell, that player draws a card.",
    )
    for text in cases:
        r, _ = opponents.parse("X", text, "Enchantment")
        assert r is None


def test_qualified_cast_scope_is_refused_instead_of_generalized():
    r, why = opponents.parse("X", "Whenever an opponent casts their second spell each turn, you draw a card.", "Enchantment")
    assert r is None
    # This syntax is outside the narrow CAST_RX and therefore may be no-match; it must never become a generic supported rule.
    assert not opponents.matches("X", "Whenever an opponent casts their second spell each turn, you draw a card.", "Enchantment")


def test_cast_grid_math_and_tax_nonpayment_axis():
    rule = {"source": "opponent_cast", "scope": "any", "cards": 1, "tax": "{1}"}
    # Permanent active after T2 and T3 => two opponent turn cycles. 3 opponents * 2 spells = 6 triggers/round.
    # At 50% nonpayment: 3 cards/round => 6 cards sensitivity by T3.
    assert opponents.side(_games(), "R", rule, 3, (2.0, 0.7, 0.5, 1.0)) == 6.0

    free = dict(rule, tax=None)
    # Unconditional draw ignores the nonpay axis: 6 per round * 2 rounds.
    assert opponents.side(_games(), "R", free, 3, (2.0, 0.7, 0.25, 1.0)) == 12.0


def test_noncreature_scope_uses_declared_composition_axis():
    rule = {"source": "opponent_cast", "scope": "noncreature", "cards": 1, "tax": None}
    # One active round at T2: 3 opponents * 2 spells * .5 noncreature = 3.
    assert opponents.side(_games(turns=2), "R", rule, 2, (2.0, 0.5, 0.25, 1.0)) == 3.0


def test_opponent_draw_proxy_counts_second_card_once_per_opponent_turn():
    rule = {"source": "opponent_draw", "scope": "second_card", "cards": 1, "tax": None}
    # At one card/opponent turn, second-card triggers never happen.
    assert opponents.side(_games(turns=2), "R", rule, 2, (1.0, 0.5, 0.5, 1.0)) == 0.0
    # At two cards/opponent turn, one event per opponent; one active round = 3.
    assert opponents.side(_games(turns=2), "R", rule, 2, (1.0, 0.5, 0.5, 2.0)) == 3.0


def test_proxy_is_declared_sensitivity_not_win_rate_or_fake_midpoint():
    spec = opponents.OpponentDependentDraw.SPEC
    assert spec["evidence_class"] == "test_result" and spec["confidence"] == "low"
    assert any("win rates" in x for x in spec["does_not_model"])
    assert any("no midpoint" in x.lower() for x in spec["limitations"])
    assert spec["parameters"]["opponents"] == 3
