"""Bot cycle 66.3 modules: cast_triggers, repeatable_draw, activated_engines, token_makers, sacrifice_additional_cost.

All read the seeded v1.1 zone trace (observe.py) plus derived events (events.py) and, where creatures matter, the
shared death layer (deaths.py). Deterministic, closed-form, test_result evidence, never win rates."""
import re

from . import deaths, events

TURNS = [4, 6, 8, 10]
NO_WR = "multiplayer win rates (never produced)"


def spec(id_, family, models, not_models, assumptions, limitations, metrics, grid=False):
    p = {"turns": TURNS}
    if grid:
        p["death_grid"] = {k: [str(x) for x in v] for k, v in deaths.GRID.items()}
    return {"id": id_, "version": "2", "family": family, "evidence_class": "test_result", "models": models,
            "does_not_model": not_models + [NO_WR], "assumptions": assumptions + (deaths.ASSUMPTIONS if grid else []),
            "parameters": p, "confidence": "low", "limitations": limitations, "metrics": metrics,
            "determinism": "seeded paired v1.1 games (grixis_sim.seed_for); derived events and the death layer are closed-form (no rng)",
            "test_file": "tests/test_mech.py"}


def _t(name, text):  # kept for older callers; parsers use semantics.clean
    return text.replace(name, "~")


def diff(base_games, chal_games, cut, add, cards, ctx, fn, matcher, grid=False):
    """Paired diff of fn(games, card, ctx, T, pt): add (challenger games) minus cut (baseline games)."""
    ia = add in cards and matcher(add, cards[add]["text"], cards[add]["type_line"])
    ic = cut in cards and matcher(cut, cards[cut]["text"], cards[cut]["type_line"])
    out = {}
    for T in TURNS:
        pts = deaths.points() if grid else [deaths.LOWER_BOUND]
        g = {pt: round((fn(chal_games, add, ctx, T, pt) if ia else 0.0) - (fn(base_games, cut, ctx, T, pt) if ic else 0.0), 4) for pt in pts}
        row = {"diff_lower_bound": g[deaths.LOWER_BOUND]}
        if grid:
            row.update(diff_range=[min(g.values()), max(g.values())], diff_mid=g[(0.1, None, True)])
        out[str(T)] = row
    return out


def _mean(games, f):
    return sum(f(tr) for _, tr in games) / max(1, len(games))


# ------------------------------------------------------------------ cast triggers
from .semantics import clean, sentences, intervening_if, N_PLAYERS  # noqa: E402

CAST_KINDS = {"": ("any",), "noncreature": ("noncreature",), "creature": ("creature",), "artifact": ("artifact",),
              "enchantment": ("enchantment",), "instant": ("instant",), "sorcery": ("sorcery",),
              "instant or sorcery": ("instant", "sorcery"), "legendary": ("legendary",), "multicolored": ("multicolored",)}


def cast_parse(name, text):
    """(filter, reason). filter: {"kinds": tuple, "ordinal": None|1|2|3, "commander": bool}; None + reason if not modelable."""
    t = clean(name, text)
    why = None
    for sent in sentences(t):
        if re.search(r"whenever (?:an opponent|a player|each opponent|another player|target player) casts", sent, re.I):
            why = "opponent / any-player cast trigger (opponents' spells are not modelled)"
            continue
        m = re.search(r"whenever you cast ([^,.]*)", sent, re.I)
        if not m:
            continue
        if intervening_if(sent):
            why = "conditional (intervening-if) cast trigger"
            continue
        w = m.group(1).strip().lower()
        if re.match(r"(?:your )?commander\b|a commander\b", w):
            return {"kinds": ("any",), "ordinal": None, "commander": True}, None
        o = re.match(r"your (first|second|third) spell each turn$", w)
        if o:
            return {"kinds": ("any",), "ordinal": {"first": 1, "second": 2, "third": 3}[o.group(1)], "commander": False}, None
        k = re.match(r"(?:(?:an|a)\s+)?(.*?)\s*spell$", w)
        if k and k.group(1) in CAST_KINDS:
            return {"kinds": CAST_KINDS[k.group(1)], "ordinal": None, "commander": False}, None
        why = "unrecognised cast-trigger qualifier: '" + w[:50] + "'"
    return None, why


def cast_filter(text, name="~"):
    f, _ = cast_parse(name, text)
    return f["kinds"] if f else None


