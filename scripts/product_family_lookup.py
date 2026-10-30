#!/usr/bin/env python3
"""Offline Phase 1B Scryfall product-family research queue lookup.

Research cohort != Wizards-classified product or premier-set determination.
Examples:
  python3 scripts/product_family_lookup.py --summary
  python3 scripts/product_family_lookup.py --cohort draft_and_starter_variants
  python3 scripts/product_family_lookup.py --type masters --only-pending --all
  python3 scripts/product_family_lookup.py --parent afr --all
  python3 scripts/product_family_lookup.py --code ltr
"""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "data/set_atlas/product_family_triage_2026-10-29.json"
SOURCE_REVIEW = ROOT / "data/set_atlas/draft_starter_primary_audit_2026-10-29.json"
SECOND_SOURCE_REVIEW = ROOT / "data/set_atlas/draft_starter_batch2_audit_2026-10-29.json"
REPRINT_SOURCE_REVIEW = ROOT / "data/set_atlas/reprint_curated_source_audit_2026-10-29.json"
BOXED_SOURCE_REVIEW = ROOT / "data/set_atlas/boxed_precon_source_audit_2026-10-29.json"
DUEL_DECKS_SOURCE_REVIEW = ROOT / "data/set_atlas/duel_decks_source_audit_2026-10-29.json"
COMMANDER_SERIES_SOURCE_REVIEW = ROOT / "data/set_atlas/commander_series_source_audit_2026-10-29.json"
COMMANDER_SET_LINKED_SOURCE_REVIEW = ROOT / "data/set_atlas/commander_set_linked_source_audit_2026-10-29.json"
COMMANDER_MODERN_SOURCE_REVIEW = ROOT / "data/set_atlas/commander_modern_source_audit_2026-10-29.json"
BOXED_SPECIALTY_SOURCE_REVIEW = ROOT / "data/set_atlas/boxed_specialty_source_audit_2026-10-29.json"
BOXED_SPECIAL_LAIR_GLOBAL_SOURCE_REVIEW = ROOT / "data/set_atlas/boxed_special_lair_global_audit_2026-10-29.json"
INSERTS_CLASH_SPELLBOOK_SOURCE_REVIEW = ROOT / "data/set_atlas/inserts_clash_spellbook_source_audit_2026-10-29.json"
MASTERPIECE_MEMORABILIA_SOURCE_REVIEW = ROOT / "data/set_atlas/masterpiece_memorabilia_source_audit_2026-10-29.json"
HISTORICAL_PROMO_SERIES_SOURCE_REVIEW = ROOT / "data/set_atlas/historical_promo_series_source_audit_2026-10-29.json"
APAC_LUNAR_YEAR_PROMOS_SOURCE_REVIEW = ROOT / "data/set_atlas/apac_lunar_year_promos_source_audit_2026-10-29.json"
EVENT_COLLAB_PROMOS_SOURCE_REVIEW = ROOT / "data/set_atlas/event_collab_promos_source_audit_2026-10-29.json"
ART_SERIES_SOURCE_REVIEW = ROOT / "data/set_atlas/art_series_primary_source_audit_2026-10-29.json"


def apply_source_overlay(data, verified):
    """Use source-backed verified additions without rewriting the dated v2.1 triage."""
    if verified["snapshot_date"] != data["snapshot_date"]:
        raise ValueError("Product review overlay snapshot/date mismatch")
    updates = {x["code"]: x for x in verified["newly_wizards_reviewed"]}
    if len(updates) != verified["reviewed_batch_size"] or len(updates) != 23:
        raise ValueError("Incomplete duplicate or malformed source review overlay")
    entries = []
    patched = set()
    for entry in data["all_848_released_nondigital_other_type_records"]:
        new = dict(entry)
        src = updates.get(new["code"])
        if src is not None:
            if new["wizards_individual_source_review"] or src["scryfall_type"] != new["scryfall_set_type"]:
                raise ValueError(f"Source review overwrite or category mismatch: {new['code']}")
            new["wizards_individual_source_review"] = True
            new["review_status"] = "wizards_primary_source_batch_reviewed"
            new["wizards_primary_source"] = src["wizards_source_url"]
            new["wizards_review_product_group"] = src["wizards_product_group"]
            new["verified_evidence_note"] = src["evidence_note"]
            new["new_card_legality_date_claim"] = src.get("new_card_legality_date_claim")
            patched.add(new["code"])
        entries.append(new)
    if patched != set(updates):
        raise ValueError(f"Source overlay contains nonmatching codes: {sorted(set(updates) - patched)}")
    revised = dict(data)
    revised["all_848_released_nondigital_other_type_records"] = entries
    revised["wizards_reviewed_examples"] = verified["cumulative_wizards_source_reviewed_other_category_codes"]
    revised["metadata_only_pending_wizards_individual_review"] = verified["cumulative_source_pending_other_category_codes"]
    revised["cohort_review_progress"] = {}
    for cohort in data["metadata_research_cohorts"]:
        members = [x for x in entries
                   if x["metadata_cohort_not_official_classification"] == cohort]
        revised["cohort_review_progress"][cohort] = {
            "codes": len(members),
            "wizards_reviewed": sum(bool(x["wizards_individual_source_review"]) for x in members),
            "needs_individual_review": sum(not x["wizards_individual_source_review"] for x in members),
            "explicit_parent_links": sum(bool(x["parent_set_code_explicit_only"]) for x in members),
        }
    if len(entries) != 848 or len([x for x in entries if x["wizards_individual_source_review"]]) != 35:
        raise ValueError("Cumulative reviewed code conservation failed")
    return revised


def apply_second_source_overlay(data, verified):
    """Add eight graded product-family citations without changing prior snapshots."""
    if verified["cutoff"] != data["snapshot_date"]:
        raise ValueError("Review dates incompatible")
    updates = {x["code"]: x for x in verified["newly_sourced_family_evidence"]}
    if len(updates) != verified["new_wizards_family_evidence_count"] or len(updates) != 8:
        raise ValueError("New review contains duplicated or absent source codes")
    patched = set()
    result = []
    for item in data["all_848_released_nondigital_other_type_records"]:
        record = dict(item)
        src = updates.get(record["code"])
        if src:
            if record["wizards_individual_source_review"]:
                raise ValueError(f"Attempt to replace previous official review: {record['code']}")
            if src["scryfall_set_type"] != record["scryfall_set_type"]:
                raise ValueError(f"Official reviewed category drift for {record['code']}")
            record.update({
                "wizards_individual_source_review": True,
                "review_status": "wizards_family_source_with_evidence_grade",
                "wizards_primary_source": src["direct_official_article_url"],
                "wizards_review_product_group": src["product_family_wizards_supported"],
                "wizards_source_grade": src["wizards_family_evidence_grade"],
                "wizards_code_explicitly_confirmed": src["wizards_explicitly_printed_set_code"],
                "verified_evidence_note": src["wizards_article_supports"],
            })
            patched.add(record["code"])
        result.append(record)
    if patched != set(updates) or len(result) != 848:
        raise ValueError("Graded citations do not match existing Scryfall codes")
    current = dict(data)
    current["all_848_released_nondigital_other_type_records"] = result
    current["wizards_reviewed_examples"] = verified[
        "cumulative_outside_category_codes_with_wizards_source_family_evidence"]
    current["metadata_only_pending_wizards_individual_review"] = verified[
        "cumulative_outside_category_codes_individual_wizards_source_pending"]
    current["cohort_review_progress"] = {}
    for cohort in data["metadata_research_cohorts"]:
        members = [r for r in result if r["metadata_cohort_not_official_classification"] == cohort]
        current["cohort_review_progress"][cohort] = {
            "codes": len(members),
            "wizards_reviewed": sum(bool(r["wizards_individual_source_review"]) for r in members),
            "needs_individual_review": sum(not r["wizards_individual_source_review"] for r in members),
            "explicit_parent_links": sum(bool(r["parent_set_code_explicit_only"]) for r in members),
        }
    if sum(bool(r["wizards_individual_source_review"]) for r in result) != 43:
        raise ValueError("Cumulative official source records not 43")
    return current


