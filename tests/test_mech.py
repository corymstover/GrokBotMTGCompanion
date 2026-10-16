"""Step E (Bot cycle 66.1): mechanic framework tests."""
import hashlib
import json
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import grixis_sim as gs  # noqa: E402
import grixis_mech as gm  # noqa: E402
from grixis_mech import observe, router, combat, graveyard  # noqa: E402
import grixis_mechanics as gmx  # noqa: E402


def _h(x):
    return hashlib.sha256(json.dumps(x, sort_keys=True, default=str).encode()).hexdigest()


def test_v11_outputs_byte_identical_to_main():
    """Golden hashes generated from origin/main 996350d before any step-E code existed."""
    gold = json.loads((ROOT / "tests/data/sim_v11_golden.json").read_text())
    for key, h in gold.items():
        slug, m = key.split("|")
        assert _h(gs.run(gs.load_deck(slug), samples=150, seed=57, model=m)) == h, key


def test_observer_does_not_change_results_and_is_deterministic():
    d = gs.load_deck("wick-the-whorled-mind")
    plain = [gs.play_game(d, random.Random(gs.seed_for(66, i)), model="1.1") for i in range(40)]
    traced = observe.trace_games(d, 40, 66)
    assert _h(plain) == _h([r for r, _ in traced])
    assert _h(traced) == _h(observe.trace_games(d, 40, 66))
    assert all(len(tr) == gs.MAX_TURNS for _, tr in traced)


def test_registry_valid_and_no_win_rates():
    assert gmx.problems() == []
    for s in gm.registry():
        assert s["evidence_class"] == "test_result" and s["does_not_model"] and s["limitations"]


def test_router():
    assert ("attack_trigger_proxy", True) in router.route("X", "Whenever X attacks, draw a card.", "Creature — Rat")
    assert ("graveyard_recursion", True) in router.route("Y", "Return target creature card from your graveyard to your hand.", "Sorcery")
    r = router.route_swap("A", "B", {"A": {"text": "Flying", "type_line": "Creature"}, "B": {"text": "Vigilance", "type_line": "Creature"}})
    assert r["status"] == "not_modelable" and r["reason"]


def test_combat_proxy_bounds():
    games = [(None, [{"turn": t, "battlefield": ["Z"] if t >= 3 else [], "graveyard": [], "hand": []} for t in range(1, 11)])]
    assert combat.triggers(games, "Z", False, 6, 0.0, 1.0) == 3  # lands T3, attacks T4-T6
    assert combat.triggers(games, "Z", True, 6, 0.0, 1.0) == 4
    assert combat.triggers(games, "Z", False, 6, 0.5, 0.7) < combat.triggers(games, "Z", False, 6, 0.0, 1.0)


def test_graveyard_live():
    games = [(None, [{"turn": 1, "battlefield": [], "graveyard": [], "hand": ["R"]},
                     {"turn": 2, "battlefield": [], "graveyard": ["C"], "hand": ["R"]}])]
    models = {"C": {"types": ["creature"], "permanent": True}}
    assert graveyard.live(games, "R", "creature", models, 1) == (0.0, 0.0)
    assert graveyard.live(games, "R", "creature", models, 2) == (1.0, 1.0)
    assert graveyard.target_kind("Return target creature card from your graveyard to the battlefield.") == "creature"


# ---- Bot cycle 66.2: shared death layer, death triggers, sacrifice, self-recursion split
from grixis_mech import deaths, death_triggers, sacrifice, self_recursion  # noqa: E402

_TR = [{"turn": t, "battlefield": (["A", "B"] if t >= 2 else []) + (["O"] if t >= 3 else []), "graveyard": [], "hand": []} for t in range(1, 9)]


def test_death_layer_lower_bound_is_v11_and_grid_bounded():
    lb = deaths.profile(_TR, {"A", "B", "O"}, {"O"}, set(), {"A"}, *deaths.LOWER_BOUND)
    assert all(r["deaths"] == 0 and r["gy_creatures"] == 0 for r in lb)
    w = deaths.profile(_TR, {"A", "B"}, set(), set(), {"A"}, 0.0, 6, False)
    assert next(r for r in w if r["turn"] == 6)["p_dead"]["A"] == 1.0 and next(r for r in w if r["turn"] == 5)["deaths"] == 0
    s = deaths.profile(_TR, {"A", "B", "O"}, {"O"}, {"B"}, {"A"}, 0.0, None, True)
    assert next(r for r in s if r["turn"] == 3)["deaths"] == 1.0  # outlet on T3 sacrifices A (B is the commander, O the outlet)
    assert next(r for r in s if r["turn"] == 3)["gy_creatures"] == 1.0
    assert deaths.profile(_TR, {"A", "B"}, set(), set(), set(), 0.25, None, False) == deaths.profile(_TR, {"A", "B"}, set(), set(), set(), 0.25, None, False)


