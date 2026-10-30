#!/usr/bin/env python3
"""Bulk claim-pack pipeline over the cached official Wizards story pages (Phase 5, 2026-10-30).

A compact *spec* (data/lore_research/claim_specs/<pack_id>.spec.json) is the hand-written source of
truth: arc tag, page slugs, entities and claims with verbatim quotes keyed by page slug. This tool
turns every spec into the standard claim pack (schema multiverse-claim-pack/v1, the same shape the
graph builder ingests) plus a self-hashed audit, so a new arc costs a spec file and nothing else.

Gates (any failure blocks the build):
- every page slug must be a row of data/primary_sources.csv whose arc tag is the spec's arc, on
  magic.wizards.com (the source register is generated from that row, never typed by hand);
- every quote must be a verbatim substring of the cached page text (.cache/story/text22/<slug>.txt);
  only whitespace is normalized, and quotes must be at least 25 characters;
- grades come from a closed set; anything other than CANON_CONFIRMED needs a limitation;
- claim ids are unique across all specs; subjects are declared entities;
- status is always PRELIMINARY_RESEARCH (not owner approved, not certified).

The audit stores per-quote sha256 values, so ``--check`` works in CI without the gitignored cache:
it rebuilds each pack from its spec, compares it byte-for-byte with the committed pack, and checks
the audit hashes; with the cache present it re-verifies every quote.

  python3 scripts/story_claim_pipeline.py build            # build all specs (needs the cache)
  python3 scripts/story_claim_pipeline.py check            # CI: rebuild + compare, cache optional
  python3 scripts/story_claim_pipeline.py find ARC REGEX   # authoring aid: matching sentences
  python3 scripts/story_claim_pipeline.py pages ARC        # list an arc's inventoried pages
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPECS = ROOT / "data/lore_research/claim_specs"
OUTDIR = ROOT / "data/lore_research"
CACHE = ROOT / ".cache/story/text22"
PRIMARY = ROOT / "data/primary_sources.csv"
MANIFEST = ROOT / "data/multiverse_graph/manifest.json"
GRADES = {"CANON_CONFIRMED", "CANON_IMPLIED", "CANON_DISPUTED", "OPEN_QUESTION", "ALTERNATE_CONTINUITY"}
ENTITY_TYPES = {"Character", "Event", "Plane", "Place", "Object", "Faction", "Concept"}
STATUS = "PRELIMINARY_RESEARCH (not owner approved, not certified)"
MIN_QUOTE = 25
KIND = {"story": "official_story_episode", "planeswalkers-guide": "official_planeswalkers_guide",
        "feature": "official_story_feature"}
PACK_SCHEMA = "multiverse-claim-pack/v1"
AUDIT_SCHEMA = "story-claim-pipeline-audit/v1"


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def sha(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def slug_of(url: str) -> str:
    return url.rstrip("/").split("/")[-1]


def primary_rows() -> dict:
    return {slug_of(r["url"]): r for r in csv.DictReader(PRIMARY.open(encoding="utf-8"))}


def page_text(slug: str, cache: Path = CACHE) -> str | None:
    f = cache / f"{slug}.txt"
    return norm(f.read_text(encoding="utf-8")) if f.exists() else None


def spec_files() -> list[Path]:
    return sorted(SPECS.glob("*.spec.json"))


def pack_paths(pack_id: str) -> tuple[Path, Path]:
    return OUTDIR / f"{pack_id}_2026-10-30.json", OUTDIR / f"{pack_id}_audit_2026-10-30.json"


def build_pack(spec: dict, rows: dict, cache: Path = CACHE, seen_ids: set | None = None):
    """Return (pack, audit, problems, cache_present)."""
    problems: list[str] = []
    arc = spec["arc"]
    reg = {}
    for sid, slug in spec["pages"].items():
        r = rows.get(slug)
        if r is None:
            problems.append(f"{sid}: page {slug} is not in data/primary_sources.csv"); continue
        if r["arc"] != arc:
            problems.append(f"{sid}: page {slug} is tagged {r['arc']!r}, not {arc!r}")
        if not r["url"].startswith("https://magic.wizards.com/"):
            problems.append(f"{sid}: not a magic.wizards.com page")
        reg[sid] = {"title": r["title"], "url": r["url"], "kind": KIND.get(r["kind"], r["kind"]),
                    "perspective": "Wizards of the Coast (official Magic Story)", "published": r["date"]}
    ents = {}
    for e in spec["entities"]:
        if e["type"] not in ENTITY_TYPES:
            problems.append(f"entity {e['id']}: type {e['type']} not allowed")
        if e["id"] in ents:
            problems.append(f"entity {e['id']} declared twice")
        ents[e["id"]] = e
    texts = {sid: page_text(spec["pages"][sid], cache) for sid in spec["pages"]}
    cache_present = all(t is not None for t in texts.values())
    claims, rows_out = [], []
    seen_ids = seen_ids if seen_ids is not None else set()
    for c in spec["claims"]:
        cid = c["id"]
        if cid in seen_ids:
            problems.append(f"{cid}: duplicate claim id")
        seen_ids.add(cid)
        if c["grade"] not in GRADES:
            problems.append(f"{cid}: unknown grade {c['grade']}")
        if c["grade"] != "CANON_CONFIRMED" and not c.get("limitation"):
            problems.append(f"{cid}: {c['grade']} needs a limitation")
        if c["subject"] not in ents:
            problems.append(f"{cid}: subject {c['subject']} is not a declared entity")
        if not c.get("quotes"):
            problems.append(f"{cid}: no evidence quotes")
        ev, sids = [], []
        for q in c.get("quotes", []):
            sid = q["page"]
            if sid not in spec["pages"]:
                problems.append(f"{cid}: quote page {sid} is not a registered page"); continue
            if sid not in sids:
                sids.append(sid)
            nq = norm(q["quote"])
            status = "NOT_CHECKED_CACHE_ABSENT"
            if len(nq) < MIN_QUOTE:
                problems.append(f"{cid}: quote shorter than {MIN_QUOTE} characters")
            if texts.get(sid) is not None:
                status = "VERBATIM" if nq in texts[sid] else "NOT_FOUND"
                if status == "NOT_FOUND":
                    problems.append(f"{cid}: quote not found verbatim in {sid}: {nq[:70]}")
            ev.append({"source_id": sid, "quote": q["quote"]})
            rows_out.append({"claim": cid, "source_id": sid, "quote_sha256": sha(nq), "status": status})
        claims.append({"id": cid, "subject": c["subject"], "predicate": c["predicate"], "object": c["object"],
                       "grade": c["grade"], "event_stage": c.get("event_stage", spec["event_stage"]),
                       "source_ids": sids, "evidence": ev, "summary": c["summary"],
                       "limitation": c.get("limitation", "")})
    cited = {s for c in claims for s in c["source_ids"]}
    pack = {"schema": PACK_SCHEMA, "pack_id": spec["pack_id"], "evidence_cutoff": "2026-10-30",
            "status": STATUS, "arc": arc, "scope": spec["scope"],
            "built_by": "scripts/story_claim_pipeline.py from data/lore_research/claim_specs/" + spec["pack_id"] + ".spec.json",
            "source_register": reg, "entities": spec["entities"], "claims": claims,
            "pages_registered": len(reg), "pages_cited": len(cited),
            "uncited_registered_pages": sorted(set(reg) - cited), "remaining": spec.get("remaining", [])}
    grades: dict[str, int] = {}
    for c in claims:
        grades[c["grade"]] = grades.get(c["grade"], 0) + 1
    audit = {"schema": AUDIT_SCHEMA, "pack": f"data/lore_research/{pack_paths(spec['pack_id'])[0].name}",
             "pack_status": STATUS, "arc": arc, "claims": len(claims), "entities": len(ents), "sources": len(reg),
             "grades": dict(sorted(grades.items())), "quotes": len(rows_out),
             "quotes_verbatim": sum(r["status"] == "VERBATIM" for r in rows_out), "quote_rows": rows_out,
             "problems": problems,
             "note": "Verbatim-quote audit against cached official Wizards story text. Research evidence only: not owner approval, not certification, not an exhaustive reading."}
    audit["content_sha256"] = sha(json.dumps(audit, sort_keys=True, ensure_ascii=False))
    return pack, audit, problems, cache_present


def dump(d: dict) -> str:
    return json.dumps(d, indent=1, ensure_ascii=False) + "\n"


def cmd_build(only: list[str]) -> int:
    rows, seen, bad = primary_rows(), set(), 0
    man = json.loads(MANIFEST.read_text(encoding="utf-8"))
    for f in spec_files():
        spec = json.loads(f.read_text(encoding="utf-8"))
        if only and spec["pack_id"] not in only:
            for c in spec["claims"]:
                seen.add(c["id"])
            continue
        pack, audit, problems, cache_present = build_pack(spec, rows, CACHE, seen)
        if not cache_present:
            print(f"{spec['pack_id']}: story cache missing for some pages", file=sys.stderr); return 2
        p, a = pack_paths(spec["pack_id"])
        print(f"{spec['pack_id']}: {audit['claims']} claims, {audit['quotes_verbatim']}/{audit['quotes']} verbatim, "
              f"{pack['pages_cited']}/{pack['pages_registered']} pages cited, problems={len(problems)}")
        for pr in problems:
            print("  -", pr)
        if problems:
            bad += 1; continue
        p.write_text(dump(pack), encoding="utf-8")
        a.write_text(dump(audit), encoding="utf-8")
        rel = f"data/lore_research/{p.name}"
        if rel not in man["claim_packs"]:
            man["claim_packs"].append(rel)
    MANIFEST.write_text(json.dumps(man, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    return 1 if bad else 0


def cmd_check() -> int:
    rows, seen, fails = primary_rows(), set(), []
    man = json.loads(MANIFEST.read_text(encoding="utf-8"))
    for f in spec_files():
        spec = json.loads(f.read_text(encoding="utf-8"))
        pack, audit, problems, cache_present = build_pack(spec, rows, CACHE, seen)
        p, a = pack_paths(spec["pack_id"])
        pid = spec["pack_id"]
        schema_problems = [x for x in problems if "quote not found" not in x]
        if schema_problems or (cache_present and problems):
            fails += [f"{pid}: {x}" for x in problems]; continue
        if not p.exists() or p.read_text(encoding="utf-8") != dump(pack):
            fails.append(f"{pid}: committed pack differs from the spec build"); continue
        old = json.loads(a.read_text(encoding="utf-8"))
        body = {k: v for k, v in old.items() if k != "content_sha256"}
        if sha(json.dumps(body, sort_keys=True, ensure_ascii=False)) != old.get("content_sha256"):
            fails.append(f"{pid}: audit self-hash mismatch"); continue
        if old["problems"] or old["quotes_verbatim"] != old["quotes"]:
            fails.append(f"{pid}: committed audit is not clean"); continue
        key = lambda rs: [(r["claim"], r["source_id"], r["quote_sha256"]) for r in rs]
        if key(old["quote_rows"]) != key(audit["quote_rows"]):
            fails.append(f"{pid}: quotes differ from the audited quotes"); continue
        if cache_present and audit != old:
            fails.append(f"{pid}: audit differs from cache-backed rerun"); continue
        if f"data/lore_research/{p.name}" not in man["claim_packs"]:
            fails.append(f"{pid}: pack not registered in manifest claim_packs"); continue
        print(f"OK {pid}: {old['claims']} claims, {old['quotes_verbatim']}/{old['quotes']} verbatim "
              f"({'re-verified against cache' if cache_present else 'cache absent: hashes verified'})")
    for x in fails:
        print("FAIL", x)
    return 1 if fails else 0


def cmd_pages(arc: str) -> int:
    for slug, r in sorted(primary_rows().items(), key=lambda kv: kv[1]["date"]):
        if r["arc"] == arc:
            t = page_text(slug)
            print(f"{r['date']}  {slug:60} {r['kind']:20} {len(t) if t else 'NOT CACHED'}  {r['title']}")
    return 0


def cmd_find(arc: str, pattern: str, width: int) -> int:
    rx = re.compile(pattern, re.I)
    for slug, r in sorted(primary_rows().items(), key=lambda kv: kv[1]["date"]):
        if r["arc"] != arc:
            continue
        t = page_text(slug)
        if not t:
            continue
        for m in rx.finditer(t):
            s = max(0, m.start() - width); e = min(len(t), m.end() + width)
            print(f"[{slug}] …{t[s:e]}…")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build"); b.add_argument("only", nargs="*")
    sub.add_parser("check")
    pg = sub.add_parser("pages"); pg.add_argument("arc")
    fd = sub.add_parser("find"); fd.add_argument("arc"); fd.add_argument("pattern"); fd.add_argument("--width", type=int, default=160)
    a = ap.parse_args(argv)
    if a.cmd == "build":
        return cmd_build(a.only)
    if a.cmd == "check":
        return cmd_check()
    if a.cmd == "pages":
        return cmd_pages(a.arc)
    return cmd_find(a.arc, a.pattern, a.width)


if __name__ == "__main__":
    sys.exit(main())
