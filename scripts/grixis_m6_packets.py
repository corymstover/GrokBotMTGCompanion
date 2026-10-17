#!/usr/bin/env python3
"""Build deterministic M6 review packets from accepted M5 + independent optimizer evidence.

Packets are triage/preparation only. They do not perform judgment, decide swaps,
edit canonical lists, or change approval/lock state. Priority is categorical and
lexicographic, not a fused power score.
"""
from __future__ import annotations

import argparse
import gzip
import json
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SUMMARY = ROOT / "data/grixis/birthday_m5/summary.json"
REGEN = ROOT / "data/grixis/birthday_m5/regen"
OPT = ROOT / "data/grixis/m6/optimizer"
OUT = ROOT / "data/grixis/m6/review_packets"
OUT_SUMMARY = ROOT / "data/grixis/m6/review_packet_summary.json"
BATCH_SIZE = 20

AUTHORITY = {
    "can_decide": False,
    "can_apply_swap": False,
    "can_write_judgment_review": False,
    "can_approve_or_lock": False,
    "note": "Deterministic triage packet only. A named human or agent must perform M6 strategic judgment; scripts cannot author judgment_review.",
}


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_gz(path: Path) -> Any:
    with gzip.open(path, "rt", encoding="utf-8") as f:
        return json.load(f)


