#!/usr/bin/env python3
"""Read-only, fail-closed Phase 6 printing/debut/publication-era restrictions.

    python3 scripts/lore_deck_restrictions.py --stem original_primeval_dragons --set-code m19
    python3 scripts/lore_deck_restrictions.py --stem original_primeval_dragons --first-printed-in lea
    python3 scripts/lore_deck_restrictions.py --stem original_primeval_dragons --release-from 2000 --release-through 2010

Set restrictions apply to the *chosen printing*; first-printed-in checks the
earliest released English paper printing of that card's exact Oracle identity.
The publication-era dates are real-world card printing dates, NOT story eras.
Ambiguous/tied debuts are preserved, not silently reduced to one set. The
October 28 historical atlas is a dated, finite Scryfall-derived record, not
live legality or proof that an in-universe event occurred in that era.

No deck file, pilot approval, Grixis approval or locked snapshot is modified.
"""
from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path

import historical_set_lookup as atlas

ROOT = Path(__file__).resolve().parents[1]
AS_OF = date(2026, 10, 29)
UUID = re.compile(r"^[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}$")
STEM = re.compile(r"^[a-z0-9_]+$")


@dataclass(frozen=True)
class Restriction:
    chosen_sets: frozenset[str] = frozenset()
    first_sets: frozenset[str] = frozenset()
    release_from: date | None = None
    release_through: date | None = None
    as_of: date = AS_OF

    def validate(self):
        if not (self.chosen_sets or self.first_sets or self.release_from or self.release_through):
            raise ValueError("provide at least one optional printing/debut/publication-era restriction")
        if self.as_of > AS_OF:
            raise ValueError("historical atlas cannot verify dates after 2026-10-29")
        if self.release_from and self.release_through and self.release_from > self.release_through:
            raise ValueError("release-from must not follow release-through")
        catalog = json.loads((atlas.DATA / "catalog_2026-10-29.json").read_text())["sets"]
        invalid = (self.chosen_sets | self.first_sets) - set(catalog)
        if invalid:
            raise ValueError("unknown Phase 1B set code(s): " + ", ".join(sorted(invalid)))


def check_printing(card: dict, rule: Restriction, folder: Path = atlas.DATA) -> dict:
    """Check a selected, immutable pilot printing; fail closed on atlas mismatches.

    Historical shard row: [set, printing_id, oracle_id, name, collector,
    released_at, language, paper]. Never infer an identity from card name.
    """
    name = card.get("name") or "<missing card name>"
    selected = card.get("printing") or {}
    oid, pid = selected.get("oracle_id"), selected.get("id")
    result = {"name": name, "oracle_id": oid, "selected_set": selected.get("set"),
              "selected_printing": pid, "status": "UNKNOWN", "reasons": [],
              "first_recorded_sets": [], "first_recorded_date": None,
              "selected_release_date": None}
    if not isinstance(oid, str) or not UUID.fullmatch(oid) or not isinstance(pid, str) or not UUID.fullmatch(pid):
        result["reasons"].append("MISSING_STABLE_ORACLE_OR_PRINTING_ID")
        return result
    try:
        rows = atlas.load(oid[0], "cards", folder)[oid]
    except (FileNotFoundError, KeyError, ValueError):
        result["reasons"].append("ORACLE_ID_ABSENT_FROM_HISTORICAL_ATLAS")
        return result
    eligible = [r for r in rows if atlas.selected(r[1:], rule.as_of)]
    if not eligible:
        result["reasons"].append("NO_RELEASED_ENGLISH_PAPER_PRINTINGS_BY_CUTOFF")
        return result
    matches = [r for r in eligible if r[1] == pid]
    if len(matches) != 1:
        result["reasons"].append("CHOSEN_PRINTING_ABSENT_OR_AMBIGUOUS_IN_ATLAS")
        return result
    chosen = matches[0]
    if (chosen[0], chosen[4], chosen[5]) != (selected.get("set"), selected.get("collector_number"),
                                            selected.get("released_at")) or chosen[2] != oid:
        result["reasons"].append("CHOSEN_PRINTING_METADATA_MISMATCH")
        return result
    debut = min(row[5] for row in eligible)
    first_sets = sorted({row[0] for row in eligible if row[5] == debut})
    result.update({"first_recorded_date": debut, "first_recorded_sets": first_sets,
                   "selected_release_date": chosen[5]})
    if rule.chosen_sets and chosen[0] not in rule.chosen_sets:
        result["reasons"].append("SELECTED_SET_NOT_ALLOWED")
    if rule.first_sets and not (set(first_sets) & rule.first_sets):
        result["reasons"].append("FIRST_RECORDED_SET_NOT_ALLOWED")
    when = date.fromisoformat(chosen[5])
    if rule.release_from and when < rule.release_from:
        result["reasons"].append("SELECTED_PRINTING_BEFORE_PUBLICATION_ERA")
    if rule.release_through and when > rule.release_through:
        result["reasons"].append("SELECTED_PRINTING_AFTER_PUBLICATION_ERA")
    result["status"] = "EXCLUDED" if result["reasons"] else "ALLOWED"
    return result


