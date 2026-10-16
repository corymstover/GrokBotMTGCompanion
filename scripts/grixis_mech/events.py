"""Derived per-turn events from the zone trace (Bot cycle 66.3): casts and creature tokens. Deterministic, no rng."""
import re

from .deaths import TOKEN

NUMW = {"a": 1, "an": 1, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "x": 1}
TOKEN_RX = re.compile(r"create (a|an|one|two|three|four|five|x|\d+) (?:tapped )?(?:[\w/+\- ]{0,40}?)creature tokens?", re.I)
ETB = re.compile(r"when(?:ever)? ~ enters", re.I)
UPKEEP = re.compile(r"at the beginning of (?:your|each)(?: [a-z]+)? (?:upkeep|end step|combat|draw step|precombat main phase)", re.I)
CAST = re.compile(r"whenever you cast", re.I)


def casts(trace, models):
    """[(turn, [names cast that turn])]: non-land cards that newly reached the battlefield or graveyard that turn without
    having been on the battlefield before (v1.1 resolves every cast to one of those zones)."""
    out, prev_bf, prev_gy = [], set(), []
    for s in trace:
        new_bf = [n for n in s["battlefield"] if n not in prev_bf]
        gy = list(s["graveyard"])
        new_gy = gy[len(prev_gy):] if gy[:len(prev_gy)] == prev_gy else [n for n in gy if n not in prev_gy]
        c = [n for n in new_bf + [n for n in new_gy if n not in prev_bf]
             if n in models and not models[n].get("land") and n != "Treasure"]
        out.append((s["turn"], c))
        prev_bf, prev_gy = set(s["battlefield"]), gy
    return out


def amount(m):
    w = m.group(1).lower()
    return int(w) if w.isdigit() else NUMW.get(w, 1)


def token_rule(name, text):
    """('etb'|'upkeep'|'cast'|'activated'|None, tokens per event)."""
    t = text.replace(name, "~")
    for sent in re.split(r"(?<=\.)\s+|\n", t):
        m = TOKEN_RX.search(sent)
        if not m:
            continue
        k = amount(m)
        if ETB.search(sent):
            return "etb", k
        if UPKEEP.search(sent):
            return "upkeep", k
        if CAST.search(sent):
            return "cast", k
        if ":" in sent.split("create")[0]:
            return "activated", k
        return "spell", k
    return None, 0


def with_tokens(trace, models, makers):
    """Copy of the trace with synthetic creature tokens on the battlefield. makers: {name: (rule, k)}.
    etb/spell: k tokens the turn the card arrives; upkeep/activated: k per later turn on the battlefield;
    cast: k per other spell cast while it is on the battlefield."""
    cs = dict(casts(trace, models))
    out, toks, n = [], [], 0
    seen = set()
    for s in trace:
        t = s["turn"]
        for name, (rule, k) in sorted(makers.items()):
            here = name in s["battlefield"]
            arrived = (here or name in s["graveyard"]) and name not in seen
            if arrived:
                seen.add(name)
            m = 0
            if rule in ("etb", "spell") and arrived:
                m = k
            elif rule in ("upkeep", "activated") and here and not arrived:
                m = k
            elif rule == "cast" and here:
                m = k * sum(1 for c in cs.get(t, []) if c != name)
            for _ in range(m):
                n += 1
                toks.append(f"{TOKEN}{name}#{n}")
        out.append(dict(s, battlefield=list(s["battlefield"]) + list(toks)))
    return out
