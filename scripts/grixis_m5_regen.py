#!/usr/bin/env python3
"""Cycle 73: regenerate M5 from Step-A saturation and bind every screening review to A–F evidence.

The legacy grixis_candidates engine remains the deterministic screening/swap-hypothesis core. This wrapper:
  * builds from the uncapped Step-A saturated universe;
  * drains both paired_test and escalated_queued work for the completed frozen M5 corpus;
  * leaves every M5 swap exploratory / undecided;
  * adds hash-bound A–F deck context;
  * adds A–F evidence/review obligations to every full screening review and every swap hypothesis;
  * writes a new corpus under data/grixis/m5_regen/candidates, preserving the capped legacy archive;
  * never writes a judgment_review, registered challenger, deck change, approval or lock.

Frozen-development usage:
  SCRYFALL_OFFLINE=1 python scripts/grixis_m5_regen.py --build [--deck slug[,slug]] [--jobs N]
  python scripts/grixis_m5_regen.py --check
  python scripts/grixis_m5_regen.py --summary
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import multiprocessing as mp
import os
import sys
from collections import Counter
from pathlib import Path

os.environ.setdefault("SCRYFALL_OFFLINE", "1")

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import grixis_authority as ga  # noqa: E402
import grixis_candidates as gc  # noqa: E402
import grixis_m5_af as gaf  # noqa: E402

VERSION = 1
CYCLE = 73
OUT = ROOT / "data/grixis/m5_regen/candidates"
SUMMARY = ROOT / "data/grixis/m5_regen/summary.json"
DEV_LOCK = ROOT / "data/grixis/dev_snapshot_lock.json"

# Step-A v3 escalation labels extend the older candidate-review vocabulary. They are preserved verbatim.
SATURATION_ESCALATION_REASONS = (
    "tier_a_score", "dependency_graph_alternative", "spellbook_near_miss_completion", "package_gap", "new_card",
    "unusual_oracle_interaction", "anomaly_source_disagreement", "human_evidence", "tournament_evidence",
    "multi_source_corroboration",
)
ga.ESCALATION_REASONS = tuple(sorted(set(ga.ESCALATION_REASONS) | set(SATURATION_ESCALATION_REASONS)))

_CTX = None


def final_triage(D, keep, sat):
    """Final M5 drains Step-A's ordered escalation queue; screen_only stays screened but unreviewed."""
    esc = {n: sat[n]["escalation"] for n in keep if sat[n]["escalation"]}
    full = [n for n in keep if sat[n]["test_tier"] in ("paired_test", "escalated_queued")]
    return full, esc, []


# grixis_candidates resolves the triage function at runtime; this changes only Cycle-73 wrapper execution.
gc.triage = final_triage


def sha_bytes(b: bytes):
    return "sha256:" + hashlib.sha256(b).hexdigest()


def dump_text(doc):
    return gc.dump(doc)


def write_doc(slug, doc):
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f"{slug}.json.gz").write_bytes(gzip.compress(dump_text(doc).encode("utf-8"), compresslevel=9, mtime=0))


def read_doc(path):
    return json.loads(gzip.decompress(Path(path).read_bytes()).decode("utf-8"))


def files():
    return {p.name[:-8]: p for p in OUT.glob("*.json.gz")}


def base_context():
    return gc._ctx()


