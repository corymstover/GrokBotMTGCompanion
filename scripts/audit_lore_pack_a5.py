#!/usr/bin/env python3
"""Audit Pack A5 (Ugin's allies; Pilot 3 research) quotes against the official story cache.

This uses the same engine as audit_lore_pack_rtd.py: schema, grade and source checks, a
verbatim-quote check when the gitignored story cache is present, and per-quote sha256
values plus a self-hash so that ``--check`` works in CI without the cache.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import audit_lore_pack_rtd as E  # noqa: E402

PACK = E.ROOT / "data/lore_research/pack_a5_ugin_allies_2026-10-30.json"
OUT = E.ROOT / "data/lore_research/pack_a5_ugin_allies_audit_2026-10-30.json"
URL_RE = re.compile(r"^https://magic\.wizards\.com/en/news/magic-story/[a-z0-9-]+$")
SCHEMA = "pack-a5-ugin-allies-audit/v1"

if __name__ == "__main__":
    sys.exit(E.main(sys.argv[1:], PACK, OUT, URL_RE, SCHEMA))
