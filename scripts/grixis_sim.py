#!/usr/bin/env python3
"""M3 goldfish simulator core (Bot cycle 57.2): exact hypergeometric layer + deterministic seeded goldfish games.

What it models (one player, no opponents, no interaction — a goldfish):
  * Library = the canonical list's main deck (quantities kept); commanders start in the command zone (CR 903.6);
    a companion stays outside the game and is ignored.
  * London mulligan (CR 103.5) with the multiplayer free first mulligan (CR 103.5c); no draw skip on turn 1 in
    multiplayer (CR 103.8c; --two-player skips it, CR 103.8a). Keep rule and bottoming rule are fixed and documented
    (KEEP_RULE) so every test pre-registers the same policy.
  * Mana: lands (Scryfall produced_mana; fetch lands produce the land types they can find; unconditional "enters
    tapped" lands are tapped the turn they're played), mana rocks (usable the turn they're cast) and mana creatures
    (usable from the next turn). Colours are paid by bipartite matching of pips to mana units; hybrid pips accept either
    colour; Phyrexian pips are paid with life; X = 0. Commander tax is 2 per earlier cast (CR 903.8).
  * Casting policy each turn: one land (the one adding the most missing colours, untapped first); the commander as soon
    as it's castable; then mana sources, cheapest first; then other permanents and spells, highest mana value first.
    Combo pieces that are instants/sorceries are held, not cast for value.
  * Recorded per game: mulligans taken, kept hand size, lands / mana available / mana spent by turn, commander cast
    turn, first-seen turn of every key-card set (blueprint packages, tutor targets) and of every card, and the
    combo-assembly turn and win-turn proxy for each Commander Spellbook combo in the list.

Win-turn proxy: the first turn on which every piece of some Spellbook combo has been drawn (or is a commander) and the
mana available that turn covers the pieces still to be cast. It is a goldfish proxy: no opponents, no removal, no
"requires" conditions, no tutors or extra card draw. It is not a win rate and is never reported as one.

Exact layer: hyper_* functions (hypergeometric), p_seen_by_turn and p_land_drops (exact dynamic programme). The unit
tests check the Monte Carlo against them.

Usage:
  python3 scripts/grixis_sim.py --deck SLUG [--samples 2000] [--seed 57] [--turns 10] [--json]
  python3 scripts/grixis_sim.py --model SLUG          # parsed mana model (lands, sources, unparsed)
  python3 scripts/grixis_sim.py --selftest            # MC vs exact math on a real deck (validate_all step 'simulator')
"""
import argparse
import hashlib
import json
import math
import random
import re
import sys
from functools import lru_cache
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

NAME = "grixis_sim"
VERSION = "1.1"
MODELS = ("1.0", "1.1")   # every model version stays runnable, so older test records re-run exactly (Bot cycle 57.6)
COLORS = "WUBRG"
BASIC_TYPES = {"Plains": "W", "Island": "U", "Swamp": "B", "Mountain": "R", "Forest": "G"}
KEEP_RULE = ("keep 2-5 lands with (lands + mana sources costing <= 2) >= 3; otherwise mulligan; always keep at 5 cards or fewer; "
             "bottom (London): excess lands beyond 4 first, then the highest mana value nonlands")
MAX_TURNS = 10


def model_sha256():
    return "sha256:" + hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


# ---------------------------------------------------------------- exact layer
def hyper_pmf(N, K, n, k):
    if k < 0 or k > K or k > n or n - k > N - K:
        return 0.0
    return comb(K, k) * comb(N - K, n - k) / comb(N, n)


def hyper_atleast(N, K, n, k):
    return sum(hyper_pmf(N, K, n, i) for i in range(max(k, 0), min(K, n) + 1))


def hyper_between(N, K, n, lo, hi):
    return sum(hyper_pmf(N, K, n, i) for i in range(max(lo, 0), min(hi, K, n) + 1))


def cards_seen(turn, hand=7, skip_first_draw=False):
    """Cards seen by the end of the draw step of `turn` (no mulligan, no extra draws)."""
    return hand + turn - (1 if skip_first_draw else 0)


def p_seen_by_turn(N, K, turn, k=1, hand=7, skip_first_draw=False):
    """P(at least k of the K copies/cards are seen by turn `turn`)."""
    return hyper_atleast(N, K, min(N, cards_seen(turn, hand, skip_first_draw)), k)


def p_land_drops(N, L, turns, hand=7, skip_first_draw=False):
    """Exact P(a land drop available on every turn 1..turns): lands seen by turn t >= t for every t (no mulligan).
    Dynamic programme over the draws; the opening hand is hypergeometric."""
    dist = {l: hyper_pmf(N, L, hand, l) for l in range(0, min(L, hand) + 1)}
    seen = hand
    for t in range(1, turns + 1):
        if not (t == 1 and skip_first_draw):
            nd = {}
            for l, p in dist.items():
                rem, reml = N - seen, L - l
                if rem <= 0:
                    nd[l] = nd.get(l, 0) + p
                    continue
                pl = reml / rem
                nd[l + 1] = nd.get(l + 1, 0) + p * pl
                nd[l] = nd.get(l, 0) + p * (1 - pl)
            dist, seen = nd, seen + 1
        dist = {l: p for l, p in dist.items() if l >= t}
    return sum(dist.values())


# ---------------------------------------------------------------- statistics
def mean_ci(xs):
    n = len(xs)
    if n == 0:
        return None, [None, None]
    m = sum(xs) / n
    if n < 2:
        return m, [m, m]
    sd = math.sqrt(sum((x - m) ** 2 for x in xs) / (n - 1))
    h = 1.96 * sd / math.sqrt(n)
    return m, [m - h, m + h]


def wilson(k, n, z=1.96):
    if n == 0:
        return None, [None, None]
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return p, [max(0.0, c - h), min(1.0, c + h)]


# ---------------------------------------------------------------- card model
def faces(c):
    return c.get("card_faces") or [c]


def front(c):
    return faces(c)[0]


def otext(c):
    return "\n".join(f.get("oracle_text") or "" for f in faces(c)) if c.get("card_faces") else (c.get("oracle_text") or "")


PIP = re.compile(r"\{([^}]+)\}")


def parse_cost(cost):
    """{generic, pips: [frozenset(colours)], life_pips}."""
    g, pips, life = 0, [], 0
    for s in PIP.findall(cost or ""):
        if s.isdigit():
            g += int(s)
        elif s in ("X", "Y", "Z"):
            continue
        elif s == "C":
            pips.append(frozenset("C"))
        elif "/P" in s:
            life += 1
        elif "/" in s:
            parts = s.split("/")
            if parts[0].isdigit():  # {2/B}: pay the colour (cheaper)
                pips.append(frozenset(parts[1]))
            else:
                pips.append(frozenset(p for p in parts if p in COLORS))
        elif s in COLORS:
            pips.append(frozenset(s))
        elif s == "S":
            g += 1
    return {"generic": g, "pips": pips, "life": life}


