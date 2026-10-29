#!/usr/bin/env python3
"""Audit GrokBot's recoverable Wizards story cache without publishing source text.

The historical fetcher stores copyrighted article bodies under .cache/story/.
This independent stdlib-only checker inventories those files, verifies that a
cached page belongs to its source URL, and flags unexpectedly short extracts.
Only URLs, dates, titles, counts, hashes and diagnoses enter the JSON report.

  python3 scripts/story_cache_audit.py --json
  python3 scripts/story_cache_audit.py --strict
  python3 scripts/story_cache_audit.py --output /tmp/story-audit.json
"""

import argparse
import ast
import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "scripts" / "fetch_story_pages.py"
PRIMARY = ROOT / "data" / "primary_sources.csv"
EXTRA = ROOT / "data" / "story_extra_sources.csv"
CACHE = ROOT / ".cache" / "story"


def article_urls(script=SOURCE):
    """Read the fetcher's literal article inventory without importing bs4 or network code."""
    tree = ast.parse(script.read_text(encoding="utf-8"))
    for statement in tree.body:
        if isinstance(statement, ast.Assign) and any(
            isinstance(t, ast.Name) and t.id == "ARTICLES" for t in statement.targets
        ):
            value = ast.literal_eval(statement.value)
            if not isinstance(value, list) or not all(isinstance(u, str) for u in value):
                raise ValueError("ARTICLES must be a literal URL list")
            return value
    raise ValueError("fetch_story_pages.py ARTICLES list not found")


def inventory(primary=PRIMARY, extra=EXTRA, articles=None):
    if articles is None:
        articles = article_urls()
    jobs = []
    with primary.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            jobs.append({"kind": "story", "url": row["url"],
                         "reference_words": int(row["words"]) if row.get("words") else None,
                         "arc": row.get("arc", "")})
    for url in articles:
        jobs.append({"kind": "article", "url": url, "reference_words": None, "arc": ""})
    if extra.exists():
        with extra.open(encoding="utf-8", newline="") as handle:
            for row in csv.DictReader(handle):
                jobs.append({"kind": "extra", "url": row["url"],
                             "reference_words": None, "arc": row.get("kind", "")})
    return jobs


def cache_path(job, root=CACHE):
    directory = {"story": "text22", "article": "articles", "extra": "extra"}[job["kind"]]
    return root / directory / (job["url"].rstrip("/").split("/")[-1] + ".txt")


def check_job(job, root=CACHE):
    path = cache_path(job, root)
    result = {"kind": job["kind"], "url": job["url"],
              "arc": job.get("arc", ""), "reference_words": job.get("reference_words"),
              "status": "missing"}
    if not path.exists():
        return result
    raw = path.read_bytes()
    result["sha256"] = hashlib.sha256(raw).hexdigest()
    try:
        page = raw.decode("utf-8")
    except UnicodeDecodeError:
        result["status"] = "invalid-encoding"
        return result
    header, sep, body = page.partition("\n\n")
    fields = dict(re.findall(r"^(URL|TITLE|DATE):\s*(.*)$", header, flags=re.M))
    result["title"] = fields.get("TITLE", "")
    result["published"] = fields.get("DATE", "")
    result["words"] = len(body.split()) if sep else 0
    if not sep or fields.get("URL", "").rstrip("/") != job["url"].rstrip("/"):
        result["status"] = "invalid-source"
    elif result["words"] == 0:
        result["status"] = "empty-body"
    elif result["words"] < (max(12, int(job["reference_words"] * 0.25))
                            if job.get("reference_words") is not None else 40):
        result["status"] = "suspect-short"
    else:
        result["status"] = "present"
    return result


def audit(jobs, root=CACHE):
    paths = [str(cache_path(job, root)) for job in jobs]
    duplicates = [p for p, n in Counter(paths).items() if n > 1]
    records = [check_job(job, root) for job in jobs]
    counts = Counter(record["status"] for record in records)
    return {"schema": "story-cache-audit/v1", "source": "Wizards primary-source URL inventories",
            "source_text_embedded": False, "total": len(records),
            "counts": dict(sorted(counts.items())),
            "colliding_cache_paths": duplicates, "records": records}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="print metadata-only JSON instead of summary")
    parser.add_argument("--output", type=Path, help="write metadata-only JSON to a chosen path")
    parser.add_argument("--strict", action="store_true", help="fail on missing, corrupt or suspicious sources")
    args = parser.parse_args(argv)
    report = audit(inventory())
    data = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(data, encoding="utf-8")
    if args.json:
        print(data, end="")
    else:
        print(f"Official story cache: {report['total']} inventoried URLs")
        for status, number in report["counts"].items():
            print(f"  {status}: {number}")
        if report["colliding_cache_paths"]:
            print(f"  WARNING: {len(report['colliding_cache_paths'])} colliding cache path(s)")
    return int(args.strict and (
        bool(report["colliding_cache_paths"]) or
        any(row["status"] != "present" for row in report["records"])))


if __name__ == "__main__":
    raise SystemExit(main())
