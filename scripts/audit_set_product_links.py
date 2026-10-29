#!/usr/bin/env python3
"""Phase 1B: dated, source-backed Scryfall set/product metadata.

Fetch ONCE with --fetch-write, committing a compact raw metadata snapshot.
Every normal --check replays from that frozen file with no network calls.
Parent links are only copied from Scryfall parent_set_code, never guessed.
Scryfall expansion/core is a category, NOT proof of "premier" release status.
"""
import argparse
import hashlib
import json
import urllib.request
from collections import Counter
from datetime import date, datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data/set_atlas"
AS_OF = date(2026, 10, 29)
ENDPOINT = "https://api.scryfall.com/sets"
SOURCE = DATA / "scryfall_set_metadata_2026-10-29.json"
CATALOG = DATA / "product_catalog_2026-10-29.json"
REPORT = DATA / "product_audit_2026-10-29.json"
FIELDS = ("id", "code", "name", "set_type", "released_at",
          "parent_set_code", "block", "block_code", "digital",
          "card_count", "printed_size", "scryfall_uri", "uri")


def encode(obj):
    return (json.dumps(obj, sort_keys=True, indent=1, ensure_ascii=False) + "\n").encode("utf-8")


def clean(records):
    result = []
    codes = set()
    for item in records:
        if not isinstance(item, dict):
            raise ValueError("Scryfall set response contains non-object")
        code = item.get("code")
        if not isinstance(code, str) or not code or code != code.lower() or code in codes:
            raise ValueError(f"Missing, nonnormalized or duplicated Scryfall set code: {code!r}")
        if not all(item.get(k) is not None for k in ("id", "name", "set_type", "card_count", "digital")):
            raise ValueError(f"{code}: missing required set metadata")
        if not isinstance(item["card_count"], int) or item["card_count"] < 0:
            raise ValueError(f"{code}: invalid set card_count")
        if not isinstance(item["digital"], bool):
            raise ValueError(f"{code}: digital flag must be Boolean")
        if item.get("released_at"):
            date.fromisoformat(item["released_at"])
        codes.add(code)
        result.append({key: item[key] for key in FIELDS if key in item})
    return sorted(result, key=lambda x: x["code"])


def fetch_source():
    req = urllib.request.Request(ENDPOINT, headers={
        "Accept": "application/json;q=0.9,*/*;q=0.8",
        "User-Agent": "MTGMultiverseCompanion/1.0 (research archive; https://github.com/corymstover/GrokBotMTGCompanion)"
    })
    with urllib.request.urlopen(req, timeout=90) as stream:
        data = json.load(stream)
    if data.get("object") != "list" or not isinstance(data.get("data"), list):
        raise ValueError("Unexpected Scryfall /sets response")
    if data.get("has_more"):
        raise ValueError("Scryfall /sets response unexpectedly paginated; do not publish incomplete list")
    return {
        "schema": 1, "fetched_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "snapshot_date": AS_OF.isoformat(), "source_url": ENDPOINT,
        "scryfall_sets": clean(data["data"]),
    }


