"""Bot cycle 57.6 (M3): simulator model v1.1 (draw, tutors, rituals, one-shot mana, treasures, conditional fast mana)
checked against exact counts / hypergeometric math on synthetic decks, plus v1.0 preservation."""
import random

from _helpers import skip  # noqa: F401  (sets sys.path)

import grixis_sim as gs
from test_simulator import land, spell


def card(name, cost, permanent=True, source=None, creature=False, artifact=False, colors=("B",), **v11):
    c = spell(name, cost, permanent, source, creature)
    c.update({"artifact": artifact, "legendary": False, "types": (["artifact"] if artifact else []) + (["creature"] if creature else []),
              "colors": list(colors), "v11": v11})
    return c


def deck_of(lib, cmd, key_sets=None, combos=None):
    d = gs.Deck("synthetic", [cmd], lib, key_sets or {}, combos or [])
    d.ci = {"B"}
    d.engine = set()
    return d


def fillers(n, start=0):
    return [card(f"Filler {i}", "{9}", colors=()) for i in range(start, start + n)]  # never castable, colourless: no side effects


def game(d, perm, turns=10, model="1.1"):
    return gs.play_game(d, random.Random(1), turns=turns, mulligan=False, perm=perm, model=model)


def test_upkeep_draw_engine_seen_count_is_exact():
    # commander {0} "At the beginning of your upkeep, draw a card", cast turn 1: seen by turn t = 7 + t + (t - 1)
    cmd = card("Engine", "", upkeep_draw=1)
    lib = [land(f"L{i}") for i in range(30)] + fillers(69)
    d = deck_of(lib, cmd)
    rng = random.Random(5)
    for g in range(200):
        perm = rng.sample(range(d.N), d.N)
        r = game(d, perm)
        for t in range(1, 11):
            assert sum(1 for v in r["first_seen"].values() if v <= t) == 7 + 2 * t - 1, (g, t)
        assert r["drawn_extra"] == 9
    # v1.0 ignores the trigger
    r0 = game(d, list(range(d.N)), model="1.0")
    assert sum(1 for v in r0["first_seen"].values() if v <= 10) == 17


def test_free_tutor_finds_blueprint_target_hypergeometric():
    # a {0} tutor and its blueprint target: P(target in hand by t) = P(either among the first 7+t) = hyper_atleast(N, 2, 7+t, 1)
    cmd = card("Cmd", "{9}")
    tut = card("Tutor", "", permanent=False, tutor={"types": [], "dest": "hand"})
    tgt = card("Target", "{9}")
    lib = [tut, tgt] + [land(f"L{i}") for i in range(36)] + fillers(61)
    d = deck_of(lib, cmd, {"tutor_targets": {"Target"}})
    rng = random.Random(9)
    hits = {t: 0 for t in (1, 3, 6)}
    n = 3000
    for g in range(n):
        perm = rng.sample(range(d.N), d.N)
        r = game(d, perm, turns=6)
        pos = {perm[i]: i for i in range(d.N)}
        for t in hits:
            got = r["first_seen"].get("Target") is not None and r["first_seen"]["Target"] <= t
            want = min(pos[0], pos[1]) < 7 + t
            assert got == want, (g, t)  # exact per game
            hits[t] += got
    for t in hits:
        p = gs.hyper_atleast(d.N, 2, 7 + t, 1)
        _, (lo, hi) = gs.wilson(hits[t], n)
        assert lo - 0.01 <= p <= hi + 0.01


def test_vampiric_style_tutor_puts_target_on_top():
    cmd = card("Cmd", "{9}")
    tut = card("TopTutor", "{B}", permanent=False, tutor={"types": [], "dest": "top"})
    tgt = card("Target", "{9}")
    lib = [land("L0"), tut] + fillers(5) + [land(f"L{i}") for i in range(1, 30)] + [tgt] + fillers(30, 5)
    d = deck_of(lib, cmd, {"tutor_targets": {"Target"}})
    r = game(d, list(range(d.N)), turns=3)
    assert r["tutored"] == [[1, "Target"]] and r["first_seen"]["Target"] == 2


def test_ritual_cast_only_when_it_enables_a_spell():
    cmd = card("Cmd", "{9}")
    rit = card("Ritual", "{B}", permanent=False, ritual=(frozenset("B"), 3))
    big = card("Three", "{2}{B}")
    lib = [land("L0"), rit, big] + fillers(4) + [land(f"L{i}") for i in range(1, 40)] + fillers(52, 4)
    r = game(deck_of(lib, cmd), list(range(len(lib))), turns=1)
    assert r["spent"][0] == 4 and r["fast_mana_used"] == 1      # {B} for the ritual + {2}{B}
    lib2 = [land("L0"), rit] + fillers(5) + [land(f"L{i}") for i in range(1, 40)] + fillers(53, 5)
    r2 = game(deck_of(lib2, cmd), list(range(len(lib2))), turns=1)
    assert r2["spent"][0] == 0 and r2["fast_mana_used"] == 0    # nothing to enable: kept in hand
    r0 = game(deck_of(lib, cmd), list(range(len(lib))), turns=1, model="1.0")
    assert r0["spent"][0] == 1                                    # v1.0: the ritual is just a 1-mana spell


