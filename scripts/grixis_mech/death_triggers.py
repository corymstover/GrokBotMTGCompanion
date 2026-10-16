"""death_triggers: Oracle-parsed death-trigger semantics under the shared death layer (Bot cycle 66.2a correction).

Distinct semantics (parsed from Oracle text; unknown wording is not_modelable with a reason, never a generic fallback):
  self         "When(ever) ~ dies"
  a            "Whenever a creature dies" / "Whenever ~ or another creature dies": every qualifying death, the
               watcher's own included (CR 603.10a look-back)
  another      "Whenever another creature dies": qualifying deaths of creatures other than the watcher
  one_or_more  "Whenever one or more creatures die": qualifying death EVENTS (a multi-creature wipe is one trigger)
  one_or_more_other  "Whenever one or more other creatures die"
  filters: controller "you control" / any; "nontoken". "an opponent controls" -> not_modelable (no opponent creatures).
Watcher expectations are weighted by the watcher's survival probability in the death layer, never by its mere
presence in the unperturbed v1.1 trace. A watcher that dies simultaneously with others (wipe, sacrifice event) still
sees them die in that event (leaves-the-battlefield look-back); its own death counts only where the wording includes it.
"""
import re

from . import deaths

SPEC = {
    "id": "death_triggers", "version": "2", "family": "death triggers", "evidence_class": "test_result",
    "models": ["self death triggers: P(the card has died by turn 6/8/10)",
               "watcher death triggers with distinct semantics (a / another / one or more / one or more other; you control "
               "or any controller; nontoken): expected triggers by turn 6/8/10, counting deaths per creature or death "
               "EVENTS per the wording, weighted by the watcher's own survival in the death layer, with CR 603.10a look-back "
               "for simultaneous deaths",
               "every metric over the shared death-perturbation grid (deaths.GRID), with the no-death lower bound reported separately"],
    "does_not_model": ["trigger payloads (value of the trigger)",
                       "opponents' creatures dying: 'a creature dies' watchers count only your creatures (lower bound), and "
                       "'an opponent controls' watchers are not_modelable",
                       "creature-type filters ('whenever a Rat you control dies'): not_modelable",
                       "real removal choices, combat deaths, politics", "multiplayer win rates (never produced)"],
    "assumptions": deaths.ASSUMPTIONS + [
        "removal deaths in one opponent turn cycle are separate events in random order: the watcher sees another creature's "
        "removal with probability alive_before(watcher) x (1 - removal/2)",
        "wipes and sacrifices are single simultaneous events; victims' death probabilities are treated as independent of the watcher's",
        "non-creature watchers are not removed by the layer (alive while on the battlefield in the trace)"],
    "parameters": {"grid": {k: [str(x) for x in v] for k, v in deaths.GRID.items()}, "turns": [6, 8, 10]},
    "confidence": "low", "limitations": ["The death layer is a scripted proxy; results are a sensitivity range, not an estimate of real games.",
                                         "Opponents' creature deaths are not modelled.",
                                         "Version 2 (66.2a) replaces v1, which counted creatures for event wording, included the "
                                         "watcher's own death for 'another', and gave full triggers while the trace still listed a dead watcher."],
    "metrics": ["self_p_dead_by_turn", "watcher_expected_triggers_by_turn"],
    "determinism": "seeded paired v1.1 games (grixis_sim.seed_for); the death layer is closed-form (no rng)",
    "test_file": "tests/test_mech.py",
}
TOKEN = "token:"
SELF_OR_ANOTHER = re.compile(r"whenever ~ or another (nontoken )?creature( you control)? dies", re.I)
WATCH = re.compile(r"whenever (a|an|another|one or more)( other)?( nontoken)? creatures?"
                   r"( you control| an opponent controls| your opponents control| you don't control)? (?:dies|die)\b", re.I)
SELF = re.compile(r"when(?:ever)? ~ dies", re.I)
ANY_DIES = re.compile(r"\b(?:dies|die)\b", re.I)


