#!/usr/bin/env python3
"""M5 candidate deep dive (Bot cycle 60): per-deck candidate universe, triage, escalations, full reviews,
pairwise swap hypotheses and paired goldfish tests.  Everything here is PROVISIONAL and EXPLORATORY.

Inputs (all local, snapshot-keyed): Scryfall Oracle + default-cards bulk (.cache), the M3 evidence layer
(EDHREC candidates), Commander Spellbook near-misses (data/grixis/candidates/spellbook_almost.json), the blueprint,
the M4 dependency graph and slot audit, simulator v1.1 and the pre-registered paired-test rule (grixis_paired.PREREG).

Universe (UNIVERSE_RULES): every Commander-legal card in the deck's colour identity that is not a basic land and not
in the list, drawn from five sources, then screened, ranked and bounded to 200-500:
  edhrec       EDHREC candidate on the commander page(s) (M3 evidence vectors)
  spellbook    the one missing piece of a Commander Spellbook variant whose other pieces are all in the list
  blueprint    named as a candidate by a blueprint package
  oracle_hook  Oracle-text search: the card's text touches a mechanic the commander's text names (grixis_refine HOOKS)
  package      Oracle/type search: shares a signature creature type of a blueprint package
  new_card     first printed on or after NEW_SINCE (Scryfall default-cards, earliest released_at per oracle id)
  rank_fill    only if the sources above give fewer than 200: identity staples with a key role, by EDHREC overall rank
Triage: the default full-review set is the top clamp(#tier A, 15, 40) by screening score; escalations add full
reviews beyond it for the ESCALATION_REASONS listed in ESCALATION_RULES (Cory constraint 3: 15-40 is not a gate).
Each full review compares the candidate with the blueprint, the role model, the graph and the best incumbent in its
role, and forms one pairwise swap hypothesis (cut = the weakest replaceable incumbent in that role).  Swaps are
swap.schema.json records, state CHALLENGER, exploratory, decision null: never registered, never promoted, no list
changes.  A paired goldfish test (simulator v1.1, PREREG) runs when the model can see something of either card.

  python3 scripts/grixis_candidates.py --build [--deck SLUG] [--jobs N]
  python3 scripts/grixis_candidates.py --check
  python3 scripts/grixis_candidates.py --summary
"""
import argparse, datetime as dt, gzip, hashlib, json, math, pickle, random, re, sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import grixis_authority as ga  # noqa: E402

VERSION = "1"
CYCLE = 60
TODAY = dt.date(2026, 10, 16)
NEW_SINCE = "2026-04-16"            # first printed within 183 days of TODAY = a new card
UNIVERSE_MIN, UNIVERSE_MAX = 200, 500
NICHE_RESERVE = 60                  # universe slots kept for no-EDHREC-row Oracle/package hits
DEFAULT_RANGE = [15, 40]
ESC_CAP = 12                        # escalations listed per reason (the overflow is recorded by name, not dropped silently)
SAMPLES, SEED = 300, 60
TIER_A, TIER_B = 45.0, 25.0
OUT = ROOT / "data" / "grixis" / "candidates"
ALMOST = OUT / "spellbook_almost.json"
GRAPH, EVID, AUDIT, BPS = (ROOT / "data" / "grixis" / x for x in ("graph", "evidence", "audit", "blueprints"))
CACHE = ROOT / ".cache"
KEY_ROLES = ("ramp", "draw", "removal", "wipe", "counter", "protection", "tutor")
INTERACTION = {"removal", "wipe", "counter", "protection"}
SKIP_LAYOUTS = {"token", "double_faced_token", "art_series", "emblem", "scheme", "planar", "vanguard", "augment", "host"}
CUT_ORDER = ["active_cut_candidate", "flexible", "weak_retain", "package_dependent", "meta_dependent", "functional_retain"]
PROTECTED = {"core", "strong_retain", "project_requirement"}
AUTHORITY = {"status": "provisional", "exploratory": True,
             "note": "M5 deep dive. Screening scores are heuristics; EDHREC is a derived metric; goldfish tests are model "
                     "evidence, never win rates. No list changes, no challenger registered or promoted, no swap decided "
                     "(constraints 2, 6, 8). Cory decides."}
UNIVERSE_RULES = {
    "definition": "Commander-legal cards in the deck's colour identity, not basic lands, not in the canonical list, from "
                  "the sources below; screened, ranked by screening score and bounded to [200, 500] (ties by name).",
    "bounds": [UNIVERSE_MIN, UNIVERSE_MAX],
    "sources": {"edhrec": "EDHREC candidate vectors of the M3 evidence layer (commander page(s))",
                "spellbook": "Commander Spellbook find-my-combos almostIncluded: the single missing piece",
                "blueprint": "blueprint package `candidates`",
                "oracle_hook": "Oracle-text search on the bulk: text touches a mechanic named by the commander (grixis_refine HOOKS)",
                "package": "type search: shares a signature creature type (>= 40% of >= 3 members) of a blueprint package",
                "new_card": f"earliest Scryfall printing on or after {NEW_SINCE}",
                "rank_fill": "only when the other sources give < 200: identity cards with a key role, by EDHREC overall rank"},
    "always_kept": "edhrec, spellbook, blueprint and relevant new cards, then the best niche (no EDHREC row) Oracle/package "
                   f"hits up to {NICHE_RESERVE}, then the rest by score",
    "excluded": "not Commander-legal (incl. unreleased / not-yet-legal cards: counted and the best few named in "
                "`not_legal_watchlist`), outside identity, basic lands, already in the list, tokens and non-game layouts"}
SCREEN_RULES = [
    "edhrec: 35 x min(1, inclusion / 0.40) + 25 x clamp(synergy / 0.25, -1, 1) (commander page; derived_metric)",
    "rank: 15 x max(0, 1 - log10(EDHREC overall rank) / 4.5) (Scryfall edhrec_rank; derived_metric)",
    "oracle_hook +12, package type +10, package role +4, blueprint candidate +15 (strategic_judgment / heuristic)",
    "spellbook near-miss +8, +8 more when the variant is infinite (fact)",
    "new card +5; a key role the list has <= 3 of +5; named by a blueprint anti-goal -25",
    f"tier A >= {TIER_A}, B >= {TIER_B}, else C",
]
ESCALATION_RULES = {
    "dependency_analysis": "completes an infinite Spellbook variant whose other pieces are all in the list",
    "new_card": f"new card (>= {NEW_SINCE}) with an Oracle hook, package fit or Spellbook near-miss",
    "unusual_oracle_interaction": "Oracle hook or package-type hit with no EDHREC row on the commander page (niche)",
    "package_gap": "fits a required blueprint package that holds fewer than its min_count in the list",
    "rank_miss_suspected": "EDHREC synergy >= 0.15 but inclusion < 0.10, or a blueprint-named candidate ranked outside the default set",
    "cap": f"at most {ESC_CAP} per reason by score; the overflow is listed by name in triage.escalation_overflow",
}