def dump(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def swap_id_from_rec(rec: dict[str, Any]) -> str:
    for ref in rec.get("evidence", []):
        if "#id=swap:" in ref:
            return ref.split("#id=", 1)[1]
    raise ValueError(f"optimizer recommendation missing swap id: {rec}")


def candidate_index(doc: dict[str, Any]) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for c in doc.get("candidates", []):
        if c.get("card"):
            out[c["card"]] = c
    return out


def test_summary(sw: dict[str, Any], tests: dict[str, dict[str, Any]]) -> dict[str, Any]:
    rows = []
    counts = Counter()
    for tid in sw.get("tests", []):
        t = tests.get(tid)
        if not t:
            rows.append({"id": tid, "status": "missing"})
            counts["missing"] += 1
            continue
        v = t.get("verdict")
        counts[v or "unknown"] += 1
        rows.append({
            "id": tid,
            "kind": t.get("kind"),
            "verdict": v,
            "scenario": t.get("scenario"),
            "samples": t.get("samples"),
            "limitations": list(t.get("limitations") or []),
        })
    return {"verdict_counts": dict(counts), "tests": rows}


def af_obligations(candidate: dict[str, Any], add: str, cut: str) -> dict[str, Any]:
    rv = candidate.get("review") or {}
    af = rv.get("a_f_evidence") or {}
    hit = None
    for h in af.get("hypotheses", []):
        if h.get("add") == add and h.get("cut") == cut:
            hit = h
            break
    if not hit:
        return {
            "hypothesis_found": False,
            "commander_review_required": True,
            "structural_route_ids": [],
            "mana_delta_status": "unknown",
            "mana_review_required": False,
            "mechanics_status": "unknown",
            "mechanics_route_status": "unknown",
            "bracket_judgment_prompts": [],
            "combo_review_required": False,
        }
    d = hit.get("D_commander") or {}
    c = hit.get("C_mana") or {}
    e = hit.get("E_mechanics") or {}
    b = hit.get("B_combo_quality") or {}
    f = hit.get("F_bracket_stress") or {}
    prompts = [
        x.get("id") for x in f.get("canonical_stress_obligations", [])
        if x.get("canonical_evidence_status") == "judgment_required" and x.get("id")
    ]
    return {
        "hypothesis_found": True,
        "commander_review_required": bool(d.get("commander_first_review_required", True)),
        "structural_route_ids": list(d.get("cut_structural_route_ids") or []),
        "mana_delta_status": c.get("delta_status"),
        "mana_review_required": bool(c.get("review_required")),
        "mechanics_status": e.get("execution_status"),
        "mechanics_route_status": (e.get("route") or {}).get("status"),
        "bracket_judgment_prompts": prompts,
        "combo_review_required": bool(b.get("review_required")),
    }


def priority_class(source: str, bp_named: bool, flags: set[str]) -> str:
    # Review priority only, never an acceptance ranking.
    if source == "agreement":
        return "P0_independent_agreement"
    if source == "performance_only":
        return "P1_measured_performance_only"
    if bp_named:
        return "P2_commander_named_blueprint_only"
    return "P3_commander_fit_only"


def risk_class(flags: set[str]) -> str:
    if "project_exception_burden" in flags or "structural_route_risk" in flags or "test_fail" in flags:
        return "high_scrutiny"
    if "elevated_burden" in flags or "mechanics_not_modelable" in flags or "explicit_judgment_prompts" in flags:
        return "enhanced_scrutiny"
    return "standard_scrutiny"


def build_one(slug: str) -> tuple[dict[str, Any], Counter]:
    doc = load_gz(REGEN / f"{slug}.json.gz")
    opt = load(OPT / f"{slug}.json")
    swaps = {s["id"]: s for s in doc.get("swaps", [])}
    tests = {t["id"]: t for t in doc.get("tests", []) if t.get("id")}
    cands = candidate_index(doc)

    a = {swap_id_from_rec(r): r for r in opt["pass_a"]["recommendations"]}
    b = {swap_id_from_rec(r): r for r in opt["pass_b"]["recommendations"]}
    deep = list(opt["reconciliation"]["deep_review"])
    if set(deep) != set(a) | set(b):
        raise ValueError(f"{slug}: optimizer deep_review != pass union")

    rows = []
    counts = Counter()
    for sid in deep:
        sw = swaps.get(sid)
        if not sw:
            raise ValueError(f"{slug}: deep-review swap missing from accepted M5: {sid}")
        add = sw.get("adds", [None])[0]
        cut = sw.get("cuts", [None])[0]
        if not add or not cut:
            raise ValueError(f"{slug}: packet builder currently requires 1-for-1 swap: {sid}")
        cand = cands.get(add, {})
        rv = cand.get("review") or {}
        bp = rv.get("blueprint") or {}
        ts = test_summary(sw, tests)
        af = af_obligations(cand, add, cut)
        source = "agreement" if sid in a and sid in b else ("commander_only" if sid in a else "performance_only")
        flags: set[str] = set()
        burden = (sw.get("burden") or {}).get("level")
        if burden == "project_exception": flags.add("project_exception_burden")
        elif burden == "elevated": flags.add("elevated_burden")
        verdicts = ts["verdict_counts"]
        if verdicts.get("pass"): flags.add("test_pass")
        if verdicts.get("fail"): flags.add("test_fail")
        if verdicts.get("inconclusive"): flags.add("test_inconclusive")
        if verdicts.get("no_detectable_difference"): flags.add("test_no_detectable_difference")
        if af["structural_route_ids"]: flags.add("structural_route_risk")
        if af["mechanics_status"] == "judgment_or_other_evidence_required" or af["mechanics_route_status"] == "not_modelable":
            flags.add("mechanics_not_modelable")
        if af["bracket_judgment_prompts"]: flags.add("explicit_judgment_prompts")
        if af["mana_review_required"]: flags.add("mana_delta_required")
        if af["combo_review_required"]: flags.add("combo_review_required")
        if bp.get("anti_goal") is True: flags.add("anti_goal_risk")
        named = bool(bp.get("named_by"))
        pclass = priority_class(source, named, flags)
        rclass = risk_class(flags)
        rows.append({
            "swap_id": sid,
            "source": source,
            "priority_class": pclass,
            "scrutiny": rclass,
            "add": add,
            "cut": cut,
            "base_hash": sw.get("base_hash"),
            "result_hash": sw.get("result_hash"),
            "burden": sw.get("burden"),
            "challenger_class": sw.get("challenger_class"),
            "hypothesis": sw.get("hypothesis"),
            "expected_benefit": sw.get("expected_benefit"),
            "expected_cost": sw.get("expected_cost"),
            "legality": sw.get("legality"),
            "rules_interactions": list(sw.get("rules_interactions") or []),
            "candidate": {
                "rank": cand.get("rank"),
                "tier": cand.get("tier"),
                "screening_score": ((cand.get("screening") or {}).get("score")),
                "blueprint_fit": bp.get("fit"),
                "blueprint_named_by": list(bp.get("named_by") or []),
                "oracle_hook": bp.get("oracle_hook"),
                "screening_review_kind": rv.get("kind"),
                "screening_can_decide": ((rv.get("decision_support") or {}).get("can_decide")),
            },
            "test_evidence": ts,
            "a_f_obligations": af,
            "flags": sorted(flags),
            "refs": {
                "m5_regen": f"data/grixis/birthday_m5/regen/{slug}.json.gz#id={sid}",
                "optimizer": f"data/grixis/m6/optimizer/{slug}.json",
                "blueprint": f"data/grixis/blueprints/{slug}.json",
                "birthday_evidence": f"data/grixis/birthday_m5/evidence/{slug}.json#{add}",
            },
            "required_next": [
                "named_agent_or_human_strategic_judgment",
                "resolve_relevant_A_F_obligations",
                "run_or_bind_required_Phase_B_evidence_before_decision",
            ],
            "authority": AUTHORITY,
        })
        counts[f"source:{source}"] += 1
        counts[f"priority:{pclass}"] += 1
        counts[f"scrutiny:{rclass}"] += 1
        for flag in flags:
            counts[f"flag:{flag}"] += 1

    porder = {
        "P0_independent_agreement": 0,
        "P1_measured_performance_only": 1,
        "P2_commander_named_blueprint_only": 2,
        "P3_commander_fit_only": 3,
    }
    rorder = {"high_scrutiny": 0, "enhanced_scrutiny": 1, "standard_scrutiny": 2}
    rows.sort(key=lambda r: (
        porder[r["priority_class"]], rorder[r["scrutiny"]],
        r["candidate"]["rank"] if r["candidate"]["rank"] is not None else 10**9,
        r["add"].casefold(), r["cut"].casefold(), r["swap_id"],
    ))
    for i, r in enumerate(rows, start=1):
        r["review_order"] = i
        r["batch"] = (i - 1) // BATCH_SIZE + 1

    packet = {
        "schema_version": 1,
        "stage": "M6_strategic_review_packet",
        "deck_id": doc["deck_id"],
        "slug": slug,
        "list_hash": doc["list_hash"],
        "policy": {
            "batch_size": BATCH_SIZE,
            "priority_order": list(porder),
            "scrutiny_order": list(rorder),
            "note": "Priority is categorical/lexicographic triage, not a fused score and not a deckbuilding verdict. All deep-review items remain in the packet.",
        },
        "counts": {
            "deep_review": len(rows),
            "batches": (len(rows) + BATCH_SIZE - 1) // BATCH_SIZE,
            **dict(sorted(counts.items())),
        },
        "items": rows,
        "authority": AUTHORITY,
    }
    return packet, counts


def build() -> None:
    summary = load(SUMMARY)
    if len(summary.get("decks", [])) != 62:
        raise SystemExit("packet builder requires 62-deck accepted M5 summary")
    OUT.mkdir(parents=True, exist_ok=True)
    expected = set()
    all_counts = Counter()
    deck_rows = []
    for d in summary["decks"]:
        slug = d["slug"]
        expected.add(slug)
        packet, counts = build_one(slug)
        dump(OUT / f"{slug}.json", packet)
        all_counts.update(counts)
        deck_rows.append({
            "slug": slug,
            "deck_id": packet["deck_id"],
            "list_hash": packet["list_hash"],
            "deep_review": packet["counts"]["deep_review"],
            "batches": packet["counts"]["batches"],
            "agreements": packet["counts"].get("source:agreement", 0),
            "performance_only": packet["counts"].get("source:performance_only", 0),
            "commander_only": packet["counts"].get("source:commander_only", 0),
        })
    for p in OUT.glob("*.json"):
        if p.stem not in expected:
            p.unlink()
    if len(list(OUT.glob("*.json"))) != 62:
        raise SystemExit("packet coverage is not 62 decks")
    total_deep = sum(x["deep_review"] for x in deck_rows)
    out = {
        "schema_version": 1,
        "stage": "M6_strategic_review_packet_summary",
        "counts": {"decks": 62, "deep_review": total_deep, **dict(sorted(all_counts.items()))},
        "decks": deck_rows,
        "authority": AUTHORITY,
    }
    dump(OUT_SUMMARY, out)
    print(json.dumps(out["counts"], sort_keys=True))


def check() -> None:
    files = sorted(OUT.glob("*.json"))
    if len(files) != 62:
        raise SystemExit(f"review packet coverage {len(files)}/62")
    total = 0
    seen_global = set()
    for p in files:
        d = load(p)
        if d["authority"] != AUTHORITY:
            raise SystemExit(f"{p.name}: authority changed")
        items = d.get("items", [])
        total += len(items)
        local = set()
        orders = []
        for x in items:
            sid = x["swap_id"]
            if sid in local:
                raise SystemExit(f"{p.name}: duplicate {sid}")
            local.add(sid)
            seen_global.add((d["slug"], sid))
            orders.append(x["review_order"])
            if x["authority"] != AUTHORITY or x["candidate"].get("screening_can_decide") not in (False, None):
                raise SystemExit(f"{p.name}: decision authority escaped")
            if not x["required_next"] or "named_agent_or_human_strategic_judgment" not in x["required_next"]:
                raise SystemExit(f"{p.name}: missing judgment gate")
        if orders != list(range(1, len(items) + 1)):
            raise SystemExit(f"{p.name}: non-contiguous review order")
    s = load(OUT_SUMMARY)
    opt = load(ROOT / "data/grixis/m6/optimizer_summary.json")
    if total != opt["counts"]["deep_review"] or total != s["counts"]["deep_review"]:
        raise SystemExit(f"review universe mismatch: packets={total}, optimizer={opt['counts']['deep_review']}, summary={s['counts']['deep_review']}")
    if total != 8848:
        raise SystemExit(f"unexpected accepted optimizer review universe {total}; expected 8848")
    if s["authority"] != AUTHORITY:
        raise SystemExit("summary authority changed")
    print(f"M6 review packet check: PASS (62/62 decks; {total} deep-review leads retained; 0 decisions)")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--build", action="store_true")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    if not (args.build or args.check):
        ap.error("choose --build and/or --check")
    if args.build:
        build()
    if args.check:
        check()


if __name__ == "__main__":
    main()
