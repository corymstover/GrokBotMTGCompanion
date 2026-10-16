"""Shared creature-death perturbation layer (Bot cycle 66.2; decision D4 bounded scripted proxy).

v1.1 never has a creature die. This layer overlays deterministic expectations on the zone trace:
  * opponent removal: after each of your turns, every creature you control dies with probability `removal`
    (one opponent turn cycle; expectation, no rng);
  * opponent wipe: at the end of turn `wipe` every creature you control dies (None = no wipe);
  * own sacrifice outlets actually used: while a sacrifice outlet you control is on the battlefield and you have
    other creatures, you sacrifice one creature's worth of expected mass per turn (`sac` on/off), never the outlet,
    never a tracked card while other fodder exists, never the commander.
Each turn's deaths are also emitted as death EVENTS (Bot cycle 66.2a): one per removed creature, one simultaneous event
per wipe, one per sacrifice; with each victim's death probability and the alive probabilities before the step.
A creature that dies goes to the graveyard, except commanders (command zone).
The grid point removal=0, wipe=None, sac=off is v1.1's no-death world (the lower bound).
"""
import re

GRID = {"removal": [0.0, 0.1, 0.25], "wipe": [None, 6, 8], "sac": [False, True]}
LOWER_BOUND = (0.0, None, False)
ASSUMPTIONS = [
    "opponent removal hits each of your creatures independently with probability `removal` per opponent turn cycle",
    "an opponent wipe at the end of turn `wipe` kills every creature you control",
    "a sacrifice outlet you control is used once per turn when it has fodder (not itself, not the commander, tracked cards last)",
    "dead non-commander creatures go to your graveyard and stay there (no exile, no graveyard hate)",
    "no regeneration, indestructible, protection or recursion of the dead creature inside the layer"]
OUTLET_RX = re.compile(r"sacrifice (?:a|another|an?) (?:creature|[a-z]+ creature|artifact or creature|creature or artifact|nontoken creature)[^:]{0,40}:", re.I)


def is_outlet(text):
    return bool(OUTLET_RX.search(text))


def points():
    return [(r, w, s) for r in GRID["removal"] for w in GRID["wipe"] for s in GRID["sac"]]


def profile(trace, creatures, outlets, commanders, tracked, removal, wipe, sac):
    """Per turn t: {'deaths': expected cumulative creature deaths, 'gy_creatures': expected dead non-commander
    creatures in the graveyard, 'p_dead': {tracked name: P(died by t)}} for one traced game."""
    alive, out = {}, []
    cum = gy = 0.0
    for s in trace:
        t = s["turn"]
        for n in s["battlefield"]:
            if n in creatures and n not in alive:
                alive[n] = 1.0
        before = dict(alive)
        died, evs = {}, []
        if wipe is not None and t == wipe:
            died = dict(alive)
            evs.append({"kind": "wipe", "victims": {n: a for n, a in alive.items() if a > 0}})  # one simultaneous event
        else:
            for n, a in alive.items():
                died[n] = a * removal
                if a * removal > 0:
                    evs.append({"kind": "removal", "victims": {n: a * removal}})  # one event per removed creature
        for n, d in died.items():
            alive[n] -= d
        if sac and any(o in s["battlefield"] and alive.get(o, 1.0) > 0 for o in outlets if o in s["battlefield"]):
            fod = sorted((n for n in alive if n not in outlets and n not in commanders and alive[n] > 0),
                         key=lambda n: (n in tracked, n))
            need, vic = 1.0, {}
            for n in fod:
                take = min(need, alive[n])
                alive[n] -= take
                died[n] = died.get(n, 0.0) + take
                vic[n] = take
                need -= take
                if need <= 0:
                    break
            if vic:
                evs.append({"kind": "sacrifice", "victims": vic})  # one creature's worth, one event
        step = sum(died.values())
        cum += step
        gy += sum(d for n, d in died.items() if n not in commanders)
        out.append({"turn": t, "deaths": cum, "step": step, "gy_creatures": gy,
                    "p_dead": {n: 1.0 - alive[n] for n in tracked if n in alive}, "alive": dict(alive),
                    "alive_before": before, "events": evs})
    return out