def sha(b):
    return "sha256:" + hashlib.sha256(b).hexdigest()


def rel(p):
    return str(Path(p).relative_to(ROOT))


# ---------------------------------------------------------------- card pool (deck-independent, cached outside the repo)
def bulk_files():
    o = sorted(CACHE.glob("oracle-cards-*.jsonl.gz"))[-1]
    d = sorted(CACHE.glob("default-cards-*.jsonl.gz"))[-1]
    return o, d


def load_pool():
    """{name: card dict} of Oracle cards, plus {oracle_id: earliest released_at}."""
    o, d = bulk_files()
    pk = Path("/tmp") / f"m5_pool_{o.name}_{d.name}_v{VERSION}.pkl"
    if pk.exists():
        return pickle.loads(pk.read_bytes())
    first = {}
    with gzip.open(d, "rt", encoding="utf-8") as f:
        for line in f:
            line = line.strip().rstrip(",")
            if not line.startswith("{"):
                continue
            c = json.loads(line)
            oid = c.get("oracle_id") or ((c.get("card_faces") or [{}])[0].get("oracle_id"))
            r = c.get("released_at")
            if oid and r and (oid not in first or r < first[oid]):
                first[oid] = r
    cards = {}
    with gzip.open(o, "rt", encoding="utf-8") as f:
        for line in f:
            line = line.strip().rstrip(",")
            if not line.startswith("{"):
                continue
            c = json.loads(line)
            if c.get("layout") in SKIP_LAYOUTS or "Basic Land" in (c.get("type_line") or ""):
                continue
            if not c.get("oracle_id"):
                c["oracle_id"] = (c.get("card_faces") or [{}])[0].get("oracle_id")
            cards[c["name"]] = c
    res = (cards, first)
    pk.write_bytes(pickle.dumps(res))
    return res


def tline(c):
    return c.get("type_line") or " // ".join(f.get("type_line", "") for f in c.get("card_faces") or [])


def otext(c):
    return c.get("oracle_text") or "\n".join(f.get("oracle_text", "") for f in c.get("card_faces") or [])


def subtypes(c):
    t = tline(c).split(" // ")[0]
    return set(t.split("—", 1)[1].split()) if "—" in t and "Creature" in t.split("—")[0] else set()


def is_land(c):
    return "Land" in tline(c).split(" // ")[0].split("—")[0]


_ROLES = {}


def roles_of(c):
    import grixis_refine as gr
    k = c["name"]
    if k not in _ROLES:
        r = set(gr.roles(c))
        if is_land(c):
            r.add("land")
        _ROLES[k] = sorted(r)
    return _ROLES[k]


def digest(c):
    t = re.sub(r"\([^)]*\)", "", otext(c)).strip().split("\n")[0].split(". ")[0].strip(" .")
    return (t[:89] + "…") if len(t) > 90 else t


def cost_of(c):
    return c.get("mana_cost") or (c.get("card_faces") or [{}])[0].get("mana_cost") or ""


# ---------------------------------------------------------------- per-deck context
class DeckCtx:
    def __init__(self, did, v, R, reg, pool, first, almost):
        import grixis_refine as gr
        self.did, self.v, self.slug = did, v, v["slug"]
        self.rid = ga.registry_id(did)
        self.e = reg["decks"][self.rid]
        self.text = ga.deck_block_text(self.slug)
        self.ents = ga.list_entries(self.text, R)
        self.names = {n for _, _, _, n in self.ents}
        self.cards = {n: R.get(n)[0] for n in self.names}
        self.cmd_names = [n for z, _, _, n in self.ents if z == "commander"]
        self.ci = set().union(*(set(self.cards[n].get("color_identity", [])) for n in self.cmd_names))
        self.ctx = gr.Ctx([self.cards[n] for n in self.cmd_names])
        bpf = BPS / f"{self.slug}.json"
        self.bpf = bpf
        self.bp = json.loads(bpf.read_text(encoding="utf-8")) if bpf.exists() else {}
        self.g = json.loads((GRAPH / f"{self.slug}.json").read_text(encoding="utf-8"))
        self.ev = json.loads((EVID / f"{self.slug}.json").read_text(encoding="utf-8"))
        self.au = json.loads((AUDIT / f"{self.slug}.json").read_text(encoding="utf-8"))
        cols = self.ev["edhrec"]["columns"]
        self.edh = {x["card"]: dict(zip(cols, x["edhrec"])) for x in self.ev["vectors"] if x.get("edhrec")}
        self.ev_cands = [x["card"] for x in self.ev["vectors"] if x["status"] == "candidate"]
        self.slots = {s["card"]: s for s in self.au["slots"]}
        tp = OUT / "tournament" / f"{self.slug}.json"
        self.tour = json.loads(tp.read_text(encoding="utf-8")) if tp.exists() else None
        self.tour_ref = f"tournament:{rel(tp)}"
        self.pool, self.first = pool, first
        self.anti = " ".join((self.bp.get("anti_goals") or {}).get("value", []) or [])
        alm = almost["decks"].get(self.slug, {"variants": [], "sig": None})
        self.almost_sig_ok = alm.get("sig") == hashlib.sha256("\n".join(sorted(
            [n for z, _, _, n in self.ents if z == "commander"] + [n for z, _, _, n in self.ents if z == "main"])).encode()).hexdigest()[:16]
        self.almost = {}
        for var in alm["variants"]:
            self.almost.setdefault(var["missing"], []).append(var)
        self.role_count = Counter()
        for n, s in self.slots.items():
            if s["zone"] == "main":
                for r in s["roles"]:
                    self.role_count[r] += s["quantity"]
        # package signatures
        self.pk = {}
        for p in self.bp.get("packages", []):
            mem = [self.pool.get(n) or self.cards.get(n) for n in p.get("cards", [])]
            mem = [m for m in mem if m]
            st = Counter(t for m in mem for t in subtypes(m))
            rl = Counter(r for m in mem for r in roles_of(m) if r != "land")
            sig_t = {t for t, k in st.items() if len(mem) >= 3 and k >= 0.4 * len(mem)}
            sig_r = {r for r, k in rl.items() if len(mem) >= 3 and k >= 0.5 * len(mem)}
            inlist = sum(1 for n in p.get("cards", []) if n in self.names)
            self.pk[p["id"]] = {"types": sig_t, "roles": sig_r, "required": bool(p.get("required")),
                                "min": p.get("min_count"), "in_list": inlist, "candidates": set(p.get("candidates") or [])}

    def legal_in_identity(self, c):
        return (c.get("legalities") or {}).get("commander") == "legal" and set(c.get("color_identity", [])) <= self.ci \
            and c["name"] not in self.names and "Basic Land" not in tline(c)


