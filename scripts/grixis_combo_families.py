#!/usr/bin/env python3
"""Step B: synthesize Commander Spellbook lines into redundancy/variant families.

This is evidence organization, not a combo verdict. A family is a connected component under the same near-variant
relation already used by the Combo Quality Model: two lines are adjacent when they share all but roughly one piece.
Connected components can be transitive, so a family is a redundancy network, not a claim that every line is strategically
identical. Final primary/secondary/backup/incidental/value-loop classifications remain judgment work.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, deque
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CQ = ROOT / "data" / "grixis" / "combo_quality"
LS = ROOT / "data" / "grixis" / "combo_line_semantics"
PC = ROOT / "data" / "grixis" / "power_core"
REGISTRY = ROOT / "data" / "grixis" / "registry.json"
OUT = ROOT / "data" / "grixis" / "combo_families"
SCHEMA = ROOT / "data" / "grixis" / "schemas" / "combo_family.schema.json"
VERSION = 1


def load(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def dump(p, obj):
    p = Path(p)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def near(a, b):
    """Same transparent near-variant relation as grixis_combo_quality.near_variants."""
    aa, bb = set(a), set(b)
    if not aa or not bb:
        return False
    needed = max(1, min(len(aa), len(bb)) - 1)
    return len(aa & bb) >= needed


def components(lines):
    """Return deterministic connected components of line records under near()."""
    rows = sorted(lines, key=lambda x: x["id"])
    adj = {x["id"]: set() for x in rows}
    by_id = {x["id"]: x for x in rows}
    for i, a in enumerate(rows):
        for b in rows[i + 1:]:
            if near(a.get("cards") or [], b.get("cards") or []):
                adj[a["id"]].add(b["id"])
                adj[b["id"]].add(a["id"])
    seen, out = set(), []
    for root in sorted(adj):
        if root in seen:
            continue
        q, ids = deque([root]), []
        seen.add(root)
        while q:
            cur = q.popleft(); ids.append(cur)
            for nxt in sorted(adj[cur]):
                if nxt not in seen:
                    seen.add(nxt); q.append(nxt)
        out.append([by_id[x] for x in sorted(ids)])
    return out


def count_hints(lines, key):
    c = Counter()
    for x in lines:
        v = x.get("classification", {}).get(key)
        if v:
            c[v] += 1
    return dict(sorted(c.items()))


def build_family(slug, index, lines, sem_by_id, pc_ids):
    ids = sorted(x["id"] for x in lines)
    card_sets = [set(x.get("cards") or []) for x in lines]
    common = sorted(set.intersection(*card_sets)) if card_sets else []
    union = sorted(set.union(*card_sets)) if card_sets else []
    endpoint = Counter()
    stack = []
    declared_mana = 0
    missing_steps = 0
    direct_endpoint_lines = 0
    for cid in ids:
        s = sem_by_id.get(cid)
        if not s:
            missing_steps += 1
            continue
        if not s.get("record_found"):
            missing_steps += 1
        if s.get("raw", {}).get("mana_needed"):
            declared_mana += 1
        hints = s.get("derived", {}).get("endpoint_hints") or []
        endpoint.update(hints)
        if any(h in ("damage", "life_loss", "mill") for h in hints):
            direct_endpoint_lines += 1
        stack.append((s.get("derived", {}).get("interaction_window_proxy") or {}).get("stack_action_count_proxy", 0))

    infinite = sum(1 for x in lines if x.get("spellbook", {}).get("infinite"))
    bpwins = sum(1 for x in lines if str(x.get("classification", {}).get("outcome_hint", "")).startswith("blueprint_"))
    commander_direct = sum(1 for x in lines if (x.get("axes", {}).get("commander_requirement", {}).get("value") or {}).get("direct_commander_pieces"))
    external_payoff = sum(1 for x in lines if (x.get("axes", {}).get("required_payoff", {}).get("value") or {}).get("status") == "known_external_enabler")
    low_signal = sorted({n for x in lines for n in ((x.get("axes", {}).get("dead_card_burden", {}).get("value") or {}).get("low_independent_signal_pieces") or [])})
    min_cards = min((len(x.get("cards") or []) for x in lines), default=0)
    max_cards = max((len(x.get("cards") or []) for x in lines), default=0)

    review_flags = []
    if any(x.get("classification", {}).get("structural_hint") == "commander_independent_power_package" for x in lines):
        review_flags.append("commander_independent_power_package_present")
    if any(cid in pc_ids for cid in ids):
        review_flags.append("power_core_review_candidate_present")
    if external_payoff:
        review_flags.append("external_payoff_or_enabler_present")
    if direct_endpoint_lines:
        review_flags.append("direct_damage_life_loss_or_mill_endpoint_hint_present")
    if missing_steps:
        review_flags.append("missing_or_unavailable_step_semantics")
    if low_signal:
        review_flags.append("low_independent_signal_piece_present")
    if commander_direct and commander_direct < len(lines):
        review_flags.append("commander_participation_varies_within_family")

    return {
        "family_id": f"{slug}:family:{index:03d}",
        "combo_ids": ids,
        "line_count": len(lines),
        "relation": {
            "kind": "connected_component_of_near_variant_lines",
            "rule": "edge when two lines share at least min(piece_count)-1 pieces, minimum overlap 1",
            "transitive_component_warning": True,
            "evidence_class": "derived_metric",
            "confidence": "high",
        },
        "pieces": {
            "common_to_every_line": common,
            "union": union,
            "alternative_or_bridge_pieces": sorted(set(union) - set(common)),
            "min_piece_count": min_cards,
            "max_piece_count": max_cards,
        },
        "line_characteristics": {
            "infinite_line_count": infinite,
            "blueprint_win_linked_count": bpwins,
            "direct_commander_piece_line_count": commander_direct,
            "power_core_review_line_count": sum(1 for cid in ids if cid in pc_ids),
            "external_payoff_or_enabler_line_count": external_payoff,
            "direct_endpoint_hint_line_count": direct_endpoint_lines,
            "declared_mana_line_count": declared_mana,
            "missing_step_semantics_line_count": missing_steps,
            "max_stack_action_proxy": max(stack) if stack else 0,
            "structural_hints": count_hints(lines, "structural_hint"),
            "outcome_hints": count_hints(lines, "outcome_hint"),
            "endpoint_hints": dict(sorted(endpoint.items())),
        },
        "burden_signals": {
            "low_independent_signal_pieces": low_signal,
            "count": len(low_signal),
            "note": "Structural review signal only; this is not a claim that any piece is literally dead."
        },
        "review_flags": sorted(review_flags),
        "authority": {
            "can_decide": False,
            "classification_status": "unresolved_requires_judgment",
            "note": "Family synthesis organizes redundancy evidence only; it cannot retain/cut a package or assign final combo priority."
        },
        "evidence": [f"combo_quality:data/grixis/combo_quality/{slug}.json#{cid}" for cid in ids] +
                    [f"combo_line_semantics:data/grixis/combo_line_semantics/{slug}.json#{cid}" for cid in ids],
    }


def build_one(did, entry):
    slug = entry["slug"]
    cq = load(CQ / f"{slug}.json")
    ls = load(LS / f"{slug}.json")
    pc = load(PC / f"{slug}.json")
    sem = {x["combo_id"]: x for x in ls.get("lines", [])}
    pc_ids = {x["combo_id"] for x in pc.get("candidates", [])}
    fams = [build_family(slug, i + 1, rows, sem, pc_ids) for i, rows in enumerate(components(cq.get("combos", [])))]
    multi = [f for f in fams if f["line_count"] > 1]
    return {
        "schema_version": 1,
        "deck_id": did,
        "slug": slug,
        "canonical_hash": entry["canonical_project_list"]["hash"],
        "status": "provisional_evidence",
        "generated_by": f"scripts/grixis_combo_families.py v{VERSION}",
        "authority": {
            "can_decide": False,
            "note": "Step B redundancy/package evidence only. No family is automatically a primary, secondary, backup, incidental or removable combo package."
        },
        "inputs": {
            "combo_quality": f"data/grixis/combo_quality/{slug}.json",
            "combo_line_semantics": f"data/grixis/combo_line_semantics/{slug}.json",
            "power_core": f"data/grixis/power_core/{slug}.json",
        },
        "families": fams,
        "summary": {
            "family_count": len(fams),
            "multi_line_family_count": len(multi),
            "singleton_family_count": len(fams) - len(multi),
            "line_count": sum(f["line_count"] for f in fams),
            "largest_family_line_count": max((f["line_count"] for f in fams), default=0),
            "power_core_family_count": sum(1 for f in fams if f["line_characteristics"]["power_core_review_line_count"]),
            "commander_independent_family_count": sum(1 for f in fams if "commander_independent_power_package_present" in f["review_flags"]),
        },
    }


def build():
    reg = load(REGISTRY)
    rows = []
    OUT.mkdir(parents=True, exist_ok=True)
    for did, e in sorted(reg["decks"].items(), key=lambda kv: kv[1]["slug"]):
        d = build_one(did, e)
        dump(OUT / f"{e['slug']}.json", d)
        rows.append({"deck_id": did, "slug": e["slug"], **d["summary"]})
    keys = ("family_count", "multi_line_family_count", "singleton_family_count", "line_count", "power_core_family_count", "commander_independent_family_count")
    dump(OUT / "summary.json", {
        "schema_version": 1,
        "generated_by": f"scripts/grixis_combo_families.py v{VERSION}",
        "decks": rows,
        "totals": {k: sum(r[k] for r in rows) for k in keys},
        "largest_family_line_count": max((r["largest_family_line_count"] for r in rows), default=0),
    })
    print(f"combo-families: built {len(rows)} decks, {sum(r['family_count'] for r in rows)} families")


def check():
    try:
        import jsonschema
    except ImportError:
        print("combo-families: jsonschema required")
        return 1
    schema = load(SCHEMA)
    reg = load(REGISTRY)
    problems = []
    expected = {e["slug"] for e in reg["decks"].values()}
    present = {p.stem for p in OUT.glob("*.json") if p.name != "summary.json"}
    if expected != present:
        problems.append(f"file coverage mismatch missing={sorted(expected-present)} extra={sorted(present-expected)}")
    for did, e in sorted(reg["decks"].items()):
        slug = e["slug"]; p = OUT / f"{slug}.json"
        if not p.exists():
            continue
        d = load(p)
        for err in jsonschema.Draft202012Validator(schema).iter_errors(d):
            problems.append(f"{slug}: schema {list(err.path)}: {err.message}")
        cq = load(CQ / f"{slug}.json")
        source_ids = {x["id"] for x in cq.get("combos", [])}
        family_ids = [cid for f in d.get("families", []) for cid in f.get("combo_ids", [])]
        if set(family_ids) != source_ids or len(family_ids) != len(source_ids):
            problems.append(f"{slug}: every combo must occur in exactly one family")
        if d.get("canonical_hash") != e["canonical_project_list"]["hash"]:
            problems.append(f"{slug}: canonical hash drift")
        if any(f.get("authority", {}).get("can_decide") for f in d.get("families", [])):
            problems.append(f"{slug}: family record became decision-capable")
    print(f"combo-families: {len(expected)} deck files, {len(problems)} problems")
    for x in problems[:40]:
        print("FAIL", x)
    return 1 if problems else 0


def main(argv=None):
    a = argparse.ArgumentParser()
    a.add_argument("--build", action="store_true")
    a.add_argument("--check", action="store_true")
    a.add_argument("--summary", action="store_true")
    x = a.parse_args(argv); rc = 0
    if x.build: build()
    if x.check: rc |= check()
    if x.summary:
        print(json.dumps(load(OUT / "summary.json"), indent=2, sort_keys=True))
    if not (x.build or x.check or x.summary):
        a.print_help()
    return rc


if __name__ == "__main__":
    sys.exit(main())
