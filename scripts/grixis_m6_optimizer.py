#!/usr/bin/env python3
"""Build M6 independent optimizer-pass evidence from accepted Birthday M5 artifacts.

Authority boundary:
- reads accepted M5 evidence only;
- does not edit canonical decklists, challengers, approvals, or lock state;
- recommendations are evidence for M6 judgment review, not decisions.

The first passes are intentionally different algorithms, not alternate weights of one score:
A) commander_first: blueprint fidelity / identity preservation only. It is blind to
   goldfish, stress, EDHREC, tournament and other performance metrics.
B) performance: measured paired-test improvement only. It is blind to blueprint,
   packages, identity-core, dependency-graph and interaction-review inputs.
They are reconciled only after both passes are complete.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REGEN = ROOT / "data/grixis/birthday_m5/regen"
SUMMARY = ROOT / "data/grixis/birthday_m5/summary.json"
REGISTRY = ROOT / "data/grixis/registry.json"
OUT = ROOT / "data/grixis/m6/optimizer"
OUT_SUMMARY = ROOT / "data/grixis/m6/optimizer_summary.json"

import sys
sys.path.insert(0, str(ROOT / "scripts"))
import grixis_authority as ga  # noqa: E402

DATE = "2026-10-17"
VERSION = 1

CMDR_FORMULA = (
    "commander_first_v1: for each accepted-M5 full-review swap linked to a candidate; "
    "reject anti-goal candidates; require strong blueprint fit or explicit blueprint named_by; "
    "reject hypotheses whose D_commander cut_structural_route_ids is nonempty; "
    "sort deterministically by explicit-named fit, strong fit, add, cut, swap id. "
    "No performance/community metric is read."
)
PERF_FORMULA = (
    "performance_v1: for each accepted-M5 swap with a paired test; recommend only when at least "
    "one referenced test verdict is pass and none is fail; sort deterministically by number of pass "
    "verdicts then add, cut, swap id. No blueprint/package/identity/dependency input is read."
)

CMDR_INPUTS = ["blueprint", "oracle_hooks", "packages", "identity_core"]
PERF_INPUTS = ["goldfish", "simulator"]
CMDR_BLIND = ["simulator", "goldfish", "stress", "edhrec_inclusion", "edhrec_lift", "edhrec_rank", "tournament", "mana_efficiency", "hypergeometric"]
PERF_BLIND = ["blueprint", "oracle_hooks", "packages", "dependency_graph", "identity_core", "anti_goals", "interaction_review"]


def sha_text(s: str) -> str:
    return "sha256:" + hashlib.sha256(s.encode("utf-8")).hexdigest()


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_gz(path: Path) -> Any:
    with gzip.open(path, "rt", encoding="utf-8") as f:
        return json.load(f)


def dump(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def m5_accepted() -> None:
    reg = load(REGISTRY)
    m5 = reg["program"]["milestones"]["M5"]
    if m5.get("status") != "accepted" or m5.get("accepted_by") != "corymstover":
        raise SystemExit("M6 optimizer blocked: M5 is not explicitly accepted by Cory")


def candidate_swap_records(doc: dict[str, Any]) -> dict[str, tuple[dict[str, Any], dict[str, Any]]]:
    """Map swap id -> (candidate, review) for M5 full-review records."""
    out: dict[str, tuple[dict[str, Any], dict[str, Any]]] = {}
    for cand in doc.get("candidates", []):
        if not cand.get("full_review"):
            continue
        rv = cand.get("review") or {}
        for sid in (rv.get("swap"), (rv.get("elevated_alternative") or {}).get("swap")):
            if sid:
                out.setdefault(sid, (cand, rv))
    return out


def commander_structural_break(rv: dict[str, Any], cut: str, add: str) -> bool:
    af = rv.get("a_f_evidence") or {}
    for hyp in af.get("hypotheses", []):
        if hyp.get("cut") != cut or hyp.get("add") != add:
            continue
        d = hyp.get("D_commander") or {}
        if d.get("cut_structural_route_ids"):
            return True
    return False


def commander_recommendations(doc: dict[str, Any]) -> list[dict[str, Any]]:
    linked = candidate_swap_records(doc)
    recs = []
    source = f"data/grixis/birthday_m5/regen/{doc['slug']}.json.gz"
    blueprint = f"data/grixis/blueprints/{doc['slug']}.json"
    for sw in doc.get("swaps", []):
        sid = sw.get("id")
        pair = linked.get(sid)
        if not pair or len(sw.get("cuts", [])) != 1 or len(sw.get("adds", [])) != 1:
            continue
        cand, rv = pair
        bp = rv.get("blueprint") or {}
        if bp.get("anti_goal") is True:
            continue
        named = list(bp.get("named_by") or [])
        strong = bp.get("fit") == "strong"
        if not named and not strong:
            continue
        cut, add = sw["cuts"][0], sw["adds"][0]
        if commander_structural_break(rv, cut, add):
            continue
        recs.append({
            "cut": cut,
            "add": add,
            "evidence": [
                f"m5_candidate:{source}#card={cand['card']}",
                f"m5_swap:{source}#id={sid}",
                f"blueprint:{blueprint}",
            ],
            "_sort": (0 if named else 1, 0 if strong else 1, add.casefold(), cut.casefold(), sid),
            "_sid": sid,
        })
    recs.sort(key=lambda r: r["_sort"])
    return recs


def performance_recommendations(doc: dict[str, Any]) -> list[dict[str, Any]]:
    tests = {t.get("id"): t for t in doc.get("tests", []) if t.get("id")}
    recs = []
    source = f"data/grixis/birthday_m5/regen/{doc['slug']}.json.gz"
    for sw in doc.get("swaps", []):
        if len(sw.get("cuts", [])) != 1 or len(sw.get("adds", [])) != 1:
            continue
        verdicts = [tests[t]["verdict"] for t in sw.get("tests", []) if t in tests]
        if not verdicts or "fail" in verdicts or "pass" not in verdicts:
            continue
        cut, add = sw["cuts"][0], sw["adds"][0]
        ev = [f"m5_swap:{source}#id={sw['id']}"]
        ev.extend(f"m5_test:{source}#id={tid}" for tid in sw.get("tests", []) if tid in tests)
        recs.append({
            "cut": cut,
            "add": add,
            "evidence": ev,
            "_sort": (-verdicts.count("pass"), add.casefold(), cut.casefold(), sw["id"]),
            "_sid": sw["id"],
        })
    recs.sort(key=lambda r: r["_sort"])
    return recs


def strip_private(recs: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [{k: v for k, v in r.items() if not k.startswith("_")} for r in recs]


def build_one(doc: dict[str, Any]) -> tuple[dict[str, Any], dict[str, int]]:
    cm = commander_recommendations(doc)
    pf = performance_recommendations(doc)
    cm_ids = {r["_sid"] for r in cm}
    pf_ids = {r["_sid"] for r in pf}
    agreements = sorted(cm_ids & pf_ids)
    disagreements = sorted(cm_ids ^ pf_ids)
    # Every first-pass recommendation still needs M6 strategic judgment, even when both
    # independent passes agree. Agreement is not approval authority.
    deep_review = sorted(cm_ids | pf_ids)

    pass_a_id = f"m6:{doc['slug']}:commander_first:v{VERSION}"
    pass_b_id = f"m6:{doc['slug']}:performance:v{VERSION}"
    artifact = {
        "schema_version": 1,
        "pass_a": {
            "pass_id": pass_a_id,
            "deck_id": doc["deck_id"],
            "list_hash": doc["list_hash"],
            "optimizer": "commander_first",
            "objective_function": {
                "id": "commander_first_blueprint_fidelity_v1",
                "family": "blueprint_fidelity",
                "inputs": CMDR_INPUTS,
                "formula_sha256": sha_text(CMDR_FORMULA),
            },
            "informed_by": [f"m5:data/grixis/birthday_m5/regen/{doc['slug']}.json.gz"],
            "blind_to": CMDR_BLIND,
            "recommendations": strip_private(cm),
        },
        "pass_b": {
            "pass_id": pass_b_id,
            "deck_id": doc["deck_id"],
            "list_hash": doc["list_hash"],
            "optimizer": "performance",
            "objective_function": {
                "id": "measured_paired_test_improvement_v1",
                "family": "measured_performance",
                "inputs": PERF_INPUTS,
                "formula_sha256": sha_text(PERF_FORMULA),
            },
            "informed_by": [f"m5:data/grixis/birthday_m5/regen/{doc['slug']}.json.gz"],
            "blind_to": PERF_BLIND,
            "recommendations": strip_private(pf),
        },
        "reconciliation": {
            "agreements": agreements,
            "disagreements": disagreements,
            "deep_review": deep_review,
            "date": DATE,
        },
    }
    probs = ga.check_reconciliation(artifact["pass_a"], artifact["pass_b"])
    if probs:
        raise ValueError(f"{doc['slug']}: optimizer independence failure: {probs}")
    counts = {
        "commander_first": len(cm),
        "performance": len(pf),
        "agreements": len(agreements),
        "disagreements": len(disagreements),
        "deep_review": len(deep_review),
    }
    return artifact, counts


def build() -> None:
    m5_accepted()
    summary = load(SUMMARY)
    if len(summary.get("decks", [])) != 62:
        raise SystemExit("M6 optimizer requires accepted 62-deck M5 summary")
    rows = []
    total = Counter()
    OUT.mkdir(parents=True, exist_ok=True)
    expected = set()
    for row in summary["decks"]:
        slug = row["slug"]
        expected.add(slug)
        doc = load_gz(REGEN / f"{slug}.json.gz")
        if doc.get("list_hash") != row.get("canonical_hash"):
            raise SystemExit(f"{slug}: M5 summary/regen hash mismatch")
        artifact, counts = build_one(doc)
        dump(OUT / f"{slug}.json", artifact)
        rows.append({"slug": slug, "deck_id": doc["deck_id"], "list_hash": doc["list_hash"], **counts})
        total.update(counts)
    for p in OUT.glob("*.json"):
        if p.stem not in expected:
            p.unlink()
    if len(list(OUT.glob("*.json"))) != 62:
        raise SystemExit("optimizer output coverage is not 62 decks")
    out = {
        "schema_version": 1,
        "stage": "M6_independent_optimizer_reconciliation",
        "date": DATE,
        "formulae": {
            "commander_first": {"text": CMDR_FORMULA, "sha256": sha_text(CMDR_FORMULA)},
            "performance": {"text": PERF_FORMULA, "sha256": sha_text(PERF_FORMULA)},
        },
        "counts": {"decks": 62, **dict(total)},
        "decks": rows,
        "authority": {
            "can_decide": False,
            "can_apply_swap": False,
            "can_approve_or_lock": False,
            "note": "Independent optimizer/reconciliation evidence only. Every recommendation in deep_review still requires M6 strategic judgment and downstream gates.",
        },
    }
    dump(OUT_SUMMARY, out)
    print(json.dumps(out["counts"], sort_keys=True))


def check() -> None:
    m5_accepted()
    files = sorted(OUT.glob("*.json"))
    if len(files) != 62:
        raise SystemExit(f"optimizer coverage {len(files)}/62")
    for p in files:
        d = load(p)
        for side in ("pass_a", "pass_b"):
            ps = d[side]
            if ps["list_hash"] != d["pass_a"]["list_hash"]:
                raise SystemExit(f"{p.name}: pass hash disagreement")
            for rec in ps["recommendations"]:
                if rec["cut"] is None or rec["add"] is None or not rec["evidence"]:
                    raise SystemExit(f"{p.name}: malformed recommendation")
        probs = ga.check_reconciliation(d["pass_a"], d["pass_b"])
        if probs:
            raise SystemExit(f"{p.name}: {probs}")
        union = set(d["reconciliation"]["agreements"]) | set(d["reconciliation"]["disagreements"])
        if set(d["reconciliation"]["deep_review"]) != union:
            raise SystemExit(f"{p.name}: every reconciled recommendation must remain deep_review")
    s = load(OUT_SUMMARY)
    if s["counts"]["decks"] != 62 or s["authority"]["can_decide"] or s["authority"]["can_approve_or_lock"]:
        raise SystemExit("optimizer summary authority/coverage failure")
    if s["formulae"]["commander_first"]["sha256"] == s["formulae"]["performance"]["sha256"]:
        raise SystemExit("optimizer formulas unexpectedly identical")
    print("M6 independent optimizer check: PASS (62/62; reconciliation preserved; no decision authority)")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--build", action="store_true")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    if not (a.build or a.check):
        ap.error("choose --build and/or --check")
    if a.build:
        build()
    if a.check:
        check()


if __name__ == "__main__":
    main()