# ---------------------------------------------------------------- screening
def screen(D, name, c, src):
    """(score, parts, facts) for one candidate."""
    parts, facts = {}, {}
    er = D.edh.get(name)
    if er and name in D.ev_cands:
        inc, syn = er["inclusion"], er["synergy"] or 0.0
        parts["edhrec"] = round(35 * min(1.0, inc / 0.40) + 25 * max(-1.0, min(1.0, syn / 0.25)), 2)
        facts["edhrec"] = {"inclusion": inc, "synergy": er["synergy"], "num_decks": er["num_decks"], "confidence": er["confidence"]}
    rk = c.get("edhrec_rank")
    if rk:
        parts["rank"] = round(15 * max(0.0, 1 - math.log10(rk) / 4.5), 2)
    facts["edhrec_rank"] = rk
    h = D.ctx.hook(c)
    if h:
        parts["oracle_hook"] = 12
        facts["oracle_hook"] = h["label"]
    st, rl = subtypes(c), set(roles_of(c))
    pt = sorted(p for p, x in D.pk.items() if st & x["types"])
    pr = sorted(p for p, x in D.pk.items() if not (st & x["types"]) and rl & x["roles"])
    if pt:
        parts["package_type"] = 10
    elif pr:
        parts["package_role"] = 4
    facts["packages"] = pt + pr
    facts["package_basis"] = {p: "type" for p in pt} | {p: "role" for p in pr}
    bpc = sorted(p for p, x in D.pk.items() if name in x["candidates"])
    if bpc:
        parts["blueprint"] = 15
        facts["blueprint_candidate_of"] = bpc
    vs = D.almost.get(name, [])
    if vs:
        parts["spellbook"] = 8 + (8 if any(v["infinite"] for v in vs) else 0)
        facts["spellbook"] = sorted(v["id"] for v in vs)[:8]
        facts["spellbook_infinite"] = any(v["infinite"] for v in vs)
    fr = D.first.get(c.get("oracle_id"))
    facts["first_printed"] = fr
    if fr and fr >= NEW_SINCE:
        parts["new_card"] = 5
    scarce = [r for r in rl if r in KEY_ROLES and D.role_count[r] <= 3]
    if scarce:
        parts["role_need"] = 5
        facts["scarce_roles"] = sorted(scarce)
    if len(name) > 4 and name in D.anti:
        parts["anti_goal"] = -25
    facts["roles"] = sorted(rl)
    return round(sum(parts.values()), 2), parts, facts


def build_universe(D):
    pool = D.pool
    cand = {}  # name -> set(sources)

    def add(n, s):
        c = pool.get(n)
        if c is None or not D.legal_in_identity(c):
            return False
        cand.setdefault(n, set()).add(s)
        return True

    excluded = Counter()
    for n in D.ev_cands:
        if not add(n, "edhrec"):
            excluded["edhrec_not_legal_or_unresolved"] += 1
    for n in D.almost:
        if not add(n, "spellbook"):
            excluded["spellbook_not_legal_or_outside_identity"] += 1
    for x in D.pk.values():
        for n in x["candidates"]:
            add(n, "blueprint")
    watch = []
    pkt = set().union(*[x["types"] for x in D.pk.values()]) if D.pk else set()
    for n, c in pool.items():
        if n in D.names or not set(c.get("color_identity", [])) <= D.ci:
            continue
        legal = (c.get("legalities") or {}).get("commander") == "legal"
        hook = D.ctx.hook(c)
        typ = bool(subtypes(c) & pkt)
        fr = D.first.get(c.get("oracle_id")) or ""
        if not legal:
            if (hook or typ) and fr >= NEW_SINCE and (c.get("legalities") or {}).get("commander") == "not_legal" and not c.get("digital"):
                watch.append((fr, n))
            continue
        if hook:
            cand.setdefault(n, set()).add("oracle_hook")
        if typ:
            cand.setdefault(n, set()).add("package")
        if fr >= NEW_SINCE and (hook or typ or set(roles_of(c)) & set(KEY_ROLES)):
            cand.setdefault(n, set()).add("new_card")
    scored = {}
    for n, s in cand.items():
        scored[n] = screen(D, n, pool[n], s)
    key = lambda n: (-scored[n][0], n)
    must = [n for n, s in cand.items() if s & {"edhrec", "spellbook", "blueprint"} or ("new_card" in s and len(s) > 1)]
    niche = [n for n, s in cand.items() if n not in must and s & {"oracle_hook", "package"} and n not in D.edh]
    rest = [n for n in cand if n not in must and n not in niche]
    must.sort(key=key), niche.sort(key=key), rest.sort(key=key)
    room = UNIVERSE_MAX - min(len(niche), NICHE_RESERVE)
    keep = must[:room]
    keep += niche[:UNIVERSE_MAX - len(keep)]
    left = sorted([n for n in must[room:]] + niche[len(keep) - len(must[:room]):] + rest, key=key)
    keep += left[:UNIVERSE_MAX - len(keep)]
    if len(keep) < UNIVERSE_MIN:
        fill = sorted((c.get("edhrec_rank") or 10 ** 9, n) for n, c in pool.items()
                      if n not in cand and D.legal_in_identity(c) and set(roles_of(c)) & set(KEY_ROLES))
        for _, n in fill[:UNIVERSE_MIN - len(keep)]:
            cand[n] = {"rank_fill"}
            scored[n] = screen(D, n, pool[n], cand[n])
            keep.append(n)
    keep.sort(key=key)
    src_all = Counter(s for n in cand for s in cand[n])
    src_kept = Counter(s for n in keep for s in cand[n])
    watch.sort(key=lambda x: (x[0], x[1]))
    meta = {"considered": len(cand), "size": len(keep), "sources_considered": dict(sorted(src_all.items())),
            "sources_kept": dict(sorted(src_kept.items())), "excluded": dict(sorted(excluded.items())),
            "not_legal_watchlist": {"count": len(watch), "cards": [f"{n} ({fr})" for fr, n in watch[-10:]]},
            "spellbook_snapshot_matches_list": D.almost_sig_ok}
    return keep, cand, scored, meta


# ---------------------------------------------------------------- triage
def tier(score):
    return "A" if score >= TIER_A else "B" if score >= TIER_B else "C"


