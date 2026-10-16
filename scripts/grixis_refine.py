#!/usr/bin/env python3
"""Grixis commander-first refinement (Bot cycle 39+, Cory's mission: grixis/Grixis Mission.md).

Measures every Grixis deck (62 pages, pending-legality decks included and noted):
  * commander dependence: share of nonland, non-commander cards that either match an Oracle "hook" taken from
    the commander's own text (see HOOKS) or have EDHREC synergy >= DEP_SYN % on the commander's EDHREC page;
  * homogenization: mean / max pairwise Jaccard overlap of nonland cards with the other 61 lists, generic share
    (cards with no commander link that appear in >= GENERIC_MIN of the 62 lists), Thoracle-core and control-core counts.
Plans card-level swaps for one batch (--plan N --decks id,id,...). A plan is frozen in data/grixis_refine_batches.json
(decisions never drift when Scryfall or EDHREC data change); every later run re-verifies the refined lists.
Renders: the <!-- REFINED --> block on each planned deck page (refined list + per-deck refinement log),
grixis/Grixis Refinement Cycle.md, data/grixis_refinement.json, and exports/grixis-archidekt/ (one Archidekt
import .txt per deck, ALL-DECKS.txt, README.md).
Bot cycle 47 (M0, authority model): v1 is frozen and kept reproducible (`--engine v1 --plan N`); its outputs are
GrokBot challengers (unapproved) or "heuristic: no candidate passed v1 gates (not a certificate)". v2 (`--engine v2`)
writes exploratory recommendations to data/grixis_refine_v2.json and never publishes a final list.
Usage:
  python3 scripts/grixis_refine.py --engine v1 --plan 1 --decks A,B,...   # reproduce a v1 batch (queries Commander Spellbook)
  python3 scripts/grixis_refine.py --engine v2 [--decks A,B]              # exploratory v2 recommendations (offline)
  python3 scripts/grixis_refine.py                             # render everything from frozen plans
  python3 scripts/grixis_refine.py --check                     # validate_all: outputs current + exports match pages
"""
import atomic_io  # noqa: F401  atomic Path.write_text (Bot cycle 34)
import argparse, datetime as dt, json, re, sys, time, unicodedata
from collections import Counter
from itertools import combinations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ingest_scryfall as ing  # noqa: E402
import evaluate_decklist as ev
import grixis_authority as ga  # noqa: E402
import detect_combos as dc  # noqa: E402
from deck_calibration import RX  # noqa: E402

ROOT = ing.ROOT
SUM = ROOT / "data" / "grixis_summary.json"
COMBOS = ROOT / "data" / "grixis_combos.json"
PLANS = ROOT / "data" / "grixis_refine_batches.json"
OUT = ROOT / "data" / "grixis_refinement.json"
PAGE = ROOT / "grixis" / "Grixis Refinement Cycle.md"
EXP = ROOT / "exports" / "grixis-archidekt"
EDH = ROOT / ".cache" / "edhrec"
START, END = "<!-- REFINED:START -->", "<!-- REFINED:END -->"
I = "https://github.com/corymstover/GrokBotMTGCompanion/issues/"
DEP_SYN, ADD_SYN, ADD_INC, CUT_SYN, GENERIC_MIN, MAX_SWAPS = 15, 15, 5.0, 5, 16, 5
CEIL_DEP, CEIL_GEN = 0.60, 0.15
KEY_ROLES = ("ramp", "draw", "removal", "wipe", "counter", "protection", "tutor")
THORACLE = {"Thassa's Oracle", "Demonic Consultation", "Tainted Pact", "Laboratory Maniac", "Jace, Wielder of Mysteries"}
CONTROL = {"Counterspell", "Mana Drain", "Force of Will", "Force of Negation", "Fierce Guardianship", "Pact of Negation",
           "Swan Song", "Flusterstorm", "Mental Misstep", "Dovin's Veto", "An Offer You Can't Refuse", "Spell Pierce",
           "Mystic Remora", "Rhystic Study", "Cyclonic Rift", "Toxic Deluge", "Deadly Rollick", "Snuff Out",
           "Deflecting Swat", "Mindbreak Trap", "Arcane Denial", "Negate", "Delay", "Stern Scolding"}
# (label, regex on the commander's Oracle text, regex on a card's Oracle text + type line). Facts: both sides are
# Scryfall Oracle text; the hook only says the card's text touches the same mechanic the commander's text names.
HOOKS = [
    ("cascade / cheap spells", r"\bcascade\b", r"\bcascade\b|\bdiscover \d"),
    ("opponents losing life", r"life (your )?opponents? (have |has )?lost|lost \d+ or more life|each opponent loses",
     r"each opponent loses|loses? \d+ life|deals? (\d+|X) damage to (each opponent|any target|target player|each player|that player)"),
    ("stealing / casting opponents' cards", r"gain control|you control but don't own|you don't own|an opponent owns",
     r"gain control|exchange control|you don't own|an opponent owns|cast (it|that card|them|spells?) [^.]*exiled|exile the top [^.]* (of|from) (each|target) (opponent|player)"),
    ("combat damage / attack triggers", r"combat damage to (a|that) player|dealt combat damage|whenever [^.]* attacks|deals damage to an opponent",
     r"\bhaste\b|can't be blocked|additional combat|extra combat|\bdouble strike\b|whenever [^.]* (attacks|deals combat damage)|\bmenace\b"),
    ("graveyard as a resource", r"from your graveyard|into your graveyard|\bmill\b|\bdies\b",
     r"\bmill\b|\bsurveil\b|\bdredge\b|from (your|a) graveyard|into your graveyard|\bdiscard\b|\breanimate\b|return target creature card"),
    ("artifacts", r"\bartifacts?\b", r"^[^\n]*Artifact|\bartifacts?\b|\bTreasure\b|\bClue\b"),
    ("sacrifice", r"\bsacrific", r"\bsacrific|\bdies\b|\bTreasure\b|creates? [^.]*tokens?"),
    ("activated abilities", r"activate an ability", r"[Ss]acrifice [^:\n]*:|\{T\}[^:\n]*:|\bcopy target activated\b|\buntap\b"),
    ("copying", r"\bcopy\b|\bcopies\b", r"\bcopy\b|\bcopies\b"),
    ("instants and sorceries", r"instant (or|and/or|and) sorcery|noncreature spell", r"^Instant|^Sorcery|instant (or|and/or|and) sorcery|noncreature spell"),
    ("card draw / hand size", r"hand size|cards in your hand|whenever you draw|or more cards in your hand", r"\bdraws? (a|one|two|three|four|X|that many) cards?\b|hand size|each player draws"),
    ("goad / forced attacks", r"\bgoad", r"\bgoad|attacks each combat if able|attack[^.]* if able"),
    ("discard", r"\bdiscard", r"\bdiscard|\bmadness\b|\bcycling\b|\bconnive"),
    ("tokens", r"create [^.]*tokens?", r"tokens?|\bpopulate\b"),
    ("+1/+1 counters", r"\+1/\+1 counters?", r"\+1/\+1 counters?|\bproliferate\b"),
    ("Treasure", r"\bTreasure\b", r"\bTreasure\b"),
    ("playing cards from exile", r"play (a card|cards|lands and cast spells) from exile|cast [^.]* from exile|exile the top card of each player's library",
     r"from exile|exile the top|collection counter|cast [^.]* exiled|you may play (that card|it|them|those cards)"),
    ("flash", r"^Flash$", r"\bflash\b"),
    ("opponents drawing (wheels / punishers)", r"whenever an opponent draws|draws an additional card|each player draws",
     r"each (player|opponent) draws|target player draws|each player discards (their|his or her) hand|draws? seven cards|whenever an opponent draws|draws an additional card|\bwheel"),
    ("crimes (targeting opponents and their things)", r"commit a crime",
     r"\btarget (player|opponent|spell|creature|permanent|nonland permanent|artifact|enchantment|planeswalker|land|activated|triggered|instant|noncreature)|\bcounter target\b|\bany target\b|an opponent controls|card in a graveyard|from an opponent's graveyard"),
    ("enters triggers", r"whenever (another|a|one or more|[^.]* or another) [^.]* enters", r"\bflicker|exile [^.]*, then return|return [^.]* to the battlefield|enters[^.]* an additional time"),
    ("casualty / power 2 or greater", r"\bcasualty\b|power 2 or greater", r"\bcasualty\b|creates? [^.]*\d/\d"),
    ("connive / looting", r"\bconniv", r"\bconniv|draw a card, then discard|discard a card, then draw"),
    # Bot cycle 43: hook gaps found in batch 5 (commanders whose text matched no hook)
    ("unearth / creature cards in your graveyard", r"\bunearth\b",
     r"\bunearth\b|\bmill\b|into your graveyard|creature cards? (from your library )?(in|into) your graveyard|When [^.]* enters"),
    ("black spells / Swamps", r"casts a black spell|\bswampwalk\b", r"\bSwamps?\b|\bswampwalk\b"),
    ("tapping / blocking creatures", r"tapped or blocking creature",
     r"\btap (target|up to|all|each)\b[^.]*creatures?|doesn't untap|don't untap|\buntap target\b|copy target activated|\bgoad|tapped creature"),
    ("life gain", r"you gain \d+ life|you gain life", r"whenever you gain life|\bgain(s)? [^.]*life\b|\blifelink\b|life total"),
    # Bot cycle 44: The Madcap Jester ("causes one or more cards to be exiled from an opponent's library, you may play those cards")
    ("exiling and playing opponents' library cards", r"exiled from an opponent's library|each opponent exiles the top card",
     r"exiles? the top [^.]*of (each|target|that) (opponent's|player's|opponent|player)|each opponent exiles the top|from an opponent's library|opponent's library[^.]*exile|exile [^.]*opponent's library|you may (play|cast) [^.]*exiled"),
    ("villainous choices / voting", r"villainous choice|\bvot(e|ing)\b", r"villainous choice|\bvotes?\b|\bcouncil's dilemma\b|will of the council"),
]
CTYPES = None
REVIEW = ROOT / "data" / "grixis_refine_review.json"
FREE = re.compile(r"(cast|play) this spell without paying its mana cost|rather than pay this spell's mana cost|rather than pay its mana cost", re.I)
RANK_X, RANK_PLUS = 4, 2000


def guard(k, c, ctx):
    """Bot cycle 40 power guard: (ok, [reasons]). The add must not be a clear power downgrade of the cut."""
    why, bad = [], []
    ks, cs = ctx.syn.get(k["name"]), ctx.syn.get(c["name"])
    if ks and cs and cs[1] < ks[1]:
        bad.append(f"commander-page inclusion {cs[1]}% < cut's {ks[1]}% (this commander's players keep the cut more often)")
    else:
        why.append(f"commander-page inclusion {cs[1] if cs else '?'}% vs cut {str(ks[1]) + '%' if ks else 'not listed'}")
    rk, rc = k.get("edhrec_rank"), c.get("edhrec_rank")
    if rk and (not rc or rc > max(RANK_X * rk, rk + RANK_PLUS)):
        bad.append(f"overall EDHREC rank {rc or 'none'} vs cut {rk} (more than {RANK_X}x / +{RANK_PLUS} worse)")
    else:
        why.append(f"overall EDHREC rank {rc} vs {rk}")
    if FREE.search(otext(k)) and not FREE.search(otext(c)):
        bad.append("the cut can be cast for free; the add cannot (tempo downgrade)")
    return (not bad), (bad or why)


def load_review():
    return json.loads(REVIEW.read_text(encoding="utf-8")) if REVIEW.exists() else {"_doc": "", "swaps": {}, "overlap": {}}


