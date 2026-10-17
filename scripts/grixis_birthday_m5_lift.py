#!/usr/bin/env python3
"""Cycle 74b: current-EDHREC correction for the fresh Birthday M5 runner.

The frozen M5 scorer intentionally remains untouched on its frozen branch. This
wrapper changes only the Birthday/current evidence path:

* EDHREC Lift is the current commander-page association metric; retired Synergy
  is not consumed by fresh screening or review evidence.
* The historical M5 workload calibration is preserved with a Lift-derived
  association differential: lift_delta = inclusion - inclusion / lift. This is
  the same unit as an inclusion-rate difference, is centered at lift=1, and is
  derived entirely from current Lift + current inclusion. It is a workload
  heuristic, never a quality verdict or decision authority.
* Fresh EDHREC derivative rows keep the legacy `synergy` column position only for
  schema compatibility and set its value to null. Raw source bytes remain in
  birthday_authority/edhrec_current.json.gz for provenance.
* Mature candidate-review evidence references are rebound from the frozen M3
  evidence directory to the fresh Birthday derivative directory.
* Summary/delta/provenance explicitly record the metric policy and validation
  fails if a fresh derivative or screening fact leaks a numeric Synergy value,
  or if a current candidate review cites the frozen EDHREC evidence path.

This file delegates all authority, saturation, A-F integration, tournament
convergence, delta, and non-decision invariants to grixis_birthday_m5.py.
"""
from __future__ import annotations

import gzip
import json
from pathlib import Path

import grixis_birthday_m5 as bm

VERSION = 2
METRIC_POLICY = {
    "current_metric": "lift",
    "retired_metric_used": False,
    "screening_transform": "lift_delta = inclusion - inclusion/lift; association points = 25 * clamp(lift_delta/0.25, -1, 1)",
    "inclusion_component": "35 * min(1, inclusion/0.40)",
    "purpose": "candidate workload ordering only; Lift and inclusion are derived/community evidence and never decide a swap",
    "source_method": "EDH Lift and Synergy.md; commander/tag/combo pages moved from Synergy to Lift on 2026-10-01",
}

_orig_screen = bm.gc.screen
_orig_full_review = bm.gc.full_review
_orig_esc_refs = bm.gc.esc_refs
_orig_build_delta = bm.build_delta
_orig_build_summary = bm.build_summary
_orig_semantic_problems = bm.semantic_problems
_orig_integrate_doc = bm.integrate_doc


def _r(x, n):
    return None if x is None else round(x, n)


def _lift_delta(inclusion, lift):
    if inclusion is None or lift is None or lift <= 0:
        return None
    return inclusion - inclusion / lift


def _edh_row_lift(views, method):
    """M3-compatible vector using current Lift; retired Synergy is always null."""
    if not views:
        return None
    flags = []
    n = sum(v.get("num_decks", 0) for v in views)
    pd = sum(v.get("potential_decks", 0) for v in views)
    if pd <= 0:
        return None

    def weighted(key):
        if any(v.get(key) is None for v in views):
            return None
        return sum(v[key] * v["potential_decks"] for v in views) / pd

    if len(views) == 1:
        v = views[0]
        inclusion = v["num_decks"] / v["potential_decks"]
        lift = v.get("lift")
        trend = v.get("trend_zscore")
        if method == "pooled":
            flags.append("one_page_of_pool")
    else:
        inclusion = n / pd
        lift = weighted("lift")
        trend = weighted("trend_zscore")
        flags.append("pooled")

    if pd < bm.ge.SMALL_SAMPLE or n < bm.ge.FEW_DECKS:
        flags.append("small_sample")
    if trend is not None and trend >= bm.ge.TREND_Z:
        flags.append("rising")
    if trend is not None and trend <= -bm.ge.TREND_Z:
        flags.append("falling")
    conf = "low" if set(flags) & {"small_sample", "pooled", "one_page_of_pool"} else "moderate"
    # ge.COLS = lift, synergy, inclusion, num_decks, potential_decks,
    # trend_zscore, confidence, flags. The retired field is intentionally null.
    return [_r(lift, 3), None, _r(inclusion, 5), n, pd, _r(trend, 3), conf, flags]


