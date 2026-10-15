#!/usr/bin/env python3
"""Citation check (Bot cycle 17, issue #67): every Wizards URL resolves or is in the sitemap; every CR rule cited exists.

1. Wizards URLs — every *.wizards.com URL cited in any .md file (card shards included) must be
   (a) listed in the official magic.wizards.com sitemap, or (b) resolve with HTTP 200 (after redirects).
   Results are stored in data/citations.json (URL → status, final URL, checked date) so the default run is offline:
   it fails if a cited URL is missing from that file (new, never checked) or recorded as broken.
   Internet Archive links that wrap a Wizards URL (web.archive.org/web/<ts>/https://magic.wizards.com/…) are
   checked as archive citations (status "archived" when the snapshot resolves); the dead original is not re-cited.
   --online refreshes the sitemap and re-checks every URL not in it (live GET, 30 s timeout).
2. Comprehensive Rules — every "CR 903.5c"-style citation must name a rule that exists in the cached CR text
   (.cache/MagicCompRules-*.txt); skipped with a warning if no CR text is cached.
Usage: python3 scripts/check_citations.py [--online | --recheck] [--verbose]
  --recheck re-tests only URLs that are unchecked or recorded as broken (fast; keeps earlier good results).
"""
import concurrent.futures as cf
import datetime as dt
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "citations.json"
URL = re.compile(r"https?://(?:[a-z0-9-]+\.)*wizards\.com[^\s)<>\]\"'`|]*", re.I)
WAYBACK = re.compile(r"https?://web\.archive\.org/web/[^/\s]+/https?://(?:[a-z0-9-]+\.)*wizards\.com[^\s)<>\]\"'`|]*", re.I)
CR = re.compile(r"\bCR\s+(\d{3}(?:\.\d+[a-z]?)?)")
SITEMAP = "https://magic.wizards.com/en/sitemap.xml"
UA = {"User-Agent": "Mozilla/5.0 (GrokBotMTGCompanion citation check; +https://github.com/corymstover/GrokBotMTGCompanion)"}


def md_files():
    return [p for p in ROOT.rglob("*.md") if ".git" not in p.parts and ".cache" not in p.parts]


def norm(u):
    u = u.rstrip(".,;:")
    u = re.sub(r"^http://", "https://", u, flags=re.I)
    u = re.sub(r"^https://www\.magic\.wizards\.com", "https://magic.wizards.com", u, flags=re.I)
    return u.split("#")[0].rstrip("/")


def cited():
    urls, crs = {}, {}
    for p in md_files():
        text = p.read_text(encoding="utf-8")
        rel = str(p.relative_to(ROOT))
        for u in WAYBACK.findall(text):  # archived citations: the Internet Archive copy is what we cite
            urls.setdefault(u.rstrip(".,;:"), set()).add(rel)
        for u in URL.findall(WAYBACK.sub(" ", text)):
            urls.setdefault(u.rstrip(".,;:"), set()).add(rel)
        for r in CR.findall(text):
            crs.setdefault(r, set()).add(rel)
    return urls, crs


def get(u, timeout=30):
    try:
        with urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=timeout) as r:
            return r.status, r.geturl()
    except urllib.error.HTTPError as e:
        return e.code, u
    except Exception as e:  # timeout, DNS, TLS
        return 0, type(e).__name__