def test_self_recursion_split():
    t = "Whenever you cast a spell from anywhere other than your hand, return this card from your graveyard to the battlefield tapped."
    assert self_recursion.matches("Poxwalkers", t, "Creature") and not graveyard.matches("Poxwalkers", t, "Creature")
    both = "Return Z from your graveyard to your hand. Return target creature card from your graveyard to your hand."
    assert graveyard.matches("Z", both, "Sorcery") and self_recursion.matches("Z", both, "Sorcery")


def test_death_trigger_kinds_and_outlets():
    assert death_triggers.kind("K", "Whenever another creature dies, each opponent loses 1 life.") == "watcher"
    assert death_triggers.kind("K", "When K dies, draw a card.") == "self"
    assert death_triggers.kind("K", "Flying") is None
    assert sacrifice.matches("V", "Sacrifice a creature: Scry 1.", "Creature") and not sacrifice.matches("V", "Flying", "Creature")


def test_no_win_rates_anywhere():
    txt = (ROOT / "data/grixis/mechanics/examples.json").read_text()
    assert "win_rate" not in txt and "win_probability" not in txt


# ---- Bot cycle 66.3: events, cast triggers, repeatable draw, activated engines, tokens, sacrifice as a cost
from grixis_mech import events, engines  # noqa: E402

_M = {"S": {"types": ["sorcery"]}, "C": {"types": ["creature"], "creature": True}, "L": {"types": ["land"], "land": True},
      "E": {"types": ["enchantment"], "permanent": True}}
_TR2 = [{"turn": 1, "battlefield": ["L"], "graveyard": [], "hand": ["S", "C", "E"], "mana": 1, "spent": 0},
        {"turn": 2, "battlefield": ["L", "E"], "graveyard": [], "hand": ["S", "C"], "mana": 2, "spent": 2},
        {"turn": 3, "battlefield": ["L", "E", "C"], "graveyard": ["S"], "hand": [], "mana": 5, "spent": 3}]


def test_events_casts_and_tokens():
    assert events.casts(_TR2, _M) == [(1, []), (2, ["E"]), (3, ["C", "S"])]
    assert events.token_rule("E", "When ~ enters, create two 1/1 black Rat creature tokens.") == ("etb", 2)
    assert events.token_rule("E", "At the beginning of your upkeep, create a 1/1 creature token.") == ("upkeep", 1)
    aug = events.with_tokens(_TR2, _M, {"E": ("cast", 1)})
    assert sum(x.startswith(deaths.TOKEN) for x in aug[-1]["battlefield"]) == 2


def test_engine_modules():
    ctx = {"cards": {"E": {"text": "Whenever you cast a creature spell, draw a card.", "type_line": "Enchantment"}},
           "models": _M, "creatures": {"C"}, "outlets": set(), "commanders": set()}
    g = [(None, _TR2)]
    assert engines.cast_count(g, "E", ctx, 3, deaths.LOWER_BOUND) == 1
    assert engines.draw_count(g, "E", ctx, 3, deaths.LOWER_BOUND) == 1
    assert engines.act_cost("{2}, {T}: Draw a card.") == {"mana": 2, "tap": True} and engines.act_cost("{T}: Add {B}.") is None
    ctx["cards"]["E"] = {"text": "{2}: Scry 1.", "type_line": "Enchantment"}
    assert engines.act_count(g, "E", ctx, 3, deaths.LOWER_BOUND) == 1  # T3: 5 - 3 >= 2 (T2: 0 left)
    assert engines.sac_kind("F", "As an additional cost to cast this spell, sacrifice a creature.") == "spell_cost"
    assert engines.sac_kind("F", "Sacrifice a creature: Scry 1.") is None  # a free outlet is sacrifice_costs
    for m in (engines.CastTriggers, engines.RepeatableDraw, engines.ActivatedEngines, engines.TokenMakers, engines.SacrificeAdditionalCost):
        assert m.SPEC["evidence_class"] == "test_result" and any("win rate" in x for x in m.SPEC["does_not_model"])
