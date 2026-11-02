#!/usr/bin/env python3
"""Replay evidence-backed, *unapproved* Commander strategy preflights.

This checks that four functional packages and three strategic play sequences
have real, unchanged Oracle anchors in each of the three existing pilot lists.
It measures the complete dated mana curve, but does NOT run games, evaluate
combos, certify power/brackets, modify a card, or approve any pilot (K108 open).

    python3 scripts/audit_phase6_strategy_preflight.py
    python3 scripts/audit_phase6_strategy_preflight.py --check
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_lore_pilot as pilots
import mv_ask

SPEC = ROOT / "data/lore_decks/strategy_preflight_spec_2026-11-01.json"
OUT = ROOT / "data/release/phase6_strategy_preflight_2026-11-01.json"
ROLES = ("ACCELERATION", "RESOURCE_FLOW", "INTERACTION", "PAYOFF")
POWER = {"SLOW_CASUAL_UNTESTED", "MANA_INTENSIVE_CASUAL_UNTESTED",
         "SYNERGY_DEPENDENT_CASUAL_UNTESTED"}
MV = re.compile(r"\*\*MV:\*\* (\d+(?:\.\d+)?)")
ORACLE = re.compile(r"^\s+> (.*)$", re.M)


def _digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _section(name: str) -> tuple[dict, str, float]:
    row = mv_ask.card_index().get(name.casefold())
    if not row:
        raise ValueError("missing exact card in dated index: " + name)
    section = mv_ask._section(ROOT / row["shard"], row["name"])
    if not section:
        raise ValueError("card shard has no exact named section: " + name)
    match = MV.search(section.split("- **Oracle text:**", 1)[0])
    if not match:
        raise ValueError("no reproducible dated mana value for " + name)
    return row, section, float(match[1])


def build(spec_path: Path = SPEC) -> dict:
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    if spec.get("schema") != "phase6-curated-strategy-preflight-spec/v1":
        raise ValueError("unrecognized strategy specification")
    files = sorted(pilots.SPECS.glob("*.json"))
    by_stem = {json.loads(p.read_text(encoding="utf-8"))["stem"]: p for p in files}
    if len(files) != 3 or len(by_stem) != 3 or len(spec.get("pilots", [])) != 3:
        raise ValueError("exactly the three existing pilots are required")

    reports, visited = [], set()
    for group in spec["pilots"]:
        stem = group["stem"]
        if stem not in by_stem or stem in visited:
            raise ValueError("unknown or duplicate pilot strategy: " + stem)
        visited.add(stem)
        pilot_spec = json.loads(by_stem[stem].read_text(encoding="utf-8"))
        audit = pilots.audit(by_stem[stem])
        if not audit["status"].startswith("UNAPPROVED"):
            raise ValueError("pilot has entered an approval workflow")
        proposal = json.loads(pilots.files(pilot_spec)["proposal.json"].read_text(encoding="utf-8"))
        if any(proposal["approval"][k] for k in ("approved", "locked", "certified")):
            raise ValueError("strategy preflight must not infer or grant approval")
        cards = json.loads(pilots.files(pilot_spec)["printing_evidence.json"].read_text(encoding="utf-8"))["cards"]
        names = [c["name"] for c in cards]
        if len(set(names)) != len(names):
            raise ValueError("duplicate named card in pilot")

        land_count = sum(pilot_spec["basics"].values())
        nonland_mvs = []
        card_sections = {}
        for card in cards:
            name = card["name"]
            row, section, mv = _section(name)
            if row["oracle_id"] != card["printing"]["oracle_id"]:
                raise ValueError("printing and dated Oracle identity disagree: " + name)
            card_sections[name] = section
            # Use the indexed *card type*, not name matching or art/beat.
            types = row["type_line"].split(" // ")[0].split(" — ")[0].split()
            if "Land" in types:
                land_count += 1
            else:
                nonland_mvs.append(mv)
        if len(nonland_mvs) + land_count != 100:
            raise ValueError("mana-curve partition is not exactly 100 cards")

        if group.get("power_hypothesis") not in POWER:
            raise ValueError("invalid or unjustifiably definitive power classification")
        for key in ("strategy", "opening", "middle", "finish", "failure_mode"):
            if not isinstance(group.get(key), str) or len(group[key]) < 100:
                raise ValueError("missing substantive staged strategy or known failure mode: " + key)
        if set(group.get("anchors", {})) != set(ROLES):
            raise ValueError("every strategy needs all four checked mechanical roles")

        proven = {}
        for role in ROLES:
            anchors = group["anchors"][role]
            if len(anchors) < 2 or len({a["name"] for a in anchors}) != len(anchors):
                raise ValueError("insufficient or repeated independently identified role anchors: " + role)
            checked = []
            for a in anchors:
                name, fragment = a["name"], a["oracle_contains"]
                if name not in names or not isinstance(fragment, str) or len(fragment) < 7:
                    raise ValueError("invalid or missing pilot anchor: " + name)
                # Oracle lines only: flavor text, third-party synergies, card
                # title and curator's prose must never prove a game mechanic.
                sec = card_sections[name].split("- **Flavor text", 1)[0]
                sec = sec.split("- **Commander notes", 1)[0]
                actual = " ".join(ORACLE.findall(sec))
                norm = lambda s: " ".join(s.casefold().split())
                if norm(fragment) not in norm(actual):
                    raise ValueError(f"unproven {role} Oracle anchor: {name} / {fragment}")
                checked.append({"card": name, "oracle_excerpt": fragment,
                                "oracle_id": next(c["printing"]["oracle_id"] for c in cards if c["name"] == name)})
            proven[role] = checked
        nonland_mvs.sort()
        reports.append({
            "stem": stem, "status": audit["status"], "approval_flags_all_false": True,
            "decklist_sha256": audit["decklist_sha256"], "oracle_index_date": "2026-10-15",
            "mana_curve": {"lands_including_basics": land_count, "nonlands_including_commander": len(nonland_mvs),
                           "average_nonland_mana_value": round(sum(nonland_mvs) / len(nonland_mvs), 3),
                           "nonlands_mv_at_least_5": sum(v >= 5 for v in nonland_mvs),
                           "nonlands_mv_at_least_7": sum(v >= 7 for v in nonland_mvs)},
            "strategy": group["strategy"], "opening": group["opening"],
            "middle": group["middle"], "finish": group["finish"],
            "failure_mode": group["failure_mode"],
            "power_hypothesis": group["power_hypothesis"],
            "verified_oracle_anchors": proven,
            "game_changers_in_dated_printing_evidence": audit["game_changers"]})
    if visited != set(by_stem):
        raise ValueError("a pilot was omitted")
    return {
        "schema": "phase6-strategy-preflight/v1", "as_of": "2026-11-01",
        "strategy_spec_sha256": _digest(spec_path),
        "dated_card_index_sha256": _digest(ROOT / "data/card_index.csv"),
        "scope": "Three existing source-graded UNAPPROVED pilots, unchanged; evidence for functional plans, not quantified matchup power",
        "status": "PRELIMINARY_MECHANICAL_STRATEGIES_K108_OPEN",
        "pilots": reports,
        "limitations": [
            "Oracle excerpts and mana values are from committed October 15 card shards, not a live updated legality or rulings feed.",
            "Card text establishes a possible mechanic, not a goldfish, mulligan, interaction, color-fixing, win-rate or matchup simulation.",
            "The average mana value includes the commander but does not model command-zone access, reductions, alternate casting costs or land timing.",
            "Power hypotheses are deliberately qualitative and untested; current Commander bracket and combo interactions remain unverified (K108/K110).",
            "All three pilot proposals remain UNAPPROVED; no pilot list, card, Grixis deck, owner gate or certification is modified.",
        ],
    }


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--check", action="store_true")
    args = p.parse_args(argv)
    actual = json.dumps(build(), indent=2, ensure_ascii=False) + "\n"
    if args.check:
        if OUT.read_text(encoding="utf-8") != actual:
            raise ValueError("strategy preflight evidence stale")
        print("PASS three unapproved strategy preflights: four Oracle-proven roles and exact dated mana curves")
    else:
        OUT.write_text(actual, encoding="utf-8")
        print("Wrote " + str(OUT.relative_to(ROOT)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
