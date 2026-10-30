#!/usr/bin/env python3
"""Extract explicit in-universe time expressions from cited claim quotes (Batch 10, Phase 3).

For every claim in the manifest's claim packs, each evidence quote is scanned for an explicit time phrase:
an AR year ("4560 AR"), a quantified span ("more than 1,200 years", "centuries ago", "millennia ago",
"thirty years ago", "last year"). The matched phrase is copied verbatim as ``value``; nothing is converted
to a calendar year, nothing is inferred, and a claim with no such phrase in its own quotes gets no date.
The graph builder attaches these as ``in_universe_date`` on the claim's edges, re-checking that the
phrase is inside a quote the claim cites.

Output: data/lore_research/in_universe_dates_2026-10-30.json (deterministic). ``--check`` fails when stale.
"""
from __future__ import annotations
import argparse, json, re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data/multiverse_graph/manifest.json"
OUT = ROOT / "data/lore_research/in_universe_dates_2026-10-30.json"
NUM = (r"(?:\d[\d,]*|a few|a couple of|several|many|countless|hundreds of|thousands of|tens of thousands of|a hundred|a thousand|"
       r"(?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|fifteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand)"
       r"(?:[- ](?:one|two|three|four|five|six|seven|eight|nine|hundred|thousand))*)")
UNIT = r"(?:years?|centuries|century|millennia|millennium|decades?|eons|aeons|generations)"
PATTERNS = [
    ("AR_YEAR", re.compile(r"\b\d[\d,]*\s?AR\b")),
    ("RELATIVE_SPAN", re.compile(rf"\b(?:(?:more than|over|nearly|almost|some|about|roughly|at least)\s+)?{NUM}\s+{UNIT}(?:\s+(?:ago|earlier|before|later|past|in the past))?\b", re.I)),
    ("RELATIVE_SPAN", re.compile(rf"\b{UNIT}\s+ago\b", re.I)),
    ("RELATIVE_SPAN", re.compile(r"\blast year\b", re.I)),
]


def find(quote: str) -> list[tuple[str, str]]:
    hits, taken = [], []
    for kind, rx in PATTERNS:
        for m in rx.finditer(quote):
            if any(a <= m.start() < b or a < m.end() <= b for a, b in taken):
                continue
            taken.append((m.start(), m.end()))
            hits.append((m.start(), kind, m.group(0)))
    return [(k, v) for _, k, v in sorted(hits)]


def build() -> dict:
    m = json.loads(MANIFEST.read_text(encoding="utf-8"))
    rows = []
    for rel in m["claim_packs"]:
        d = json.loads((ROOT / rel).read_text(encoding="utf-8"))
        for c in d.get("claims", []):
            if c.get("in_universe_date"):
                continue
            for ev in c.get("evidence", []):
                q, sid = ev.get("quote", ""), ev.get("source_id")
                if not q or sid not in c.get("source_ids", []):
                    continue
                hits = find(q)
                if hits:
                    kind, val = hits[0]
                    rows.append({"claim": c["id"], "pack": Path(rel).name, "value": val, "kind": kind,
                                 "also_in_quote": [v for _, v in hits[1:]], "quote": q, "source_id": sid})
                    break
    return {"schema": "in_universe_dates.v1",
            "status": "PRELIMINARY_RESEARCH; verbatim time phrases from cited quotes only; no calendar years inferred; not owner approved",
            "basis": "value is the exact phrase in the quote; RELATIVE_SPAN is relative to the cited story's present, not to any fixed calendar",
            "count": len(rows), "by_kind": {k: sum(1 for r in rows if r["kind"] == k) for k in ("AR_YEAR", "RELATIVE_SPAN")},
            "dates": rows}


def render(d: dict) -> str:
    return json.dumps(d, ensure_ascii=False, indent=1) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    text = render(build())
    if a.check:
        ok = OUT.exists() and OUT.read_text(encoding="utf-8") == text
        print("PASS" if ok else "STALE: rerun scripts/build_in_universe_dates.py")
        return 0 if ok else 1
    OUT.write_text(text, encoding="utf-8")
    d = json.loads(text)
    print(f"OK: {d['count']} claims with a quoted in-universe time phrase {d['by_kind']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