def test_treasure_is_one_shot_mana():
    cmd = card("Cmd", "{9}")
    maker = card("Maker", "{B}", permanent=False, treasures=1)
    three = card("Three", "{2}{B}")
    lib = [land("L0"), maker, land("L1"), three] + fillers(12) + [land(f"L{i}") for i in range(2, 30)] + fillers(52, 12)
    d = deck_of(lib, cmd)
    r = game(d, list(range(d.N)), turns=3)
    assert r["spent"][:2] == [1, 3] and r["mana"][1] == 3 and r["fast_mana_used"] == 1
    assert r["mana"][2] == 2  # the treasure is gone


def test_lotus_petal_and_mana_vault_are_used_once():
    cmd = card("Cmd", "{9}")
    petal = card("Petal", "", artifact=True, oneshot=(frozenset("B"), 1, "sacrifice", None))
    two = card("Two", "{1}{B}")
    lib = [land("L0"), petal, two] + fillers(12) + [land(f"L{i}") for i in range(1, 30)] + fillers(54, 12)
    r = game(deck_of(lib, cmd), list(range(len(lib))), turns=2)
    assert r["spent"][0] == 2 and r["fast_mana_used"] == 1 and r["mana"][1] == 1
    vault = card("Vault", "{1}", artifact=True, oneshot=(frozenset("C"), 3, "stays", None))
    four = card("Four", "{3}{B}")
    lib = [land("L0"), vault, land("L1"), four] + fillers(12) + [land(f"L{i}") for i in range(2, 30)] + fillers(52, 12)
    r = game(deck_of(lib, cmd), list(range(len(lib))), turns=3)
    assert r["spent"][:3] == [1, 4, 0] and r["mana"][2] == 2


def test_conditional_fast_mana():
    cmd = card("Cmd", "{9}")
    two = card("Two", "{1}{B}")
    chrome = card("Chrome", "", source=(frozenset("B"), 1), artifact=True, condition="imprint")
    food = card("Imprintable", "{5}{B}", colors=("B",))
    base = [land("L0")]
    tail = [land(f"L{i}") for i in range(1, 30)]
    # with something to imprint: land + mox -> two mana turn 1
    lib = base + [chrome, food, two] + fillers(3) + tail + fillers(63, 3)
    r = game(deck_of(lib, cmd), list(range(len(lib))), turns=1)
    assert r["spent"][0] == 2
    # nothing to imprint: the mox stays in hand
    lib = base + [chrome, two] + fillers(4) + tail + fillers(63, 4)
    r = game(deck_of(lib, cmd), list(range(len(lib))), turns=1)
    assert r["spent"][0] == 0
    # Mox Diamond: needs a land card in hand after the land drop
    dia = card("Diamond", "", source=(frozenset("B"), 1), artifact=True, condition="discard_land")
    lib = base + [dia, land("Lx"), two] + fillers(12) + tail + fillers(54, 12)
    r = game(deck_of(lib, cmd), list(range(len(lib))), turns=2)
    assert r["spent"][0] == 2 and r["lands"][1] == 1  # the second land was discarded
    lib = base + [dia, two] + fillers(12) + tail + fillers(55, 12)
    assert game(deck_of(lib, cmd), list(range(len(lib))), turns=1)["spent"][0] == 0
    # Mox Opal: no mana below three artifacts
    opal = card("Opal", "", source=(frozenset("B"), 1), artifact=True, condition="metalcraft")
    lib = base + [opal, two] + fillers(4) + tail + fillers(63, 4)
    assert game(deck_of(lib, cmd), list(range(len(lib))), turns=1)["spent"][0] == 0
    rocks = [card(f"Rock{i}", "", artifact=True) for i in range(2)]
    lib = base + [opal, two] + rocks + fillers(2) + tail + fillers(63, 2)
    assert game(deck_of(lib, cmd), list(range(len(lib))), turns=1)["spent"][0] == 2
    # v1.0 treats every one of them as unconditional
    lib = base + [opal, two] + fillers(4) + tail + fillers(63, 4)
    assert game(deck_of(lib, cmd), list(range(len(lib))), turns=1, model="1.0")["spent"][0] == 2


def test_models_are_explicit_and_unknown_rejected():
    assert gs.VERSION == "1.1" and gs.MODELS == ("1.0", "1.1")
    cmd = card("Cmd", "{9}")
    d = deck_of([land("L0")] + fillers(98), cmd)
    try:
        game(d, list(range(d.N)), model="9.9")
    except ValueError:
        return
    raise AssertionError("unknown model accepted")
