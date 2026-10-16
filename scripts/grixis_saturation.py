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

VERSION = "1"
OUT = ROOT / "data" / "grixis" / "saturation"
SCHEMA = ROOT / "data" / "grixis" / "schemas" / "saturation_certificate.schema.json"
MATERIAL_K = 3                 # k: new candidates at or above MATERIAL_SCORE that make a pass material
MATERIAL_SCORE = gc.TIER_B     # X: screening score threshold (tier B = 25.0)
STOP_N = 2                     # N: consecutive non-material expansion rounds before stopping
RELEVANCE_RANK = 8000          # broad-pass nomination: EDHREC overall rank <= this, or an Oracle hook, or a package type
ARCHETYPE_MIN_LISTS = 3        # archetype_tech: in >= this many other Grixis canonical lists and shares the deck's hook label
TEST_TIER_RULE = "paired_test if screening tier A or escalated; otherwise screen_only (workload order, never exclusion)"
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


def escalation(D, n, c, f, srcs):
    r = []
    if f.get("spellbook_infinite"):
        r.append("dependency_evidence")
    if f.get("blueprint_candidate_of"):
        r.append("package_gap")
    if (f.get("first_printed") or "") >= gc.NEW_SINCE and (f.get("oracle_hook") or f.get("packages")):
        r.append("new_card")
    if f.get("oracle_hook") and n not in D.edh and f.get("packages") and \
            (f.get("scarce_roles") or f.get("blueprint_candidate_of") or f.get("spellbook")):
        r.append("unusual_oracle_interaction")  # hook outside EDHREC that also meets a package and a role/blueprint/combo need
    if "tournament" in srcs:
        r.append("tournament_evidence")
    return r


class Run:
    def __init__(self, D, pool):
        self.D, self.pool = D, pool
        self.cand, self.scored, self.passes = {}, {}, []
        self.excl = Counter()

    def ok(self, n):
        c = self.pool.get(n)
        if c is None:
            self.excl["unresolved_name"] += 1
            return None
        if n in self.D.names:
            self.excl["already_in_list"] += 1
            return None
        if "Basic Land" in gc.tline(c):
            self.excl["basic_land"] += 1
            return None
        if not set(c.get("color_identity", [])) <= self.D.ci:
            self.excl["outside_colour_identity"] += 1
            return None
        if (c.get("legalities") or {}).get("commander") != "legal":
            self.excl["not_commander_legal"] += 1
            return None
        return c

    def run_pass(self, name, names, kind="source", inputs=None):
        new, dup = [], 0
        for n in sorted(set(names)):
            c = self.ok(n)
            if c is None:
                continue
            if n in self.cand:
                self.cand[n].add(name)
                dup += 1
                continue
            self.cand[n] = {name}
            new.append(n)
        for n in new:
            self.scored[n] = gc.screen(self.D, n, self.pool[n], self.cand[n])
        mat_hits = [n for n in new if self.scored[n][0] >= MATERIAL_SCORE]
        esc = [n for n in new if escalation(self.D, n, self.pool[n], self.scored[n][2], self.cand[n])]
        material = is_material(len(mat_hits), len(esc))
        self.passes.append({"index": len(self.passes) + 1, "pass": name, "kind": kind, "nominated": len(set(names)),
                            "new": len(new), "duplicates": dup, "new_at_or_above_score": len(mat_hits),
                            "new_escalated": len(esc), "material": material, "inputs": inputs or []})
        return new, material


def other_lists(reg):
    out = {}
    for e in reg["decks"].values():
        p = ROOT / e["canonical_project_list"]["export"]
        if p.is_file():
            out[e["slug"]] = {re.sub(r"^\d+x?\s+", "", l).split(" [")[0].split(" (")[0].strip() for l in p.read_text().splitlines() if l.strip()}
    return out