def rkey(did, cut, add):
    return f"{did}|{cut}|{add}"


def ctypes():
    global CTYPES
    if CTYPES is None:
        t = sorted((ROOT / ".cache").glob("MagicCompRules-*.txt"))[-1].read_text(encoding="utf-8", errors="ignore")
        m = re.search(r"^205\.3m [^:]*: (.*)$", t, re.M)
        CTYPES = [x.strip().rstrip(".") for x in m.group(1).split(",")]
    return CTYPES


def otext(c):
    return ev.oracle(c)


def tline(c):
    return c.get("type_line") or " // ".join(f.get("type_line", "") for f in c.get("card_faces") or [])


def is_land(c):
    return "Land" in (c.get("card_faces") or [c])[0].get("type_line", c.get("type_line", "")).split("—")[0]


def sentence(text, m):
    a = max(text.rfind("\n", 0, m.start()), text.rfind(". ", 0, m.start()) + 1)
    b = min([x for x in (text.find("\n", m.end()), text.find(". ", m.end())) if x != -1] or [len(text)])
    return text[a:b].strip().lstrip(". ").strip()


def eslug(name):
    n = unicodedata.normalize("NFKD", name.split(" // ")[0]).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[ ]+", "-", re.sub(r"[^a-z0-9 -]", "", n).strip())


def edhrec(cmds):
    """EDHREC synergy (community data, cached JSON): name -> (synergy %, inclusion %, num_decks, potential)."""
    slugs = ["-".join(sorted(eslug(c) for c in cmds))] if len(cmds) > 1 else []
    slugs += [eslug(c) for c in cmds]
    out, used = {}, []
    for s in slugs:
        p = EDH / f"commanders__{s}.json"
        if not p.exists():
            continue
        d = json.loads(p.read_text(encoding="utf-8"))
        if "container" not in d:
            continue
        used.append(s)
        for cl in d["container"]["json_dict"].get("cardlists", []):
            if cl.get("tag") in ("newcards", "topcommanders", "newcommanders"):
                continue
            for v in cl.get("cardviews", []):
                if v.get("synergy") is None or not v.get("potential_decks"):
                    continue
                x = (round(100 * v["synergy"]), round(100 * v["num_decks"] / v["potential_decks"], 1), v["num_decks"], v["potential_decks"])
                out.setdefault(v["name"], x)  # pair page first, then each partner's own page
        if len(cmds) > 1 and s == slugs[0]:
            break
    return out, used


class Ctx:
    def __init__(self, cmd_cards):
        self.cmds = cmd_cards
        self.hooks = []
        for c in cmd_cards:
            t = otext(c)
            own = set(re.findall(r"[A-Za-z']+", c["name"]))
            for lab, crx, krx in HOOKS:
                m = re.search(crx, t, re.I)
                if m:
                    self.hooks.append((lab, c["name"], sentence(t, m), re.compile(krx, re.I | re.M)))
            for ty in ctypes():
                if ty in own:
                    continue
                m = re.search(r"\b" + re.escape(ty) + r"s?\b", t)
                if m:
                    self.hooks.append((f"{ty} synergy", c["name"], sentence(t, m), re.compile(r"\b" + re.escape(ty) + r"s?\b")))
        self.syn, self.pages = edhrec([c["name"] for c in cmd_cards])

    def hook(self, c):
        body = tline(c) + "\n" + otext(c)
        for lab, cn, frag, rx in self.hooks:
            m = rx.search(body)
            if m:
                ev_ = sentence(body, m) if m.start() >= len(tline(c)) else tline(c)
                return {"label": lab, "commander": cn, "commander_text": frag, "card_text": ev_}
        return None

    def dependent(self, c):
        s = self.syn.get(c["name"])
        return bool(self.hook(c)) or bool(s and s[0] >= DEP_SYN)


EXTRA_RX = {  # wider than deck_calibration.RX: a cut must never silently drop interaction
    "wipe": re.compile(r"\ball creatures get -|\beach creature gets -|\b(destroy|exile) all\b|\breturn all\b|damage to each creature", re.I),
    "removal": re.compile(r"\bowner of target [^.]*shuffles|\bput target [^.]* on (the )?(top|bottom)|\breturn target [^.]* to its owner's hand|\bgain control of target|damage to target (creature|planeswalker|permanent)|\btarget [^.]* gets -\d+/-\d+", re.I),
    "protection": re.compile(r"\b(target|equipped|enchanted) (creature|permanent)[^.]*\b(hexproof|shroud|indestructible|phases? out)\b|\bnew targets? for target\b|\bchange the target", re.I),
    "draw": re.compile(r"\bdraws? cards equal\b|\bthen draws?\b|\bdraws? (a|one|two|three|seven|X) cards?\b|\bdraw that many\b", re.I),
    "counter": re.compile(r"\bcounter (target|that|it|all)\b", re.I),
}
INTERACTION = {"removal", "wipe", "counter", "protection"}


NOT_REMOVAL = re.compile(r"target ([\w-]+ ){0,3}card\b|graveyard|target ([\w-]+ ){0,3}you control|until end of turn", re.I)


def roles(c):
    t = re.sub(r"\([^)]*\)", "", otext(c))  # reminder text (e.g. ward's "counter it unless") is not a role
    out = set()
    for k in KEY_ROLES:
        rxs = [RX[k]] + ([EXTRA_RX[k]] if k in EXTRA_RX else [])
        for rx in rxs:
            for m in rx.finditer(t):
                if k == "removal" and NOT_REMOVAL.search(sentence(t, m)):
                    continue  # graveyard hate, self-blink and temporary theft are not spot removal
                if k == "counter" and re.search(r"\bward\b", sentence(t, m), re.I):
                    continue  # ward is not a counterspell
                if k == "protection" and re.search(r"this creature|" + re.escape(c["name"].split(",")[0]), sentence(t, m)):
                    continue  # a creature protecting itself does not protect the commander
                out.add(k)
    return out


def deck_block(p):
    m = re.search(r"## Decklist[^\n]*\n.*?```[^\n]*\n(.*?)```", p.read_text(encoding="utf-8"), re.S)
    return m.group(1)


def lines_of(text, R):
    """[(qty, card, zone)] from an import list."""
    out = []
    for e in ev.parse(text):
        c, _ = R.get(e["name"])
        z = "commander" if "commander" in e["tags"].lower() else "companion" if "companion" in e["tags"].lower() else "main"
        out.append((e["qty"], c, z))
    return out


def nonland_names(lst):
    return {c["name"] for q, c, z in lst if z == "main" and not is_land(c)}


def apply_swaps(src_text, swaps):
    cuts = {s["cut"] for s in swaps}
    keep = [l for l in src_text.strip().splitlines() if not any(re.match(r"^1x? " + re.escape(n) + r"( \[|$| \()", l.strip()) for n in cuts)]
    return "\n".join(keep + [f"1x {s['add']} [Refined (Bot cycle {s['cycle']})]" for s in swaps]) + "\n"


def hard(res, pending_cards=(), deck_id=None):
    """Hard failures. Bot cycle 47: registered, Cory-authorized project exceptions (data/grixis/exceptions.json) are
    accepted for `deck_id` on Commander legality only; callers must still label them NOT Commander-legal."""
    out = [i for i in res["issues"] if i["type"] in ev.HARD and not (i["type"] == "not Commander-legal" and i["card"] in pending_cards)]
    return ga.accepted_hard_issues(deck_id, out)[0] if deck_id else out


def spellbook(lst, cache, did, fetch):
    cmd = [c["name"] for q, c, z in lst if z == "commander"]
    mn = [c["name"] for q, c, z in lst if z == "main"]
    sig = sorted(cmd + mn)
    if did in cache and cache[did]["sig"] == sig:
        return cache[did]
    if not fetch:
        return None
    res = dc.query(cmd, mn)
    rows = [{"id": v["id"], "cards": [u["card"]["name"] for u in v["uses"]], "infinite": dc.infinite(v)} for v in res["included"]]
    cache[did] = {"sig": sig, "combos": rows, "queried": dt.date.today().isoformat()}
    time.sleep(1)
    return cache[did]


def target_of(v):
    m = re.match(r"(\d)", v.get("src_claim") or "")
    return int(m.group(1)) if m else v["floor"]


