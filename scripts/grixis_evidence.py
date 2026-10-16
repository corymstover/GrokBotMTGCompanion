#!/usr/bin/env python3
"""M3 evidence layer (Bot cycle 57): one evidence vector per (deck, card) for every card in the canonical list and every
EDHREC candidate on the deck's commander page(s).

A vector holds the EDHREC numbers (lift, synergy, inclusion, sample size, trend z-score, retrieval date), the Oracle hook
(the commander-text regex match used by grixis_refine v2), and graph facts (Commander Spellbook combo membership, M1
interaction-review ids, blueprint package / identity-core membership). Every part carries an evidence class and a
confidence (grixis/Grixis Authority Model.md#evidence-classes), and `items()` expands a vector into evidence items that
validate against data/grixis/schemas/evidence.schema.json.

Aggregation: a partner deck with a combined EDHREC page uses that page. Otherwise the individual commander pages are
pooled: num_decks and potential_decks are summed, and inclusion, lift, synergy and trend z-score are potential_decks-
weighted means (method "pooled"; confidence capped at low, because the pages are different populations).

EDHREC identity, checked on every unpooled row: lift = inclusion / (inclusion - synergy). Synergy is the commander's
inclusion rate minus a baseline rate, and lift is inclusion over a baseline; when both use the same baseline the identity
holds (to 0.1% on 51 of the 62 pages). Rows where it fails by more than 2% are flagged lift_synergy_inconsistent and kept
at low confidence: the two numbers then rest on different baselines, so neither is read alone.

Snapshot-keyed caching: each deck file records the sha256 of every input (EDHREC pages, Oracle bulk name, combo cache,
M1 review, blueprint, canonical deck page, this script). The snapshot id is the hash of those. --build skips decks whose
snapshot id is unchanged; --check fails on a stale snapshot (when the cache is present) and validates every vector.

Usage:
  python3 scripts/grixis_evidence.py --build [--decks slug,slug] [--force]
  python3 scripts/grixis_evidence.py --check
  python3 scripts/grixis_evidence.py --show SLUG CARD
"""
import argparse
import datetime as dt
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import grixis_authority as ga  # noqa: E402

VERSION = "1"
OUT = ROOT / "data" / "grixis" / "evidence"
SCHEMA = ROOT / "data" / "grixis" / "schemas" / "evidence_vector.schema.json"
EDH = ROOT / ".cache" / "edhrec"
COMBOS = ROOT / "data" / "grixis_combos.json"
INTER = ROOT / "data" / "grixis_interactions"
BPS = ROOT / "data" / "grixis" / "blueprints"
SMALL_SAMPLE = 50     # potential_decks below this: low confidence (same threshold as grixis_refine v2)
FEW_DECKS = 20        # num_decks below this: low confidence
TREND_Z = 2.0         # |trend_zscore| at or above this is flagged rising / falling
SKIP_LISTS = ("newcards", "topcommanders", "newcommanders")
TODAY = dt.date(2026, 10, 16)


def sha_file(p):
    return "sha256:" + hashlib.sha256(Path(p).read_bytes()).hexdigest()


def sha_text(t):
    return "sha256:" + hashlib.sha256(t.encode("utf-8")).hexdigest()


def eslug(name):
    s = name.split(" // ")[0].lower().replace("'", "").replace(",", "")
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def pages_for(cmds):
    """(pages, method): the combined partner page when cached, else the individual commander pages."""
    if len(cmds) > 1:
        comb = "-".join(sorted(eslug(c) for c in cmds))
        if (EDH / f"commanders__{comb}.json").exists():
            return [comb], "combined_page"
        got = [eslug(c) for c in cmds if (EDH / f"commanders__{eslug(c)}.json").exists()]
        return got, ("pooled" if len(got) > 1 else "single_page")
    s = eslug(cmds[0])
    return ([s] if (EDH / f"commanders__{s}.json").exists() else []), "single_page"


def read_page(s):
    p = EDH / f"commanders__{s}.json"
    d = json.loads(p.read_text(encoding="utf-8"))
    rows = {}
    for cl in (d.get("container") or {}).get("json_dict", {}).get("cardlists", []):
        if cl.get("tag") in SKIP_LISTS:
            continue
        for v in cl.get("cardviews", []):
            if v.get("synergy") is None or not v.get("potential_decks"):
                continue
            rows.setdefault(v["name"], v)
    sv = sorted((d.get("savedate_counts") or {}).keys())
    mt = dt.datetime.fromtimestamp(p.stat().st_mtime, dt.timezone.utc).date().isoformat()
    return rows, {"page": s, "sha256": sha_file(p), "retrieved": mt, "newest_deck_save": sv[-1] if sv else None}


