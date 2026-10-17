#!/usr/bin/env python3
"""Sealed, commit-separated M6 first passes. Reconcile only after A and B commits.

Unlike cycle 76's simultaneous generator, A receives a blueprint-only projection;
B receives test verdicts/limitations but no blueprint, package, or structural data.
Each pass is generated and committed separately. Reconciliation checks the exact
git blobs and verifies neither pass was modified between the two commits.

This is technical isolation, not a substitute for a genuinely independent
strategic critic. Pass C remains REQUIRED, never auto-accepted by this script.
"""
from __future__ import annotations

import argparse
from collections import Counter
import gzip
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import grixis_authority as ga  # noqa: E402
import grixis_m6_optimizer as previous  # noqa: E402

SUMMARY = ROOT / "data/grixis/birthday_m5/summary.json"
REGISTRY = ROOT / "data/grixis/registry.json"
REGEN = ROOT / "data/grixis/birthday_m5/regen"
OUT = ROOT / "data/grixis/m6/sealed"
MANIFEST = OUT / "reconciliation_manifest.json"
AUTHORITY = {"can_decide": False, "can_apply_swap": False, "can_approve_or_lock": False}


def encode(obj):
    return json.dumps(obj, indent=1, sort_keys=True, ensure_ascii=False) + "\n"


def sha_bytes(data):
    return "sha256:" + hashlib.sha256(data).hexdigest()


def fingerprint(obj):
    return sha_bytes(encode(obj).encode("utf-8"))


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_document(slug):
    with gzip.open(REGEN / (slug + ".json.gz"), "rt", encoding="utf-8") as f:
        return json.load(f)


def summary_rows():
    reg = load(REGISTRY)
    m5 = reg["program"]["milestones"]["M5"]
    if m5.get("status") != "accepted" or m5.get("accepted_by") != "corymstover":
        raise ValueError("M5 acceptance missing")
    s = load(SUMMARY)
    rows = s["decks"]
    if len(rows) != 62 or len({r["slug"] for r in rows}) != 62:
        raise ValueError("unexpected accepted M5 inventory")
    by_slug = {d["slug"]: d for d in reg["decks"].values()}
    if len(by_slug) != 62:
        raise ValueError("registry inventory wrong")
    for row in rows:
        if row["slug"] not in by_slug or row["canonical_hash"] != by_slug[row["slug"]]["current_canonical_hash"]:
            raise ValueError("canonical hash mismatch: " + row["slug"])
    return rows


def project_a(doc):
    """Strict projection: no goldfish, test, meta, EDHREC or tournament fields."""
    candidates = []
    for c in doc.get("candidates", []):
        if not c.get("full_review"):
            continue
        rv = c.get("review") or {}
        bp = rv.get("blueprint") or {}
        af = rv.get("a_f_evidence") or {}
        hypotheses = []
        for h in af.get("hypotheses", []):
            d = h.get("D_commander") or {}
            hypotheses.append({"cut": h.get("cut"), "add": h.get("add"),
                               "D_commander": {"cut_structural_route_ids": d.get("cut_structural_route_ids") or []}})
        candidates.append({
            "card": c.get("card"),
            "full_review": True,
            "review": {
                "swap": rv.get("swap"),
                "elevated_alternative": {"swap": (rv.get("elevated_alternative") or {}).get("swap")},
                "blueprint": {"anti_goal": bp.get("anti_goal"), "named_by": bp.get("named_by") or [],
                              "fit": bp.get("fit")},
                "a_f_evidence": {"hypotheses": hypotheses},
            },
        })
    return {"slug": doc["slug"], "deck_id": doc["deck_id"], "list_hash": doc["list_hash"],
            "candidates": candidates,
            "swaps": [{"id": s["id"], "cuts": s.get("cuts", []), "adds": s.get("adds", [])}
                      for s in doc.get("swaps", [])]}