def plan(dids, batch, R, summ, plans, cycle):
    combos = json.loads(COMBOS.read_text(encoding="utf-8"))["decks"]
    lists = {d: lines_of(ga.challenger_base(d, deck_block(ROOT / "grixis" / "decks" / f"{v['slug']}.md"))[0], R) for d, v in summ.items()}
    freq = Counter(n for l in lists.values() for n in nonland_names(l))
    cache = plans.setdefault("spellbook", {})
    reg = json.loads((ROOT / "data" / "grixis_pending.json").read_text(encoding="utf-8"))["decks"]
    for did in dids:
        v = summ[did]
        src = ga.challenger_base(did, deck_block(ROOT / "grixis" / "decks" / f"{v['slug']}.md"))[0]
        lst = lists[did]
        ctx = Ctx([c for q, c, z in lst if z == "commander"])
        have = {c["name"] for q, c, z in lst}
        pend = reg.get(did, {}).get("cards", []) if reg.get(did, {}).get("status") == "pending" else []
        ci = set().union(*(set(c.get("color_identity", [])) for c in ctx.cmds))
        gcn = sum(1 for q, c, z in lst if c.get("game_changer"))
        tgt = target_of(v)
        xturn = any("extra turn" in otext(c).lower() for q, c, z in lst)
        nl = [c for q, c, z in lst if z == "main" and not is_land(c)]
        dep = sum(ctx.dependent(c) for c in nl) / len(nl)
        gen = sum(1 for c in nl if not ctx.dependent(c) and freq[c["name"]] >= GENERIC_MIN) / len(nl)
        entry = {"deck": did, "batch": batch, "cycle": cycle, "date": dt.date.today().isoformat(), "swaps": [], "decision": "", "edhrec_pages": ctx.pages}
        if dep >= CEIL_DEP and gen <= CEIL_GEN and not load_review().get("manual_swaps", {}).get(did):
            entry["decision"] = f"at/near ceiling: commander dependence {dep:.0%} ≥ {CEIL_DEP:.0%} and generic share {gen:.0%} ≤ {CEIL_GEN:.0%}; unchanged"
            plans["decks"][did] = entry
            continue
        pieces = {n for co in combos.get(did, {}).get("combos", []) for n in co["cards"]}
        cuts = []
        keep = set(load_review().get("protect", {}).get(did, {}).get("cards", []))  # manual review: deck core, never cut
        for c in nl:
            if c["name"] in keep:
                continue
            s = ctx.syn.get(c["name"])
            if ctx.hook(c) or (s and s[0] >= CUT_SYN) or freq[c["name"]] < GENERIC_MIN or c.get("game_changer") or c["name"] in pieces:
                continue
            if re.search(r"triggers an additional time", otext(c)) and any("triggers" in otext(x) or re.search(r"^(When|Whenever|At)\b", otext(x), re.M) for x in ctx.cmds):
                continue  # trigger doublers (e.g. Roaming Throne naming the commander's type) serve a triggered commander
            if "ramp" in roles(c) and c.get("cmc", 0) <= 2:
                continue  # fast mana / cheap rocks: speed serves every commander at its ceiling
            cuts.append(c)
        cuts.sort(key=lambda c: (-freq[c["name"]], (ctx.syn.get(c["name"]) or (0,))[0], c["name"]))
        adds = []
        for n, s in sorted(ctx.syn.items(), key=lambda kv: (-kv[1][0], -kv[1][1], kv[0])):
            c, _ = R.get(n)
            if not c or c["name"] in have or s[0] < ADD_SYN or s[1] < ADD_INC or is_land(c):
                continue
            if c.get("legalities", {}).get("commander") != "legal" or not set(c.get("color_identity", [])) <= ci:
                continue
            if (c.get("game_changer") and not (gcn > 3 and tgt >= 4)) or ev.MLD.search(otext(c)) or ("extra turn" in otext(c).lower() and not xturn):
                continue
            h = ctx.hook(c)
            if not h:
                continue
            adds.append((c, s, h))
        swaps, used, rejected, needs = [], set(), [], []
        rv = load_review()["swaps"]
        # Bot cycle 41: hand-picked swaps (data/grixis_refine_review.json "manual_swaps") pass the same gates as automatic ones
        nlnames = {x["name"] for x in nl}
        for m in load_review().get("manual_swaps", {}).get(did, []):
            k, _ = R.get(m["cut"]); c, _ = R.get(m["add"])
            fail = []
            if not k or k["name"] not in nlnames:
                fail.append("cut is not a nonland card of the list")
            if not c:
                fail.append("add does not resolve on Scryfall")
            if not fail:
                if c["name"] in have:
                    fail.append("add is already in the list")
                if c.get("legalities", {}).get("commander") != "legal" or not set(c.get("color_identity", [])) <= ci:
                    fail.append("add is not Commander-legal inside the color identity")
                if (c.get("game_changer") and not (gcn > 3 and tgt >= 4)) or ev.MLD.search(otext(c)) or ("extra turn" in otext(c).lower() and not xturn):
                    fail.append("add would raise the bracket (Game Changer / mass land denial / extra turn)")
                if k["name"] in pieces:
                    fail.append("cut is a piece of a Commander Spellbook combo in the list")
                rk = roles(k)
                cap = k.get("cmc", 0) if rk & INTERACTION else k.get("cmc", 0) + 1
                if not (rk <= roles(c) and c.get("cmc", 0) <= cap):
                    fail.append(f"role/MV parity: cut roles {sorted(rk)} MV {k.get('cmc', 0):g}, add roles {sorted(roles(c))} MV {c.get('cmc', 0):g}")
                ok, reasons = guard(k, c, ctx)
                if not ok:
                    fail += reasons
                h = m["hook"]
                cmd_txt = " ".join(otext(x) for x in ctx.cmds)
                if h["commander_text"] not in cmd_txt or h["card_text"] not in (tline(c) + "\n" + otext(c)):
                    fail.append("quoted Oracle text is not verbatim")
            if fail:
                rejected.append({"cut": m["cut"], "add": m["add"], "by": "manual pick, failed gates", "why": "; ".join(fail)})
                continue
            used.add(k["name"]); have.add(c["name"])
            ks, s_ = ctx.syn.get(k["name"]), ctx.syn.get(c["name"])
            swaps.append({"cut": k["name"], "add": c["name"], "cycle": cycle, "guard": reasons, "review": m["why"], "manual": True,
                          "roles": sorted(roles(k)) or ["(no key role)"], "add_roles": sorted(roles(c)),
                          "hook": {"label": m["hook"]["label"], "commander": ctx.cmds[0]["name"], "commander_text": m["hook"]["commander_text"], "card_text": m["hook"]["card_text"]},
                          "add_edhrec": list(s_) if s_ else None, "cut_edhrec": list(ks) if ks else None,
                          "cut_freq": freq[k["name"]], "mv": [k.get("cmc", 0), c.get("cmc", 0)]})
        adds = [x for x in adds if x[0]["name"] not in have]
        for c, s, h in adds:
            if len(swaps) + len(needs) >= MAX_SWAPS:
                break
            for k in cuts:
                if k["name"] in used:
                    continue
                rk = roles(k)
                cap = k.get("cmc", 0) if rk & INTERACTION else k.get("cmc", 0) + 1  # interaction: never slower
                if rk <= roles(c) and c.get("cmc", 0) <= cap:
                    ok, reasons = guard(k, c, ctx)
                    r = rv.get(rkey(did, k["name"], c["name"]))
                    if not ok or (r and r["verdict"] == "reject"):
                        if len(rejected) < 8:
                            rejected.append({"cut": k["name"], "add": c["name"], "by": "power guard" if not ok else "manual review",
                                             "why": "; ".join(reasons) if not ok else r["why"]})
                        continue
                    used.add(k["name"])
                    ks = ctx.syn.get(k["name"])
                    (swaps if r else needs).append({"cut": k["name"], "add": c["name"], "cycle": cycle, "guard": reasons,
                                  "review": r["why"] if r else None,
                                  "roles": sorted(roles(k)) or ["(no key role)"], "add_roles": sorted(roles(c)),
                                  "hook": h, "add_edhrec": list(s), "cut_edhrec": list(ks) if ks else None,
                                  "cut_freq": freq[k["name"]], "mv": [k.get("cmc", 0), c.get("cmc", 0)]})
                    break
        src_combo_ids = {co["id"] for co in combos.get(did, {}).get("combos", [])}
        floor_src = v["floor"]
        while swaps:
            text = apply_swaps(src, swaps)
            res = ev.check(text, R)
            sb = spellbook(lines_of(text, R), cache, did, True)
            two = sum(1 for co in sb["combos"] if co["infinite"] and len(co["cards"]) == 2)
            fl, _, _ = ev.bracket_floor(res["cards"], two)
            if not hard(res, pend, did) and fl <= max(floor_src, tgt) and src_combo_ids <= {co["id"] for co in sb["combos"]}:
                break
            x = swaps.pop()
            rejected.append({"cut": x["cut"], "add": x["add"], "by": "verification", "why": "dropped: the refined list failed legality, the bracket-floor cap or kept-combo check"})
        entry["swaps"] = swaps
        entry["rejected"] = rejected
        entry["needs_review"] = needs
        for w in needs:
            print(f"  NEEDS REVIEW {rkey(did, w['cut'], w['add'])}: {w['hook']['label']} · {'; '.join(w['guard'])} · add syn {w['add_edhrec']} cut syn {w['cut_edhrec']}", flush=True)
        entry["decision"] = (f"refined: {len(swaps)} swap(s)" if swaps else
                             f"awaiting manual review of {len(needs)} candidate swap(s)" if needs else
                             f"at/near ceiling: all {len(rejected)} role-compatible candidate swap(s) failed the power guard or manual review; unchanged" if rejected else
                             "at/near ceiling: no generic, unprotected cut has a role-compatible commander-specific replacement; unchanged")
        plans["decks"][did] = entry
        print(f"  plan {did}: {entry['decision']}", flush=True)


def q(s):
    return s.replace("|", "/").replace("\n", " / ")


def render(R, summ, plans, fetch=False):
    reg = json.loads((ROOT / "data" / "grixis_pending.json").read_text(encoding="utf-8"))["decks"]
    cache = plans.get("spellbook", {})
    src_lists, fin_lists, info, problems = {}, {}, {}, []
    for did, v in summ.items():
        p = ROOT / "grixis" / "decks" / f"{v['slug']}.md"
        src = deck_block(p)
        e = plans["decks"].get(did)
        base_text, base = ga.challenger_base(did, src)
        fin = apply_swaps(base_text, e["swaps"]) if e and e["swaps"] else src
        src_lists[did], fin_lists[did] = lines_of(src, R), lines_of(fin, R)
        info[did] = {"src_text": src, "fin_text": fin, "plan": e, "page": p, "base": base if e and e["swaps"] else "canonical_project_list",
                     "challenger": bool(e and e["swaps"])}
    freq = Counter(n for l in src_lists.values() for n in nonland_names(l))
    sets_src = {d: nonland_names(l) for d, l in src_lists.items()}
    sets_fin = {d: nonland_names(l) for d, l in fin_lists.items()}
    jac = lambda a, b: len(a & b) / len(a | b) if a | b else 0
    metrics = {}
    for did, v in summ.items():
        ctx = Ctx([c for q_, c, z in src_lists[did] if z == "commander"])
        m = {}
        for tag, l, sets in (("source", src_lists[did], sets_src), ("final", fin_lists[did], sets_fin)):
            nl = [c for q_, c, z in l if z == "main" and not is_land(c)]
            dep = [c["name"] for c in nl if ctx.dependent(c)]
            gen = [c["name"] for c in nl if c["name"] not in dep and freq[c["name"]] >= GENERIC_MIN]
            ov = sorted(((jac(sets[did], sets[o]), o) for o in summ if o != did), reverse=True)
            names = {c["name"] for q_, c, z in l}
            m[tag] = {"nonland": len(nl), "dependence": round(len(dep) / len(nl), 3), "generic_share": round(len(gen) / len(nl), 3),
                      "mean_overlap": round(sum(x for x, _ in ov) / len(ov), 3), "max_overlap": [round(ov[0][0], 3), ov[0][1]],
                      "thoracle_core": sorted(THORACLE & names), "control_core": sorted(CONTROL & names)}
        m["hooks"] = sorted({h[0] for h in ctx.hooks})
        m["edhrec_pages"] = ctx.pages
        metrics[did] = m
        # verification of the final list
        pend = reg.get(did, {}).get("cards", []) if reg.get(did, {}).get("status") == "pending" else []
        res = ev.check(info[did]["fin_text"], R)
        if hard(res, pend, did):
            problems.append(f"{did}: refined list fails {[i['type'] + ' ' + i['card'] for i in hard(res, pend, did)]}")
        info[did]["res"] = res
        info[did]["pending"] = pend
        if info[did]["plan"] and info[did]["plan"]["swaps"]:
            sb = spellbook(fin_lists[did], cache, did, fetch)
            if not sb:
                problems.append(f"{did}: no Commander Spellbook result cached for the refined list (run without --check)")
                info[did]["sb"] = None
            else:
                info[did]["sb"] = sb
    # Bot cycle 45: ties sorted by name (set iteration order is hash-randomized, so most_common() reordered ties between runs)
    top = sorted(Counter(n for s in sets_src.values() for n in s).items(), key=lambda kv: (-kv[1], kv[0]))[:25]
    return info, metrics, top, problems


def fmt_syn(s):
    return f"synergy {s[0]:+d}%, in {s[2]:,} of {s[3]:,} decks ({s[1]}%)" if s else "not listed on the commander's EDHREC page"