def pool(views):
    """Pool cardviews from several pages: sums for counts, potential_decks-weighted means for rates."""
    n = sum(v["num_decks"] for v in views)
    pd = sum(v["potential_decks"] for v in views)
    w = lambda k: None if any(v.get(k) is None for v in views) else sum(v[k] * v["potential_decks"] for v in views) / pd
    return {"num_decks": n, "potential_decks": pd, "inclusion": n / pd, "synergy": w("synergy"), "lift": w("lift"), "trend_zscore": w("trend_zscore")}


COLS = ["lift", "synergy", "inclusion", "num_decks", "potential_decks", "trend_zscore", "confidence", "flags"]
IDENTITY_TOL = 0.02   # relative tolerance for lift = inclusion / (inclusion - synergy)
LOW_FLAGS = {"small_sample", "pooled", "one_page_of_pool", "lift_synergy_inconsistent"}


def lift_identity(lift, synergy, inclusion):
    """EDHREC: lift = inclusion / (inclusion - synergy). Relative error, or None when the baseline is too small to check."""
    if lift is None or synergy is None:
        return None
    base = inclusion - synergy
    if base <= 0.001:
        return None
    return abs(inclusion / base - lift) / max(lift, 1e-9)


def edh_row(views, method):
    """Compact EDHREC vector (columns COLS) for one card, or None when no page lists it."""
    if not views:
        return None
    flags = []
    if len(views) == 1:
        v = views[0]
        e = {"num_decks": v["num_decks"], "potential_decks": v["potential_decks"], "inclusion": v["num_decks"] / v["potential_decks"],
             "synergy": v["synergy"], "lift": v.get("lift"), "trend_zscore": v.get("trend_zscore")}
        if method == "pooled":
            flags.append("one_page_of_pool")
    else:
        e = pool(views)
        flags.append("pooled")
    if e["potential_decks"] < SMALL_SAMPLE or e["num_decks"] < FEW_DECKS:
        flags.append("small_sample")
    tz = e["trend_zscore"]
    if tz is not None and tz >= TREND_Z:
        flags.append("rising")
    if tz is not None and tz <= -TREND_Z:
        flags.append("falling")
    r = lambda x, k: None if x is None else round(x, k)
    e = {**e, "lift": r(e["lift"], 3), "synergy": r(e["synergy"], 5), "inclusion": r(e["inclusion"], 5), "trend_zscore": r(tz, 3)}
    if "pooled" not in flags:  # checked on the stored (rounded) numbers, so --check reproduces it exactly
        err = lift_identity(e["lift"], e["synergy"], e["inclusion"])
        if err is not None and err > IDENTITY_TOL:
            flags.append("lift_synergy_inconsistent")
    conf = "low" if set(flags) & LOW_FLAGS else "moderate"
    return [e["lift"], e["synergy"], e["inclusion"], e["num_decks"], e["potential_decks"], e["trend_zscore"], conf, flags]


def edh_dict(row):
    return None if row is None else dict(zip(COLS, row))


def oracle_hook(ctx, card):
    try:
        h = ctx.hook(card)
    except Exception:  # pragma: no cover - defensive: a malformed card dict
        h = None
    if not h:
        return None
    return {"label": h["label"], "commander": h["commander"], "class": "heuristic", "confidence": "moderate"}


def graph_facts(name, did, slug, combos, m1, bp):
    g = {}
    cids = sorted(co["id"] for co in combos.get(did, {}).get("combos", []) if name in co["cards"])
    if cids:
        g["spellbook"] = {"ids": cids, "class": "fact", "confidence": "verified"}
    mids = [(x["id"], x.get("status")) for x in m1 if name in x.get("cards", [])]
    if mids:
        st = {s for _, s in mids}
        g["m1"] = {"ids": [i for i, _ in mids], "class": "fact",
                   "confidence": "test_required" if "uncertain" in st else ("high" if "flag" in st else "verified"),
                   "flags": [i for i, s in mids if s in ("flag", "uncertain")]}
    if bp:
        pk = [p["id"] for p in bp.get("packages", []) if name in p.get("cards", [])]
        core = any(c["card"] == name for c in bp.get("identity_core", []))
        if pk or core:
            g["blueprint"] = {"packages": pk, "identity_core": core, "version": bp.get("version"), "class": "strategic_judgment",
                              "confidence": "high" if core else "moderate"}
    return g


