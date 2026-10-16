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
Usage:
  python3 scripts/grixis_refine.py --plan 1 --decks A,B,...   # freeze batch 1 swaps (queries Commander Spellbook)
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
import evaluate_decklist as ev  # noqa: E402
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
    ("combat damage / attack triggers", r"combat damage to (a|that) player|dealt combat damage|whenever [^.]* attacks",
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
    ("enters triggers", r"whenever (another|a|one or more|[^.]* or another) [^.]* enters", r"\bflicker|exile [^.]*, then return|return [^.]* to the battlefield|enters[^.]* an additional time"),
    ("casualty / power 2 or greater", r"\bcasualty\b|power 2 or greater", r"\bcasualty\b|creates? [^.]*\d/\d"),
    ("connive / looting", r"\bconniv", r"\bconniv|draw a card, then discard|discard a card, then draw"),
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
    t = otext(c)
    out = set()
    for k in KEY_ROLES:
        rxs = [RX[k]] + ([EXTRA_RX[k]] if k in EXTRA_RX else [])
        for rx in rxs:
            for m in rx.finditer(t):
                if k == "removal" and NOT_REMOVAL.search(sentence(t, m)):
                    continue  # graveyard hate, self-blink and temporary theft are not spot removal
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


def hard(res, pending_cards=()):
    return [i for i in res["issues"] if i["type"] in ev.HARD and not (i["type"] == "not Commander-legal" and i["card"] in pending_cards)]


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
    lists = {d: lines_of(deck_block(ROOT / "grixis" / "decks" / f"{v['slug']}.md"), R) for d, v in summ.items()}
    freq = Counter(n for l in lists.values() for n in nonland_names(l))
    cache = plans.setdefault("spellbook", {})
    reg = json.loads((ROOT / "data" / "grixis_pending.json").read_text(encoding="utf-8"))["decks"]
    for did in dids:
        v = summ[did]
        src = deck_block(ROOT / "grixis" / "decks" / f"{v['slug']}.md")
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
        if dep >= CEIL_DEP and gen <= CEIL_GEN:
            entry["decision"] = f"at/near ceiling: commander dependence {dep:.0%} ≥ {CEIL_DEP:.0%} and generic share {gen:.0%} ≤ {CEIL_GEN:.0%}; unchanged"
            plans["decks"][did] = entry
            continue
        pieces = {n for co in combos.get(did, {}).get("combos", []) for n in co["cards"]}
        cuts = []
        for c in nl:
            s = ctx.syn.get(c["name"])
            if ctx.hook(c) or (s and s[0] >= CUT_SYN) or freq[c["name"]] < GENERIC_MIN or c.get("game_changer") or c["name"] in pieces:
                continue
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
            if not hard(res, pend) and fl <= max(floor_src, tgt) and src_combo_ids <= {co["id"] for co in sb["combos"]}:
                break
            swaps.pop()
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
        fin = apply_swaps(src, e["swaps"]) if e and e["swaps"] else src
        src_lists[did], fin_lists[did] = lines_of(src, R), lines_of(fin, R)
        info[did] = {"src_text": src, "fin_text": fin, "plan": e, "page": p}
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
        if hard(res, pend):
            problems.append(f"{did}: refined list fails {[i['type'] + ' ' + i['card'] for i in hard(res, pend)]}")
        info[did]["res"] = res
        info[did]["pending"] = pend
        if info[did]["plan"] and info[did]["plan"]["swaps"]:
            sb = spellbook(fin_lists[did], cache, did, fetch)
            if not sb:
                problems.append(f"{did}: no Commander Spellbook result cached for the refined list (run without --check)")
                info[did]["sb"] = None
            else:
                info[did]["sb"] = sb
    top = Counter(n for s in sets_src.values() for n in s).most_common(25)
    return info, metrics, top, problems


def fmt_syn(s):
    return f"synergy {s[0]:+d}%, in {s[2]:,} of {s[3]:,} decks ({s[1]}%)" if s else "not listed on the commander's EDHREC page"


def block(did, v, info, m, plans):
    e = info["plan"]
    L = [START, "## Refined list (Bot cycle 39)", "",
         f"> **Commander-first refinement** ([Grixis Mission](../Grixis%20Mission.md), Cory's principles; log: [Grixis Refinement Cycle](../Grixis%20Refinement%20Cycle.md)). "
         "The [source list](#decklist-archidekt-import) above stays as integrated, credited to Cory's "
         "[grixis-commander-encyclopediaGPT](https://github.com/corymstover/grixis-commander-encyclopediaGPT). This section is **our recommendation (guidance)**. "
         "Facts behind it: Scryfall Oracle text, legality and Game Changer flags; EDHREC synergy (community data, cached); Commander Spellbook combos. "
         "Generated by `scripts/grixis_refine.py`.", ""]
    s, f = m["source"], m["final"]
    L += [f"- **Commander hooks (from Oracle text):** {', '.join(m['hooks']) or '—'}.",
          f"- **Commander dependence:** {s['dependence']:.0%} → **{f['dependence']:.0%}** · generic share {s['generic_share']:.0%} → **{f['generic_share']:.0%}** · "
          f"mean overlap with the other 61 lists {s['mean_overlap']:.0%} → **{f['mean_overlap']:.0%}**.",
          f"- **Decision:** {e['decision']}."]
    if info["pending"]:
        L.append(f"- ⏳ **Pending legality:** {', '.join(info['pending'])} are not Commander-legal before {plans_pending_date(did)}; the export is marked pending.")
    if e["swaps"]:
        L += ["", "| Cut | Add | Role kept | Why (commander-specific) | Power guard + review (Bot cycle 40) |", "|---|---|---|---|---|"]
        for w in e["swaps"]:
            h = w["hook"]
            why = (f"**{h['label']}**: {h['commander']} reads \"{q(h['commander_text'])}\"; {w['add']} reads \"{q(h['card_text'])}\". "
                   f"EDHREC: {fmt_syn(w['add_edhrec'])}. Cut: no Oracle hook to the commander, EDHREC {fmt_syn(w['cut_edhrec'])}, "
                   f"in {w['cut_freq']}/62 Grixis lists (generic). MV {w['mv'][0]:g} → {w['mv'][1]:g}.")
            L.append(f"| {w['cut']} | **{w['add']}** | {', '.join(w['roles'])} | {why} | {q('; '.join(w.get('guard') or ['(cycle 39 swap, not re-checked)']))}. **Review:** {q(w.get('review') or '—')} |")
        res, sb = info["res"], info.get("sb")
        two = sum(1 for co in sb["combos"] if co["infinite"] and len(co["cards"]) == 2) if sb else 0
        fl, gcs, mld = ev.bracket_floor(res["cards"], two)
        ok = "✅ 100 cards, singleton, color identity, Commander-legal" if not hard(res, info["pending"]) else "❌ fails"
        L += ["", f"- **Verification (`evaluate_decklist.check`):** {ok}{' (except the ⏳ pending cards)' if info['pending'] else ''}. "
              f"Game Changers {v['gcs'].__len__()} → {len(gcs)} · floor Bracket {v['floor']} → **{fl}** (target {target_of(v)}) · "
              f"Commander Spellbook: {len(sb["combos"]) if sb else "?"} combo(s) ({two} two-card infinite), every source combo kept (queried {sb['queried'] if sb else '?'}).",
              "", "```text", info["fin_text"].strip(), "```"]
    if e.get("rejected"):
        L += ["", "**Considered and rejected:** " + " · ".join(f"−{x['cut']} +{x['add']} ({x['by']}: {q(x['why'])})" for x in e["rejected"])]
    L += ["", "### Refinement log", "", "| Date | Cycle | Change | Cards added | Cards removed |", "|---|---|---|---|---|"]
    for x in plans["log"].get(did, []):
        L.append(f"| {x['date']} | Bot cycle {x['cycle']} (batch {x['batch']}) | {x['change']} | {', '.join(x['added']) or '—'} | {', '.join(x['removed']) or '—'} |")
    L.append(END)
    return "\n".join(L)


PEND_DATES = {}


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
    rest = sorted(f"{q_} {c['name']}" for q_, c, z in lst if z == "main")
    rest.sort(key=lambda l: l.split(" ", 1)[1].lower())
    return "\n".join(cmd + rest) + "\n"


def summary_page(summ, info, metrics, top, plans):
    done = [d for d in summ if plans["decks"].get(d)]
    L = ["# Grixis Refinement Cycle", "",
         f"> **Bot cycle 39+** · Cory's commander-first mission ([Grixis Mission](Grixis%20Mission.md)). Auto-generated by `scripts/grixis_refine.py` from Scryfall Oracle data, "
         "EDHREC synergy (community data, cached) and Commander Spellbook. Metrics are facts about the lists; swaps are guidance. "
         "Source lists stay on each deck page, credited to Cory's [grixis-commander-encyclopediaGPT](https://github.com/corymstover/grixis-commander-encyclopediaGPT). "
         "Archidekt exports: [exports/grixis-archidekt/](../exports/grixis-archidekt/README.md).", "",
         f"Grixis source commit used: `{plans.get('source', {}).get('commit', '?')}` ({plans.get('source', {}).get('note', '')}).", "",
         "## Contents", "- [Status](#status)", "- [Batch log](#batch-log)", "- [Overlap review (manual)](#overlap-review-manual)", "- [All decks: metrics](#all-decks-metrics)", "- [Homogenization](#homogenization)", "- [Method](#method)", "",
         "## Status", "",
         f"- **Reviewed: {len(done)}/62** decks ({sum(1 for d in done if plans['decks'][d]['swaps'])} refined, {sum(1 for d in done if not plans['decks'][d]['swaps'])} at/near ceiling and unchanged). "
         f"{sum(1 for d in summ if info[d]['pending'])} decks are ⏳ pending legality (measured; exports marked pending).",
         f"- Mean commander dependence, all 62 (final lists): **{sum(metrics[d]['final']['dependence'] for d in summ) / len(summ):.0%}** · "
         f"mean generic share: **{sum(metrics[d]['final']['generic_share'] for d in summ) / len(summ):.0%}** · "
         f"mean pairwise overlap: **{sum(metrics[d]['final']['mean_overlap'] for d in summ) / len(summ):.0%}**.",
         f"- Thoracle core present in {sum(1 for d in summ if metrics[d]['final']['thoracle_core'])} lists · median control-core cards per list: "
         f"{sorted(len(metrics[d]['final']['control_core']) for d in summ)[31]}.", "", "## Batch log", ""]
    for b, bv in sorted(plans["batches"].items(), key=lambda kv: int(kv[0])):
        L += [f"### Batch {b} — Bot cycle {bv['cycle']}, {bv['date']}", ""]
        for d in bv["decks"]:
            e = plans["decks"][d]
            v = summ[d]
            nm = " + ".join(v["commanders"])
            m = metrics[d]
            L.append(f"- [{nm}](decks/{v['slug']}.md#refined-list-bot-cycle-39): {e['decision']}. Dependence {m['source']['dependence']:.0%} → {m['final']['dependence']:.0%}." +
                     ("".join(f" Cut **{w['cut']}** → add **{w['add']}** ({w['hook']['label']})." for w in e["swaps"])))
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
        st = ("⏳ pending · " if info[d]["pending"] else "") + ("refined" if e and e["swaps"] else "unchanged (ceiling)" if e else "not reviewed yet")
        cl = summ[f["max_overlap"][1]]["commanders"][0]
        L.append(f"| [{' + '.join(v['commanders'])}](decks/{v['slug']}.md) | {st} | {m['source']['dependence']:.0%}" + (f" → **{f['dependence']:.0%}**" if e and e["swaps"] else "") +
                 f" | {f['generic_share']:.0%} | {f['mean_overlap']:.0%} | {cl} ({f['max_overlap'][0]:.0%}) | {len(f['thoracle_core'])} | {len(f['control_core'])} | {', '.join(m['hooks'][:4])}{' …' if len(m['hooks']) > 4 else ''} |")
    L += ["", "## Homogenization", "", "Most-shared nonland cards across the 62 source lists (count of lists):", "",
          "| Card | Lists |", "|---|---|"] + [f"| {n} | {k} |" for n, k in top]
    L += ["", "## Method", "",
          f"- **Commander dependence (fact-based heuristic):** a nonland, non-commander card counts if (a) its Oracle text or type line matches a *hook* taken from the commander's own Oracle text (mechanic patterns in `HOOKS`, plus creature types named in the commander's text, from CR 205.3m), or (b) its EDHREC synergy on the commander's page is ≥ {DEP_SYN}%. Score = counted / nonland cards. Patterns are loose by design; the score ranks decks, it is not a rules statement.",
          f"- **Generic share:** cards with no commander link that appear in ≥ {GENERIC_MIN} of the 62 source lists. **Overlap:** Jaccard index of nonland card sets. **Thoracle core:** {', '.join(sorted(THORACLE))}. **Control core:** {', '.join(sorted(CONTROL))}.",
          f"- **Ceiling:** a deck with dependence ≥ {CEIL_DEP:.0%} and generic share ≤ {CEIL_GEN:.0%}, or with no qualifying swap, is flagged at/near its ceiling and left unchanged.",
          f"- **Cuts:** only generic cards (≥ {GENERIC_MIN} lists) with no Oracle hook and EDHREC synergy < {CUT_SYN}%. Never a Game Changer, a piece of a Commander Spellbook combo in the list, or a mana source of MV ≤ 2 (speed serves every commander at its ceiling).",
          f"- **Adds:** EDHREC synergy ≥ {ADD_SYN}% and inclusion ≥ {ADD_INC}% on the commander's page, **and** an Oracle hook to the commander; Commander-legal, inside the color identity, no new Game Changer unless the list already has 4+ and targets Bracket 4+, no mass land denial, no extra-turn card unless the list already plays one.",
          f"- **Pairing:** each add replaces a cut whose key roles ({', '.join(KEY_ROLES)}; Oracle patterns) it covers, at MV at most 1 higher; interaction (removal, wipes, counterspells, protection) is only replaced by interaction at equal or lower MV. At most {MAX_SWAPS} swaps per deck per batch.",
          f"- **Power guard (Bot cycle 40):** an add must not be a clear power downgrade of its cut: commander-page inclusion at least the cut's (this commander's players choose it at least as often), overall EDHREC rank no worse than {RANK_X}× the cut's or +{RANK_PLUS}, and no free spell (pitch/commander-free) replaced by a non-free one. Every guard-passing swap needs a written manual review (`data/grixis_refine_review.json`) saying why the add does more in *this* deck; unreviewed swaps are not applied and fail `validate_all`.",
          "- **Verification:** the refined list must pass `evaluate_decklist.check` (100 cards, singleton, color identity, Commander-legal), keep every Commander Spellbook combo of the source list (re-queried), and not raise the bracket floor above the source floor or target. A failing swap is dropped.",
          "- **Frozen decisions:** each batch's swaps are stored in `data/grixis_refine_batches.json`; `validate_all` re-verifies them on every run.",
          "- **Limits:** EDHREC synergy measures how often decks of *this* commander play a card versus all decks of its colors: community data, not a quality judgment. The heuristic cannot see multi-card lines the Oracle patterns miss; at-ceiling decks are candidates for a hand review."]
    return "\n".join(L) + "\n"


def exports(summ, info, plans):
    files = {}
    idx = ["# Grixis Archidekt exports", "",
           "> Generated by `scripts/grixis_refine.py` (Bot cycle 39+). One Archidekt import file per deck: the deck page's **final** list "
           "(the refined list where a batch changed it, otherwise the source list). Format checked against the source repo's Archidekt package "
           "(`exports/archidekt_2026-10-15/`: one `1x Card Name` line per card, commander first, no set codes); here lines read `1 Card Name` and the "
           "commander line carries Archidekt's `[Commander]` category so Archidekt sets it as commander on import. Paste one file into one deck. "
           "`ALL-DECKS.txt` is for reference only (do not paste it into one deck). `validate_all` checks every file against its deck page.", "",
           "| # | File | Commander(s) | Status | Changes vs previous version |", "|---|---|---|---|---|"]
    master = []
    for i, (did, v) in enumerate(summ.items(), 1):
        lst = lines_of(info[did]["fin_text"], ev_R)
        txt = export_txt(lst)
        files[EXP / f"{v['slug']}.txt"] = txt
        e = info[did]["plan"]
        st = ("⏳ PENDING LEGALITY (not Commander-legal before " + plans_pending_date(did) + ") · " if info[did]["pending"] else "") + \
             ("refined" if e and e["swaps"] else "unchanged (at/near ceiling)" if e else "unchanged (not reviewed yet)")
        ch = "; ".join(f"−{w['cut']} +{w['add']} ({w['hook']['label']})" for w in e["swaps"]) if e and e["swaps"] else "none"
        idx.append(f"| {i} | [{v['slug']}.txt]({v['slug']}.txt) | {' + '.join(v['commanders'])} | {st} | {ch} |")
        master += [f"===== {i:02d}/62 — {' + '.join(v['commanders'])} — {st} =====", txt.rstrip(), ""]
    files[EXP / "ALL-DECKS.txt"] = "\n".join(master)
    files[EXP / "README.md"] = "\n".join(idx) + "\n"
    return files


ev_R = None


def main():
    global ev_R
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", type=int)
    ap.add_argument("--decks", default="")
    ap.add_argument("--cycle", type=int, default=39)
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    R = ev_R = ev.Resolver()
    summ = json.loads(SUM.read_text(encoding="utf-8"))
    reg = json.loads((ROOT / "data" / "grixis_pending.json").read_text(encoding="utf-8"))["decks"]
    PEND_DATES.update({k: x["legal_from"] for k, x in reg.items()})
    plans = json.loads(PLANS.read_text(encoding="utf-8")) if PLANS.exists() else {"_doc": "Frozen Grixis refinement plans (scripts/grixis_refine.py).", "batches": {}, "decks": {}, "log": {}, "spellbook": {}}
    if a.plan:
        import subprocess
        src = ROOT.parent / "grixis-src"
        if src.exists():
            sha = subprocess.run(["git", "-C", str(src), "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip()
            prev = plans.get("source", {}).get("commit")
            plans["source"] = {"commit": sha, "checked": dt.date.today().isoformat(),
                               "note": f"`git pull` on {dt.date.today().isoformat()}: " + ("no upstream changes since the Bot cycle 37 re-analysis" if sha == "1836b97" else f"moved from {prev}")}
        dids = [d.strip() for d in a.decks.split(",") if d.strip()]
        assert all(d in summ for d in dids), [d for d in dids if d not in summ]
        old = {d: plans["decks"].get(d, {}) for d in dids}
        plan(dids, a.plan, R, summ, plans, a.cycle)
        b = plans["batches"].get(str(a.plan), {})
        plans["batches"][str(a.plan)] = {"cycle": b.get("cycle", a.cycle), "date": b.get("date", dt.date.today().isoformat()), "decks": dids,
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
                plans["log"][d] = prev + [{"date": e["date"], "cycle": a.cycle, "batch": f"{a.plan} re-check", "change": f"power-guard re-check: {txt}",
                                           "added": [c for c, _ in gone] + [ad for _, ad in new], "removed": [ad for _, ad in gone] + [c for c, _ in new]}]
                continue
            plans["log"][d] = [x for x in plans["log"].get(d, []) if x["batch"] != a.plan] + [{
                "date": e["date"], "cycle": a.cycle, "batch": a.plan,
                "change": (f"{len(e['swaps'])} commander-first swap(s): " + "; ".join(f"{w['hook']['label']}" for w in e["swaps"])) if e["swaps"] else "reviewed: " + e["decision"],
                "added": [w["add"] for w in e["swaps"]], "removed": [w["cut"] for w in e["swaps"]]}]
        PLANS.write_text(json.dumps(plans, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    info, metrics, top, problems = render(R, summ, plans, fetch=not a.check)
    files = {}
    for did, v in summ.items():
        p = info[did]["page"]
        blk = block(did, v, info[did], metrics[did], plans) if info[did]["plan"] else ""
        files[p] = inject(p.read_text(encoding="utf-8"), blk)
    files[PAGE] = summary_page(summ, info, metrics, top, plans)
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
        # each export matches its deck page's final list and passes the hard checks
        for did, v in summ.items():
            ep = EXP / f"{v['slug']}.txt"
            if not ep.exists():
                problems.append(f"exports/grixis-archidekt/{v['slug']}.txt missing"); continue
            exp_l = Counter((c["name"] if c else None, z) for q_, c, z in lines_of(ep.read_text(encoding="utf-8"), R) for _ in range(q_))
            fin_l = Counter((c["name"], z) for q_, c, z in lines_of(info[did]["fin_text"], R) for _ in range(q_))
            if exp_l != fin_l:
                problems.append(f"exports/grixis-archidekt/{v['slug']}.txt differs from the deck page's final list")
            if hard(ev.check(ep.read_text(encoding="utf-8"), R), info[did]["pending"]):
                problems.append(f"exports/grixis-archidekt/{v['slug']}.txt fails the hard checks")
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