def block(did, v, info, m, plans):
    e = info["plan"]
    ch = bool(e["swaps"])
    L = [START, "## Refined list (Bot cycle 39)", "",  # heading kept as a stable anchor; the content is relabeled (Bot cycle 47)
         (f"> 🧪 **{ga.CHALLENGER_LABEL}** — evidence, not an approval. " if ch else f"> 🧪 **v1 review record ({ga.V1_HEURISTIC_LABEL}).** ")
         + "Bot cycles 39–44 commander-first refinement ([Grixis Mission](../Grixis%20Mission.md); log: [Grixis Refinement Cycle](../Grixis%20Refinement%20Cycle.md)), engine `grixis_refine v1` (frozen). "
         f"The canonical list is the [{'source baseline' if ch else 'source list'}](#decklist-archidekt-import) above (state `{STATE.get(did, 'SOURCE_BASELINE')}` in the "
         "[authority registry](../../data/grixis/registry.json)), credited to Cory's [grixis-commander-encyclopediaGPT](https://github.com/corymstover/grixis-commander-encyclopediaGPT). "
         + ("This challenger competes with it but has **no approval**: v1's gates are diagnostic evidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#deck-states)). " if ch else
            "v1's gates found no qualifying swap. That is a heuristic result, **not a certificate** that the list is at its ceiling. ")
         + ("Its swaps were computed on the Bot cycle 16 legal list, which is now this deck's derived compliance projection, so the challenger is officially legal. " if info.get("base") == "official_legal_projection" else "")
         + "Facts behind it: Scryfall Oracle text, legality and Game Changer flags; EDHREC synergy (community data, cached); Commander Spellbook combos. Generated by `scripts/grixis_refine.py`.", ""]
    s, f = m["source"], m["final"]
    L += [f"- **Commander hooks (from Oracle text):** {', '.join(m['hooks']) or '—'}.",
          f"- **Commander dependence:** {s['dependence']:.0%} → **{f['dependence']:.0%}** · generic share {s['generic_share']:.0%} → **{f['generic_share']:.0%}** · "
          f"mean overlap with the other 61 lists {s['mean_overlap']:.0%} → **{f['mean_overlap']:.0%}**.",
          f"- **v1 decision (historical record):** {e['decision']}." + ("" if ch else f" Bot cycle 47 reading: *{ga.V1_HEURISTIC_LABEL}*.")]
    if info["pending"]:
        L.append(f"- ⏳ **Pending legality:** {', '.join(info['pending'])} are not Commander-legal before {plans_pending_date(did)}; the export is marked pending.")
    if e["swaps"]:
        L += ["", "| Cut | Add | Role kept | Why (commander-specific) | Power guard + review (Bot cycle 40) |", "|---|---|---|---|---|"]
        for w in e["swaps"]:
            h = w["hook"]
            why = (f"**{h['label']}**: {h['commander']} reads \"{q(h['commander_text'])}\"; {w['add']} reads \"{q(h['card_text'])}\". "
                   f"EDHREC: {fmt_syn(w['add_edhrec'])}. Cut: " + ("" if w.get("manual") else "no Oracle hook to the commander, ") + f"EDHREC {fmt_syn(w['cut_edhrec'])}, "
                   f"in {w['cut_freq']}/62 Grixis lists" + ("" if w.get("manual") else " (generic)") + f". MV {w['mv'][0]:g} → {w['mv'][1]:g}.")
            L.append(f"| {w['cut']} | **{w['add']}**{' (hand-picked)' if w.get('manual') else ''} | {', '.join(w['roles'])} | {why} | {q('; '.join(w.get('guard') or ['(cycle 39 swap, not re-checked)']))}. **Review:** {q(w.get('review') or '—')} |")
        res, sb = info["res"], info.get("sb")
        two = sum(1 for co in sb["combos"] if co["infinite"] and len(co["cards"]) == 2) if sb else 0
        fl, gcs, mld = ev.bracket_floor(res["cards"], two)
        ok = ("✅ 100 cards, singleton, color identity, Commander-legal" if not hard(res, info["pending"]) else
              "✅ 100 cards, singleton, color identity; ❌ not Commander-legal (registered project exceptions)" if not hard(res, info["pending"], did) else "❌ fails")
        L += ["", f"- **Verification (`evaluate_decklist.check`):** {ok}{' (except the ⏳ pending cards)' if info['pending'] else ''}. "
              f"Game Changers {v['gcs'].__len__()} → {len(gcs)} · floor Bracket {v['floor']} → **{fl}** (target {target_of(v)}) · "
              f"Commander Spellbook: {len(sb["combos"]) if sb else "?"} combo(s) ({two} two-card infinite), every source combo kept — a v1 gate, kept as diagnostic evidence (queried {sb['queried'] if sb else '?'}).",
              "", "```text", info["fin_text"].strip(), "```"]
    hr = load_review().get("hand_review", {}).get(did)
    if hr:
        L += ["", f"> 🔎 **Hand review (Bot cycle {hr['cycle']}): {hr['verdict']}.** {hr['tradeoff']}"]
    if e.get("rejected"):
        L += ["", "**Considered and rejected:** " + " · ".join(f"−{x['cut']} +{x['add']} ({x['by']}: {q(x['why'])})" for x in e["rejected"])]
    L += ["", "### Refinement log", "", "| Date | Cycle | Change | Cards added | Cards removed |", "|---|---|---|---|---|"]
    for x in plans["log"].get(did, []):
        L.append(f"| {x['date']} | Bot cycle {x['cycle']} (batch {x['batch']}) | {x['change']} | {', '.join(x['added']) or '—'} | {', '.join(x['removed']) or '—'} |")
    L.append(END)
    return "\n".join(L)


PEND_DATES = {}
STATE = {}  # deck_id -> authority state (data/grixis/registry.json), filled in main()


def plans_pending_date(did):
    return PEND_DATES.get(did, "?")


def inject(text, blk):
    text = re.sub(r"\n*" + re.escape(START) + r".*?" + re.escape(END) + r"\n*", "\n\n", text, flags=re.S)
    if blk:
        text = text.replace("\n\n## Card breakdown", "\n\n" + blk + "\n\n## Card breakdown", 1)
        if "- [Refined list (Bot cycle 39)]" not in text:
            text = text.replace("- [Card breakdown](#card-breakdown)", "- [Refined list (Bot cycle 39)](#refined-list-bot-cycle-39)\n- [Card breakdown](#card-breakdown)", 1)
    else:
        text = text.replace("- [Refined list (Bot cycle 39)](#refined-list-bot-cycle-39)\n", "")
    return text


def export_txt(lst):
    cmd = [f"1 {c['name']} [Commander]" for q_, c, z in lst if z == "commander"]
    cmd += [f"1 {c['name']} [Companion]" for q_, c, z in lst if z == "companion"]  # Bot cycle 47: outside the 100
    rest = sorted(f"{q_} {c['name']}" for q_, c, z in lst if z == "main")
    rest.sort(key=lambda l: l.split(" ", 1)[1].lower())
    return "\n".join(cmd + rest) + "\n"


def final_summary(summ, info, metrics, top, plans):
    """Bot cycle 43: end-of-cycle summary for the legal decks (data/grixis_refine_review.json → final)."""
    rv = load_review()
    fin = rv.get("final", {})
    legal = [d for d in summ if not info[d]["pending"]]
    pend = [d for d in summ if info[d]["pending"]]
    done = [d for d in summ if plans["decks"].get(d)]
    ch = [d for d in done if plans["decks"][d]["swaps"]]
    nm = lambda d: " + ".join(summ[d]["commanders"])
    lk = lambda d: f"[{nm(d)}](decks/{summ[d]['slug']}.md#refined-list-bot-cycle-39)"
    nsw = sum(len(plans["decks"][d]["swaps"]) for d in ch)
    nman = sum(1 for d in ch for w in plans["decks"][d]["swaps"] if w.get("manual"))
    ver = rv.get("swaps", {})
    pdone = [d for d in pend if d in done]
    L = ["## End-of-cycle summary (all 62 decks)", "",
         f"Bot cycles 39–{max(b['cycle'] for b in plans['batches'].values())}, batches 1–{len(plans['batches'])}. "
         f"**{len(done)}/{len(summ)} decks reviewed ({len([d for d in legal if d in done])}/{len(legal)} legal + {len(pdone)}/{len(pend)} ⏳ pending legality): "
         f"{len(ch)} produced a GrokBot challenger (unapproved; {nsw} swaps, {nman} hand-picked), {len(done) - len(ch)} with no candidate passing the v1 gates (heuristic, not a certificate).** "
         + (f"The {len(pdone)} pending decks are refined but pending: their refinement pass is done (batch 6), and they stay ⏳ pending until their cards are Commander-legal. " if pdone else "") +
         f"{len(ver)} written verdicts on guard-passing automatic candidates ({sum(1 for x in ver.values() if x['verdict'] == 'accept')} accepted, "
         f"{sum(1 for x in ver.values() if x['verdict'] == 'reject')} rejected); {len(rv.get('hand_review', {}))} hand reviews; "
         f"{len(rv.get('protect', {}))} decks with protected core cards. Source lists stay on each deck page; every change is guidance with its evidence.", "",
         "### Method in brief", "",
         "- **Commander identity first:** every add needs an Oracle-text hook to the commander (quoted verbatim on the deck page) and EDHREC synergy ≥ "
         f"{ADD_SYN}% on that commander's page. Every cut must be generic: in ≥ {GENERIC_MIN} of the 62 lists, no hook, and synergy < {CUT_SYN}%.",
         "- **Power guard (Bot cycle 40):** no clear downgrade. The add's inclusion on the commander's page must be at least the cut's, its overall EDHREC rank no worse than "
         f"{RANK_X}× the cut's or +{RANK_PLUS}, and a free spell is never replaced by one that costs mana. Never cut Game Changers, Spellbook combo pieces, mana sources of MV ≤ 2, "
         "trigger doublers for triggered commanders, or reviewer-protected core cards. Role parity: interaction is replaced only by interaction at equal or lower MV.",
         "- **Written review:** a swap that passes the guard is applied only with a written verdict saying why the add does more in *this* deck. Unreviewed swaps fail `validate_all`.",
         "- **Hand-picked swaps (Bot cycle 41):** reviewer-chosen swaps with verbatim Oracle hooks. They pass the same gates.",
         "- **Hand reviews:** every deck scoring under about 30% commander dependence when it was reviewed (Evelyn, Marchesa, Dealer of Death, Nicol Bolas, Fire Lord Azula) got a commander-first hand look, as did both new pending decks (batch 6). "
         "So did the decks near that line (Garza Zol, Sol'kanar the Swamp King, Tetsuo Umezawa) and Thraximundar, for its source flag. Several low scores were hook gaps, fixed below.",
         "- **Scoring fixes found by hand review:** Evelyn's exile-play hook (cycle 40); the crimes hook for Marchesa (cycle 41); the wheels / punishers hook (Nekusar), "
         "\"deals damage to an opponent\" (Nicol Bolas), ward no longer counted as a counterspell (cycle 42); unearth (Sedris), life gain and black spells (Sol'kanar), "
         "tapping / blocking creatures (Tetsuo Umezawa), villainous choice / voting (The Valeyard), and reminder text ignored for roles (cycle 43).",
         "- **Verification:** each challenger passes `evaluate_decklist.check`, keeps every Spellbook combo of the source list, and does not raise the bracket floor.", "",
         "### Decks with a GrokBot challenger (unapproved)", "", "Bot cycle 47: these lists are challengers to the canonical source baseline, not approvals ([Grixis Authority Model](Grixis%20Authority%20Model.md#deck-states)).", "", "| Deck | Batch | Swaps | Identity impact (commander dependence) | Why |", "|---|---|---|---|---|"]
    for d in ch:
        e, m = plans["decks"][d], metrics[d]
        why = " ".join((w.get("review") or "").split(". ")[0].rstrip(".") + "." for w in e["swaps"])
        L.append(f"| {lk(d)} | {e['batch']} | " + "; ".join(f"−{w['cut']} +**{w['add']}**{' (hand-picked)' if w.get('manual') else ''}" for w in e["swaps"]) +
                 f" | {', '.join(sorted({w['hook']['label'] for w in e['swaps']}))}: {m['source']['dependence']:.0%} → **{m['final']['dependence']:.0%}** | {q(why)} |")
    L += ["", f"### {ga.V1_HEURISTIC_LABEL[0].upper() + ga.V1_HEURISTIC_LABEL[1:]}", "",
          "No qualifying swap passed the v1 gates, guard and review, so these lists stay as the source built them (principle 2). "
          "Bot cycle 47: this is a heuristic outcome of one engine, **not a certificate that a list is at its ceiling**; v1's ceiling shortcut and its \"all candidates failed\" fallback are retired in v2. Hand-reviewed decks are marked 🔎.", ""]
    for b, bv in sorted(plans["batches"].items(), key=lambda kv: int(kv[0])):
        un = [d for d in bv["decks"] if d in done and not plans["decks"][d]["swaps"]]
        if un:
            L.append(f"- **Batch {b}:** " + " · ".join(f"{lk(d)} ({metrics[d]['final']['dependence']:.0%}{' 🔎' if d in rv.get('hand_review', {}) else ''}{' ⏳ pending' if info[d]['pending'] else ''})" for d in un))
    L += ["", "### Flagged items", ""]
    for x in fin.get("flags", []):
        lab = nm(x["deck"]) if x.get("deck") in summ else x.get("label") or x.get("deck") or "General"
        L.append(f"- ⚠️ **{lab}:** " + x["item"])
    legal = list(summ)  # homogenization is measured on all 62 lists
    srcm = sum(metrics[d]["source"]["dependence"] for d in legal) / len(legal)
    finm = sum(metrics[d]["final"]["dependence"] for d in legal) / len(legal)
    L += ["", "### Homogenization and overlap findings", "",
          f"- All 62 lists, source → final: mean commander dependence {srcm:.1%} → **{finm:.1%}** · mean generic share "
          f"{sum(metrics[d]['source']['generic_share'] for d in legal) / len(legal):.1%} → **{sum(metrics[d]['final']['generic_share'] for d in legal) / len(legal):.1%}** · "
          f"mean pairwise overlap {sum(metrics[d]['source']['mean_overlap'] for d in legal) / len(legal):.1%} → **{sum(metrics[d]['final']['mean_overlap'] for d in legal) / len(legal):.1%}**.",
          f"- Most shared cards: " + ", ".join(f"{n} ({k})" for n, k in top[:10]) + " (lists out of 62).",
          f"- {fin.get('homogenization', '')}"]
    for k, x in rv.get("overlap", {}).items():
        L.append(f"- **{k}:** {x['verdict'].split('. ')[0].rstrip('.')}.")
    L += ["", "### Pending decks: refined but pending legality", ""]
    for d in pend:
        e = plans["decks"].get(d)
        hr = rv.get("hand_review", {}).get(d)
        L.append(f"- ⏳ {lk(d)}: **refined but pending**. " + (f"Batch {e['batch']} (Bot cycle {e['cycle']}): {e['decision']}" + (" (hand review: " + hr["verdict"] + ")" if hr else "") + ". " if e else "Not reviewed yet. ") +
                 f"Pending card(s): {', '.join(info[d]['pending'])} (registry `legal_from` {plans_pending_date(d)}). The export stays marked pending.")
    L += [f"- **Activation follow-up (routine `grixis-pending-legality-activation`, scheduled for 2026-11-13):** {fin.get('pending_followup', '')}", ""]
    return L