def cast_ok(f, m):
    if m is None:
        return False
    ty = m.get("types", [])
    if f == ("any",):
        return True
    if f == ("noncreature",):
        return "creature" not in ty
    if f == ("legendary",):
        return bool(m.get("legendary"))
    if f == ("multicolored",):
        return len(m.get("colors", [])) > 1
    return any(k in ty for k in f)


def cast_count(games, n, ctx, T, pt, text=None):
    f, _ = cast_parse(n, text or ctx["cards"][n]["text"])

    def one(tr):
        on, tot = False, 0
        for (t, cs), s in zip(events.casts(tr, ctx["models"]), tr):
            if t > T:
                break
            if f["commander"]:
                tot += 1 if on and s.get("commander_cast") == t else 0
            elif on:
                q = [c for c in cs if c != n and cast_ok(f["kinds"], ctx["models"].get(c))]
                if f["ordinal"]:
                    tot += 1 if len([c for c in cs if c != n]) >= f["ordinal"] else 0  # the Nth spell each turn: <= 1/turn
                else:
                    tot += len(q)
            on = on or n in s["battlefield"]
        return tot
    return _mean(games, one)


class CastTriggers:
    SPEC = spec("cast_triggers", "cast triggers",
                ["'whenever you cast ...' triggers: your spells of the named kind cast in turns after the card is on the "
                 "battlefield, from the v1.1 trace (a cast = a non-land card newly reaching battlefield or graveyard)",
                 "expected trigger count by turn 4/6/8/10"],
                ["trigger payloads", "copies, cascade or free spells v1.1 does not cast", "opponents' spells",
                 "casts in the turn the trigger card arrives (counted from the next turn)"],
                ["every spell v1.1 casts resolves to the battlefield or graveyard that turn",
                 "'your second spell each turn' triggers at most once per turn, when v1.1 casts >= 2 spells that turn",
                 "'whenever you cast your commander' triggers on v1.1's single commander cast (recasts are not modelled)",
                 "copies are not casts; reminder text and abilities granted to other objects (quoted text) are ignored",
                 "opponent / any-player cast triggers and unrecognised qualifiers (kicked, from exile, that targets, during "
                 "an opponent's turn, ...) are not_modelable with a reason"],
                ["Counts only spells the v1.1 model casts; casting from graveyard or exile is not seen."],
                ["cast_triggers_by_turn"])

    @staticmethod
    def matches(name, text, type_line):
        return "Instant" not in type_line and "Sorcery" not in type_line and cast_parse(name, text)[0] is not None

    @staticmethod
    def why_not(name, text, type_line):
        return cast_parse(name, text)[1]

    @classmethod
    def evaluate(cls, b, c, cut, add, cards, ctx):
        return {"module": cls.SPEC["id"], "evidence_class": "test_result", "metrics": diff(b, c, cut, add, cards, ctx, cast_count, cls.matches)}


# ------------------------------------------------------------------ repeatable draw
DRAW_RX = re.compile(r"\bdraws? (a|an|one|two|three|x|\d+) (?:additional )?cards?", re.I)


def draw_parse(name, text):
    """(rule, net cards per event, sentence, reason). rule: upkeep / cast / death / attack."""
    t = clean(name, text)
    why = None
    for sent in sentences(t):
        m = DRAW_RX.search(sent)
        if not m or not re.search(r"\b(?:at the beginning of|whenever)\b", sent, re.I):
            continue
        pre = sent[:m.start()].lower()
        if re.search(r"whenever you draw|would draw", sent, re.I):
            why = "draw-triggered or replacement text, not a draw"
            continue
        if re.search(r"\bunless\b", sent, re.I):
            why = "opponent-dependent draw (Rhystic-style): planned bounded proxy, not counted as full draw"
            continue
        if re.search(r"each player's", pre) and re.search(r"that player draws", sent, re.I):
            k = events.amount(m)
            return "upkeep", k, sent, "symmetric"  # Howling Mine style: you get k on your own turn; opponents' draws not counted
        if re.search(r"(that player|target player|its controller|an opponent|each opponent|its owner) draws", sent, re.I):
            why = "another player draws (not your card advantage)"
            continue
        sym = bool(re.search(r"each player draws", sent, re.I))
        if intervening_if(sent):
            why = "conditional (intervening-if) draw trigger"
            continue
        if re.search(r"\bfor each\b|equal to", sent, re.I) or m.group(1).lower() == "x":
            why = "variable draw count"
            continue
        k = events.amount(m)
        net = 0 if re.search(r"then discard|if you do, discard", sent, re.I) else k  # loot = 0 net cards
        if events.UPKEEP.search(pre):
            mult = N_PLAYERS if re.search(r"beginning of each", pre) else 1
            return "upkeep", net * mult, sent, ("symmetric" if sym else None)
        if re.search(r"whenever you cast", pre):
            f, w = cast_parse(name, sent)
            if f:
                return "cast", net, sent, None
            why = w
            continue
        if re.search(r"\bdies\b|\bdie\b", pre):
            from . import death_triggers as dt
            if dt.parse(name, sent)[0]:
                return "death", net, sent, None
            why = dt.parse(name, sent)[1] or "unrecognised death wording"
            continue
        if re.search(r"whenever ~ attacks", pre):
            return "attack", net, sent, None
        why = "draw trigger condition not modelled: " + pre.strip()[:60]
    if why is None and DRAW_RX.search(t):
        why = "one-shot or untriggered draw (not a repeatable engine)"
    return None, 0, None, why