def apply_reprint_source_overlay(data, report):
    """Only update the exact 28 new Wizards-family cited codes; preserve history."""
    if report["cutoff"] != data["snapshot_date"]:
        raise ValueError("Incompatible research snapshot")
    rows = {x["code"]:x for x in report["newly_sourced_family_evidence"]}
    if len(rows) != report["source_reviewed_this_batch"] or len(rows) != 28:
        raise ValueError("Unexpected duplicate/missing reprint source rows")
    result = []
    changed = set()
    for record in data["all_848_released_nondigital_other_type_records"]:
        item = dict(record)
        src = rows.get(item["code"])
        if src:
            if item["wizards_individual_source_review"]:
                raise ValueError(f"Cannot replace previously verified review: {item['code']}")
            if item["scryfall_set_type"] != src["scryfall_set_type"]:
                raise ValueError(f"Scryfall category changed for {item['code']}")
            item.update({
                "wizards_individual_source_review": True,
                "review_status": "wizards_reprint_curated_product_family_reviewed",
                "wizards_primary_source": src["wizards_source_url"],
                "wizards_review_product_group": src["wizards_product_family"],
                "wizards_source_grade": src["evidence_grade"],
                "wizards_code_explicitly_confirmed": src["wizards_explicit_scryfall_code"],
                "verified_evidence_note": src["source_note"],
                "wizards_premier_status_certified": False
            })
            changed.add(item["code"])
        result.append(item)
    if changed != set(rows) or len(result) != 848:
        raise ValueError("Review overlay failed total exact-code coverage")
    out = dict(data)
    out["all_848_released_nondigital_other_type_records"] = result
    out["wizards_reviewed_examples"] = report["cumulative_wizards_family_evidence_codes"]
    out["metadata_only_pending_wizards_individual_review"] = report["cumulative_pending_codes"]
    out["cohort_review_progress"] = {}
    for cohort in data["metadata_research_cohorts"]:
        members = [r for r in result if r["metadata_cohort_not_official_classification"] == cohort]
        out["cohort_review_progress"][cohort] = {
            "codes": len(members),
            "wizards_reviewed": sum(bool(r["wizards_individual_source_review"]) for r in members),
            "needs_individual_review": sum(not r["wizards_individual_source_review"] for r in members),
            "explicit_parent_links": sum(bool(r["parent_set_code_explicit_only"]) for r in members)
        }
    if sum(bool(r["wizards_individual_source_review"]) for r in result) != 71:
        raise ValueError("Review overlay conservation not 71")
    return out


def apply_boxed_source_overlay(data, review):
    """Overlay fifteen Wizards-backed boxes/component records without rewriting history."""
    if review["cutoff"] != data["snapshot_date"]:
        raise ValueError("Boxed product snapshot mismatch")
    items={r["code"]:r for r in review["reviewed_boxed_codes"]}
    if len(items)!=review["new_source_backed_product_codes"] or len(items)!=15:
        raise ValueError("Boxed review count/uniqueness failed")
    rows=[]
    seen=set()
    for prior in data["all_848_released_nondigital_other_type_records"]:
        row=dict(prior)
        source=items.get(row["code"])
        if source:
            if row["wizards_individual_source_review"]:
                raise ValueError(f"Overwriting earlier product review: {row['code']}")
            if row["scryfall_set_type"]!=source["scryfall_set_type"]:
                raise ValueError(f"Changed Scryfall type for {row['code']}")
            row.update({
                "wizards_individual_source_review":True,
                "review_status":"wizards_boxed_family_product_source_verified",
                "wizards_primary_source":source["wizards_primary_url"],
                "wizards_review_product_group":source["product_group_supported_by_wizards"],
                "verified_evidence_note":source["source_note"],
                "wizards_source_grade":source["evidence_grade"],
                "wizards_code_explicitly_confirmed":False,
                "box_component_of_parent_product":source["component_of_existing_parent_product"],
                "box_or_component_source_class":source["separate_sold_box_vs_card_component"],
                "wizards_premier_status_certified":False
            })
            seen.add(row["code"])
        rows.append(row)
    if seen!=set(items) or len(rows)!=848:
        raise ValueError("Boxed review overlay lost code(s)")
    current=dict(data)
    current["all_848_released_nondigital_other_type_records"]=rows
    current["wizards_reviewed_examples"]=review["cumulative_family_source_backed_codes"]
    current["metadata_only_pending_wizards_individual_review"]=review["cumulative_source_pending_codes"]
    current["cohort_review_progress"]={}
    for cohort in data["metadata_research_cohorts"]:
        members=[r for r in rows if r["metadata_cohort_not_official_classification"]==cohort]
        current["cohort_review_progress"][cohort]={
            "codes":len(members),
            "wizards_reviewed":sum(bool(r["wizards_individual_source_review"]) for r in members),
            "needs_individual_review":sum(not r["wizards_individual_source_review"] for r in members),
            "explicit_parent_links":sum(bool(r["parent_set_code_explicit_only"]) for r in members)
        }
    if sum(bool(r["wizards_individual_source_review"]) for r in rows)!=86:
        raise ValueError("Boxed review total does not conserve 86")
    return current