def deck_inputs(did, slug, pages):
    files = [EDH / f"commanders__{p}.json" for p in pages] + [COMBOS, INTER / f"{slug}.json", BPS / f"{slug}.json",
                                                              ROOT / "grixis" / "decks" / f"{slug}.md", Path(__file__)]
    inp = {str(f.relative_to(ROOT)): (sha_file(f) if f.exists() else None) for f in files}
    bulk = sorted((ROOT / ".cache").glob("oracle-cards-*.jsonl.gz"))
    inp["oracle_bulk"] = bulk[-1].name if bulk else None
    sid = sha_text(json.dumps(inp, sort_keys=True) + VERSION)
    return inp, sid


def build_deck(did, v, R, combos, force=False):
    import grixis_refine as gr
    slug = v["slug"]
    cmds = v["commanders"]
    pages, method = pages_for(cmds)
    inp, sid = deck_inputs(did, slug, pages)
    out = OUT / f"{slug}.json"
    if out.exists() and not force:
        old = json.loads(out.read_text(encoding="utf-8"))
        if old.get("snapshot", {}).get("id") == sid:
            return "cached"
    lst = {n: z for z, o, q, n in ga.list_entries(ga.deck_block_text(slug), R)}
    pg = [read_page(p) for p in pages]
    by = {}
    for rows, meta in pg:
        for n, cv in rows.items():
            by.setdefault(n, []).append(cv)
    cards = {n: R.get(n)[0] for n in lst}
    ctx = gr.Ctx([cards[n] for n, z in lst.items() if z == "commander"])
    m1 = json.loads((INTER / f"{slug}.json").read_text(encoding="utf-8")).get("interactions", []) if (INTER / f"{slug}.json").exists() else []
    bpp = BPS / f"{slug}.json"
    bp = json.loads(bpp.read_text(encoding="utf-8")) if bpp.exists() else None
    ci = set().union(*(set(cards[n].get("color_identity", [])) for n, z in lst.items() if z == "commander"))
    vecs = []

    def vec(name, status, c):
        tl = (c.get("type_line") or "") if c else ""
        row = {"card": name, "status": status}
        if status == "incumbent":
            row["zone"] = lst[name]
        lg = (c.get("legalities") or {}).get("commander") if c else None
        if lg != "legal":
            row["legal"] = lg  # only recorded when not Commander-legal (e.g. a pending-release card)
        row["edhrec"] = edh_row(by.get(name, []), method)
        h = oracle_hook(ctx, c) if c and status != "commander" else None
        if h:
            row["oracle_hook"] = h
        g = graph_facts(name, did, slug, combos, m1, bp)
        if g:
            row["graph"] = g
        return row

    for n, z in sorted(lst.items()):
        vecs.append(vec(n, "commander" if z == "commander" else "incumbent", cards[n]))
    for n in sorted(by):
        if n in lst:
            continue
        c, _ = R.get(n)
        if not c or "Basic Land" in (c.get("type_line") or ""):
            continue
        if not set(c.get("color_identity", [])) <= ci:
            continue
        vecs.append(vec(n, "candidate", c))
    doc = {"schema_version": 1, "deck_id": ga.registry_id(did), "slug": slug, "generated_by": f"scripts/grixis_evidence.py v{VERSION}",
           "cycle": 57, "date": TODAY.isoformat(),
           "edhrec": {"pages": [m for _, m in pg], "method": method if pages else "none", "class": "derived_metric", "columns": COLS,
                      "note": "EDHREC is community data (derived_metric): it informs, it never decides (decision_support_ok)."},
           "snapshot": {"id": sid, "inputs": inp},
           "counts": {"incumbent": sum(r["status"] == "incumbent" for r in vecs), "candidate": sum(r["status"] == "candidate" for r in vecs),
                      "with_edhrec": sum(r["edhrec"] is not None for r in vecs)},
           "vectors": vecs}
    out.write_text(dump(doc), encoding="utf-8")
    return "built"