def triage(D, keep, cand, scored):
    nA = sum(1 for n in keep if tier(scored[n][0]) == "A")
    k = max(DEFAULT_RANGE[0], min(DEFAULT_RANGE[1], nA))
    default = keep[:k]
    esc = {}
    over = {}
    reasons = {r: [] for r in ESCALATION_RULES if r != "cap"}
    for n in keep[k:]:
        sc, parts, f = scored[n]
        s = cand[n]
        if f.get("spellbook_infinite"):
            reasons["dependency_analysis"].append(n)
        if "new_card" in parts and (f.get("oracle_hook") or f.get("packages") or f.get("spellbook")):
            reasons["new_card"].append(n)
        if (f.get("oracle_hook") or "package_type" in parts) and n not in D.edh:
            reasons["unusual_oracle_interaction"].append(n)
        gap = [p for p in f.get("packages", []) if D.pk[p]["required"] and D.pk[p]["min"] and D.pk[p]["in_list"] < D.pk[p]["min"]
               and f["package_basis"].get(p) == "type"]
        if gap:
            reasons["package_gap"].append(n)
        e = f.get("edhrec") or {}
        if (e.get("synergy") is not None and e["synergy"] >= 0.15 and e["inclusion"] < 0.10) or "blueprint" in s:
            reasons["rank_miss_suspected"].append(n)
    for r, ns in reasons.items():
        for n in ns[:ESC_CAP]:
            esc.setdefault(n, []).append(r)
        if len(ns) > ESC_CAP:
            over[r] = ns[ESC_CAP:]
    return default, esc, over, k


def esc_refs(D, n, rs, f):
    out = []
    for r in rs:
        if r == "dependency_analysis":
            out += [f"spellbook:{i}" for i in f.get("spellbook", [])[:3]]
        elif r == "new_card":
            out.append(f"oracle:{n}#first_printed={f.get('first_printed')}")
        elif r == "unusual_oracle_interaction":
            out.append(f"oracle:{n}" + (f"#hook={f['oracle_hook']}" if f.get("oracle_hook") else "#package_type"))
        elif r == "package_gap":
            out += [f"blueprint:{rel(D.bpf)}#packages/{p}" for p in f.get("packages", []) if D.pk[p]["required"]][:2]
        elif r == "rank_miss_suspected":
            out.append(f"evidence:data/grixis/evidence/{D.slug}.json#{n}" if f.get("edhrec") else f"blueprint:{rel(D.bpf)}#packages")
    return sorted(set(out))


# ---------------------------------------------------------------- full review
def type_key(c):
    t = tline(c).split(" // ")[0].split("—")[0]
    for w in ("Creature", "Planeswalker", "Artifact", "Enchantment", "Instant", "Sorcery", "Battle"):
        if w in t:
            return ("type", w)
    return ("type", "other")


def role_key(D, n, c, f):
    """(kind, value): the role the candidate competes in."""
    rl = f["roles"]
    if "land" in rl:
        return ("land", "land")
    for r in KEY_ROLES:
        if r in rl:
            return ("role", r)
    if f.get("packages"):
        return ("package", f["packages"][0])
    if f.get("oracle_hook"):
        return ("hook", f["oracle_hook"])
    return type_key(c)


def in_role(D, kind, val, s, inc_card):
    if kind == "land":
        return "land" in s["roles"]
    if "land" in s["roles"]:
        return False
    if kind == "role":
        return val in s["roles"]
    if kind == "package":
        return val in s["packages"]
    if kind == "hook":
        body = tline(inc_card) + "\n" + otext(inc_card) if inc_card else ""
        return any(lab == val and rx.search(body) for lab, _, _, rx in D.ctx.hooks)
    return inc_card is not None and val in tline(inc_card).split(" // ")[0].split("—")[0]


def incl(D, n):
    e = D.edh.get(n)
    return e["inclusion"] if e else None


def pick(D, kind, val, completes_with, R):
    mates = []
    for n, s in sorted(D.slots.items()):
        if s["zone"] != "main":
            continue
        ic = D.cards.get(n) or R.get(n)[0]
        if in_role(D, kind, val, s, ic):
            mates.append((n, s))
    nonbasic = [(n, s) for n, s in mates if not (n in D.cards and "Basic Land" in tline(D.cards[n]))]
    bench = max(nonbasic, key=lambda x: ((incl(D, x[0]) or 0.0), x[0]), default=None)
    elig = [(n, s) for n, s in mates if s["disposition"] not in PROTECTED and n not in completes_with and s["disposition"] in CUT_ORDER]
    cut = min(elig, key=lambda x: (CUT_ORDER.index(x[1]["disposition"]), incl(D, x[0]) or 0.0, -x[1]["redundancy"], x[0]), default=None)
    return mates, bench, cut


