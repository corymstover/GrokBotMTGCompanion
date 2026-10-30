#!/usr/bin/env python3
"""Build a verbatim excerpt of CR 701 (keyword actions) and 702 (keyword abilities).

Source: the official Wizards Comprehensive Rules TXT, effective 2026-09-25, the same file and
sha256 as data/rules/cr_20260925_commander_excerpt.json. Rule text is copied verbatim; the
Example lines are left out. The excerpt is used for rules citations by
scripts/rules_interactions.py.

  python3 scripts/build_cr_keyword_excerpt.py [--source PATH]   # needs the official TXT
  python3 scripts/build_cr_keyword_excerpt.py --check           # self-hash (and source, if present)
"""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data/rules/cr_20260925_keyword_excerpt.json"
BASE = json.loads((ROOT / "data/rules/cr_20260925_commander_excerpt.json").read_text(encoding="utf-8"))
DEFAULT_SRC = ROOT / ".cache/MagicCompRules-20260925.txt"


def build(src: Path) -> dict:
    raw = src.read_bytes()
    if hashlib.sha256(raw).hexdigest() != BASE["source_sha256"]:
        raise SystemExit("source TXT sha256 does not match the committed CR source hash")
    lines = [l.strip() for l in raw.decode("utf-8-sig").splitlines() if l.strip()]
    start = max(i for i, l in enumerate(lines) if l == "701. Keyword Actions")
    end = next(i for i in range(start, len(lines)) if lines[i].startswith("703. "))
    sections, rules = {}, {}
    for l in lines[start:end]:
        m = re.match(r"^(70[12]\.\d+)\. (.+)$", l)
        if m:
            sections[m.group(1)] = m.group(2)
            continue
        m = re.match(r"^(70[12]\.\d+[a-z]+) (.+)$", l)
        if m:
            rules[m.group(1)] = m.group(2)
    body = {"schema": "cr-excerpt/v1",
            "title": "Magic: The Gathering Comprehensive Rules — keyword actions (701) and keyword abilities (702) excerpt",
            "publisher": "Wizards of the Coast", "effective": BASE["effective"], "rules_page": BASE["rules_page"],
            "source_url": BASE["source_url"], "source_sha256": BASE["source_sha256"],
            "source_bytes": BASE["source_bytes"],
            "note": "Verbatim rule text (Example lines omitted) for citation. Re-check when Wizards publishes new rules.",
            "sections": sections, "rules": rules}
    body["content_sha256"] = hashlib.sha256(json.dumps(body, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
    return body


def main(argv=None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--source", type=Path, default=DEFAULT_SRC)
    p.add_argument("--check", action="store_true")
    a = p.parse_args(argv)
    if a.check:
        cur = json.loads(OUT.read_text(encoding="utf-8"))
        body = {k: v for k, v in cur.items() if k != "content_sha256"}
        if hashlib.sha256(json.dumps(body, sort_keys=True, ensure_ascii=False).encode()).hexdigest() != cur["content_sha256"]:
            print("FAIL: keyword excerpt self-hash mismatch")
            return 1
        if a.source.exists() and build(a.source) != cur:
            print("FAIL: keyword excerpt differs from the official source")
            return 1
        print(f"PASS keyword excerpt: {len(cur['sections'])} sections, {len(cur['rules'])} rules"
              + ("" if a.source.exists() else " (source TXT absent: self-hash only)"))
        return 0
    d = build(a.source)
    OUT.write_text(json.dumps(d, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}: {len(d['sections'])} sections, {len(d['rules'])} rules")
    return 0


if __name__ == "__main__":
    sys.exit(main())