def summary_page(summ, info, metrics, top, plans):
    done = [d for d in summ if plans["decks"].get(d)]
    L = ["# Grixis Refinement Cycle", "",
         f"> **Bot cycle 39+** · Cory's commander-first mission ([Grixis Mission](Grixis%20Mission.md)). Auto-generated by `scripts/grixis_refine.py` from Scryfall Oracle data, "
         "EDHREC synergy (community data, cached) and Commander Spellbook. Metrics are facts about the lists; swaps are guidance. "
         "Source lists stay on each deck page, credited to Cory's [grixis-commander-encyclopediaGPT](https://github.com/corymstover/grixis-commander-encyclopediaGPT). "
         "Archidekt exports: [exports/grixis-archidekt/](../exports/grixis-archidekt/README.md).", "",
         f"Grixis source commit used: `{plans.get('source', {}).get('commit', '?')}` ({plans.get('source', {}).get('note', '')}).", "",
         "## Contents", "- [Status](#status)", "- [End-of-cycle summary (all 62 decks)](#end-of-cycle-summary-all-62-decks)", "- [Batch log](#batch-log)", "- [Hand reviews](#hand-reviews)", "- [Overlap review (manual)](#overlap-review-manual)", "- [All decks: metrics](#all-decks-metrics)", "- [Homogenization](#homogenization)", "- [Method](#method)", "",
         "> 🏛️ **Bot cycle 47 (M0) authority reading.** Every list produced here is a **GrokBot challenger (unapproved)** or a v1 review record. "
         "The canonical list of each deck is its source baseline (state in [data/grixis/registry.json](../data/grixis/registry.json)). v1 is frozen for reproduction "
         "(`--engine v1`); v2 (`--engine v2`) writes exploratory recommendations to `data/grixis_refine_v2.json` and never publishes a final list. "
         "Model: [Grixis Authority Model](Grixis%20Authority%20Model.md).", "",
         "## Status", "",
         f"- **Reviewed by v1: {len(done)}/62** decks ({sum(1 for d in done if plans['decks'][d]['swaps'])} GrokBot challengers (unapproved), {sum(1 for d in done if not plans['decks'][d]['swaps'])} heuristic: no candidate passed v1 gates (not a certificate)). "
         f"{sum(1 for d in summ if info[d]['pending'])} decks are ⏳ pending legality (measured; exports marked pending).",
         f"- Mean commander dependence, all 62 (final lists): **{sum(metrics[d]['final']['dependence'] for d in summ) / len(summ):.0%}** · "
         f"mean generic share: **{sum(metrics[d]['final']['generic_share'] for d in summ) / len(summ):.0%}** · "
         f"mean pairwise overlap: **{sum(metrics[d]['final']['mean_overlap'] for d in summ) / len(summ):.0%}**.",
         f"- Thoracle core present in {sum(1 for d in summ if metrics[d]['final']['thoracle_core'])} lists · median control-core cards per list: "
         f"{sorted(len(metrics[d]['final']['control_core']) for d in summ)[31]}.", ""] + final_summary(summ, info, metrics, top, plans) + ["## Batch log", ""]
    for b, bv in sorted(plans["batches"].items(), key=lambda kv: int(kv[0])):
        L += [f"### Batch {b} — Bot cycle {bv['cycle']}, {bv['date']}", ""]
        for d in (d for d in bv["decks"] if d in summ):
            e = plans["decks"][d]
            v = summ[d]
            nm = " + ".join(v["commanders"])
            m = metrics[d]
            L.append(f"- [{nm}](decks/{v['slug']}.md#refined-list-bot-cycle-39): {e['decision']}. Dependence {m['source']['dependence']:.0%} → {m['final']['dependence']:.0%}." +
                     ("".join(f" Cut **{w['cut']}** → add **{w['add']}** ({w['hook']['label']})." for w in e["swaps"])))
        sw = {k: x for k, x in load_review().get("swaps", {}).items() if k.split("|")[0] in bv["decks"]}
        man = sum(len(load_review().get("manual_swaps", {}).get(d, [])) for d in bv["decks"])
        if sw or man:
            acc = sum(1 for x in sw.values() if x["verdict"] == "accept")
            L += ["", f"- *Written reviews in this batch:* {len(sw)} verdict(s) on automatic candidates ({acc} accepted, {len(sw) - acc} rejected) covering "
                      f"{len({k.split('|')[2] for k in sw})} distinct add(s)" + (f", plus {man} hand-picked swap(s)" if man else "") + "."]
        L.append("")
    hrs = load_review().get("hand_review", {})
    if hrs:
        L += ["## Hand reviews", "", "Decks given a commander-first hand look (guidance; principle 2: no artificial weakening).", ""]
        for d, x in ((d, x) for d, x in hrs.items() if d in summ):  # a deck dropped from the build (e.g. legality) is skipped, not a crash
            L += [f"- **[{' + '.join(summ[d]['commanders'])}](decks/{summ[d]['slug']}.md#refined-list-bot-cycle-39)** (Bot cycle {x['cycle']}): **{x['verdict']}.** {x['tradeoff']}"]
        L.append("")
    ov = load_review().get("overlap", {})
    L += ["## Overlap review (manual)", "", "High-overlap pairs judged by hand (Bot cycle 40): is the shared core explained by both commanders' Oracle text, or is it homogenization? Guidance.", ""]
    for k, x in ov.items():
        L += [f"### {k}", "", f"- **Shared nonland cards:** {x['shared']}.", f"- **Verdict:** {x['verdict']}", f"- **Proposed identity-driven changes:** {x['proposals']}", ""]
    L += ["## All decks: metrics", "",
          "| Deck | Status | Dependence | Generic share | Mean overlap | Closest list | Thoracle core | Control core | Hooks |", "|---|---|---|---|---|---|---|---|---|"]
    for d, v in sorted(summ.items(), key=lambda kv: metrics[kv[0]]["final"]["dependence"]):
        m, f = metrics[d], metrics[d]["final"]
        e = plans["decks"].get(d)
        st = ("⏳ pending · " if info[d]["pending"] else "") + ("challenger (unapproved)" if e and e["swaps"] else "no v1 candidate (heuristic)" if e else "not reviewed yet")
        cl = summ[f["max_overlap"][1]]["commanders"][0]
        L.append(f"| [{' + '.join(v['commanders'])}](decks/{v['slug']}.md) | {st} | {m['source']['dependence']:.0%}" + (f" → **{f['dependence']:.0%}**" if e and e["swaps"] else "") +
                 f" | {f['generic_share']:.0%} | {f['mean_overlap']:.0%} | {cl} ({f['max_overlap'][0]:.0%}) | {len(f['thoracle_core'])} | {len(f['control_core'])} | {', '.join(m['hooks'][:4])}{' …' if len(m['hooks']) > 4 else ''} |")
    L += ["", "## Homogenization", "", "Most-shared nonland cards across the 62 source lists (count of lists):", "",
          "| Card | Lists |", "|---|---|"] + [f"| {n} | {k} |" for n, k in top]
    L += ["", "## Method", "",
          f"- **Commander dependence (fact-based heuristic):** a nonland, non-commander card counts if (a) its Oracle text or type line matches a *hook* taken from the commander's own Oracle text (mechanic patterns in `HOOKS`, plus creature types named in the commander's text, from CR 205.3m), or (b) its EDHREC synergy on the commander's page is ≥ {DEP_SYN}%. Score = counted / nonland cards. Patterns are loose by design; the score ranks decks, it is not a rules statement.",
          f"- **Generic share:** cards with no commander link that appear in ≥ {GENERIC_MIN} of the 62 source lists. **Overlap:** Jaccard index of nonland card sets. **Thoracle core:** {', '.join(sorted(THORACLE))}. **Control core:** {', '.join(sorted(CONTROL))}.",
          f"- **Ceiling (v1, retired in v2):** v1 flagged a deck with dependence ≥ {CEIL_DEP:.0%} and generic share ≤ {CEIL_GEN:.0%}, or with no qualifying swap, as at/near its ceiling and left it unchanged. Since Bot cycle 47 that is read as *{ga.V1_HEURISTIC_LABEL}*.",
          f"- **Cuts:** only generic cards (≥ {GENERIC_MIN} lists) with no Oracle hook and EDHREC synergy < {CUT_SYN}%. Never a Game Changer, a piece of a Commander Spellbook combo in the list, or a mana source of MV ≤ 2 (speed serves every commander at its ceiling).",
          f"- **Adds:** EDHREC synergy ≥ {ADD_SYN}% and inclusion ≥ {ADD_INC}% on the commander's page, **and** an Oracle hook to the commander; Commander-legal, inside the color identity, no new Game Changer unless the list already has 4+ and targets Bracket 4+, no mass land denial, no extra-turn card unless the list already plays one.",
          f"- **Pairing:** each add replaces a cut whose key roles ({', '.join(KEY_ROLES)}; Oracle patterns) it covers, at MV at most 1 higher; interaction (removal, wipes, counterspells, protection) is only replaced by interaction at equal or lower MV. At most {MAX_SWAPS} swaps per deck per batch.",
          f"- **Power guard (Bot cycle 40):** an add must not be a clear power downgrade of its cut: commander-page inclusion at least the cut's (this commander's players choose it at least as often), overall EDHREC rank no worse than {RANK_X}× the cut's or +{RANK_PLUS}, and no free spell (pitch/commander-free) replaced by a non-free one. Every guard-passing swap needs a written manual review (`data/grixis_refine_review.json`) saying why the add does more in *this* deck; unreviewed swaps are not applied and fail `validate_all`.",
          "- **Verification:** the refined list must pass `evaluate_decklist.check` (100 cards, singleton, color identity, Commander-legal), keep every Commander Spellbook combo of the source list (re-queried), and not raise the bracket floor above the source floor or target. A failing swap is dropped.",
          "- **Frozen decisions:** each batch's swaps are stored in `data/grixis_refine_batches.json`; `validate_all` re-verifies them on every run.",
          "- **v2 (Bot cycle 47, exploratory):** gates become diagnostics, protections become priors (only explicit project/user constraints veto), combo preservation is reported per candidate instead of required, every nonland slot of every deck is analyzed (no ceiling shortcut), and EDHREC lift, trend z-score, sample size (num_decks / potential_decks) and cache retrieval date are recorded. Output: `data/grixis_refine_v2.json`, recommendations only, labeled exploratory until M2 and M4 are accepted.",
          "- **Limits:** EDHREC synergy measures how often decks of *this* commander play a card versus all decks of its colors: community data, not a quality judgment. The heuristic cannot see multi-card lines the Oracle patterns miss; at-ceiling decks are candidates for a hand review."]
    return "\n".join(L) + "\n"


