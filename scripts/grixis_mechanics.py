#!/usr/bin/env python3
"""Step E (Bot cycle 66.1): mechanic-module registry, router coverage over legacy M5 not_modelable swaps, real-deck examples.

  python3 scripts/grixis_mechanics.py --build    # writes data/grixis/mechanics/{modules,coverage_legacy_m5,examples}.json
  python3 scripts/grixis_mechanics.py --check    # schema + registry matches code + no forbidden metric (cheap)
"""
import argparse, glob, gzip, json, os, sys, time

os.environ.setdefault("SCRYFALL_OFFLINE", "1")  # never refresh the shared bulk cache (snap-20261016 is frozen, Cory D6)
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import grixis_mech as gm  # noqa: E402
from grixis_mech import router, observe  # noqa: E402

OUT = ROOT / "data" / "grixis" / "mechanics"
SCHEMA = ROOT / "data" / "grixis" / "schemas" / "mechanic_module.schema.json"
EXAMPLES = [("wick-the-whorled-mind", None, None)]  # filled from the coverage scan: first routed swap per implemented module
SAMPLES, SEED = 300, 66
RECURSION_REPLAY = {"swap:abaddon-the-despoiler:m5:19cc391585d8"}  # 66.1 recursion example (Birgi -> Poxwalkers), re-run in 66.2


def dump(p, d):
    p.write_text(json.dumps(d, indent=1, ensure_ascii=False, sort_keys=True) + "\n")


def cards_index():
    import grixis_candidates as gc
    pool, _ = gc.load_pool()
    return {n: {"text": gc.otext(c), "type_line": gc.tline(c)} for n, c in pool.items()}


def coverage(cards):
    tot, st, per, ex = 0, Counter(), Counter(), {}
    from grixis_mech import death_triggers as dt
    dnm = Counter()
    for f in sorted(glob.glob(str(ROOT / "data/grixis/candidates/*.json.gz"))):
        d = json.loads(gzip.decompress(Path(f).read_bytes()))
        for sw in d["swaps"]:
            if sw["tests"]:
                continue
            tot += 1
            r = router.route_swap(sw["cuts"][0], sw["adds"][0], cards)
            for n in (sw["cuts"][0], sw["adds"][0]):
                if n in cards:
                    why = dt.parse(n, cards[n]["text"])[1]
                    if why:
                        dnm[why] += 1
            st[r["status"]] += 1
            for k in r["modules"] + r["planned"]:
                per[k] += 1
            for k in r["modules"]:
                ex.setdefault(k, (d["slug"], sw["cuts"][0], sw["adds"][0], sw["id"]))
            if sw["id"] in RECURSION_REPLAY:
                ex.setdefault("replay:" + sw["id"], (d["slug"], sw["cuts"][0], sw["adds"][0], sw["id"]))
    return {"evidence_class": "derived_metric", "scope": "legacy M5 (capped, Bot cycle 61) swaps with no paired test",
            "not_modelable_swaps": tot, "by_status": dict(sorted(st.items())),
            "now_routed_to_implemented_module": st["routed"], "now_routed_share": round(st["routed"] / max(1, tot), 4),
            "routed_incl_planned_share": round((st["routed"] + st["planned_module"]) / max(1, tot), 4),
            "per_module_family": dict(sorted(per.items())),
            "death_triggers_not_modelable_card_occurrences": dict(sorted(dnm.items())), "note": "a swap can route to several families; routing is "
            "eligibility to be tested by a module, not a test result"}, ex