def draw_rule(name, text):
    r, k, _, _ = draw_parse(name, text)
    return r, k


def draw_count(games, n, ctx, T, pt):
    rule, k, sent, _ = draw_parse(n, ctx["cards"][n]["text"])
    if rule == "cast":
        return k * cast_count(games, n, ctx, T, pt, text=sent)
    if rule == "death":
        from . import death_triggers as dt
        return k * dt.side(games, n, dt.parse(n, sent)[0], ctx, T, pt)

    def one(tr):
        land = next((s["turn"] for s in tr if n in s["battlefield"]), None)
        if land is None or land >= T:
            return 0.0
        return k * (T - land)
    return _mean(games, one)


class RepeatableDraw:
    SPEC = spec("repeatable_draw", "repeatable draw",
                ["repeatable draw on a permanent: beginning-of-phase (1 event per later turn), 'whenever you cast' (per "
                 "matching cast), 'whenever ... attacks' (per later turn, attack proxy), 'whenever ... dies' (per death in "
                 "the death layer)", "expected extra cards by turn 4/6/8/10"],
                ["what the drawn cards do (the v1.1 game does not draw them)", "other trigger conditions (counted 0)",
                 "opponents' draws"],
                ["the permanent stays on the battlefield (death-triggered draw uses death_triggers v2 semantics and the death layer)",
                 "'at the beginning of each upkeep/end step' fires on every player's turn: x4 (N_PLAYERS)",
                 "loots (draw then discard) are 0 net cards; 'each player draws' counts only your draw (flagged symmetric)",
                 "not_modelable with a reason: another player draws, opponent-dependent (Rhystic-style) draw, draw-triggered or "
                 "replacement text, intervening-if conditions, variable counts, unmodelled trigger conditions"],
                ["Extra cards are counted, not played."],
                ["net_extra_cards_by_turn"], grid=True)

    @staticmethod
    def matches(name, text, type_line):
        return "Instant" not in type_line and "Sorcery" not in type_line and draw_parse(name, text)[0] is not None

    @staticmethod
    def why_not(name, text, type_line):
        return draw_parse(name, text)[3] if not draw_parse(name, text)[0] else None

    @classmethod
    def evaluate(cls, b, c, cut, add, cards, ctx):
        return {"module": cls.SPEC["id"], "evidence_class": "test_result", "layer": "deaths",
                "metrics": diff(b, c, cut, add, cards, ctx, draw_count, cls.matches, grid=True)}


# ------------------------------------------------------------------ activated engines
def REMINDER_STRIP(t):
    return re.sub(r"\([^)]*\)", "", t)


ACT_RX = re.compile(r"^((?:\{[^}]+\})+(?:, [^:]{0,60})?|\{T\}(?:, [^:]{0,60})?): (?!add\b)", re.I | re.M)


