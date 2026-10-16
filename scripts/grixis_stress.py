#!/usr/bin/env python3
"""M3 scripted stress scenarios (Bot cycle 57.4): deterministic perturbations in the goldfish engine, no win rates.

For each deck and each scenario in grixis_sim.SCENARIOS, the canonical list is played twice on identical seeds and
shuffles: once unperturbed (scenario "none") and once perturbed. Results are paired per-game differences (perturbed -
unperturbed) with CI95s, plus scenario-only measurements (commander recovery turn, the share of games where the event
fired). Nothing here simulates opponents or a win rate: "how much does this deck's own development and combo assembly
suffer, and how fast does it recover" is the only question.

Pre-registered (STRESS_PREREG, written in Bot cycle 57.4 before any stress run): a primary metric and a threshold per
scenario. Verdict (on the primary; a drop is a negative difference):
  no_detectable_difference  CI95 contains 0
  pass                      a detectable drop whose CI95 lower bound stays above -threshold (bounded below the threshold)
  fail                      a drop of at least the threshold with CI95 upper bound < 0
  inconclusive              anything else (the CI straddles -threshold, or a detectable gain)
Records: data/grixis/stress/<slug>.json, each valid against test.schema.json (kind stress_scenario).

Usage:
  python3 scripts/grixis_stress.py --build [--samples 500] [--seed 57] [--decks a,b] [--jobs 8]
  python3 scripts/grixis_stress.py --check          # schema, coverage, version, verdict rule, exact re-run of 2 decks
  python3 scripts/grixis_stress.py --summary
"""
import argparse
import hashlib
import json
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import grixis_authority as ga  # noqa: E402
import grixis_sim as gs  # noqa: E402

OUT = ROOT / "data" / "grixis" / "stress"
REGISTERED = "2026-10-16 (Bot cycle 57.4, before any stress run)"
CHECK_DECKS = ("abaddon-the-despoiler", "wick-the-whorled-mind")
TURNS = 10
STRESS_PREREG = {
    "commander_removed_once": ("commander_bf_turns", 1.0),
    "commander_removed_twice": ("commander_bf_turns", 1.0),
    "board_wipe": ("mana_available_t8", 0.5),
    "artifacts_wiped": ("mana_available_t8", 0.5),
    "mana_screw": ("commander_cast_by_t6", 0.05),
    "color_screw": ("commander_cast_by_t6", 0.05),
    "first_key_spell_countered": ("assembly_or_spent", None),
    "key_engine_exiled": ("assembly_or_spent", None),
    "graveyard_exiled": ("assembly_or_spent", None),
}
ASSEMBLY = ("win_turn_proxy_by_t8", 0.02)   # decks with Spellbook combos
SPENT = ("mana_spent_t1_t8", 0.5)           # decks without
# v1.0 stress records (Bot cycle 57.4, PR #132) stay in git history; the stress set is rebuilt at the current model.
LIMITATIONS = [
    "Goldfish stress test: one player, scripted perturbations, no opponents; never a win rate.",
] + gs.MODEL_NOTES[gs.VERSION] + [
    "The graveyard holds only what the model puts there (cast instants/sorceries, countered, destroyed, discarded or "
    "wheeled-away cards, Mox Diamond lands); self-mill and recursion are not modelled, so graveyard_exiled mostly "
    "measures nothing in this model.",
    "A graveyard piece counts toward a combo only when some piece of that combo mentions a graveyard in its Oracle text (recursion assumed, not simulated).",
]


def primary_for(kind, deck):
    m, th = STRESS_PREREG[kind]
    if m == "assembly_or_spent":
        return ASSEMBLY if deck.combos else SPENT
    return m, th


def metrics(r, deck):
    m = {"commander_bf_turns": float(sum(r["cmd_bf"])),
         "mana_available_t8": float(r["mana"][7]),
         "commander_cast_by_t4": 1.0 if r["commander_turn"] is not None and r["commander_turn"] <= 4 else 0.0,
         "commander_cast_by_t6": 1.0 if r["commander_turn"] is not None and r["commander_turn"] <= 6 else 0.0,
         "win_turn_proxy_by_t8": 1.0 if r["win_turn_proxy"] is not None and r["win_turn_proxy"] <= 8 else 0.0,
         "combo_assembled_by_t8": 1.0 if r["combo_turn"] is not None and r["combo_turn"] <= 8 else 0.0,
         "mana_spent_t1_t8": float(sum(r["spent"][:8]))}
    return m


def run_pair(deck, kind, samples, seed):
    base, pert = [], []
    for i in range(samples):
        s = gs.seed_for(seed, i)
        perm = random.Random(s ^ 0x5EED).sample(range(deck.N), deck.N)
        base.append(gs.play_game(deck, random.Random(s), TURNS, perm=perm, scenario={"kind": "none"}))
        pert.append(gs.play_game(deck, random.Random(s), TURNS, perm=perm, scenario={"kind": kind}))
    return base, pert