def prepare_evidence_lift(m):
    current = bm.read_gz_json(bm.EDH_CURRENT)
    snap = m["snapshot_id"]
    bm.EVID.mkdir(parents=True, exist_ok=True)
    counts = {"decks": 0, "vectors": 0, "with_lift": 0, "without_lift": 0}
    for slug, d in sorted(current["decks"].items()):
        pages = d.get("pages", [])
        method = d.get("method", "single_page")
        by = {}
        for page in pages:
            for name, row in page.get("rows", {}).items():
                if not row.get("potential_decks"):
                    continue
                by.setdefault(name, []).append(row)
        vecs = []
        canon = bm.canonical_names(slug)
        for name in sorted(by):
            row = _edh_row_lift(by[name], method)
            if row is not None:
                vecs.append({"card": name, "status": "incumbent" if name in canon else "candidate", "edhrec": row})
                counts["with_lift" if row[0] is not None else "without_lift"] += 1
        page_meta = [{"page": x.get("page"), "sha256": x.get("sha256"), "retrieved": current.get("retrieved")} for x in pages]
        payload = {
            "schema_version": 1,
            "deck_id": d.get("deck_id"),
            "slug": slug,
            "generated_by": f"scripts/grixis_birthday_m5_lift.py v{VERSION}",
            "cycle": "ChatGPT cycle 74b",
            "date": bm.TODAY.isoformat(),
            "edhrec": {
                "pages": page_meta,
                "method": method,
                "class": "derived_metric",
                "columns": bm.ge.COLS,
                "current_metric": "lift",
                "retired_synergy_policy": "column retained for schema compatibility; every fresh derivative value is null and is not used in screening",
                "note": "Fresh Birthday EDHREC derivative. Lift is current association evidence; inclusion/Lift order workload only and never decide.",
            },
            "snapshot": {
                "id": bm.sha_bytes(json.dumps({"birthday": snap, "pages": page_meta, "metric": "lift", "wrapper_version": VERSION}, sort_keys=True).encode()),
                "birthday_authority": snap,
                "source_artifact": bm.rel(bm.EDH_CURRENT),
                "source_sha256": bm.sha_file(bm.EDH_CURRENT),
            },
            "counts": {"vectors": len(vecs), "with_edhrec": len(vecs)},
            "vectors": vecs,
        }
        (bm.EVID / f"{slug}.json").write_text(json.dumps(payload, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
        counts["decks"] += 1
        counts["vectors"] += len(vecs)
    if counts["decks"] != 62:
        raise SystemExit(f"fresh Lift evidence coverage {counts['decks']}/62")
    return counts


def screen_lift(D, name, card, src):
    """Run the mature structural scorer, replacing only its retired EDHREC term."""
    score, parts, facts = _orig_screen(D, name, card, src)
    er = D.edh.get(name)
    if er and name in D.ev_cands:
        old = parts.get("edhrec", 0.0)
        inc, lift = er.get("inclusion"), er.get("lift")
        ld = _lift_delta(inc, lift)
        assoc = 0.0 if ld is None else ld
        fresh = round(35 * min(1.0, inc / 0.40) + 25 * max(-1.0, min(1.0, assoc / 0.25)), 2)
        parts["edhrec"] = fresh
        facts["edhrec"] = {
            "metric": "lift",
            "inclusion": inc,
            "lift": lift,
            "lift_delta": _r(ld, 5),
            "num_decks": er.get("num_decks"),
            "potential_decks": er.get("potential_decks"),
            "confidence": er.get("confidence"),
            "flags": er.get("flags", []),
        }
        score = round(score - old + fresh, 2)
    return score, parts, facts


def _fresh_ref_prefix(slug):
    return "evidence:" + bm.rel(bm.EVID / f"{slug}.json")


def _rewrite_ref(x, slug):
    old = f"evidence:data/grixis/evidence/{slug}.json"
    new = _fresh_ref_prefix(slug)
    if isinstance(x, str):
        return x.replace(old, new)
    if isinstance(x, list):
        return [_rewrite_ref(v, slug) for v in x]
    if isinstance(x, tuple):
        return tuple(_rewrite_ref(v, slug) for v in x)
    if isinstance(x, dict):
        return {k: _rewrite_ref(v, slug) for k, v in x.items()}
    return x


def full_review_lift(D, n, c, sc, parts, facts, R):
    rv, cut, items, alt = _orig_full_review(D, n, c, sc, parts, facts, R)
    return _rewrite_ref(rv, D.slug), cut, _rewrite_ref(items, D.slug), alt


def esc_refs_lift(D, n, reasons, facts):
    return _rewrite_ref(_orig_esc_refs(D, n, reasons, facts), D.slug)


def integrate_doc_lift(doc, af, m):
    doc = _orig_integrate_doc(doc, af, m)
    doc["snapshot"]["edhrec_current_metric"] = "lift"
    doc["snapshot"]["edhrec_retired_synergy_used"] = False
    doc["generated_by"] = f"scripts/grixis_birthday_m5_lift.py v{VERSION} -> " + doc["generated_by"]
    return doc


def build_delta_lift(m, convergence, before_frozen):
    d = _orig_build_delta(m, convergence, before_frozen)
    d["screening_metric_policy"] = METRIC_POLICY
    bm.DELTA.write_text(json.dumps(d, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    return d


def build_summary_lift(m, delta, convergence, evid_counts, before_frozen):
    s = _orig_build_summary(m, delta, convergence, evid_counts, before_frozen)
    s["edhrec_metric_policy"] = METRIC_POLICY
    s["generated_by"] = f"scripts/grixis_birthday_m5_lift.py v{VERSION} -> scripts/grixis_birthday_m5.py v{bm.VERSION}"
    bm.SUMMARY.write_text(json.dumps(s, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")

    p = json.loads(bm.PROVENANCE.read_text(encoding="utf-8"))
    p["edhrec_metric_policy"] = METRIC_POLICY
    p["metric_patch"] = {"file": bm.rel(Path(__file__)), "sha256": bm.sha_file(Path(__file__))}
    p["outputs"]["summary"] = bm.sha_file(bm.SUMMARY)
    p["outputs"]["delta"] = bm.sha_file(bm.DELTA)
    bm.PROVENANCE.write_text(json.dumps(p, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    return s


def semantic_problems_lift(m):
    probs = _orig_semantic_problems(m)
    for p in sorted(bm.EVID.glob("*.json")):
        d = json.loads(p.read_text(encoding="utf-8"))
        cols = d.get("edhrec", {}).get("columns", [])
        if d.get("edhrec", {}).get("current_metric") != "lift":
            probs.append(f"{p.name}: fresh EDHREC metric is not Lift")
        if "synergy" not in cols:
            probs.append(f"{p.name}: compatibility synergy column unexpectedly absent")
            continue
        si = cols.index("synergy")
        for v in d.get("vectors", []):
            row = v.get("edhrec")
            if row and row[si] is not None:
                probs.append(f"{p.name}/{v.get('card')}: retired Synergy leaked into fresh derivative")
                break
    for p in sorted(bm.CANDS.glob("*.json.gz")):
        slug = p.name[:-8]
        raw = gzip.decompress(p.read_bytes()).decode("utf-8")
        if f"evidence:data/grixis/evidence/{slug}.json" in raw:
            probs.append(f"{p.name}: current candidate review cites frozen EDHREC evidence")
    for p in sorted(bm.REGEN.glob("*.json.gz")):
        d = json.loads(gzip.decompress(p.read_bytes()).decode("utf-8"))
        if d.get("snapshot", {}).get("edhrec_current_metric") != "lift" or d.get("snapshot", {}).get("edhrec_retired_synergy_used") is not False:
            probs.append(f"{p.name}: regenerated deck lacks Lift policy binding")
        for c in d.get("candidates", []):
            e = ((c.get("screening") or {}).get("facts") or {}).get("edhrec")
            if e and (e.get("metric") != "lift" or e.get("synergy") is not None):
                probs.append(f"{p.name}/{c.get('card')}: screening fact is not Lift-only")
                break
    if bm.SUMMARY.exists():
        s = json.loads(bm.SUMMARY.read_text(encoding="utf-8"))
        if s.get("edhrec_metric_policy", {}).get("current_metric") != "lift":
            probs.append("summary missing current Lift policy")
    if bm.DELTA.exists():
        d = json.loads(bm.DELTA.read_text(encoding="utf-8"))
        if d.get("screening_metric_policy", {}).get("retired_metric_used") is not False:
            probs.append("delta does not attest retired Synergy is unused")
    return probs


def install():
    bm.prepare_evidence = prepare_evidence_lift
    bm.gc.screen = screen_lift
    bm.gc.full_review = full_review_lift
    bm.gc.esc_refs = esc_refs_lift
    bm.integrate_doc = integrate_doc_lift
    bm.build_delta = build_delta_lift
    bm.build_summary = build_summary_lift
    bm.semantic_problems = semantic_problems_lift
    bm.gc.SCREEN_RULES = [
        "Birthday EDHREC: 35 x min(1, inclusion / 0.40) + 25 x clamp(lift_delta / 0.25, -1, 1), where lift_delta = inclusion - inclusion/lift (current Lift; derived_metric; workload only)",
        *[x for x in bm.gc.SCREEN_RULES if not x.startswith("edhrec:")],
    ]
    bm.gc.ESCALATION_RULES = dict(bm.gc.ESCALATION_RULES)
    bm.gc.ESCALATION_RULES["rank_miss_suspected"] = "current Lift/inclusion anomaly or a blueprint-named candidate ranked outside the default set; workload signal only"


if __name__ == "__main__":
    install()
    raise SystemExit(bm.main())
