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