def results_of(deck, kind, base, pert):
    n = len(base)
    mb = [metrics(r, deck) for r in base]
    mp = [metrics(r, deck) for r in pert]
    keys = [k for k in mb[0] if deck.combos or k not in ("win_turn_proxy_by_t8", "combo_assembled_by_t8")]
    out = []
    for k in keys:
        d = [y[k] - x[k] for x, y in zip(mb, mp)]
        md, ci = gs.mean_ci(d)
        out.append({"metric": k, "baseline": round(sum(x[k] for x in mb) / n, 5), "challenger": round(sum(y[k] for y in mp) / n, 5),
                    "diff": round(md, 5), "ci95": [round(ci[0], 5), round(ci[1], 5)],
                    "method": "paired: baseline unperturbed, challenger perturbed, same shuffles; diff per game; CI95 normal"})
    fired = sum(1 for r in pert if r["event_turn"] is not None or r["removals"])
    sm = [{"metric": "event_fired_share", "value": round(fired / n, 5), "ci95": [round(x, 5) for x in gs.wilson(fired, n)[1]], "n": n,
           "method": "share of perturbed games in which the scripted event happened (e.g. the commander was on the battlefield to be removed)"}]
    if kind.startswith("commander_removed") or kind == "board_wipe":
        rem = [r for r in pert if r["removals"]]
        rec_t = [r["recasts"][0] - r["removals"][0] for r in rem if r["recasts"]]
        k = len(rec_t)
        sm.append({"metric": "commander_recast_share", "value": round(k / len(rem), 5) if rem else 0.0,
                   "ci95": [round(x, 5) for x in gs.wilson(k, len(rem))[1]] if rem else [0.0, 0.0], "n": len(rem),
                   "method": "share of games with a commander removal in which the commander was recast by turn 10"})
        if rec_t:
            m, ci = gs.mean_ci(rec_t)
            sm.append({"metric": "recovery_turns", "value": round(m, 5), "ci95": [round(ci[0], 5), round(ci[1], 5)], "n": k,
                       "method": "turns from the first removal (end step) to the recast, among games where it was recast"})
            w2 = sum(1 for x in rec_t if x <= 2)
            sm.append({"metric": "recovered_within_2_turns_share", "value": round(w2 / len(rem), 5), "ci95": [round(x, 5) for x in gs.wilson(w2, len(rem))[1]], "n": len(rem),
                       "method": "share of removal games where the commander was recast within 2 turns"})
    return out, sm


def verdict(results, metric, threshold):
    r = next(x for x in results if x["metric"] == metric)
    lo, hi = r["ci95"]
    if lo <= 0 <= hi:
        return "no_detectable_difference"
    if hi < 0 and lo > -threshold:
        return "pass"
    if r["diff"] <= -threshold and hi < 0:
        return "fail"
    return "inconclusive"


def build_deck(slug, did, samples, seed, R=None):
    deck = gs.load_deck(slug, R)
    reg = ga.load_json(ga.REGISTRY)["decks"][ga.registry_id(did)]
    h = reg["canonical_project_list"]["hash"]
    recs = []
    for kind in STRESS_PREREG:
        base, pert = run_pair(deck, kind, samples, seed)
        res, sm = results_of(deck, kind, base, pert)
        metric, th = primary_for(kind, deck)
        key = json.dumps({"b": h, "v": gs.VERSION, "k": kind, "s": seed, "n": samples, "p": [metric, th]}, sort_keys=True)
        T = gs.SCENARIOS[kind][0]
        recs.append({"schema_version": 1, "id": f"test:{slug}:stress:{kind}:" + hashlib.sha256(key.encode()).hexdigest()[:12],
                     "deck_id": ga.registry_id(did), "kind": "stress_scenario", "baseline_hash": h, "challenger_hash": None,
                     "simulator": {"name": gs.NAME, "version": gs.VERSION, "model_sha256": gs.model_sha256()},
                     "seed": seed, "paired": True, "samples": samples, "mulligan": gs.KEEP_RULE,
                     "seat": "multiplayer, seat-agnostic (no turn-1 draw skip, CR 103.8c); first mulligan free (CR 103.5c)",
                     "scenario": f"{kind}@T{T}: {gs.SCENARIOS[kind][1]}",
                     "preregistered": {"metric": metric, "threshold": th, "registered": REGISTERED},
                     "results": res, "scenario_metrics": sm, "verdict": verdict(res, metric, th), "limitations": LIMITATIONS})
    return {"_doc": "Bot cycle 57.4 (M3): scripted stress scenarios on the canonical list (paired: unperturbed vs perturbed on identical shuffles). Built by scripts/grixis_stress.py; schema test.schema.json. Not win rates.",
            "deck_id": ga.registry_id(did), "slug": slug, "records": recs}