def online(urls, old, only_failed=False):
    with urllib.request.urlopen(urllib.request.Request(SITEMAP, headers=UA), timeout=60) as r:
        sm = {norm(u) for u in re.findall(r"<loc>([^<]+)</loc>", r.read().decode("utf-8", "ignore"))}
    today = dt.date.today().isoformat()
    res = {}
    todo = []
    prev = old.get("urls", {})
    for u in urls:
        if only_failed and prev.get(u, {}).get("status") not in (None, "broken"):
            res[u] = prev[u]
        elif norm(u) in sm:
            res[u] = {"status": "sitemap", "checked": today}
        else:
            todo.append(u)

    def one(u):
        slow = 90 if "web.archive.org" in u else 30
        code, final = get(u, slow)
        if code != 200 and u.lower().startswith("http://"):  # port 80 may be unreachable; the https form is the same page
            code, final = get("https://" + u[7:], slow)
        if code == 0:  # one retry for transient failures
            code, final = get(u, slow * 2)
        if "web.archive.org/web/" in u:
            st = "archived" if code == 200 else "broken"
            if st == "broken":  # snapshot fetches time out under load; the availability API is the authoritative fallback
                orig = re.sub(r"^https?://web\.archive\.org/web/[^/]+/", "", u)
                try:
                    with urllib.request.urlopen(urllib.request.Request(
                            "https://archive.org/wayback/available?url=" + urllib.parse.quote(orig, safe=":/"), headers=UA), timeout=60) as r:
                        snap = json.loads(r.read()).get("archived_snapshots", {}).get("closest") or {}
                    if snap.get("available") and snap.get("status") == "200":
                        st, final = "archived", snap["url"]
                except Exception:
                    pass
        else:
            st = "live" if code == 200 and norm(final) == norm(u) else "redirect" if code == 200 else "broken"
        d = {"status": st, "http": code, "checked": today}
        if st == "redirect":
            d["final"] = final
        return u, d

    live = [u for u in todo if "web.archive.org" not in u]
    with cf.ThreadPoolExecutor(6) as ex:
        for u, d in ex.map(one, live):
            res[u] = d
    for u in [u for u in todo if "web.archive.org" in u]:  # the Internet Archive throttles parallel clients
        for attempt in range(3):
            u, d = one(u)
            if d["status"] != "broken":
                break
            time.sleep(5 * (attempt + 1))
        res[u] = d
        time.sleep(1)
    return {"generated_by": "scripts/check_citations.py --online", "sitemap": SITEMAP, "sitemap_urls": len(sm),
            "checked": today, "urls": dict(sorted(res.items()))}


def cr_rules():
    cached = sorted((ROOT / ".cache").glob("MagicCompRules-*.txt"))
    if not cached:
        return None, None
    rules = set()
    for line in cached[-1].read_text(encoding="utf-8-sig", errors="ignore").splitlines():
        m = re.match(r"^(\d{3})\.(\d+)([a-z]?)\.?\s", line)
        if m:
            rules.update({m.group(1), f"{m.group(1)}.{m.group(2)}", f"{m.group(1)}.{m.group(2)}{m.group(3)}"})
        m = re.match(r"^(\d{3})\.\s", line)
        if m:
            rules.add(m.group(1))
    return rules, cached[-1].name


def main(argv):
    urls, crs = cited()
    old = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {"urls": {}}
    if "--online" in argv or "--recheck" in argv:
        old = online(urls, old, only_failed="--recheck" in argv)
        OUT.write_text(json.dumps(old, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    rec = old["urls"]
    bad = []
    counts = {}
    for u, where in sorted(urls.items()):
        st = rec.get(u, {}).get("status")
        counts[st or "unchecked"] = counts.get(st or "unchecked", 0) + 1
        if st is None:
            bad.append(f"unchecked URL (run --online): {u}  [{sorted(where)[0]}]")
        elif st == "broken":
            bad.append(f"broken URL (HTTP {rec[u].get('http')}): {u}  [{', '.join(sorted(where)[:3])}]")
    rules, crname = cr_rules()
    n_cr = 0
    if rules is None:
        print("citations: ⚠️ no cached CR text in .cache/ — CR citation check skipped")
    else:
        for r, where in sorted(crs.items()):
            n_cr += 1
            if r not in rules:
                bad.append(f"CR rule not found in {crname}: CR {r}  [{', '.join(sorted(where)[:3])}]")
    print(f"citations: {len(urls)} Wizards URLs ({', '.join(f'{k} {v}' for k, v in sorted(counts.items()))}; "
          f"checked {old.get('checked', '—')}); {n_cr} distinct CR rules cited; {len(bad)} problems")
    for b in bad[: (10**6 if "--verbose" in argv else 30)]:
        print("  - " + b)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
