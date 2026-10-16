#!/usr/bin/env python3
"""M3 paired-seed champion-vs-challenger goldfish tests (Bot cycle 57.3).

The champion is the deck's canonical project list; a challenger is any other list for the same commander(s). The
registered challengers (registry `challengers[]`) are tested by --run-registered. Both libraries are aligned (shared cards
in the same positions, swapped cards in each other's positions), and every game i uses the same shuffle permutation and
the same mulligan reshuffles for both lists (seed_for(seed, i)), so per-game differences isolate the swap.

Pre-registration: the metrics, directions, thresholds and the verdict rule are fixed in PREREG below; they were written
in Bot cycle 57.3 before any paired run (`registered`), and a record stores them. A record's verdict uses the primary
metric only; the others are reported with paired CI95s and never change the verdict.

Verdict rule (primary metric, higher is better):
  pass                      diff >= threshold and CI95 lower bound > 0
  fail                      diff <= -threshold and CI95 upper bound < 0
  no_detectable_difference  CI95 contains 0
  inconclusive              a detectable difference smaller than the threshold
Goldfish results are about this deck's own development (mana, curve, commander, access); they are never win rates and
say nothing about opponents, interaction or card draw the model doesn't simulate (see LIMITATIONS).

Records: data/grixis/tests/<slug>.json ({"records": [...]}, each valid against test.schema.json). The id is keyed by the
snapshot (both list hashes, the simulator model version, seed, samples, PREREG). Since Bot cycle 57.6 a file holds one
record per (challenger, model version): v1.0 records are kept and --check re-runs each under its own version, and every
registered challenger needs a record for the current version. --check fails when a list or the registry
changed (stale), the simulator version differs, or a re-run doesn't reproduce the stored results exactly; a behaviour
change therefore needs a version bump (model_sha256 records the code that produced the record).

Usage:
  python3 scripts/grixis_paired.py --run-registered [--samples 2000] [--seed 57]
  python3 scripts/grixis_paired.py --deck SLUG --swap "Cut=>Add" [--swap ...]   # ad hoc, printed, not stored
  python3 scripts/grixis_paired.py --check
"""
import argparse
import hashlib
import json
import math
import random
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import grixis_authority as ga  # noqa: E402
import grixis_sim as gs  # noqa: E402

OUT = ROOT / "data" / "grixis" / "tests"
REGISTERED = "2026-10-16 (Bot cycle 57.3, before any paired run)"
TURNS = 10
PREREG = {
    "primary": {"metric": "mana_spent_t1_t6", "threshold": 0.25,
                "definition": "mean per game of the mana spent on turns 1-6 (curve use); higher is better"},
    "secondary": [
        {"metric": "commander_cast_by_t4", "threshold": 0.02, "definition": "share of games with the commander cast by turn 4"},
        {"metric": "mana_available_t4", "threshold": 0.1, "definition": "mean mana available on turn 4"},
        {"metric": "win_turn_proxy_by_t8", "threshold": 0.02, "definition": "share of games where a Spellbook combo is drawn and affordable by turn 8 (goldfish proxy, not a win rate)"},
        {"metric": "mulligans_neg", "threshold": 0.05, "definition": "minus the mean mulligans taken (higher is better)"},
        {"metric": "key_access_by_t4:<package>", "threshold": 0.02, "definition": "share of games with at least one card of the blueprint package seen by turn 4"},
    ],
}
LIMITATIONS = [
    "Goldfish: one player, no opponents, no interaction, no combat; results are about the deck's own development, never win rates.",
    "Not modelled: tutors, card draw and selection beyond the natural draw, treasures, rituals and one-shot mana (Lotus Petal, Mana Vault, Lion's Eye Diamond); a swap whose value is card draw, interaction or a tutor effect is invisible here.",
    "Conditional fast mana (Chrome Mox, Mox Diamond, Mox Opal, Mox Amber, Springleaf Drum, Paradise Mantle) is treated as unconditional; 'enters tapped unless ...' lands as untapped.",
    "Combo pieces are 'assembled' when drawn; Commander Spellbook 'requires' conditions and the combo's own mana needs beyond the cards' mana values are ignored.",
    "Fixed policy: commander first, then mana sources, then highest mana value; keep/bottom rule as recorded in 'mulligan'.",
]
# Bot cycle 57.6: one limitations list per simulator model version; v1.0 records keep the list above verbatim.
LIMITATIONS_BY_MODEL = {
    "1.0": LIMITATIONS,
    "1.1": [LIMITATIONS[0]] + gs.MODEL_NOTES["1.1"] + [
        "'Enters tapped unless ...' lands as untapped.",
        LIMITATIONS[3],
        "Fixed policy: commander first, then mana sources (conditions met), then tutors and draw spells (cheapest "
        "first), then highest mana value, then a ritual only if it enables an otherwise uncastable card; keep/bottom "
        "rule as recorded in 'mulligan'.",
    ],
}