def saturate(D, pool, lists):
    R = Run(D, pool)
    edh_ref = rel(gc.EVID / f"{D.slug}.json")
    R.run_pass("edhrec", D.ev_cands, inputs=[edh_ref])
    R.run_pass("spellbook_near_miss", list(D.almost), inputs=[rel(gc.ALMOST)])
    R.run_pass("blueprint_package", [n for x in D.pk.values() for n in x["candidates"]], inputs=[rel(D.bpf)])
    legal = [(n, c) for n, c in sorted(pool.items()) if set(c.get("color_identity", [])) <= D.ci
             and (c.get("legalities") or {}).get("commander") == "legal" and n not in D.names]
    hooks = {n: D.ctx.hook(c) for n, c in legal}
    R.run_pass("oracle_text", [n for n, _ in legal if hooks[n]], inputs=["oracle_bulk", "grixis_refine.HOOKS"])
    pkt = set().union(*[x["types"] for x in D.pk.values()]) if D.pk else set()
    R.run_pass("type_search", [n for n, c in legal if gc.subtypes(c) & pkt], inputs=["oracle_bulk", rel(D.bpf)])
    ip = ROOT / "data" / "grixis_interactions" / f"{D.slug}.json"
    kws = set()
    if ip.is_file():
        it = json.loads(ip.read_text())
        txt = " ".join((x.get("title", "") + " " + x.get("ruling", "")) for x in it.get("interactions", [])).lower()
        allk = {k for _, c in legal for k in (c.get("keywords") or [])}
        kws = {k for k in allk if len(k) > 3 and re.search(r"\b" + re.escape(k.lower()) + r"\b", txt)}
        named = [n for x in it.get("interactions", []) for n in x.get("cards", [])]
    else:
        named = []
    R.run_pass("rules_interaction", named + [n for n, c in legal if set(c.get("keywords") or []) & kws and (hooks[n] or (c.get("edhrec_rank") or 10**9) <= RELEVANCE_RANK)],
               inputs=[rel(ip)] if ip.is_file() else [])
    R.run_pass("new_card", [n for n, c in legal if (D.first.get(c.get("oracle_id")) or "") >= gc.NEW_SINCE], inputs=["default_bulk (earliest printing)"])
    rel_ok = lambda n, c: (c.get("edhrec_rank") or 10 ** 9) <= RELEVANCE_RANK or hooks.get(n) or (gc.subtypes(c) & pkt)
    need = sorted(D.role_count, key=lambda r: (D.role_count[r], r))
    gaps = [r for r in gc.KEY_ROLES if D.role_count[r] <= sorted(D.role_count[x] for x in gc.KEY_ROLES)[2]]
    R.run_pass("role_gap", [n for n, c in legal if set(gc.roles_of(c)) & set(gaps) and rel_ok(n, c)], inputs=[rel(gc.AUDIT / f"{D.slug}.json")])
    alts = [a.split("#", 1)[1] for s in D.slots.values() for a in s.get("alternatives", []) if a.startswith("evidence:")]
    weak = [s for s in D.slots.values() if s["disposition"] in gc.CUT_ORDER[:3] and s["zone"] == "main"]
    def sig(c):
        return (tuple(sorted(r for r in gc.roles_of(c) if r != "land")), gc.tline(c).split(" — ")[0].split(" // ")[0])
    wsig = {}
    for s in weak:
        c = D.cards.get(s["card"])
        if c and sig(c)[0]:
            wsig.setdefault(sig(c), []).append(c.get("cmc") or 0)
    R.run_pass("graph_alternative", alts + [n for n, c in legal if sig(c) in wsig and (c.get("cmc") or 0) <= max(wsig[sig(c)]) and rel_ok(n, c)],
               inputs=[rel(gc.AUDIT / f"{D.slug}.json"), rel(gc.GRAPH / f"{D.slug}.json")])
    tt = [t["target"] for t in (D.bp.get("tutor_targets") or [])] if isinstance(D.bp.get("tutor_targets"), list) else []
    tsig = {sig(pool[t]) for t in tt if t in pool}
    R.run_pass("tutor_target", tt + [n for n, c in legal if sig(c) in tsig and rel_ok(n, c)], inputs=[rel(D.bpf)])
    def mana_ok(c):
        if gc.is_land(c):
            prod = set(c.get("produced_mana") or [])
            return bool(prod & D.ci)
        return "ramp" in gc.roles_of(c) and "Artifact" in gc.tline(c)
    R.run_pass("mana_base", [n for n, c in legal if mana_ok(c) and rel_ok(n, c)], inputs=["oracle_bulk produced_mana"])
    mine = D.ctx.hook
    cnt = Counter(n for s, L in lists.items() if s != D.slug for n in L)
    R.run_pass("archetype_tech", [n for n, c in legal if cnt[n] >= ARCHETYPE_MIN_LISTS and (hooks[n] or gc.subtypes(c) & pkt)],
               inputs=["exports/grixis-archidekt/*.txt (other canonical lists)"])
    tour = D.tour or {}
    tc = [n for n, x in (tour.get("cards") or {}).items() if (x.get("withCard") or {}).get("entries", 0) > 0]
    R.run_pass("tournament", tc, inputs=[rel(gc.OUT / "tournament" / f"{D.slug}.json")] if D.tour else [])
    # expansion rounds from tier-A frontier
    frontier = sorted(n for n in R.cand if R.scored[n][0] >= gc.TIER_A)
    seen_seed, quiet, rnd = set(), 0, 0
    while quiet < STOP_N:
        rnd += 1
        seeds = [n for n in frontier if n not in seen_seed]
        seen_seed |= set(seeds)
        kw = {k for n in seeds for k in (pool[n].get("keywords") or [])}
        st = {t for n in seeds for t in gc.subtypes(pool[n])}
        noms = [n for n, c in legal if ((set(c.get("keywords") or []) & kw) or (gc.subtypes(c) & st)) and rel_ok(n, c)] if seeds else []
        new, material = R.run_pass(f"expansion_{rnd}", noms, kind="expansion", inputs=[f"{len(seeds)} tier-A seeds"])
        frontier = sorted(n for n in new if R.scored[n][0] >= gc.TIER_A)
        quiet = 0 if material else quiet + 1
    return R