ADD = re.compile(r"\{T\}(?:, [^:]*)?: Add ([^.]*)\.")
WORDS = {"one": 1, "two": 2, "three": 3}


def mana_amount(add):
    syms = PIP.findall(add)
    if "or" in add.split() and syms:
        return 1
    m = re.match(r"(one|two|three) mana", add)
    if m:
        return WORDS[m.group(1)]
    return max(1, len(syms))


def source_spec(c, ci):
    """(colours, amount) for a permanent that taps for mana every turn, or None (front face only)."""
    t = front(c).get("oracle_text") or ""
    if "doesn't untap during your untap step" in t:
        return None
    m = ADD.search(t)
    pm = None if c.get("card_faces") else c.get("produced_mana")
    if not m:
        return None
    if re.search(r"\{T\}, Sacrifice [^:]*: Add", t):
        return None
    cols = set(pm or []) or set(x for x in PIP.findall(m.group(1)) if x in COLORS + "C")
    cols = {x for x in cols if x == "C" or x in ci}
    if not cols:
        cols = {"C"}
    return frozenset(cols), mana_amount(m.group(1))


def fetch_colors(t, ci):
    m = re.search(r"Search your library for an? ([^.]*?) card", t)
    if not m:
        return None
    s = m.group(1)
    if "basic land" in s:
        return frozenset(ci) or frozenset("C")
    cols = {v for k, v in BASIC_TYPES.items() if k in s}
    cols &= set(ci) | set()
    return frozenset(cols) if cols else None


def enters_tapped(t):
    for l in t.splitlines():
        if re.search(r"enters (the battlefield )?tapped", l) and not re.search(r"unless|you may pay|if you don't|If you control two or fewer", l, re.I):
            if l.lower().startswith(("this land enters tapped", "this land enters the battlefield tapped")) or "enters tapped." in l:
                return True
    return False


NUM = {"a": 1, "an": 1, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7}
CONDITIONAL = {"Chrome Mox": "imprint", "Mox Diamond": "discard_land", "Mox Opal": "metalcraft", "Mox Amber": "legend",
               "Springleaf Drum": "creature", "Paradise Mantle": "creature"}
TYPE_WORDS = ("artifact", "creature", "enchantment", "instant", "sorcery", "planeswalker", "battle", "land")


def _resolve_lines(t, permanent):
    """Oracle lines that happen when the card resolves: a spell's text, or a permanent's 'When ... enters' trigger.
    Activated abilities, 'Whenever' / 'At the beginning' triggers and death triggers are excluded."""
    out = []
    for l in t.splitlines():
        s0 = l.strip()
        if not s0 or s0.startswith("(") or re.match(r"^[^\"]*\{[^}]*\}[^:\"]*:", s0) or re.match(r"^[^\"]*:", s0.split(".")[0]) and "—" not in s0.split(":")[0]:
            continue
        if permanent:
            if re.match(r"^When [^,]* enters", s0):
                out.append(s0)
        elif not re.match(r"^(Whenever|At the beginning|When)", s0):
            out.append(s0)
    return out


def v11_features(c, ci, tl, permanent):
    """Card features used only by model v1.1 (draw, tutors, rituals, one-shot mana, treasures, conditional mana)."""
    t = otext(c) if not c.get("card_faces") else (front(c).get("oracle_text") or "")
    f = {}
    lines = _resolve_lines(t, permanent)
    body = " ".join(lines)
    if not re.search(r"\b(opponent|target player)\b[^.]*\bdraws?\b", body):
        m = re.search(r"\b(?:you |each player )?draws? (a|one|two|three|four|five|six|seven) (?:additional )?cards?", body, re.I)
        if m:
            f["draw"] = NUM[m.group(1).lower()]
        if re.search(r"discards? (their|your) hand", body):
            f["wheel"] = True
            if "draw" not in f and re.search(r"draws? (?:that many|cards equal to)", body):
                f["draw"] = -1  # as many as discarded
        m = re.search(r"then discard (a|one|two|three) cards?", body)
        if m and "draw" in f:
            f["discard_after"] = NUM[m.group(1)]
    if permanent and re.search(r"At the beginning of (?:your upkeep|your draw step)[^.]*\b(?:you )?draws? (?:a|an additional) card", t) and \
            "opponent" not in re.search(r"At the beginning of[^.]*", t).group(0):
        f["upkeep_draw"] = 1
    m = re.search(r"[Ss]earch your library for (a|an) ([^.]*?) card(?: with [^,.]*)?, ([^.]*)", body)
    if m and "land" not in m.group(2) and not re.search(r"Swamp|Island|Mountain|Forest|Plains", m.group(2)):
        rest = m.group(3)
        dest = "graveyard" if "graveyard" in rest else "battlefield" if "onto the battlefield" in rest else "top" if "on top" in rest else "hand"
        if dest != "graveyard":
            words = m.group(2).lower()
            types = {w for w in TYPE_WORDS if w in words}
            if words.strip() in ("", "a") or not re.search(r"[a-z]", words.replace("instant or sorcery", "")) and not types:
                types = set()
            if re.search(r"\b(?:" + "|".join(TYPE_WORDS) + r")\b", words) or words.strip() == "":
                f["tutor"] = {"types": sorted(types), "dest": dest}
            elif words.strip() in ("",):
                f["tutor"] = {"types": [], "dest": dest}
    if re.search(r"[Ss]earch your library for a card[ ,]", body):
        rest = body.split("for a card", 1)[1]
        dest = "graveyard" if "graveyard" in rest.split(".")[0] else "top" if "on top" in rest.split(".")[0] else "hand"
        if dest != "graveyard":
            f["tutor"] = {"types": [], "dest": dest}
    if not permanent:
        m = re.search(r"(?:^|\. )Add ((?:\{[^}]+\})+)", body)
        if m:
            syms = PIP.findall(m.group(1))
            cols = frozenset(x for x in syms if x in ci) or frozenset("C")
            f["ritual"] = (cols, len(syms))
    else:
        name = c["name"]
        if re.search(r"\{T\}, Sacrifice [^:]*: Add ", t) and "Land" not in tl:
            m = re.search(r"\{T\}, Sacrifice [^:]*: Add ([^.]*)\.", t)
            add = m.group(1)
            cols = frozenset(ci) if "any color" in add else frozenset(x for x in PIP.findall(add) if x in ci) or frozenset("C")
            f["oneshot"] = (cols, mana_amount(add), "sacrifice", "commander" if "only to cast your commander" in t else None)
        elif "doesn't untap during your untap step" in t:
            m = ADD.search(t)
            if m:
                f["oneshot"] = (frozenset("C"), mana_amount(m.group(1)), "stays", None)
        if name in CONDITIONAL:
            f["condition"] = CONDITIONAL[name]
    if re.search(r"As an additional cost to cast this spell, discard a card", t):
        f["addl_discard"] = 1
    if re.search(r"discard a card at random", body):
        f["random_discard"] = 1
    kw = c.get("keywords") or []
    m = re.search(r"Suspend (\d+)—((?:\{[^}]+\})+)", t)
    if "Suspend" in kw and m and not (c.get("mana_cost") or front(c).get("mana_cost")):
        f["suspend"] = (int(m.group(1)), parse_cost(m.group(2)))
    m = re.search(r"create (a|one|two|three|four) Treasure tokens?", body)
    if m:
        f["treasures"] = NUM[m.group(1)]
    return f


