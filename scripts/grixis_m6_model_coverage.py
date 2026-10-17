#!/usr/bin/env python3
"""Flag positive exploratory M5 proxy verdicts as non-decisive for M6.

This is a conservative limitation audit, NOT an inference that a card is bad.
Never alters M5, optimizer votes, approved decks, or canonical authority.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import grixis_authority as ga  # noqa: E402

PACKETS = ROOT / "data/grixis/m6/review_packets"
OUT = ROOT / "data/grixis/m6/model_coverage"
SUMMARY = ROOT / "data/grixis/birthday_m5/summary.json"
NO_DECISION = {"can_decide": False, "can_apply_swap": False, "can_approve_or_lock": False}


def json_text(obj):
    return json.dumps(obj, ensure_ascii=False, indent=1, sort_keys=True) + "\n"


def sha(path):
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def inspect_item(item):
    tests = item.get("test_evidence", {}).get("tests", [])
    limitations = [str(s).casefold() for t in tests for s in t.get("limitations", [])]
    verdicts = [str(t.get("verdict") or "unknown") for t in tests]
    positive = "pass" in verdicts
    unmodeled = any("no effect modelled beyond being a castable card" in s or
                    "no effect modeled beyond being a castable card" in s for s in limitations)
    multiplayer = any("cannot see:" in s and
                      any(k in s for k in ("opponents", "combat", "multiplayer politics", "interaction"))
                      for s in limitations)
    if not positive:
        reason = "M5_exploratory_no_positive_verdict"
    elif unmodeled:
        reason = "M5_goldfish_unmodeled_effects"
    else:
        reason = "M5_goldfish_incomplete_or_unknown_coverage"
    return {
        "swap_id": item["swap_id"],
        "review_order": item["review_order"],
        "test_verdicts": verdicts,
        "has_positive_proxy_verdict": positive,
        "swapped_effects_unmodeled": unmodeled,
        "multiplayer_model_limit": multiplayer,
        "supports_improvement_claim": False,
        "reason": reason,
        "required_next": "Phase-B effect-aware comparisons and named strategic judgment before any improvement claim",
    }


def derive(packet, packet_path):
    items = [inspect_item(x) for x in packet["items"]]
    positive = [x for x in items if x["has_positive_proxy_verdict"]]
    n_unmodeled = sum(x["swapped_effects_unmodeled"] for x in positive)
    doc = {
        "schema_version": 1, "stage": "M6_M5_proxy_coverage_guard",
        "deck_id": packet["deck_id"], "slug": packet["slug"], "list_hash": packet["list_hash"],
        "packet_sha256": sha(packet_path),
        "counts": {"hypotheses": len(items),
                   "positive_proxy_verdicts": len(positive),
                   "positive_unmodeled_swap_effects": n_unmodeled,
                   "positive_other_or_unknown_coverage": len(positive) - n_unmodeled,
                   "claim_eligible_from_M5": 0},
        "items": items, "authority": NO_DECISION
    }
    errs = ga.validate_file(doc, "m6_model_coverage.schema.json")
    if errs:
        raise ValueError("model coverage schema invalid: " + "; ".join(errs[:6]))
    if len({x["swap_id"] for x in items}) != len(items):
        raise ValueError("duplicate review hypotheses")
    return doc


def run(build, check):
    summary = load(SUMMARY)
    expected = {d["slug"] for d in summary["decks"]}
    if len(expected) != 62:
        raise ValueError("M5 source inventory not 62")
    if build:
        OUT.mkdir(parents=True, exist_ok=True)
    counts = Counter()
    detail = []
    for slug in sorted(expected):
        path = PACKETS / (slug + ".json")
        packet = load(path)
        if packet["slug"] != slug or packet["authority"]["can_decide"]:
            raise ValueError("packet authority/slug drift: " + slug)
        doc = derive(packet, path)
        dest = OUT / (slug + ".json")
        if build:
            dest.write_text(json_text(doc), encoding="utf-8")
        if check and (not dest.is_file() or dest.read_text(encoding="utf-8") != json_text(doc)):
            raise ValueError("missing/tampered model coverage: " + slug)
        counts.update(doc["counts"])
        detail.append({"slug": slug, **doc["counts"]})
    top = {
        "schema_version": 1, "stage": "M6_M5_proxy_coverage_aggregate",
        "counts": {"decks": 62, **dict(counts)},
        "policy": {
            "M5_proxy_pass_can_decide": False,
            "M5_proxy_pass_proves_improvement": False,
            "phase_b_and_judgment_required": True,
            "note": "No M5 proxy verdict qualifies alone as improvement evidence even if it is marked pass.",
        },
        "decks": detail,
    }
    if counts["claim_eligible_from_M5"] != 0:
        raise ValueError("forbidden M5 upgrade claim")
    sfile = OUT / "summary.json"
    if build:
        sfile.write_text(json_text(top), encoding="utf-8")
    if check:
        if not sfile.is_file() or sfile.read_text(encoding="utf-8") != json_text(top):
            raise ValueError("aggregate model coverage drift")
        present = {p.stem for p in OUT.glob("*.json")}
        if present != expected | {"summary"}:
            raise ValueError("coverage file set drift")
    print(json.dumps(top["counts"], sort_keys=True))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--build", action="store_true")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    if not (args.build or args.check):
        ap.error("choose --build and/or --check")
    run(args.build, args.check)