def build(source, atlas):
    if source.get("source_url") != ENDPOINT or source.get("snapshot_date") != AS_OF.isoformat():
        raise ValueError("Set source provenance/date does not match this frozen atlas")
    raw_records = source.get("scryfall_sets")
    sets = clean(raw_records)
    if sets != raw_records:
        raise ValueError("Saved source metadata is not normalized; refuse silent mutation")
    known = {s["code"]: s for s in sets}
    published = atlas["sets"]
    result, parents, warnings, counts = {}, [], [], Counter()
    candidate_types = ("expansion", "core")
    for code, record in sorted(published.items()):
        meta = known.get(code)
        if meta is None:
            result[code] = {"name_at_printing_snapshot": record["name"],
                            "set_type_at_printing_snapshot": record["set_type"],
                            "scryfall_set_metadata_missing": True}
            warnings.append({"code": code, "issue": "code missing from /sets metadata"})
            continue
        if record["name"] != meta["name"]:
            warnings.append({"code": code, "issue": "name differs between printing snapshot and set API",
                             "printing_name": record["name"], "set_api_name": meta["name"]})
        if record["set_type"] != meta["set_type"]:
            warnings.append({"code": code, "issue": "set_type changed between snapshots",
                             "printing_type": record["set_type"], "set_api_type": meta["set_type"]})
        day = date.fromisoformat(meta["released_at"]) if meta.get("released_at") else None
        state = ("undated" if day is None else "announced_future" if day > AS_OF else "released_by_cutoff")
        parent = meta.get("parent_set_code")
        if parent == code:
            raise ValueError(f"{code}: self-referential parent_set_code")
        if parent:
            parents.append({"child": code, "parent": parent,
                            "parent_in_printing_atlas": parent in published,
                            "parent_in_scryfall_set_snapshot": parent in known,
                            "relation_source": "Scryfall Set.parent_set_code"})
        counts["all_codes"] += 1
        counts["set_type:" + meta["set_type"]] += 1
        counts["release_status:" + state] += 1
        counts["digital_only_set_flag"] += int(meta["digital"])
        counts["parent_links"] += int(bool(parent))
        if (meta["set_type"] in candidate_types and
                not meta["digital"] and state == "released_by_cutoff"):
            counts["released_nondigital_expansion_core_candidates_NOT_premier_certification"] += 1
        result[code] = {
            "name": meta["name"], "scryfall_set_id": meta["id"], "scryfall_uri": meta.get("scryfall_uri"),
            "scryfall_set_type": meta["set_type"], "released_at": meta.get("released_at"),
            "release_status_as_of_cutoff": state, "digital_only": meta["digital"],
            "parent_set_code": parent, "block": meta.get("block"), "block_code": meta.get("block_code"),
            "scryfall_card_count_at_fetch": meta["card_count"],
            "scryfall_printed_size": meta.get("printed_size"),
            "printing_records_in_oct29_default_cards": record["printings"],
            "released_distinct_oracle_ids_in_oct29_default_cards": record["released_distinct_oracle_ids"],
            "set_category_source": "Scryfall", "parent_relation_source": "Scryfall Set.parent_set_code",
            "premier_release_status": "not_independently_certified"
        }
    if len(result) != len(published):
        raise ValueError("Missing published set codes in derived catalog")
    source_hash = hashlib.sha256(encode(source)).hexdigest()
    catalog = {
        "schema": 1, "snapshot_date": AS_OF.isoformat(), "set_api_fetched_utc": source["fetched_utc"],
        "source_uri": ENDPOINT, "source_metadata_sha256": source_hash,
        "oracle_printing_source_sha256": atlas["source_sha256"],
        "sets": result
    }
    summary = {
        "schema": 1, "snapshot_date": AS_OF.isoformat(),
        "metadata_fetched_utc": source["fetched_utc"], "metadata_source": ENDPOINT,
        "source_metadata_sha256": source_hash, "printing_atlas_codes": len(published),
        "api_set_codes_at_fetch": len(sets), "mapped_codes": sum(not x.get("scryfall_set_metadata_missing") for x in result.values()),
        "counts": dict(sorted(counts.items())),
        "direct_parent_relationships": sorted(parents, key=lambda p: (p["child"], p["parent"])),
        "warnings": warnings,
        "count_limitations": [
            "Scryfall /sets metadata is fetched on the recorded timestamp, not assumed frozen with the October 29 Default Cards snapshot.",
            "A set_type of expansion or core is not a Wizards-certified list of premier sets.",
            "Scryfall card_count and printed_size are product metadata, not equal to Default Cards printing rows or distinct Oracle identities.",
            "Only explicit Scryfall parent_set_code relationships are reported. Missing parent links must not be guessed from name or prefix.",
            "Scryfall released_at is set release or first-card date; it is distinct from individual card printing dates.",
            "Future-dated sets are announced products, not yet released as of the cutoff."
        ]
    }
    return catalog, summary


def render(source_path=SOURCE, out_catalog=CATALOG, out_report=REPORT, write=False):
    source = json.loads(source_path.read_text(encoding="utf-8"))
    atlas = json.loads((DATA / "catalog_2026-10-29.json").read_text(encoding="utf-8"))
    catalog, summary = build(source, atlas)
    for file, data in ((out_catalog, catalog), (out_report, summary)):
        b = encode(data)
        if write:
            file.write_bytes(b)
        elif not file.exists() or file.read_bytes() != b:
            raise ValueError(f"{file.name} differs from reproducible frozen-set-metadata output")
    print(json.dumps({"mapped": summary["mapped_codes"], "printing_atlas_codes": summary["printing_atlas_codes"],
                      "source_set_codes": summary["api_set_codes_at_fetch"],
                      "explicit_parent_relations": len(summary["direct_parent_relationships"]),
                      "warnings": len(summary["warnings"]),
                      "candidate_non_digital_expansion_core":
                          summary["counts"].get("released_nondigital_expansion_core_candidates_NOT_premier_certification", 0)},
                     sort_keys=True))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--fetch-write", action="store_true", help="one live API fetch; write frozen metadata and derived reports")
    p.add_argument("--check", action="store_true", help="default: strictly compare against committed, frozen output")
    args = p.parse_args()
    if args.fetch_write:
        DATA.mkdir(parents=True, exist_ok=True)
        if SOURCE.exists():
            raise ValueError("Snapshot already exists; do not replace a frozen metadata archive")
        SOURCE.write_bytes(encode(fetch_source()))
        render(write=True)
    else:
        render(write=False)


if __name__ == "__main__":
    main()
