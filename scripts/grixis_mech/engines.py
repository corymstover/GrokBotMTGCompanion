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
    return {"id": id_, "version": "1", "family": family, "evidence_class": "test_result", "models": models,
            "does_not_model": not_models + [NO_WR], "assumptions": assumptions + (deaths.ASSUMPTIONS if grid else []),
            "parameters": p, "confidence": "low", "limitations": limitations, "metrics": metrics,
            "determinism": "seeded paired v1.1 games (grixis_sim.seed_for); derived events and the death layer are closed-form (no rng)",
            "test_file": "tests/test_mech.py"}


def _t(name, text):
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
CAST_RX = re.compile(r"whenever you cast (?:a|an|your)?\s*([^,.]{0,50}?)(?:spell|,)", re.I)


def cast_filter(text):
    m = CAST_RX.search(text)
    if not m:
        return None
    w = m.group(1).lower()
    if "instant or sorcery" in w or "instant and sorcery" in w:
        return ("instant", "sorcery")
    for k in ("noncreature", "creature", "artifact", "enchantment", "instant", "sorcery", "legendary"):
        if k in w:
            return (k,)
    return ("any",)


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
    return any(k in ty for k in f)


def cast_count(games, n, ctx, T, pt):
    f = cast_filter(_t(n, ctx["cards"][n]["text"]))

    def one(tr):
        on, tot = False, 0
        for (t, cs), s in zip(events.casts(tr, ctx["models"]), tr):
            if t > T:
                break
            if on:
                tot += sum(1 for c in cs if c != n and cast_ok(f, ctx["models"].get(c)))
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
                ["every spell v1.1 casts resolves to the battlefield or graveyard that turn"],
                ["Counts only spells the v1.1 model casts; casting from graveyard or exile is not seen."],
                ["cast_triggers_by_turn"])

    @staticmethod
    def matches(name, text, type_line):
        return "Instant" not in type_line and "Sorcery" not in type_line and cast_filter(_t(name, text)) is not None

    @classmethod
    def evaluate(cls, b, c, cut, add, cards, ctx):
        return {"module": cls.SPEC["id"], "evidence_class": "test_result", "metrics": diff(b, c, cut, add, cards, ctx, cast_count, cls.matches)}


# ------------------------------------------------------------------ repeatable draw
DRAW_RX = re.compile(r"draws? (a|an|one|two|three|x|\d+) cards?", re.I)


def draw_rule(name, text):
    t = _t(name, text)
    for sent in re.split(r"(?<=\.)\s+|\n", t):
        m = DRAW_RX.search(sent)
        if not m or not re.search(r"(?:at the beginning of|whenever)", sent, re.I):
            continue
        k = events.amount(m)
        if events.UPKEEP.search(sent):
            return "upkeep", k
        if events.CAST.search(sent):
            return "cast", k
        if re.search(r"\bdies\b", sent):
            return "death", k
        if re.search(r"attacks", sent):
            return "attack", k
        return "other", k
    return None, 0


def draw_count(games, n, ctx, T, pt):
    rule, k = draw_rule(n, ctx["cards"][n]["text"])
    if rule == "cast":
        return k * cast_count(games, n, ctx, T, pt)

    def one(tr):
        land = next((s["turn"] for s in tr if n in s["battlefield"]), None)
        if land is None or land >= T:
            return 0.0
        if rule in ("upkeep", "attack"):
            return k * (T - land)
        if rule == "death":
            pr = deaths.profile(tr, ctx["creatures"], ctx["outlets"], ctx["commanders"], set(), *pt)
            return k * sum(x["step"] for x in pr if land <= x["turn"] <= T)
        return 0.0
    return _mean(games, one)


class RepeatableDraw:
    SPEC = spec("repeatable_draw", "repeatable draw",
                ["repeatable draw on a permanent: beginning-of-phase (1 event per later turn), 'whenever you cast' (per "
                 "matching cast), 'whenever ... attacks' (per later turn, attack proxy), 'whenever ... dies' (per death in "
                 "the death layer)", "expected extra cards by turn 4/6/8/10"],
                ["what the drawn cards do (the v1.1 game does not draw them)", "other trigger conditions (counted 0)",
                 "opponents' draws"],
                ["the permanent stays on the battlefield (death-triggered draw uses the death layer)"],
                ["Extra cards are counted, not played."],
                ["extra_cards_by_turn"], grid=True)

    @staticmethod
    def matches(name, text, type_line):
        return "Instant" not in type_line and "Sorcery" not in type_line and draw_rule(name, text)[0] is not None

    @classmethod
    def evaluate(cls, b, c, cut, add, cards, ctx):
        return {"module": cls.SPEC["id"], "evidence_class": "test_result", "layer": "deaths",
                "metrics": diff(b, c, cut, add, cards, ctx, draw_count, cls.matches, grid=True)}


