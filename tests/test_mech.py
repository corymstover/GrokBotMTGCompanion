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
    # Cycle 72.2: updated to the cycle-66.5a API (string semantics + card table); the old boolean form no longer exists.
    games = [(None, [{"turn": t, "battlefield": ["Z"] if t >= 3 else [], "graveyard": [], "hand": []} for t in range(1, 11)])]
    cards = {"Z": {"text": "Whenever Z attacks, draw a card.", "type_line": "Creature — Rat"}}
    assert combat.triggers(games, "Z", "self", 6, 1.0, 1.0, cards) == 3  # lands T3, summoning-sick, attacks T4-T6
    assert combat.triggers(games, "Z", "another_attacks", 6, 1.0, 1.0, cards) == 0
    assert combat.triggers(games, "Z", "self", 6, 0.5, 0.7, cards) < combat.triggers(games, "Z", "self", 6, 1.0, 1.0, cards)


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
    assert death_triggers.kind("K", "Whenever another creature dies, each opponent loses 1 life.") == "another"
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

# ---- Bot cycle 66.2a: death-trigger semantics correction (Cory t56u)
DT = death_triggers
A_ = {"scope": "a", "controller": "any", "nontoken": False}
AN = {"scope": "another", "controller": "any", "nontoken": False}
OM = {"scope": "one_or_more", "controller": "any", "nontoken": False}
OMO = {"scope": "one_or_more_other", "controller": "any", "nontoken": False}
SF = {"scope": "self", "controller": "you", "nontoken": False}


def _row(*events):
    return {"events": [{"kind": k, "victims": v} for k, v in events]}


def test_another_excludes_watcher_own_death():
    r = _row(("removal", {"W": 0.1}))
    assert DT.triggers_in_row(AN, "W", 1.0, r, 0.1) == 0.0
    assert DT.triggers_in_row(A_, "W", 1.0, r, 0.1) == 0.1 and DT.triggers_in_row(SF, "W", 1.0, r, 0.1) == 0.1


def test_one_or_more_counts_events_not_creatures():
    wipe = _row(("wipe", {"A": 1.0, "B": 1.0, "C": 1.0}))
    assert DT.triggers_in_row(OM, "W", 1.0, wipe, 0.0) == 1.0   # one wipe = one trigger
    assert DT.triggers_in_row(AN, "W", 1.0, wipe, 0.0) == 3.0   # per creature
    two = _row(("removal", {"A": 0.25}), ("removal", {"B": 0.25}))
    assert abs(DT.triggers_in_row(OM, "W", 1.0, two, 0.25) - 2 * 0.25 * (1 - 0.125)) < 1e-9  # separate removal events


def test_simultaneous_watcher_death_look_back():
    wipe = _row(("wipe", {"W": 1.0, "A": 1.0}))
    assert DT.triggers_in_row(AN, "W", 1.0, wipe, 0.0) == 1.0   # sees A die in the same event, not itself
    assert DT.triggers_in_row(A_, "W", 1.0, wipe, 0.0) == 2.0   # 'a creature' includes its own death
    assert DT.triggers_in_row(SF, "W", 1.0, wipe, 0.0) == 1.0
    assert DT.triggers_in_row(OMO, "W", 1.0, wipe, 0.0) == 1.0
    assert DT.triggers_in_row(OMO, "W", 1.0, _row(("wipe", {"W": 1.0})), 0.0) == 0.0  # only itself died


def test_watcher_weighted_by_survival():
    wipe = _row(("wipe", {"W": 0.5, "A": 1.0}))
    assert DT.triggers_in_row(AN, "W", 0.5, wipe, 0.0) == 0.5
    tr = [{"turn": t, "battlefield": ["W", "A"], "graveyard": [], "hand": []} for t in range(1, 9)]
    ctx = {"creatures": {"W", "A"}, "outlets": set(), "commanders": set()}
    v = DT.side([(None, tr)], "W", [AN], ctx, 8, (0.0, 6, False))
    assert v == 1.0  # the wipe on T6 kills both; no triggers on T7-8 although the trace still lists W
    assert DT.side([(None, tr)], "W", [AN], ctx, 8, deaths.LOWER_BOUND) == 0.0
    assert DT.side([(None, tr)], "W", [AN], ctx, 8, (0.25, None, False)) < 7 * 0.25  # survival-weighted, below naive