def metrics_of(rec, keys):
    m = {"mana_spent_t1_t6": sum(rec["spent"][:6]),
         "commander_cast_by_t4": 1.0 if rec["commander_turn"] is not None and rec["commander_turn"] <= 4 else 0.0,
         "mana_available_t4": rec["mana"][3],
         "win_turn_proxy_by_t8": 1.0 if rec["win_turn_proxy"] is not None and rec["win_turn_proxy"] <= 8 else 0.0,
         "mulligans_neg": -rec["mulligans"]}
    for k in keys:
        t = rec["key_turn"].get(k)
        m[f"key_access_by_t4:{k}"] = 1.0 if t is not None and t <= 4 else 0.0
    return m


def align(a, b, pairs=None):
    """Reorder two libraries so shared cards share positions and each cut takes its add's position (`pairs`: the
    registered [(cut, add)] order; otherwise alphabetical)."""
    ca, cb = Counter(c["name"] for c in a.library), Counter(c["name"] for c in b.library)
    if sum(ca.values()) != sum(cb.values()):
        raise ValueError(f"library sizes differ: {sum(ca.values())} vs {sum(cb.values())}")
    common = ca & cb
    only_a, only_b = sorted((ca - common).elements()), sorted((cb - common).elements())
    if pairs and sorted(x for x, _ in pairs) == only_a and sorted(y for _, y in pairs) == only_b:
        only_a, only_b = [x for x, _ in pairs], [y for _, y in pairs]
    pick = lambda d, name: next(c for c in d.library if c["name"] == name)
    order_common = sorted(common.elements())
    la = [pick(a, n) for n in order_common] + [pick(a, n) for n in only_a]
    lb = [pick(b, n) for n in order_common] + [pick(b, n) for n in only_b]
    a2 = gs.Deck(a.slug, a.commanders, la, a.key_sets, a.combos)
    b2 = gs.Deck(b.slug, b.commanders, lb, a.key_sets, b.combos)  # same key-set definitions (the champion's blueprint)
    a2.ci, b2.ci = a.ci, b.ci
    return a2, b2, list(zip(only_a, only_b))


def paired(a, b, samples, seed, turns=TURNS, pairs=None, model=gs.VERSION):
    a2, b2, swaps = align(a, b, pairs)
    N = a2.N
    ra, rb = [], []
    for i in range(samples):
        s = gs.seed_for(seed, i)
        perm = random.Random(s ^ 0x5EED).sample(range(N), N)
        ra.append(gs.play_game(a2, random.Random(s), turns, perm=perm, model=model))
        rb.append(gs.play_game(b2, random.Random(s), turns, perm=perm, model=model))
    keys = sorted(a2.key_sets)
    ma = [metrics_of(r, keys) for r in ra]
    mb = [metrics_of(r, keys) for r in rb]
    out = []
    for m in ma[0]:
        xa = [x[m] for x in ma]
        xb = [x[m] for x in mb]
        d = [y - x for x, y in zip(xa, xb)]
        md, ci = gs.mean_ci(d)
        out.append({"metric": m, "baseline": round(sum(xa) / samples, 5), "challenger": round(sum(xb) / samples, 5),
                    "diff": round(md, 5), "ci95": [round(ci[0], 5), round(ci[1], 5)],
                    "method": f"paired goldfish, {samples} games on identical shuffles; diff = challenger - baseline per game; CI95 = mean ± 1.96·sd/√n of the per-game differences"
                              + ("" if m == PREREG["primary"]["metric"] else "; secondary (does not set the verdict)")})
    return out, swaps


def verdict(results):
    pr = PREREG["primary"]
    r = next(x for x in results if x["metric"] == pr["metric"])
    lo, hi = r["ci95"]
    if lo <= 0 <= hi:
        return "no_detectable_difference"
    if r["diff"] >= pr["threshold"] and lo > 0:
        return "pass"
    if r["diff"] <= -pr["threshold"] and hi < 0:
        return "fail"
    return "inconclusive"


