#!/usr/bin/env python3
"""Rebuild the gitignored official story-page cache (Bot cycle 35).

Fetches every page listed in data/primary_sources.csv into .cache/story/text22/<slug>.txt and the cited
non-story Wizards pages (ARTICLES below, Bot cycle 32) into .cache/story/articles/<slug>.txt, the text
that scripts/lore_quotes.py, build_card_enrichment.py, build_primary_sources.py and build_art_flavor.py
read. Full page text is never committed.

File format (unchanged from Bot cycle 22):
    URL: <url>\nTITLE: <html title>\nDATE: <YYYY-MM-DD published, if given>\n\n<article text, one text node per line>
Art captions keep the site's "<Card>\n| Art by:\n<Artist>" lines.

Polite and resumable: one request at a time, --delay seconds apart (default 1.0), 3 tries with backoff,
existing files are skipped unless --refresh; each file is written atomically (scripts/atomic_io.py), so
an interrupted run never leaves a partial page. Pages that fail are listed at the end (exit code 1).

  python3 scripts/fetch_story_pages.py [--refresh] [--delay 1.0] [--only SUBSTRING]
"""
import atomic_io  # noqa: F401  atomic Path.write_text (Bot cycle 34)
import argparse
import csv
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
TEXT = ROOT / ".cache" / "story" / "text22"
ART = ROOT / ".cache" / "story" / "articles"
CSV = ROOT / "data" / "primary_sources.csv"
UA = {"User-Agent": "Mozilla/5.0 (GrokBotMTGCompanion lore research)"}
ARTICLES = [  # cited non-story Wizards pages verified by lore_quotes (Bot cycle 32, #96)
    "https://magic.wizards.com/en/banned-restricted-list",
    "https://magic.wizards.com/en/keyword-glossary",
    "https://magic.wizards.com/en/news/announcements/official-reprint-policy",
    "https://magic.wizards.com/en/news/card-preview/introducing-ward-2021-03-25",
    "https://magic.wizards.com/en/news/feature/core-set-2021-and-jumpstart-release-notes-2020-06-20",
    "https://magic.wizards.com/en/news/making-magic/evergreen-eggs-ham-2015-06-08",
    "https://magic.wizards.com/en/news/making-magic/deciduous-2022-03-28",
    "https://magic.wizards.com/en/formats/commander",
]


INLINE = ["a", "abbr", "b", "cite", "code", "em", "i", "mark", "q", "s", "small", "span", "strong", "sub", "sup", "u"]


def slug(url):
    return url.rstrip("/").split("/")[-1]


def get(url, tries=3):
    for i in range(tries):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read().decode("utf-8", "ignore")
        except urllib.error.HTTPError as ex:
            if ex.code in (404, 410):
                return None
        except Exception:  # noqa: BLE001 — network trouble: back off and retry
            pass
        time.sleep(5 * (i + 1))
    return None


def extract(url, html):
    soup = BeautifulSoup(html, "lxml")
    title = (soup.title.string or "").strip() if soup.title else ""
    m = re.search(r'publishedDateTime:"(\d{4}-\d\d-\d\d)', html) or re.search(r'"datePublished":"(\d{4}-\d\d-\d\d)', html)
    for t in soup(["script", "style", "noscript"]):
        t.decompose()
    main = soup.find("article") or soup.find("main") or soup.body
    body = ""
    if main:
        # inline markup (<em>, <a>, …) must not split a sentence: unwrap it and re-parse so adjacent text merges,
        # then put one block-level text run per line (Bot cycle 35)
        for t in main.find_all(INLINE):
            t.unwrap()
        main = BeautifulSoup(str(main), "lxml")
        body = main.get_text("\n", strip=True)
        body = re.sub(r"[ \t]+", " ", body)
    return f"URL: {url}\nTITLE: {title}\nDATE: {m.group(1) if m else ''}\n\n{body}"


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--refresh", action="store_true")
    ap.add_argument("--delay", type=float, default=1.0)
    ap.add_argument("--only", default="")
    a = ap.parse_args(argv)
    jobs = [(r["url"], TEXT) for r in csv.DictReader(CSV.open(encoding="utf-8"))] + [(u, ART) for u in ARTICLES]
    jobs = [(u, d) for u, d in jobs if a.only in u]
    TEXT.mkdir(parents=True, exist_ok=True)
    ART.mkdir(parents=True, exist_ok=True)
    seen, failed, got, have = set(), [], 0, 0
    for i, (u, d) in enumerate(jobs, 1):
        f = d / f"{slug(u)}.txt"
        if f in seen:
            print(f"duplicate slug {f.name}: {u}", file=sys.stderr)
        seen.add(f)
        if f.exists() and not a.refresh:
            have += 1
            continue
        html = get(u)
        time.sleep(a.delay)
        if not html:
            failed.append(u)
            print(f"[{i}/{len(jobs)}] FAILED {u}", flush=True)
            continue
        txt = extract(u, html)
        f.write_text(txt, encoding="utf-8")
        got += 1
        if i % 25 == 0:
            print(f"[{i}/{len(jobs)}] {f.name} ({len(txt.split())} words)", flush=True)
    print(f"story pages: {got} fetched, {have} already cached, {len(failed)} failed of {len(jobs)}")
    for u in failed:
        print("  failed:", u)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