def card_model(c, ci):
    f0 = front(c)
    tl = f0.get("type_line") or c.get("type_line") or ""
    back = faces(c)[1] if len(faces(c)) > 1 else None
    t = otext(c)
    d = {"name": c["name"], "mv": int(c.get("cmc") or 0), "cost": parse_cost(f0.get("mana_cost") if c.get("card_faces") else c.get("mana_cost")),
         "land": "Land" in tl, "flex_land": bool(back and "Land" in (back.get("type_line") or "") and "Land" not in tl and c.get("layout") == "modal_dfc"),
         "permanent": not any(x in tl for x in ("Instant", "Sorcery")), "creature": "Creature" in tl, "artifact": "Artifact" in tl,
         "gy_text": "graveyard" in t.lower(), "source": None, "tapped": False,
         "legendary": "Legendary" in tl, "types": [w for w in TYPE_WORDS if w in tl.lower()],
         "colors": sorted(set(c.get("colors") or f0.get("colors") or []))}
    d["v11"] = v11_features(c, ci, tl, d["permanent"])
    if d["land"]:
        pm = c.get("produced_mana")
        if pm:
            d["source"] = (frozenset(x for x in pm if x == "C" or x in ci) or frozenset("C"), mana_amount(ADD.search(t).group(1)) if ADD.search(t) else 1)
        else:
            fc = fetch_colors(t, ci)
            d["source"] = (fc, 1) if fc else None
        d["tapped"] = enters_tapped(t)
    elif d["permanent"]:
        d["source"] = source_spec(c, ci)
    if d["flex_land"]:
        bt = back.get("oracle_text") or ""
        m = ADD.search(bt)
        cols = frozenset(x for x in PIP.findall(m.group(1)) if x in ci) if m else frozenset()
        d["flex_source"] = (cols or frozenset("C"), 1)
        d["flex_tapped"] = "enters tapped" in bt or "enters the battlefield tapped" in bt
    return d


class Deck:
    """A simulatable deck: library cards (with quantity), commanders, key sets and combos."""

    def __init__(self, slug, commanders, library, key_sets=None, combos=None, name_order=None):
        self.slug = slug
        self.commanders = commanders          # list of card models
        self.library = library                # list of card models (one per physical card)
        self.key_sets = key_sets or {}        # id -> set(card names)
        self.combos = combos or []            # [{id, cards}]
        self.ci = set()
        self.engine = set()                   # combo pieces + identity-core cards (stress scenario key_engine_exiled)
        self.gy_combo = {}                    # combo id -> any piece's Oracle text mentions a graveyard

    @property
    def N(self):
        return len(self.library)


def load_deck(slug, R=None, text=None):
    """Build a Deck from the canonical project list (or `text`, an import list, for a challenger)."""
    import grixis_authority as ga
    if R is None:
        import evaluate_decklist as ev
        R = ev.Resolver()
    summ = ga.summary()
    did = next(k for k, v in summ.items() if v["slug"] == slug)
    ents = ga.list_entries(text if text is not None else ga.deck_block_text(slug), R)
    cards = {n: R.get(n)[0] for _, _, _, n in ents}
    ci = set().union(*(set(cards[n].get("color_identity", [])) for z, _, _, n in ents if z == "commander"))
    cmds = [card_model(cards[n], ci) for z, _, _, n in ents if z == "commander"]
    lib = []
    for z, _, q, n in sorted(ents, key=lambda e: e[3]):
        if z == "main":
            m = card_model(cards[n], ci)
            lib += [m] * q
    names = {m["name"] for m in lib} | {m["name"] for m in cmds}
    keys = {}
    bp = ROOT / "data" / "grixis" / "blueprints" / f"{slug}.json"
    if bp.exists():
        b = json.loads(bp.read_text(encoding="utf-8"))
        for p in b.get("packages", []):
            s = {x for x in p.get("cards", []) if x in names}
            if s:
                keys[p["id"]] = s
        tt = {x.get("card") for x in b.get("tutor_targets", []) if isinstance(x, dict)} & names
        if tt:
            keys["tutor_targets"] = tt
    combos = []
    cj = ROOT / "data" / "grixis_combos.json"
    if cj.exists():
        src = ga.source_deck_id(did) if hasattr(ga, "source_deck_id") else did
        cd = json.loads(cj.read_text(encoding="utf-8"))["decks"]
        for co in (cd.get(src) or cd.get(did) or {}).get("combos", []):
            if set(co["cards"]) <= names:
                combos.append({"id": co["id"], "cards": list(co["cards"])})
    d = Deck(slug, cmds, lib, keys, combos)
    d.ci = ci
    core = set()
    if bp.exists():
        core = {x.get("card") for x in b.get("identity_core", []) if isinstance(x, dict)} & names
    d.engine = (core | {n for co in combos for n in co["cards"]}) - {m["name"] for m in cmds}
    bym = {m["name"]: m for m in lib + cmds}
    d.gy_combo = {co["id"]: any(bym[n].get("gy_text") for n in co["cards"] if n in bym) for co in combos}
    return d


NOV11 = {}  # cards built without card_model (synthetic tests) have no v1.1 features
TREASURE = {"name": "Treasure", "mv": 0, "cost": {"pips": [], "generic": 0, "life": 0}, "land": False, "flex_land": False, "permanent": True,
            "creature": False, "artifact": True, "gy_text": False, "source": None, "tapped": False, "legendary": False,
            "types": ["artifact"], "colors": [], "v11": {}}


# ---------------------------------------------------------------- payment
def can_pay(cost, units, tax=0):
    """units: list of frozensets (one per mana). Returns indices used, or None. Coloured pips by bipartite matching."""
    pips = cost["pips"]
    need = len(pips) + cost["generic"] + tax
    if need > len(units):
        return None
    match = {}  # unit index -> pip index

    def aug(pi, seen):
        for ui, u in enumerate(units):
            if ui in seen or not (pips[pi] & u):
                continue
            seen.add(ui)
            if ui not in match or aug(match[ui], seen):
                match[ui] = pi
                return True
        return False

    # most-constrained pips first
    for pi in sorted(range(len(pips)), key=lambda i: len(pips[i])):
        if not aug(pi, set()):
            return None
    used = set(match)
    rest = [i for i in range(len(units)) if i not in used]
    # generic: spend the least flexible units first
    rest.sort(key=lambda i: len(units[i]))
    g = cost["generic"] + tax
    if len(rest) < g:
        return None
    return sorted(used | set(rest[:g]))


