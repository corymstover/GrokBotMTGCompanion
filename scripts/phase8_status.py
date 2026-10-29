#!/usr/bin/env python3
"""Read-only, source-of-truth Phase 8 coverage report.

Unlike the historical README dashboard, this reads the generated enrichment
artifact directly. It makes no new card or canon claims, writes no files, and
does not depend on the old GrokBot scratch/cache directories.

Usage: python3 scripts/phase8_status.py [--json] [--strict]
"""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DATA = ROOT / "data" / "card_enrichment.json"
IMPORTANT_TIERS = ("priority pool (any tier)", "legendary-creature", "planeswalker",
                   "story-flavor", "character-card", "entry-linked")


def summarize(data):
    """Calculate numbers from generated data, not from old notes or README."""
    if not isinstance(data.get("cards"), dict) or not isinstance(data.get("coverage"), dict):
        raise ValueError("Phase 8 artifact lacks cards/coverage mappings")
    tiers = {}
    for tier in IMPORTANT_TIERS:
        row = data["coverage"].get(tier)
        if row is None:
            continue
        size, enriched = row.get("size"), row.get("enriched")
        if not isinstance(size, int) or not isinstance(enriched, int) or not 0 <= enriched <= size:
            raise ValueError(f"malformed coverage for {tier}")
        tiers[tier] = {"total": size, "enriched": enriched, "remaining": size - enriched,
                       "percent": round(100 * enriched / size, 1) if size else 100.0}
    return {"artifact": "data/card_enrichment.json", "source": data.get("generated_by"),
            "total_enrichment_records": len(data["cards"]),
            "batches": data.get("batches", []), "coverage": tiers,
            "caution": "Coverage is measured from the stored artifact; it is not proof of canon accuracy or current source freshness."}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--strict", action="store_true", help="fail if missing or priority pool incomplete")
    args = parser.parse_args(argv)
    if not args.data.is_file():
        report = {"available": False, "artifact": str(args.data),
                  "warning": "Stored enrichment artifact not in this checkout; coverage cannot be calculated."}
    else:
        try:
            report = {"available": True, **summarize(json.loads(args.data.read_text(encoding="utf-8")))}
        except (ValueError, KeyError, json.JSONDecodeError) as exc:
            parser.error(f"invalid enrichment data: {exc}")
    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    elif not report["available"]:
        print(report["warning"])
    else:
        print(f"Phase 8: {report['total_enrichment_records']:,} enrichment records (stored artifact)")
        for tier, row in report["coverage"].items():
            print(f"  {tier}: {row['enriched']:,}/{row['total']:,} ({row['percent']}%), "
                  f"{row['remaining']:,} remaining")
    pool = report.get("coverage", {}).get("priority pool (any tier)")
    return 1 if args.strict and (not report["available"] or (pool and pool["remaining"] > 0)) else 0


if __name__ == "__main__":
    raise SystemExit(main())
