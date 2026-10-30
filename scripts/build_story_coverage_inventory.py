#!/usr/bin/env python3
"""Phase 5 coverage/gaps inventory: which official story arcs the claim packs cite (2026-10-30).

For every story arc tag in data/primary_sources.csv, this counts the inventoried Wizards pages and how
many of them at least one claim pack in data/multiverse_graph/manifest.json cites. It also lists the
citing packs and the uncited page URLs, so gaps show up as data rather than as prose. Untagged pages
(empty arc) are reported as one bucket.

Pages listed in data/lore_research/reviewed_no_claim.json (Batch 9) were read and found to hold no
quotable story relation (index pages, design interviews, duplicates). They are counted separately as
reviewed_no_claim_pages and give a second status, review_status; they never count as cited, and a
listed page that a pack also cites is an error. The register is not an approval and is reversible.

A cited page is not an exhaustively read page: packs are targeted, so "cited" means "used at least once".
This file makes no lore claim. Committed inputs only, so it runs in CI.

  python3 scripts/build_story_coverage_inventory.py           # rebuild
  python3 scripts/build_story_coverage_inventory.py --check   # rebuild and compare
"""
import argparse
import csv
import hashlib
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data/lore_research/story_coverage_inventory_2026-10-30.json"
PRIMARY = ROOT / "data/primary_sources.csv"
MANIFEST = ROOT / "data/multiverse_graph/manifest.json"
REVIEWED = ROOT / "data/lore_research/reviewed_no_claim.json"
REVIEWED_SCHEMA = "reviewed-no-claim/v1"
SCHEMA = "story-coverage-inventory/v1"
URL = re.compile(r"https://magic\.wizards\.com/[^\s\"'<>)\]]+")


def norm(u):
    return u.rstrip("/.,;")


def load_reviewed(rows, cited):
    """Validate the reviewed-no-claim register and return {normalized url: entry}."""
    if not REVIEWED.exists():
        return {}
    reg = json.loads(REVIEWED.read_text(encoding="utf-8"))
    if reg.get("schema") != REVIEWED_SCHEMA:
        raise ValueError(f"{REVIEWED.name}: schema must be {REVIEWED_SCHEMA}")
    arc_of = {norm(r["url"]): r["arc"] for r in rows}
    out = {}
    for e in reg["entries"]:
        u = norm(e["url"])
        problems = []
        if u in out:
            problems.append("listed twice")
        if u not in arc_of:
            problems.append("not in data/primary_sources.csv")
        elif e.get("arc", "") != arc_of[u]:
            problems.append(f"arc {e.get('arc')!r} != inventory arc {arc_of[u]!r}")
        if u in cited:
            problems.append("also cited by a claim pack; remove the register entry")
        if e.get("reason") not in reg["reasons"]:
            problems.append(f"unknown reason {e.get('reason')!r}")
        if e.get("reason") == "DUPLICATE_PAGE" and norm(e.get("duplicate_of", "")) not in cited:
            problems.append("DUPLICATE_PAGE needs duplicate_of naming a cited URL")
        for k in ("page_key", "reviewer", "reviewed_on", "note"):
            if not e.get(k):
                problems.append(f"missing {k}")
        if e.get("page_key") and u.split("/")[-1] != e["page_key"]:
            problems.append("page_key does not match the URL")
        if problems:
            raise ValueError(f"{REVIEWED.name}: {e['url']}: " + "; ".join(problems))
        out[u] = e
    return out


def build():
    rows = list(csv.DictReader(PRIMARY.open(encoding="utf-8")))
    packs = json.loads(MANIFEST.read_text(encoding="utf-8"))["claim_packs"]
    cited = defaultdict(set)
    claims = {}
    for p in packs:
        d = json.loads((ROOT / p).read_text(encoding="utf-8"))
        claims[Path(p).name] = len(d.get("claims", []))
        for u in URL.findall(json.dumps(d)):
            cited[norm(u)].add(Path(p).name)
    reviewed = load_reviewed(rows, cited)
    arcs = defaultdict(list)
    for r in rows:
        arcs[r["arc"] or "(untagged)"].append(r)
    out = []
    for arc in sorted(arcs, key=lambda a: (a == "(untagged)", a)):
        rs = arcs[arc]
        hit = [r for r in rs if norm(r["url"]) in cited]
        out.append({"arc": arc, "pages": len(rs), "cited_pages": len(hit),
                    "kinds": {k: sum(r["kind"] == k for r in rs) for k in sorted({r["kind"] for r in rs})},
                    "citing_packs": sorted({p for r in hit for p in cited[norm(r["url"])]}),
                    "status": "NOT_STARTED" if not hit else ("ALL_PAGES_CITED" if len(hit) == len(rs) else "PARTIAL"),
                    "uncited_urls": sorted(r["url"] for r in rs if norm(r["url"]) not in cited)})
        rv = sum(norm(r["url"]) in reviewed for r in rs)
        done = len(hit) + rv
        out[-1].update(reviewed_no_claim_pages=rv,
                       review_status="NOT_STARTED" if not done else (
                           "ALL_PAGES_CITED_OR_REVIEWED" if done == len(rs) else "PARTIAL"),
                       unreviewed_urls=sorted(r["url"] for r in rs
                                              if norm(r["url"]) not in cited and norm(r["url"]) not in reviewed))
    inventoried = {norm(r["url"]) for r in rows}
    body = {"schema": SCHEMA, "inputs": {"primary_sources": "data/primary_sources.csv", "claim_packs": packs,
                                         "reviewed_no_claim": REVIEWED.relative_to(ROOT).as_posix()},
            "meaning": "cited = a claim pack quotes or cites the page at least once; it does not mean the page was read exhaustively",
            "totals": {"arcs": len(out), "pages": len(rows), "cited_pages": sum(a["cited_pages"] for a in out),
                       "arcs_not_started": sum(a["status"] == "NOT_STARTED" for a in out),
                       "arcs_partial": sum(a["status"] == "PARTIAL" for a in out),
                       "arcs_all_cited": sum(a["status"] == "ALL_PAGES_CITED" for a in out),
                       "reviewed_no_claim_pages": sum(a["reviewed_no_claim_pages"] for a in out),
                       "arcs_all_cited_or_reviewed": sum(a["review_status"] == "ALL_PAGES_CITED_OR_REVIEWED" for a in out),
                       "claims": sum(claims.values()),
                       "pack_urls_outside_inventory": len([u for u in cited if u not in inventoried])},
            "claims_per_pack": claims, "arcs": out}
    body["sha256"] = hashlib.sha256(json.dumps(body, sort_keys=True).encode()).hexdigest()
    return body


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    d = build()
    if a.check:
        ok = json.loads(OUT.read_text(encoding="utf-8")) == d
        print("PASS" if ok else "FAIL: inventory is stale; rebuild it")
        return 0 if ok else 1
    OUT.write_text(json.dumps(d, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(d["totals"]))
    for x in d["arcs"]:
        print(f'{x["arc"]:12} {x["cited_pages"]:3}+{x["reviewed_no_claim_pages"]}r/{x["pages"]:<3} {x["status"]:16} {",".join(p.split("_2026")[0] for p in x["citing_packs"])}')
    return 0


if __name__ == "__main__":
    sys.exit(main())