# ---------------------------------------------------------------- one game
def keep(hand):
    lands = sum(1 for c in hand if c["land"])
    cheap = sum(1 for c in hand if not c["land"] and c["source"] and c["mv"] <= 2)
    return 2 <= lands <= 5 and lands + cheap >= 3


def bottom(hand, k):
    """London mulligan bottoming: lands beyond 4 first, then the highest mana value nonlands, then lands."""
    h, out = list(hand), []
    while len(out) < k:
        lands = [c for c in h if c["land"]]
        nl = sorted([c for c in h if not c["land"]], key=lambda c: (-c["mv"], c["name"]))
        c = lands[-1] if len(lands) > 4 or not nl else nl[0]
        h.remove(c)
        out.append(c)
    return h, out


SCENARIOS = {
    "none": (None, "no perturbation, but scored with the scenario rules (the stress baseline)"),
    # kind: (default T, description) — deterministic perturbations in the same engine (Authority Model, testing doctrine)
    "commander_removed_once": (4, "the commander is removed (to the command zone) at the end of the first turn >= T it is on the battlefield"),
    "commander_removed_twice": (4, "as once, and again at the end of the first turn after the recast that it is back on the battlefield"),
    "graveyard_exiled": (5, "your graveyard is exiled at the end of turn T"),
    "artifacts_wiped": (4, "every nonland artifact you control is destroyed at the end of turn T"),
    "board_wipe": (5, "every nonland creature you control is destroyed at the end of turn T (commanders go to the command zone)"),
    "first_key_spell_countered": (1, "the first key spell you cast (a blueprint package card, tutor target or combo piece; not the commander) is countered"),
    "mana_screw": (3, "no land drop on turns T and T+1"),
    "color_screw": (5, "the colour the commander needs most produces nothing coloured before turn T (those units become {C})"),
    "key_engine_exiled": (1, "the first engine card (combo piece or identity-core card) to reach the battlefield is exiled at the end of that turn"),
}


def screw_colour(deck):
    cnt = {}
    for cm in deck.commanders:
        for p in cm["cost"]["pips"]:
            for x in p:
                if x in COLORS:
                    cnt[x] = cnt.get(x, 0) + 1
    if not cnt:
        for c in deck.library:
            for p in c["cost"]["pips"]:
                for x in p:
                    if x in COLORS:
                        cnt[x] = cnt.get(x, 0) + 1
    return max(sorted(cnt), key=lambda x: cnt[x]) if cnt else None


