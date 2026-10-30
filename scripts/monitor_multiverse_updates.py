#!/usr/bin/env python3
"""Read-only Phase 8 source-change signals; never changes repository data.

  python3 scripts/monitor_multiverse_updates.py --validate
  python3 scripts/monitor_multiverse_updates.py --live --output /tmp/mv-updates.json

The weekly GitHub Action saves a report artifact, but does not open/merge a PR,
download full card bulk files, or edit approval/snapshot records. Rule-page ETags
are only review signals, NEVER verification that a specific rule changed.
"""
from __future__ import annotations

import argparse
import csv
from datetime import datetime
from html.parser import HTMLParser
import json
from pathlib import Path
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlsplit, urlunsplit
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
BASELINE = ROOT / "data/maintenance/multiverse_update_monitor_baseline_2026-10-30.json"
TIMEOUT = 18


def canonical_url(url: str) -> str:
    parts = urlsplit(url)
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), parts.path.rstrip("/"), "", ""))


class StoryLinks(HTMLParser):
    def __init__(self, origin: str):
        super().__init__()
        self.origin = origin
        self.urls = set()

    def handle_starttag(self, tag, attrs):
        if tag != "a":
            return
        for k, v in attrs:
            if k == "href" and v:
                url = canonical_url(urljoin(self.origin, v))
                parts = urlsplit(url)
                if parts.netloc == "magic.wizards.com" and parts.path.startswith("/en/news/magic-story/"):
                    self.urls.add(url)


class RulesDocumentLinks(HTMLParser):
    """Only Wizards-hosted Comprehensive Rules PDF URLs, not arbitrary HTML text."""
    def __init__(self, origin):
        super().__init__()
        self.origin = origin
        self.urls = set()

    def handle_starttag(self, tag, attrs):
        if tag != "a":
            return
        for key, value in attrs:
            if key == "href" and value:
                url = canonical_url(urljoin(self.origin, value))
                p = urlsplit(url)
                if (p.netloc in {"media.wizards.com", "magic.wizards.com"} and
                    "MagicCompRules" in p.path and p.path.lower().endswith(".pdf")):
                    self.urls.add(url)


def known_story_urls(baseline):
    known = set()
    for path in baseline["story_inventory_sources"]:
        with (ROOT / path).open(encoding="utf-8-sig", newline="") as fh:
            for row in csv.DictReader(fh):
                url = row.get("url", "").strip()
                if url.startswith("https://magic.wizards.com/"):
                    known.add(canonical_url(url))
    return known


def baseline_data():
    d = json.loads(BASELINE.read_text(encoding="utf-8"))
    if d["schema"] != "multiverse-update-monitor-baseline/v1":
        raise ValueError("unknown monitor schema")
    if not all(p["url"].startswith("https://magic.wizards.com/") for p in d["watch_pages"]):
        raise ValueError("monitor may watch only official Wizards rules/Commander pages")
    if d["story_index_url"] != "https://magic.wizards.com/en/news/magic-story":
        raise ValueError("unexpected official story index")
    if not all(urlsplit(u).netloc == "media.wizards.com" and u.endswith(".pdf")
               for u in d["known_official_rules_documents"]):
        raise ValueError("unrecognized baseline official rules PDF URL")
    snap = json.loads((ROOT / d["active_snapshot_manifest"]).read_text(encoding="utf-8"))
    for key in ("default-cards", "oracle-cards", "rulings"):
        if not snap["files"][key].get("sha256") or not snap["files"][key].get("scryfall_updated_at"):
            raise ValueError("missing pinned snapshot hash/timestamp for " + key)
    if len(known_story_urls(d)) < 550:
        raise ValueError("official source inventory unexpectedly small")
    return d, snap


def story_signals(page_html: str, origin: str, known: set[str]) -> dict:
    parser = StoryLinks(origin)
    parser.feed(page_html)
    candidates = sorted(parser.urls - known)
    return {"status": "NEW_CANDIDATES_REVIEW_REQUIRED" if candidates else "NO_NEW_LINK_CANDIDATES_ON_INDEX_PAGE",
            "current_index_links": len(parser.urls), "new_story_url_candidates": candidates,
            "limitation": "One official listing page only, not a complete crawling/indexing of Wizards fiction."}