def coverage(a, b, swaps, model):
    """v1.1+: what the model simulates of each swapped card (a swap between an unmodelled and a modelled effect is a
    model asymmetry, not evidence about the cards)."""
    if model == "1.0":
        return []
    by = {c["name"]: c for c in a.library + b.library}
    out = []
    for x, y in swaps:
        def f(n):
            c = by.get(n)
            ft = sorted(k for k, v in (c or {}).get("v11", {}).items() if v) if c else []
            src = c and c.get("source")
            return f"{n} [{', '.join(ft + (['mana source'] if src else [])) or 'no effect modelled beyond being a castable card'}]"
        out.append(f"{f(x)} → {f(y)}")
    return [f"Model v{model} coverage of the swapped cards: " + "; ".join(out) + "."]


def record(slug, did, champ_hash, chal, samples, seed, results, swaps, model=gs.VERSION, cov=None):
    key = json.dumps({"b": champ_hash, "c": chal["hash"], "v": model, "s": seed, "n": samples, "p": PREREG}, sort_keys=True)
    tid = "test:" + slug + ":goldfish:" + hashlib.sha256(key.encode()).hexdigest()[:16]
    return {"schema_version": 1, "id": tid, "deck_id": ga.registry_id(did), "kind": "goldfish_mc", "baseline_hash": champ_hash,
            "challenger_hash": chal["hash"], "simulator": {"name": gs.NAME, "version": model, "model_sha256": gs.model_sha256()},
            "seed": seed, "paired": True, "samples": samples, "mulligan": gs.KEEP_RULE,
            "seat": "multiplayer, seat-agnostic (no turn-1 draw skip, CR 103.8c); first mulligan free (CR 103.5c)", "scenario": None,
            "preregistered": {"metric": PREREG["primary"]["metric"], "threshold": PREREG["primary"]["threshold"], "registered": REGISTERED},
            "results": results, "verdict": verdict(results),
            "limitations": LIMITATIONS_BY_MODEL[model] + [f"Challenger {chal['id']} ({chal['label']}); swaps tested: " + "; ".join(f"{x} → {y}" for x, y in swaps) + "."] + (cov or [])}


def registered_pairs():
    reg = ga.load_json(ga.REGISTRY)
    summ = ga.summary()
    by_rid = {ga.registry_id(k): k for k in summ}
    for rid, e in sorted(reg["decks"].items()):
        for ch in e.get("challengers") or []:
            yield by_rid.get(rid, rid), e, ch


def run_registered(samples, seed, force=False, verbose=True, model=gs.VERSION):
    """Run every registered challenger under `model` and add the records; records of other model versions are kept
    (Bot cycle 57.6: old records are preserved, keyed by version)."""
    import evaluate_decklist as ev
    R = ev.Resolver()
    OUT.mkdir(parents=True, exist_ok=True)
    files = {}
    for did, e, ch in registered_pairs():
        slug = e["slug"]
        champ_hash = e["canonical_project_list"]["hash"]
        text = (ROOT / ch["export_path"]).read_text(encoding="utf-8")
        h = ga.text_hash(text, R)
        if h != ch["hash"]:
            raise SystemExit(f"{slug}: challenger export hash {h} != registry {ch['hash']}")
        f = OUT / f"{slug}.json"
        old = json.loads(f.read_text(encoding="utf-8")) if f.exists() else {"records": []}
        a = gs.load_deck(slug, R)
        b = gs.load_deck(slug, R, text=text)
        res, swaps = paired(a, b, samples, seed, pairs=[(x["cut"], x["add"]) for x in ch.get("swaps", [])], model=model)
        rec = record(slug, did, champ_hash, ch, samples, seed, res, swaps, model, coverage(a, b, swaps, model))
        doc = files.setdefault(slug, old)
        doc["_doc"] = ("Bot cycle 57.3 (M3): paired goldfish test records; built by scripts/grixis_paired.py; schema "
                       "test.schema.json. One record per (challenger, simulator model version); records of older model "
                       "versions are kept and re-checked under their own version (Bot cycle 57.6).")
        if not force and any(r["id"] == rec["id"] for r in doc["records"]):
            continue
        doc["records"] = [r for r in doc["records"] if not (r.get("challenger_hash") == ch["hash"] and r["simulator"]["version"] == model)] + [rec]
        doc["records"].sort(key=lambda r: (r["challenger_hash"], r["simulator"]["version"]))
        if verbose:
            p = next(x for x in res if x["metric"] == PREREG["primary"]["metric"])
            print(f"{slug}: {rec['verdict']} (primary {p['metric']} diff {p['diff']:+.3f}, CI95 {p['ci95']}); swaps {swaps}")
    for slug, doc in files.items():
        (OUT / f"{slug}.json").write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    return files