def apply_duel_decks_source_overlay(data, review):
    """Add 25 historical Duel Decks code reviews, preserving product/box distinctions."""
    if review["cutoff"] != data["snapshot_date"] or data["wizards_reviewed_examples"] != 86:
        raise ValueError("Duel Decks overlay previous checkpoint mismatch")
    updates = {r["code"]: r for r in review["reviewed_duel_decks_codes"]}
    if len(updates) != review["new_source_backed_product_codes"] or len(updates) != 25:
        raise ValueError("Duel Decks evidence missing/duplicated")
    rows = []
    seen = set()
    for previous in data["all_848_released_nondigital_other_type_records"]:
        item = dict(previous)
        src = updates.get(item["code"])
        if src is not None:
            if item["wizards_individual_source_review"]:
                raise ValueError(f"Duel Decks review would overwrite prior evidence: {item['code']}")
            if item["scryfall_set_type"] != src["scryfall_set_type"]:
                raise ValueError(f"Duel Decks Scryfall category drift: {item['code']}")
            if item["parent_set_code_explicit_only"] != src["scryfall_explicit_parent_code_unchanged"]:
                raise ValueError(f"Duel Decks Scryfall parent drift: {item['code']}")
            item.update({
                "wizards_individual_source_review": True,
                "review_status": "wizards_historical_duel_decks_source_verified",
                "wizards_primary_source": src["wizards_primary_url"],
                "wizards_review_product_group": src["wizards_supported_family"],
                "verified_evidence_note": src["source_note"],
                "wizards_source_grade": src["evidence_grade"],
                "wizards_code_explicitly_confirmed": False,
                "box_component_of_parent_product": src["anthology_component_of_one_2014_box"],
                "box_or_component_source_class": (
                    "anthology_catalog_component" if src["anthology_component_of_one_2014_box"]
                    else "boxed_or_collection_release"
                ),
                "wizards_actual_anthology_box": src["wizards_product_relation_not_scryfall_parent"],
                "wizards_anthology_official_product_code": src["anthology_official_box_code_when_component"],
                "wizards_premier_status_certified": False,
            })
            seen.add(item["code"])
        rows.append(item)
    if seen != set(updates) or len(rows) != 848:
        raise ValueError("Duel Decks overlay lost/misclassified code")
    result = dict(data)
    result["all_848_released_nondigital_other_type_records"] = rows
    result["wizards_reviewed_examples"] = review["cumulative_family_source_backed_codes"]
    result["metadata_only_pending_wizards_individual_review"] = review["cumulative_source_pending_codes"]
    result["cohort_review_progress"] = {}
    for cohort in data["metadata_research_cohorts"]:
        members = [row for row in rows if row["metadata_cohort_not_official_classification"] == cohort]
        result["cohort_review_progress"][cohort] = {
            "codes": len(members),
            "wizards_reviewed": sum(bool(row["wizards_individual_source_review"]) for row in members),
            "needs_individual_review": sum(not row["wizards_individual_source_review"] for row in members),
            "explicit_parent_links": sum(bool(row["parent_set_code_explicit_only"]) for row in members),
        }
    if sum(bool(r["wizards_individual_source_review"]) for r in rows) != 111:
        raise ValueError("Duel Decks review total not 111")
    return result


def apply_commander_series_source_overlay(data, review):
    """Source historical annual Commander release families without deck-count claims."""
    if review["cutoff"] != data["snapshot_date"] or data["wizards_reviewed_examples"] != 111:
        raise ValueError("Commander series source overlay prior state changed")
    updates = {x["code"]: x for x in review["reviewed_commander_codes"]}
    if len(updates) != review["new_source_backed_commander_product_family_codes"] or len(updates) != 9:
        raise ValueError("Commander series source overlay duplicate/missing entries")
    patched = set()
    rows = []
    for old in data["all_848_released_nondigital_other_type_records"]:
        row = dict(old)
        source = updates.get(row["code"])
        if source:
            if row["wizards_individual_source_review"]:
                raise ValueError(f"Commander series would overwrite prior review: {row['code']}")
            if row["scryfall_set_type"] != source["scryfall_set_type"]:
                raise ValueError(f"Commander series type changed: {row['code']}")
            if row["parent_set_code_explicit_only"] != source["scryfall_parent_set_code_unchanged"]:
                raise ValueError(f"Commander series parent changed: {row['code']}")
            row.update({
                "wizards_individual_source_review": True,
                "review_status": "wizards_historical_annual_commander_family_source_verified",
                "wizards_primary_source": source["wizards_primary_url"],
                "wizards_review_product_group": source["wizards_supported_family"],
                "verified_evidence_note": source["source_note"],
                "wizards_source_grade": source["evidence_grade"],
                "wizards_code_explicitly_confirmed": False,
                "wizards_premier_status_certified": False,
                "individual_deck_box_count_certified": False,
            })
            patched.add(row["code"])
        rows.append(row)
    if patched != set(updates) or len(rows) != 848:
        raise ValueError("Commander series source overlay lost/changed codes")
    result = dict(data)
    result["all_848_released_nondigital_other_type_records"] = rows
    result["wizards_reviewed_examples"] = review["cumulative_family_source_backed_codes"]
    result["metadata_only_pending_wizards_individual_review"] = review["cumulative_source_pending_codes"]
    result["cohort_review_progress"] = {}
    for cohort in data["metadata_research_cohorts"]:
        members = [row for row in rows if row["metadata_cohort_not_official_classification"] == cohort]
        result["cohort_review_progress"][cohort] = {
            "codes": len(members),
            "wizards_reviewed": sum(bool(row["wizards_individual_source_review"]) for row in members),
            "needs_individual_review": sum(not row["wizards_individual_source_review"] for row in members),
            "explicit_parent_links": sum(bool(row["parent_set_code_explicit_only"]) for row in members),
        }
    if sum(bool(row["wizards_individual_source_review"]) for row in rows) != 120:
        raise ValueError("Commander series source review total is not 120")
    return result


def apply_commander_set_linked_source_overlay(data, review):
    """Overlay twelve Wizards-backed 2020–2022 Commander release families."""
    if review["cutoff"] != data["snapshot_date"] or data["wizards_reviewed_examples"] != 120:
        raise ValueError("Set-linked Commander overlay prior audit mismatch")
    updates = {r["code"]: r for r in review["reviewed_commander_set_linked_codes"]}
    if len(updates) != review["new_source_backed_commander_release_codes"] or len(updates) != 12:
        raise ValueError("Set-linked Commander source codes missing or repeated")
    rows = []
    seen = set()
    for old in data["all_848_released_nondigital_other_type_records"]:
        row = dict(old)
        source = updates.get(row["code"])
        if source:
            if row["wizards_individual_source_review"]:
                raise ValueError(f"Replacing earlier Commander review: {row['code']}")
            if row["scryfall_set_type"] != source["scryfall_type"]:
                raise ValueError(f"Set-linked Commander type drift: {row['code']}")
            if row["parent_set_code_explicit_only"] != source["scryfall_explicit_parent_code_unchanged"]:
                raise ValueError(f"Set-linked Commander parent drift: {row['code']}")
            row.update({
                "wizards_individual_source_review": True,
                "review_status": "wizards_set_linked_commander_product_source_verified",
                "wizards_primary_source": source["wizards_primary_url"],
                "wizards_review_product_group": source["product_family_wizards_supported"],
                "verified_evidence_note": source["wizards_source_note"],
                "wizards_source_grade": source["evidence_grade"],
                "wizards_code_explicitly_confirmed": False,
                "wizards_premier_status_certified": False,
                "exact_deck_printings_certified": False,
                "new_card_count_certified": False,
            })
            seen.add(row["code"])
        rows.append(row)
    if seen != set(updates) or len(rows) != 848:
        raise ValueError("Set-linked Commander source overlay lost a code")
    result = dict(data)
    result["all_848_released_nondigital_other_type_records"] = rows
    result["wizards_reviewed_examples"] = review["cumulative_family_source_backed_codes"]
    result["metadata_only_pending_wizards_individual_review"] = review["cumulative_source_pending_codes"]
    result["cohort_review_progress"] = {}
    for cohort in data["metadata_research_cohorts"]:
        members = [r for r in rows if r["metadata_cohort_not_official_classification"] == cohort]
        result["cohort_review_progress"][cohort] = {
            "codes": len(members),
            "wizards_reviewed": sum(bool(r["wizards_individual_source_review"]) for r in members),
            "needs_individual_review": sum(not r["wizards_individual_source_review"] for r in members),
            "explicit_parent_links": sum(bool(r["parent_set_code_explicit_only"]) for r in members),
        }
    if sum(bool(r["wizards_individual_source_review"]) for r in rows) != 132:
        raise ValueError("Set-linked Commander cumulative reviewed count is not 132")
    return result


