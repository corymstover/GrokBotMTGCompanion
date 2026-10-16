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
Triage: the default review set is the top clamp(#tier A, 15, 40) by screening score; every card meeting an
ESCALATION_RULES reason is escalated and reviewed too, with no cap (Cory constraint 3; Bot cycle 61).
Reviews are `screening_review`s (scripted, heuristic/derived evidence, can_decide false): they triage and can never
satisfy an M6 decision, which needs a human-grade `judgment_review` (grixis_authority.decision_review_problems).
Each review compares the candidate with the blueprint, the role model, the graph and the best incumbent in its role,
and forms a pairwise swap hypothesis: cut = the weakest standard incumbent in that role; core / strong-retain / combo
pieces / project requirements are not immune but must clear the recorded BURDEN_RULES (evidence, compensation of every
graph break, identity), and a cleared one is recorded as a second, labeled hypothesis.  A card the would-be cut
dominates on every recorded axis gets a card-specific `dominated_by` instead of a swap.  Files are <slug>.json.gz
(deterministic gzip; --check compares the decompressed text).  Swaps are
swap.schema.json records, state CHALLENGER, exploratory, decision null: never registered, never promoted, no list
changes.  A paired goldfish test (simulator v1.1, PREREG) runs when the model can see something of either card.

  python3 scripts/grixis_candidates.py --build [--deck SLUG[,SLUG...]] [--jobs N]
  python3 scripts/grixis_candidates.py --check
  python3 scripts/grixis_candidates.py --summary
"""
import argparse, datetime as dt, gzip, hashlib, json, math, pickle, random, re, sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import grixis_authority as ga  # noqa: E402

VERSION = "2"
CYCLE = 61
TODAY = dt.date(2026, 10, 16)
NEW_SINCE = "2026-04-16"            # first printed within 183 days of TODAY = a new card
SATURATION = ROOT / "data" / "grixis" / "saturation"   # step A (Bot cycle 65.3): the universe is the saturated, uncapped pool
SAMPLES, SEED = 300, 60
TIER_A, TIER_B = 45.0, 25.0
OUT = ROOT / "data" / "grixis" / "candidates"
WRITE_DIR = OUT                     # --out DIR redirects writes (scratch smoke runs never overwrite stored M5 files)
ALMOST = OUT / "spellbook_almost.json"
GRAPH, EVID, AUDIT, BPS = (ROOT / "data" / "grixis" / x for x in ("graph", "evidence", "audit", "blueprints"))
CACHE = ROOT / ".cache"
KEY_ROLES = ("ramp", "draw", "removal", "wipe", "counter", "protection", "tutor")
INTERACTION = {"removal", "wipe", "counter", "protection"}
SKIP_LAYOUTS = {"token", "double_faced_token", "art_series", "emblem", "scheme", "planar", "vanguard", "augment", "host"}
CUT_ORDER = ["active_cut_candidate", "flexible", "weak_retain", "package_dependent", "meta_dependent", "functional_retain"]
ELEVATED = {"core", "strong_retain"}   # cuttable only when the recorded higher burden clears (BURDEN_RULES)
REVIEW_KIND = "screening_review"      # scripted; never a judgment_review (M6), never decision-capable
BURDEN_RULES = {
    "levels": {"standard": "an unprotected incumbent (CUT_ORDER) with no Spellbook combo and nothing in breaks_if_removed",
               "elevated": "core or strong_retain, or a Spellbook combo piece, or anything that breaks something per the graph",
               "project_exception": "a registered project requirement (exceptions.json, AUTHORIZED_*): evaluated like elevated and "
                                    "labeled; cutting it would revoke an exception only Cory can revoke"},
    "B1_evidence": f"the add's screening score >= {TIER_A} (tier A) and EDHREC inclusion >= the cut's + 0.05 (or the cut has no row); "
                   "or the add completes an infinite Spellbook variant that does not use the cut",
    "B2_compensation": "every graph break of the cut is compensated: combo:<id> by an interchangeable incumbent (graph "
                       "interchangeable_with) or a variant the add completes; package:<p> by the add fitting <p>; win:<w> by "
                       "an infinite variant the add completes; engine:<e> never by script (judgment needed)",
    "B3_identity": "a blueprint identity_core cut needs an add with the same Oracle hook and a package fit",
    "cleared": "B1 and B2 and (B3 when it applies); the cost (breaks, compensation, uncompensated) is recorded on the swap",
    "never_cut": "a piece of the very combo the add completes (the swap would remove what it adds): recorded, not a protection",
}
AUTHORITY = {"status": "provisional", "exploratory": True,
             "note": "M5 deep dive. Screening scores are heuristics; EDHREC is a derived metric; goldfish tests are model "
                     "evidence, never win rates. No list changes, no challenger registered or promoted, no swap decided "
                     "(constraints 2, 6, 8). Cory decides."}
UNIVERSE_RULES = {
    "mode": "saturation",
    "definition": "Step A (Bot cycle 65.3): the deck's saturated universe from data/grixis/saturation/<slug>.json: every "
                  "Commander-legal card (or authorized project exception) in colour identity, not a basic land, not in the "
                  "canonical list (full-pool sweep, coverage 1.0). No size bound; screening tiers order work and never exclude.",
    "sources": "per-card `sources` are the saturation signals (full_pool_sweep when no signal pass named the card)",
    "full_review_rule": "test_tier paired_test from the saturation certificate (escalated, ranked by score + 5 x reasons, batch "
                        "target 250); escalated_queued cards are kept, listed and reviewed in later batches",
    "excluded": "not Commander-legal (unreleased cards listed with legal_from in the certificate's blind_spots), outside "
                "identity, basic lands, already in the list"}
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
    "cap": "none (Bot cycle 61, constraint 3): every card meeting a reason is escalated and gets a screening review",
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
        self.met = self.g["metrics"]
        self.node = {x["name"]: x for x in self.g["nodes"] if x["kind"] in ("card", "commander")}
        self.exc = {x["card"]: x for x in ga.load_json(ga.EXCEPTIONS)["exceptions"] if x["deck_id"] in (self.rid, did)
                    and x.get("project_authorization_status") in ("AUTHORIZED_EXCEPTION", "AUTHORIZED_FUTURE_RELEASE")}
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
    """The saturated universe (step A). Refuses a certificate built for another list hash."""
    import grixis_saturation as gsat
    cp = SATURATION / f"{D.slug}.json"
    cert = json.loads(cp.read_text(encoding="utf-8"))
    if cert["list_hash"] != D.e["canonical_project_list"]["hash"]:
        raise SystemExit(f"{D.slug}: saturation certificate is for another list hash (run grixis_saturation.py)")
    rows = gsat.load_universe(ROOT / cert["universe"]["file"])
    keep = [x["card"] for x in rows if x["card"] in D.pool]
    cand = {x["card"]: set(x["signals"]) for x in rows}
    sat = {x["card"]: x for x in rows}
    scored = {n: screen(D, n, D.pool[n], cand[n]) for n in keep}
    keep.sort(key=lambda n: (-scored[n][0], n))
    meta = {"considered": cert["pool"]["eligible"], "size": len(keep), "sweep_coverage": cert["pool"]["sweep_coverage"],
            "saturation_certificate": rel(cp), "saturation_sha256": cert["universe"]["sha256"],
            "sources_considered": dict(sorted(cert["universe"]["per_signal"].items())),
            "excluded": dict(sorted(cert["hard_exclusions"].items())),
            "not_legal_watchlist": {"count": len(cert["blind_spots"][0]["cards"]),
                                    "cards": [f"{x['card']} ({x['legal_from']})" for x in cert["blind_spots"][0]["cards"][-10:]]},
            "spellbook_snapshot_matches_list": D.almost_sig_ok}
    return keep, cand, scored, meta, sat


# ---------------------------------------------------------------- triage
def tier(score):
    return "A" if score >= TIER_A else "B" if score >= TIER_B else "C"


def triage(D, keep, sat):
    """Full screening reviews = the certificate's paired_test cards; escalated_queued cards are listed for later batches."""
    esc = {n: sat[n]["escalation"] for n in keep if sat[n]["escalation"]}
    default = [n for n in keep if sat[n]["test_tier"] == "paired_test"]
    queued = [n for n in keep if sat[n]["test_tier"] == "escalated_queued"]
    return default, esc, queued


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


def level_of(D, n, s):
    m = D.met.get(n) or {}
    if s["disposition"] == "project_requirement" or n in D.exc:
        return "project_exception"
    if s["disposition"] in ELEVATED or m.get("combos") or m.get("breaks_if_removed"):
        return "elevated"
    return "standard"


def burden(D, x, n, f, sc, R):
    """The recorded higher burden for cutting an elevated / project-exception incumbent `x` for the add `n`."""
    m = D.met.get(x) or {}
    e_c, e_x = incl(D, n), incl(D, x)
    own_inf = [v["id"] for v in D.almost.get(n, []) if v["infinite"] and x not in v["cards"]]
    b1 = bool(own_inf) or (sc >= TIER_A and (e_x is None or (e_c is not None and e_c >= e_x + 0.05)))
    comp, unc = {}, []
    mates = [y for y in m.get("interchangeable_with", []) if y != x and y in D.slots]
    for br in m.get("breaks_if_removed", []):
        k, _, v = br.partition(":")
        if k == "combo" and mates:
            comp[br] = f"interchangeable incumbent(s) {', '.join(mates[:3])} keep the line"
        elif k == "combo" and own_inf:
            comp[br] = f"the add completes {own_inf[0]}"
        elif k == "package" and (v in f.get("packages", []) and f.get("package_basis", {}).get(v) == "type" or n in (D.pk.get(v) or {}).get("candidates", set())):
            comp[br] = f"the add fits {v}"
        elif k == "win" and own_inf:
            comp[br] = f"new route: the add completes {own_inf[0]}"
        else:
            unc.append(br)
    core = bool((D.node.get(x) or {}).get("identity_core"))
    b3 = None
    if core:
        xc = D.cards.get(x) or R.get(x)[0]
        xh = D.ctx.hook(xc) if xc else None
        b3 = bool(xh and f.get("oracle_hook") == xh["label"] and f.get("packages"))
    cleared = b1 and not unc and (b3 is not False)
    out = {"level": level_of(D, x, D.slots[x]), "tests": {"B1_evidence": b1, "B2_compensation": not unc, **({"B3_identity": b3} if core else {})},
           "breaks": m.get("breaks_if_removed", []), "compensated": comp, "uncompensated": unc,
           "compensating_adds": [n] + mates[:3], "cleared": cleared}
    if out["level"] == "project_exception":
        ex = D.exc.get(x) or {}
        out["note"] = (f"Authorized project exception {ex.get('id', '(audit project_requirement)')}: evaluable, not immune; any cut is a "
                       "project decision only Cory can make (labeled hypothesis).")
    return out


def pick(D, kind, val, completes_with, R, n=None, f=None, sc=0.0):
    """(mates, bench, cut, considered). cut = (name, slot, burden-or-None). Standard incumbents first (weakest by
    CUT_ORDER); elevated and project-exception incumbents are evaluated against BURDEN_RULES and used when no standard
    cut exists and the burden clears."""
    mates = []
    for x, s in sorted(D.slots.items()):
        if s["zone"] != "main":
            continue
        ic = D.cards.get(x) or R.get(x)[0]
        if in_role(D, kind, val, s, ic):
            mates.append((x, s))
    nonbasic = [(x, s) for x, s in mates if not (x in D.cards and "Basic Land" in tline(D.cards[x]))]
    bench = max(nonbasic, key=lambda y: ((incl(D, y[0]) or 0.0), y[0]), default=None)
    std = [(x, s) for x, s in mates if x not in completes_with and level_of(D, x, s) == "standard" and s["disposition"] in CUT_ORDER]
    cut = min(std, key=lambda y: (CUT_ORDER.index(y[1]["disposition"]), incl(D, y[0]) or 0.0, -y[1]["redundancy"], y[0]), default=None)
    cut = (cut[0], cut[1], None) if cut else None
    considered = {"elevated": 0, "project_exception": 0, "cleared": [], "closest": None, "excluded_own_combo": sorted(completes_with & {x for x, _ in mates})}
    if n is not None:
        best = None
        for x, s in mates:
            lv = level_of(D, x, s)
            if lv == "standard" or x in completes_with:
                continue
            considered[lv] += 1
            if lv == "project_exception":
                considered.setdefault("project_exception_cards", []).append(x)
            bd = burden(D, x, n, f, sc, R)
            if bd["cleared"]:
                considered["cleared"].append(x)
                if best is None or (incl(D, x) or 0.0) < (incl(D, best[0]) or 0.0):
                    best = (x, s, bd)
            elif considered["closest"] is None or len(bd["uncompensated"]) + (not bd["tests"]["B1_evidence"]) < considered["closest"][1]:
                considered["closest"] = (x, len(bd["uncompensated"]) + (not bd["tests"]["B1_evidence"]),
                                         [k for k, v in bd["tests"].items() if v is False] + bd["uncompensated"][:3])
        if considered["closest"]:
            x, _, failed = considered["closest"]
            considered["closest"] = {"card": x, "failed": failed}
        alt = None
        if cut is None and best:
            cut = best
        elif best:
            alt = best  # a cleared elevated cut is a second, labeled hypothesis next to the standard one
        return mates, bench, cut, considered, alt
    return mates, bench, cut, considered, None


def full_review(D, n, c, sc, parts, f, R):
    comp_with = set()
    inf = False
    for v in D.almost.get(n, []):
        comp_with |= set(v["cards"]) - {n}
        inf |= v["infinite"]
    kind, val = role_key(D, n, c, f)
    mates, bench, cut, considered, alt = pick(D, kind, val, comp_with, R, n, f, sc)
    if cut is None and kind != "type":  # nothing replaceable in the primary role: fall back to the card type
        kind, val = type_key(c)
        mates, bench, cut, considered, alt = pick(D, kind, val, comp_with, R, n, f, sc)
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
    dom = dominated(D, n, c, f, parts, cut, R) if cut and cut[2] is None else None
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
    if cut and dom:
        lines.append(f"No swap hypothesis: dominated by the would-be cut {cut[0]} ({dom}).")
    elif cut and cut[2]:
        bd = cut[2]
        lines.append(f"Swap hypothesis at the {bd['level'].replace('_', ' ')} burden: cut {cut[0]} ({cut[1]['disposition'].replace('_', ' ')}); "
                     f"breaks {len(bd['breaks'])}, all compensated." + (" " + bd["note"] if bd.get("note") else ""))
    elif cut:
        lines.append(f"Swap hypothesis: cut {cut[0]} ({cut[1]['disposition'].replace('_', ' ')}).")
    if alt:
        lines.append(f"Second hypothesis at the {alt[2]['level'].replace('_', ' ')} burden (cleared): cut {alt[0]} "
                     f"({alt[1]['disposition'].replace('_', ' ')}; breaks {len(alt[2]['breaks'])}, all compensated).")
    else:
        cl = considered.get("closest")
        lines.append(f"No swap hypothesis: no standard cut in role and no elevated cut clears the burden ({considered['elevated']} elevated, "
                     f"{considered['project_exception']} project-exception incumbent(s) evaluated" +
                     (f"; closest {cl['card']}, failed {', '.join(cl['failed'])}" if cl else "") + ").")
    rv = {"kind": REVIEW_KIND, "method": "scripted", "by": f"script:grixis_candidates.py v{VERSION}",
          "evidence_class": "heuristic" if not e else "derived_metric",
          "role": {"kind": kind, "value": val, "incumbents": len(mates), "list_counts": {r: D.role_count[r] for r in f["roles"] if r in KEY_ROLES or r == "land"}},
          "blueprint": {"fit": fit, "named_by": named, "oracle_hook": f.get("oracle_hook"), "packages": f.get("packages", []), "anti_goal": anti},
          "graph": {"completes_spellbook": f.get("spellbook", []), "infinite": inf, "with_incumbents": sorted(comp_with)[:8]},
          "best_incumbent": cmp_, "cut": None if (not cut or dom) else cut[0],
          "cut_level": None if (not cut or dom) else (cut[2]["level"] if cut[2] else "standard"),
          "protected_considered": {k: v for k, v in considered.items() if v not in (0, [], None)},
          **({"dominated_by": {"card": cut[0], "detail": dom}} if dom else {}),
          **({"elevated_alternative": {"card": alt[0], "level": alt[2]["level"]}} if alt else {}), **({"tournament": tour} if tour else {}), "assessment": " ".join(lines),
          "evidence_classes": dict(sorted(Counter(i["class"] for i in items).items())),
          "decision_support": {"evidence_ok": ok, "why_not": why_not, "can_decide": False,
                               "because": "screening_review (scripted heuristic/derived evidence): an M6 decision needs a judgment_review"}}
    return rv, (None if dom else cut), items, alt


def dominated(D, n, c, f, parts, cut, R):
    """Card-specific reason the add cannot improve on the would-be (standard) cut, or None. Never applied to new cards,
    Spellbook links, blueprint-named cards or package fits the cut lacks."""
    x = cut[0]
    xc = D.cards.get(x) or R.get(x)[0]
    if not xc or "new_card" in parts or f.get("spellbook") or f.get("blueprint_candidate_of"):
        return None
    xs = D.slots[x]
    if set(f.get("packages", [])) - set(xs["packages"]):
        return None
    kr = {r for r in f["roles"] if r in KEY_ROLES}
    if not kr <= set(xs["roles"]):
        return None
    if f.get("oracle_hook"):
        body = tline(xc) + "\n" + otext(xc)
        if not any(lab == f["oracle_hook"] and rx.search(body) for lab, _, _, rx in D.ctx.hooks):
            return None
    mv_c, mv_x = int(c.get("cmc") or 0), int(xc.get("cmc") or 0)
    rk_c, rk_x = c.get("edhrec_rank"), xc.get("edhrec_rank")
    if mv_c < mv_x or not rk_x or (rk_c and rk_c <= rk_x) or (incl(D, n) or 0) > (incl(D, x) or 0):
        return None
    return (f"MV {mv_c} vs {mv_x}; EDHREC overall rank {rk_c or 'none'} vs {rk_x}; roles {sorted(kr) or 'none'} within the cut's; "
            + (f"both match hook {f['oracle_hook']}" if f.get("oracle_hook") else "no Oracle hook") + "; no package, Spellbook or blueprint edge the cut lacks")


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
    combos = [co for co in base.combos if cut not in co["cards"]] + [{"id": v["id"], "cards": v["cards"]} for v in D.almost.get(add_c["name"], [])
                                  if set(v["cards"]) - {add_c["name"]} <= ({x["name"] for x in lib} | {x["name"] for x in base.commanders})
                                  and cut not in v["cards"]]
    b = gs.Deck(base.slug, base.commanders, lib, base.key_sets, combos)
    b.ci = base.ci
    b.engine, b.gy_combo = base.engine, base.gy_combo
    res, sw = gp.paired(base, b, SAMPLES, SEED, pairs=[(cut, add_c["name"])], model=gs.VERSION)
    return res, sw, b, sum(1 for co in combos if co not in base.combos)


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


def make_swap(D, n, c, parts, f, rv, cut, items, R, base, base_cm, bd=None):
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
                        + ("without breaking a dependency" if not bd else f"while every graph break of the cut is compensated ({bd['level'].replace('_', ' ')} burden cleared)")
                        + f" (cut is {D.slots[cut]['disposition'].replace('_', ' ')}; add blueprint fit {rv['blueprint']['fit']})."
                        + (" " + bd["note"] if bd and bd.get("note") else ""),
          "expected_benefit": "; ".join(filter(None, [
              f"Oracle hook {f['oracle_hook']}" if f.get("oracle_hook") else "",
              f"completes Spellbook {', '.join(f['spellbook'][:2])}" if f.get("spellbook") else "",
              f"EDHREC inclusion {f['edhrec']['inclusion']:.1%} vs cut {(incl(D, cut) or 0):.1%}" if f.get("edhrec") else "",
              f"roles {', '.join(f['roles'])}" if f["roles"] else ""])) or "unclear (screening only)",
          "expected_cost": (f"breaks {', '.join(bd['breaks'][:4])}" + ("…" if len(bd["breaks"]) > 4 else "") + "; compensated by "
                            + ", ".join(bd["compensating_adds"]) + ". " if bd and bd["breaks"] else "") + f"loses {cut}: " + (D.slots[cut]["reason"][:160]),
          "burden": dict(bd, rules="BURDEN_RULES (this file's swap_rules)") if bd else {"level": "standard", "cleared": True},
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
    keep, cand, scored, meta, sat = build_universe(D)
    default, esc, queued = triage(D, keep, sat)
    full = set(default)
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
                              "note": "triage.escalation_rules" if rs else None},
               "evidence": sorted({f"oracle:{n}"} | ({f"evidence:data/grixis/evidence/{D.slug}.json#{n}"} if f.get("edhrec") else set()) |
                                  {f"spellbook:{x}" for x in f.get("spellbook", [])[:4]}),
               "workload": {"test_tier": sat[n]["test_tier"], "is_gate": False},
               "sources": sorted(cand[n]), "screening": {"score": sc, "parts": parts, "facts": f}}
        if n in full:
            rv, cut, items, alt = full_review(D, n, c, sc, parts, f, R)
            rec["review"] = rv
            if cut:
                sw, test, gold = make_swap(D, n, c, parts, f, rv, cut[0], items, R, base, base_cm, cut[2])
                rec["review"]["swap"] = sw["id"]
                same = {ch.get("hash"): ch.get("id") for ch in D.e.get("challengers") or []}.get(sw["result_hash"])
                if same:  # an independent rediscovery of a registered challenger: noted, never merged into it
                    rec["review"]["matches_registered_challenger"] = same
                rec["review"]["goldfish"] = gold
                swaps.append(sw)
                if test:
                    tests.append(test)
            if alt:
                sw, test, gold = make_swap(D, n, c, parts, f, rv, alt[0], items, R, base, base_cm, alt[2])
                rec["review"]["elevated_alternative"].update({"swap": sw["id"], "goldfish": gold})
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
           "triage": {"default_full_reviews": len(default), "default_rule": UNIVERSE_RULES["full_review_rule"],
                      "escalated_queued": queued,
                      "tier_A": sum(1 for n in keep if tier(scored[n][0]) == "A"), "escalated": len(esc),
                      "escalation_reasons": dict(sorted(Counter(r for rs in esc.values() for r in rs).items())),
                      "escalation_rules": ESCALATION_RULES, "escalation_cap": None,
                      "screening_reviews": len(full), "workload_is_gate": False,
                      "review_kind": REVIEW_KIND, "review_note": REVIEW_NOTE},
           "swap_rules": BURDEN_RULES,
           "project_requirements": proj_block(D, recs),
           "counts": {"universe": len(recs), "screening_reviews": len(full), "judgment_reviews": 0, "swaps": len(swaps), "paired_tests": len(tests),
                      "not_modelable": len(swaps) - len(tests), "verdicts": dict(sorted(vd.items())),
                      "swap_levels": dict(sorted(Counter(sw["burden"]["level"] for sw in swaps).items())),
                      "dominated": sum(1 for r in recs if (r.get("review") or {}).get("dominated_by")),
                      "no_cut": sum(1 for r in recs if r.get("review") and not r["review"]["cut"] and not r["review"].get("dominated_by")),
                      "tiers": dict(sorted(Counter(r["tier"] for r in recs).items()))},
           "tournament": tournament_block(D),
           "test_common": test_common(),
           "candidates": recs, "swaps": swaps, "tests": tests}
    return doc


