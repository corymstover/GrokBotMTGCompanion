#!/usr/bin/env python3
"""Replace [[Card Name]] placeholders in Markdown files with links to the card's entry.

Lore and EDH pages are hand-written; this keeps their card links exact. Resolution uses
data/card_index.csv: exact heading match first, then the front face of a multi-face card
("Alrund, God of the Cosmos" -> "Alrund, God of the Cosmos // Hakka, Whispering Raven").
[[Name|label]] sets the link text. Unresolvable names abort with exit code 1 (nothing written).
Usage: python3 scripts/resolve_card_links.py "Planes Index.md" [more.md ...]
"""
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PH = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")


def load():
    rows = {}
    with (ROOT / "data" / "card_index.csv").open(encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            rows[r["name"]] = r
            if " // " in r["name"]:
                rows.setdefault(r["name"].split(" // ")[0], r)
    return rows


def link_for(r, md_path: Path, label: str) -> str:
    depth = len(md_path.resolve().relative_to(ROOT).parts) - 1
    rel = "../" * depth + r["shard"].replace(" ", "%20")
    return f"[{label}]({rel}#{r['anchor']})"


def main(paths):
    rows = load()
    bad = 0
    for p in map(Path, paths):
        text = p.read_text(encoding="utf-8")
        missing = [m.group(1) for m in PH.finditer(text) if m.group(1) not in rows]
        if missing:
            print(f"{p}: unresolved card names: {missing}")
            bad += 1
            continue
        n = len(PH.findall(text))
        text = PH.sub(lambda m: link_for(rows[m.group(1)], p, m.group(2) or m.group(1)), text)
        p.write_text(text, encoding="utf-8")
        print(f"{p}: {n} card links resolved")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
