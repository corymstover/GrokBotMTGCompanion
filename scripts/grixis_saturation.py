#!/usr/bin/env python3
"""Step A (Bot cycle 65.1): adaptive candidate saturation + per-deck saturation certificate.

Replaces the fixed M5 universe bound (grixis_candidates UNIVERSE_MIN/MAX = 200/500; 61/62 decks sat exactly at 500) with
multi-pass discovery that runs until further passes stop producing materially new candidates (Cory decision D1, t54u).

Passes (fixed order, deterministic):
  source passes   edhrec, spellbook_near_miss, blueprint_package, oracle_text, type_search, rules_interaction, new_card,
                  role_gap, graph_alternative, tutor_target, mana_base, archetype_tech, tournament
  expansion       rounds seeded by the tier-A candidates the previous pass/round found: Oracle keyword + creature-type
                  neighbours, repeated until STOP_N consecutive non-material rounds.
Material pass: adds >= MATERIAL_K new candidates whose screening score >= MATERIAL_SCORE (tier B), or any new escalated
candidate (ESCALATION). Hard exclusions are only: not Commander-legal (project exceptions are handled as in M5),
outside the commanders' colour identity, already in the list, basic land. Screening never excludes: every discovered
legal in-identity card stays in the universe with a tier; the test tier (paired_test vs screen_only) only orders work.
Broad passes (role_gap, graph_alternative, mana_base, archetype_tech) use a recorded relevance predicate to *nominate*;
a card they do not nominate is not excluded, it is simply not yet discovered (listed as a blind spot).

  python3 scripts/grixis_saturation.py --decks wick-the-whorled-mind,the-valeyard   write data/grixis/saturation/<slug>.json(.gz)
  python3 scripts/grixis_saturation.py --check                                        schema + determinism re-run of one deck
"""
import argparse
import gzip
import hashlib
import json
import re
import sys
import time
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import grixis_authority as ga  # noqa: E402
import grixis_candidates as gc  # noqa: E402

VERSION = "2"
OUT = ROOT / "data" / "grixis" / "saturation"
SCHEMA = ROOT / "data" / "grixis" / "schemas" / "saturation_certificate.schema.json"
MATERIAL_K = 3                 # k: new candidates at or above MATERIAL_SCORE that make a pass material
MATERIAL_SCORE = gc.TIER_B     # X: screening score threshold (tier B = 25.0)
STOP_N = 2                     # N: consecutive non-material expansion rounds before stopping
SNAPSHOT_DATE = "2026-10-16"   # development snapshot (Cory D6); later first printings are unreleased
SPECIFIC_FRAC = 0.02           # an Oracle hook label is commander_specific if it matches <= 2% of the eligible pool
ANOMALY_GAP = 30.0             # anomaly: EDHREC part vs structural part disagree by this much
PAIRED_TARGET = 250            # paired-test target per batch (not a cap: overflow is queued, never dropped)
SIGNAL_WEIGHT = 5.0            # queue priority = score + this x number of escalation reasons
ARCHETYPE_MIN_LISTS = 3        # archetype_tech: in >= this many other Grixis canonical lists and shares the deck's hook label
TEST_TIER_RULE = "escalated cards ranked by score + 5 x reasons; the first PAIRED_TARGET are paired_test, the rest escalated_queued (kept, run in later batches); others screen_only. Workload order, never exclusion"
SOURCE_PASSES = ["edhrec", "spellbook_near_miss", "blueprint_package", "oracle_text", "type_search", "rules_interaction",
                 "new_card", "role_gap", "graph_alternative", "tutor_target", "mana_base", "archetype_tech", "tournament"]


def sha_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return "sha256:" + h.hexdigest()


def rel(p):
    return str(Path(p).relative_to(ROOT))


def is_material(n_at_or_above_score, n_escalated):
    return n_at_or_above_score >= MATERIAL_K or n_escalated > 0


def name_index(names):
    idx = {}
    for n in names:
        if len(n) > 4:
            idx.setdefault(n.split()[0], []).append(n)
    return idx


def mentions(blob, idx):
    """Card names that occur in `blob` (first-word index, then exact substring at that position)."""
    out = set()
    for m in re.finditer(r"[A-Z][\w'\-]*,?", blob):
        w = m.group(0)
        for n in list(idx.get(w, [])) + (list(idx.get(w.rstrip(","), [])) if w.endswith(",") else []):
            if blob.startswith(n, m.start()):
                out.add(n)
    return out