def play_game(deck, rng, turns=MAX_TURNS, multiplayer=True, skip_first_draw=False, mulligan=True, perm=None, scenario=None,
              model=VERSION):
    """One goldfish game. `perm` (a permutation of library indices) overrides the rng shuffle (paired seeds).
    `scenario`: None or {"kind": one of SCENARIOS, "T": turn} (Bot cycle 57.4).
    `model`: "1.0" (lands, permanent mana sources, commander tax) or "1.1" (adds card draw, tutors, rituals, one-shot
    mana, treasures and conditional fast mana; see MODEL_NOTES). v1.0 behaviour is kept bit-identical."""
    if model not in MODELS:
        raise ValueError(f"unknown model {model!r}; known: {MODELS}")
    v11 = model == "1.1"
    sk = scenario["kind"] if scenario else None
    sT = (scenario.get("T") or SCENARIOS[sk][0]) if scenario else None
    lib_idx = perm if perm is not None else rng.sample(range(deck.N), deck.N)
    lib = [deck.library[i] for i in lib_idx]
    mulls, counted = 0, 0
    while True:
        hand, rest = lib[:7], lib[7:]
        if not mulligan or keep(hand) or len(hand) - counted <= 5:
            break
        mulls += 1
        if not (multiplayer and mulls == 1):
            counted += 1
        if 7 - counted <= 4:
            break
        lib = rng.sample(lib, len(lib))
    hand, bot = bottom(hand, counted)
    library = rest + bot
    seen = {c["name"] for c in hand} | {c["name"] for c in deck.commanders}
    first_seen = {c["name"]: 0 for c in hand}
    battlefield, cmd_zone, graveyard, exile = [], list(deck.commanders), [], []
    cmd_casts = {c["name"]: 0 for c in deck.commanders}
    cmdn = {c["name"] for c in deck.commanders}
    rec = {"mulligans": mulls, "kept": len(hand), "lands": [], "mana": [], "spent": [], "commander_turn": None,
           "key_turn": {k: (0 if s & seen else None) for k, s in deck.key_sets.items()}, "combo_turn": None, "win_turn_proxy": None}
    if scenario:
        rec.update({"cmd_bf": [], "removals": [], "recasts": [], "event_turn": None})
    hold = {n for co in deck.combos for n in co["cards"]}
    key_spells = (set().union(*deck.key_sets.values()) if deck.key_sets else set()) | hold
    key_spells -= cmdn
    engine = getattr(deck, "engine", set()) - cmdn
    gy_combo = getattr(deck, "gy_combo", {})
    bad_colour = screw_colour(deck) if sk == "color_screw" else None
    countered = False
    lands_played = 0
    suspended = []  # v1.1: [turn it resolves, card]
    if v11:
        rec["drawn_extra"] = 0
        rec["tutored"] = []
        rec["fast_mana_used"] = 0
        tut_targets = deck.key_sets.get("tutor_targets", set())
        core = getattr(deck, "engine", set())
    t = 0

    def draw(k, extra=True):
        for _ in range(k):
            if not library:
                return
            c = library.pop(0)
            hand.append(c)
            first_seen.setdefault(c["name"], t)
            seen.add(c["name"])
            if extra:
                rec["drawn_extra"] += 1

    def tutor_pick(types):
        """v1.1 tutor target: the missing piece of the closest combo, else a blueprint tutor target not yet seen,
        else an identity-core card not yet seen, else the highest mana value card of the allowed type."""
        def ok(x):
            return not types or any(ty in x.get("types", []) for ty in types)
        here = {x["name"] for x in hand} | {q["card"]["name"] for q in battlefield} | {x["name"] for x in cmd_zone}
        inlib = {}
        for x in library:
            if ok(x):
                inlib.setdefault(x["name"], x)
        best = None
        for co in deck.combos:
            miss = sorted(n for n in co["cards"] if n not in here)
            if miss and all(n in inlib for n in miss) and (best is None or len(miss) < len(best)):
                best = miss
        if best:
            return inlib[best[0]]
        for pool in (tut_targets, core):
            cand = sorted(n for n in pool if n in inlib and n not in seen)
            if cand:
                return inlib[cand[0]]
        rest = [x for x in inlib.values() if not x["land"]]
        return max(rest, key=lambda x: (x["mv"], x["name"])) if rest else None

    def v11_effects(c):
        """v1.1 resolution effects: draw, wheel, loot, random discard, tutor, treasures. The library is not
        re-shuffled after a search: the rest of it is already in uniformly random order, so this is
        distributionally identical and keeps paired seeds aligned."""
        f = c.get("v11", NOV11)
        if f.get("addl_discard") and hand:  # paid on casting; applied here, before the draw
            keep_h, out = bottom(hand, 1)
            hand[:] = keep_h
            graveyard.extend(out)
        if f.get("wheel"):
            k = len(hand)
            graveyard.extend(hand)
            hand.clear()
            draw(k if f.get("draw") == -1 else f.get("draw", 0))
        elif f.get("draw", 0) > 0:
            draw(f["draw"])
        if f.get("discard_after"):
            keep_h, out = bottom(hand, min(f["discard_after"], len(hand)))
            hand[:] = keep_h
            graveyard.extend(out)
        if f.get("tutor"):
            x = tutor_pick(f["tutor"]["types"])
            if x is not None:
                library.remove(x)
                rec["tutored"].append([t, x["name"]])
                dest = f["tutor"]["dest"]
                if dest == "top":
                    library.insert(0, x)
                elif dest == "battlefield" and x["permanent"]:
                    seen.add(x["name"])
                    first_seen.setdefault(x["name"], t)
                    battlefield.append({"card": x, "_src": x["source"], "_tapped": False, "_sick": True})
                else:
                    hand.append(x)
                    seen.add(x["name"])
                    first_seen.setdefault(x["name"], t)
        if f.get("random_discard") and hand:
            x = hand[rng.randrange(len(hand))]
            hand.remove(x)
            graveyard.append(x)
        for _ in range(f.get("treasures", 0)):
            battlefield.append({"card": TREASURE, "_src": (frozenset(deck.ci) or frozenset("C"), 1), "_tapped": False,
                                "_sick": False, "_once": "sacrifice", "_token": True})

    for t in range(1, turns + 1):
        # untap; sickness ends
        for p in battlefield:
            p["_tapped"] = False
            p["_sick"] = False
        if v11:
            # upkeep: draw triggers, then suspended spells whose last counter comes off
            for p in list(battlefield):
                draw(p["card"].get("v11", NOV11).get("upkeep_draw", 0))
            for e in [e for e in suspended if e[0] == t]:
                suspended.remove(e)
                v11_effects(e[1])
                graveyard.append(e[1])
        if not (t == 1 and skip_first_draw) and library:
            c = library.pop(0)
            hand.append(c)
            first_seen.setdefault(c["name"], t)
            seen.add(c["name"])
        # land drop
        lands = [c for c in hand if c["land"] or c.get("flex_land")]
        if lands and not (sk == "mana_screw" and sT <= t <= sT + 1):
            have = set().union(*[set(p["_src"][0]) for p in battlefield if p.get("_src")]) if battlefield else set()
            want = set()
            for c in hand + cmd_zone:
                for pp in c["cost"]["pips"]:
                    want |= set(pp)
            real = [c for c in lands if c["land"]]
            pool = real or lands

            def score(c):
                src = c["source"] if c["land"] else c["flex_source"]
                tap = c["tapped"] if c["land"] else c["flex_tapped"]
                cols = set(src[0]) if src else set()
                return (len((cols - have) & want), not tap, src[1] if src else 0, c["name"])
            c = max(pool, key=score)
            hand.remove(c)
            src = c["source"] if c["land"] else c["flex_source"]
            p = {"card": c, "_src": src, "_tapped": c["tapped"] if c["land"] else c["flex_tapped"], "_sick": False, "_land": True}
            battlefield.append(p)
            lands_played += 1

        floating = []  # unspent mana from sources tapped this turn (a Sol Ring tapped for one spell keeps its 2nd {C})
        screw_now = bad_colour is not None and t < sT

        def ucol(cols):
            if screw_now and bad_colour in cols:
                cols = frozenset(x for x in cols if x != bad_colour) or frozenset("C")
            return cols

        def units(once=False, cmd=False):
            u = [(None, f) for f in floating]
            for p in battlefield:
                if p.get("_src") and not p["_tapped"] and not (p["_sick"] and p["card"]["creature"]):
                    if p.get("_once") and not once or p.get("_cmdonly") and not cmd:
                        continue
                    src = cond_src(p) if p.get("_cond") else p["_src"]
                    if src:
                        u += [(p, ucol(src[0]))] * src[1]
            return u

        def cond_src(p):
            """v1.1: a conditional fast-mana permanent's current output, or None when its condition fails."""
            k = p["_cond"]
            if k == "imprint" or k == "discard_land":
                return p["_src"]
            if k == "metalcraft":
                return p["_src"] if sum(1 for q in battlefield if q["card"].get("artifact")) >= 3 else None
            if k == "legend":
                cols = set()
                for q in battlefield:
                    qc = q["card"]
                    if qc.get("legendary") and ("creature" in qc.get("types", []) or "planeswalker" in qc.get("types", [])):
                        cols |= set(qc.get("colors", [])) & set(deck.ci)
                return (frozenset(cols), 1) if cols else None
            if k == "creature":
                ok = any(q["card"]["creature"] and not q["_sick"] and not q.get("_src") for q in battlefield)
                return p["_src"] if ok else None
            return None

        avail = len(units(once=v11))
        spent = 0

        def cast(c, tax=0):
            nonlocal spent, floating
            if v11 and c.get("v11", NOV11).get("addl_discard") and not any(x is not c for x in hand):
                return False  # nothing to discard for the additional cost
            us = units()
            cost = c.get("v11", NOV11)["suspend"][1] if v11 and c.get("v11", NOV11).get("suspend") else c["cost"]
            idx = can_pay(cost, [u[1] for u in us], tax)
            if idx is None and v11:
                # one-shot mana (Lotus Petal, Mana Vault, treasures, Jeweled Lotus for the commander) only when needed
                us = units(once=True, cmd=c["name"] in cmdn)
                idx = can_pay(cost, [u[1] for u in us], tax)
            if idx is None:
                return False
            used = set(idx)
            newf = [us[i][1] for i in range(len(us)) if us[i][0] is None and i not in used]
            tapped = {}
            for i in idx:
                if us[i][0] is not None:
                    tapped[id(us[i][0])] = us[i][0]
            srcs_now = {k: (cond_src(p) if p.get("_cond") else p["_src"]) for k, p in tapped.items()}
            for key, p in tapped.items():
                p["_tapped"] = True
                k = sum(1 for i in idx if us[i][0] is p)
                src = srcs_now[key]
                newf += [ucol(src[0])] * (src[1] - k)
                if p.get("_once"):
                    rec["fast_mana_used"] += 1
                    if p["_once"] == "sacrifice":
                        battlefield.remove(p)
                        if not p.get("_token"):
                            graveyard.append(p["card"])
                    else:  # "doesn't untap": used once
                        p["_src"] = None
            floating = newf
            spent += len(idx)
            return True

        def resolve(c, imprint=None):
            """A cast spell resolves (or is countered by the scenario). Returns False when countered."""
            nonlocal countered
            if sk == "first_key_spell_countered" and not countered and c["name"] in key_spells:
                countered = True
                graveyard.append(c)
                rec["event_turn"] = t
                return False
            if v11 and c.get("v11", NOV11).get("suspend"):
                suspended.append([t + c.get("v11", NOV11)["suspend"][0], c])
                return True
            if c["permanent"]:
                e = {"card": c, "_src": c["source"], "_tapped": False, "_sick": True}
                if v11:
                    f = c.get("v11", NOV11)
                    if f.get("oneshot"):
                        cols, amt, how, only = f["oneshot"]
                        e.update({"_src": (cols, amt), "_once": how, "_cmdonly": only == "commander"})
                    if f.get("condition"):
                        e["_cond"] = f["condition"]
                        if f["condition"] == "imprint":
                            e["_src"] = (frozenset(imprint), 1) if imprint else None
                battlefield.append(e)
            else:
                graveyard.append(c)
            if v11:
                v11_effects(c)
            return True

        def cond_choice(c):
            """v1.1: the card a Chrome Mox imprints / a Mox Diamond discards, False when its condition can't be met,
            None when there is nothing to pay. Pure (pays nothing)."""
            k = c.get("v11", NOV11).get("condition") if v11 else None
            if k == "imprint":
                opts = [x for x in hand if x is not c and not x["land"] and not x.get("artifact")
                        and set(x.get("colors", [])) & set(deck.ci) and x["name"] not in key_spells]
                return max(opts, key=lambda x: (x["mv"], x["name"])) if opts else False
            if k == "discard_land":
                ls = [x for x in hand if x["land"]]
                return ls[-1] if ls else False
            return None

        progress = True
        while progress:
            progress = False
            for cm in list(cmd_zone):
                tax = 2 * cmd_casts[cm["name"]]
                if cast(cm, tax):
                    cmd_zone.remove(cm)
                    cmd_casts[cm["name"]] += 1
                    battlefield.append({"card": cm, "_src": cm["source"], "_tapped": False, "_sick": True})
                    if rec["commander_turn"] is None:
                        rec["commander_turn"] = t
                    if scenario and rec["removals"] and len(rec["recasts"]) < len(rec["removals"]):
                        rec["recasts"].append(t)
                    progress = True
            if v11:
                srcs = sorted([c for c in hand if not c["land"] and c["permanent"] and (c["source"] or c.get("v11", NOV11).get("oneshot"))],
                              key=lambda c: (c["mv"], c["name"]))
            else:
                srcs = sorted([c for c in hand if not c["land"] and c["source"] and c["permanent"]], key=lambda c: (c["mv"], c["name"]))
            for c in srcs:
                ch = cond_choice(c)
                if ch is False:
                    continue
                if v11 and c.get("v11", NOV11).get("oneshot") and not c["source"] and c["mv"] > 0 and c.get("v11", NOV11)["oneshot"][2] == "sacrifice":
                    continue  # a paid one-shot (e.g. a 1-mana sacrifice source) is not cast for itself
                if cast(c):
                    hand.remove(c)
                    imp = None
                    if ch is not None:
                        hand.remove(ch)
                        if c.get("v11", NOV11)["condition"] == "imprint":
                            exile.append(ch)
                            imp = sorted(set(ch["colors"]) & set(deck.ci))
                        else:
                            graveyard.append(ch)
                    resolve(c, imp)
                    progress = True
                    break
            if progress:
                continue
            if v11:
                dt = sorted([c for c in hand if not c["land"] and (c.get("v11", NOV11).get("tutor") or c.get("v11", NOV11).get("draw"))
                             and not (not c["permanent"] and c["name"] in hold)], key=lambda c: (c["mv"], c["name"]))
                for c in dt:
                    if c.get("v11", NOV11).get("tutor") and not c.get("v11", NOV11).get("draw") and tutor_pick(c.get("v11", NOV11)["tutor"]["types"]) is None:
                        continue
                    if cast(c):
                        hand.remove(c)
                        resolve(c)
                        progress = True
                        break
                if progress:
                    continue
            others = sorted([c for c in hand if not c["land"] and not (not c["permanent"] and c["name"] in hold)],
                            key=lambda c: (-c["mv"], c["name"]))
            for c in others:
                if v11 and (c.get("v11", NOV11).get("ritual") or c.get("v11", NOV11).get("condition") and cond_choice(c) is False):
                    continue
                if cast(c):
                    hand.remove(c)
                    resolve(c)
                    progress = True
                    break
            if progress or not v11:
                continue
            # ritual check: cast a ritual only if its mana makes an otherwise uncastable card castable
            for r in sorted([c for c in hand if c.get("v11", NOV11).get("ritual")], key=lambda c: (c["mv"], c["name"])):
                snap = (list(floating), [(q, q["_tapped"], q.get("_src")) for q in battlefield], list(battlefield),
                        list(graveyard), spent, rec["fast_mana_used"])
                if not cast(r):
                    continue
                cols, amt = r.get("v11", NOV11)["ritual"]
                floating += [ucol(cols)] * amt
                us = [u[1] for u in units(once=True)]
                targets = [x for x in hand if x is not r and not x["land"] and not x.get("v11", NOV11).get("ritual")
                           and not (not x["permanent"] and x["name"] in hold) and cond_choice(x) is not False]
                good = any(can_pay(x["cost"], us) is not None for x in targets) or \
                    any(can_pay(cm["cost"], us, 2 * cmd_casts[cm["name"]]) is not None for cm in cmd_zone)
                if good:
                    hand.remove(r)
                    graveyard.append(r)
                    rec["fast_mana_used"] += 1
                    progress = True
                    break
                floating[:] = snap[0]
                for q, tp, sr in snap[1]:
                    q["_tapped"] = tp
                    q["_src"] = sr
                battlefield[:] = snap[2]
                graveyard[:] = snap[3]
                spent, rec["fast_mana_used"] = snap[4], snap[5]
        rec["lands"].append(lands_played)
        rec["mana"].append(avail)
        rec["spent"].append(spent)
        for k, s in deck.key_sets.items():
            if rec["key_turn"][k] is None and s & seen:
                rec["key_turn"][k] = t
        if deck.combos and rec["win_turn_proxy"] is None:
            onbf = {p["card"]["name"] for p in battlefield}
            if scenario:
                live = {c["name"] for c in hand} | onbf | {c["name"] for c in cmd_zone}
                gyn = {c["name"] for c in graveyard}
            for co in deck.combos:
                if scenario:
                    ok = all(n in live or (gy_combo.get(co["id"]) and n in gyn) for n in co["cards"])
                else:
                    ok = all(n in seen for n in co["cards"])
                if ok:
                    if rec["combo_turn"] is None:
                        rec["combo_turn"] = t
                    need = 0
                    for n in co["cards"]:
                        if n in onbf:
                            continue
                        m = next((c for c in deck.library if c["name"] == n), None) or next((c for c in deck.commanders if c["name"] == n), None)
                        need += (m["mv"] if m else 0) + (2 * cmd_casts.get(n, 0) if n in cmdn else 0)
                    if avail >= need:
                        rec["win_turn_proxy"] = t
                        break
        # end step: scenario events
        if scenario:
            if sk in ("commander_removed_once", "commander_removed_twice"):
                limit = 1 if sk == "commander_removed_once" else 2
                on = [p for p in battlefield if p["card"]["name"] in cmdn]
                if on and t >= sT and len(rec["removals"]) < limit and len(rec["recasts"]) == len(rec["removals"]):
                    battlefield.remove(on[0])
                    cmd_zone.append(on[0]["card"])
                    rec["removals"].append(t)
                    rec["event_turn"] = rec["event_turn"] or t
            elif sk in ("board_wipe", "artifacts_wiped") and t == sT:
                hit = [p for p in battlefield if not p["card"]["land"] and (p["card"]["creature"] if sk == "board_wipe" else p["card"].get("artifact"))]
                for p in hit:
                    battlefield.remove(p)
                    if p["card"]["name"] in cmdn:
                        cmd_zone.append(p["card"])
                        rec["removals"].append(t)
                    else:
                        graveyard.append(p["card"])
                rec["event_turn"] = t
            elif sk == "graveyard_exiled" and t == sT:
                exile += graveyard
                graveyard.clear()
                rec["event_turn"] = t
            elif sk == "key_engine_exiled" and rec["event_turn"] is None:
                hit = [p for p in battlefield if p["card"]["name"] in engine]
                if hit:
                    battlefield.remove(hit[0])
                    exile.append(hit[0]["card"])
                    rec["event_turn"] = t
            rec["cmd_bf"].append(any(p["card"]["name"] in cmdn for p in battlefield))
    rec["first_seen"] = first_seen
    return rec