def exports(summ, info, plans):
    """Bot cycle 47: every file is labeled. `<slug>.txt` keeps its pre-cycle-47 content (M1 interaction reviews hash it):
    the GrokBot challenger (unapproved) where v1 produced one, the derived compliance projection where the canonical list
    keeps project exceptions (Bjorna), otherwise the source baseline (canonical project list).
    Decks with a challenger also get `source-baseline/<slug>.txt`; decks with a projection get
    `projections/<slug>.official-legal-projection.txt`. `index.json` lists label, state and hashes per file."""
    files, manifest = {}, []
    idx = ["# Grixis Archidekt exports", "",
           "> Generated by `scripts/grixis_refine.py` (Bot cycle 39+; labels and authority states since Bot cycle 47). **Every file is labeled.** "
           f"**{ga.BASELINE_LABEL}** is the deck's one canonical project list. **{ga.CHALLENGER_LABEL}** is a GrokBot cycle 39–44 refinement that competes with it and has no approval. "
           f"**{ga.PROJECTION_LABEL}** is an officially legal version derived from a canonical list that keeps project exceptions; it never competes for authority. "
           "Deck states come from the [authority registry](../../data/grixis/registry.json); nothing here is APPROVED or CANONICAL_LOCKED until Cory signs off "
           "([Grixis Authority Model](../../grixis/Grixis%20Authority%20Model.md)). Machine-readable manifest: [`index.json`](index.json).", "",
           "> Format checked against the source repo's Archidekt package (`exports/archidekt_2026-10-15/`: one `1x Card Name` line per card, commander first, no set codes); "
           "here lines read `1 Card Name`, commander lines carry Archidekt's `[Commander]` category and a companion line carries `[Companion]` (outside the 100). "
           "Paste one file into one deck. `ALL-DECKS.txt` is for reference only (do not paste it into one deck). `validate_all` checks every file against its deck page.", "",
           "| # | File | Label | State | Commander(s) | Legality | Changes vs canonical | Key notes |", "|---|---|---|---|---|---|---|---|"]
    rv = load_review()
    flags = {x["deck"]: x["item"].split(". ")[0] for x in rv.get("final", {}).get("flags", []) if x.get("deck")}
    exc_decks = {x["deck_id"] for x in ga.load_json(ga.EXCEPTIONS, {"exceptions": []})["exceptions"] if x["project_authorization_status"] == "AUTHORIZED_EXCEPTION"}
    master = []

    def add(path, txt, did, role, label, legality):
        files[path] = txt
        manifest.append({"file": str(path.relative_to(EXP)), "deck_id": did, "commanders": summ[did]["commanders"], "role": role, "label": label,
                         "state": STATE.get(did, "SOURCE_BASELINE") if role == "canonical" else "CHALLENGER" if role == "challenger" else None,
                         "official_commander_compliance": legality, "list_hash": ga.text_hash(txt, ev_R), "raw_sha256": ga.raw_hash(txt.encode("utf-8"))})

    for i, (did, v) in enumerate(summ.items(), 1):
        e = info[did]["plan"]
        pend = info[did]["pending"]
        leg_c = "pending_release" if pend else "not_compliant_project_exceptions" if did in exc_decks else "compliant"
        leg_txt = {"pending_release": f"⏳ not Commander-legal before {plans_pending_date(did)}", "not_compliant_project_exceptions": "🚩 NOT Commander-legal (project exceptions)", "compliant": "✅ Commander-legal"}
        canon = export_txt(lines_of(info[did]["src_text"], ev_R))
        st = STATE.get(did, "SOURCE_BASELINE")
        m = info[did].get("metrics")
        hr = rv.get("hand_review", {}).get(did)
        note = ([f"dependence {m['source']['dependence']:.0%}" + (f" → {m['final']['dependence']:.0%}" if e and e["swaps"] else "") + (f"; hooks: {', '.join(m['hooks'][:3])}{' …' if len(m['hooks']) > 3 else ''}" if m['hooks'] else "")] if m else []) + \
               ([f"hand review: {hr['verdict']}"] if hr else []) + ([f"⚠️ {flags[did]}"] if did in flags else []) + \
               ([f"protected core (v1 prior): {', '.join(rv['protect'][did]['cards'])}"] if did in rv.get("protect", {}) else [])
        if info[did]["challenger"]:
            txt = export_txt(lines_of(info[did]["fin_text"], ev_R))
            ch = "; ".join(f"−{w['cut']} +{w['add']} ({w['hook']['label']})" for w in e["swaps"])
            if info[did]["base"] == "official_legal_projection":
                ch = "on the derived compliance projection: " + ch
            add(EXP / f"{v['slug']}.txt", txt, did, "challenger", ga.CHALLENGER_LABEL, "pending_release" if pend else "compliant")
            add(EXP / "source-baseline" / f"{v['slug']}.txt", canon, did, "canonical", ga.BASELINE_LABEL, leg_c)
            idx.append(f"| {i} | [{v['slug']}.txt]({v['slug']}.txt) | 🧪 {ga.CHALLENGER_LABEL} | CHALLENGER | {' + '.join(v['commanders'])} | {leg_txt['pending_release' if pend else 'compliant']} | {ch} | {q('; '.join(note)) or '—'} |")
            idx.append(f"| {i} | [source-baseline/{v['slug']}.txt](source-baseline/{v['slug']}.txt) | {ga.BASELINE_LABEL} | {st} | {' + '.join(v['commanders'])} | {leg_txt[leg_c]} | — (canonical) | v1 verdict: challenger produced |")
            lab = ga.CHALLENGER_LABEL
        elif ga.projection_text(did, info[did]["src_text"]):
            # the deck's canonical list keeps project exceptions: the legacy path keeps its pre-cycle-47 bytes (the officially
            # legal list that M1 interaction reviews hashed) and is labeled as the projection; the canonical file is source-baseline/
            txt = export_txt(lines_of(ga.projection_text(did, info[did]["src_text"]), ev_R))
            add(EXP / f"{v['slug']}.txt", txt, did, "projection", ga.PROJECTION_LABEL, "compliant")
            add(EXP / "source-baseline" / f"{v['slug']}.txt", canon, did, "canonical", ga.BASELINE_LABEL, leg_c)
            idx.append(f"| {i} | [{v['slug']}.txt]({v['slug']}.txt) | {ga.PROJECTION_LABEL} (legacy path, byte-stable for M1 interaction hashes) | — (never in an approval state) | {' + '.join(v['commanders'])} | ✅ Commander-legal | derived from the canonical list | same list as projections/ |")
            idx.append(f"| {i} | [source-baseline/{v['slug']}.txt](source-baseline/{v['slug']}.txt) | {ga.BASELINE_LABEL} | {st} | {' + '.join(v['commanders'])} | {leg_txt[leg_c]} | — (canonical) | v1 verdict: {ga.V1_HEURISTIC_LABEL if e else 'not reviewed by v1'}; {q('; '.join(note)) or '—'} |")
            lab = ga.PROJECTION_LABEL
        else:
            txt = canon
            add(EXP / f"{v['slug']}.txt", txt, did, "canonical", ga.BASELINE_LABEL, leg_c)
            vv = ga.V1_HEURISTIC_LABEL if e else "not reviewed by v1"
            idx.append(f"| {i} | [{v['slug']}.txt]({v['slug']}.txt) | {ga.BASELINE_LABEL} | {st} | {' + '.join(v['commanders'])} | {leg_txt[leg_c]} | — (canonical) | v1 verdict: {vv}; {q('; '.join(note)) or '—'} |")
            lab = ga.BASELINE_LABEL
        pt = ga.projection_text(did, info[did]["src_text"])
        if pt:
            ptxt = export_txt(lines_of(pt, ev_R))
            add(EXP / "projections" / f"{v['slug']}.official-legal-projection.txt", ptxt, did, "projection", ga.PROJECTION_LABEL, "compliant")
            idx.append(f"| {i} | [projections/{v['slug']}.official-legal-projection.txt](projections/{v['slug']}.official-legal-projection.txt) | {ga.PROJECTION_LABEL} | — (never in an approval state) | {' + '.join(v['commanders'])} | ✅ Commander-legal | derived from the canonical list | substitutions on the deck page |")
        master += [f"===== {i:02d}/62 — {' + '.join(v['commanders'])} — {lab} · {'CHALLENGER' if info[did]['challenger'] else st}{' · ' + leg_txt['pending_release'] if pend else ''} =====", txt.rstrip(), ""]
    files[EXP / "ALL-DECKS.txt"] = "\n".join(master)
    files[EXP / "index.json"] = json.dumps({"_doc": "Bot cycle 47: manifest of exports/grixis-archidekt (scripts/grixis_refine.py). role canonical = source baseline (the deck's one canonical project list); challenger = GrokBot challenger (unapproved); projection = derived compliance projection (not canonical, never in an approval state). list_hash is the logical lh1 hash (data/grixis/registry.json hash_definition); raw_sha256 hashes the file bytes.",
                                            "schema_version": 1, "files": manifest}, indent=1, ensure_ascii=False) + "\n"
    fu = rv.get("final", {}).get("pending_followup", "")
    idx += ["", "## Import notes", "",
            "- ⚠️ **Not tested in Archidekt itself.** The files are checked offline on every `validate_all` run. Each matches its deck page card for card. "
            "Each is 100 cards plus at most one `[Companion]` line, with the commander line(s) first and tagged `[Commander]`, no duplicate lines and no blank lines inside the list. "
            "Each passes `evaluate_decklist.check` (singleton, color identity, Commander legality), except that registered project exceptions are accepted and labeled 🚩 NOT Commander-legal. "
            "Paste one deck into Archidekt and confirm the commander category before relying on it.",
            "- 🚩 **Project exceptions:** a canonical list may keep Cory-authorized exceptions (registry `data/grixis/exceptions.json`). Such a file is never Commander-legal; "
            "its officially legal version is the matching file in `projections/`.",
            "- ⏳ The two pending decks are exported for completeness, but they are not Commander-legal yet. "
            "The legality column shows the registry's `legal_from`, Wizards' official Commander date for new MBC cards: 2026-11-13 "
            "([What's Inside Mystery Booster Commander Edition?](https://magic.wizards.com/en/news/feature/whats-inside-mystery-booster-commander-edition)). " + fu,
            "- Full method, every challenger swap with its written review, flagged items and homogenization findings: "
            "[Grixis Refinement Cycle](../../grixis/Grixis%20Refinement%20Cycle.md#end-of-cycle-summary-all-62-decks)."]
    files[EXP / "README.md"] = "\n".join(idx) + "\n"
    return files