def act_cost(text, name="~"):
    t = clean(name, text) if name != "~" else REMINDER_STRIP(text)
    m = ACT_RX.search(t)
    if not m:
        return None
    cost = m.group(1)
    if re.search(r"(?:sacrifice|exile|discard|return) ~", cost, re.I) or re.match(r"^[+\u2212\-]?\d+$", cost.strip()):
        return None  # one-shot (sacrifice/exile/discard/return itself) or loyalty: not an engine
    pips = re.findall(r"\{([^}]+)\}", cost)
    mana = sum(int(p) if p.isdigit() else 0 if p in ("T", "Q", "X") else 1 for p in pips)
    return {"mana": mana, "tap": "{T}" in cost}


def act_count(games, n, ctx, T, pt):
    c = act_cost(ctx["cards"][n]["text"], n)
    mod = ctx["models"].get(n, {})
    sick = bool(mod.get("creature")) and c["tap"]
    need = c["mana"] + (1 if c["tap"] and mod.get("source") else 0)  # tapping a mana source for the ability forgoes its mana

    def one(tr):
        land, tot = None, 0
        for s in tr:
            if s["turn"] > T:
                break
            if n in s["battlefield"] and land is None:
                land = s["turn"]
            if land is None or (sick and s["turn"] == land):
                continue
            if (s.get("mana") or 0) - (s.get("spent") or 0) >= need:
                tot += 1
        return tot
    return _mean(games, one)


class ActivatedEngines:
    SPEC = spec("activated_engines", "activated engines",
                ["non-mana activated abilities on a permanent: turns from its arrival (creatures with {T}: after summoning "
                 "sickness) where the mana v1.1 left unspent that turn covers the activation's mana cost",
                 "expected activations by turn 4/6/8/10"],
                ["the ability's effect", "non-mana costs (discard, sacrifice, life) beyond the mana check",
                 "activations on opponents' turns (one per own turn)"],
                ["one activation per own turn when unspent mana >= its mana cost (+1 when the {T} cost taps a mana source); "
                 "unspent = v1.1 available minus spent; repeatable non-{T} abilities are also counted once per turn (lower bound)",
                 "summoning sickness applies to {T} abilities of creatures (no haste check)",
                 "excluded: abilities that sacrifice/exile/discard/return the card itself (one-shot), loyalty abilities, reminder text"],
                ["Leftover mana is measured after v1.1's own spending, so activations never compete with spells."],
                ["activations_by_turn"])

    @staticmethod
    def matches(name, text, type_line):
        return "Instant" not in type_line and "Sorcery" not in type_line and "Planeswalker" not in type_line and act_cost(text, name) is not None

    @classmethod
    def evaluate(cls, b, c, cut, add, cards, ctx):
        return {"module": cls.SPEC["id"], "evidence_class": "test_result", "metrics": diff(b, c, cut, add, cards, ctx, act_count, cls.matches)}


# ------------------------------------------------------------------ token makers
def tok_count(games, n, ctx, T, pt):
    rule = events.token_rule(n, ctx["cards"][n]["text"], ctx["cards"][n]["type_line"])

    def one(tr):
        aug = events.with_tokens(tr, ctx["models"], {n: rule})
        row = next((s for s in aug if s["turn"] == T), aug[-1])
        return sum(1 for x in row["battlefield"] if x.startswith(deaths.TOKEN + n + "#"))
    return _mean(games, one)


class TokenMakers:
    SPEC = spec("token_makers", "tokens",
                ["creature tokens a card creates: on arrival (ETB or spell), per later turn (beginning-of-phase or "
                 "activated), or per matching cast; expected tokens created by turn 4/6/8/10",
                 "the same tokens are death-layer and sacrifice fodder (events.with_tokens)"],
                ["token abilities, power or combat", "non-creature tokens (Treasure is v1.1's own)", "token doublers"],
                ["activated token makers are used once per later turn; attack makers once per later turn (attack proxy)",
                 "'each upkeep/end step' makers fire on every player's turn (x4); 'for each opponent' = x3",
                 "only creature tokens; ETB/attack/upkeep/cast/activated/spell rules are parsed per sentence",
                 "not_modelable with a reason: variable counts (for each / equal to / X), planeswalker loyalty, intervening-if "
                 "and other trigger conditions (combat damage, Aura attached, ...)"],
                ["Token counts are created totals; the death layer decides how many survive."],
                ["tokens_created_by_turn"])

    @staticmethod
    def matches(name, text, type_line):
        return events.token_rule(name, text, type_line)[0] is not None

    @staticmethod
    def why_not(name, text, type_line):
        return events.token_reason(name, text, type_line)

    @classmethod
    def evaluate(cls, b, c, cut, add, cards, ctx):
        return {"module": cls.SPEC["id"], "evidence_class": "test_result", "metrics": diff(b, c, cut, add, cards, ctx, tok_count, cls.matches)}


