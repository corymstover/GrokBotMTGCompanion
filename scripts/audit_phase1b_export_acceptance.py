#!/usr/bin/env python3
"""End-to-end, offline export acceptance for every published historical set code.

Checks all set/card index rows and every set export from October 28 committed
shards, using October 29, 2026 as the default released English-paper cutoff.
Does not assert exact card-ID equality with the separate October 29 bulk file.
"""
import argparse
import csv
import io
import json
from collections import Counter
from datetime import date
from pathlib import Path

from export_phase1b_set_cards import export_set, format_export
from historical_set_lookup import DATA, load

ROOT = Path(__file__).resolve().parent.parent
HIST = DATA / "historical_shard_audit_2026-10-29.json"
FAST = DATA / "phase1b_fasttrack_readiness_2026-10-29.json"
CURRENT = DATA / "catalog_2026-10-29.json"
OUTPUT = DATA / "phase1b_export_acceptance_2026-10-29.json"
BUCKETS = "0123456789abcdef"
CUTOFF = date(2026, 10, 29)
PRINTING_TOTAL = 119509
ORACLE_TOTAL = 39099
ENGLISH_PAPER_TOTAL = 107700
RELEASED_ENGLISH_PAPER_TOTAL = 106855


def encode(obj):
    return (json.dumps(obj, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def build(hist, fast, current, folder=DATA):
    if (hist["cutoff"], fast["as_of"], current["as_of"]) != (CUTOFF.isoformat(),) * 3:
        raise ValueError("Historical, fast-track and current audits have different cutoffs")
    if (hist["printing_ids"], hist["stable_oracle_ids_indexed"], hist["english_paper"],
            hist["released_english_paper"]) != (PRINTING_TOTAL, ORACLE_TOTAL,
                                               ENGLISH_PAPER_TOTAL, RELEASED_ENGLISH_PAPER_TOTAL):
        raise ValueError("Archived historical printing/identity manifest drift")
    if fast["released_english_paper_as_of_cutoff"] != RELEASED_ENGLISH_PAPER_TOTAL:
        raise ValueError("Fast-track aggregate parity checkpoint changed")
    if set(current["sets"]) != set(hist["per_set"]) or len(current["sets"]) != 1062:
        raise ValueError("Published set-code sets do not match current catalog")

    printing_by_id, per_set_codes = {}, set()
    total_paper = total_released = 0
    for bucket in BUCKETS:
        groups = load(bucket, "sets", folder)
        for code, rows in groups.items():
            if code in per_set_codes or code not in hist["per_set"]:
                raise ValueError(f"Unknown or duplicate set-code bucket: {code}")
            per_set_codes.add(code)
            counts = Counter()
            for row in rows:
                if len(row) != 7 or not row[0] or row[0] in printing_by_id:
                    raise ValueError(f"Invalid/duplicate printing in {code}")
                printing_by_id[row[0]] = (code, tuple(row))
                counts["all"] += 1
                if row[5] == "en" and row[6]:
                    counts["english_paper"] += 1
                    if row[4] <= CUTOFF.isoformat():
                        counts["released_english_paper"] += 1
            expected = hist["per_set"][code]
            if any(counts[key] != expected.get(key, 0) for key in
                   ("all", "english_paper", "released_english_paper")):
                raise ValueError(f"Set {code}: index counts conflict with the independently audited shard manifest")
            if counts["released_english_paper"] != current["sets"][code]["released_english_paper"]:
                raise ValueError(f"Set {code}: released English-paper count differs from current bulk audit")
            total_paper += counts["english_paper"]
            total_released += counts["released_english_paper"]
    if (len(printing_by_id), len(per_set_codes), total_paper, total_released) != (
            PRINTING_TOTAL, 1062, ENGLISH_PAPER_TOTAL, RELEASED_ENGLISH_PAPER_TOTAL):
        raise ValueError("Whole-index printing and set bucket conservation failed")

    linked_printing_ids, oracle_ids = set(), set()
    for bucket in BUCKETS:
        histories = load(bucket, "cards", folder)
        for oid, rows in histories.items():
            if not oid or oid[0].lower() != bucket or oid in oracle_ids:
                raise ValueError(f"Misplaced or repeated Oracle identity in bucket {bucket}")
            oracle_ids.add(oid)
            for item in rows:
                if len(item) != 8 or item[2] != oid:
                    raise ValueError(f"Card chronology has malformed printing identity: {oid}")
                code, pid = item[:2]
                if pid in linked_printing_ids or printing_by_id.get(pid) != (code, tuple(item[1:])):
                    raise ValueError(f"Card-to-set chronology does not reverse-match printing {pid}")
                linked_printing_ids.add(pid)
    if len(oracle_ids) != ORACLE_TOTAL or linked_printing_ids != set(printing_by_id):
        raise ValueError("Bidirectional card-to-set index is incomplete")

    exports, empties, exported_printing_rows, exported_identity_rows, checked = [], [], 0, 0, 0
    for code in sorted(per_set_codes):
        printings = export_set(code, mode="printings", cutoff=CUTOFF, folder=folder)
        unique = export_set(code, mode="unique", cutoff=CUTOFF, folder=folder)
        expected = hist["per_set"][code].get("released_english_paper", 0)
        if (printings["printing_records"] != expected or
                len(printings["rows"]) != expected or
                unique["printing_records"] != expected or
                unique["distinct_identities_or_unresolved"] != len(unique["rows"])):
            raise ValueError(f"Full printing or unique-card export not available for set {code}")
        if sum(row["printings_in_set"] for row in unique["rows"]) != expected:
            raise ValueError(f"Unique-card export failed to conserve all printing rows in {code}")
        if any(r["language"] != "en" or not r["paper"] or r["released_at"] > CUTOFF.isoformat()
               for r in printings["rows"]):
            raise ValueError(f"Default export unexpectedly includes foreign/digital/future records in {code}")
        # Verify the emitted CSV itself, including quoting/escapes and header-only empty sets.
        csv_rows = list(csv.DictReader(io.StringIO(format_export(printings, "csv"))))
        if len(csv_rows) != expected:
            raise ValueError(f"CSV serialization lost printing rows for {code}")
        checked += 1
        if not expected:
            empties.append(code)
        exported_printing_rows += expected
        exported_identity_rows += len(unique["rows"])
        if code in {"lea", "leg", "c21", "40k", "pznr", "tfin", "ydmu", "trk", "fbb"}:
            exports.append({"code": code, "printing_rows": expected, "unique_cards": len(unique["rows"])})
    if exported_printing_rows != RELEASED_ENGLISH_PAPER_TOTAL:
        raise ValueError("Complete exported English-paper rows differ from dated manifest")
    return {
        "schema": 1, "as_of": CUTOFF.isoformat(),
        "source": "2026-10-28 committed historical printing index; October 29 aggregate comparison only",
        "all_set_codes_full_export_checked": checked,
        "historical_printing_ids_reverse_joined": len(linked_printing_ids),
        "stable_oracle_ids_reverse_joined": len(oracle_ids),
        "released_english_paper_printing_rows_exported": exported_printing_rows,
        "per_set_unique_card_export_rows": exported_identity_rows,
        "set_codes_with_zero_default_released_paper_rows": len(empties),
        "zero_default_released_paper_examples": [x for x in ("trk", "ydmu", "fbb") if x in empties],
        "representative_sets": exports,
        "all_1062_printing_and_unique_card_exports": "PASS",
        "all_119509_set_to_card_and_card_to_set_printing_ID_joins": "PASS",
        "filter_policy": "English paper and released by October 29, 2026 by default; foreign, digital, future entries only by explicit flags",
        "remaining_known_limitations": [
            "The exact October 29 Scryfall printing-ID corpus is not present in this GitHub-readable index; per-set count parity is not exact new-vs-old ID parity.",
            "This audit does not certify complete foreign-language, future-preview or digital-first printing inventory in the default English-paper export.",
            "Individual product families still needing direct Wizards primary-source review remain a separate nonblocking research queue of 555 records."
        ]
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--write", action="store_true")
    args = p.parse_args()
    report = build(*(json.loads(path.read_text(encoding="utf-8"))
                     for path in (HIST, FAST, CURRENT)))
    payload = encode(report)
    if args.write:
        OUTPUT.write_bytes(payload)
    elif not OUTPUT.exists() or OUTPUT.read_bytes() != payload:
        raise ValueError("Phase 1B full export acceptance not reproducible from committed indexes")
    print(json.dumps({k: report[k] for k in (
        "all_set_codes_full_export_checked", "historical_printing_ids_reverse_joined",
        "stable_oracle_ids_reverse_joined", "released_english_paper_printing_rows_exported",
        "set_codes_with_zero_default_released_paper_rows")}, sort_keys=True))


if __name__ == "__main__":
    main()