def full_review(D, n, c, sc, parts, f, R):
    comp_with = set()
    inf = False
    for v in D.almost.get(n, []):
        comp_with |= set(v["cards"]) - {n}
        inf |= v["infinite"]
    kind, val = role_key(D, n, c, f)
    mates, bench, cut = pick(D, kind, val, comp_with, R)
    if cut is None and kind != "type":  # nothing replaceable in the primary role: fall back to the card type
        kind, val = type_key(c)
        mates, bench, cut = pick(D, kind, val, comp_with, R)
    bref = f"blueprint:{rel(D.bpf)}"
    named = sorted(p for p, x in D.pk.items() if n in x["candidates"])
    anti = len(n) > 4 and n in D.anti
    fit = "strong" if (named or f.get("spellbook_infinite") or ("package_type" in parts and f.get("oracle_hook"))) else \
        "partial" if (f.get("oracle_hook") or f.get("packages")) else "none"
    e = f.get("edhrec") or {}
    cmp_ = None
    if bench:
        bn, bs = bench
        be = D.edh.get(bn) or {}
        bc = D.cards.get(bn) or R.get(bn)[0]
        d_inc = None if e.get("inclusion") is None or be.get("inclusion") is None else round(e["inclusion"] - be["inclusion"], 4)
        d_syn = None if e.get("synergy") is None or be.get("synergy") is None else round(e["synergy"] - be["synergy"], 4)
        d_mv = int(c.get("cmc") or 0) - int(bc.get("cmc") or 0) if bc else None
        verdict = "unknown" if d_inc is None else "above" if d_inc > 0.05 else "below" if d_inc < -0.15 else "comparable"
        cmp_ = {"card": bn, "disposition": bs["disposition"], "inclusion": be.get("inclusion"), "synergy": be.get("synergy"),
                "mv_delta": d_mv, "inclusion_delta": d_inc, "synergy_delta": d_syn, "on_inclusion": verdict,
                "basis": "highest EDHREC inclusion among incumbents in the same role (derived_metric)"}
    items = [{"id": f"oracle:{n}", "class": "fact", "confidence": "verified"},
             {"id": f"screen:{D.slug}:{n}", "class": "heuristic", "confidence": "moderate"}]
    items += [{"id": f"role:{r}", "class": "heuristic", "confidence": "moderate"} for r in f["roles"]]
    if e:
        items.append({"id": f"evidence:data/grixis/evidence/{D.slug}.json#{n}", "class": "derived_metric", "confidence": e.get("confidence") or "moderate"})
    items += [{"id": f"spellbook:{i}", "class": "fact", "confidence": "verified"} for i in f.get("spellbook", [])[:4]]
    items += [{"id": f"{bref}#packages/{p}", "class": "strategic_judgment", "confidence": "moderate"} for p in named]
    if f.get("oracle_hook"):
        items.append({"id": f"oracle:{n}#hook={f['oracle_hook']}", "class": "heuristic", "confidence": "moderate"})
    tour = None
    if D.tour and D.tour.get("status") == "collected":
        tc = D.tour["cards"]
        tour = {"window": D.tour["window"], "retrieved": D.tour["retrieved"], "commander_entries": D.tour["sample_size"],
                "card": tc.get(n), "cut": tc.get(cut[0]) if cut else None}
        if tc.get(n):
            items.append({"id": f"{D.tour_ref}#{n}", "class": "derived_metric", "confidence": "low" if (tc[n].get("withCard") or {}).get("entries", 0) < 30 else "moderate"})
    ok, why_not = ga.decision_support_ok(items)
    lines = [f"{cost_of(c) or 'MV ' + str(int(c.get('cmc') or 0))} {tline(c).split(' // ')[0]}: “{digest(c)}”."]
    lines.append(f"Competes as {kind} `{val}` ({len(mates)} incumbent(s) in that role).")
    lines.append(f"Blueprint fit {fit}" + (f": named by {', '.join(named)}" if named else "") +
                 (f"; Oracle hook {f['oracle_hook']}" if f.get("oracle_hook") else "") +
                 (f"; packages {', '.join(f['packages'])}" if f.get("packages") else "") + ".")
    if anti:
        lines.append("A blueprint anti-goal names it.")
    if f.get("spellbook"):
        lines.append(f"Spellbook: completes {len(D.almost.get(n, []))} variant(s) with " + ", ".join(sorted(comp_with)[:4]) +
                     (" (infinite)" if inf else "") + ".")
    if cmp_:
        lines.append(f"Best incumbent in role: {cmp_['card']} ({cmp_['disposition'].replace('_', ' ')}" +
                     (f", EDHREC {cmp_['inclusion']:.0%}" if cmp_["inclusion"] is not None else "") + f"); candidate is {cmp_['on_inclusion']} on inclusion.")
    if e:
        lines.append(f"EDHREC inclusion {e['inclusion']:.1%}" + (f", synergy {e['synergy']:+.2f}" if e.get("synergy") is not None else "") + ".")
    else:
        lines.append("No EDHREC row on the commander page.")
    if tour and tour["card"]:
        w = tour["card"].get("withCard") or {}
        lines.append(f"EDHTop16 ({tour['window']}): in {w.get('entries', 0)} of {tour['commander_entries']} tournament entries" +
                     (f", conversion {w['conversion']:.0%}" if w.get("conversion") is not None else "") + ".")
    if cut:
        lines.append(f"Swap hypothesis: cut {cut[0]} ({cut[1]['disposition'].replace('_', ' ')}).")
    else:
        lines.append("No replaceable incumbent in role (all protected): no swap hypothesis.")
    rv = {"role": {"kind": kind, "value": val, "incumbents": len(mates), "list_counts": {r: D.role_count[r] for r in f["roles"] if r in KEY_ROLES or r == "land"}},
          "blueprint": {"fit": fit, "named_by": named, "oracle_hook": f.get("oracle_hook"), "packages": f.get("packages", []), "anti_goal": anti},
          "graph": {"completes_spellbook": f.get("spellbook", []), "infinite": inf, "with_incumbents": sorted(comp_with)[:8]},
          "best_incumbent": cmp_, "cut": cut[0] if cut else None, **({"tournament": tour} if tour else {}), "assessment": " ".join(lines),
          "evidence_classes": dict(sorted(Counter(i["class"] for i in items).items())),
          "decision_support": {"ok": ok, "why_not": why_not}}
    return rv, cut, items


# ---------------------------------------------------------------- swaps and paired tests
def swap_text(D, cut, add):
    out, done = [], False
    for l in D.text.splitlines():
        m = re.match(r"^\s*(\d+)x?\s+(.+?)(\s+\[.*\])?\s*$", l)
        if not done and m and m.group(2).strip() == cut:
            q = int(m.group(1))
            if q > 1:
                out.append(f"{q - 1} {cut}")
            out.append(f"1 {add}")
            done = True
            continue
        out.append(l)
    if not done:
        raise ValueError(f"{D.slug}: cut {cut} not found in the list text")
    return "\n".join(out) + "\n"


def modelled(cm):
    return sorted(k for k, v in cm.get("v11", {}).items() if v) + (["mana source"] if cm.get("source") else []) + (["land"] if cm.get("land") else [])


def run_paired(D, base, add_c, cut, R):
    import grixis_sim as gs, grixis_paired as gp
    am = gs.card_model(add_c, D.ci)
    i = next(j for j, x in enumerate(base.library) if x["name"] == cut)
    lib = base.library[:i] + [am] + base.library[i + 1:]
    combos = list(base.combos) + [{"id": v["id"], "cards": v["cards"]} for v in D.almost.get(add_c["name"], [])
                                  if set(v["cards"]) - {add_c["name"]} <= ({x["name"] for x in lib} | {x["name"] for x in base.commanders})
                                  and cut not in v["cards"]]
    b = gs.Deck(base.slug, base.commanders, lib, base.key_sets, combos)
    b.ci = base.ci
    b.engine, b.gy_combo = base.engine, base.gy_combo
    res, sw = gp.paired(base, b, SAMPLES, SEED, pairs=[(cut, add_c["name"])], model=gs.VERSION)
    return res, sw, b, len(combos) - len(base.combos)


def swap_class(f, parts):
    if "new_card" in parts:
        return "new_card"
    if f.get("spellbook_infinite"):
        return "alt_win"
    if set(f["roles"]) & INTERACTION:
        return "resilience"
    if f.get("oracle_hook") or f.get("packages") or "blueprint" in parts:
        return "identity_max"
    return "raw_efficiency"


