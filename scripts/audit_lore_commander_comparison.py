#!/usr/bin/env python3
"""Fail-closed, dated commander-option comparisons for three UNAPPROVED pilots.

Each candidate's eligibility and color identity is replayed through the real
Commander-rules/card-shard route. Story context is either an existing audited
Wizards source on the exact named card, or explicitly an unverified thematic/
mechanical option. No proposal, list, approval or Grixis file is modified.

    python3 scripts/audit_lore_commander_comparison.py --check
    python3 scripts/audit_lore_commander_comparison.py --stem original_primeval_dragons
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_lore_pilot as pilot
import commander_rules as rules

SPEC = ROOT / "data/lore_decks/commander_comparison_spec_2026-11-01.json"
OUT = ROOT / "data/release/phase6_commander_comparison_2026-11-01.json"
CONTEXT = {"CURATED_OFFICIAL_SOURCE", "THEMATIC_UNVERIFIED_IDENTITY", "NO_VERIFIED_UGIN_ALLY_LINK"}


def build(spec_file: Path = SPEC):
    spec = json.loads(spec_file.read_text(encoding="utf-8"))
    if spec["schema"] != "phase6-commander-comparison-spec/v1":
        raise ValueError("unknown comparison spec schema")
    pilot_paths = {json.loads(path.read_text(encoding="utf-8"))["stem"]: path
                   for path in pilot.SPECS.glob("*.json")}
    if len(spec["pilots"]) != 3 or len(pilot_paths) != 3:
        raise ValueError("every one of three known pilots must be compared")
    found = set()
    reports = []
    for group in spec["pilots"]:
        stem = group["stem"]
        if stem not in pilot_paths or stem in found:
            raise ValueError("unrecognized or duplicate pilot comparison")
        found.add(stem)
        raw = json.loads(pilot_paths[stem].read_text(encoding="utf-8"))
        frozen = pilot.audit(pilot_paths[stem])
        if not frozen["status"].startswith("UNAPPROVED"):
            raise ValueError("pilot approval must remain pending")
        evidence = json.loads(pilot.files(raw)["printing_evidence.json"].read_text(encoding="utf-8"))
        curated = {c["name"]: c for c in evidence["cards"]}
        required = set(raw["color_identity"])
        candidates = []
        seen_names = set()
        if len(group["candidates"]) < 2:
            raise ValueError("must compare two or more commander options")
        for item in group["candidates"]:
            name = item["name"]
            if name in seen_names or item["context"] not in CONTEXT or len(item["context_note"]) < 35:
                raise ValueError("duplicate, ungraded or undocumented comparison candidate")
            seen_names.add(name)
            opinion = rules.commander([name])
            if opinion["confidence"] != "QUALIFIED" or not opinion["result"].get("allowed"):
                raise ValueError("candidate lacks date-qualified commander eligibility: " + name)
            if opinion["flags"] != [rules.HISTORICAL_LEGALITY_FLAG]:
                raise ValueError("candidate has an additional unmodelled rule ambiguity: " + name)
            cr = opinion["result"]["commanders"][0]
            if cr["scryfall_commander_legality"] != "legal" or cr["eligible_by_cr"] is not True:
                raise ValueError("unverified commander eligibility")
            context = item["context"]
            source_url, claim_tier = None, None
            record = curated.get(name)
            if context == "CURATED_OFFICIAL_SOURCE":
                if not record or record["tier"] not in ("DIRECT_DEPICTION", "CANON_REFERENCE"):
                    raise ValueError("official context must be audited story-grade evidence: " + name)
                if not record["source"].startswith("https://magic.wizards.com/"):
                    raise ValueError("official context must have a Wizards URL: " + name)
                source_url, claim_tier = record["source"], record["tier"]
            elif context == "THEMATIC_UNVERIFIED_IDENTITY":
                if record and record["tier"] not in ("LORE_INSPIRED", "MECHANICAL_SYMBOL"):
                    raise ValueError("cannot downgrade a confirmed story-graded candidate to an uncited thematic idea")
                if "not" not in item["context_note"].casefold() and "no " not in item["context_note"].casefold():
                    raise ValueError("thematic link requires an explicit non-canon limitation")
            elif context == "NO_VERIFIED_UGIN_ALLY_LINK":
                if record:
                    raise ValueError("unverified alternative must be outside the curated pilot")
                if "no verified" not in item["context_note"].casefold():
                    raise ValueError("unverified relationship must be expressly named")
            ci = cr["color_identity"]
            can_host = required <= set(ci)
            candidates.append({"name": cr["name"], "eligible_commander_in_dated_model": True,
                               "indexed_color_identity": ci, "candidate_index_source": cr["shard"],
                               "eligibility_basis": cr["basis"], "can_host_existing_100_card_color_pool": can_host,
                               "story_context_grade": context, "verified_first_party_story_source": source_url,
                               "existing_curated_card_tier": claim_tier,
                               "story_context_note": item["context_note"],
                               "currently_selected": name == raw["commander"]["name"]})
        if sum(row["currently_selected"] for row in candidates) != 1:
            raise ValueError("the original draft commander must be compared exactly once")
        if sum(row["can_host_existing_100_card_color_pool"] for row in candidates) < 2:
            raise ValueError("must compare at least two legally modelled color-pool options")
        reports.append({"stem": stem, "theme": raw["theme"], "draft_status": frozen["status"],
                        "selected_draft_color_pool": "".join(c for c in rules.COLORS if c in required),
                        "candidates": candidates, "number_eligible_to_host_color_pool": sum(
                            row["can_host_existing_100_card_color_pool"] for row in candidates)})
    if found != set(pilot_paths):
        raise ValueError("a pilot omitted from commander comparisons")
    return {"schema": "phase6-source-graded-commander-comparison/v1", "as_of": "2026-11-01",
            "scope": "Three existing unapproved pilot themes; two dated card/rules-eligible commander options each",
            "card_index_date": rules.CARD_SHARDS_AS_OF,
            "comprehensive_rules_effective": rules.CR["effective"],
            "newer_rules_bulletin": rules.RULES_BULLETIN["bulletin"]["published_on"],
            "index_sha256": hashlib.sha256((ROOT / "data/card_index.csv").read_bytes()).hexdigest(),
            "comparison_spec_sha256": hashlib.sha256(spec_file.read_bytes()).hexdigest(),
            "pilots": reports,
            "limitations": ["Not a live Commander legality/ban or current bracket certification; October 19 bulletin not reconciled with September 25 full CR.",
                            "Story context is graded; a thematic resemblance is not canon participant identity or a verified relationship.",
                            "Eligibility to host the existing color pool is necessary, not sufficient for deck quality or unchanged legality under a rulebreaker.",
                            "Each selected pilot remains UNAPPROVED; no deck/card selection is changed."]}


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--check", action="store_true")
    p.add_argument("--stem")
    a = p.parse_args(argv)
    result = build()
    if a.stem:
        matches = [row for row in result["pilots"] if row["stem"] == a.stem]
        if not matches:
            p.error("unrecognized pilot")
        print(json.dumps(matches[0], indent=2))
    elif a.check:
        if OUT.read_text(encoding="utf-8") != json.dumps(result, indent=2, ensure_ascii=False) + "\n":
            raise ValueError("commander comparison artifact stale")
        print("PASS commander candidates: 2 per pilot, dated identity and qualified story context")
    else:
        OUT.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print("Wrote " + str(OUT.relative_to(ROOT)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
