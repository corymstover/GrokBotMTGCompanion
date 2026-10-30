#!/usr/bin/env python3
"""Reproducible 28-code Wizards source review for Masters/reprint curated cohort.

This is an *overlay* on the dated, preserved 43-code family source baseline;
all categories/IDs/dates come from frozen Scryfall, and only exact Wizards
citations support product-family claims. Never infer premier/legal status.
"""
import argparse
import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data/set_atlas"
BASE = DATA / "product_family_triage_2026-10-29.json"
PREVIOUS = DATA / "draft_starter_batch2_audit_2026-10-29.json"
EVIDENCE = DATA / "reprint_curated_sources_2026-10-29.json"
OUTPUT = DATA / "reprint_curated_source_audit_2026-10-29.json"
REVIEW_COHORT = "reprint_and_curated_products"
EXPECTED_PENDING = {"bchr", "rin", "ss2"}
GROUPS = {
    "masters_randomized_all_reprint_booster",
    "remastered_or_masters_independent_draft_booster",
    "mystery_booster_event_reprint_draft_booster",
    "early_chronicles_reprint_booster",
    "localized_early_renaissance_reprint_product",
    "embedded_the_list_reprint_distribution",
    "universes_within_alternate_names_in_list",
    "fixed_from_the_vault_collectible_reprint_box",
    "signature_spellbook_fixed_8_plus_1_card_box",
}
GRADES = {
    "exact_product_wizards_name_scryfall_code_crosswalk",
    "exact_code_and_group_primary",
}

def serialized(v):
    return (json.dumps(v, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode("utf-8")

def build(base, previous, evidence):
    if base["snapshot_date"] != previous["cutoff"] or evidence["as_of"] != previous["cutoff"]:
        raise ValueError("Dated source snapshots are incompatible")
    if previous["cumulative_outside_category_codes_with_wizards_source_family_evidence"] != 43:
        raise ValueError("Prior individual source review drifted")
    if previous["cumulative_outside_category_codes_individual_wizards_source_pending"] != 805:
        raise ValueError("Previously certified 805 pending codes drifted")
    baseline = {v["code"]:v for v in base["all_848_released_nondigital_other_type_records"]}
    old_pending = {v["code"]:v for v in previous["still_source_pending_queue"]}
    if len(baseline) != 848 or len(old_pending) != 805:
        raise ValueError("Duplicated/missing source set codes")
    cohort_pending = {code for code in old_pending if baseline[code]["metadata_cohort_not_official_classification"] == REVIEW_COHORT}
    if len(cohort_pending) != 31:
        raise ValueError("Original Masters/curated cohort no longer has 31 pending codes")
    reviewed = []
    used = set()
    for row in evidence["records"]:
        code = row.get("code")
        if code in used:
            raise ValueError(f"Duplicate source review {code}")
        if code not in cohort_pending:
            raise ValueError(f"Previously reviewed or outside cohort: {code}")
        if row.get("group") not in GROUPS:
            raise ValueError(f"Unsupported official product group: {code}")
        if row.get("evidence_grade") not in GRADES:
            raise ValueError(f"Unsupported provenance grade: {code}")
        url = row.get("source_url", "")
        uri = urlparse(url)
        if uri.scheme != "https" or uri.hostname not in ("magic.wizards.com", "www.magic.wizards.com"):
            raise ValueError(f"Non-Wizards primary source for {code}")
        if len(row.get("note", "")) < 65 or not row.get("source_section"):
            raise ValueError(f"Insufficient per-source evidence or section for {code}")
        original = baseline[code]
        used.add(code)
        reviewed.append({
            "code": code, "name": original["name"],
            "scryfall_set_type": original["scryfall_set_type"],
            "scryfall_release_or_first_card_date": original["scryfall_release_or_first_card_date"],
            "scryfall_parent_set_code_explicit_only": original["parent_set_code_explicit_only"],
            "wizards_product_family": row["group"],
            "wizards_source_url": url,
            "wizards_source_section": row["source_section"],
            "source_note": row["note"],
            "evidence_grade": row["evidence_grade"],
            "wizards_explicit_scryfall_code": row["evidence_grade"] == "exact_code_and_group_primary",
            "standalone_booster_classification": (
                "source_confirmed_booster" if row["group"] in {
                    "masters_randomized_all_reprint_booster",
                    "remastered_or_masters_independent_draft_booster",
                    "mystery_booster_event_reprint_draft_booster",
                    "early_chronicles_reprint_booster"
                } else "not_assumed_standalone_booster"
            ),
            "wizards_premier_status_certified": False,
            "card_legality_inferred_from_printing": False
        })
    if len(reviewed) != 28 or cohort_pending-used != EXPECTED_PENDING or set(evidence["still_pending"]) != EXPECTED_PENDING:
        raise ValueError(f"Wrong 28-code bounded review; residual: {sorted(cohort_pending-used)}")
    remaining = [r for r in previous["still_source_pending_queue"] if r["code"] not in used]
    if len(remaining) != 777 or len(remaining) + 43 + len(used) != 848:
        raise ValueError("Whole outside-category conservation failed")
    exact = sum(v["wizards_explicit_scryfall_code"] for v in reviewed)
    if exact != 1 or next(v for v in reviewed if v["code"] == "slx")["wizards_explicit_scryfall_code"] is not True:
        raise ValueError("Official code-exact evidence grade was incorrectly promoted")
    return {
        "schema": 1,
        "cutoff": evidence["as_of"],
        "prior_review": PREVIOUS.name,
        "ledger": EVIDENCE.name,
        "cohort": REVIEW_COHORT,
        "source_reviewed_this_batch": len(used),
        "source_confirmed_product_with_scryfall_code_crosswalk": len(used)-exact,
        "wizards_explicitly_prints_exact_code": exact,
        "outside_category_total": 848,
        "previously_reviewed_codes": 43,
        "cumulative_wizards_family_evidence_codes": 71,
        "cumulative_pending_codes": 777,
        "reprint_curated_source_pending_codes": sorted(EXPECTED_PENDING),
        "reprint_curated_remaining_pending_count": 3,
        "newly_sourced_family_evidence": sorted(reviewed, key=lambda r:r["code"]),
        "still_source_pending_queue": remaining,
        "caveats": [
            "Only product family is source-verified; code crosswalk for 27 items comes from Scryfall not an exact code printed by Wizards.",
            "FBB Chronicles and Rinascimento, and Gideon Signature Spellbook, remain in the source-pending list due to weaker direct support.",
            "From the Vault and Signature Spellbook are fixed collections, not draft booster sets.",
            "The List and Universes Within are reprint/alternate-name distributions inside other products, not newly sold standalone booster releases.",
            "Mystery Booster 2 is a reprint/event booster product, not a premier Standard expansion.",
            "All data are as-of October 29 2026; released-at set date is not per-card legality.",
            "71 reviewed does not mean 71 premier releases or 71 different new original card sets."
        ]
    }

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--write",action="store_true")
    args = p.parse_args()
    data = build(*(json.loads(f.read_text(encoding="utf-8")) for f in [BASE,PREVIOUS,EVIDENCE]))
    out = serialized(data)
    if args.write: OUTPUT.write_bytes(out)
    elif not OUTPUT.exists() or OUTPUT.read_bytes() != out:
        raise ValueError("Derived reprint-curated source audit differs from committed bytes")
    print(json.dumps({"new": data["source_reviewed_this_batch"], "cumulative": data["cumulative_wizards_family_evidence_codes"], "pending":data["cumulative_pending_codes"],"curated_pending":data["reprint_curated_source_pending_codes"]},sort_keys=True))
if __name__ == "__main__":
    main()
