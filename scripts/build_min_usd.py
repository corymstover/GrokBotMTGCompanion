"""Rebuild the gitignored price snapshot `.cache/min_usd_<YYYYMMDD>.json` used by scripts/edh_lib.py.

Bot cycle 34 (cache recovery): per paper printing in the Scryfall `default_cards` bulk, take `usd`,
else `usd_foil` (etched-only and digital printings are skipped), and keep the minimum per oracle_id.
Reproduces the committed EDH Packages price columns exactly for the 2026-10-15 bulk.
"""
import atomic_io
import gzip
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / ".cache"


def main():
    bulks = sorted(CACHE.glob("default-cards-*.json*"))
    if not bulks:
        sys.exit("no .cache/default-cards-*.jsonl.gz bulk; run scripts/ingest_scryfall.py first")
    bulk = bulks[-1]
    date = re.search(r"-(\d{8})\d{6}\.", bulk.name).group(1)
    best = {}
    opener = gzip.open if bulk.suffix == ".gz" else open
    with opener(bulk, "rt", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip().rstrip(",")
            if not line or line in "[]":
                continue
            c = json.loads(line)
            if c.get("digital"):
                continue
            oid = c.get("oracle_id") or (c.get("card_faces") or [{}])[0].get("oracle_id")
            p = c.get("prices") or {}
            first = next((p[k] for k in ("usd", "usd_foil") if p.get(k)), None)
            if not oid or first is None:
                continue
            best[oid] = min(best.get(oid, float("inf")), float(first))
    out = CACHE / f"min_usd_{date}.json"
    with atomic_io.atomic_open(out, "w") as fh:
        json.dump(best, fh)
    print(f"{out.relative_to(ROOT)}: {len(best)} oracle ids")


if __name__ == "__main__":
    main()