def apply_commander_modern_source_overlay(data, review):
    """Add the nineteen remaining Commander-family citations, retaining FDC dates."""
    if review["cutoff"] != data["snapshot_date"] or data["wizards_reviewed_examples"] != 132:
        raise ValueError("Modern Commander overlay historical checkpoint changed")
    sources = {r["code"]: r for r in review["reviewed_commander_modern_codes"]}
    if len(sources) != review["new_source_backed_commander_product_family_codes"] or len(sources) != 19:
        raise ValueError("Modern Commander citations missing or duplicated")
    seen = set()
    rows = []
    for previous in data["all_848_released_nondigital_other_type_records"]:
        row = dict(previous)
        source = sources.get(row["code"])
        if source is not None:
            if row["wizards_individual_source_review"]:
                raise ValueError(f"Modern Commander citation overwrites earlier source: {row['code']}")
            if (row["scryfall_set_type"] != source["scryfall_type"] or
                    row["scryfall_release_or_first_card_date"] != source["scryfall_release_or_first_card_date"] or
                    row["parent_set_code_explicit_only"] != source["scryfall_explicit_parent_code_unchanged"]):
                raise ValueError(f"Modern Commander source changed frozen Scryfall metadata: {row['code']}")
            row.update({
                "wizards_individual_source_review": True,
                "review_status": "wizards_modern_commander_product_family_source_verified",
                "wizards_primary_source": source["wizards_primary_url"],
                "wizards_review_product_group": source["wizards_product_family_supported"],
                "wizards_source_grade": source["evidence_grade"],
                "verified_evidence_note": source["wizards_source_note"],
                "wizards_versus_scryfall_date_relationship": source["wizards_versus_scryfall_date_relationship"],
                "wizards_code_explicitly_confirmed": False,
                "wizards_premier_status_certified": False,
                "exact_deck_printings_certified": False,
                "new_card_count_certified": False,
            })
            seen.add(row["code"])
        rows.append(row)
    if seen != set(sources) or len(rows) != 848:
        raise ValueError("Modern Commander overlay lost catalog entries")
    result = dict(data)
    result["all_848_released_nondigital_other_type_records"] = rows
    result["wizards_reviewed_examples"] = review["cumulative_family_source_backed_codes"]
    result["metadata_only_pending_wizards_individual_review"] = review["cumulative_source_pending_codes"]
    result["cohort_review_progress"] = {}
    for cohort in data["metadata_research_cohorts"]:
        members = [r for r in rows if r["metadata_cohort_not_official_classification"] == cohort]
        result["cohort_review_progress"][cohort] = {
            "codes": len(members),
            "wizards_reviewed": sum(bool(r["wizards_individual_source_review"]) for r in members),
            "needs_individual_review": sum(not r["wizards_individual_source_review"] for r in members),
            "explicit_parent_links": sum(bool(r["parent_set_code_explicit_only"]) for r in members),
        }
    if sum(bool(r["wizards_individual_source_review"]) for r in rows) != 151:
        raise ValueError("Modern Commander current lookup conservation is not 151")
    return result


def apply_boxed_specialty_source_overlay(data, review):
    """Apply fourteen bounded box and premium-deck family reviews."""
    if review["cutoff"] != data["snapshot_date"] or data["wizards_reviewed_examples"] != 151:
        raise ValueError("Specialty boxed source review previous checkpoint changed")
    updates = {r["code"]: r for r in review["reviewed_boxed_specialty_codes"]}
    if len(updates) != review["source_reviewed_this_batch"] or len(updates) != 14:
        raise ValueError("Specialty boxed review missing or duplicated codes")
    seen = set()
    rows = []
    for prior in data["all_848_released_nondigital_other_type_records"]:
        row = dict(prior)
        source = updates.get(row["code"])
        if source is not None:
            if row["wizards_individual_source_review"]:
                raise ValueError(f"Specialty boxed review overwrites old verification: {row['code']}")
            if (row["scryfall_set_type"] != source["scryfall_type"] or
                    row["scryfall_release_or_first_card_date"] != source["scryfall_release_or_first_card_date"] or
                    row["parent_set_code_explicit_only"] != source["scryfall_explicit_parent_code_unchanged"]):
                raise ValueError(f"Specialty boxed review changed frozen set metadata: {row['code']}")
            row.update({
                "wizards_individual_source_review": True,
                "review_status": "wizards_specialty_box_or_premium_deck_source_verified",
                "wizards_primary_source": source["wizards_primary_url"],
                "wizards_review_product_group": source["product_family_wizards_supported"],
                "wizards_source_grade": source["evidence_grade"],
                "wizards_code_explicitly_confirmed": source["wizards_exact_scryfall_code_explicit"],
                "verified_evidence_note": source["wizards_source_note"],
                "wizards_premier_status_certified": False,
                "exact_deck_printings_certified": False,
                "new_card_count_certified": False,
            })
            seen.add(row["code"])
        rows.append(row)
    if seen != set(updates) or len(rows) != 848:
        raise ValueError("Specialty boxed overlay dropped source codes")
    result = dict(data)
    result["all_848_released_nondigital_other_type_records"] = rows
    result["wizards_reviewed_examples"] = review["cumulative_family_source_backed_codes"]
    result["metadata_only_pending_wizards_individual_review"] = review["cumulative_source_pending_codes"]
    result["cohort_review_progress"] = {}
    for cohort in data["metadata_research_cohorts"]:
        members = [r for r in rows if r["metadata_cohort_not_official_classification"] == cohort]
        result["cohort_review_progress"][cohort] = {
            "codes": len(members),
            "wizards_reviewed": sum(bool(r["wizards_individual_source_review"]) for r in members),
            "needs_individual_review": sum(not r["wizards_individual_source_review"] for r in members),
            "explicit_parent_links": sum(bool(r["parent_set_code_explicit_only"]) for r in members),
        }
    if sum(bool(r["wizards_individual_source_review"]) for r in rows) != 165:
        raise ValueError("Specialty boxed source overlay is not 165 verified codes")
    return result