def human_blobs(D):
    """Text of human-review / correction / audit-flag records that can mention a card for this deck."""
    bl = []
    br = json.loads((ROOT / "data/grixis/blueprint_reviews.json").read_text())
    bl.append(json.dumps([v for k, v in (br.get("reviews") or br).items() if D.slug in str(k)] if isinstance(br.get("reviews") or br, dict) else
                         [x for x in br.get("reviews", []) if D.slug in json.dumps(x)], ensure_ascii=False))
    m1 = json.loads((ROOT / "data/grixis/m1_corrections.json").read_text())
    bl.append(json.dumps([x for x in m1.get("corrections", []) if D.slug in json.dumps(x) or D.rid in json.dumps(x)], ensure_ascii=False))
    au = json.loads((gc.AUDIT / f"{D.slug}.json").read_text())
    bl.append(json.dumps([au.get("lint")] + [s.get("m1_flags") for s in au.get("slots", []) if s.get("m1_flags")], ensure_ascii=False))
    return "\n".join(bl)


class Run:
    """Every eligible card is screened once (full-pool sweep); source passes attach signals."""

    def __init__(self, D, pool):
        self.D, self.pool = D, pool
        self.excl, self.unreleased = Counter(), []
        self.exc = {n for n, x in (getattr(D, "exc", None) or {}).items() if n in pool and str(x.get("project_authorization_status", "")).startswith("AUTHORIZED")}
        self.elig = {}
        for n, c in sorted(pool.items()):
            if n in D.names:
                self.excl["already_in_list"] += 1
            elif "Basic Land" in gc.tline(c):
                self.excl["basic_land"] += 1
            elif not set(c.get("color_identity", [])) <= D.ci:
                self.excl["outside_colour_identity"] += 1
            elif (c.get("legalities") or {}).get("commander") != "legal" and n not in self.exc:
                self.excl["not_commander_legal"] += 1
                fr = D.first.get(c.get("oracle_id")) or c.get("released_at") or ""
                if fr > SNAPSHOT_DATE:
                    self.unreleased.append({"card": n, "legal_from": fr})
            else:
                self.elig[n] = c
        self.scored = {n: gc.screen(D, n, c, set()) for n, c in self.elig.items()}
        self.sig = {n: set() for n in self.elig}
        self.passes, self.esc_seen = [], set()
        self.hooks = {n: D.ctx.hook(c) for n, c in self.elig.items()}
        lab = Counter(h["label"] for h in self.hooks.values() if h)
        self.spec = {}
        for n, h in self.hooks.items():
            if not h:
                continue
            if lab[h["label"]] <= SPECIFIC_FRAC * len(self.elig):
                self.spec[n] = "commander_specific"
            elif self.scored[n][2].get("package_basis"):
                self.spec[n] = "blueprint_package"
            else:
                self.spec[n] = "generic"

    def run_pass(self, name, names, kind="signal", inputs=None):
        names = sorted(set(names))
        hit, unres, fresh = [], 0, []
        for n in names:
            if n not in self.elig:
                if n not in self.pool:
                    unres += 1
                continue
            hit.append(n)
            if not self.sig[n]:
                fresh.append(n)
            self.sig[n].add(name)
        mat = [n for n in fresh if self.scored[n][0] >= MATERIAL_SCORE]
        newesc = [n for n in hit if n not in self.esc_seen and self.escalation(n)]
        self.esc_seen |= set(newesc)
        material = is_material(len(mat), len(newesc))
        self.passes.append({"index": len(self.passes) + 1, "pass": name, "kind": kind, "nominated": len(names),
                            "eligible_signalled": len(hit), "first_signal": len(fresh), "unresolved_names": unres,
                            "first_signal_at_or_above_score": len(mat), "new_escalated": len(newesc), "material": material,
                            "inputs": inputs or []})
        return fresh, material

    def escalation(self, n):
        D, (sc, parts, f), s = self.D, self.scored[n], self.sig[n]
        r = []
        if gc.tier(sc) == "A":
            r.append("tier_a_score")
        if "graph_alternative_ref" in s:
            r.append("dependency_graph_alternative")
        if f.get("spellbook_infinite"):
            r.append("spellbook_near_miss_completion")
        if f.get("blueprint_candidate_of") or ("blueprint_package" in s and sc >= MATERIAL_SCORE):
            r.append("package_gap")
        if (f.get("first_printed") or "") >= gc.NEW_SINCE and f.get("oracle_hook") and sc >= MATERIAL_SCORE:
            r.append("new_card")
        if self.spec.get(n) == "commander_specific" and n not in D.edh and f.get("packages"):
            r.append("unusual_oracle_interaction")
        e = parts.get("edhrec", 0)
        rest = sc - e - parts.get("rank", 0)
        if (e >= ANOMALY_GAP and rest <= 0) or (rest >= ANOMALY_GAP and e < 0):
            r.append("anomaly_source_disagreement")
        if "human_evidence" in s:
            r.append("human_evidence")
        if "tournament" in s:
            r.append("tournament_evidence")
        return r


