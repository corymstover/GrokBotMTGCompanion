#!/usr/bin/env python3
"""Validate relative Markdown links and #anchors in the knowledge base.

Checks every .md file (including generated card shards with --all) for links whose
target file or heading anchor does not exist. External http(s) links are not fetched.
Exit code 1 if any broken link is found.  Usage: python3 scripts/check_links.py [--all]
"""
import re
import sys
import urllib.parse
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from grixis_archive import in_archive  # noqa: E402  Bot cycle 45: archived Grixis source is inert data, not checked

ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)\)")
HEAD = re.compile(r"^#{1,6}\s+(.*?)\s*$", re.M)
FENCE = re.compile(r"```.*?```", re.S)


def anchor(text: str) -> str:
    t = re.sub(r"[^\w\- ]", "", text.strip().lower(), flags=re.UNICODE)
    return t.replace(" ", "-")


_cache: dict[Path, set] = {}


def anchors_of(p: Path) -> set:
    if p not in _cache:
        seen, out = Counter(), set()
        for h in HEAD.findall(FENCE.sub("", p.read_text(encoding="utf-8"))):
            a = anchor(h)
            out.add(a if not seen[a] else f"{a}-{seen[a]}")
            seen[a] += 1
        _cache[p] = out
    return _cache[p]


def main() -> int:
    include_cards = "--all" in sys.argv
    files = [p for p in ROOT.rglob("*.md") if ".git" not in p.parts and ".cache" not in p.parts and not in_archive(p)
             and (include_cards or "cards" not in p.relative_to(ROOT).parts[:1])]
    bad = 0
    for f in sorted(files):
        text = FENCE.sub("", f.read_text(encoding="utf-8"))
        for target in LINK.findall(text):
            if re.match(r"^[a-z]+:", target):
                continue
            path, _, frag = target.partition("#")
            dest = (f.parent / urllib.parse.unquote(path)).resolve() if path else f
            if not dest.exists():
                print(f"{f.relative_to(ROOT)}: missing file -> {target}")
                bad += 1
            elif frag and dest.suffix == ".md" and urllib.parse.unquote(frag) not in anchors_of(dest):
                print(f"{f.relative_to(ROOT)}: missing anchor -> {target}")
                bad += 1
    print(f"checked {len(files)} files, {bad} broken links")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