# ------------------------------------------------------------------ sacrifice as an additional cost
ADD_SAC = re.compile(r"as an additional cost to cast (?:~|this spell), sacrifice (?:a|an|one|another|x) ([a-z ]{0,30}?)(creatures?|artifacts?|permanents?|lands?)\b( or discard a card)?", re.I)
ACT_SAC = re.compile(r"sacrifice (?:a|an|another) ([a-z ]{0,20}?)(creature|artifact|permanent)[^:.]{0,30}:", re.I)


def sac_parse(name, text):
    """(cost kind, fodder kind, alternative) or (None, reason)."""
    t = clean(name, text)
    m = ADD_SAC.search(t)
    if m:
        q, fod, alt = m.group(1).strip().lower(), m.group(2).lower().rstrip("s"), bool(m.group(3))
        if q.startswith("artifact or") or "or creature" in q or re.match(r"\s*or (?:a |an )?creature", t[m.end(2):], re.I):
            fod = "artifact_or_creature"
        elif q and q not in ("", "nontoken", "another"):
            return None, "unrecognised sacrifice qualifier: '" + q + "'"
        return ("spell_cost", fod, alt), None
    m = ACT_SAC.search(t)
    if m and not deaths.is_outlet(t):
        return ("ability_cost", m.group(2).lower(), False), None
    return None, None


def sac_kind(name, text):
    r, _ = sac_parse(name, text)
    return r[0] if r else None


def payable(games, n, ctx, T, pt):
    (kind, fod, alt), _ = sac_parse(n, ctx["cards"][n]["text"])
    models = ctx["models"]

    def one(tr):
        pr = deaths.profile(tr, ctx["creatures"], set(), ctx["commanders"], set(), pt[0], pt[1], False)
        for s, row in zip(tr, pr):
            if s["turn"] > T:
                break
            if not (n in s["hand"] or n in s["battlefield"]):
                continue
            crea = sum(a for m, a in row["alive"].items() if m != n and m not in ctx["commanders"])
            arts = sum(1 for m in s["battlefield"] if m != n and "artifact" in models.get(m, {}).get("types", []))
            lands = sum(1 for m in s["battlefield"] if models.get(m, {}).get("land"))
            have = {"creature": crea, "artifact": arts, "artifact_or_creature": crea + arts, "land": lands,
                    "permanent": crea + arts + lands}.get(fod, 0)
            if have >= 1 or (alt and len([h for h in s["hand"] if h != n]) >= 1):
                return 1.0
        return 0.0
    return _mean(games, one)


class SacrificeAdditionalCost:
    SPEC = spec("sacrifice_additional_cost", "sacrifice costs (additional cost)",
                ["spells with 'as an additional cost to cast this spell, sacrifice a creature/artifact/permanent' and "
                 "abilities that sacrifice a creature as part of a paid cost (not free outlets): P(payable = the card is "
                 "available with >= 1 expected live non-commander creature or token, by turn 4/6/8/10)",
                 "tokens from the deck's token makers count as fodder"],
                ["what the spell or ability does", "the value lost by sacrificing",
                 "artifact tokens (Treasure etc.) as fodder beyond the v1.1 trace"],
                ["fodder of the named kind must exist at the end of a turn when the card is in hand or on the battlefield: "
                 "creatures/tokens alive in the death layer, artifacts or lands on the battlefield in the trace",
                 "'or discard a card' alternatives are payable with any other card in hand",
                 "unrecognised sacrifice qualifiers are not_modelable with a reason"],
                ["Payability, not value: a payable cost can still be a bad trade."],
                ["cost_payable_by_turn"], grid=True)

    @staticmethod
    def matches(name, text, type_line):
        return sac_parse(name, text)[0] is not None

    @staticmethod
    def why_not(name, text, type_line):
        return sac_parse(name, text)[1]

    @classmethod
    def evaluate(cls, b, c, cut, add, cards, ctx):
        return {"module": cls.SPEC["id"], "evidence_class": "test_result", "layer": "deaths",
                "metrics": diff(b, c, cut, add, cards, ctx, payable, cls.matches, grid=True)}
