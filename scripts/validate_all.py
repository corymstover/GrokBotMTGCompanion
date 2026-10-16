#!/usr/bin/env python3
"""One entry point for every automated check (Bot cycle 17, issue #67). Exit 1 if any check fails.

Steps (run in this order; each prints its own summary):
  1 links        scripts/check_links.py --all            relative links + #anchors in every .md (card shards included)
  2 schema       scripts/front_matter.py --check         typed YAML front-matter on pages, decks and card shards
  3 index        scripts/kb_find.py --check              retrieval index data/kb_index.json is current
  4 crossrefs    scripts/build_crossrefs.py --check      reverse card index + "Referenced in" lines are current (when present)
  4b calibration scripts/deck_calibration.py --check   bracket-calibration blocks + EDH Bracket Calibration.md are current
  4c lore        scripts/build_lore_decks.py --check     kind: lore decks are >= 85% story-linked (Bot cycle 23)
  4d lore-entries scripts/check_lore.py                 every lore entry cites an official page; statement/timeline rows cited;
                                                         entry anchors resolve; spark state agrees across Characters Index,
                                                         dossiers and retcon log; Lore Entry Index current (Bot cycle 31, #94)
  4e lore-quotes  scripts/lore_quotes.py --check        every quotation on 13 lore + 12 rules/FAQ/EDH pages is verbatim in the
                                                         cached official page it cites (or card text / CR / rulings), or a
                                                         documented exception (Bot cycles 31–32)
  4f card-enrichment scripts/build_card_enrichment.py --check  card Lore/Synergy lines current; every lore relation cited and
                                                         linked back by its entry; decks contain the card; tiers labelled (Bot cycle 33, #102)
  5 citations    scripts/check_citations.py              Wizards URLs in sitemap/resolving (data/citations.json) + CR rule numbers exist
  6 oracle       scripts/verify_cards.py                 every card entry matches the Scryfall Oracle/rulings bulk verbatim
  7 decks        (built in)                              every deck list still resolves, is legal, fits identity, 100 cards, singleton,
                                                         and its stored Game Changer count matches the current Scryfall flags
  7b source-archive scripts/grixis_archive.py --check  archived Grixis source tree matches SHA256SUMS + source.json (count, hashes, bundle)
  8 freshness    (built in)                              generated pages built from an older bulk than the cache (warning);
                                                         with --online, a newer Scryfall bulk than the cache (warning; --strict fails)
Default is offline (SCRYFALL_OFFLINE=1: newest cached bulk in .cache/, recorded citation results).
  python3 scripts/validate_all.py                 all steps, offline
  python3 scripts/validate_all.py --online        also refresh citations live and compare the cache with Scryfall's latest bulk
  python3 scripts/validate_all.py --skip oracle   skip steps by name (comma-separated); --only links,schema runs a subset
"""
import datetime as dt
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
    bad, n, pending_n = [], 0, 0
    pf = ROOT / "data" / "grixis_pending.json"
    pend_reg = json.loads(pf.read_text(encoding="utf-8"))["decks"] if pf.exists() else {}
    slugs = json.loads((ROOT / "data" / "grixis_summary.json").read_text(encoding="utf-8")) if (ROOT / "data" / "grixis_summary.json").exists() else {}
    by_slug = {v["slug"]: k for k, v in slugs.items()}
    did_of = lambda p: by_slug.get(p.stem) if p.parent.name == "decks" and p.parent.parent.name == "grixis" else None
    for did, v in pend_reg.items():
        if v.get("status") == "pending" and did in slugs and slugs[did].get("legality_status") != "pending":
            bad.append(f"data/grixis_pending.json: {did} is pending but its page is not (re-run scripts/build_grixis.py)")
    for d in ("decks", "grixis/decks"):
        for p in sorted((ROOT / d).glob("*.md")):
            n += 1
            rel = p.relative_to(ROOT)
            res = ev.check(deck_text(p), R)
            hard = [i for i in res["issues"] if i["type"] in ev.HARD]
            text = p.read_text(encoding="utf-8")
            if re.search(r"^legality_status: pending$", text, re.M):
                # Bot cycle 38: a pending-legality deck may contain its listed not-yet-legal cards, only before legal_from
                lf = re.search(r"^legal_from: (\d{4}-\d{2}-\d{2})$", text, re.M)
                pc = re.search(r"^pending_cards: (\[.*\])$", text, re.M)
                names = re.findall(r'"((?:[^"\\]|\\.)*)"', pc.group(1)) if pc else []
                pending_n += 1
                if not lf or not names:
                    bad.append(f"{rel}: legality_status pending needs legal_from and pending_cards")
                elif dt.date.fromisoformat(lf.group(1)) <= dt.date.today():
                    bad.append(f"{rel}: pending legality expired (legal_from {lf.group(1)} has passed) — run python3 scripts/activate_pending_grixis.py")
                else:
                    failing = {i["card"] for i in hard if i["type"] == "not Commander-legal"}
                    hard = [i for i in hard if not (i["type"] == "not Commander-legal" and i["card"] in names)]
                    for n_ in names:
                        if n_ not in failing:
                            bad.append(f"{rel}: pending card {n_} is already Commander-legal on Scryfall — run python3 scripts/activate_pending_grixis.py")
                if did_of(p) and pend_reg.get(did_of(p), {}).get("status") != "pending":
                    bad.append(f"{rel}: page is pending but data/grixis_pending.json is not")
            bad += [f"{rel}: [{i['type']}] {i['card']}: {i['detail']}" for i in hard]
            gcs = [r["name"] for r in res["cards"] if r["gc"] and r["zone"] != "companion"]
            fm = re.search(r"^game_changers: (\d+)", p.read_text(encoding="utf-8"), re.M)
            if fm and int(fm.group(1)) != len(gcs):
                bad.append(f"{rel}: Game Changer drift — page says {fm.group(1)}, Scryfall flags now {len(gcs)} ({', '.join(gcs) or 'none'})")
    return (1 if bad else 0), [f"decks: {n} lists re-checked against Scryfall bulk {R.bulk[:10]} ({pending_n} pending legality, accepted until legal_from); {len(bad)} problems"] + ["  - " + b for b in bad[:30]]


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
             ("lore", ["scripts/build_lore_decks.py", "--check"]),  # Bot cycle 23: kind: lore decks must be >= 85% story-linked
             ("lore-entries", ["scripts/check_lore.py"]),  # Bot cycle 31 (#94): lore entry citations, anchors, spark consistency
             ("lore-quotes", ["scripts/lore_quotes.py", "--check"]),  # Bot cycle 31 (#94): verbatim quote verification
             ("card-enrichment", ["scripts/build_card_enrichment.py", "--check"]),  # Bot cycle 33 (#102): card Lore/Synergy lines
             ("citations", ["scripts/check_citations.py"] + (["--online"] if online else [])),
             ("oracle", ["scripts/verify_cards.py"]), ("decks", None),
             ("grixis-refine", ["scripts/grixis_refine.py", "--check"]),  # Bot cycle 39: refined lists verified, exports match deck pages
             ("source-archive", ["scripts/grixis_archive.py", "--check"]),  # Bot cycle 45: archived Grixis source byte-identical to its manifest
             ("freshness", None)]
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
