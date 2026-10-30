"""Batch 9 authoring aid: print relation-bearing sentences from cached official pages.

Usage: python3 candidates.py slug [slug ...]. Output is a reading aid only; every claim is still written
by hand from the quoted sentence and gated verbatim by story_claim_pipeline.py."""
import re, sys
from pathlib import Path
TXT = Path(__file__).resolve().parents[4] / ".cache/story/text22"
PAT = re.compile(r"\b(kill(?:ed|s)?|slain|slew|murder\w*|khan of|leader of|led the|leads the|rul(?:er|ed|es) |brother|sister|mother|father|son of|daughter|twin|"
                 r"found(?:ed|er)|mentor|apprentice|student of|married|wife|husband|betray\w*|imprison\w*|creat(?:ed|or)|"
                 r"spirit dragon|ally|allies|alliance|sworn|serve[sd]? |captain of|queen|king|emperor|guildmaster|parun|born on|home plane)\b", re.I)
for slug in sys.argv[1:]:
    t = re.sub(r"\s+", " ", (TXT / f"{slug}.txt").read_text(encoding="utf-8"))
    print(f"=== {slug}")
    for s in re.split(r"(?<=[.!?\"”])\s+", t):
        if PAT.search(s) and 30 <= len(s) <= 320:
            print(" -", s)
