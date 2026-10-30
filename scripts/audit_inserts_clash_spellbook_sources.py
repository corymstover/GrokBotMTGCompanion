#!/usr/bin/env python3
"""Reproduce nine official insert, Clash Pack and Gideon Spellbook source reviews."""
import argparse
import json
from pathlib import Path
from urllib.parse import urlparse

DATA = Path(__file__).resolve().parent.parent / "data" / "set_atlas"
BASE = DATA / "product_family_triage_2026-10-29.json"
PREV = DATA / "boxed_special_lair_global_audit_2026-10-29.json"
LEDGER = DATA / "inserts_clash_spellbook_sources_2014_2026.json"
OUT = DATA / "inserts_clash_spellbook_source_audit_2026-10-29.json"
INSERTS = {"bot", "rex", "spe", "tle", "tmc", "hoc"}
CLASH = {"cp1", "cp2"}
SPELLBOOK = {"ss2"}
REQUIRED = INSERTS | CLASH | SPELLBOOK
GRADES = {
    "wizards_article_explicit_set_code": INSERTS,
    "wizards_product_family_scryfall_code_crosswalk": CLASH,
    "wizards_card_gallery_exact_printing_code": SPELLBOOK,
}
COHORTS = {"insert": "special_inserts_and_eternal_subsets", "clash": "draft_and_starter_variants", "spellbook": "reprint_and_curated_products"}