def other_lists(reg):
    out = {}
    for e in reg["decks"].values():
        p = ROOT / e["canonical_project_list"]["export"]
        if p.is_file():
            out[e["slug"]] = {re.sub(r"^\d+x?\s+", "", l).split(" [")[0].split(" (")[0].strip() for l in p.read_text().splitlines() if l.strip()}
    return out


def saturate(D, pool, lists, idx):
    R = Run(D, pool)
    legal = sorted(R.elig.items())
    hooks = R.hooks
    R.run_pass("edhrec", D.ev_cands, inputs=[rel(gc.EVID / f"{D.slug}.json")])
    R.run_pass("spellbook_near_miss", list(D.almost), inputs=[rel(gc.ALMOST)])
    members = [n for p in D.bp.get("packages", []) for n in (p.get("cards") or []) + (p.get("candidates") or [])]
    R.run_pass("blueprint_package", members + [n for n, c in legal if R.scored[n][2].get("package_basis", {}) and
                                               "type" in R.scored[n][2]["package_basis"].values()],
               inputs=[rel(D.bpf) + "#packages (members not in list, candidates, package-type matches)"])
    R.run_pass("oracle_text", [n for n, _ in legal if R.spec.get(n) in ("commander_specific", "blueprint_package")],
               inputs=["oracle_bulk", "grixis_refine.HOOKS (commander_specific and blueprint_package specificity; generic hooks only score)"])
    pkt = set().union(*[x["types"] for x in D.pk.values()]) if D.pk else set()
    R.run_pass("type_search", [n for n, c in legal if gc.subtypes(c) & pkt],
               inputs=["oracle_bulk", rel(D.bpf), "package types: " + ",".join(sorted(pkt))])
    ip = ROOT / "data" / "grixis_interactions" / f"{D.slug}.json"
    kws, named = set(), []
    if ip.is_file():
        it = json.loads(ip.read_text())
        txt = " ".join((x.get("title", "") + " " + x.get("ruling", "")) for x in it.get("interactions", [])).lower()
        allk = {k for _, c in legal for k in (c.get("keywords") or [])}
        kws = {k for k in allk if len(k) > 3 and re.search(r"\b" + re.escape(k.lower()) + r"\b", txt)}
        named = [n for x in it.get("interactions", []) for n in x.get("cards", [])]
    R.run_pass("rules_interaction", named + [n for n, c in legal if set(c.get("keywords") or []) & kws and hooks[n]],
               inputs=[rel(ip)] if ip.is_file() else [])
    R.run_pass("new_card", [n for n, c in legal if (D.first.get(c.get("oracle_id")) or "") >= gc.NEW_SINCE], inputs=["default_bulk (earliest printing)"])
    gaps = [r for r in gc.KEY_ROLES if D.role_count[r] <= sorted(D.role_count[x] for x in gc.KEY_ROLES)[2]]
    R.run_pass("role_gap", [n for n, c in legal if set(gc.roles_of(c)) & set(gaps) and R.scored[n][0] >= MATERIAL_SCORE],
               inputs=[rel(gc.AUDIT / f"{D.slug}.json"), "roles: " + ",".join(gaps)])
    alts = [a.split("#", 1)[1] for s in D.slots.values() for a in s.get("alternatives", []) if a.startswith("evidence:")]
    R.run_pass("graph_alternative_ref", alts, inputs=[rel(gc.AUDIT / f"{D.slug}.json") + "#slots/*/alternatives"])
    weak = [s for s in D.slots.values() if s["disposition"] in gc.CUT_ORDER[:3] and s["zone"] == "main"]
    def sig(c):
        return (tuple(sorted(r for r in gc.roles_of(c) if r != "land")), gc.tline(c).split(" — ")[0].split(" // ")[0])
    wsig = {}
    for s in weak:
        c = D.cards.get(s["card"])
        if c and sig(c)[0]:
            wsig.setdefault(sig(c), []).append(c.get("cmc") or 0)
    R.run_pass("graph_alternative", [n for n, c in legal if sig(c) in wsig and (c.get("cmc") or 0) <= max(wsig[sig(c)])],
               inputs=[rel(gc.GRAPH / f"{D.slug}.json")])
    tt = [t["target"] for t in (D.bp.get("tutor_targets") or [])] if isinstance(D.bp.get("tutor_targets"), list) else []
    tsig = {sig(pool[t]) for t in tt if t in pool}
    R.run_pass("tutor_target", tt + [n for n, c in legal if sig(c) in tsig], inputs=[rel(D.bpf) + "#tutor_targets"])
    def mana_ok(c):
        if gc.is_land(c):
            return bool(set(c.get("produced_mana") or []) & D.ci)
        return "ramp" in gc.roles_of(c) and "Artifact" in gc.tline(c)
    R.run_pass("mana_base", [n for n, c in legal if mana_ok(c)], inputs=["oracle_bulk produced_mana"])
    cnt = Counter(n for s, L in lists.items() if s != D.slug for n in L)
    R.run_pass("archetype_tech", [n for n, _ in legal if cnt[n] >= ARCHETYPE_MIN_LISTS],
               inputs=[f"exports/grixis-archidekt (other canonical lists, >= {ARCHETYPE_MIN_LISTS})"])
    tour = D.tour or {}
    tc = [n for n, x in (tour.get("cards") or {}).items() if (x.get("withCard") or {}).get("entries", 0) > 0]
    R.run_pass("tournament", tc, inputs=[rel(gc.OUT / "tournament" / f"{D.slug}.json")] if D.tour else ["none: no tournament evidence file for this deck"])
    R.run_pass("human_evidence", mentions(human_blobs(D), idx),
               inputs=["data/grixis/blueprint_reviews.json", "data/grixis/m1_corrections.json", rel(gc.AUDIT / f"{D.slug}.json") + "#lint,m1_flags"])
    frontier = sorted(n for n in R.elig if R.sig[n] and R.scored[n][0] >= gc.TIER_A)
    seen_seed, quiet, rnd = set(), 0, 0
    while quiet < STOP_N:
        rnd += 1
        seeds = [n for n in frontier if n not in seen_seed]
        seen_seed |= set(seeds)
        kw = {k for n in seeds for k in (pool[n].get("keywords") or [])}
        st = {t for n in seeds for t in gc.subtypes(pool[n])}
        noms = [n for n, c in legal if ((set(c.get("keywords") or []) & kw) or (gc.subtypes(c) & st))] if seeds else []
        new, material = R.run_pass(f"expansion_{rnd}", noms, kind="expansion", inputs=[f"{len(seeds)} tier-A seeds"])
        frontier = sorted(n for n in new if R.scored[n][0] >= gc.TIER_A)
        quiet = 0 if material else quiet + 1
    # mandatory final full-pool sweep: every eligible card enters the universe
    R.sweep = sum(1 for n in R.elig if not R.sig[n])
    R.passes.append({"index": len(R.passes) + 1, "pass": "full_pool_sweep", "kind": "sweep", "nominated": len(R.elig),
                     "eligible_signalled": len(R.elig), "first_signal": 0, "unresolved_names": 0, "first_signal_at_or_above_score": 0,
                     "new_escalated": 0, "material": False, "added_without_signal": R.sweep,
                     "inputs": ["oracle_bulk: every card Commander-legal (or authorized project exception), in colour identity, not in the list"]})
    return R


