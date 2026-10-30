#!/usr/bin/env python3
"""Verify primary-source research on a bounded draft/starter product batch.

Inputs are immutable October 29 source snapshots. Existing 12 reviewed items
remain untouched; this produces a separate 23-record overlay and a complete
pending review queue with no inferred Wizards classification.
"""
import argparse
import json
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data/set_atlas"
BASE = DATA / "product_family_triage_2026-10-29.json"
EVIDENCE = DATA / "draft_starter_primary_sources_2026-10-29.json"
OUT = DATA / "draft_starter_primary_audit_2026-10-29.json"
COHORT = "draft_and_starter_variants"
AS_OF = "2026-10-29"
REQUIRED = {
    "bbd", "clb", "clu", "cmb1", "cmb2", "cn2", "cns", "cp3",
    "dbl", "j25", "jmp", "mbc", "p02", "por", "ptk", "s00", "s99",
    "sunf", "ugl", "und", "unf", "unh", "ust",
}
SPECIAL = {
    "sunf": "component_sticker_sheet",
    "cmb1": "mystery_booster_convention_playtest_sheet",
    "cmb2": "mystery_booster_convention_playtest_sheet",
    "mbc": "commander_draft_standalone_booster_later_card_legality",
    "cp3": "preconstructed_clash_pack",
}
ALLOWED_GROUPS = {
    "two_headed_giant_draft_booster",
    "commander_draft_standalone_booster",
    "commander_draft_standalone_booster_later_card_legality",
    "themed_clue_game_box",
    "mystery_booster_convention_playtest_sheet",
    "multiplayer_conspiracy_draft_booster",
    "preconstructed_clash_pack",
    "curated_combined_reprint_draft_booster",
    "jumpstart_mix_two_boosters",
    "introductory_simplified_standalone_set",
    "introductory_starter_standalone_product",
    "component_sticker_sheet",
    "un_set_supplemental_booster",
    "un_set_preconstructed_box",
    "un_set_mixed_legality_booster",
}


