"""Batch 10 authoring aid: print sentences of a cached official page that match a regex.

Usage: python3 grepq.py <slug> <regex> [<regex> ...]. Reading aid only; claims are written by hand from the printed
sentences and gated verbatim by story_claim_pipeline.py."""
import re, sys
from pathlib import Path
TXT = Path(__file__).resolve().parents[4] / ".cache/story/text22"
slug, pats = sys.argv[1], [re.compile(p, re.I) for p in sys.argv[2:]]
t = re.sub(r"\s+", " ", (TXT / f"{slug}.txt").read_text(encoding="utf-8"))
for s in re.split(r"(?<=[.!?\"”])\s+", t):
    if any(p.search(s) for p in pats) and len(s) <= 400:
        print(" -", s)