REVIEW_NOTE = ("Every `review` here is a screening_review: scripted, heuristic/derived evidence, can_decide false. It "
               "triages; it never satisfies an M6 decision requirement, which needs a judgment_review "
               "(grixis_authority.decision_review_problems). This script never writes a judgment_review.")


def proj_block(D, recs):
    """Registered project requirements (e.g. Bjorna's exceptions): authorized, still evaluated, labeled, never silently immune."""
    out = []
    for x, ex in sorted(D.exc.items()):
        ev = sum(1 for r in recs if x in ((r.get("review") or {}).get("protected_considered") or {}).get("project_exception_cards", []))
        cl = sum(1 for r in recs if x in ((r.get("review") or {}).get("protected_considered") or {}).get("cleared", []))
        zone = (D.slots.get(x) or {}).get("zone") or ex.get("zone")
        out.append({"card": x, "exception": ex["id"], "authorization": ex["project_authorization_status"], "zone": zone,
                    "evaluated_in_reviews": ev, "burden_cleared_in": cl,
                    "note": ("Authorized exception, evaluable and not immune: in-role challengers are checked against it at the "
                             "project_exception burden; a cut stays a labeled hypothesis that only Cory can act on."
                             + (" Companion (outside the 100): no main-deck role to compete in; an alternative companion or none "
                                "is a project-level question, recorded here rather than as a swap." if zone == "companion" else ""))})
    return out


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