def evaluate(cards: list[dict], rule: Restriction, folder: Path = atlas.DATA) -> dict:
    rule.validate()
    rows = [check_printing(card, rule, folder) for card in cards]
    totals = {state: sum(r["status"] == state for r in rows) for state in ("ALLOWED", "EXCLUDED", "UNKNOWN")}
    return {"schema": "lore-deck-printing-restrictions/v1", "as_of": rule.as_of.isoformat(),
            "source": "Phase 1B historical English/paper Oracle-ID shards, frozen 2026-10-28",
            "restrictions": {"selected_set_codes": sorted(rule.chosen_sets),
                             "first_printed_in_set_codes": sorted(rule.first_sets),
                             "publication_era_from": rule.release_from.isoformat() if rule.release_from else None,
                             "publication_era_through": rule.release_through.isoformat() if rule.release_through else None},
            "totals": totals, "cards": rows,
            "limits": ["First-printed means first recorded released English paper Oracle-ID printing, not first fictional appearance.",
                       "Same-day multi-set debuts retain all first sets.",
                       "Publication-era filtering is NOT an in-universe story chronology filter.",
                       "A selected printing missing from the dated archive is UNKNOWN, not permitted.",
                       "Legality, bracket, currentness and deck approval are separate gates."]}


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--stem", required=True, help="existing UNAPPROVED lore-pilot file stem")
    p.add_argument("--set-code", action="append", default=[])
    p.add_argument("--first-printed-in", action="append", default=[])
    p.add_argument("--release-from", help="first YYYY year of publication-era restriction")
    p.add_argument("--release-through", help="last YYYY year of publication-era restriction")
    p.add_argument("--require-all", action="store_true", help="exit nonzero if any card is excluded")
    args = p.parse_args(argv)
    if not STEM.fullmatch(args.stem):
        p.error("invalid pilot stem")
    try:
        start = date(int(args.release_from), 1, 1) if args.release_from else None
        end = date(int(args.release_through), 12, 31) if args.release_through else None
        rule = Restriction(frozenset(args.set_code), frozenset(args.first_printed_in), start, end)
        source = ROOT / "data/lore_decks/drafts" / (args.stem + "_printing_evidence.json")
        evidence = json.loads(source.read_text(encoding="utf-8"))
        proposal = json.loads((source.parent / (args.stem + "_proposal.json")).read_text(encoding="utf-8"))
        if not proposal["status"].startswith("UNAPPROVED") or proposal["approval"]["approved"]:
            raise ValueError("only UNAPPROVED pilot drafts may be evaluated")
        result = evaluate(evidence["cards"], rule)
    except (ValueError, KeyError, FileNotFoundError, TypeError) as e:
        p.error(str(e))
    print(json.dumps(result, indent=2))
    return 2 if result["totals"]["UNKNOWN"] else 1 if args.require_all and result["totals"]["EXCLUDED"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