def apply_boxed_special_lair_global_source_overlay(data, report):
    """Source five separate collection families without equating codes to boxes."""
    if report["cutoff"] != data["snapshot_date"] or data["wizards_reviewed_examples"] != 165:
        raise ValueError("Secret Lair source batch previous checkpoint changed")
    sources = {r["code"]: r for r in report["reviewed_secret_lair_global_codes"]}
    if len(sources) != report["new_source_backed_product_family_codes"] or len(sources) != 5:
        raise ValueError("Secret Lair/Global Series source evidence missing or duplicated")
    changed = set()
    rows = []
    for previous in data["all_848_released_nondigital_other_type_records"]:
        row = dict(previous)
        source = sources.get(row["code"])
        if source is not None:
            if row["wizards_individual_source_review"]:
                raise ValueError(f"Secret Lair source would overwrite an earlier citation: {row['code']}")
            if (row["scryfall_set_type"] != source["scryfall_type"] or
                    row["scryfall_release_or_first_card_date"] != source["scryfall_release_or_first_card_date"] or
                    row["parent_set_code_explicit_only"] != source["scryfall_explicit_parent_code_unchanged"]):
                raise ValueError(f"Secret Lair source changed immutable code/date/parent: {row['code']}")
            row.update({
                "wizards_individual_source_review": True,
                "review_status": "wizards_secret_lair_or_global_series_family_verified",
                "wizards_primary_source": source["wizards_primary_url"],
                "wizards_review_product_group": source["product_family_wizards_supported"],
                "wizards_source_grade": source["evidence_grade"],
                "wizards_code_explicitly_confirmed": source["wizards_exact_scryfall_code_explicit"],
                "verified_evidence_note": source["wizards_supported_relationship_note"],
                "wizards_premier_status_certified": False,
                "exact_deck_printings_certified": False,
                "current_format_legality_certified": False,
                "new_card_count_certified": False,
            })
            changed.add(row["code"])
        rows.append(row)
    if changed != set(sources) or len(rows) != 848:
        raise ValueError("Secret Lair/Global Series source overlay dropped a record")
    result = dict(data)
    result["all_848_released_nondigital_other_type_records"] = rows
    result["wizards_reviewed_examples"] = report["cumulative_family_source_backed_codes"]
    result["metadata_only_pending_wizards_individual_review"] = report["cumulative_source_pending_codes"]
    result["cohort_review_progress"] = {}
    for cohort in data["metadata_research_cohorts"]:
        members = [r for r in rows if r["metadata_cohort_not_official_classification"] == cohort]
        result["cohort_review_progress"][cohort] = {
            "codes": len(members),
            "wizards_reviewed": sum(bool(r["wizards_individual_source_review"]) for r in members),
            "needs_individual_review": sum(not r["wizards_individual_source_review"] for r in members),
            "explicit_parent_links": sum(bool(r["parent_set_code_explicit_only"]) for r in members),
        }
    if sum(bool(r["wizards_individual_source_review"]) for r in rows) != 170:
        raise ValueError("Source-backed family count is not 170")
    return result


def apply_inserts_clash_spellbook_source_overlay(data, report):
    """Add nine graded exact-code and family citations without rewriting old metadata."""
    if report["cutoff"] != data["snapshot_date"] or data["wizards_reviewed_examples"] != 170:
        raise ValueError("Insert/Clash source audit prior checkpoint changed")
    updates = {r["code"]: r for r in report["reviewed_inserts_clash_spellbook_codes"]}
    if len(updates) != report["new_source_backed_product_family_codes"] or len(updates) != 9:
        raise ValueError("Insert/Clash source audit missing or duplicated codes")
    seen = set()
    rows = []
    for old in data["all_848_released_nondigital_other_type_records"]:
        row = dict(old)
        source = updates.get(row["code"])
        if source is not None:
            if row["wizards_individual_source_review"]:
                raise ValueError(f"Insert/Clash citation overwrites earlier source: {row['code']}")
            if (row["scryfall_set_type"] != source["scryfall_type"] or
                    row["scryfall_release_or_first_card_date"] != source["scryfall_release_or_first_card_date"] or
                    row["parent_set_code_explicit_only"] != source["scryfall_explicit_parent_code_unchanged"] or
                    row["metadata_cohort_not_official_classification"] != source["scryfall_research_cohort"]):
                raise ValueError(f"Insert/Clash review changed frozen metadata: {row['code']}")
            row.update({
                "wizards_individual_source_review": True,
                "review_status": "wizards_insert_clash_spellbook_graded_source_reviewed",
                "wizards_primary_source": source["wizards_primary_url"],
                "wizards_secondary_gallery_url": source["wizards_secondary_gallery_url"],
                "wizards_review_product_group": source["product_family_wizards_supported"],
                "wizards_source_grade": source["evidence_grade"],
                "wizards_code_explicitly_confirmed": source["wizards_set_code_printed_in_article"],
                "wizards_card_gallery_printing_code_confirmed": source["wizards_printing_code_printed_in_card_gallery"],
                "verified_evidence_note": source["wizards_source_note"],
                "wizards_premier_status_certified": False,
                "exact_deck_printings_certified": False,
                "current_format_legality_certified": False,
                "new_card_count_certified": False,
            })
            seen.add(row["code"])
        rows.append(row)
    if seen != set(updates) or len(rows) != 848:
        raise ValueError("Insert/Clash source lookup lost catalog rows")
    result = dict(data)
    result["all_848_released_nondigital_other_type_records"] = rows
    result["wizards_reviewed_examples"] = report["cumulative_family_source_backed_codes"]
    result["metadata_only_pending_wizards_individual_review"] = report["cumulative_source_pending_codes"]
    result["cohort_review_progress"] = {}
    for cohort in data["metadata_research_cohorts"]:
        members = [r for r in rows if r["metadata_cohort_not_official_classification"] == cohort]
        result["cohort_review_progress"][cohort] = {
            "codes": len(members),
            "wizards_reviewed": sum(bool(r["wizards_individual_source_review"]) for r in members),
            "needs_individual_review": sum(not r["wizards_individual_source_review"] for r in members),
            "explicit_parent_links": sum(bool(r["parent_set_code_explicit_only"]) for r in members),
        }
    if sum(bool(r["wizards_individual_source_review"]) for r in rows) != 179:
        raise ValueError("New current product source evidence count is not 179")
    return result