def certificate(D, R, inputs, runtime):
    uni = []
    for n in sorted(R.elig, key=lambda n: (-R.scored[n][0], n)):
        sc, parts, f = R.scored[n]
        esc = R.escalation(n)
        uni.append({"card": n, "score": sc, "tier": gc.tier(sc), "signals": sorted(R.sig[n]) or ["full_pool_sweep"],
                    "oracle_hook_specificity": R.spec.get(n), "escalation": esc})
    escd = sorted((x for x in uni if x["escalation"]), key=lambda x: (-(x["score"] + SIGNAL_WEIGHT * len(x["escalation"])), x["card"]))
    for i, x in enumerate(escd):
        x["priority"] = i + 1
        x["test_tier"] = "paired_test" if i < PAIRED_TARGET else "escalated_queued"
    for x in uni:
        x.setdefault("test_tier", "screen_only")
    body = json.dumps(uni, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode()
    gz = gzip.compress(body, compresslevel=9, mtime=0)
    sig_passes = [p for p in R.passes if p["kind"] != "sweep"]
    last_mat = max((p["index"] for p in sig_passes if p["material"]), default=None)
    per_sig = Counter(s for x in uni for s in x["signals"])
    queue = [{"card": x["card"], "priority": x["priority"], "score": x["score"], "escalation": x["escalation"]}
             for x in escd if x["test_tier"] == "escalated_queued"]
    cert = {
        "schema_version": 2, "kind": "saturation_certificate", "generated_by": f"scripts/grixis_saturation.py v{VERSION}",
        "cycle": "Bot cycle 65.2", "deck_id": D.rid, "slug": D.slug, "list_hash": D.e["canonical_project_list"]["hash"],
        "snapshot": {"id": "snap-20261016 (development snapshot, Cory D6)", "inputs": inputs},
        "evidence_class": "derived_metric",
        "authority": {"exploratory": True, "can_decide": False, "note": "Discovery coverage evidence only; screening tiers order work and never exclude or decide. M5 stays unaccepted (Cory)."},
        "stopping_rule": {"material_k": MATERIAL_K, "material_score": MATERIAL_SCORE, "stop_after_non_material": STOP_N,
                          "definition": f"a signal pass is material if it gives a first signal to >= {MATERIAL_K} eligible cards with screening score >= {MATERIAL_SCORE}, or newly escalates any card; expansion stops after {STOP_N} consecutive non-material rounds; the full-pool sweep then admits every eligible card",
                          "test_tier_rule": TEST_TIER_RULE},
        "pool": {"oracle_cards": len(R.pool), "eligible": len(R.elig), "sweep_coverage": 1.0 if len(uni) == len(R.elig) else len(uni) / max(1, len(R.elig)),
                 "added_by_sweep_without_signal": R.sweep, "project_exceptions_admitted": sorted(R.exc & set(R.elig))},
        "passes": R.passes, "last_material_pass": last_mat,
        "saturated": bool(sig_passes) and sig_passes[-1]["kind"] == "expansion" and not sig_passes[-1]["material"] and len(uni) == len(R.elig),
        "hard_exclusions": dict(sorted(R.excl.items())),
        "hard_exclusion_kinds": ["not_commander_legal", "outside_colour_identity", "already_in_list", "basic_land", "unresolved_name"],
        "universe": {"size": len(uni), "previous_m5_bound": 500, "by_tier": dict(sorted(Counter(x["tier"] for x in uni).items())),
                     "by_test_tier": dict(sorted(Counter(x["test_tier"] for x in uni).items())), "per_signal": dict(sorted(per_sig.items())),
                     "escalated": len(escd), "by_escalation_reason": dict(sorted(Counter(r for x in escd for r in x["escalation"]).items())),
                     "oracle_hook_specificity": dict(sorted(Counter(v for v in R.spec.values()).items())),
                     "paired_test_target": PAIRED_TARGET, "file": rel(OUT / f"{D.slug}.universe.json.gz"),
                     "sha256": "sha256:" + hashlib.sha256(body).hexdigest()},
        "escalated_untested_queue": queue,
        "blind_spots": [
            {"kind": "unreleased_not_yet_legal", "note": "Excluded from candidates until legal; picked up at the Birthday snapshot.",
             "cards": sorted(R.unreleased, key=lambda x: (x["legal_from"], x["card"]))},
            {"kind": "spellbook_snapshot", "note": "Commander Spellbook near-misses come from the cached almostIncluded snapshot (one missing piece only)."},
            {"kind": "edhrec_pages", "note": "EDHREC rows exist only for the commander page(s) in the evidence layer; partner/background pages may be thin."},
            {"kind": "tournament", "note": "Tournament evidence exists only for cEDH-ceiling decks and is sparse; an empty tournament pass is recorded, not an error."},
            {"kind": "screening_model", "note": "Sweep-only cards are scored by the M5 screening function; a card whose value it does not model can sit low in tier C (still in the universe)."}],
        "runtime_seconds": None,
    }
    return cert, gz, round(runtime, 1)


_G = {}


def _one(slug):
    g = _G
    t0 = time.time()
    did, v = next((k, v) for k, v in g["summary"].items() if v["slug"] == slug)
    D = gc.DeckCtx(did, v, g["R0"], g["reg"], g["pool"], g["first"], g["almost"])
    R = saturate(D, g["pool"], g["lists"], g["idx"])
    ins = dict(g["inputs"], blueprint=sha_file(D.bpf), evidence=sha_file(gc.EVID / f"{slug}.json"), audit=sha_file(gc.AUDIT / f"{slug}.json"))
    cert, gz, rt = certificate(D, R, ins, time.time() - t0)
    (OUT / f"{slug}.universe.json.gz").write_bytes(gz)
    (OUT / f"{slug}.json").write_text(json.dumps(cert, indent=1, ensure_ascii=False) + "\n")
    u = cert["universe"]
    print(slug, u["size"], "eligible;", len(R.passes), "passes; last material", cert["last_material_pass"], u["by_tier"], u["by_test_tier"], f"{rt}s", flush=True)
    return slug, u["size"], u["by_tier"], u["by_test_tier"], u["escalated"], cert["last_material_pass"], rt


def build(slugs, jobs=1):
    R0, reg, pool, first, almost = gc._ctx()
    o, d = gc.bulk_files()
    _G.update(R0=R0, reg=reg, pool=pool, first=first, almost=almost, lists=other_lists(reg), idx=name_index(pool),
              summary=ga.summary(), inputs={"oracle_bulk": o.name, "default_bulk": d.name, "spellbook_almost": sha_file(gc.ALMOST)})
    OUT.mkdir(parents=True, exist_ok=True)
    if jobs > 1:
        import multiprocessing as mp
        with mp.get_context("fork").Pool(jobs) as P:
            return P.map(_one, slugs, chunksize=1)
    return [_one(s) for s in slugs]


def problems(slugs=None, rerun=True):
    import jsonschema
    v = jsonschema.Draft202012Validator(json.loads(SCHEMA.read_text()))
    p = []
    files = sorted(OUT.glob("*.json"))
    for f in files:
        c = json.loads(f.read_text())
        p += [f"{f.name}: {e.message}" for e in v.iter_errors(c)]
        u = OUT / f"{c['slug']}.universe.json.gz"
        if not u.is_file() or "sha256:" + hashlib.sha256(gzip.decompress(u.read_bytes())).hexdigest() != c["universe"]["sha256"]:
            p.append(f"{f.name}: universe file missing or hash mismatch")
        if not c["saturated"]:
            p.append(f"{f.name}: stopping rule not reached")
    if rerun and files:
        slug = json.loads(files[0].read_text())["slug"]
        before = (OUT / f"{slug}.json").read_bytes(), (OUT / f"{slug}.universe.json.gz").read_bytes()
        build([slug])
        after = (OUT / f"{slug}.json").read_bytes(), (OUT / f"{slug}.universe.json.gz").read_bytes()
        if before != after:
            p.append(f"{slug}: rebuild is not byte-identical")
            (OUT / f"{slug}.json").write_bytes(before[0]); (OUT / f"{slug}.universe.json.gz").write_bytes(before[1])
    return p


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--decks")
    a.add_argument("--all", action="store_true")
    a.add_argument("--jobs", type=int, default=1)
    a.add_argument("--check", action="store_true")
    a.add_argument("--no-rerun", action="store_true")
    x = a.parse_args()
    if x.all:
        build(sorted(v["slug"] for v in ga.summary().values()), x.jobs)
    elif x.decks:
        build(x.decks.split(","), x.jobs)
    if x.check:
        p = problems(rerun=not x.no_rerun)
        for e in p:
            print("FAIL", e)
        print(f"saturation: {len(list(OUT.glob('*.json')))} certificates, {len(p)} problems")
        sys.exit(1 if p else 0)


if __name__ == "__main__":
    main()