def scryfall_signals(payload: dict, snapshot: dict) -> dict:
    names = {"default_cards": "default-cards", "oracle_cards": "oracle-cards", "rulings": "rulings"}
    current = {r["type"]: r for r in payload.get("data", []) if r.get("type") in names}
    out = {}
    for typ, key in names.items():
        prior = snapshot["files"][key]["scryfall_updated_at"]
        now = current.get(typ, {}).get("updated_at")
        # Strict ISO timestamps; no filename or lexicographic clock guessing.
        try:
            newer = datetime.fromisoformat(now.replace("Z", "+00:00")) > datetime.fromisoformat(prior.replace("Z", "+00:00"))
        except (AttributeError, ValueError, TypeError):
            newer = None
        out[key] = {"pinned_updated_at": prior, "currently_advertised_updated_at": now,
                    "status": "NEWER_BULK_AVAILABLE_REVIEW_FIRST" if newer is True else
                    "NOT_NEWER" if newer is False else "UNVERIFIABLE_METADATA"}
    return out


def fetch(url, *, head=False):
    req = Request(url, method="HEAD" if head else "GET",
                  headers={"User-Agent": "MTG-Multiverse-Companion-source-monitor/1.0", "Accept": "application/json,text/html;q=0.8,*/*;q=0.5"})
    with urlopen(req, timeout=TIMEOUT) as resp:
        return (resp.read().decode("utf-8", errors="replace") if not head else "",
                resp.headers.get("ETag"))


def live_report(baseline, snapshot, getter=fetch):
    report = {"schema": "multiverse-update-signals/v1", "status": "RESEARCH_SIGNALS_ONLY_NOT_CERTIFICATION",
              "sources": {}, "requires_review": [],
              "policy": "No automatic card, rule, lore, deck, approval, or historical-snapshot mutations."}
    try:
        html, _ = getter(baseline["story_index_url"])
        report["sources"]["official_stories"] = story_signals(html, baseline["story_index_url"], known_story_urls(baseline))
        report["requires_review"].extend(report["sources"]["official_stories"]["new_story_url_candidates"])
    except (OSError, HTTPError, URLError, ValueError, TimeoutError) as e:
        report["sources"]["official_stories"] = {"status": "SOURCE_UNAVAILABLE", "error": type(e).__name__}
    try:
        data, _ = getter(baseline["scryfall_bulk_metadata_url"])
        report["sources"]["scryfall"] = scryfall_signals(json.loads(data), snapshot)
        report["requires_review"].extend(k for k, v in report["sources"]["scryfall"].items()
                                         if v["status"] == "NEWER_BULK_AVAILABLE_REVIEW_FIRST")
    except (OSError, HTTPError, URLError, ValueError, TimeoutError) as e:
        report["sources"]["scryfall"] = {"status": "SOURCE_UNAVAILABLE", "error": type(e).__name__}
    rules = []
    for page in baseline["watch_pages"]:
        try:
            body, etag = getter(page["url"], head=False)
            status = ("ETAG_DIFFERENT_INFORMATIONAL_ONLY" if etag and etag != page["etag"] else
                      "FINGERPRINT_UNCHANGED" if etag else "NO_ETAG_UNVERIFIABLE")
            links = []
            if page["url"].endswith("/rules"):
                parser = RulesDocumentLinks(page["url"])
                parser.feed(body)
                links = sorted(parser.urls - set(baseline["known_official_rules_documents"]))
                report["requires_review"].extend(links)
            rules.append({"name": page["name"], "url": page["url"], "etag": etag, "status": status,
                          "new_official_rules_documents": links,
                          "limitation": "Page ETag changes are informational; only new official rules-document URLs become review candidates. A link change is not proof of a rules change."})
        except (OSError, HTTPError, URLError, ValueError, TimeoutError) as e:
            rules.append({"name": page["name"], "url": page["url"], "status": "SOURCE_UNAVAILABLE", "error": type(e).__name__})
    report["sources"]["wizards_rules_pages"] = rules
    report["requires_review"] = sorted(set(report["requires_review"]))
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--validate", action="store_true")
    group.add_argument("--live", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    baseline, snapshot = baseline_data()
    if args.validate:
        print(json.dumps({"status": "PASS", "known_official_urls": len(known_story_urls(baseline)),
                          "watched_rules_pages": len(baseline["watch_pages"]),
                          "pinned_snapshot": snapshot["snapshot_id"]}))
        return
    report = live_report(baseline, snapshot)
    output = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.write_text(output, encoding="utf-8")
        print(f"Update signal report written: {args.output}; review signals: {len(report['requires_review'])}")
    else:
        print(output)


if __name__ == "__main__":
    main()
