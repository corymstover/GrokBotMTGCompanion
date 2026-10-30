#!/usr/bin/env python3
"""Phase 8: machine-checked readiness against the "Definition of the first major Companion release".

Read-only. Each criterion from MTG_MULTIVERSE_MASTER_WORKFLOW.md is evaluated from committed artifacts and
reported as MET, PARTIAL, NOT_MET or EXTERNAL (needs CI or a human). This tool never approves, locks or certifies
anything; "MET" means the committed evidence satisfies the written criterion, not owner sign-off.

  python3 scripts/release_readiness.py [--json] [--out data/release/readiness_<date>.json]
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

PROTECTED = ["state/current_deck_overrides.json", "data/lore_decks/approvals", "data/grixis/approvals.json",
             "data/grixis/exceptions.json", "data/grixis/dev_snapshot_lock.json"]
FOUNDATION_PACKS = {"A": "pack_a_", "B": "pack_b_", "C": "pack_c_"}


def _json(rel):
    p = ROOT / rel
    return json.loads(p.read_text(encoding="utf-8")) if p.is_file() else None


def tree_digest(paths) -> dict:
    out = {}
    for rel in paths:
        p = ROOT / rel
        files = sorted(x for x in ([p] if p.is_file() else p.rglob("*") if p.is_dir() else []) if x.is_file())
        h = hashlib.sha256()
        for f in files:
            h.update(f.relative_to(ROOT).as_posix().encode() + b"\0" + hashlib.sha256(f.read_bytes()).digest())
        out[rel] = {"files": len(files), "sha256": h.hexdigest() if files else None}
    return out


def c_enrichment():
    d = _json("data/card_enrichment.json")
    if not d:
        return "NOT_MET", "data/card_enrichment.json missing", {}
    row = d["coverage"]["priority pool (any tier)"]
    total, done = row.get("total", row.get("size")), row["enriched"]
    ev = {"enriched": done, "total": total, "remaining": total - done}
    if done == total:
        return "MET", "all priority cards enriched", ev
    return "PARTIAL", (f"{done}/{total} enriched; {total - done} remaining. Blocked: the guarded rebuild needs verified "
                       "story-text, EDHREC and Commander Spellbook caches that are absent offline."), ev


def c_graph():
    import build_multiverse_graph as B
    man = _json("data/multiverse_graph/manifest.json") or {}
    packs = man.get("claim_packs", [])
    found = {k: [p for p in packs if Path(p).name.startswith(v)] for k, v in FOUNDATION_PACKS.items()}
    g = _json("data/multiverse_graph/multiverse_graph.json") or {}
    stats = g.get("stats", {})
    built = B.build()
    fresh = built.get("content_sha256") == g.get("content_sha256") and not built["problems"]
    statuses = set()
    for p in packs:
        statuses.add((_json(p) or {}).get("status", ""))
    ev = {"packs_by_foundation": found, "graph_stats": {k: stats.get(k) for k in ("nodes", "edges", "claims_by_status",
                                                                               "non_wizards_sources")},
          "pack_statuses": sorted(statuses), "graph_matches_inputs": fresh}
    if not fresh:
        return "NOT_MET", "committed graph is stale or has problems", ev
    if not all(found.values()):
        return "NOT_MET", "missing foundational pack(s): " + ",".join(k for k, v in found.items() if not v), ev
    if stats.get("non_wizards_sources"):
        return "PARTIAL", "graph cites non-Wizards sources", ev
    pre = any("PRELIMINARY" in s for s in statuses)
    return ("PARTIAL" if pre else "MET"), ("Packs A, B and C are searchable with cited connections, but every pack is "
                                            "PRELIMINARY_RESEARCH (not owner approved)" if pre else "all packs reviewed"), ev


def c_lookup():
    drift = sorted((ROOT / "data/card_db").glob("oracle_drift_*.json"))
    if not drift:
        return "NOT_MET", "no Oracle drift report", {}
    d = json.loads(drift[-1].read_text(encoding="utf-8"))
    changed = sum(len(v) for v in d["changed"].values())
    ev = {"report": drift[-1].relative_to(ROOT).as_posix(), "snapshot_date": d["snapshot_date"], "changes": changed,
          "index_rows": d["index_rows"], "rules_checks": ("Commander deck-construction checks built (scripts/commander_rules.py, CR 2026-09-25 "
          "excerpt; eligibility audit agrees with every index row); gameplay rules-interaction checks not built")}
    if changed:
        return "PARTIAL", f"{changed} card fields differ from snapshot {d['snapshot_date']}; refresh pending", ev
    return "PARTIAL", (f"card lookups reconcile with snapshot {d['snapshot_date']} (0 changes across {d['index_rows']} "
                       "cards); Commander deck-construction checks are built, gameplay rules-interaction checks are not"), ev


def c_atlas():
    d = _json("data/set_atlas/phase1b_qualified_functional_release_2026-10-29.json")
    if not d:
        return "NOT_MET", "no Phase 1B release record", {}
    ev = {"gate": d.get("gate"), "as_of": d.get("as_of"), "limitations": len(d.get("release_limitations", []))}
    if d.get("gate") == "QUALIFIED_OFFLINE_FUNCTIONAL_RELEASE_READY":
        return "MET", "Phase 1B qualified functional release (with stated limitations)", ev
    return "PARTIAL", f"gate {d.get('gate')}", ev


def c_deck():
    appr = sorted(p.name for p in (ROOT / "data/lore_decks/approvals").glob("*.md"))
    drafts = sorted(p.name for p in (ROOT / "data/lore_decks/drafts").glob("*_proposal.json"))
    man = _json("data/multiverse_graph/manifest.json") or {}
    graph_built = [Path(p).name for p in man.get("deck_evidence", [])]  # decks whose evidence feeds the graph
    ev = {"owner_approval_files": appr, "draft_proposals": len(drafts), "graph_based_drafts": graph_built}
    return "NOT_MET", (f"{len(appr)} owner-approval files exist for earlier lore decks, but no deck built from the new "
                       f"graph has owner review yet ({len(graph_built)} graph-linked draft(s) await review)"), ev


def c_grixis():
    return "EXTERNAL", ("guarded by focused-validation CI (validate_all) and protected-path digests below; this tool does "
                        "not re-run the 62-deck audit"), {"protected_path_digests": tree_digest(PROTECTED)}


def c_ci():
    return "EXTERNAL", "CI status lives on GitHub; check the required workflows on the release commit", {}


CRITERIA = [
    ("priority_enrichment", "Priority-card enrichment backlog fully accounted for", c_enrichment),
    ("foundation_graph", "Searchable cited connections across the three foundational lore packs", c_graph),
    ("lookup_and_rules", "Reliable lookup and rules checks backed by current Scryfall and official sources", c_lookup),
    ("set_atlas", "Verified Phase 1B set catalog", c_atlas),
    ("reviewed_graph_deck", "At least one complete, reviewed lore-first Commander deck built from the new graph", c_deck),
    ("grixis_no_regression", "No regression in the 62 archived approved Grixis decks", c_grixis),
    ("ci_and_coverage", "Passing focused CI and an up-to-date, source-backed coverage report", c_ci),
]


def readiness() -> dict:
    rows = []
    for cid, text, fn in CRITERIA:
        status, note, ev = fn()
        rows.append({"id": cid, "criterion": text, "status": status, "note": note, "evidence": ev})
    try:
        head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    except OSError:
        head = None
    tally = {s: sum(r["status"] == s for r in rows) for s in ("MET", "PARTIAL", "NOT_MET", "EXTERNAL")}
    return {"schema": "release-readiness/v1", "generated": dt.date.today().isoformat(), "commit": head or None,
            "verdict": "NOT_RELEASE_READY" if tally["NOT_MET"] or tally["PARTIAL"] else "READY_FOR_OWNER_REVIEW",
            "note": "Read-only readiness evidence. Never an approval, lock or certification.",
            "tally": tally, "criteria": rows}


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--json", action="store_true")
    p.add_argument("--out", type=Path)
    a = p.parse_args(argv)
    r = readiness()
    if a.out:
        r2 = dict(r, commit=None)  # committed copy omits the volatile commit id
        a.out.parent.mkdir(parents=True, exist_ok=True)
        a.out.write_text(json.dumps(r2, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    if a.json:
        print(json.dumps(r, indent=1, ensure_ascii=False))
    else:
        print(f"{r['verdict']}  {r['tally']}")
        for c in r["criteria"]:
            print(f"  [{c['status']:<8}] {c['criterion']}: {c['note']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
