#!/usr/bin/env python3
"""Reproducible 15-code Wizards product-family review of boxed products.

Distinguishes independently sold boxed decks from oversized scheme/planar
component codes. This overlays, never edits, previously validated snapshots.
"""
import argparse
import json
from pathlib import Path
from urllib.parse import urlparse
ROOT=Path(__file__).resolve().parent.parent
DATA=ROOT/"data"/"set_atlas"
BASE=DATA/"product_family_triage_2026-10-29.json"
PREV=DATA/"reprint_curated_source_audit_2026-10-29.json"
LEDGER=DATA/"boxed_precon_sources_2026-10-29.json"
OUT=DATA/"boxed_precon_source_audit_2026-10-29.json"
COHORT="preconstructed_and_boxed"
COMPONENT_PARENT={"oarc":"arc","oe01":"e01","ohop":"hop","opc2":"pc2","opca":"pca"}
REQUIRED=set(COMPONENT_PARENT)|{"arc","e01","hop","pc2","pca","cma","cm2","cc1","cc2","cm1"}
GRADES={"wizards_primary_family_scryfall_code_crosswalk"}
BOX_GROUPS={
 "archenemy_original_multi_deck_product",
 "archenemy_nicol_bolas_box",
 "planechase_2009_preconstructed_release",
 "planechase_2012_preconstructed_release",
 "planechase_anthology_preconstructed_reprint_box",
 "commander_anthology_four_reprinted_decks",
 "commander_anthology_volume_two_four_reprinted_decks",
 "commander_collection_green_eight_fixed_reprints",
 "commander_collection_black_eight_fixed_reprints",
 "commanders_arsenal_special_fixed_reprint_box"
}
COMPONENT_GROUPS={
 "archenemy_scheme_component",
 "archenemy_nicol_bolas_scheme_component",
 "planechase_2009_planar_cards_component",
 "planechase_2012_planar_cards_component",
 "planechase_anthology_planar_cards_component"
}

def encode(j):return (json.dumps(j,sort_keys=True,indent=2,ensure_ascii=False)+"\n").encode("utf-8")