def test_nontoken_and_unmodelable_wording():
    r = _row(("wipe", {"token:X#1": 1.0, "A": 1.0}))
    assert DT.triggers_in_row(dict(AN, nontoken=True), "W", 1.0, r, 0.0) == 1.0
    s, why = DT.parse("K", "Whenever a creature an opponent controls dies, you gain 1 life.")
    assert s == [] and "opponent" in why
    s, why = DT.parse("K", "Whenever a Rat you control dies, draw a card.")
    assert s == [] and why
    assert DT.parse("K", "Whenever one or more other creatures you control die, draw a card.")[0] == [
        {"scope": "one_or_more_other", "controller": "you", "nontoken": False}]
    assert DT.parse("Blood Artist", "Whenever Blood Artist or another creature dies, drain 1.")[0][0]["scope"] == "a"


def test_death_events_count_tokens():
    """66.3b: tokens are death-event victims (wipe/sacrifice/removal) and count for watchers unless 'nontoken'."""
    tr = [{"turn": t, "battlefield": ["W", "token:M#1", "token:M#2"], "graveyard": [], "hand": []} for t in range(1, 8)]
    ctx = {"creatures": {"W"}, "outlets": set(), "commanders": set()}
    an = {"scope": "another", "controller": "any", "nontoken": False}
    assert death_triggers.side([(None, tr)], "W", [an], ctx, 6, (0.0, 6, False)) == 2.0
    assert death_triggers.side([(None, tr)], "W", [dict(an, nontoken=True)], ctx, 6, (0.0, 6, False)) == 0.0
    pr = deaths.profile(tr, {"W"}, set(), set(), set(), 0.0, 6, False)
    assert pr[5]["gy_creatures"] == 1.0  # only W reaches the graveyard; tokens cease to exist


# ---------------------------------------------------------------- Bot cycle 66.4 semantic self-audit (negative / edge cases)
def test_664_cast_trigger_semantics():
    from grixis_mech import engines as E
    P = E.cast_parse
    assert P("X", "Whenever you cast a noncreature spell, create a 1/1 token.")[0]["kinds"] == ("noncreature",)
    assert P("X", "Whenever you cast an instant or sorcery spell, draw a card.")[0]["kinds"] == ("instant", "sorcery")
    f = P("X", "Whenever you cast your second spell each turn, draw a card.")[0]
    assert f["ordinal"] == 2
    assert P("X", "Whenever you cast your commander, draw a card.")[0]["commander"]
    for t in ("Whenever an opponent casts a spell, you may draw a card.", "Whenever a player casts a spell, X deals 1 damage."):
        f, why = P("X", t)
        assert f is None and "opponent" in why
    for t in ("Whenever you cast a kicked spell, draw a card.", "Whenever you cast a spell during an opponent's turn, mill two.",
              "Whenever you cast a spell that targets X, scry 1."):
        f, why = P("X", t)
        assert f is None and why.startswith("unrecognised")
    # copies are not casts; granted quoted abilities and reminder text are not the card's own
    assert P("X", "Whenever you copy a spell, draw a card.") == (None, None)
    assert P("X", 'When X enters, create a token with "Whenever you cast a spell, scry 1."')[0] is None
    assert P("X", "Prowess (Whenever you cast a noncreature spell, this creature gets +1/+1 until end of turn.)")[0] is None
    assert P("X", "Whenever you cast a spell, if it's your turn, draw a card.")[0] is None