# ---------------------------------------------------------------- many games
def seed_for(seed, i):
    return int.from_bytes(hashlib.sha256(f"{seed}:{i}".encode()).digest()[:8], "big")


def run(deck, samples=2000, seed=57, turns=MAX_TURNS, multiplayer=True, skip_first_draw=False, mulligan=True, perms=None,
        model=VERSION):
    recs = []
    for i in range(samples):
        rng = random.Random(seed_for(seed, i))
        recs.append(play_game(deck, rng, turns, multiplayer, skip_first_draw, mulligan, perm=perms[i] if perms else None,
                              model=model))
    return recs


def summarize(deck, recs, turns=MAX_TURNS):
    n = len(recs)
    out = {"samples": n}
    m, ci = mean_ci([r["mulligans"] for r in recs])
    out["mulligans_mean"] = {"value": m, "ci95": ci}
    ct = [r["commander_turn"] for r in recs]
    got = [x for x in ct if x is not None]
    out["commander_cast_by_turn"] = {str(t): wilson(sum(1 for x in got if x <= t), n)[0] for t in (2, 3, 4, 5, 6, turns)}
    out["commander_turn_mean_when_cast"] = mean_ci(got)[0]
    for k in ("lands", "mana", "spent"):
        out[f"{k}_by_turn"] = [round(sum(r[k][t] for r in recs) / n, 3) for t in range(turns)]
    out["key_access_by_turn4"] = {k: wilson(sum(1 for r in recs if r["key_turn"][k] is not None and r["key_turn"][k] <= 4), n)[0] for k in deck.key_sets}
    if deck.combos:
        w = [r["win_turn_proxy"] for r in recs]
        out["win_turn_proxy_by_turn"] = {str(t): sum(1 for x in w if x is not None and x <= t) / n for t in (4, 6, 8, turns)}
        out["combo_assembled_by_turn"] = {str(t): sum(1 for r in recs if r["combo_turn"] is not None and r["combo_turn"] <= t) / n for t in (4, 6, 8, turns)}
    return out