# ---------------------------------------------------------------- v2 (Bot cycle 47, M0): exploratory, diagnostic, never final
REFINE_V2 = ROOT / "data" / "grixis_refine_v2.json"
V2_LABEL = "GrokBot challenger (unapproved) — exploratory v2 recommendations"
V2_OBJECTIVE = ("commander-identity heuristic v2: one heuristic pass ranking weak slots and commander-linked adds. Not an optimizer certificate. "
                "M6 runs two independent optimizer passes (commander-first / blueprint fidelity vs measured performance) with different objective functions, "
                "reconciled afterwards (data/grixis/schemas/optimizer_pass.schema.json).")
SMALL_SAMPLE = 50  # potential_decks below this: EDHREC numbers are low-confidence


def edhrec_full(cmds):
    """EDHREC cardview stats confirmed in the cache: synergy, lift, num_decks, potential_decks, trend_zscore.
    The payload carries no fetch timestamp, so the retrieval date is the cache file's mtime; savedate_counts gives the newest deck save."""
    slugs = ["-".join(sorted(eslug(c) for c in cmds))] if len(cmds) > 1 else []
    slugs += [eslug(c) for c in cmds]
    out, used, dates, stats = {}, [], [], Counter()
    for s in slugs:
        p = EDH / f"commanders__{s}.json"
        if not p.exists():
            continue
        d = json.loads(p.read_text(encoding="utf-8"))
        if "container" not in d:
            continue
        used.append(s)
        dates.append(dt.datetime.fromtimestamp(p.stat().st_mtime, dt.timezone.utc).date().isoformat())
        sv = sorted((d.get("savedate_counts") or {}).keys())
        for cl in d["container"]["json_dict"].get("cardlists", []):
            if cl.get("tag") in ("newcards", "topcommanders", "newcommanders"):
                continue
            for v in cl.get("cardviews", []):
                stats["cardviews"] += 1
                stats["with_lift"] += v.get("lift") is not None
                stats["with_trend"] += v.get("trend_zscore") is not None
                if v.get("synergy") is None or not v.get("potential_decks"):
                    continue
                out.setdefault(v["name"], {"synergy": round(100 * v["synergy"]), "lift": None if v.get("lift") is None else round(v["lift"], 3),
                                           "inclusion": round(100 * v["num_decks"] / v["potential_decks"], 1), "num_decks": v["num_decks"],
                                           "potential_decks": v["potential_decks"], "trend_zscore": v.get("trend_zscore"),
                                           "small_sample": v["potential_decks"] < SMALL_SAMPLE, "page": s, "newest_deck_save": sv[-1] if sv else None})
        if len(cmds) > 1 and s == slugs[0]:
            break
    return out, used, (max(dates) if dates else None), stats


def plan_v2(dids, R, summ):
    """Exploratory recommendations for every nonland slot of every listed deck. Differences from v1 (Cory decision, M0):
    no at-ceiling shortcut and no "all candidates failed, so ceiling" fallback; gates (power guard, role parity, combo
    preservation, bracket) are recorded as diagnostics, not vetoes; reviewer protections, Game Changers, combo pieces and
    cheap mana are priors; only explicit project/user constraints (registered project exceptions, the commanders) are hard."""
    combos = json.loads(COMBOS.read_text(encoding="utf-8"))["decks"]
    lists = {d: lines_of(deck_block(ROOT / "grixis" / "decks" / f"{v['slug']}.md"), R) for d, v in summ.items()}
    freq = Counter(n for l in lists.values() for n in nonland_names(l))
    prot = load_review().get("protect", {})
    exc = ga.load_json(ga.EXCEPTIONS, {"exceptions": []})["exceptions"]
    lift = Counter()
    out = {}
    for did in dids:
        v = summ[did]
        text = deck_block(ROOT / "grixis" / "decks" / f"{v['slug']}.md")
        lst = lists[did]
        cmds = [c for q_, c, z in lst if z == "commander"]
        ctx = Ctx(cmds)
        st, pages, retrieved, stats = edhrec_full([c["name"] for c in cmds])
        lift.update(stats)
        lift["pages"] += len(pages)
        have = {c["name"] for q_, c, z in lst}
        ci = set().union(*(set(c.get("color_identity", [])) for c in cmds))
        tgt = target_of(v)
        constraint = {x["card"]: x for x in exc if x["deck_id"] == did and x["project_authorization_status"] == "AUTHORIZED_EXCEPTION"}
        pieces = {}
        for co in combos.get(did, {}).get("combos", []):
            for n in co["cards"]:
                pieces.setdefault(n, []).append(co["id"])
        slots = []
        for c in (c for q_, c, z in lst if z == "main" and not is_land(c)):
            if c["name"] in constraint:
                continue
            h, s = ctx.hook(c), st.get(c["name"])
            pri = []
            if c["name"] in prot.get(did, {}).get("cards", []):
                pri.append("reviewer-protected core (v1 review, data/grixis_refine_review.json): prior, not a veto")
            if c.get("game_changer"):
                pri.append("Game Changer: power prior")
            if c["name"] in pieces:
                pri.append(f"piece of {len(pieces[c['name']])} Commander Spellbook combo(s): prior; a cut would break them (reported)")
            if "ramp" in roles(c) and c.get("cmc", 0) <= 2:
                pri.append("cheap mana (MV <= 2): speed prior")
            diag = {"oracle_hook": h["label"] if h else None, "edhrec": s, "lists_of_62": freq[c["name"]], "roles": sorted(roles(c)), "mv": c.get("cmc", 0)}
            w = (0 if h else 2) + (1 if not s or s["synergy"] < CUT_SYN else 0) + (1 if freq[c["name"]] >= GENERIC_MIN else 0) \
                - (0.5 if s and s["inclusion"] >= 50 and not s["small_sample"] else 0) - 0.75 * len(pri)
            diag["weakness_score"] = round(w, 2)
            slots.append((w, c, diag, pri))
        slots.sort(key=lambda x: (-x[0], x[1]["name"]))
        adds = []
        for n, s in sorted(st.items(), key=lambda kv: (-kv[1]["synergy"], -kv[1]["inclusion"], kv[0])):
            c, _ = R.get(n)
            if not c or c["name"] in have or is_land(c) or s["synergy"] < ADD_SYN:
                continue
            if c.get("legalities", {}).get("commander") != "legal" or not set(c.get("color_identity", [])) <= ci:
                continue  # official legality and color identity are rules, not heuristics
            adds.append((c, s, ctx.hook(c)))
        recs, used = [], set()
        for c, s, h in adds[:40]:
            if len(recs) >= MAX_SWAPS:
                break
            opts = []
            for w, k, kd, kp in slots[:12]:
                if k["name"] in used:
                    continue
                rk = roles(k)
                cap = k.get("cmc", 0) if rk & INTERACTION else k.get("cmc", 0) + 1
                if not (rk <= roles(c) and c.get("cmc", 0) <= cap):
                    continue  # pairing needs a role match to be a coherent swap; still only a recommendation
                ok, reasons = guard(k, c, ctx)
                opts.append((not ok, len(opts), k, kd, kp, ok, reasons))
            # the guard is a diagnostic, not a veto: a guard-passing pairing is preferred, a failing one is still reported as such
            for _, _, k, kd, kp, ok, reasons in sorted(opts, key=lambda o: o[:2])[:1]:
                parity = True
                used.add(k["name"])
                diag = {"power_guard": {"pass": ok, "notes": reasons}, "role_parity": parity, "add_oracle_hook": h["label"] if h else None,
                        "add_edhrec": s, "cut_edhrec": st.get(k["name"]), "cut_weakness": kd["weakness_score"],
                        "breaks_source_combos": pieces.get(k["name"], []),
                        "bracket_signals": [x for x, f in (("Game Changer", c.get("game_changer")), ("mass land denial", ev.MLD.search(otext(c))),
                                                           ("extra turn", "extra turn" in otext(c).lower())) if f], "target_bracket": tgt}
                ev_refs = [f"oracle:{k['name']}", f"oracle:{c['name']}", f"edhrec:.cache/edhrec/commanders__{s['page']}.json#{c['name']}"] + \
                          ([f"spellbook:data/grixis_combos.json#{did}"] if pieces.get(k["name"]) else [])
                recs.append({"cut": k["name"], "add": c["name"], "diagnostics": diag, "priors": kp, "evidence": ev_refs})
                break
        out[did] = {"deck_id": did, "base_hash": ga.text_hash(text, R), "label": V2_LABEL, "state": "CHALLENGER",
                    "edhrec": {"pages": pages, "retrieved": retrieved}, "objective": V2_OBJECTIVE,
                    "hard_constraints": [f"{x['card']}: registered project exception ({x['id']}); an automated engine never cuts it" for x in constraint.values()]
                                        + ["commanders are fixed; lands are outside v2's scope (M2 blueprint work)"],
                    "weakest_slots": [{"card": c["name"], "diagnostics": d, "priors": pr} for w, c, d, pr in slots[:8]],
                    "recommendations": recs,
                    "verdict": (f"{len(recs)} exploratory recommendation(s); not a final list and not approved — promotion needs an M2 blueprint and M4 tests" if recs else
                                "no candidate identified by v2 heuristics; this is NOT evidence that the list is at its ceiling")}
        print(f"  v2 {did}: {len(recs)} recommendation(s)", flush=True)
    ms = ga.load_json(ga.REGISTRY, {"program": {"milestones": {}}})["program"]["milestones"]
    st2, st4 = (ms.get("M2") or {}).get("status", "not_started"), (ms.get("M4") or {}).get("status", "not_started")
    gate_open = st2 == "accepted" and st4 == "accepted"
    return {"_doc": "Bot cycle 47+: grixis_refine v2 output. Recommendations only: never a final list, never written to deck pages or exports. "
                    "Always exploratory: M2+M4 acceptance opens the M6 gate (Cory constraint 6) but approves no refinement result (t52u); M6 decisions need a judgment_review. Schema: data/grixis/schemas/refine_v2.schema.json.",
            "schema_version": 1, "engine": "grixis_refine v2", "exploratory": True,  # Bot cycle 63.2: stays exploratory after M2/M4 acceptance (Cory t52u scope: approves no refinement result; M6 needs judgment_review) "generated": dt.date.today().isoformat(),
            "m6_gate": {"M2": st2, "M4": st4, "open": gate_open},
            "lift_check": {"pages": lift["pages"], "cardviews": lift["cardviews"], "with_lift": lift["with_lift"], "with_trend": lift["with_trend"],
                           "note": "Confirmed in the cached EDHREC commander JSON: each cardview carries synergy, lift, num_decks, potential_decks and trend_zscore. "
                                   "No fetch timestamp in the payload, so retrieval date = cache file mtime (UTC date)."},
            "decks": out}


ev_R = None