def make_swap(D, n, c, parts, f, rv, cut, items, R, base, base_cm):
    import grixis_sim as gs, grixis_paired as gp
    text = swap_text(D, cut, n)
    rh = ga.text_hash(text, R)
    sid = "swap:" + D.slug + ":m5:" + hashlib.sha256(f"{D.e['canonical_project_list']['hash']}|{cut}|{n}".encode()).hexdigest()[:12]
    am, cm = gs.card_model(c, D.ci), base_cm[cut]
    seen_a, seen_c = modelled(am), modelled(cm)
    nm = D.almost.get(n, [])
    can = bool(seen_a or seen_c or nm or any(cut in s for s in base.key_sets.values()) or any(cut in co["cards"] for co in base.combos))
    test, note = None, None
    unseen = [r for r in f["roles"] if r in ("draw", "removal", "wipe", "counter", "protection") and not (r == "draw" and am.get("v11", {}).get("draw"))]
    cut_roles = D.slots[cut]["roles"]
    blind = sorted(set(unseen + [r for r in cut_roles if r in INTERACTION]))
    model_cant = (["interaction (" + ", ".join(blind) + ")"] if blind else []) + \
                 (["the Oracle hook / commander synergy"] if f.get("oracle_hook") else []) + \
                 (["opponents, combat and multiplayer politics"])
    if can:
        res, sw, b, added = run_paired(D, base, c, cut, R)
        cov = gp.coverage(base, b, sw, gs.VERSION)
        chal = {"hash": rh, "id": sid, "label": f"M5 exploratory swap {cut} → {n}"}
        test = gp.record(D.slug, D.did, D.e["canonical_project_list"]["hash"], chal, SAMPLES, SEED, res, sw, gs.VERSION, cov)
        for x in test["results"]:  # the shared method text lives once per file in test_common (size)
            x["method"] = "paired goldfish; see test_common.method" + ("" if x["metric"] == gp.PREREG["primary"]["metric"] else "; secondary (does not set the verdict)")
        test["limitations"] = [f"Simulator v{gs.VERSION} limitations: see this file's test_common.limitations (grixis_paired.LIMITATIONS_BY_MODEL)."] + cov + [
            "M5 exploratory paired test (Bot cycle 60): not a registered challenger; the result is model evidence only."] + \
            ([f"Spellbook near-miss variant(s) completed by the add counted as combos for the win-turn proxy ({added})."] if added else []) + \
            [f"The model cannot see: {'; '.join(model_cant)}."]
    else:
        note = (f"Not modelable: simulator v{gs.VERSION} sees neither card beyond mana value and castability "
                f"({n}: MV {am['mv']}; {cut}: MV {cm['mv']}); the swap's value lies in {'; '.join(model_cant)}.")
    pv = gp.verdict(test["results"]) if test else None
    prim = next(x for x in test["results"] if x["metric"] == gp.PREREG["primary"]["metric"]) if test else None
    speed = {"pass": "+", "fail": "-", "no_detectable_difference": "0"}.get(pv, "?")
    ar, crl = set(f["roles"]) & INTERACTION, set(cut_roles) & INTERACTION
    inter = "+" if ar - crl else "-" if crl - ar else "0"
    ch = D.ctx.hook(D.cards.get(cut) or R.get(cut)[0])
    ident = "+" if (f.get("oracle_hook") or f.get("packages")) and not (ch or D.slots[cut]["packages"]) else \
        "-" if (ch or D.slots[cut]["packages"]) and not (f.get("oracle_hook") or f.get("packages")) else "0"
    ev = sorted(set(i["id"] for i in items) | {f"audit:data/grixis/audit/{D.slug}.json#{cut}"})
    sw = {"schema_version": 1, "id": sid, "deck_id": D.rid, "challenger_class": swap_class(f, parts),
          "base_hash": D.e["canonical_project_list"]["hash"], "result_hash": rh, "adds": [n], "cuts": [cut],
          "role_package": f"{rv['role']['kind']}:{rv['role']['value']}",
          "hypothesis": f"Replacing {cut} with {n} in role {rv['role']['value']} improves the deck's fit or efficiency "
                        f"without breaking a dependency (cut is {D.slots[cut]['disposition'].replace('_', ' ')}; add blueprint fit {rv['blueprint']['fit']}).",
          "expected_benefit": "; ".join(filter(None, [
              f"Oracle hook {f['oracle_hook']}" if f.get("oracle_hook") else "",
              f"completes Spellbook {', '.join(f['spellbook'][:2])}" if f.get("spellbook") else "",
              f"EDHREC inclusion {f['edhrec']['inclusion']:.1%} vs cut {(incl(D, cut) or 0):.1%}" if f.get("edhrec") else "",
              f"roles {', '.join(f['roles'])}" if f["roles"] else ""])) or "unclear (screening only)",
          "expected_cost": f"loses {cut}: " + (D.slots[cut]["reason"][:220]),
          "rules_interactions": [], "legality": {"official": "legal", "project_authorization": "NOT_REQUIRED"},
          "impacts": {"identity": ident, "power": "?", "speed": speed, "consistency": "?", "resilience": "?", "interaction": inter,
                      "distinctiveness": "?", "commander_dependence": "?", "homogenization": "?", "complexity": "?"},
          "priors_overridden": [], "evidence": ev, "tests": [test["id"]] if test else [],
          "state": "CHALLENGER", "exploratory": True,
          "decision": {"verdict": None, "confidence": "test_required", "reason": None, "by": None, "date": None}}
    goldfish = {"test": test["id"], "verdict": pv, "primary_diff": prim["diff"], "primary_ci95": prim["ci95"],
                "model_cannot_see": model_cant} if test else {"test": None, "verdict": None, "not_modelable": note, "model_cannot_see": model_cant}
    return sw, test, goldfish