def dump(doc):
    """Compact but diffable: one vector per line."""
    head = {k: v for k, v in doc.items() if k != "vectors"}
    s = json.dumps(head, indent=1, ensure_ascii=False)[:-2]
    rows = ",\n  ".join(json.dumps(r, ensure_ascii=False, separators=(",", ":")) for r in doc["vectors"])
    return s + ',\n "vectors": [\n  ' + rows + "\n ]\n}\n"


def items(doc, row):
    """Expand one vector into evidence items (data/grixis/schemas/evidence.schema.json)."""
    slug, card = doc["slug"], row["card"]
    base = f"evidence:{slug}/{eslug(card)}"
    pages = doc["edhrec"]["pages"]
    out = []
    e = edh_dict(row.get("edhrec"))
    if e:
        out.append({"id": base + "#edhrec", "class": doc["edhrec"]["class"], "confidence": e["confidence"],
                    "claim": f"EDHREC ({doc['edhrec']['method']}): {card} is in {e['num_decks']}/{e['potential_decks']} {doc['slug']} decks; lift {e['lift']}, synergy {e['synergy']}, trend z {e['trend_zscore']}" + (f"; flags {', '.join(e['flags'])}" if e["flags"] else "") + ".",
                    "value": {k: e[k] for k in COLS if k != "confidence"},
                    "source": {"kind": "edhrec", "ref": ", ".join(f"commanders/{p['page']}" for p in pages),
                               "snapshot": pages[0]["sha256"] if len(pages) == 1 else doc["snapshot"]["id"], "retrieved": max(p["retrieved"] for p in pages)},
                    "author": "bot", "created": doc["date"]})
    h = row.get("oracle_hook")
    if h:
        out.append({"id": base + "#oracle-hook", "class": h["class"], "confidence": h["confidence"],
                    "claim": f"{card}'s Oracle text matches the commander hook '{h['label']}' ({h['commander']}).", "value": h["label"],
                    "source": {"kind": "scryfall", "ref": f"oracle:{card}", "snapshot": doc["snapshot"]["inputs"].get("oracle_bulk"), "retrieved": None},
                    "author": "bot", "created": doc["date"]})
    g = row.get("graph") or {}
    if "spellbook" in g:
        out.append({"id": base + "#spellbook", "class": "fact", "confidence": "verified", "claim": f"{card} is a piece of Commander Spellbook combo(s) {', '.join(g['spellbook']['ids'])} in this list.",
                    "value": g["spellbook"]["ids"], "source": {"kind": "spellbook", "ref": "data/grixis_combos.json", "snapshot": doc["snapshot"]["inputs"].get("data/grixis_combos.json"), "retrieved": None},
                    "author": "bot", "created": doc["date"]})
    if "m1" in g:
        out.append({"id": base + "#m1", "class": "fact", "confidence": g["m1"]["confidence"], "claim": f"{card} appears in M1 interaction review(s) {', '.join(g['m1']['ids'])}.",
                    "value": g["m1"]["ids"], "source": {"kind": "review", "ref": f"data/grixis_interactions/{slug}.json", "snapshot": doc["snapshot"]["inputs"].get(f"data/grixis_interactions/{slug}.json"), "retrieved": None},
                    "author": "bot", "created": doc["date"]})
    if "blueprint" in g:
        b = g["blueprint"]
        out.append({"id": base + "#blueprint", "class": b["class"], "confidence": b["confidence"],
                    "claim": f"{card} is in blueprint v{b['version']} " + ("identity core" if b["identity_core"] else "") + (" and " if b["identity_core"] and b["packages"] else "") + (", ".join(b["packages"]) if b["packages"] else "") + ".",
                    "value": {"packages": b["packages"], "identity_core": b["identity_core"]},
                    "source": {"kind": "companion", "ref": f"data/grixis/blueprints/{slug}.json", "snapshot": doc["snapshot"]["inputs"].get(f"data/grixis/blueprints/{slug}.json"), "retrieved": None},
                    "author": "bot", "created": doc["date"]})
    return out


