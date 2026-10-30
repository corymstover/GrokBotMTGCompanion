#!/usr/bin/env python3
"""Audit Pack C4 (March of the Machine episode extraction) quotes against the official story cache.

This uses the same engine as audit_lore_pack_rtd.py: schema, grade and source checks, a
verbatim-quote check when the gitignored story cache is present, and per-quote sha256
values plus a self-hash so that ``--check`` works in CI without the cache.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import audit_lore_pack_rtd as E  # noqa: E402

PACK = E.ROOT / "data/lore_research/pack_c4_march_of_the_machine_2026-10-30.json"
OUT = E.ROOT / "data/lore_research/pack_c4_march_of_the_machine_audit_2026-10-30.json"
URL_RE = re.compile(r"^https://magic\.wizards\.com/en/news/magic-story/episode-(?:1-triumph-of-the-fleshless|2-holding-your-breath|3-mother-son-and-story|4-beneath-eyes-unblinking|5-cathartic-reunion|6-the-last-to-leave|7-divine-intervention|8-wrenn-and-eight|9-the-old-sins-of-new-phyrexia|10-the-rhythms-of-life)$")
SCHEMA = "pack-c4-mom-audit/v1"

if __name__ == "__main__":
    sys.exit(E.main(sys.argv[1:], PACK, OUT, URL_RE, SCHEMA))