def main():
    global ev_R
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", type=int)
    ap.add_argument("--decks", default="")
    ap.add_argument("--cycle", type=int, default=39)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--engine", choices=("v1", "v2"), help="v1: frozen Bot cycle 39-44 planner, for reproduction only (--plan needs --engine v1); "
                    "v2: exploratory recommendations -> data/grixis_refine_v2.json (Bot cycle 47)")
    a = ap.parse_args()
    if a.plan and a.engine != "v1":
        ap.error("--plan runs the frozen v1 planner; pass --engine v1 explicitly to reproduce it (new work: --engine v2)")
    R = ev_R = ev.Resolver()
    summ = json.loads(SUM.read_text(encoding="utf-8"))
    reg = json.loads((ROOT / "data" / "grixis_pending.json").read_text(encoding="utf-8"))["decks"]
    PEND_DATES.update({k: x["legal_from"] for k, x in reg.items()})
    STATE.update({ga.source_deck_id(k): x["state"] for k, x in (ga.load_json(ga.REGISTRY, {"decks": {}})["decks"]).items()})  # keyed by source id (Bot cycle 55)
    plans = json.loads(PLANS.read_text(encoding="utf-8")) if PLANS.exists() else {"_doc": "Frozen Grixis refinement plans (scripts/grixis_refine.py).", "batches": {}, "decks": {}, "log": {}, "spellbook": {}}
    if a.engine == "v2" and not a.check:
        dids = [d.strip() for d in a.decks.split(",") if d.strip()] or list(summ)
        old = ga.load_json(REFINE_V2) or {}
        doc = plan_v2(dids, R, summ)
        if a.decks and old.get("decks"):
            doc["decks"] = {**old["decks"], **doc["decks"]}
        REFINE_V2.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"grixis refine v2: {len(doc['decks'])} decks, {sum(len(x['recommendations']) for x in doc['decks'].values())} exploratory recommendation(s) -> {REFINE_V2.relative_to(ROOT)}")
        return 0
    if a.plan:
        import subprocess
        import grixis_archive  # Bot cycle 45: the companion's source archive is the source of truth
        src = grixis_archive.TREE
        if src.exists():
            sha = grixis_archive.source_commit()
            prev = plans.get("source", {}).get("commit")
            plans["source"] = {"commit": sha, "checked": dt.date.today().isoformat(),
                               "note": f"`git pull` on {dt.date.today().isoformat()}: " + ("no upstream changes since the Bot cycle 37 re-analysis" if sha == "1836b97" else f"moved from {prev}")}
        dids = [d.strip() for d in a.decks.split(",") if d.strip()]
        assert all(d in summ for d in dids), [d for d in dids if d not in summ]
        old = {d: plans["decks"].get(d, {}) for d in dids}
        plan(dids, a.plan, R, summ, plans, a.cycle)
        b = plans["batches"].get(str(a.plan), {})
        plans["batches"][str(a.plan)] = {"cycle": b.get("cycle", a.cycle), "date": b.get("date", dt.date.today().isoformat()),
                                         "decks": b.get("decks", []) + [d for d in dids if d not in b.get("decks", [])],
                                         **({"rechecked": {"cycle": a.cycle, "date": dt.date.today().isoformat()}} if b and b.get("cycle") != a.cycle else {})}
        for d in dids:
            e = plans["decks"][d]
            prev = [x for x in plans["log"].get(d, []) if x["cycle"] != a.cycle]
            if prev:  # re-check of an earlier batch: log the difference against the previous final list
                was = {(w["cut"], w["add"]) for w in old.get(d, {}).get("swaps", [])}
                now = {(w["cut"], w["add"]) for w in e["swaps"]}
                gone, new = sorted(was - now), sorted(now - was)
                rej = {(x["cut"], x["add"]): x for x in e.get("rejected", [])}
                txt = "; ".join([f"reverted −{c} +{ad} ({rej[(c, ad)]['by']}: {rej[(c, ad)]['why']})" if (c, ad) in rej else f"reverted −{c} +{ad}" for c, ad in gone] +
                                [f"new −{c} +{ad}" for c, ad in new]) or "re-checked: no change"
                hr = load_review().get("hand_review", {}).get(d)
                if hr:
                    txt = f"hand review ({hr['verdict']}): {txt}"
                plans["log"][d] = prev + [{"date": e["date"], "cycle": a.cycle, "batch": f"{a.plan} re-check", "change": f"power-guard re-check: {txt}",
                                           "added": [c for c, _ in gone] + [ad for _, ad in new], "removed": [ad for _, ad in gone] + [c for c, _ in new]}]
                continue
            plans["log"][d] = [x for x in plans["log"].get(d, []) if x["batch"] != a.plan] + [{
                "date": e["date"], "cycle": a.cycle, "batch": a.plan,
                "change": (f"hand review ({load_review()['hand_review'][d]['verdict']}); " if d in load_review().get("hand_review", {}) else "") +
                          ((f"{len(e['swaps'])} commander-first swap(s): " + "; ".join(f"{w['hook']['label']}" for w in e["swaps"])) if e["swaps"] else "reviewed: " + e["decision"]),
                "added": [w["add"] for w in e["swaps"]], "removed": [w["cut"] for w in e["swaps"]]}]
        PLANS.write_text(json.dumps(plans, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    info, metrics, top, problems = render(R, summ, plans, fetch=not a.check)
    files = {}
    for did, v in summ.items():
        p = info[did]["page"]
        blk = block(did, v, info[did], metrics[did], plans) if info[did]["plan"] else ""
        files[p] = inject(p.read_text(encoding="utf-8"), blk)
    files[PAGE] = summary_page(summ, info, metrics, top, plans)
    for did in summ:
        info[did]["metrics"] = metrics[did]
    files.update(exports(summ, info, plans))
    files[OUT] = json.dumps({"_doc": "Bot cycle 39+: per-deck commander-dependence and homogenization metrics (scripts/grixis_refine.py).",
                             "decks": metrics}, indent=1, ensure_ascii=False) + "\n"
    if a.check:
        for p, t in files.items():
            if p == PAGE or p == OUT:
                cur = p.read_text(encoding="utf-8") if p.exists() else None
                if cur is None:
                    problems.append(f"{p.relative_to(ROOT)} missing (run scripts/grixis_refine.py)")
                continue  # metrics depend on caches; the deck blocks and exports below are the contract
            cur = p.read_text(encoding="utf-8") if p.exists() else None
            if cur != t:
                problems.append(f"{p.relative_to(ROOT)} is stale (run scripts/grixis_refine.py)")
        # each export matches its deck page list and passes the hard checks (Bot cycle 47: challenger, source baseline and projection files)
        exc_ok = {x["deck_id"] for x in ga.load_json(ga.EXCEPTIONS, {"exceptions": []})["exceptions"] if x["project_authorization_status"] == "AUTHORIZED_EXCEPTION"}
        for did, v in summ.items():
            pt = ga.projection_text(did, info[did]["src_text"])
            want = {EXP / f"{v['slug']}.txt": (info[did]["fin_text"], "challenger") if info[did]["challenger"] else (pt, "projection") if pt else (info[did]["src_text"], "canonical")}
            if info[did]["challenger"] or pt:
                want[EXP / "source-baseline" / f"{v['slug']}.txt"] = (info[did]["src_text"], "canonical")
            if pt:
                want[EXP / "projections" / f"{v['slug']}.official-legal-projection.txt"] = (pt, "projection")
            for ep, (ref, role) in want.items():
                rel = ep.relative_to(ROOT)
                if not ep.exists():
                    problems.append(f"{rel} missing"); continue
                exp_l = Counter((c["name"] if c else None, z) for q_, c, z in lines_of(ep.read_text(encoding="utf-8"), R) for _ in range(q_))
                fin_l = Counter((c["name"], z) for q_, c, z in lines_of(ref, R) for _ in range(q_))
                if exp_l != fin_l:
                    problems.append(f"{rel} differs from the deck page's {role} list")
                res_e = ev.check(ep.read_text(encoding="utf-8"), R)
                if hard(res_e, info[did]["pending"], did if role == "canonical" else None):
                    problems.append(f"{rel} fails the hard checks")
                if role == "canonical" and did in exc_ok and hard(res_e, info[did]["pending"]) == []:
                    problems.append(f"{rel}: deck has registered project exceptions but the file passes plain legality (exception registry stale?)")
                comp_ban = [i for i in res_e["issues"] if i["type"] == "companion" and "banned as a companion" in i["detail"]]
                if comp_ban and (role != "canonical" or did not in exc_ok):
                    problems.append(f"{rel}: carries a companion banned as a companion outside a registered project exception")
                raw = ep.read_text(encoding="utf-8").rstrip("\n").split("\n")
                bad = [l for l in raw if not re.fullmatch(r"\d+ [^\s].*[^\s]", l)]
                if bad or not raw:
                    problems.append(f"{rel} has malformed line(s): {bad[:3]}")
                cmdl = [l for l in raw if l.endswith(" [Commander]")]
                compl = [l for l in raw if l.endswith(" [Companion]")]
                if not cmdl or raw[:len(cmdl)] != cmdl or not all(l.startswith("1 ") for l in cmdl):
                    problems.append(f"{rel}: commander line(s) must come first as `1 Name [Commander]`")
                if len(compl) > 1 or (compl and raw[len(cmdl)] != compl[0]):
                    problems.append(f"{rel}: at most one `1 Name [Companion]` line, right after the commander line(s)")
                if sum(int(l.split(" ", 1)[0]) for l in raw if not bad and l not in compl) != 100:
                    problems.append(f"{rel} is not 100 cards (companion excluded)")
                if len({l.split(" ", 1)[1] for l in raw}) != len(raw):
                    problems.append(f"{rel} repeats a card line")
        man = json.loads((EXP / "index.json").read_text(encoding="utf-8")) if (EXP / "index.json").exists() else {"files": []}
        for x in man["files"]:
            if x["role"] == "projection" and (x["state"] is not None or x["label"] != ga.PROJECTION_LABEL):
                problems.append(f"index.json {x['file']}: a projection is never canonical or in a state")
            if x["role"] == "challenger" and x["label"] != ga.CHALLENGER_LABEL:
                problems.append(f"index.json {x['file']}: challenger must be labeled '{ga.CHALLENGER_LABEL}'")
            if x["role"] != "canonical" and x["state"] in ga.GATED_STATES:
                problems.append(f"index.json {x['file']}: only a canonical list can carry an approval state")
        for d in summ:
            for w in (plans["decks"].get(d) or {}).get("needs_review", []):
                problems.append(f"{d}: swap −{w['cut']} +{w['add']} has no manual review in data/grixis_refine_review.json")
        n_ref = sum(1 for d in summ if info[d]["plan"])
        print(f"grixis refine: {n_ref}/62 reviewed, {len(summ)} exports; {len(problems)} problem(s)")
        for x in problems:
            print("  ", x)
        return 1 if problems else 0
    for p, t in files.items():
        p.parent.mkdir(parents=True, exist_ok=True)
        if p.suffix == ".md" and p.exists() and not t.startswith("---\n"):
            old = p.read_text(encoding="utf-8")
            if old.startswith("---\n"):
                t = old[:old.index("\n---\n", 4) + 5] + "\n" + t  # keep the front matter front_matter.py wrote
        if not p.exists() or p.read_text(encoding="utf-8") != t:
            p.write_text(t, encoding="utf-8")
    PLANS.write_text(json.dumps(plans, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"grixis refine: {sum(1 for d in summ if info[d]['plan'])}/62 reviewed; {len(problems)} problem(s)")
    for x in problems:
        print("  ", x)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