# Bot cycle 61 (footprint): one gzip per deck, written deterministically (mtime 0, level 9). Reproducibility is checked on
# the decompressed JSON text, so a different zlib build cannot break --check.
def path_of(slug):
    return OUT / f"{slug}.json.gz"


def write_path(slug):
    return WRITE_DIR / f"{slug}.json.gz"


def write_doc(slug, doc):
    WRITE_DIR.mkdir(parents=True, exist_ok=True)
    write_path(slug).write_bytes(gzip.compress(dump(doc).encode("utf-8"), compresslevel=9, mtime=0))


def read_text(path):
    return gzip.decompress(Path(path).read_bytes()).decode("utf-8")


def load(slug):
    return json.loads(read_text(path_of(slug)))


def deck_files():
    return {f.name[:-len(".json.gz")]: f for f in OUT.glob("*.json.gz")}


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
    write_doc(slug, doc)
    c = doc["counts"]
    return f"{slug}: universe {c['universe']}, screening reviews {c['screening_reviews']} (escalated {doc['triage']['escalated']}), swaps {c['swaps']}, tests {c['paired_tests']} {c['verdicts']}"


def build(only=None, jobs=6):
    global _CTX
    OUT.mkdir(parents=True, exist_ok=True)
    _CTX = _ctx()  # loaded once before forking; workers share it copy-on-write
    want = set(only.split(",")) if only else None
    slugs = sorted(v["slug"] for v in ga.summary().values() if not want or v["slug"] in want)
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
    files = deck_files()
    for f in OUT.glob("*.json"):
        if f.stem != "spellbook_almost":
            p.append(f"{f.name}: uncompressed deck file (Bot cycle 61 stores <slug>.json.gz)")
    for s in sorted(set(want) - set(files)):
        p.append(f"{s}: no candidate file (run --build)")
    tot = Counter()
    ctx = None
    for s, f in sorted(files.items()):
        if s not in want:
            p.append(f"{s}: candidate file for an unknown deck")
            continue
        did, v = want[s]
        text = read_text(f)
        doc = json.loads(text)
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
        legacy = doc["universe"].get("mode") != "saturation"
        if legacy:  # capped legacy file (Bot cycle 61): validated against the bound it recorded, superseded at M5 regeneration
            lo, hi = doc["universe"]["bounds"]
            if not lo <= n <= hi:
                p.append(f"{s}: legacy universe size {n} outside its recorded bounds")
        elif n != doc["universe"]["considered"]:
            p.append(f"{s}: saturated universe size {n} != certificate eligible {doc['universe']['considered']}")
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
            r = c.get("review")
            if r and (r["kind"] != REVIEW_KIND or r["method"] != "scripted" or r["decision_support"]["can_decide"] is not False):
                p.append(f"{s}: {c['card']}: a scripted review must be a screening_review that cannot decide")
            if "judgment_review" in c:
                p += [f"{s}: {x}" for x in ga.decision_review_problems(c)]
                if str(c["judgment_review"].get("by", "")).startswith("script"):
                    p.append(f"{s}: {c['card']}: a script wrote a judgment_review")
            elif not ga.decision_review_problems(c):
                p.append(f"{s}: {c['card']}: decision-capable without a judgment_review")
        if legacy and nf < doc["triage"]["default_full_reviews"]:
            p.append(f"{s}: only {nf} screening reviews (< recorded default {doc['triage']['default_full_reviews']})")
        elif not legacy and nf != doc["triage"]["default_full_reviews"]:
            p.append(f"{s}: {nf} screening reviews != the certificate's paired_test count {doc['triage']['default_full_reviews']}")
        if doc["counts"]["judgment_reviews"] != sum(1 for c in doc["candidates"] if "judgment_review" in c):
            p.append(f"{s}: counts.judgment_reviews is wrong")
        byc = {c["card"]: c for c in doc["candidates"]}
        for c in doc["candidates"]:
            r = c.get("review") or {}
            if r.get("swap"):
                sw = next((x for x in doc["swaps"] if x["id"] == r["swap"]), None)
                if not sw or sw["burden"]["level"] != r["cut_level"]:
                    p.append(f"{s}: {c['card']}: cut_level does not match its swap's burden")
        tids = {t["id"] for t in doc["tests"]}
        for sw in doc["swaps"]:
            for x in ga.validate_file(sw, "swap.schema.json"):
                p.append(f"{s}: {sw['id']}: {x}")
            if sw["state"] != "CHALLENGER" or not sw["exploratory"] or sw["decision"]["verdict"] is not None:
                p.append(f"{s}: {sw['id']}: M5 swaps must stay exploratory CHALLENGER hypotheses with no decision")
            if sw["base_hash"] != e["canonical_project_list"]["hash"]:
                p.append(f"{s}: {sw['id']}: base_hash is not the canonical hash")
            b = sw["burden"]
            if b["level"] != "standard" and (not b["cleared"] or b.get("uncompensated")):
                p.append(f"{s}: {sw['id']}: a {b['level']} cut needs a cleared burden with every break compensated")
            if b["level"] == "project_exception" and not b.get("note"):
                p.append(f"{s}: {sw['id']}: a project-exception cut must carry the labeled note")
            p += [f"{s}: {x}" for x in ga.swap_decision_problems(sw, byc)]
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
        if rebuild and not legacy and (ROOT / ".cache").exists() and s in CHECK_REBUILD:
            ctx = ctx or _ctx()
            R, reg2, pool, first, almost = ctx
            if dump(build_deck(did, v, R, reg2, pool, first, almost)) != text:
                p.append(f"{s}: rebuild does not reproduce the stored candidate file")
    if verbose:
        print(f"candidates: {len(files)} deck(s); universe {tot['universe']}, screening reviews {tot['full']} (escalated {tot['escalated']}), "
              f"swaps {tot['swaps']}, paired tests {tot['tests']}; {len(p)} problem(s)")
        for x in p[:30]:
            print("  -", x)
    return p


def summary():
    tot, vd, rs, cl = Counter(), Counter(), Counter(), Counter()
    for slug, f in sorted(deck_files().items()):
        d = json.loads(read_text(f))
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
    ap.add_argument("--out", help="write built files here instead of data/grixis/candidates (scratch smoke runs)")
    a = ap.parse_args()
    global WRITE_DIR
    if a.out:
        WRITE_DIR = Path(a.out)
    elif a.build:
        raise SystemExit("--build without --out would overwrite the stored (capped legacy) M5 files; M5 is regenerated only after steps A-F")
    if a.build:
        build(a.deck, a.jobs)
    if a.summary:
        summary()
    if a.check:
        sys.exit(1 if check() else 0)


if __name__ == "__main__":
    main()
