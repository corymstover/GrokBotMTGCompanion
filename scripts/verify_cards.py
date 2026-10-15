#!/usr/bin/env python3
"""Verify every generated card entry against Scryfall oracle_cards bulk data.

Checks: CSV index <-> shard headings agree (no missing/duplicate entries); each entry's
Oracle text, type line, mana cost, color identity and flavor text match the bulk file
verbatim (after the same Markdown escaping the generator applies).
Usage: python3 scripts/verify_cards.py      (uses the cached bulk file in .cache/)
"""
import csv
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ingest_scryfall as ing  # noqa: E402


def main() -> int:
    cards, bulk = ing.get_bulk(ing.DEFAULT_CACHE, None)
    rulings, rbulk = ing.get_bulk(ing.DEFAULT_CACHE, None, "rulings")
    R = {}
    for r in rulings:
        R.setdefault(r["oracle_id"], []).append(r)
    by_id = {c["oracle_id"]: c for c in cards}
    rows = list(csv.DictReader(ing.INDEX_CSV.open(encoding="utf-8")))
    errors = []
    # parse shards into {heading: block}
    blocks = {}
    heads = Counter()
    for p in ing.CARDS_DIR.rglob("*.md"):
        text = p.read_text(encoding="utf-8")
        body = text.split("\n## Entries\n", 1)[1]
        seen = Counter()
        for chunk in re.split(r"\n(?=### )", "\n" + body):
            chunk = chunk.strip("\n")
            if not chunk.startswith("### "):
                continue
            a = ing.gh_anchor(chunk.split("\n", 1)[0][4:])
            name = f"{a}-{seen[a]}" if seen[a] else a
            seen[a] += 1
            rel = str(p.relative_to(ing.ROOT))
            blocks[(rel, name)] = chunk
            heads[(rel, name)] += 1
    dups = [k for k, v in heads.items() if v > 1]
    if dups:
        errors.append(f"{len(dups)} duplicate headings, e.g. {dups[:3]}")
    if len(blocks) != len(rows):
        errors.append(f"shard entries {len(blocks)} != index rows {len(rows)}")
    checked = flavor = r_cards = r_total = 0
    for r in rows:
        c = by_id.get(r["oracle_id"])
        blk = blocks.get((r["shard"], r["anchor"]))
        if c is None or blk is None:
            errors.append(f"missing: {r['name']}")
            continue
        faces = c.get("card_faces") if c.get("card_faces") and any("oracle_text" in f for f in c["card_faces"]) else [c]
        for f in faces:
            for ln in (f.get("oracle_text") or "").split("\n"):
                if ln and ("  > " + ln.replace("<", "&lt;")) not in blk:
                    errors.append(f"oracle mismatch: {r['name']}: {ln[:60]}")
                    break
            if f.get("type_line") and f["type_line"] not in blk:
                errors.append(f"type mismatch: {r['name']}")
            if f.get("mana_cost") and f["mana_cost"] not in blk:
                errors.append(f"cost mismatch: {r['name']}")
            if f.get("flavor_text"):
                flavor += 1
                first = f["flavor_text"].split("\n")[0].strip().replace("*", "\\*").replace("<", "&lt;")
                if first and first not in blk:
                    errors.append(f"flavor mismatch: {r['name']}")
        if r.get("rulings", "") != "":
            want = R.get(r["oracle_id"], [])
            got = len(re.findall(r"^  - \*\d{4}-\d{2}-\d{2}\*", blk, re.M))
            if int(r["rulings"]) != len(want) or got != len(want):
                errors.append(f"rulings count mismatch: {r['name']} csv={r['rulings']} file={got} bulk={len(want)}")
            for ru in want:
                if f"*{ru['published_at']}*" not in blk or ing.ruling_text(ru) not in blk:
                    errors.append(f"ruling text mismatch: {r['name']}: {ru['comment'][:50]}")
                    break
            if not want and "- **Rulings:** none published on Scryfall" not in blk:
                errors.append(f"rulings 'none' line missing: {r['name']}")
            r_cards += 1
            r_total += len(want)
        elif "**Rulings" in blk:
            errors.append(f"rulings present but CSV says pending: {r['name']}")
        if ing.ci_label(c.get("color_identity", [])) not in blk:
            errors.append(f"identity mismatch: {r['name']}")
        checked += 1
    print(f"verified {checked} entries ({flavor} faces with flavor text) against Scryfall bulk {bulk[:10]}; "
          f"rulings verified on {r_cards} processed cards ({r_total} rulings, rulings bulk {rbulk[:10]}); "
          f"{len(errors)} problems")
    for e in errors[:40]:
        print("  -", e)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