def integrate(doc, af):
    """Mutate one freshly generated saturated M5 doc into the A-F-bound Cycle-73 form."""
    swap_by = {sw["id"]: sw for sw in doc["swaps"]}
    sat_ref = f"saturation:data/grixis/saturation/{doc['slug']}.json"
    for rec in doc["candidates"]:
        if rec["escalation"]["escalated"]:
            # The Step-A certificate is itself the provenance for the new escalation vocabulary.
            rec["escalation"]["evidence_refs"] = sorted(set(rec["escalation"]["evidence_refs"] + [sat_ref + "#candidate=" + rec["card"]]))
            rec["escalation"]["by"] = "script:grixis_saturation.py v3; drained by grixis_m5_regen.py"
            rec["escalation"]["note"] = "Step-A saturation escalation; final Cycle-73 M5 drains paired_test and escalated_queued work."
        rv = rec.get("review")
        if not rv:
            continue
        facts = rec.get("screening", {}).get("facts", {})
        hypotheses = []
        ids = []
        if rv.get("swap"):
            ids.append(rv["swap"])
        alt = rv.get("elevated_alternative") or {}
        if alt.get("swap"):
            ids.append(alt["swap"])
        for sid in ids:
            sw = swap_by[sid]
            test_id = sw["tests"][0] if sw.get("tests") else None
            hypotheses.append(af.swap_envelope(sw["cuts"][0], sw["adds"][0], facts, test_id))
        rv["a_f_evidence"] = af.review_envelope(rec["card"], facts, hypotheses)

    afc = af.deck_context()
    doc["a_f_context"] = afc
    doc["triage"]["escalated_queued"] = []
    doc["triage"]["default_rule"] = (
        "Cycle 73 final frozen M5: fully review every Step-A paired_test and escalated_queued candidate in priority order; "
        "screen_only cards remain in the uncapped legal-pool universe but are not promoted to scripted full review."
    )
    doc["universe"]["full_review_rule"] = doc["triage"]["default_rule"]

    old_snapshot = doc["snapshot"]["id"]
    dev = json.loads(DEV_LOCK.read_text(encoding="utf-8"))["snapshot"]
    doc["snapshot"]["development_snapshot"] = dev
    doc["snapshot"]["a_f_digest"] = afc["digest"]
    wrapper_sha = sha_bytes(Path(__file__).read_bytes())
    sid = sha_bytes(json.dumps({
        "legacy_screening_snapshot": old_snapshot,
        "a_f_digest": afc["digest"],
        "wrapper": wrapper_sha,
        "cycle": CYCLE,
    }, sort_keys=True).encode())
    doc["snapshot"]["id"] = sid
    doc["generated_by"] = f"scripts/grixis_m5_regen.py v{VERSION} + grixis_candidates.py v{gc.VERSION}"
    doc["cycle"] = CYCLE
    doc["pass_id"] = f"m5:{doc['slug']}:c{CYCLE}:" + sid[7:19]
    doc["authority"]["note"] += (
        " Cycle 73 regeneration drains Step-A escalations and binds every screening hypothesis to validated A-F "
        "evidence/review obligations. Those envelopes remain non-decision-capable and do not register or promote a challenger."
    )
    return doc


def build_one(slug):
    R, reg, pool, first, almost = _CTX or base_context()
    did, v = next((d, v) for d, v in ga.summary().items() if v["slug"] == slug)
    doc = gc.build_deck(did, v, R, reg, pool, first, almost)
    rid = ga.registry_id(did)
    canonical_hash = reg["decks"][rid]["canonical_project_list"]["hash"]
    af = gaf.DeckAFEvidence(slug, rid, canonical_hash, pool)
    doc = integrate(doc, af)
    write_doc(slug, doc)
    c = doc["counts"]
    return {
        "slug": slug,
        "universe": c["universe"],
        "reviews": c["screening_reviews"],
        "swaps": c["swaps"],
        "tests": c["paired_tests"],
        "af_digest": doc["a_f_context"]["digest"],
    }


def build(only=None, jobs=6):
    global _CTX
    _CTX = base_context()
    want = set(only.split(",")) if only else None
    slugs = sorted(v["slug"] for v in ga.summary().values() if not want or v["slug"] in want)
    OUT.mkdir(parents=True, exist_ok=True)
    rows = []
    if jobs > 1 and len(slugs) > 1:
        with mp.get_context("fork").Pool(jobs) as pool:
            for row in pool.imap(build_one, slugs):
                rows.append(row)
                print(row, flush=True)
    else:
        for slug in slugs:
            row = build_one(slug)
            rows.append(row)
            print(row, flush=True)
    write_summary(rows, partial=bool(want))


def write_summary(rows=None, partial=False):
    if rows is None:
        rows = []
        for slug, path in sorted(files().items()):
            d = read_doc(path)
            rows.append({
                "slug": slug,
                "universe": d["counts"]["universe"],
                "reviews": d["counts"]["screening_reviews"],
                "swaps": d["counts"]["swaps"],
                "tests": d["counts"]["paired_tests"],
                "af_digest": d["a_f_context"]["digest"],
            })
    totals = Counter()
    for r in rows:
        for k in ("universe", "reviews", "swaps", "tests"):
            totals[k] += r[k]
    out = {
        "schema_version": 1,
        "generated_by": f"scripts/grixis_m5_regen.py v{VERSION}",
        "cycle": CYCLE,
        "development_snapshot": json.loads(DEV_LOCK.read_text(encoding="utf-8"))["snapshot"],
        "status": "partial" if partial else "complete_corpus_generated",
        "authority": {
            "can_decide": False,
            "can_approve_or_lock": False,
            "note": "M5 regeneration output is screening evidence only. Cory acceptance is a later explicit milestone and approves no deck."
        },
        "decks": rows,
        "totals": dict(totals),
        "historical_raw_edhrec_required": False,
    }
    SUMMARY.parent.mkdir(parents=True, exist_ok=True)
    SUMMARY.write_text(json.dumps(out, indent=1, sort_keys=True) + "\n", encoding="utf-8")