def project_b(doc):
    """Strict projection: no commander blueprint, hooks, packages or graph."""
    return {"slug": doc["slug"], "deck_id": doc["deck_id"], "list_hash": doc["list_hash"],
            "swaps": [{"id": s["id"], "cuts": s.get("cuts", []), "adds": s.get("adds", []),
                       "tests": s.get("tests", [])} for s in doc.get("swaps", [])],
            "tests": [{"id": t.get("id"), "verdict": t.get("verdict")}
                      for t in doc.get("tests", [])]}


def pass_output(side, doc):
    if side == "A":
        projection = project_a(doc)
        recs = previous.strip_private(previous.commander_recommendations(projection))
        passage = {
            "pass_id": f"m6:{doc['slug']}:commander_first:v{previous.VERSION}",
            "deck_id": doc["deck_id"], "list_hash": doc["list_hash"],
            "optimizer": "commander_first",
            "objective_function": {"id": "commander_first_blueprint_fidelity_v1",
                "family": "blueprint_fidelity", "inputs": previous.CMDR_INPUTS,
                "formula_sha256": previous.sha_text(previous.CMDR_FORMULA)},
            "informed_by": [f"m5:data/grixis/birthday_m5/regen/{doc['slug']}.json.gz"],
            "blind_to": previous.CMDR_BLIND, "recommendations": recs,
        }
    else:
        projection = project_b(doc)
        recs = previous.strip_private(previous.performance_recommendations(projection))
        passage = {
            "pass_id": f"m6:{doc['slug']}:performance:v{previous.VERSION}",
            "deck_id": doc["deck_id"], "list_hash": doc["list_hash"],
            "optimizer": "performance",
            "objective_function": {"id": "measured_paired_test_improvement_v1",
                "family": "measured_performance", "inputs": previous.PERF_INPUTS,
                "formula_sha256": previous.sha_text(previous.PERF_FORMULA)},
            "informed_by": [f"m5:data/grixis/birthday_m5/regen/{doc['slug']}.json.gz"],
            "blind_to": previous.PERF_BLIND, "recommendations": recs,
        }
    return {"schema_version": 1, "side": side, "input_projection_sha256": fingerprint(projection),
            "pass": passage, "scope": "Unreconciled first-pass evidence; not a deck decision.",
            "authority": AUTHORITY}


def path_for(side, slug):
    return OUT / side / (slug + ".json")


def emit(side):
    rows = summary_rows()
    (OUT / side).mkdir(parents=True, exist_ok=True)
    for row in rows:
        doc = load_document(row["slug"])
        if doc["list_hash"] != row["canonical_hash"]:
            raise ValueError("M5 hash mismatch: " + row["slug"])
        path_for(side, row["slug"]).write_text(encode(pass_output(side, doc)), encoding="utf-8")
    actual = {p.stem for p in (OUT / side).glob("*.json")}
    if actual != {r["slug"] for r in rows}:
        raise ValueError("separate first-pass coverage not 62")
    print(f"Pass {side} independently emitted: {len(rows)} sealed-candidate files, no reconciliation")


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def assert_git_seals(a_commit, b_commit):
    if not (len(a_commit) == len(b_commit) == 40) or a_commit == b_commit:
        raise ValueError("distinct A and B commit SHAs required")
    subprocess.run(["git", "merge-base", "--is-ancestor", a_commit, b_commit],
                   cwd=ROOT, check=True)
    a_paths = set(git("diff", "--name-only", a_commit + "^", a_commit).decode().splitlines())
    b_paths = set(git("diff", "--name-only", a_commit, b_commit).decode().splitlines())
    slugs = {r["slug"] for r in summary_rows()}
    expected_a = {f"data/grixis/m6/sealed/A/{slug}.json" for slug in slugs}
    expected_b = {f"data/grixis/m6/sealed/B/{slug}.json" for slug in slugs}
    if a_paths != expected_a or b_paths != expected_b:
        raise ValueError("A/B commits not isolated to exactly 62 separate pass files")
    return slugs