# ---------------------------------------------------------------- deck build
def build_deck(did, v, R, reg, pool, first, almost):
    import grixis_sim as gs, grixis_paired as gp
    D = DeckCtx(did, v, R, reg, pool, first, almost)
    keep, cand, scored, meta = build_universe(D)
    default, esc, over, k = triage(D, keep, cand, scored)
    full = set(default) | set(esc)
    base = gs.load_deck(D.slug, R)
    base_cm = {x["name"]: x for x in base.library}
    recs, swaps, tests = [], [], []
    for i, n in enumerate(keep):
        c = pool[n]
        sc, parts, f = scored[n]
        rs = esc.get(n, [])
        rec = {"schema_version": 1, "deck_id": D.rid, "card": n, "oracle_id": c.get("oracle_id") or "", "rank": i + 1, "tier": tier(sc),
               "full_review": n in full,
               "escalation": {"escalated": bool(rs), "reasons": rs, "evidence_refs": esc_refs(D, n, rs, f) if rs else [],
                              "by": "script:grixis_candidates.py" if rs else None,
                              "note": ("; ".join(ESCALATION_RULES[r] for r in rs)) if rs else None},
               "evidence": sorted({f"oracle:{n}"} | ({f"evidence:data/grixis/evidence/{D.slug}.json#{n}"} if f.get("edhrec") else set()) |
                                  {f"spellbook:{x}" for x in f.get("spellbook", [])[:4]}),
               "workload": {"default_full_review_range": DEFAULT_RANGE, "is_gate": False},
               "sources": sorted(cand[n]), "screening": {"score": sc, "parts": parts, "facts": f}}
        if n in full:
            rv, cut, items = full_review(D, n, c, sc, parts, f, R)
            rec["review"] = rv
            if cut:
                sw, test, gold = make_swap(D, n, c, parts, f, rv, cut[0], items, R, base, base_cm)
                rec["review"]["swap"] = sw["id"]
                same = {ch.get("hash"): ch.get("id") for ch in D.e.get("challengers") or []}.get(sw["result_hash"])
                if same:  # an independent rediscovery of a registered challenger: noted, never merged into it
                    rec["review"]["matches_registered_challenger"] = same
                rec["review"]["goldfish"] = gold
                swaps.append(sw)
                if test:
                    tests.append(test)
        recs.append(rec)
    sid = sha((json.dumps([D.g["snapshot"]["id"], D.ev["snapshot"]["id"], D.au["snapshot"]["id"], D.au["list_hash"],
                           sha(ALMOST.read_bytes()), *[p.name for p in bulk_files()], sha(Path(__file__).read_bytes()),
                           sha(D.bpf.read_bytes()) if D.bpf.exists() else "", gs.model_sha256(), VERSION])).encode())
    vd = Counter(t["verdict"] for t in tests)
    doc = {"schema_version": 1, "deck_id": D.rid, "slug": D.slug, "generated_by": f"scripts/grixis_candidates.py v{VERSION}", "cycle": CYCLE,
           "list_hash": D.e["canonical_project_list"]["hash"], "pass_id": f"m5:{D.slug}:c{CYCLE}:" + sid[7:19],
           "snapshot": {"id": sid, "graph": D.g["snapshot"]["id"], "evidence": D.ev["snapshot"]["id"], "audit": D.au["snapshot"]["id"],
                        "oracle_bulk": bulk_files()[0].name, "default_bulk": bulk_files()[1].name,
                        "spellbook_almost": {"retrieved": almost["retrieved"], "sha256": sha(ALMOST.read_bytes())},
                        "edhrec_pages": D.ev["edhrec"]["pages"], "simulator": {"version": gs.VERSION, "model_sha256": gs.model_sha256()},
                        "date": TODAY.isoformat()},
           "authority": dict(AUTHORITY, m2_status=reg["program"]["milestones"]["M2"]["status"]),
           "universe": dict(UNIVERSE_RULES, **meta, screen_rules=SCREEN_RULES),
           "triage": {"default_full_reviews": k, "default_rule": f"top clamp(#tier A, {DEFAULT_RANGE[0]}, {DEFAULT_RANGE[1]}) by screening score",
                      "tier_A": sum(1 for n in keep if tier(scored[n][0]) == "A"), "escalated": len(esc),
                      "escalation_reasons": dict(sorted(Counter(r for rs in esc.values() for r in rs).items())),
                      "escalation_rules": ESCALATION_RULES, "escalation_overflow": {r: ns[:40] + ([f"+{len(ns) - 40} more"] if len(ns) > 40 else []) for r, ns in sorted(over.items())},
                      "full_reviews": len(full), "workload_is_gate": False},
           "counts": {"universe": len(recs), "full_reviews": len(full), "swaps": len(swaps), "paired_tests": len(tests),
                      "not_modelable": len(swaps) - len(tests), "verdicts": dict(sorted(vd.items())),
                      "tiers": dict(sorted(Counter(r["tier"] for r in recs).items()))},
           "tournament": tournament_block(D),
           "test_common": test_common(),
           "candidates": recs, "swaps": swaps, "tests": tests}
    return doc


def test_common():
    import grixis_sim as gs, grixis_paired as gp
    return {"simulator": {"name": gs.NAME, "version": gs.VERSION, "model_sha256": gs.model_sha256()}, "samples": SAMPLES, "seed": SEED,
            "turns": gp.TURNS, "prereg": gp.PREREG, "registered": gp.REGISTERED, "limitations": gp.LIMITATIONS_BY_MODEL[gs.VERSION],
            "method": f"paired goldfish, {SAMPLES} games on identical shuffles; the cut takes the add's library position; diff = "
                      "swap - canonical per game; CI95 = mean ± 1.96·sd/√n of the per-game differences; verdict by grixis_paired.verdict (PREREG primary)"}


def tournament_block(D):
    """Tournament evidence applies only when the blueprint's estimated ceiling is bracket 5 (cEDH); filled by 60.3."""
    ce = ((D.bp.get("power") or {}).get("grok_estimated_ceiling") or {}).get("value", {})
    val = ce.get("value") if isinstance(ce, dict) else ce
    p = OUT / "tournament" / f"{D.slug}.json"
    if str(val) != "5":
        return {"applicable": False, "estimated_ceiling": val, "reason": "estimated ceiling below bracket 5 (cEDH): tournament evidence not used (M5 rule)"}
    if p.exists():
        t = json.loads(p.read_text(encoding="utf-8"))
        return {"applicable": True, "estimated_ceiling": val, "ref": f"tournament:{rel(p)}", "status": t.get("status"),
                "sample_size": t.get("sample_size"), "date": t.get("retrieved"), "window": t.get("window")}
    return {"applicable": True, "estimated_ceiling": val, "status": "not_collected", "sample_size": None, "date": None}


def dump(doc):
    head = {k: v for k, v in doc.items() if k not in ("candidates", "swaps", "tests")}
    s = json.dumps(head, indent=1, ensure_ascii=False)[:-2]
    for k in ("candidates", "swaps", "tests"):
        rows = ",\n  ".join(json.dumps(r, ensure_ascii=False, separators=(",", ":")) for r in doc[k])
        s += f',\n "{k}": [' + (f"\n  {rows}\n ]" if rows else "]")
    return s + "\n}\n"


def _ctx():
    import evaluate_decklist as ev
    R = ev.Resolver()
    reg = ga.load_json(ga.REGISTRY)
    pool, first = load_pool()
    almost = json.loads(ALMOST.read_text(encoding="utf-8"))
    return R, reg, pool, first, almost


_CTX = None


def _one(slug):
    R, reg, pool, first, almost = _CTX or _ctx()
    did, v = next((d, v) for d, v in ga.summary().items() if v["slug"] == slug)
    doc = build_deck(did, v, R, reg, pool, first, almost)
    (OUT / f"{slug}.json").write_text(dump(doc), encoding="utf-8")
    c = doc["counts"]
    return f"{slug}: universe {c['universe']}, full reviews {c['full_reviews']} (escalated {doc['triage']['escalated']}), swaps {c['swaps']}, tests {c['paired_tests']} {c['verdicts']}"