def certificate(D, R, inputs, runtime):
    uni = []
    for n in sorted(R.cand, key=lambda n: (-R.scored[n][0], n)):
        sc, parts, f = R.scored[n]
        esc = escalation(D, n, R.pool[n], f, R.cand[n])
        uni.append({"card": n, "score": sc, "tier": gc.tier(sc), "sources": sorted(R.cand[n]), "escalation": esc,
                    "test_tier": "paired_test" if gc.tier(sc) == "A" or esc else "screen_only"})
    body = json.dumps(uni, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode()
    gz = gzip.compress(body, compresslevel=9, mtime=0)
    last_mat = max((p["index"] for p in R.passes if p["material"]), default=None)
    per_src = Counter(s for x in uni for s in x["sources"])
    cert = {
        "schema_version": 1, "kind": "saturation_certificate", "generated_by": f"scripts/grixis_saturation.py v{VERSION}",
        "cycle": "Bot cycle 65.1", "deck_id": D.rid, "slug": D.slug, "list_hash": D.e["canonical_project_list"]["hash"],
        "snapshot": {"id": "snap-20261016 (development snapshot, Cory D6)", "inputs": inputs},
        "evidence_class": "derived_metric",
        "authority": {"exploratory": True, "can_decide": False, "note": "Discovery coverage evidence only; screening tiers order work and never exclude or decide. M5 stays unaccepted (Cory)."},
        "stopping_rule": {"material_k": MATERIAL_K, "material_score": MATERIAL_SCORE, "stop_after_non_material": STOP_N,
                          "definition": f"a pass is material if it adds >= {MATERIAL_K} new candidates with screening score >= {MATERIAL_SCORE} or any new escalated candidate; expansion stops after {STOP_N} consecutive non-material rounds",
                          "relevance_predicate": f"broad passes nominate cards with EDHREC rank <= {RELEVANCE_RANK}, an Oracle hook or a package creature type",
                          "test_tier_rule": TEST_TIER_RULE},
        "passes": R.passes, "last_material_pass": last_mat, "saturated": R.passes[-1]["kind"] == "expansion" and not R.passes[-1]["material"],
        "hard_exclusions": dict(sorted(R.excl.items())),
        "hard_exclusion_kinds": ["not_commander_legal", "outside_colour_identity", "already_in_list", "basic_land", "unresolved_name"],
        "universe": {"size": len(uni), "previous_m5_bound": 500, "by_tier": dict(sorted(Counter(x["tier"] for x in uni).items())),
                     "by_test_tier": dict(sorted(Counter(x["test_tier"] for x in uni).items())), "per_source": dict(sorted(per_src.items())),
                     "escalated": sum(1 for x in uni if x["escalation"]), "file": rel(OUT / f"{D.slug}.universe.json.gz"),
                     "sha256": "sha256:" + hashlib.sha256(body).hexdigest()},
        "blind_spots": [
            "Cards no pass nominates (outside every source, below the relevance predicate) are undiscovered, not excluded.",
            "Commander Spellbook near-misses come from the cached almostIncluded snapshot (one missing piece only).",
            "EDHREC rows exist only for the commander page(s) in the evidence layer; partner/background pages may be thin.",
            "Tournament evidence exists only for cEDH-ceiling decks and is sparse.",
            "Oracle hooks use grixis_refine HOOKS regexes; mechanics they do not name are found only via type, keyword or role passes.",
            "Not-yet-legal cards (pending release) are hard-excluded until legal; they are re-discovered at the Birthday snapshot."],
        "runtime_seconds": None,
    }
    return cert, gz, round(runtime, 1)


def build(slugs):
    R0, reg, pool, first, almost = gc._ctx()
    o, d = gc.bulk_files()
    inputs = {"oracle_bulk": o.name, "default_bulk": d.name, "spellbook_almost": sha_file(gc.ALMOST)}
    lists = other_lists(reg)
    OUT.mkdir(parents=True, exist_ok=True)
    rep = []
    for slug in slugs:
        t0 = time.time()
        did, v = next((k, v) for k, v in ga.summary().items() if v["slug"] == slug)
        D = gc.DeckCtx(did, v, R0, reg, pool, first, almost)
        R = saturate(D, pool, lists)
        ins = dict(inputs, blueprint=sha_file(D.bpf), evidence=sha_file(gc.EVID / f"{slug}.json"), audit=sha_file(gc.AUDIT / f"{slug}.json"))
        cert, gz, rt = certificate(D, R, ins, time.time() - t0)
        (OUT / f"{slug}.universe.json.gz").write_bytes(gz)
        (OUT / f"{slug}.json").write_text(json.dumps(cert, indent=1, ensure_ascii=False) + "\n")
        rep.append((slug, cert["universe"]["size"], len(R.passes), cert["last_material_pass"], cert["universe"]["by_test_tier"], rt))
        print(slug, cert["universe"]["size"], "candidates;", len(R.passes), "passes; last material", cert["last_material_pass"],
              cert["universe"]["by_test_tier"], f"{rt}s", flush=True)
    return rep


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
    a.add_argument("--check", action="store_true")
    a.add_argument("--no-rerun", action="store_true")
    x = a.parse_args()
    if x.decks:
        build(x.decks.split(","))
    if x.check:
        p = problems(rerun=not x.no_rerun)
        for e in p:
            print("FAIL", e)
        print(f"saturation: {len(list(OUT.glob('*.json')))} certificates, {len(p)} problems")
        sys.exit(1 if p else 0)


if __name__ == "__main__":
    main()
