#!/usr/bin/env python3
"""Fail-closed owner-authorized *bounded* repository completion acceptance.

On 2026-11-02 Cory explicitly chose a new repository finish line: existing
source-graded capabilities and visible UNKNOWN outcomes may satisfy the 14
unfinished construction checkboxes.  This is not retroactive primary-source
corroboration, exhaustive canon history, final deck tests, pilot approval or
permanent fulfillment of recurring monitoring.  The artifact must preserve
every limitation and is separate from the v3.00 foundation certificate.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_foundation_milestone_certificate as foundation
import audit_full_checklist as checklist
import audit_phase6_engine_scope as engine
import audit_phase6_strategy_preflight as strategy

RELEASE = ROOT / "data/release"
SETS = ROOT / "data/set_atlas"
LORE = ROOT / "data/lore_research"
OUT = RELEASE / "bounded_repository_completion_2026-11-02.json"

K045 = {"bchr", "rin", "itp", "ph17", "ph18", "ph19", "ph20", "ph21", "ph22", "ph23", "phtr", "punk", "w16"}
K046 = {"rqs", "mgb", "ath", "brb", "btd", "dkm", "psal", "phuk", "dpa", "ps11", "g17"}
GATES = {
    "K022": ("SOURCE_GAP_DOCUMENTED", "Two foreign-border Scryfall variants remain provisional and have no independently corroborated Wizards source."),
    "K045": ("SOURCE_GAP_DOCUMENTED", "Thirteen curated, foreign, starter or special codes stay individually pending; no new official product evidence is inferred."),
    "K046": ("SOURCE_GAP_DOCUMENTED", "Eleven older boxed and regional products remain source-pending and never automatically become premier sets."),
    "K074": ("SOURCE_GRADED_RESEARCH_ACCEPTED", "Pack A has a sourced claims/relationship/card dossier; Elder Dragon genealogy, faction breadth and chronology remain incomplete."),
    "K078": ("DISPUTES_RETAINED_WITH_OWNER_DISPOSITIONS", "Seven genealogy disputes carry conservative owner dispositions; unresolved canon is not invented and pilot cards stay proposals."),
    "K079": ("SOURCE_GRADED_RESEARCH_ACCEPTED", "Pack B cited Thran, Yawgmoth, Old Phyrexia and Brothers' War dossier remains a bounded historical slice."),
    "K080": ("SOURCE_GRADED_RESEARCH_ACCEPTED", "Pack C cited Weatherlight, Legacy and invasions dossier is bounded; unextracted novels/side stories remain explicit."),
    "K088": ("PARTIAL_ORDER_ACCEPTED_WITH_UNKNOWNS", "All three pack dossiers and an acyclic strictly sourced partial chronology are published; unresolved cross-source pairs remain UNKNOWN."),
    "K098": ("CITED_ARC_COVERAGE_ACCEPTED", "Cited Mending and Gatewatch strands exist; no exhaustive planeswalker biography or total chronology is asserted."),
    "K099": ("CITED_ARC_COVERAGE_ACCEPTED", "Bolas and War of the Spark graph/story evidence is queryable; extraction of every event/card is not claimed."),
    "K100": ("CITED_ARC_COVERAGE_ACCEPTED", "Phyrexian and March of the Machine source arcs are represented without assuming every side-story consequence is ingested."),
    "K103": ("SOURCE_LOCAL_BRIDGES_WITH_UNKNOWN_PAIRS", "Eight verified legacy bridges allow conservative navigation; undated or unbridged cross-plane history is UNKNOWN."),
    "K108": ("STRATEGY_PREFLIGHT_ENGINE_READY", "Three unchanged unapproved pilots have four Oracle-proven roles, staged plans and dated mana curves; matchup power is untested."),
    "K110": ("VALIDATOR_READY_FOR_POST_BUILD_DECKS", "100-card/singleton/color/snapshot legality, printing and source-aware rules infrastructure is ready; live brackets, combos and rebuilt lists await later review."),
}
EXCLUDED = {"K105", "K112", "K113", "K114", "K125", "K126"}


def read(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify(path: Path, condition: bool, detail: str) -> None:
    if not condition:
        raise ValueError(f"{path.name}: {detail}")


def build(paths: dict[str, Path] | None = None) -> dict:
    files = {
        "scope": SETS / "phase1b_release_scope_story_bridge_2026-10-29.json",
        "catalog": SETS / "product_catalog_2026-10-29.json",
        "draft": SETS / "draft_starter_primary_audit_2026-10-29.json",
        "boxed": SETS / "boxed_precon_source_audit_2026-10-29.json",
        "dossiers": LORE / "pack_dossiers_2026-10-30.json",
        "genealogy": LORE / "pack_a_genealogy_disputes_2026-10-30.json",
        "dispositions": RELEASE / "pack_a_genealogy_owner_dispositions_2026-11-01.json",
        "chronology": LORE / "relative_chronology_2026-10-30.json",
        "bridges": LORE / "source_event_sequences_2026-10-30.json",
        "story_coverage": LORE / "story_coverage_inventory_2026-10-30.json",
        "rules": RELEASE / "lookup_rules_scope_review_2026-11-01.json",
        "strategy": RELEASE / "phase6_strategy_preflight_2026-11-01.json",
    }
    if paths:
        unknown = set(paths) - set(files)
        if unknown:
            raise ValueError("unknown evidence override: " + str(unknown))
        files.update(paths)
    d = {k: read(v) for k, v in files.items()}
    s, product = d["scope"], d["catalog"]
    for code in ("fbb", "4bb"):
        row = s["set_scope_records"][code]
        verify(files["scope"], row["scope_label"] == "localized_variant_provisional"
               and row["scope_evidence"] == "third_party_corroborated_only"
               and row["wizards_release_source"] is None, "foreign-border uncertainty was promoted")
    verify(files["catalog"], (K045 | K046 | {"fbb", "4bb"}) <= set(product["sets"]),
           "one or more named pending codes absent from frozen catalog")
    verify(files["draft"], K045 - {"bchr", "rin"} <= set(d["draft"]["draft_starter_pending_codes"]),
           "draft/starter primary-source exception was silently removed")
    boxed_pending = {x["code"] for x in d["boxed"]["remaining_source_pending_queue"]}
    verify(files["boxed"], K046 <= boxed_pending, "boxed regional primary-source exception was silently removed")
    for code in ("bchr", "rin"):
        verify(files["scope"], s["set_scope_records"][code]["wizards_release_source"] is None,
               "unsourced historical reprint was promoted")

    p = d["dossiers"]["families"]
    for family, expected in (("A", (48, 33, 21)), ("B", (18, 8, 26)), ("C", (107, 34, 68))):
        row = p[family]
        verify(files["dossiers"], (row["claim_count"], len(row["bibliography"]),
               len(row["lore_deck_commander_candidates"])) == expected,
               "pack " + family + " source-graded dossier drifted")
        verify(files["dossiers"], bool(row["uncertainties"]) and bool(row["relationship_map"])
               and bool(row["stage_sequence"]), "pack " + family + " limitations/relationships absent")
    g, o = d["genealogy"], d["dispositions"]
    verify(files["genealogy"], g["counts"]["disputes"] == 7
           and g["counts"]["evidence_quotes"] >= 23 and g["counts"]["open"] >= 6,
           "genealogy conflict was suppressed")
    verify(files["dispositions"], len(o["dispositions"]) == 7
           and {x["id"] for x in o["dispositions"]} == {f"GD{i}" for i in range(1, 8)}
           and o["canon_claims_promoted"] == 0 and o["deck_pilots_approved"] == 0
           and bool(o["remaining_source_questions"]), "unresolved genealogy/owner decision was overclaimed")
    chrono = d["chronology"]
    cc = chrono["counts"]
    verify(files["chronology"], cc["event_nodes"] >= 56 and cc["stated_edges"] >= 63
           and cc["cycles"] == 0 and 0 < cc["comparable_pairs"] < cc["total_pairs"]
           and chrono["l244_closure"]["closes_l244"] is False
           and bool(chrono["l244_closure"]["missing"]), "partial chronology wrongly treated as global proof")
    bridges = d["bridges"]["counts"]
    verify(files["bridges"], bridges["verified_legacy_bridges"] >= 8
           and 0 < bridges["ordered_pairs"] < bridges["total_pairs"],
           "cross-plane unknown-pair safety lost")
    coverage = d["story_coverage"]["totals"]
    verify(files["story_coverage"], coverage["arcs"] >= 33 and coverage["claims"] >= 1263
           and coverage["arcs_partial"] >= 2 and coverage["pages"] > coverage["cited_pages"],
           "partial source coverage was silently promoted to completeness")
    arc_keys = {x["arc"] for x in d["story_coverage"]["arcs"]}
    verify(files["story_coverage"], {"DOM/WAR", "BFZ/OGW", "BRO", "MOM", "ONE", "AKH/HOU"} <= arc_keys,
           "historical source arcs vanished")
    rules = d["rules"]
    verify(files["rules"], rules["post_bulletin_rulebreaker_and_meld_current_verdict"]
           == "UNKNOWN_UNTIL_OFFICIAL_TEXT_RECONCILED" and bool(rules["out_of_scope"]),
           "unverified current Commander rule/interaction silently promoted")
    st = d["strategy"]
    verify(files["strategy"], len(st["pilots"]) == 3
           and st["status"] == "PRELIMINARY_MECHANICAL_STRATEGIES_K108_OPEN"
           and all(x["status"].startswith("UNAPPROVED") and x["approval_flags_all_false"]
                   and len(x["verified_oracle_anchors"]) == 4 for x in st["pilots"]),
           "pilot strategy limitation, role anchors or unapproved status changed")
    # Reuse the stronger immutable baseline/printing/engine replay, not an
    # owner-acceptance inference from an archived markdown summary.
    foundation.check()
    engine_result = engine.build()
    strategy_result = strategy.build()
    if len(engine_result["pilots"]) != 3 or strategy_result != st:
        raise ValueError("protected deck or strategy-engine replay drifted")
    triage = checklist.build()
    if (triage["totals"]["checked"] != 131 or triage["totals"]["open"] != 6
            or triage["totals"]["remaining_repository_build"] != 0
            or triage["totals"]["excluded_from_repository_build"] != 6):
        raise ValueError("bounded finish line not exactly 131 checked / 6 owner exclusions")
    by_id = {x["id"]: x for x in triage["items"]}
    if (any(not by_id[k]["checked"] for k in GATES)
            or any(by_id[k]["checked"] for k in EXCLUDED)
            or len(GATES) != 14):
        raise ValueError("bounded gate or excluded historical checkbox misclassified")

    return {
        "schema": "owner-redefined-bounded-repository-completion/v1",
        "owner_decision_date": "2026-11-02",
        "decision": "Cory selected bounded completion: verified capabilities and explicit UNKNOWN source/canon/gameplay gaps constitute repository construction acceptance; this modifies the original strict checklist interpretation.",
        "status": "BOUNDED_REPOSITORY_BUILD_ACCEPTED_NOT_UNIVERSAL_CANON_OR_LIVE_DECK_CERTIFICATION",
        "gates": [{"id": k, "acceptance_mode": mode, "scope_limitation": note}
                  for k, (mode, note) in GATES.items()],
        "counts": {"bounded_gates_accepted": len(GATES), "historical_checklist_items": 137,
                   "historical_checked": 131, "historical_open_owner_exclusions": 6,
                   "active_repository_build_remaining": 0, "phase6_pilot_approvals": 0,
                   "pack_claims": {k: p[k]["claim_count"] for k in ("A", "B", "C")},
                   "chronology_known_pairs": cc["comparable_pairs"],
                   "chronology_total_pairs": cc["total_pairs"],
                   "source_arc_partial_count": coverage["arcs_partial"]},
        "evidence_sha256": {str(path.relative_to(ROOT)): sha(path) for path in files.values()},
        "foundation_milestone": "CERTIFIED_BOUNDED_KNOWLEDGE_FOUNDATION_MILESTONE_7_OF_7_UNCHANGED",
        "protected_grixis_digests_unchanged": True,
        "three_pilot_proposals_still_unapproved": True,
        "deferred_post_build_pilot_reviews": ["K112", "K113", "K114"],
        "recurring_upkeep_excluded_not_permanently_complete": ["K105", "K125", "K126"],
        "not_certified": [
            "Missing individual Wizards primary sources for foreign border, draft/starter and boxed/region-specific historical products",
            "A single canonical resolution for six disputed Elder Dragon genealogy matters",
            "Complete in-universe calendars and a total order across unbridged plane/story events",
            "Exhaustive every-article/every-card lore biographies or complete side-story consequences",
            "Empirically established Commander power/matchups, current unindexed interactions and brackets",
            "Any rebuilt final pilot list or individual owner pilot approval, deferred until after repository construction",
            "Perpetual completion of new-source/Oracle/rules monitoring and future-set ingestion",
        ],
    }


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--check", action="store_true")
    a = p.parse_args(argv)
    rendered = json.dumps(build(), indent=2, ensure_ascii=False) + "\n"
    if a.check:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != rendered:
            raise ValueError("owner-bounded repository acceptance is stale")
        print("PASS owner-bounded repository completion: 14 scoped gates, 0 active build, 6 preserved exclusions")
    else:
        OUT.write_text(rendered, encoding="utf-8")
        print("Wrote " + str(OUT.relative_to(ROOT)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
