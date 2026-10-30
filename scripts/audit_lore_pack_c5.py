#!/usr/bin/env python3
"""Pack C5: independently check two official 2008 invasion-outcome attributions.

Offline --check validates the committed evidence schema/source and distinct
roles. --live additionally fetches the actual Wizards page and checks both
short excerpts verbatim (with HTML whitespace normalization). Neither mode
approves the pack or asserts a before/after order between the two outcomes.
"""
import argparse
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "data/lore_research/pack_c5_phyrexian_invasion_outcome_2026-10-30.json"
OFFICIAL = "https://magic.wizards.com/en/news/feature/known-mutliverse-2008-03-19"


class TextOnly(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)


def normalize(s):
    return " ".join(html.unescape(s).split()).casefold()


def audit(page_html=None):
    d = json.loads(PACK.read_text(encoding="utf-8"))
    assert d["status"].startswith("PRELIMINARY_RESEARCH")
    assert d["source_register"]["km"]["url"] == OFFICIAL
    assert [c["id"] for c in d["claims"]] == ["C501", "C502"]
    for c in d["claims"]:
        assert c["grade"] == "CANON_CONFIRMED" and c["source_ids"] == ["km"]
        assert c["source_excerpt"] and c["limitation"]
        assert "before" not in c["predicate"] and "after" not in c["predicate"]
    assert "does not name" in d["claims"][1]["limitation"].lower()
    assert "before or after" in d["claims"][1]["limitation"]
    if page_html is not None:
        reader = TextOnly()
        reader.feed(page_html)
        text = normalize(" ".join(reader.parts))
        for c in d["claims"]:
            if normalize(c["source_excerpt"]) not in text:
                raise ValueError(f"claim {c['id']} excerpt missing from live official Wizards page")
    return {"status": "PASS", "claims": len(d["claims"]),
            "official_url": OFFICIAL, "live_quote_check": page_html is not None,
            "owner_approval": False, "outcome_order": "UNESTABLISHED"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", action="store_true")
    group.add_argument("--live", action="store_true")
    a = parser.parse_args()
    page = None
    if a.live:
        with urlopen(Request(OFFICIAL, headers={"User-Agent": "MTG-Multiverse-Companion-lore-source-check/1.0"}), timeout=18) as r:
            page = r.read().decode("utf-8", errors="replace")
    print(json.dumps(audit(page), indent=2))


if __name__ == "__main__":
    main()