def check(verbose=True):
    p = []
    have_cache = (ROOT / ".cache").exists()
    want = {(e["slug"], ch["hash"]): (did, e, ch) for did, e, ch in registered_pairs()}
    seen = set()
    n = 0
    R = None
    for f in sorted(OUT.glob("*.json")):
        doc = json.loads(f.read_text(encoding="utf-8"))
        for r in doc.get("records", []):
            n += 1
            for e in ga.validate_file(r, "test.schema.json"):
                p.append(f"{f.name}: {r.get('id')}: {e}")
            slug = f.stem
            k = (slug, r["challenger_hash"])
            ver = r["simulator"]["version"]
            seen.add(k + (ver,))
            if k not in want:
                p.append(f"{f.name}: {r['id']}: challenger {r['challenger_hash']} is not a registered challenger")
                continue
            did, e, ch = want[k]
            if r["baseline_hash"] != e["canonical_project_list"]["hash"]:
                p.append(f"{f.name}: {r['id']}: baseline hash is not the canonical list hash (stale)")
            if ver not in gs.MODELS:
                p.append(f"{f.name}: {r['id']}: simulator model v{ver} is not runnable (known: {gs.MODELS})")
                continue
            if r["preregistered"]["metric"] != PREREG["primary"]["metric"] or r["preregistered"]["threshold"] != PREREG["primary"]["threshold"]:
                p.append(f"{f.name}: {r['id']}: pre-registered metric/threshold differs from PREREG")
            if r["verdict"] != verdict(r["results"]):
                p.append(f"{f.name}: {r['id']}: verdict {r['verdict']} doesn't follow the rule ({verdict(r['results'])})")
            if have_cache and not any(x.startswith(f"{f.name}: {r['id']}") for x in p):
                if R is None:
                    import evaluate_decklist as ev
                    R = ev.Resolver()
                text = (ROOT / ch["export_path"]).read_text(encoding="utf-8")
                res, _ = paired(gs.load_deck(slug, R), gs.load_deck(slug, R, text=text), r["samples"], r["seed"],
                                pairs=[(x["cut"], x["add"]) for x in ch.get("swaps", [])], model=ver)
                if res != r["results"]:
                    p.append(f"{f.name}: {r['id']}: re-run does not reproduce the stored results")
    for k in sorted(set(want) - {x[:2] for x in seen if x[2] == gs.VERSION}):
        p.append(f"{k[0]}: registered challenger {k[1]} has no paired test record for the current model v{gs.VERSION} (run --run-registered)")
    if verbose:
        print(f"paired tests: {n} record(s) for {len(want)} registered challenger(s); {len(p)} problem(s)" + ("" if have_cache else " (no .cache: re-runs skipped)"))
        for x in p[:30]:
            print("  -", x)
    return p


def adhoc(slug, swaps, samples, seed):
    import evaluate_decklist as ev
    R = ev.Resolver()
    text = ga.deck_block_text(slug)
    lines = text.splitlines()
    for sw in swaps:
        cut, add = [x.strip() for x in sw.split("=>")]
        i = next(i for i, l in enumerate(lines) if l.split(" ", 1)[-1].split(" [")[0].strip() == cut)
        lines[i] = f"1 {add}"
    a = gs.load_deck(slug, R)
    b = gs.load_deck(slug, R, text="\n".join(lines) + "\n")
    res, sw = paired(a, b, samples, seed)
    print(json.dumps({"deck": slug, "model": gs.VERSION, "swaps": sw, "verdict": verdict(res), "results": res}, indent=1, ensure_ascii=False))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-registered", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--deck")
    ap.add_argument("--swap", action="append", default=[])
    ap.add_argument("--samples", type=int, default=2000)
    ap.add_argument("--seed", type=int, default=57)
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()
    if a.run_registered:
        run_registered(a.samples, a.seed, a.force)
        return 0
    if a.deck:
        adhoc(a.deck, a.swap, a.samples, a.seed)
        return 0
    return 1 if check() else 0


if __name__ == "__main__":
    sys.exit(main())