def apply_masterpiece_memorabilia_source_overlay(data, review):
    """Overlay exact Wizards evidence, keeping family-only joins visibly distinct."""
    if review["cutoff"] != data["snapshot_date"] or data["wizards_reviewed_examples"] != 179:
        raise ValueError("Collectible review's previous source checkpoint changed")
    additions = {r["code"]: r for r in review["reviewed_source_records"]}
    if len(additions) != review["new_source_backed_codes"] or len(additions) != 19:
        raise ValueError("Collectible review lost or duplicated source code")
    rows = []
    patched = set()
    for prior in data["all_848_released_nondigital_other_type_records"]:
        row = dict(prior)
        source = additions.get(row["code"])
        if source:
            if row["wizards_individual_source_review"]:
                raise ValueError(f"Collectible evidence overwrites prior review: {row['code']}")
            if (row["scryfall_set_type"] != source["scryfall_type"] or
                    row["scryfall_release_or_first_card_date"] != source["scryfall_first_card_date"] or
                    row["parent_set_code_explicit_only"] != source["scryfall_parent_code_unchanged"]):
                raise ValueError(f"Collectible evidence changes frozen metadata: {row['code']}")
            row.update({
                "wizards_individual_source_review": True,
                "review_status": "wizards_special_sheet_or_collectible_source_reviewed",
                "wizards_primary_source": source["wizards_primary_url"],
                "wizards_review_product_group": source["wizards_family_context"],
                "wizards_source_grade": source["evidence_grade"],
                "wizards_code_explicitly_confirmed": source["wizards_exact_code_in_source"],
                "verified_evidence_note": source["wizards_evidence_caution"],
                "wizards_premier_status_certified": False,
                "one_code_one_sold_product_certified": False,
                "complete_printing_inventory_certified": False,
                "current_format_legality_certified": False,
            })
            patched.add(row["code"])
        rows.append(row)
    if patched != set(additions) or len(rows) != 848:
        raise ValueError("Collectible overlay not an exact source-code update")
    result = dict(data)
    result["all_848_released_nondigital_other_type_records"] = rows
    result["wizards_reviewed_examples"] = review["cumulative_family_source_backed_codes"]
    result["metadata_only_pending_wizards_individual_review"] = review["cumulative_source_pending_codes"]
    result["cohort_review_progress"] = {}
    for cohort in data["metadata_research_cohorts"]:
        members = [r for r in rows if r["metadata_cohort_not_official_classification"] == cohort]
        result["cohort_review_progress"][cohort] = {
            "codes": len(members),
            "wizards_reviewed": sum(bool(r["wizards_individual_source_review"]) for r in members),
            "needs_individual_review": sum(not r["wizards_individual_source_review"] for r in members),
            "explicit_parent_links": sum(bool(r["parent_set_code_explicit_only"]) for r in members),
        }
    if sum(bool(r["wizards_individual_source_review"]) for r in rows) != 198:
        raise ValueError("Collectible source review census is not 198")
    return result


def apply_historical_promo_series_overlay(data, review):
    """Add dated Wizards event/retrospective evidence, never invent exact printed codes."""
    if review["cutoff"] != data["snapshot_date"] or data["wizards_reviewed_examples"] != 198:
        raise ValueError("Annual promo evidence requires the 198-code checkpoint")
    updates = {r["code"]: r for r in review["reviewed_named_promo_families"]}
    if len(updates) != review["new_source_backed_codes"] or len(updates) != 10:
        raise ValueError("Historical promo series review has duplicate/missing codes")
    changed = set()
    rows = []
    for original in data["all_848_released_nondigital_other_type_records"]:
        item = dict(original)
        src = updates.get(item["code"])
        if src is not None:
            if item["wizards_individual_source_review"]:
                raise ValueError(f"Cannot replace already reviewed promo source {item['code']}")
            if (item["scryfall_set_type"] != src["scryfall_type"] or
                    item["scryfall_release_or_first_card_date"] != src["scryfall_earliest_card_date"] or
                    item["parent_set_code_explicit_only"] != src["scryfall_parent_set_code_unchanged"] or
                    src["wizards_prints_exact_scryfall_code"]):
                raise ValueError(f"Historical promo metadata/code-evidence mismatch {item['code']}")
            item.update({
                "wizards_individual_source_review": True,
                "review_status": "wizards_annual_promo_or_retrospective_family_only_reviewed",
                "wizards_primary_source": src["official_source_url"],
                "wizards_review_product_group": src["officially_supported_product_family"],
                "wizards_source_grade": src["source_grade"],
                "wizards_code_explicitly_confirmed": False,
                "verified_evidence_note": src["source_caveat"],
                "wizards_premier_status_certified": False,
                "complete_printing_inventory_certified": False,
                "current_format_legality_certified": False,
            })
            changed.add(item["code"])
        rows.append(item)
    if changed != set(updates) or len(rows) != 848:
        raise ValueError("Historical promo review changed frozen catalog coverage")
    result = dict(data)
    result["all_848_released_nondigital_other_type_records"] = rows
    result["wizards_reviewed_examples"] = review["cumulative_family_source_backed_codes"]
    result["metadata_only_pending_wizards_individual_review"] = review["cumulative_source_pending_codes"]
    result["cohort_review_progress"] = {}
    for cohort in data["metadata_research_cohorts"]:
        members = [r for r in rows if r["metadata_cohort_not_official_classification"] == cohort]
        result["cohort_review_progress"][cohort] = {
            "codes": len(members),
            "wizards_reviewed": sum(bool(r["wizards_individual_source_review"]) for r in members),
            "needs_individual_review": sum(not r["wizards_individual_source_review"] for r in members),
            "explicit_parent_links": sum(bool(r["parent_set_code_explicit_only"]) for r in members),
        }
    if sum(bool(x["wizards_individual_source_review"]) for x in rows) != 208:
        raise ValueError("208 cumulative official cited family records not conserved")
    return result