def build(only=None, jobs=6):
    global _CTX
    OUT.mkdir(parents=True, exist_ok=True)
    _CTX = _ctx()  # loaded once before forking; workers share it copy-on-write
    slugs = sorted(v["slug"] for v in ga.summary().values() if not only or v["slug"] == only)
    if jobs > 1 and len(slugs) > 1:
        import multiprocessing as mp
        with mp.get_context("fork").Pool(jobs) as p:
            for line in p.imap(_one, slugs):
                print(line, flush=True)
    else:
        for s in slugs:
            print(_one(s), flush=True)


CHECK_REBUILD = ("wick-the-whorled-mind", "the-madcap-jester")


def check(verbose=True, rebuild=True):
    p = []
    summ = ga.summary()
    reg = ga.load_json(ga.REGISTRY)
    want = {v["slug"]: (did, v) for did, v in summ.items()}
    files = {f.stem: f for f in OUT.glob("*.json") if f.stem != "spellbook_almost"}
    for s in sorted(set(want) - set(files)):
        p.append(f"{s}: no candidate file (run --build)")
    tot = Counter()
    ctx = None
    for s, f in sorted(files.items()):
        if s not in want:
            p.append(f"{s}: candidate file for an unknown deck")
            continue
        did, v = want[s]
        doc = json.loads(f.read_text(encoding="utf-8"))
        for e in ga.validate_file({k: v2 for k, v2 in doc.items() if k not in ("candidates", "swaps", "tests")} | {"candidates": [], "swaps": [], "tests": []},
                                  "candidate_universe.schema.json"):
            p.append(f"{s}: {e}")
        e = reg["decks"][ga.registry_id(did)]
        if doc["list_hash"] != e["canonical_project_list"]["hash"]:
            p.append(f"{s}: list_hash is not the canonical list hash (stale)")
        au = json.loads((AUDIT / f"{s}.json").read_text(encoding="utf-8"))
        if doc["snapshot"]["audit"] != au["snapshot"]["id"]:
            p.append(f"{s}: built from an older audit (run --build)")
        n = len(doc["candidates"])
        if not UNIVERSE_MIN <= n <= UNIVERSE_MAX:
            p.append(f"{s}: universe size {n} outside [{UNIVERSE_MIN}, {UNIVERSE_MAX}]")
        names = {x["card"] for x in doc["candidates"]}
        lst = {x["card"] for x in au["slots"]}
        if names & lst:
            p.append(f"{s}: candidates already in the list: {sorted(names & lst)[:5]}")
        nf = 0
        for c in doc["candidates"]:
            for x in ga.validate_file(c, "candidate.schema.json"):
                p.append(f"{s}: {c['card']}: {x}")
            p += [f"{s}: {x}" for x in ga.candidate_problems(c)]
            nf += c["full_review"]
            if c["full_review"] and "review" not in c:
                p.append(f"{s}: {c['card']}: full_review without a review")
        if nf < DEFAULT_RANGE[0]:
            p.append(f"{s}: only {nf} full reviews (default range starts at {DEFAULT_RANGE[0]})")
        tids = {t["id"] for t in doc["tests"]}
        for sw in doc["swaps"]:
            for x in ga.validate_file(sw, "swap.schema.json"):
                p.append(f"{s}: {sw['id']}: {x}")
            if sw["state"] != "CHALLENGER" or not sw["exploratory"] or sw["decision"]["verdict"] is not None:
                p.append(f"{s}: {sw['id']}: M5 swaps must stay exploratory CHALLENGER hypotheses with no decision")
            if sw["base_hash"] != e["canonical_project_list"]["hash"]:
                p.append(f"{s}: {sw['id']}: base_hash is not the canonical hash")
            for t in sw["tests"]:
                if t not in tids:
                    p.append(f"{s}: {sw['id']}: test {t} missing")
        reg_ch = {ch.get("hash") for ch in e.get("challengers") or []}
        swap_of = {sw["id"]: sw["result_hash"] for sw in doc["swaps"]}
        flagged = {swap_of.get(c["review"].get("swap")) for c in doc["candidates"] if c.get("review", {}).get("matches_registered_challenger")}
        for t in doc["tests"]:
            for x in ga.validate_file(t, "test.schema.json"):
                p.append(f"{s}: {t['id']}: {x}")
            import grixis_paired as gp
            if t["verdict"] != gp.verdict(t["results"]):
                p.append(f"{s}: {t['id']}: verdict does not follow PREREG")
            if t["challenger_hash"] in reg_ch and t["challenger_hash"] not in flagged:
                p.append(f"{s}: {t['id']}: matches a registered challenger without `matches_registered_challenger`")
        tot["universe"] += n
        tot["full"] += nf
        tot["escalated"] += doc["triage"]["escalated"]
        tot["swaps"] += len(doc["swaps"])
        tot["tests"] += len(doc["tests"])
        if rebuild and (ROOT / ".cache").exists() and s in CHECK_REBUILD:
            ctx = ctx or _ctx()
            R, reg2, pool, first, almost = ctx
            if dump(build_deck(did, v, R, reg2, pool, first, almost)) != f.read_text(encoding="utf-8"):
                p.append(f"{s}: rebuild does not reproduce the stored candidate file")
    if verbose:
        print(f"candidates: {len(files)} deck(s); universe {tot['universe']}, full reviews {tot['full']} (escalated {tot['escalated']}), "
              f"swaps {tot['swaps']}, paired tests {tot['tests']}; {len(p)} problem(s)")
        for x in p[:30]:
            print("  -", x)
    return p


def summary():
    tot, vd, rs, cl = Counter(), Counter(), Counter(), Counter()
    for f in sorted(OUT.glob("*.json")):
        if f.stem == "spellbook_almost":
            continue
        d = json.loads(f.read_text(encoding="utf-8"))
        tot["decks"] += 1
        for k, v in d["counts"].items():
            if isinstance(v, int):
                tot[k] += v
        vd.update(d["counts"]["verdicts"])
        rs.update(d["triage"]["escalation_reasons"])
        cl.update(s["challenger_class"] for s in d["swaps"])
        tot["escalated"] += d["triage"]["escalated"]
    print(dict(tot), dict(vd), dict(rs), dict(cl))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--build", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--summary", action="store_true")
    ap.add_argument("--deck")
    ap.add_argument("--jobs", type=int, default=6)
    a = ap.parse_args()
    if a.build:
        build(a.deck, a.jobs)
    if a.summary:
        summary()
    if a.check:
        sys.exit(1 if check() else 0)


if __name__ == "__main__":
    main()
