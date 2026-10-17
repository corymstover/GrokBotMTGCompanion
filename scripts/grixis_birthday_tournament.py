#!/usr/bin/env python3
"""Current cEDH meta snapshot for the Birthday authority boundary.

The authority snapshot needs a current, provenance-bearing tournament/meta view, but
it must not eagerly re-query every historical candidate card. Card-level EDHTop16
rows are challenger/review evidence and are refreshed later by the Birthday M5 delta
for the decks/candidates the impact audit says are affected.

This module therefore queries current commander-level ONE_YEAR/SIX_MONTHS stats for
every cEDH-ceiling project deck and records an explicit deferred card-row status.
It is observational evidence only and cannot decide a swap.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import time
from pathlib import Path

import grixis_authority as ga
import grixis_tournament as tr

VERSION = 2
ROOT = Path(__file__).resolve().parent.parent


def sha_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return "sha256:" + h.hexdigest()


def refresh(out_root: Path):
    target = out_root / "tournament"
    target.mkdir(parents=True, exist_ok=True)
    summ = {v["slug"]: v for v in ga.summary().values()}
    old_root = ROOT / "data/grixis/candidates/tournament"
    docs = {}
    problems = []
    today = dt.date.today().isoformat()
    for slug in tr.cedh_slugs():
        v = summ[slug]
        name = " / ".join(sorted(v["commanders"]))
        win = " ".join(f'{w}: stats(filters:{{timePeriod:{w}}}) {{ count topCuts conversionRate metaShare }}' for w in tr.WINDOWS)
        try:
            r = tr.gql(f'{{ commander(name:"{tr.esc(name)}") {{ name colorId {win} }} }}')
            cmd = (r.get("data") or {}).get("commander")
        except Exception as e:
            cmd = None
            problems.append(f"{slug}: EDHTop16 commander query failed: {type(e).__name__}: {e}"[:400])
        doc = {
            "schema_version": 1,
            "generated_by": f"scripts/grixis_birthday_tournament.py v{VERSION}",
            "slug": slug,
            "source": tr.API,
            "commander_query": name,
            "retrieved": today,
            "class": "derived_metric",
            "note": tr.NOTE,
            "card_window": tr.CARD_WINDOW,
            "card_rows_status": "deferred_to_birthday_m5_delta",
            "cards": {},
            "authority": {"can_decide": False, "can_approve_or_lock": False},
        }
        if not cmd or not cmd.get("ONE_YEAR") or not cmd["ONE_YEAR"].get("count"):
            doc.update({"status": "no_data", "sample_size": 0, "window": tr.CARD_WINDOW, "commander": None})
        else:
            doc.update({
                "status": "collected",
                "sample_size": cmd["ONE_YEAR"]["count"],
                "window": tr.CARD_WINDOW,
                "commander": {
                    "name": cmd["name"],
                    "color_id": cmd.get("colorId"),
                    "windows": {w: {k: (round(x, 4) if isinstance(x, float) else x) for k, x in cmd[w].items()} for w in tr.WINDOWS},
                },
            })
        p = target / f"{slug}.json"
        p.write_text(json.dumps(doc, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
        oldp = old_root / p.name
        old = json.loads(oldp.read_text(encoding="utf-8")) if oldp.exists() else None
        docs[slug] = {
            "status": doc["status"], "retrieved": today, "sample_size": doc["sample_size"],
            "old_sample_size": None if old is None else old.get("sample_size"),
            "sample_size_delta": None if old is None else doc["sample_size"] - (old.get("sample_size") or 0),
            "card_rows_status": doc["card_rows_status"],
            "file": str(p.relative_to(ROOT)),
            "sha256": sha_file(p),
            "bytes": p.stat().st_size,
        }
        print(f"  {slug}: {doc['status']}, sample {doc['sample_size']} (card rows deferred)", flush=True)
        time.sleep(0.25)
    return {
        "status": "collected" if not problems else "partial",
        "source": tr.API,
        "class": "derived_metric",
        "problems": problems,
        "decks": docs,
        "counts": {"expected_cedh": len(tr.cedh_slugs()), "collected_files": len(docs)},
        "card_rows_status": "deferred_to_birthday_m5_delta",
        "note": "Current commander/meta stats collected at authority boundary; per-card EDHTop16 rows are refreshed only for affected M5 review work.",
    }