# fast mana whose condition the model does not check (it's treated as unconditional): listed in model_report and
# in every test record's limitations
CONDITIONAL_SOURCES = {"Chrome Mox", "Mox Diamond", "Mox Opal", "Mox Amber", "Springleaf Drum", "Paradise Mantle"}


def model_report(deck):
    lands = [c for c in deck.library if c["land"]]
    rep = {"N": deck.N, "lands": len(lands), "lands_no_mana": sorted({c["name"] for c in lands if not c["source"]}),
           "tapped_lands": sorted({c["name"] for c in lands if c["tapped"]}),
           "mana_sources": sorted({c["name"] for c in deck.library if not c["land"] and c["source"]}),
           "flex_lands": sorted({c["name"] for c in deck.library if c.get("flex_land")}),
           "conditional_sources": sorted({c["name"] for c in deck.library if c["name"] in CONDITIONAL_SOURCES}),
           "commanders": [{"name": c["name"], "mv": c["mv"]} for c in deck.commanders],
           "key_sets": {k: len(v) for k, v in deck.key_sets.items()}, "combos": len(deck.combos)}
    inv = {}
    for c in deck.library + deck.commanders:
        for k in ("draw", "upkeep_draw", "tutor", "ritual", "oneshot", "treasures", "condition", "suspend", "wheel"):
            if c.get("v11", {}).get(k):
                inv.setdefault(k, set()).add(c["name"])
    rep["v1_1_features"] = {k: sorted(v) for k, v in sorted(inv.items())}
    return rep


# what each model version simulates and leaves out (copied into every test record's limitations)
MODEL_NOTES = {
    "1.0": ["Model 1.0: lands, permanent mana sources and commander tax only; no card draw beyond the draw step, no "
            "tutors, rituals, one-shot mana or treasures; conditional fast mana (" + ", ".join(sorted(CONDITIONAL_SOURCES)) +
            ") is treated as unconditional."],
    "1.1": ["Model 1.1 adds: draw on resolution / enters triggers (incl. wheels and loot discards), upkeep/draw-step "
            "draw triggers, suspend timing, tutors (spell or enters trigger; to hand, top or battlefield; target = missing "
            "piece of the closest combo, else a blueprint tutor target, else an identity-core card, else the highest-MV "
            "legal card; no re-shuffle, which is distributionally identical), rituals (cast only when they enable an "
            "otherwise uncastable card), one-shot mana (sacrifice sources, doesn't-untap rocks, Jeweled Lotus for the "
            "commander only, spent only when needed), treasures from resolution / enters effects, and the conditions of "
            + ", ".join(sorted(CONDITIONAL_SOURCES)) + " (imprint / land discard / metalcraft / a legend's colours / an "
            "untapped non-mana creature).",
            "Model 1.1 still leaves out: opponent-dependent draw (Rhystic Study, Mystic Remora), activated or repeating "
            "draw and tutors (Sensei's Divining Top, Tamiyo's Journal, Wishclaw Talisman), attack/cast/death triggers, "
            "Lion's Eye Diamond, sacrifice additional costs (Deadly Dispute, Culling the Weak: not paid; 'discard a card' "
            "additional costs are paid), X costs, Paradise Mantle's equip cost, graveyard tutors (Entomb, Buried Alive) and "
            "recursion, discard to hand size."],
}