def semantic_problems(doc):
    p = []
    p.extend(gaf.problems(doc.get("a_f_context", {})))
    if doc.get("cycle") != CYCLE:
        p.append("cycle is not 73")
    if doc.get("universe", {}).get("mode") != "saturation":
        p.append("not a Step-A saturated universe")
    if doc.get("snapshot", {}).get("development_snapshot") != "snap-20261016":
        p.append("wrong frozen development snapshot")
    if doc.get("authority", {}).get("exploratory") is not True:
        p.append("M5 lost exploratory authority")
    if doc.get("triage", {}).get("escalated_queued"):
        p.append("Step-A escalated queue not fully drained")
    swap_ids = {s["id"] for s in doc.get("swaps", [])}
    for c in doc.get("candidates", []):
        rv = c.get("review")
        if c.get("escalation", {}).get("escalated") and not c.get("full_review"):
            p.append(f"{c['card']}: escalated candidate left without final M5 full review")
        if c.get("full_review") and not rv:
            p.append(f"{c['card']}: full review missing")
            continue
        if not rv:
            continue
        af = rv.get("a_f_evidence")
        if not af:
            p.append(f"{c['card']}: full review lacks A-F evidence")
            continue
        if af.get("authority", {}).get("can_decide") is not False or af.get("authority", {}).get("aggregate_score") is not None:
            p.append(f"{c['card']}: A-F review became deciding/scored")
        for h in af.get("hypotheses", []):
            if h.get("F_bracket_stress", {}).get("aggregate_score") is not None:
                p.append(f"{c['card']}: F hypothesis has aggregate score")
            if h.get("F_bracket_stress", {}).get("challenger_status") != "delta_review_required_if_advanced":
                p.append(f"{c['card']}: canonical F evidence was treated as challenger evidence")
            if h.get("E_mechanics", {}).get("route") is None:
                p.append(f"{c['card']}: missing Step-E routing")
        ids = [x for x in (rv.get("swap"), (rv.get("elevated_alternative") or {}).get("swap")) if x]
        if len(af.get("hypotheses", [])) != len(ids):
            p.append(f"{c['card']}: A-F hypothesis count mismatch")
        if any(x not in swap_ids for x in ids):
            p.append(f"{c['card']}: review references missing swap")
    for sw in doc.get("swaps", []):
        if sw.get("decision", {}).get("verdict") is not None or sw.get("state") != "CHALLENGER" or not sw.get("exploratory"):
            p.append(f"{sw.get('id')}: M5 swap became decided/non-exploratory")
    return p


def check(verbose=True):
    probs = []
    summ = ga.summary()
    expected = {v["slug"] for v in summ.values()}
    got = set(files())
    if got != expected:
        probs.append(f"coverage mismatch missing={sorted(expected-got)} extra={sorted(got-expected)}")

    # Reuse the mature structural/schema checker against the regenerated directory, without its expensive rebuild check.
    old_out = gc.OUT
    try:
        gc.OUT = OUT
        probs.extend(gc.check(verbose=False, rebuild=False))
    finally:
        gc.OUT = old_out

    for slug, path in sorted(files().items()):
        doc = read_doc(path)
        probs.extend(f"{slug}: {x}" for x in semantic_problems(doc))

    if SUMMARY.exists():
        s = json.loads(SUMMARY.read_text(encoding="utf-8"))
        if s.get("status") != "complete_corpus_generated" and got == expected:
            probs.append("summary not marked complete despite full coverage")
        if s.get("historical_raw_edhrec_required") is not False:
            probs.append("summary introduced a raw historical EDHREC dependency")
        if s.get("authority", {}).get("can_decide") is not False:
            probs.append("summary became decision-capable")
    else:
        probs.append("summary missing")

    if verbose:
        print(f"m5-regen: {len(got)}/62 decks, {len(probs)} problems")
        for x in probs[:100]:
            print("FAIL", x)
    return probs


def summary():
    totals = Counter()
    route = Counter()
    bracket = Counter()
    rows = 0
    for slug, path in sorted(files().items()):
        d = read_doc(path)
        rows += 1
        c = d["counts"]
        for k in ("universe", "screening_reviews", "swaps", "paired_tests"):
            totals[k] += c[k]
        bracket[d["a_f_context"]["F"]["suite_family"]] += 1
        for cand in d["candidates"]:
            af = (cand.get("review") or {}).get("a_f_evidence") or {}
            for h in af.get("hypotheses", []):
                route[h["E_mechanics"]["route"]["status"]] += 1
    print(json.dumps({"decks": rows, "totals": dict(totals), "E_routes": dict(route), "F_families": dict(bracket)}, indent=2, sort_keys=True))


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
    if a.check:
        sys.exit(1 if check() else 0)
    if a.summary:
        summary()
    if not (a.build or a.check or a.summary):
        ap.print_help()


if __name__ == "__main__":
    main()