def example(slug, cut, add, cards):
    import grixis_sim as gs
    base = gs.load_deck(slug)
    i = next(j for j, x in enumerate(base.library) if x["name"] == cut)
    import grixis_candidates as gc
    pool, _ = gc.load_pool()
    am = gs.card_model(pool[add], base.ci)
    chal = gs.Deck(base.slug, base.commanders, base.library[:i] + [am] + base.library[i + 1:], base.key_sets, base.combos)
    chal.ci, chal.engine, chal.gy_combo = base.ci, base.engine, base.gy_combo
    t0 = time.time()
    bg = observe.trace_games(base, SAMPLES, SEED)
    cg = observe.trace_games(chal, SAMPLES, SEED)
    models = {x["name"]: x for x in base.library + [am] + list(base.commanders)}
    from grixis_mech import deaths
    ctx = {"creatures": {n for n, x in models.items() if x.get("creature")}, "commanders": {x["name"] for x in base.commanders},
           "outlets": {n for n in models if n in cards and deaths.is_outlet(cards[n]["text"])}}
    r = router.route_swap(cut, add, cards)
    res = []
    for k in r["modules"]:
        m = gm.MODULES[k]
        if k == "graveyard_recursion":
            res.append(m.evaluate(bg, cg, cut, add, cards, models))          # no-death lower bound
            res.append(m.evaluate_grid(bg, cg, cut, add, cards, models, ctx))  # shared death layer grid
        elif k == "attack_trigger_proxy":
            res.append(m.evaluate(bg, cg, cut, add, cards))
        else:
            res.append(m.evaluate(bg, cg, cut, add, cards, ctx))
    return {"deck": slug, "cut": cut, "add": add, "route": r, "samples": SAMPLES, "seed": SEED, "results": res,
            "evidence_class": "test_result", "authority": {"exploratory": True, "can_decide": False},
            "runtime_seconds_note": f"{round(time.time() - t0, 1)}s for {2 * SAMPLES} traced games (not stored in the check)"}


def build():
    OUT.mkdir(parents=True, exist_ok=True)
    dump(OUT / "modules.json", {"framework_version": gm.FRAMEWORK_VERSION, "modules": gm.registry(),
                                "planned_families": sorted(k for k in router.PLANNED if k not in gm.MODULES)})
    cards = cards_index()
    cov, ex = coverage(cards)
    dump(OUT / "coverage_legacy_m5.json", cov)
    print(json.dumps({k: cov[k] for k in ("not_modelable_swaps", "by_status", "now_routed_share", "routed_incl_planned_share")}))
    exs = []
    for k, (slug, cut, add, sid) in sorted(ex.items()):
        e = example(slug, cut, add, cards)
        e["swap"] = sid
        print(k, slug, cut, "->", add, e["runtime_seconds_note"])
        e.pop("runtime_seconds_note")
        exs.append(e)
    dump(OUT / "examples.json", {"framework_version": gm.FRAMEWORK_VERSION, "examples": exs})


def problems():
    import jsonschema
    v = jsonschema.Draft202012Validator(json.loads(SCHEMA.read_text()))
    p = []
    for s in gm.registry():
        p += [f"{s['id']}: {e.message}" for e in v.iter_errors(s)]
        if any(f in m for m in s["metrics"] for f in gm.FORBIDDEN_METRICS):
            p.append(f"{s['id']}: forbidden metric")
    reg = json.loads((OUT / "modules.json").read_text())
    if reg["modules"] != json.loads(json.dumps(gm.registry())):
        p.append("modules.json does not match the code registry (run --build)")
    for f in ("coverage_legacy_m5.json", "examples.json"):
        if not (OUT / f).is_file():
            p.append(f"{f} missing")
    txt = (OUT / "examples.json").read_text() if (OUT / "examples.json").is_file() else ""
    if any(f in txt for f in gm.FORBIDDEN_METRICS):
        p.append("examples.json contains a forbidden metric")
    return p


if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--build", action="store_true")
    a.add_argument("--check", action="store_true")
    x = a.parse_args()
    if x.build:
        build()
    if x.check:
        p = problems()
        for e in p:
            print("FAIL", e)
        print(f"mechanics: {len(gm.MODULES)} modules, {len(p)} problems")
        sys.exit(1 if p else 0)