def parse(name, text):
    """([semantics...], reason_if_not_modelable)."""
    t = text.replace(name, "~")
    sems, bad = [], None
    for m in SELF_OR_ANOTHER.finditer(t):
        sems.append({"scope": "a", "controller": "you" if m.group(2) else "any", "nontoken": bool(m.group(1))})
    t2 = SELF_OR_ANOTHER.sub("", t)
    for m in WATCH.finditer(t2):
        q, other, nt, ctl = m.group(1).lower(), bool(m.group(2)), bool(m.group(3)), (m.group(4) or "").strip().lower()
        if ctl and ctl != "you control":
            bad = "watcher counts opponents' creatures ('" + ctl + "'), which the death layer does not model"
            continue
        scope = ("one_or_more_other" if other else "one_or_more") if q == "one or more" else ("another" if q == "another" else "a")
        sems.append({"scope": scope, "controller": "you" if ctl else "any", "nontoken": nt})
    t3 = WATCH.sub("", t2)
    if SELF.search(t3):
        sems.append({"scope": "self", "controller": "you", "nontoken": False})
        t3 = SELF.sub("", t3)
    if not sems and not bad and re.search(r"whenever [^.]{0,60}\b(?:dies|die)\b", t3, re.I):
        bad = "unrecognised death-trigger wording (e.g. a creature-type filter)"
    return sems, (None if sems else bad)


def kind(name, text):
    s, _ = parse(name, text)
    return "+".join(sorted({x["scope"] for x in s})) or None


def matches(name, text, type_line):
    return bool(parse(name, text)[0])


def _q(sem, w, n):
    if sem["nontoken"] and n.startswith(TOKEN):
        return False
    if sem["scope"] in ("another", "one_or_more_other") and n == w:
        return False
    return True


def triggers_in_row(sem, w, a_w, row, removal):
    """Expected triggers of watcher w (semantics sem) from one turn's death events."""
    tot = 0.0
    for e in row["events"]:
        v = e["victims"]
        if e["kind"] == "removal":
            (n, p), = v.items()
            if n == w:
                tot += p if sem["scope"] in ("self", "a", "one_or_more") else 0.0  # own death, seen via look-back
            elif sem["scope"] != "self" and _q(sem, w, n):
                tot += p * a_w * (1 - removal / 2)
            continue
        # simultaneous event (wipe / sacrifice): w sees every victim if it was on the battlefield before the event
        pw = v.get(w, 0.0)
        others = {n: p for n, p in v.items() if n != w and _q(sem, w, n)}
        if sem["scope"] == "self":
            tot += pw
        elif sem["scope"] in ("a", "another"):
            tot += (pw if sem["scope"] == "a" else 0.0) + a_w * sum(others.values())
        else:  # one_or_more / one_or_more_other: at most one trigger per event
            miss = 1.0
            for p in others.values():
                miss *= 1 - min(1.0, p)
            if sem["scope"] == "one_or_more" and a_w > 0:
                miss *= 1 - min(1.0, pw / a_w)
            tot += a_w * (1 - miss)
    return tot


def side(games, n, sems, ctx, T, pt):
    tot = 0.0
    creature = n in ctx["creatures"]
    for _, tr in games:
        pr = deaths.profile(tr, ctx["creatures"], ctx["outlets"], ctx["commanders"], {n}, *pt)
        for s, row in zip(tr, pr):
            if s["turn"] > T:
                break
            a_w = row["alive_before"].get(n, 0.0) if creature else (1.0 if n in s["battlefield"] else 0.0)
            if a_w <= 0:
                continue
            for sem in sems:
                tot += triggers_in_row(sem, n, a_w, row, pt[0])
    return tot / max(1, len(games))


def evaluate(base_games, chal_games, cut, add, cards, ctx):
    out = {"module": SPEC["id"], "version": SPEC["version"], "evidence_class": "test_result", "metrics": {}}
    sa, ra = parse(add, cards[add]["text"]) if add in cards else ([], None)
    sc, rc = parse(cut, cards[cut]["text"]) if cut in cards else ([], None)
    out["semantics"] = {"add": sa, "cut": sc, "not_modelable": {k: r for k, r in (("add", ra), ("cut", rc)) if r}}
    for T in SPEC["parameters"]["turns"]:
        grid = {}
        for pt in deaths.points():
            grid[pt] = round((side(chal_games, add, sa, ctx, T, pt) if sa else 0.0) - (side(base_games, cut, sc, ctx, T, pt) if sc else 0.0), 4)
        out["metrics"][str(T)] = {"add_kind": kind(add, cards[add]["text"]) if add in cards else None,
                                  "cut_kind": kind(cut, cards[cut]["text"]) if cut in cards else None,
                                  "diff_lower_bound": grid[deaths.LOWER_BOUND],
                                  "diff_range": [min(grid.values()), max(grid.values())], "diff_mid": grid[(0.1, None, True)]}
    return out