def selftest_v11(samples=3000):
    """Model v1.1 vs exact math on synthetic decks (draw engine seen count, tutor hypergeometric). Returns problems."""
    def mk(name, cost, permanent=True, **v11):
        c = parse_cost(cost)
        return {"name": name, "mv": c["generic"] + len(c["pips"]), "cost": c, "land": False, "flex_land": False,
                "permanent": permanent, "creature": False, "artifact": False, "source": None, "tapped": False,
                "legendary": False, "types": [], "colors": [], "v11": v11}

    def lnd(i):
        return dict(mk(f"Land {i}", ""), land=True, source=(frozenset("B"), 1))
    p = []
    fill = [mk(f"Filler {i}", "{9}") for i in range(61)]
    d = Deck("selftest-engine", [mk("Engine", "", upkeep_draw=1)], [lnd(i) for i in range(38)] + fill)
    d.ci = {"B"}
    bad = 0
    for i in range(200):
        r = play_game(d, random.Random(seed_for(2, i)), turns=8, mulligan=False, model="1.1")
        bad += any(sum(1 for v in r["first_seen"].values() if v <= t) != cards_seen(t) + (t - 1) for t in range(1, 9))
    print(f"  v1.1 upkeep-draw engine: cards seen by turn t == 7 + t + (t-1) in {200 - bad}/200 games ({'ok' if not bad else 'OFF'})")
    if bad:
        p.append(f"v1.1 upkeep draw: {bad} games off the exact count")
    lib = [mk("Tutor", "", permanent=False, tutor={"types": [], "dest": "hand"}), mk("Target", "{9}")] + [lnd(i) for i in range(36)] + fill
    d = Deck("selftest-tutor", [mk("Cmd", "{9}")], lib, {"tutor_targets": {"Target"}})
    d.ci = {"B"}
    hits = sum(1 for i in range(samples) if (play_game(d, random.Random(seed_for(3, i)), turns=4, mulligan=False, model="1.1")
                                            ["first_seen"].get("Target", 99) <= 4))
    exact = hyper_atleast(d.N, 2, cards_seen(4), 1)
    se = math.sqrt(exact * (1 - exact) / samples)
    ok = abs(hits / samples - exact) <= 4 * se
    print(f"  v1.1 free tutor: P(target in hand by turn 4) MC {hits / samples:.4f} vs exact {exact:.4f} ({'ok' if ok else 'OFF'}; 4 SE = {4 * se:.4f})")
    if not ok:
        p.append("v1.1 tutor probability off")
    return p


def selftest(slug="wick-the-whorled-mind", samples=4000):
    """Monte Carlo (mulligans off) vs exact math on a real deck (model 1.0: no extra draws or tutors, so the
    hypergeometric layer is exact), then the v1.1 synthetic checks. Returns problems."""
    deck = load_deck(slug)
    recs = run(deck, samples, seed=1, mulligan=False, model="1.0")
    N = deck.N
    L = sum(1 for c in deck.library if c["land"])
    p = []

    def close(name, mc, exact):
        se = math.sqrt(max(exact * (1 - exact), 1e-9) / samples)
        ok = abs(mc - exact) <= 4 * se + 1e-9
        print(f"  {name}: MC {mc:.4f} vs exact {exact:.4f} ({'ok' if ok else 'OFF'}; 4 SE = {4 * se:.4f})")
        if not ok:
            p.append(f"{name}: MC {mc:.4f} vs exact {exact:.4f}")

    # lands in the opening 7 (same seeds and shuffles as the games)
    rng_hands = []
    for i in range(samples):
        rng = random.Random(seed_for(1, i))
        idx = rng.sample(range(N), N)
        rng_hands.append(sum(1 for j in idx[:7] if deck.library[j]["land"]))
    close("P(3-4 lands in opening 7)", sum(1 for x in rng_hands if 3 <= x <= 4) / samples, hyper_between(N, L, 7, 3, 4))
    # land drop every turn through 4 (land count by turn = min(t, lands seen))
    LF = L + sum(1 for c in deck.library if c.get("flex_land"))  # modal DFC lands also make land drops
    close("P(land drop on each of turns 1-4)", sum(1 for r in recs if r["lands"][3] >= 4) / samples, p_land_drops(N, LF, 4))
    # a specific singleton card seen by turn 5
    name = sorted({c["name"] for c in deck.library if not c["land"]})[0]
    K = sum(1 for c in deck.library if c["name"] == name)
    close(f"P({name} seen by turn 5)", sum(1 for r in recs if r["first_seen"].get(name, 99) <= 5) / samples, p_seen_by_turn(N, K, 5))
    for k, s in deck.key_sets.items():
        K = sum(1 for c in deck.library if c["name"] in s)
        if K and all(n not in {c["name"] for c in deck.commanders} for n in s):
            close(f"P(any of {k} ({K} cards) seen by turn 4)", sum(1 for r in recs if r["key_turn"][k] is not None and r["key_turn"][k] <= 4) / samples, p_seen_by_turn(N, K, 4))
            break
    # v1.1 on the same deck: the opening hand is untouched by the new model (same seeds)
    r11 = run(deck, 200, seed=1, mulligan=False, model="1.1")
    if [sorted(n for n, v in r["first_seen"].items() if v == 0) for r in r11] != \
            [sorted(n for n, v in r["first_seen"].items() if v == 0) for r in recs[:200]]:
        p.append("v1.1 changed the opening hands")
    else:
        print("  v1.1: opening hands identical to v1.0 on the same seeds (200/200)")
    p += selftest_v11()
    return p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--deck")
    ap.add_argument("--model")
    ap.add_argument("--samples", type=int, default=2000)
    ap.add_argument("--seed", type=int, default=57)
    ap.add_argument("--turns", type=int, default=MAX_TURNS)
    ap.add_argument("--two-player", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        print(f"{NAME} v{VERSION} selftest (model {model_sha256()[:19]}…):")
        p = selftest()
        print(f"selftest: {len(p)} problem(s)")
        return 1 if p else 0
    if a.model:
        print(json.dumps(model_report(load_deck(a.model)), indent=1, ensure_ascii=False))
        return 0
    if a.deck:
        d = load_deck(a.deck)
        recs = run(d, a.samples, a.seed, a.turns, multiplayer=not a.two_player, skip_first_draw=a.two_player)
        s = summarize(d, recs, a.turns)
        s.update({"deck": a.deck, "seed": a.seed, "simulator": {"name": NAME, "version": VERSION, "model_sha256": model_sha256()}, "keep_rule": KEEP_RULE})
        print(json.dumps(s, indent=1) if a.json else json.dumps(s, indent=1))
        return 0
    ap.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