# ------------------------------------------------------------------ activated engines
ACT_RX = re.compile(r"^((?:\{[^}]+\})+(?:, [^:]{0,60})?|\{T\}(?:, [^:]{0,60})?): (?!add\b)", re.I | re.M)


def act_cost(text):
    m = ACT_RX.search(text)
    if not m:
        return None
    cost = m.group(1)
    if re.search(r"sacrifice ~|exile ~", cost, re.I):
        return None  # one-shot, not an engine
    pips = re.findall(r"\{([^}]+)\}", cost)
    mana = sum(int(p) if p.isdigit() else 0 if p in ("T", "Q", "X") else 1 for p in pips)
    return {"mana": mana, "tap": "{T}" in cost}


def act_count(games, n, ctx, T, pt):
    c = act_cost(_t(n, ctx["cards"][n]["text"]))
    sick = bool(ctx["models"].get(n, {}).get("creature")) and c["tap"]

    def one(tr):
        land, tot = None, 0
        for s in tr:
            if s["turn"] > T:
                break
            if n in s["battlefield"] and land is None:
                land = s["turn"]
            if land is None or (sick and s["turn"] == land):
                continue
            if (s.get("mana") or 0) - (s.get("spent") or 0) >= c["mana"]:
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
                ["one activation per turn when unspent mana >= its mana cost; unspent = v1.1 available minus spent"],
                ["Leftover mana is measured after v1.1's own spending, so activations never compete with spells."],
                ["activations_by_turn"])

    @staticmethod
    def matches(name, text, type_line):
        return "Instant" not in type_line and "Sorcery" not in type_line and act_cost(_t(name, text)) is not None

    @classmethod
    def evaluate(cls, b, c, cut, add, cards, ctx):
        return {"module": cls.SPEC["id"], "evidence_class": "test_result", "metrics": diff(b, c, cut, add, cards, ctx, act_count, cls.matches)}


# ------------------------------------------------------------------ token makers
def tok_count(games, n, ctx, T, pt):
    rule = events.token_rule(n, ctx["cards"][n]["text"])

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
                ["activated token makers are used once per later turn", "X = 1"],
                ["Token counts are created totals; the death layer decides how many survive."],
                ["tokens_created_by_turn"])

    @staticmethod
    def matches(name, text, type_line):
        return events.token_rule(name, text)[0] is not None

    @classmethod
    def evaluate(cls, b, c, cut, add, cards, ctx):
        return {"module": cls.SPEC["id"], "evidence_class": "test_result", "metrics": diff(b, c, cut, add, cards, ctx, tok_count, cls.matches)}


# ------------------------------------------------------------------ sacrifice as an additional cost
ADD_SAC = re.compile(r"as an additional cost to cast (?:this spell|~), sacrifice (?:a|an|one|another) [a-z ]{0,30}?(?:creature|artifact|permanent)", re.I)
ACT_SAC = re.compile(r"sacrifice (?:a|an|another) (?:[a-z ]{0,20})?creature[^:.]{0,30}:", re.I)


def sac_kind(name, text):
    t = _t(name, text)
    if ADD_SAC.search(t):
        return "spell_cost"
    if ACT_SAC.search(t) and not deaths.is_outlet(t):
        return "ability_cost"
    return None


def payable(games, n, ctx, T, pt):
    makers = ctx.get("token_makers", {})

    def one(tr):
        aug = events.with_tokens(tr, ctx["models"], makers) if makers else tr
        pr = deaths.profile(aug, ctx["creatures"], set(), ctx["commanders"], set(), pt[0], pt[1], False)
        for s, row in zip(aug, pr):
            if s["turn"] > T:
                break
            if n in s["hand"] or n in s["battlefield"]:
                if sum(a for m, a in row["alive"].items() if m != n and m not in ctx["commanders"]) >= 1:
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
                 "artifact/land fodder (only creatures and creature tokens are tracked)"],
                ["fodder must be alive (death layer) at the end of a turn when the card is in hand or on the battlefield"],
                ["Payability, not value: a payable cost can still be a bad trade."],
                ["cost_payable_by_turn"], grid=True)

    @staticmethod
    def matches(name, text, type_line):
        return sac_kind(name, text) is not None

    @classmethod
    def evaluate(cls, b, c, cut, add, cards, ctx):
        return {"module": cls.SPEC["id"], "evidence_class": "test_result", "layer": "deaths",
                "metrics": diff(b, c, cut, add, cards, ctx, payable, cls.matches, grid=True)}