def test_664_repeatable_draw_semantics():
    from grixis_mech import engines as E
    D = E.draw_parse
    assert D("X", "At the beginning of your upkeep, you draw a card and you lose 1 life.")[:2] == ("upkeep", 1)
    assert D("X", "At the beginning of each end step, draw a card.")[:2] == ("upkeep", 4)
    assert D("X", "Whenever you cast a noncreature spell, draw a card, then discard a card.")[:2] == ("cast", 0)  # loot = 0 net
    r = D("X", "At the beginning of each player's draw step, that player draws an additional card.")
    assert r[0] == "upkeep" and r[1] == 1 and r[3] == "symmetric"
    for t, frag in (("Whenever an opponent casts a spell, you may draw a card unless that player pays {1}.", "Rhystic"),
                    ("Whenever you draw a card, X deals 1 damage to each opponent.", "not a draw"),
                    ("If you would draw a card, draw two cards instead.", None),
                    ("At the beginning of your upkeep, if you control a Wizard, draw a card.", "intervening-if"),
                    ("Whenever X deals combat damage to a player, draw a card.", "not modelled"),
                    ("At the beginning of your upkeep, draw a card for each creature you control.", "variable"),
                    ("At the beginning of your upkeep, target player draws a card.", "another player")):
        rule, k, _, why = D("X", t)
        assert rule is None, t
        if frag:
            assert frag in why, (t, why)
    # reminder text (Blitz) is not a death draw
    assert D("X", "Blitz {2}{R} (If you cast this spell for its blitz cost, it gains haste and \"When this creature dies, draw a card.\" Sacrifice it at the beginning of the next end step.)")[0] is None


def test_664_activated_engine_costs():
    from grixis_mech import engines as E
    assert E.act_cost("{2}, Sacrifice X: Draw a card.", "X") is None
    assert E.act_cost("{1}, Sacrifice this artifact: Draw a card.", "X") is None
    assert E.act_cost("{2}, Discard X: Search your library for a land.", "X") is None
    assert E.act_cost("Channel \u2014 {1}{R}, Discard X: It deals 4 damage.", "X") is None
    c = E.act_cost("{2}, {T}: Draw a card.", "X")
    assert c["tap"] and c["mana"] == 2
    assert not E.ActivatedEngines.matches("X", "+1: Draw a card.", "Legendary Planeswalker \u2014 X")


def test_664_token_and_sac_semantics():
    from grixis_mech import events as V, engines as E
    assert V.token_rule("X", "When X enters, create a 1/1 black Rat creature token.", "Creature")[0] == "etb"
    assert V.token_rule("X", "At the beginning of each upkeep, create a 1/1 black Faerie Rogue creature token with flying.", "Enchantment")[1] == 4
    assert V.token_rule("X", "Whenever X attacks, create a 1/1 red Goblin creature token.", "Creature")[0] == "attack"
    assert V.token_rule("X", "When X enters, create a Treasure token.", "Artifact")[0] is None  # not a creature token
    assert V.token_rule("X", "Create a 1/1 Rat creature token for each creature you control.", "Sorcery")[0] is None
    assert "loyalty" in V.token_reason("X", "+1: Create a 1/1 Ninja creature token.", "Legendary Planeswalker \u2014 X")
    assert "intervening-if" in V.token_reason("X", "Whenever X attacks, if you control a Dragon, create a 4/4 Dragon creature token.", "Creature")
    assert E.sac_parse("X", "As an additional cost to cast this spell, sacrifice an artifact.")[0] == ("spell_cost", "artifact", False)
    assert E.sac_parse("X", "As an additional cost to cast this spell, sacrifice an artifact or discard a card.")[0] == ("spell_cost", "artifact", True)
    assert E.sac_parse("X", "As an additional cost to cast this spell, sacrifice an artifact or creature.")[0][1] == "artifact_or_creature"
    assert E.sac_parse("X", "As an additional cost to cast this spell, sacrifice a creature.")[0] == ("spell_cost", "creature", False)
