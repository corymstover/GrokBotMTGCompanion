#!/usr/bin/env python3
"""One entry point for every automated check (Bot cycle 17, issue #67). Exit 1 if any check fails.

Steps (run in this order; each prints its own summary):
  1 links        scripts/check_links.py --all            relative links + #anchors in every .md (card shards included)
  2 schema       scripts/front_matter.py --check         typed YAML front-matter on pages, decks and card shards
  3 index        scripts/kb_find.py --check              retrieval index data/kb_index.json is current
  4 crossrefs    scripts/build_crossrefs.py --check      reverse card index + "Referenced in" lines are current (when present)
  4b calibration scripts/deck_calibration.py --check   bracket-calibration blocks + EDH Bracket Calibration.md are current
  5 citations    scripts/check_citations.py              Wizards URLs in sitemap/resolving (data/citations.json) + CR rule numbers exist
  6 oracle       scripts/verify_cards.py                 every card entry matches the Scryfall Oracle/rulings bulk verbatim
  7 decks        (built in)                              every deck list still resolves, is legal, fits identity, 100 cards, singleton,
                                                         and its stored Game Changer count matches the current Scryfall flags
  8 freshness    (built in)                              generated pages built from an older bulk than the cache (warning);
                                                         with --online, a newer Scryfall bulk than the cache (warning; --strict fails)
Default is offline (SCRYFALL_OFFLINE=1: newest cached bulk in .cache/, recorded citation results).
  python3 scripts/validate_all.py                 all steps, offline
  python3 scripts/validate_all.py --online        also refresh citations live and compare the cache with Scryfall's latest bulk
  python3 scripts/validate_all.py --skip oracle   skip steps by name (comma-separated); --only links,schema runs a subset
"""
import json
import os
import re
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
S = ROOT / "scripts"
sys.path.insert(0, str(S))


def run(cmd, env):
    t = time.time()
    p = subprocess.run([sys.executable] + cmd, cwd=ROOT, env=env, capture_output=True, text=True)
    out = (p.stdout + p.stderr).strip().splitlines()
    return p.returncode, out, time.time() - t


def deck_text(path):
    body = path.read_text(encoding="utf-8")
    m = re.search(r"## Decklist[^\n]*\n.*?```[^\n]*\n(.*?)```", body, re.S)
    return m.group(1) if m else ""


def decks_step():
    import evaluate_decklist as ev
    R = ev.Resolver()
    bad, n = [], 0
    for d in ("decks", "grixis/decks"):
        for p in sorted((ROOT / d).glob("*.md")):
            n += 1
            rel = p.relative_to(ROOT)
            res = ev.check(deck_text(p), R)
            hard = [i for i in res["issues"] if i["type"] in ev.HARD]
            bad += [f"{rel}: [{i['type']}] {i['card']}: {i['detail']}" for i in hard]
            gcs = [r["name"] for r in res["cards"] if r["gc"] and r["zone"] != "companion"]
            fm = re.search(r"^game_changers: (\d+)", p.read_text(encoding="utf-8"), re.M)
            if fm and int(fm.group(1)) != len(gcs):
                bad.append(f"{rel}: Game Changer drift — page says {fm.group(1)}, Scryfall flags now {len(gcs)} ({', '.join(gcs) or 'none'})")
    return (1 if bad else 0), [f"decks: {n} lists re-checked against Scryfall bulk {R.bulk[:10]}; {len(bad)} problems"] + ["  - " + b for b in bad[:30]]


def freshness_step(online, strict):
    import ingest_scryfall as ing
    _, cached = ing.get_bulk(ing.DEFAULT_CACHE, None)
    day = cached[:10]
    out, warn = [], []
    rx = re.compile(r"(?:Oracle bulk|bulk data|Scryfall bulk)[^0-9\n]{0,20}\(?(\d{4}-\d{2}-\d{2})")
    for p in sorted(ROOT.glob("*.md")) + sorted((ROOT / "grixis").glob("*.md")):
        m = rx.search(p.read_text(encoding="utf-8")[:4000])
        if m and m.group(1) < day:
            warn.append(f"{p.name}: built from bulk {m.group(1)} (cache {day}) — re-run its generator")
    code = 0
    if online:
        os.environ.pop("SCRYFALL_OFFLINE", None)
        try:
            meta = json.loads(urllib.request.urlopen(urllib.request.Request(f"{ing.API}/bulk-data/oracle-cards", headers=ing.HEADERS), timeout=60).read())
            if meta["updated_at"][:19] > cached[:19]:
                warn.append(f"Scryfall has a newer oracle bulk ({meta['updated_at'][:19]}) than the cache ({cached[:19]}) — run scripts/ingest_scryfall.py")
                code = 1 if strict else 0
            else:
                out.append(f"freshness: cache matches Scryfall's latest oracle bulk ({meta['updated_at'][:19]})")
        except Exception as e:
            warn.append(f"could not reach Scryfall bulk metadata: {type(e).__name__}")
    out.insert(0, f"freshness: cached bulk {cached[:19]}; {len(warn)} warning(s)")
    return code, out + ["  ⚠️ " + w for w in warn]


def main(argv):
    online, strict = "--online" in argv, "--strict" in argv
    opt = lambda k: set(argv[argv.index(k) + 1].split(",")) if k in argv else set()
    skip, only = opt("--skip"), opt("--only")
    env = dict(os.environ)
    if not online:
        env["SCRYFALL_OFFLINE"] = "1"
        os.environ["SCRYFALL_OFFLINE"] = "1"
    steps = [("links", ["scripts/check_links.py", "--all"]), ("schema", ["scripts/front_matter.py", "--check"]),
             ("index", ["scripts/kb_find.py", "--check"]), ("crossrefs", ["scripts/build_crossrefs.py", "--check"]),
             ("calibration", ["scripts/deck_calibration.py", "--check"]),
             ("citations", ["scripts/check_citations.py"] + (["--online"] if online else [])),
             ("oracle", ["scripts/verify_cards.py"]), ("decks", None), ("freshness", None)]
    results = []
    for name, cmd in steps:
        if name in skip or (only and name not in only):
            results.append((name, "skipped", 0))
            continue
        if name == "crossrefs" and not (S / "build_crossrefs.py").exists():
            results.append((name, "n/a", 0))
            continue
        t = time.time()
        if cmd:
            code, out, dt_ = run(cmd, env)
        else:
            code, out = decks_step() if name == "decks" else freshness_step(online, strict)
            dt_ = time.time() - t
        print(f"== {name} ({dt_:.0f}s): {'PASS' if code == 0 else 'FAIL'}")
        for line in out[-35:]:
            print("   " + line)
        results.append((name, "PASS" if code == 0 else "FAIL", dt_))
    print("\nvalidate_all summary: " + " · ".join(f"{n} {s}" for n, s, _ in results))
    return 1 if any(s == "FAIL" for _, s, _ in results) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