def encode(value):
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def build(base, evidence):
    if base.get("snapshot_date") != AS_OF or evidence.get("as_of") != AS_OF:
        raise ValueError("Evidence and triage snapshot dates mismatch")
    if base.get("wizards_reviewed_examples") != 12 or base.get("metadata_only_pending_wizards_individual_review") != 836:
        raise ValueError("Prior independently-reviewed baseline changed")
    if base.get("released_nondigital_other_type_codes") != 848:
        raise ValueError("Outside-category denominator changed")

    items = base["all_848_released_nondigital_other_type_records"]
    indexed = {x["code"]: x for x in items}
    if len(indexed) != len(items) or len(indexed) != 848:
        raise ValueError("Input has duplicate or missing Scryfall set codes")
    queue = {
        r["code"] for r in items
        if r["metadata_cohort_not_official_classification"] == COHORT
        and not r["wizards_individual_source_review"]
    }
    if len(queue) != 44:
        raise ValueError(f"Expected exactly 44 source-pending draft/starter codes, got {len(queue)}")
    reviewed = []
    counts = Counter()
    seen = set()
    for row in evidence.get("records", []):
        code = row.get("code")
        if code in seen:
            raise ValueError(f"Duplicate sourced code: {code}")
        if code not in queue:
            raise ValueError(f"Outside draft/starter pending queue or previously reviewed code: {code}")
        group = row.get("group")
        if group not in ALLOWED_GROUPS:
            raise ValueError(f"Unsupported or unrecognized product-family claim for {code}")
        url = row.get("source_url", "")
        parsed = urlparse(url)
        if parsed.scheme != "https" or parsed.hostname not in ("magic.wizards.com", "www.magic.wizards.com"):
            raise ValueError(f"Official Wizards URL required for {code}")
        if not row.get("source_section") or len(row.get("reason", "")) < 25:
            raise ValueError(f"Missing primary-source excerpt description for {code}")
        if code in SPECIAL and group != SPECIAL[code]:
            raise ValueError(f"Auxiliary or legality caveat for {code} was improperly reclassified")
        s = indexed[code]
        if s["premier_release_status"] != "not_inferred_from_set_type":
            raise ValueError(f"Scryfall record incorrectly claims premier certainty: {code}")
        seen.add(code)
        counts[group] += 1
        reviewed.append({
            "code": code, "name": s["name"],
            "scryfall_type": s["scryfall_set_type"],
            "cohort_from_metadata": COHORT,
            "release_or_first_card_date_from_scryfall": s["scryfall_release_or_first_card_date"],
            "parent_set_code_explicit_only": s["parent_set_code_explicit_only"],
            "wizards_source_review": "direct_official_product_source",
            "wizards_product_group": group,
            "wizards_source_url": url,
            "wizards_source_section": row["source_section"],
            "evidence_note": row["reason"],
            "regular_premier_release_certified": False,
            "new_card_legality_date_claim": (
                {"commander": "2026-11-13", "legacy_vintage_eternal": "2027-01-01",
                 "source": url, "note": "MBC set date 2026-10-19 is not the new cards' legality date"}
                if code == "mbc" else None
            ),
        })
    if seen != REQUIRED or len(reviewed) != 23:
        raise ValueError(f"Source review must cover exactly 23 expected codes; missing {sorted(REQUIRED-seen)}")

    pending = [
        {"code": r["code"], "name": r["name"], "scryfall_type": r["scryfall_set_type"],
         "release_date": r["scryfall_release_or_first_card_date"],
         "explicit_parent_set_code": r["parent_set_code_explicit_only"],
         "research_priority": r["research_priority_1_highest"]}
        for r in items if r["code"] not in seen and not r["wizards_individual_source_review"]
    ]
    pending.sort(key=lambda x: (x["research_priority"], x["scryfall_type"],
                                x["release_date"] or "", x["code"]))
    draft_remaining = sorted(queue-seen)
    if len(draft_remaining) != 21 or len(pending) != 813:
        raise ValueError("Source coverage counts or conservation failed")
    if not any(x["code"] == "mbc" for x in reviewed):
        raise ValueError("Missing MBC source-level release vs legality exception")
    original = {x["code"] for x in items if x["wizards_individual_source_review"]}
    if seen & original:
        raise ValueError("Previously reviewed codes were overwritten")
    if len(original) + len(seen) + len(pending) != 848:
        raise ValueError("Cumulative reviews and pending do not conserve the 848 set codes")

    return {
        "schema": 1, "snapshot_date": AS_OF,
        "source_ledger": EVIDENCE.name, "prior_triage": BASE.name,
        "review_definition": "Specific Wizards primary article supports a product-family claim; no implied premier/legality classification",
        "reviewed_batch_size": len(seen),
        "cumulative_wizards_source_reviewed_other_category_codes": len(original)+len(seen),
        "cumulative_source_pending_other_category_codes": len(pending),
        "draft_starter_reviewed_prior": 7,
        "draft_starter_reviewed_this_batch": len(seen),
        "draft_starter_pending_after_batch": len(draft_remaining),
        "draft_starter_pending_codes": draft_remaining,
        "source_verified_product_groups_in_batch": dict(sorted(counts.items())),
        "newly_wizards_reviewed": sorted(reviewed, key=lambda x: x["code"]),
        "remaining_source_pending_queue_all_other_categories": pending,
        "limitations": [
            "23 exact source-backed products were reviewed; remaining 21 draft/starter codes are NOT individually certified.",
            "Earlier 12 individually-reviewed set codes were preserved unchanged; cumulative reviewed is 35 out of 848.",
            "Some products have a Scryfall set code solely for sheets, inserts, or prints and are not standalone released boosters.",
            "Separate Wizards product-family assertions do not certify Standard, Commander, or premier legality.",
            "For MBC, Wizards states new-to-Magic cards only become Commander legal November 13, 2026, despite an earlier Scryfall set-level first-card date.",
            "All counts and timestamps are frozen October 29 data, not a fresh 2027/current dataset.",
        ],
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--write", action="store_true")
    args = p.parse_args()
    result = build(json.loads(BASE.read_text(encoding="utf-8")),
                   json.loads(EVIDENCE.read_text(encoding="utf-8")))
    serialized = encode(result)
    if args.write:
        OUT.write_bytes(serialized)
    elif not OUT.exists() or OUT.read_bytes() != serialized:
        raise ValueError("Committed draft/starter primary-source audit absent or differs from strict deterministic output")
    print(json.dumps({
        "reviewed_this_batch": result["reviewed_batch_size"],
        "reviewed_total_other_type": result["cumulative_wizards_source_reviewed_other_category_codes"],
        "pending_total_other_type": result["cumulative_source_pending_other_category_codes"],
        "draft_pending": result["draft_starter_pending_after_batch"],
        "draft_codes_pending": result["draft_starter_pending_codes"],
    }, indent=2))


if __name__ == "__main__":
    main()