def build(base,previous,ledger):
    date=base.get("snapshot_date")
    if date!="2026-10-29" or previous.get("cutoff")!=date or ledger.get("cutoff")!=date:
        raise ValueError("Mismatched historical snapshot")
    if previous.get("cumulative_wizards_family_evidence_codes")!=71 or previous.get("cumulative_pending_codes")!=777:
        raise ValueError("Previous 71/777 audited state changed")
    old=previous.get("still_source_pending_queue",[])
    remaining_codes={x["code"] for x in old}
    if len(remaining_codes)!=777 or len(old)!=777:
        raise ValueError("Missing/duplicate source-pending original codes")
    catalog={x["code"]:x for x in base["all_848_released_nondigital_other_type_records"]}
    if len(catalog)!=848:raise ValueError("Original Scryfall set catalog changed")
    seen=set()
    verified=[]
    for row in ledger["records"]:
        code=row.get("code")
        if code in seen:raise ValueError(f"Duplicate row {code}")
        if code not in remaining_codes or code not in REQUIRED:
            raise ValueError(f"Unreviewed or unsupported target {code}")
        v=catalog[code]
        if v["metadata_cohort_not_official_classification"]!=COHORT:
            raise ValueError(f"Incorrect cohort {code}")
        if row.get("grade") not in GRADES:raise ValueError(f"Unapproved evidence grade {code}")
        source=row.get("source_url","")
        uri=urlparse(source)
        if uri.scheme!="https" or uri.hostname not in ("magic.wizards.com","www.magic.wizards.com"):
            raise ValueError(f"Non-Wizards source {code}")
        if not row.get("source_section") or len(row.get("reason",""))<60:
            raise ValueError(f"Incomplete product-source explanation {code}")
        group=row.get("group")
        if code in COMPONENT_PARENT:
            if group not in COMPONENT_GROUPS:raise ValueError(f"Component promoted to independent product {code}")
            if v["parent_set_code_explicit_only"]!=COMPONENT_PARENT[code]:
                raise ValueError(f"Component missing explicit source parent {code}")
        elif group not in BOX_GROUPS:
            raise ValueError(f"Unapproved box/collection family {code}")
        seen.add(code)
        verified.append({
            "code":code,"name":v["name"],"scryfall_set_type":v["scryfall_set_type"],
            "scryfall_date":v["scryfall_release_or_first_card_date"],
            "scryfall_explicit_parent_code":v["parent_set_code_explicit_only"],
            "product_group_supported_by_wizards":group,
            "wizards_primary_url":source,"wizards_section":row["source_section"],
            "source_note":row["reason"],"evidence_grade":row["grade"],
            "official_product_name_verified":True,
            "exact_scryfall_code_printed_by_wizards":False,
            "component_of_existing_parent_product":code in COMPONENT_PARENT,
            "parent_product_code_when_component":COMPONENT_PARENT.get(code),
            "separate_sold_box_vs_card_component":("packaged_game_card_component" if code in COMPONENT_PARENT else "boxed_or_collection_release"),
            "standalone_booster_expansion":False,"premier_set_status_certified":False,
            "card_format_legality_inferred":False
        })
    if seen!=REQUIRED or len(seen)!=15:raise ValueError(f"Expected 15 exact reviewed codes; missing {sorted(REQUIRED-seen)}")
    pending=[item for item in old if item["code"] not in seen]
    if len(pending)!=762 or len(pending)+len(seen)+71!=848:
        raise ValueError("Source review count conservation failed")
    prior_boxes={item["code"] for item in old if catalog[item["code"]]["metadata_cohort_not_official_classification"]==COHORT}
    if len(prior_boxes)!=110 or len(prior_boxes-seen)!=95:
        raise ValueError("Precon cohort source status changed")
    return {
        "schema":1,"cutoff":date,"prior_audit":PREV.name,"source":LEDGER.name,
        "new_source_backed_product_codes":15,
        "new_component_codes_of_parent_products":len(COMPONENT_PARENT),
        "new_box_or_collection_products":10,
        "cumulative_family_source_backed_codes":86,
        "cumulative_source_pending_codes":762,
        "previous_boxed_source_pending":110,
        "boxed_source_pending_after_batch":95,
        "reviewed_boxed_codes":sorted(verified,key=lambda x:x["code"]),
        "remaining_source_pending_queue":pending,
        "caveats":[
            "The 15 exact Scryfall code mappings are from archived Scryfall metadata; Wizards official articles verify the named products and cards but do not necessarily print all codes.",
            "Separate Scryfall scheme/plane component codes are not separately sold booster products.",
            "A Commander anthology containing four previously published decks does not imply four newly original expansions.",
            "The 86 cumulative source-backed product records do NOT mean 86 premier releases, 86 original-card sets or 86 Standard legal sets.",
            "The 95 remaining preconstructed/box codes and broader 762 pending codes require individual further source work.",
            "This is an as-of October 29 2026 snapshot, not live releases or format legality."
        ]
    }

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--write",action="store_true")
    j=p.parse_args()
    v=build(*(json.loads(x.read_text(encoding="utf-8")) for x in (BASE,PREV,LEDGER)))
    blob=encode(v)
    if j.write:OUT.write_bytes(blob)
    elif not OUT.exists() or OUT.read_bytes()!=blob:
        raise ValueError("Committed box/planar scheme audit missing or not reproducible")
    print(json.dumps({k:v[k] for k in ("new_source_backed_product_codes","new_component_codes_of_parent_products","cumulative_family_source_backed_codes","cumulative_source_pending_codes","boxed_source_pending_after_batch")},sort_keys=True))
if __name__=="__main__":main()