def check(verbose=True):
    summ = ga.summary()
    p, n_vec, n_items, stale, ident_bad, doc_classes_bad = [], 0, 0, 0, 0, False
    have_cache = EDH.exists()
    for did, v in sorted(summ.items(), key=lambda kv: kv[1]["slug"]):
        f = OUT / f"{v['slug']}.json"
        if not f.exists():
            p.append(f"{v['slug']}: no evidence file (run --build)")
            continue
        doc = json.loads(f.read_text(encoding="utf-8"))
        doc_classes_bad = doc_classes_bad or doc["edhrec"].get("class") != "derived_metric"
        for e in ga.validate_file(doc, "evidence_vector.schema.json"):
            p.append(f"{f.name}: {e}")
        if doc["deck_id"] != ga.registry_id(did):
            p.append(f"{f.name}: deck_id {doc['deck_id']} != registry id {ga.registry_id(did)}")
        if have_cache:
            pages, method = pages_for(v["commanders"])
            inp, sid = deck_inputs(did, v["slug"], pages)
            if sid != doc["snapshot"]["id"]:
                stale += 1
                changed = sorted(k for k in set(inp) | set(doc["snapshot"]["inputs"]) if inp.get(k) != doc["snapshot"]["inputs"].get(k))
                p.append(f"{f.name}: stale snapshot (changed: {', '.join(changed)}); run --build")
        seen = set()
        for r in doc["vectors"]:
            n_vec += 1
            if r["card"] in seen:
                p.append(f"{f.name}: duplicate vector {r['card']}")
            seen.add(r["card"])
            e = edh_dict(r.get("edhrec"))
            if e:
                if len(r["edhrec"]) != len(COLS):
                    p.append(f"{f.name}: {r['card']}: EDHREC vector has {len(r['edhrec'])} columns, expected {len(COLS)}")
                    continue
                err = None if "pooled" in e["flags"] else lift_identity(e["lift"], e["synergy"], e["inclusion"])
                bad = err is not None and err > IDENTITY_TOL
                ident_bad += bad
                if bad != ("lift_synergy_inconsistent" in e["flags"]):
                    p.append(f"{f.name}: {r['card']}: lift_synergy_inconsistent flag doesn't match the identity check")
                if abs(e["num_decks"] / e["potential_decks"] - e["inclusion"]) > 1e-5:
                    p.append(f"{f.name}: {r['card']}: inclusion != num_decks / potential_decks")
                if e["confidence"] != ("low" if set(e["flags"]) & LOW_FLAGS else "moderate"):
                    p.append(f"{f.name}: {r['card']}: EDHREC confidence {e['confidence']} (community data: moderate at most, low when flagged)")
            for it in items(doc, r):
                n_items += 1
                for e in ga.validate_file(it, "evidence.schema.json"):
                    p.append(f"{f.name}: {r['card']}: evidence item: {e}")
    if verbose:
        if doc_classes_bad:
            p.append("an evidence file classes EDHREC numbers as something other than derived_metric")
        print(f"evidence: {len(summ)} decks, {n_vec} vectors, {n_items} evidence items; {stale} stale; {ident_bad} EDHREC rows where lift and synergy imply different baselines (flagged, low confidence); {len(p)} problem(s)" + ("" if have_cache else " (no .cache: snapshot freshness not checked)"))
        for x in p[:40]:
            print("  -", x)
    return p


def show(slug, card):
    doc = json.loads((OUT / f"{slug}.json").read_text(encoding="utf-8"))
    r = next(r for r in doc["vectors"] if r["card"].lower() == card.lower())
    print(json.dumps(r, indent=1, ensure_ascii=False))
    print(json.dumps(items(doc, r), indent=1, ensure_ascii=False))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--build", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--decks", default="")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--show", nargs=2, metavar=("SLUG", "CARD"))
    a = ap.parse_args()
    if a.show:
        show(*a.show)
        return 0
    if a.build:
        import evaluate_decklist as ev
        R = ev.Resolver()
        combos = json.loads(COMBOS.read_text(encoding="utf-8"))["decks"]
        summ = ga.summary()
        want = {s.strip() for s in a.decks.split(",") if s.strip()}
        OUT.mkdir(parents=True, exist_ok=True)
        res = {}
        for did, v in sorted(summ.items(), key=lambda kv: kv[1]["slug"]):
            if want and v["slug"] not in want:
                continue
            res[v["slug"]] = build_deck(did, v, R, combos, a.force)
        print(f"evidence --build: {sum(x == 'built' for x in res.values())} built, {sum(x == 'cached' for x in res.values())} unchanged (snapshot cache)")
    if a.check or not (a.build or a.show):
        return 1 if check() else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