def dump(doc):
    """One record per line (compact, diffable)."""
    head = json.dumps({k: v for k, v in doc.items() if k != "records"}, indent=1, ensure_ascii=False)[:-2]
    return head + ',\n "records": [\n  ' + ",\n  ".join(json.dumps(r, ensure_ascii=False, separators=(",", ":")) for r in doc["records"]) + "\n ]\n}\n"


def _job(args):
    slug, did, samples, seed = args
    return slug, build_deck(slug, did, samples, seed)


def build(samples, seed, decks=None, jobs=8):
    OUT.mkdir(parents=True, exist_ok=True)
    summ = ga.summary()
    todo = [(v["slug"], did, samples, seed) for did, v in sorted(summ.items(), key=lambda kv: kv[1]["slug"]) if not decks or v["slug"] in decks]
    if jobs > 1:
        from multiprocessing import Pool
        with Pool(jobs) as p:
            out = p.map(_job, todo)
    else:
        out = [_job(t) for t in todo]
    for slug, doc in out:
        (OUT / f"{slug}.json").write_text(dump(doc), encoding="utf-8")
    print(f"stress --build: {len(out)} deck(s) × {len(STRESS_PREREG)} scenarios, {samples} paired games each")


def check(verbose=True, rerun=True):
    p = []
    summ = ga.summary()
    reg = ga.load_json(ga.REGISTRY)["decks"]
    n = 0
    for did, v in sorted(summ.items(), key=lambda kv: kv[1]["slug"]):
        f = OUT / f"{v['slug']}.json"
        if not f.exists():
            p.append(f"{v['slug']}: no stress records (run --build)")
            continue
        doc = json.loads(f.read_text(encoding="utf-8"))
        kinds = [r["scenario"].split("@")[0] for r in doc["records"]]
        if sorted(kinds) != sorted(STRESS_PREREG):
            p.append(f"{f.name}: scenarios {sorted(kinds)} != {sorted(STRESS_PREREG)}")
        h = reg[ga.registry_id(did)]["canonical_project_list"]["hash"]
        for r in doc["records"]:
            n += 1
            for e in ga.validate_file(r, "test.schema.json"):
                p.append(f"{f.name}: {r['id']}: {e}")
            if r["baseline_hash"] != h:
                p.append(f"{f.name}: {r['id']}: list changed since the run (stale)")
            if r["simulator"]["version"] != gs.VERSION:
                p.append(f"{f.name}: {r['id']}: simulator v{r['simulator']['version']} != current v{gs.VERSION} (rerun --build)")
            if r["verdict"] != verdict(r["results"], r["preregistered"]["metric"], r["preregistered"]["threshold"]):
                p.append(f"{f.name}: {r['id']}: verdict doesn't follow the rule")
            if any("win_rate" in x["metric"] for x in r["results"]):
                p.append(f"{f.name}: {r['id']}: win-rate metric (not allowed)")
    if rerun and (ROOT / ".cache").exists() and not p:
        for slug in CHECK_DECKS:
            did = next(k for k, v in summ.items() if v["slug"] == slug)
            doc = json.loads((OUT / f"{slug}.json").read_text(encoding="utf-8"))
            r0 = doc["records"][0]
            fresh = build_deck(slug, did, r0["samples"], r0["seed"])
            strip = lambda d: [{k: v for k, v in r.items() if k != "simulator"} for r in d["records"]]
            if strip(fresh) != strip(doc):
                p.append(f"{slug}: re-run does not reproduce the stored stress records (behaviour changed without a version bump?)")
    if verbose:
        print(f"stress: {n} record(s) for {len(summ)} decks; {len(p)} problem(s)" + ("" if rerun else " (re-run skipped)"))
        for x in p[:30]:
            print("  -", x)
    return p


def summary():
    from collections import Counter
    v = Counter()
    rows = {}
    for f in sorted(OUT.glob("*.json")):
        for r in json.loads(f.read_text(encoding="utf-8"))["records"]:
            k = r["scenario"].split("@")[0]
            v[(k, r["verdict"])] += 1
            rows.setdefault(k, []).append(next(x for x in r["results"] if x["metric"] == r["preregistered"]["metric"])["diff"])
    for k in STRESS_PREREG:
        vs = {vv: c for (kk, vv), c in v.items() if kk == k}
        d = sorted(rows.get(k, []))
        print(f"{k:28s} {vs}  primary diff median {d[len(d) // 2] if d else None}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--build", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--summary", action="store_true")
    ap.add_argument("--samples", type=int, default=500)
    ap.add_argument("--seed", type=int, default=57)
    ap.add_argument("--decks", default="")
    ap.add_argument("--jobs", type=int, default=8)
    a = ap.parse_args()
    if a.build:
        build(a.samples, a.seed, {s for s in a.decks.split(",") if s} or None, a.jobs)
        return 0
    if a.summary:
        summary()
        return 0
    return 1 if check() else 0


if __name__ == "__main__":
    sys.exit(main())
