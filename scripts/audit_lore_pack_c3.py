#!/usr/bin/env python3
"""Audit Pack C3 (Assault on New Phyrexia episode extraction) quotes against the official story cache.

This uses the same engine as audit_lore_pack_rtd.py: schema, grade and source checks, a
verbatim-quote check when the gitignored story cache is present, and per-quote sha256
values plus a self-hash so that ``--check`` works in CI without the cache.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import audit_lore_pack_rtd as E  # noqa: E402

PACK = E.ROOT / "data/lore_research/pack_c3_assault_on_new_phyrexia_2026-10-30.json"
OUT = E.ROOT / "data/lore_research/pack_c3_assault_on_new_phyrexia_audit_2026-10-30.json"
URL_RE = re.compile(r"^https://magic\.wizards\.com/en/news/magic-story/assault-on-new-phyrexia-or-episode-[1-5]-[a-z-]+$")
SCHEMA = "pack-c3-one-audit/v1"

if __name__ == "__main__":
    sys.exit(E.main(sys.argv[1:], PACK, OUT, URL_RE, SCHEMA))