def apply_apac_lunar_year_promos_overlay(data, review):
    """Six annual first-party program citations, not claims of officially printed catalog codes."""
    if review["cutoff"] != data["snapshot_date"] or data["wizards_reviewed_examples"] != 208:
        raise ValueError("Lunar promo overlay requires the 208-reviewed code checkpoint")
    updates = {r["code"]: r for r in review["reviewed_apac_lunar_year_promo_families"]}
    if len(updates) != review["new_source_backed_codes"] or len(updates) != 6:
        raise ValueError("Annual Lunar source overlay duplicate/missing records")
    reviewed = set()
    rows = []
    for original in data["all_848_released_nondigital_other_type_records"]:
        item = dict(original)
        source = updates.get(item["code"])
        if source is not None:
            if item["wizards_individual_source_review"]:
                raise ValueError(f"Cannot overwrite an already verified Lunar promo {item['code']}")
            if (item["scryfall_set_type"] != source["scryfall_type"] or
                    item["scryfall_release_or_first_card_date"] != source["scryfall_earliest_card_date"] or
                    item["parent_set_code_explicit_only"] != source["scryfall_parent_set_code_unchanged"] or
                    source["wizards_prints_exact_scryfall_code"]):
                raise ValueError(f"Scryfall metadata or exact-code claim drift for Lunar promo {item['code']}")
            item.update({
                "wizards_individual_source_review": True,
                "review_status": "wizards_apac_lunar_year_promo_family_only_reviewed",
                "wizards_primary_source": source["official_source_url"],
                "wizards_review_product_group": source["officially_supported_product_family"],
                "wizards_source_grade": source["source_grade"],
                "wizards_code_explicitly_confirmed": False,
                "verified_evidence_note": source["source_caveat"],
                "wizards_premier_status_certified": False,
                "complete_printing_inventory_certified": False,
                "current_format_legality_certified": False,
            })
            reviewed.add(item["code"])
        rows.append(item)
    if reviewed != set(updates) or len(rows) != 848:
        raise ValueError("Lunar promo overlay failed exact 848-code conservation")
    result = dict(data)
    result["all_848_released_nondigital_other_type_records"] = rows
    result["wizards_reviewed_examples"] = review["cumulative_family_source_backed_codes"]
    result["metadata_only_pending_wizards_individual_review"] = review["cumulative_source_pending_codes"]
    result["cohort_review_progress"] = {}
    for cohort in data["metadata_research_cohorts"]:
        members = [r for r in rows if r["metadata_cohort_not_official_classification"] == cohort]
        result["cohort_review_progress"][cohort] = {
            "codes": len(members),
            "wizards_reviewed": sum(bool(r["wizards_individual_source_review"]) for r in members),
            "needs_individual_review": sum(not r["wizards_individual_source_review"] for r in members),
            "explicit_parent_links": sum(bool(r["parent_set_code_explicit_only"]) for r in members),
        }
    if sum(bool(r["wizards_individual_source_review"]) for r in rows) != 214:
        raise ValueError("214 cumulative official named-family records not conserved")
    return result


def apply_event_collab_promos_overlay(data, review):
    """Add seven specifically dated event/collaboration sources without code overclaims."""
    if review["cutoff"] != data["snapshot_date"] or data["wizards_reviewed_examples"] != 214:
        raise ValueError("Event/collab source overlay requires 214 prior reviews")
    updates = {r["code"]: r for r in review["reviewed_event_collab_promo_families"]}
    if len(updates) != review["new_source_backed_codes"] or len(updates) != 7:
        raise ValueError("Incomplete/duplicate event-collaboration citations")
    patched = set()
    rows = []
    for previous in data["all_848_released_nondigital_other_type_records"]:
        item = dict(previous)
        source = updates.get(item["code"])
        if source is not None:
            if item["wizards_individual_source_review"]:
                raise ValueError(f"Cannot overwrite earlier official event source {item['code']}")
            if (item["scryfall_set_type"] != source["scryfall_type"] or
                    item["scryfall_release_or_first_card_date"] != source["scryfall_earliest_card_date"] or
                    item["parent_set_code_explicit_only"] != source["scryfall_parent_set_code_unchanged"] or
                    source["wizards_prints_exact_scryfall_code"]):
                raise ValueError(f"Unexpected Scryfall type, date, parent or exact-code claim: {item['code']}")
            item.update({
                "wizards_individual_source_review": True,
                "review_status": "wizards_event_collaboration_promo_family_only_reviewed",
                "wizards_primary_source": source["official_source_url"],
                "wizards_review_product_group": source["officially_supported_product_family"],
                "wizards_source_grade": source["source_grade"],
                "wizards_code_explicitly_confirmed": False,
                "verified_evidence_note": source["source_caveat"],
                "wizards_premier_status_certified": False,
                "complete_printing_inventory_certified": False,
                "current_format_legality_certified": False,
            })
            patched.add(item["code"])
        rows.append(item)
    if patched != set(updates) or len(rows) != 848:
        raise ValueError("Event/collab source overlay not an exact 848-code crosswalk")
    result = dict(data)
    result["all_848_released_nondigital_other_type_records"] = rows
    result["wizards_reviewed_examples"] = review["cumulative_family_source_backed_codes"]
    result["metadata_only_pending_wizards_individual_review"] = review["cumulative_source_pending_codes"]
    result["cohort_review_progress"] = {}
    for cohort in data["metadata_research_cohorts"]:
        members = [item for item in rows if item["metadata_cohort_not_official_classification"] == cohort]
        result["cohort_review_progress"][cohort] = {
            "codes": len(members),
            "wizards_reviewed": sum(bool(item["wizards_individual_source_review"]) for item in members),
            "needs_individual_review": sum(not item["wizards_individual_source_review"] for item in members),
            "explicit_parent_links": sum(bool(item["parent_set_code_explicit_only"]) for item in members),
        }
    if sum(bool(item["wizards_individual_source_review"]) for item in rows) != 221:
        raise ValueError("221 cumulative independently cited records not conserved")
    return result


def apply_art_series_source_overlay(data, review):
    """Cite collectible art-card families, preserving Scryfall metadata and legality boundaries."""
    if review["cutoff"] != data["snapshot_date"] or data["wizards_reviewed_examples"] != 221:
        raise ValueError("Art-series overlay requires the 221-reviewed event checkpoint")
    updates = {r["code"]: r for r in review["reviewed_art_series_families"]}
    if len(updates) != review["new_source_backed_codes"] or len(updates) != 38:
        raise ValueError("Art-series source overlay duplicate/missing records")
    patched, rows = set(), []
    for original in data["all_848_released_nondigital_other_type_records"]:
        item = dict(original)
        source = updates.get(item["code"])
        if source is not None:
            if item["wizards_individual_source_review"]:
                raise ValueError(f"Cannot overwrite previously reviewed art-series record {item['code']}")
            if (item["scryfall_set_type"] != source["scryfall_type"] or
                    item["scryfall_release_or_first_card_date"] != source["scryfall_earliest_card_date"] or
                    item["parent_set_code_explicit_only"] != source["scryfall_parent_set_code_explicit_only_unchanged"] or
                    source["wizards_prints_exact_scryfall_art_series_code"] or
                    source["standalone_premier_expansion_certified"] or
                    source["individual_art_printing_inventory_certified"] or
                    source["new_playable_card_debut_count_certified"] or
                    source["current_format_legality_certified"]):
                raise ValueError(f"Art-series metadata or certification drift: {item['code']}")
            item.update({
                "wizards_individual_source_review": True,
                "review_status": "wizards_named_art_series_component_source_reviewed",
                "wizards_primary_source": source["official_source_url"],
                "wizards_review_product_group": source["officially_named_product_family"],
                "wizards_source_grade": source["source_grade"],
                "wizards_code_explicitly_confirmed": False,
                "verified_evidence_note": source["source_note"],
                "wizards_premier_status_certified": False,
                "complete_printing_inventory_certified": False,
                "current_format_legality_certified": False,
            })
            patched.add(item["code"])
        rows.append(item)
    if patched != set(updates) or len(rows) != 848:
        raise ValueError("Art-series source overlay failed 848-code conservation")
    result = dict(data)
    result["all_848_released_nondigital_other_type_records"] = rows
    result["wizards_reviewed_examples"] = review["cumulative_family_source_backed_codes"]
    result["metadata_only_pending_wizards_individual_review"] = review["cumulative_source_pending_codes"]
    result["cohort_review_progress"] = {}
    for cohort in data["metadata_research_cohorts"]:
        members = [item for item in rows if item["metadata_cohort_not_official_classification"] == cohort]
        result["cohort_review_progress"][cohort] = {
            "codes": len(members),
            "wizards_reviewed": sum(bool(item["wizards_individual_source_review"]) for item in members),
            "needs_individual_review": sum(not item["wizards_individual_source_review"] for item in members),
            "explicit_parent_links": sum(bool(item["parent_set_code_explicit_only"]) for item in members),
        }
    if sum(bool(item["wizards_individual_source_review"]) for item in rows) != 259:
        raise ValueError("259 cumulative first-party named-family reviews not conserved")
    return result