def sealed_record(side, slug, sha):
    rel = str(path_for(side, slug).relative_to(ROOT))
    committed = git("show", sha + ":" + rel)
    disk = path_for(side, slug).read_bytes()
    if committed != disk:
        raise ValueError(f"{slug}: {side} output changed after its commit")
    saved = json.loads(committed)
    expected = pass_output(side, load_document(slug))
    if saved != expected:
        raise ValueError(f"{slug}: {side} not reproducible from its permitted projection")
    return saved, sha_bytes(committed)


def swap_ids(passage):
    found = set()
    for rec in passage["recommendations"]:
        ids = [item.split("#id=", 1)[1] for item in rec["evidence"] if "#id=" in item and item.startswith("m5_swap:")]
        if len(ids) != 1:
            raise ValueError("recommendation must cite exactly one accepted-M5 swap ID")
        if ids[0] in found:
            raise ValueError("duplicate swap recommendation")
        found.add(ids[0])
    return found


def compute_manifest(a_commit, b_commit):
    slugs = assert_git_seals(a_commit, b_commit)
    lines = []
    total = Counter()
    for row in summary_rows():
        slug = row["slug"]
        if slug not in slugs:
            raise ValueError("missing deck")
        a, a_hash = sealed_record("A", slug, a_commit)
        b, b_hash = sealed_record("B", slug, b_commit)
        x, y = a["pass"], b["pass"]
        problems = ga.check_reconciliation(x, y)
        if problems:
            raise ValueError(slug + ": " + str(problems))
        xs, ys = swap_ids(x), swap_ids(y)
        both = xs & ys
        disagree = xs ^ ys
        total.update({"agreements": len(both), "disagreements": len(disagree),
                      "deep_review": len(xs | ys)})
        lines.append({"slug": slug, "deck_id": row["slug"].replace("-", "_") if False else x["deck_id"],
                      "list_hash": row["canonical_hash"], "a_sha256": a_hash, "b_sha256": b_hash,
                      "agreements": len(both), "disagreements": len(disagree),
                      "deep_review": len(xs | ys)})
    obj = {"schema_version": 1, "stage": "M6_A_B_commit_then_reveal",
           "pass_a_commit": a_commit, "pass_b_commit": b_commit,
           "passes": lines, "counts": {"decks": 62, **dict(total)},
           "pass_c": {"complete": False, "status": "awaiting_named_critic",
                      "model_limited_positive_tests_decisive": False},
           "authority": AUTHORITY}
    if obj["counts"]["deep_review"] != 8848:
        raise ValueError("new sealed pass universe drift; deliberate investigation required")
    errs = ga.validate_file(obj, "m6_sealed_reconciliation.schema.json")
    if errs:
        raise ValueError("manifest schema errors: " + "; ".join(errs[:7]))
    return obj


def main():
    ap = argparse.ArgumentParser()
    modes = ap.add_mutually_exclusive_group(required=True)
    modes.add_argument("--emit-a", action="store_true")
    modes.add_argument("--emit-b", action="store_true")
    modes.add_argument("--reconcile", action="store_true")
    modes.add_argument("--check", action="store_true")
    ap.add_argument("--a-commit")
    ap.add_argument("--b-commit")
    a = ap.parse_args()
    if a.emit_a or a.emit_b:
        emit("A" if a.emit_a else "B")
        return
    if a.reconcile:
        if not a.a_commit or not a.b_commit:
            ap.error("reconciliation requires both sealed commit SHAs")
        obj = compute_manifest(a.a_commit, a.b_commit)
        MANIFEST.write_text(encode(obj), encoding="utf-8")
        print("A/B sealed and reconciled:", obj["counts"], "; Pass C still pending")
    if a.check:
        if not MANIFEST.exists():
            raise ValueError("sealed manifest missing")
        saved = load(MANIFEST)
        expected = compute_manifest(saved["pass_a_commit"], saved["pass_b_commit"])
        if saved != expected:
            raise ValueError("sealed manifest drift")
        print("A/B immutable commits verified; Pass C still not complete", expected["counts"])


if __name__ == "__main__":
    main()
