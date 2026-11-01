#!/usr/bin/env python3
"""Fail-closed acceptance for *supported, dated* card and rules lookup routes.

This does not certify a gameplay simulator, every Commander variant, or that
the October 19 rules bulletin is already incorporated into the last official
Comprehensive Rules TXT. Affected cases must remain explicitly unresolved.

  python3 scripts/audit_lookup_rules_scope.py
  python3 scripts/audit_lookup_rules_scope.py --check
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data/release/lookup_rules_scope_review_2026-11-01.json"


def read(rel: str) -> dict:
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def require(value, reason: str) -> None:
    if not value:
        raise ValueError("lookup/rules scope: " + reason)


def build() -> dict:
    import sys
    sys.path.insert(0, str(ROOT / "scripts"))
    import commander_rules as C  # noqa: E402
    import mv_ask as M  # noqa: E402

    previous = read("data/card_db/oracle_drift_2026-10-30.json")
    delta = read("data/scryfall_snapshots/oct30_to_nov01_2200_release_delta_2026-11-01.json")
    manifest = read("data/scryfall_snapshots/snap-20261101-2200-live-20261101.manifest.json")
    bulletin = read("data/rules/cr_20261019_bulletin_review.json")
    require(delta["source_bytes_sha256_and_counts_verified"] is True and
            delta["current_snapshot"] == manifest["snapshot_id"] == "snap-20261101-2200-live-20261101" and
            delta["current_manifest_files"] == manifest["files"], "newest independently replayed bulk provenance absent")
    require({k: manifest["files"][k]["records"] for k in ("oracle-cards", "default-cards", "rulings")} ==
            {"oracle-cards": 39287, "default-cards": 120019, "rulings": 79706},
            "unexpected November 1 bulk record counts")
    require(delta["delta"]["rulings"]["identical_record_multiset"] and
            delta["delta"]["oracle-cards"]["existing_ids_with_tracked_field_changes"] == 7 and
            delta["delta"]["default-cards"]["existing_ids_with_tracked_field_changes"] == 49,
            "unreviewed current-source change")
    require(all(len(v) == 0 for v in previous["changed"].values()) and previous["index_rows"] == 33894,
            "October 30 indexed Oracle-text reconciliation no longer holds")
    with (ROOT / "data/card_index.csv").open(encoding="utf-8") as card_index:
        indexed = {row["oracle_id"] for row in csv.DictReader(card_index)}
    changes = delta["delta"]["oracle-cards"]["changed_existing_samples"]
    require(len(changes) == delta["delta"]["oracle-cards"]["existing_ids_with_tracked_field_changes"],
            "Oracle differences are not fully enumerated")
    impact = [x for x in changes if x["id"] in indexed]
    require(all(set(x["fields"]) <= {"layout"} for x in impact),
            "an indexed card has a new Oracle/rules-relevant field; must reconcile the shard first")
    parity = delta["indexed_card_parity"]
    require(parity["missing_indexed_ids"] == 0 and parity["indexed_ids"] == previous["index_rows"] and
            all(parity["field_differences"][k]["count"] == 0 for k in
                ("type_line", "color_identity", "commander_legality", "game_changer")),
            "indexed current Oracle/Commander critical fields diverge")
    art = delta["prior_art_source_integrity"]
    require(art["checked_specific_printings"] >= 581 and not art["missing_from_new_bulk"] and
            not art["material_art_identity_changes"], "previously reviewed printing identities changed")

    require(C.CR["effective"] == bulletin["committed_cited_excerpt_effective"] == "2026-09-25" and
            C.CR["source_url"] == bulletin["official_rules_page_still_links_to"] and
            bulletin["status"] == "OFFICIAL_UPDATE_BULLETIN_NEWER_THAN_LINKED_CR_DOWNLOAD" and
            bulletin["bulletin"]["published_on"] == "2026-10-19" and
            {"903.5e", "713"} <= set(bulletin["announced_new_rules"]),
            "the official post-September rules discrepancy has been hidden")

    normal = C.include("Sol Ring", ["Krark, the Thumbless"])
    illegal = C.include("Counterspell", ["Krark, the Thumbless"])
    exceptional = C.commander(["Tolabow, Loch Rascal"])
    published = M.ask("How does Urza's Saga interact with Urza's Tower?")
    absent = M.ask("How do Sol Ring and Serra Angel interact?")
    meld = M.ask("What does meld mean?")
    require(normal["result"]["allowed"] is True and normal["confidence"] == "QUALIFIED" and
            illegal["result"]["allowed"] is False and illegal["confidence"] == "QUALIFIED" and
            "color identity" in " ".join(illegal["result"]["reasons"]),
            "ordinary Commander color/identity checks regressed")
    require("RULEBREAKER_COMMANDER_EXCEPTION_NOT_MODELLED" in exceptional["flags"] and
            exceptional["later_official_rules_bulletin"]["url"] == bulletin["bulletin"]["url"],
            "new rulebreaker exception is presented as fully modelled")
    require(published["confidence"] == "QUALIFIED" and published["result"]["direct_rulings"] and
            absent["confidence"] == "QUALIFIED" and "NO_DIRECT_RULING" in absent["flags"] and
            "NO_RULES_SIMULATION" in absent["flags"], "published-ruling absence falsely resolved")
    require(meld["confidence"] == "QUALIFIED" and
            "RULES_UPDATE_AFFECTED_TOPIC_REQUIRES_CURRENT_CR_REVIEW" in meld["flags"] and
            meld["result"]["current_gameplay_application"] == "UNRESOLVED_PENDING_CURRENT_CR_TEXT_RECONCILIATION" and
            bulletin["bulletin"]["url"] in meld["sources"],
            "September meld/DFC source incorrectly treated as current conclusive rules")

    return {"schema": "bounded-lookup-rules-scope-review/v1", "reviewed_on": "2026-11-01",
            "status": "SUPPORTED_LOOKUPS_WITH_DATED_SOURCES_AND_FAIL_CLOSED_RULE_CHANGES_ACCEPTED",
            "owner_authorization": "Cory's November 1 finite foundation acceptance; no claim to all gameplay rules",
            "oracle_source": manifest["snapshot_id"],
            "indexed_oracle_ids_reconciled": parity["indexed_ids"],
            "indexed_november_oracle_text_or_identity_differences": 0,
            "november_unindexed_oracle_text_change_ids": [x["id"] for x in changes
                                                         if "oracle_text_digest" in x["fields"] and x["id"] not in indexed],
            "indexed_layout_only_changes": [x["id"] for x in impact],
            "rulings_record_count": manifest["files"]["rulings"]["records"],
            "new_rulings_since_october_30": 0,
            "current_full_cr_download_effective": C.CR["effective"],
            "newer_official_bulletin_date": bulletin["bulletin"]["published_on"],
            "post_bulletin_rulebreaker_and_meld_current_verdict": "UNKNOWN_UNTIL_OFFICIAL_TEXT_RECONCILED",
            "independent_checked_routes": ["normal Commander inclusion", "invalid identity inclusion",
                                           "rulebreaker advisory", "specific published ruling",
                                           "no published ruling", "meld/version mismatch"],
            "supported_scope": "Dated indexed card/printing lookup, Commander eligibility/inclusion under cited ordinary rules, "
                               "published-rulings retrieval and dated keyword evidence; unsupported cases return QUALIFIED or NOT_FOUND",
            "out_of_scope": ["Global/current gameplay simulation or a conclusive interaction with no matching official ruling",
                             "Unannounced/unsupported rulebreaker exceptions or current meld/DFC semantics after the bulletin",
                             "New unindexed Oracle IDs and automatically rewriting archived Commander lists",
                             "A future Scryfall bulk or revised official CR not yet independently replayed"],
            "full_foundation_release_certified": False}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    d = build()
    output = json.dumps(d, indent=2, ensure_ascii=False) + "\n"
    if a.check:
        require(OUT.is_file() and OUT.read_text(encoding="utf-8") == output, "committed review stale")
    else:
        OUT.write_text(output, encoding="utf-8")
    print(f"PASS supported rules/lookup scope: {d['indexed_oracle_ids_reconciled']} indexed IDs; "
          f"{len(d['independent_checked_routes'])} guarded routes; not a rules simulator")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