def load_current_index():
    data = json.loads(INDEX.read_text(encoding="utf-8"))
    if SOURCE_REVIEW.exists():
        verified = json.loads(SOURCE_REVIEW.read_text(encoding="utf-8"))
        data = apply_source_overlay(data, verified)
    if SECOND_SOURCE_REVIEW.exists():
        second = json.loads(SECOND_SOURCE_REVIEW.read_text(encoding="utf-8"))
        data = apply_second_source_overlay(data, second)
    if REPRINT_SOURCE_REVIEW.exists():
        report = json.loads(REPRINT_SOURCE_REVIEW.read_text(encoding="utf-8"))
        data = apply_reprint_source_overlay(data, report)
    if BOXED_SOURCE_REVIEW.exists():
        report = json.loads(BOXED_SOURCE_REVIEW.read_text(encoding="utf-8"))
        data = apply_boxed_source_overlay(data, report)
    if DUEL_DECKS_SOURCE_REVIEW.exists():
        report = json.loads(DUEL_DECKS_SOURCE_REVIEW.read_text(encoding="utf-8"))
        data = apply_duel_decks_source_overlay(data, report)
    if COMMANDER_SERIES_SOURCE_REVIEW.exists():
        report = json.loads(COMMANDER_SERIES_SOURCE_REVIEW.read_text(encoding="utf-8"))
        data = apply_commander_series_source_overlay(data, report)
    if COMMANDER_SET_LINKED_SOURCE_REVIEW.exists():
        report = json.loads(COMMANDER_SET_LINKED_SOURCE_REVIEW.read_text(encoding="utf-8"))
        data = apply_commander_set_linked_source_overlay(data, report)
    if COMMANDER_MODERN_SOURCE_REVIEW.exists():
        report = json.loads(COMMANDER_MODERN_SOURCE_REVIEW.read_text(encoding="utf-8"))
        data = apply_commander_modern_source_overlay(data, report)
    if BOXED_SPECIALTY_SOURCE_REVIEW.exists():
        report = json.loads(BOXED_SPECIALTY_SOURCE_REVIEW.read_text(encoding="utf-8"))
        data = apply_boxed_specialty_source_overlay(data, report)
    if BOXED_SPECIAL_LAIR_GLOBAL_SOURCE_REVIEW.exists():
        report = json.loads(BOXED_SPECIAL_LAIR_GLOBAL_SOURCE_REVIEW.read_text(encoding="utf-8"))
        data = apply_boxed_special_lair_global_source_overlay(data, report)
    if INSERTS_CLASH_SPELLBOOK_SOURCE_REVIEW.exists():
        report = json.loads(INSERTS_CLASH_SPELLBOOK_SOURCE_REVIEW.read_text(encoding="utf-8"))
        data = apply_inserts_clash_spellbook_source_overlay(data, report)
    if MASTERPIECE_MEMORABILIA_SOURCE_REVIEW.exists():
        report = json.loads(MASTERPIECE_MEMORABILIA_SOURCE_REVIEW.read_text(encoding="utf-8"))
        data = apply_masterpiece_memorabilia_source_overlay(data, report)
    if HISTORICAL_PROMO_SERIES_SOURCE_REVIEW.exists():
        report = json.loads(HISTORICAL_PROMO_SERIES_SOURCE_REVIEW.read_text(encoding="utf-8"))
        data = apply_historical_promo_series_overlay(data, report)
    if APAC_LUNAR_YEAR_PROMOS_SOURCE_REVIEW.exists():
        report = json.loads(APAC_LUNAR_YEAR_PROMOS_SOURCE_REVIEW.read_text(encoding="utf-8"))
        data = apply_apac_lunar_year_promos_overlay(data, report)
    if EVENT_COLLAB_PROMOS_SOURCE_REVIEW.exists():
        report = json.loads(EVENT_COLLAB_PROMOS_SOURCE_REVIEW.read_text(encoding="utf-8"))
        data = apply_event_collab_promos_overlay(data, report)
    if ART_SERIES_SOURCE_REVIEW.exists():
        report = json.loads(ART_SERIES_SOURCE_REVIEW.read_text(encoding="utf-8"))
        data = apply_art_series_source_overlay(data, report)
    return data


def select(data, code=None, cohort=None, set_type=None, parent=None,
           only_pending=False, priority=None):
    rows = []
    for item in data["all_848_released_nondigital_other_type_records"]:
        if code is not None and item["code"] != code.lower():
            continue
        if cohort is not None and item["metadata_cohort_not_official_classification"] != cohort:
            continue
        if set_type is not None and item["scryfall_set_type"] != set_type:
            continue
        if parent is not None and item["parent_set_code_explicit_only"] != parent.lower():
            continue
        if only_pending and item["wizards_individual_source_review"]:
            continue
        if priority is not None and item["research_priority_1_highest"] != priority:
            continue
        rows.append(item)
    return sorted(rows, key=lambda x: (
        x["research_priority_1_highest"], x["scryfall_set_type"],
        x["scryfall_release_or_first_card_date"] or "", x["code"]))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--summary", action="store_true")
    p.add_argument("--code")
    p.add_argument("--cohort")
    p.add_argument("--type", dest="set_type")
    p.add_argument("--parent")
    p.add_argument("--only-pending", action="store_true")
    p.add_argument("--priority", type=int, choices=(1, 2, 3, 4))
    p.add_argument("--all", action="store_true")
    args = p.parse_args()
    data = load_current_index()
    if args.summary:
        print(json.dumps({
            "snapshot": data["snapshot_date"],
            "metadata_research_cohorts": data["metadata_research_cohorts"],
            "cohort_review_progress": data["cohort_review_progress"],
            "reviewed": data["wizards_reviewed_examples"],
            "individual_source_review_pending": data["metadata_only_pending_wizards_individual_review"],
            "metadata_not_premier_status": True,
        }, indent=2, ensure_ascii=False))
        return
    results = select(
        data, code=args.code, cohort=args.cohort, set_type=args.set_type,
        parent=args.parent, only_pending=args.only_pending, priority=args.priority
    )
    print(json.dumps({
        "snapshot": data["snapshot_date"], "matches": len(results),
        "shown": len(results if args.all else results[:30]),
        "research_cohorts_not_official_classification": True,
        "results": results if args.all else results[:30],
    }, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