def encode(obj):
    return (json.dumps(obj, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def official_url(url):
    parsed = urlparse(url)
    return (parsed.scheme == "https" and parsed.hostname in
            ("magic.wizards.com", "www.magic.wizards.com", "mtg-jp.com", "www.mtg-jp.com")
            and (parsed.path.startswith("/en/news/") or
                 parsed.path.startswith("/reading/") or
                 parsed.path.startswith("/products/")))


def build(base, previous, ledger):
    if (base.get("snapshot_date"), previous.get("cutoff"), ledger.get("cutoff")) != (
            "2026-10-29", "2026-10-29", "2026-10-29"):
        raise ValueError("Set family source cutoff changed")
    if (previous.get("cumulative_family_source_backed_codes"),
            previous.get("cumulative_source_pending_codes"),
            previous.get("boxed_source_pending_after_batch")) != (170, 678, 11):
        raise ValueError("Previous Secret Lair source checkpoint mismatch")
    old = previous["remaining_source_pending_queue"]
    pending = {r["code"] for r in old}
    catalog = {r["code"]: r for r in base["all_848_released_nondigital_other_type_records"]}
    if len(old) != 678 or len(pending) != 678 or len(catalog) != 848:
        raise ValueError("Frozen 848-code catalog or pending list changed")
    seen = set()
    urls = set()
    verified = []
    for source in ledger["records"]:
        code = source.get("code")
        if code in seen:
            raise ValueError(f"Duplicate research source code: {code}")
        if code not in REQUIRED or code not in pending:
            raise ValueError(f"Unsupported or previously reviewed research code: {code}")
        grade = source.get("source_grade", "")
        if grade not in GRADES or code not in GRADES[grade]:
            raise ValueError(f"Unsupported official code-evidence grade: {code}")
        url = source.get("official_url", "")
        if not official_url(url):
            raise ValueError(f"Not a direct Wizards product source: {code}")
        if url in urls:
            raise ValueError(f"Duplicate product source URL reused: {code}")
        section = source.get("source_section", "")
        if len(section) < 65:
            raise ValueError(f"Missing detailed Wizards product section: {code}")
        if code in INSERTS and code.upper() not in section:
            raise ValueError(f"Wizards article's explicit code unverified: {code}")
        gallery_url = source.get("secondary_official_gallery_url")
        if code == "ss2":
            if not gallery_url or not official_url(gallery_url) or "470542" not in gallery_url or "SS2" not in section:
                raise ValueError("SS2 exact printing code requires direct Wizards card gallery")
        elif gallery_url:
            raise ValueError(f"Unexpected secondary gallery for {code}")
        note = source.get("source_note", "")
        if len(note) < 65:
            raise ValueError(f"Missing product/printing caution for {code}")
        meta = catalog[code]
        expected_cohort = (COHORTS["insert"] if code in INSERTS else
                           COHORTS["clash"] if code in CLASH else COHORTS["spellbook"])
        expected_type = "eternal" if code in INSERTS else "starter" if code in CLASH else "spellbook"
        if (meta["metadata_cohort_not_official_classification"] != expected_cohort or
                meta["scryfall_set_type"] != expected_type):
            raise ValueError(f"Unexpected official source research category: {code}")
        if code == "cp2" and (
                "January 30" not in note or "January 23" not in note or
                meta["scryfall_release_or_first_card_date"] != "2015-01-23"):
            raise ValueError("CP2 marketed product versus first-card date distinction lost")
        verified.append({
            "code": code,
            "name": meta["name"],
            "scryfall_type": meta["scryfall_set_type"],
            "scryfall_research_cohort": meta["metadata_cohort_not_official_classification"],
            "scryfall_release_or_first_card_date": meta["scryfall_release_or_first_card_date"],
            "scryfall_explicit_parent_code_unchanged": meta["parent_set_code_explicit_only"],
            "wizards_primary_url": url,
            "wizards_secondary_gallery_url": gallery_url,
            "wizards_article_section": section,
            "evidence_grade": grade,
            "wizards_set_code_printed_in_article": code in INSERTS,
            "wizards_printing_code_printed_in_card_gallery": code == "ss2",
            "wizards_product_code_explicitly_printed": False,
            "wizards_source_note": note,
            "product_family_wizards_supported": (
                "integrated_special_insert_or_eternal_card_subset" if code in INSERTS else
                "two_deck_clash_pack" if code in CLASH else "fixed_signature_spellbook_box"
            ),
            "standalone_premier_set_certified": False,
            "exact_box_printing_inventory_certified": False,
            "new_card_count_certified": False,
            "current_format_legality_certified": False,
        })
        seen.add(code)
        urls.add(url)
    if seen != REQUIRED or len(verified) != 9:
        raise ValueError(f"Missing set-family evidence rows: {sorted(REQUIRED-seen)}")
    remaining = [r for r in old if r["code"] not in seen]
    buckets = {cohort: sum(catalog[x["code"]]["metadata_cohort_not_official_classification"] == cohort for x in remaining)
               for cohort in COHORTS.values()}
    if (len(remaining), buckets[COHORTS["insert"]], buckets[COHORTS["clash"]],
            buckets[COHORTS["spellbook"]]) != (669, 0, 11, 2):
        raise ValueError("Whole catalog, special insert, draft or reprint partitions changed")
    if 179 + len(remaining) != 848:
        raise ValueError("Conserved 848-code outside-category census failed")
    return {
        "schema": 1, "cutoff": "2026-10-29", "prior_audit": PREV.name,
        "source": LEDGER.name,
        "new_source_backed_product_family_codes": 9,
        "wizards_explicit_article_set_codes": sorted(INSERTS),
        "wizards_exact_card_gallery_printing_codes": ["ss2"],
        "cumulative_family_source_backed_codes": 179,
        "cumulative_source_pending_codes": 669,
        "remaining_special_inserts_and_eternal_subsets": 0,
        "remaining_draft_and_starter_variants": 11,
        "remaining_reprint_and_curated_products": 2,
        "remaining_boxed_preconstructed": 11,
        "reviewed_inserts_clash_spellbook_codes": sorted(verified, key=lambda x: x["code"]),
        "remaining_source_pending_queue": remaining,
        "caveats": ledger["caveats"] + [
            "179 source-backed plus 669 source-pending conserves the 848 released nondigital non-expansion/core paper set codes.",
            "All six official Eternal/insert codes are integrated subsets, not six extra premier expansions.",
            "Historic family-level and card-gallery sources do not alone prove current formats, all cards, or physical boxed printing variants.",
        ],
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--write", action="store_true")
    args = p.parse_args()
    report = build(*(json.loads(path.read_text(encoding="utf-8")) for path in (BASE, PREV, LEDGER)))
    content = encode(report)
    if args.write:
        OUT.write_bytes(content)
    elif not OUT.exists() or OUT.read_bytes() != content:
        raise ValueError("Nine-code insert / Clash Pack / Spellbook review not reproducible")
    print(json.dumps({k: report[k] for k in (
        "new_source_backed_product_family_codes", "cumulative_family_source_backed_codes",
        "cumulative_source_pending_codes", "remaining_special_inserts_and_eternal_subsets",
        "remaining_draft_and_starter_variants", "remaining_reprint_and_curated_products")}, sort_keys=True))


if __name__ == "__main__":
    main()
