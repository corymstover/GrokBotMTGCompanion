#!/usr/bin/env python3
"""One-command, read-only M7 intake using the existing M6/Grok infrastructure.

Usage: python scripts/grixis_m7_one_command.py --deck next --output /tmp/m7.json

This PREPARES evidence. It does not choose upgrades, simulate Magic, mark P0
executed, approve a deck, or run paid models. ChatGPT applies strategic judgment
and the established M7/IJ gates to produce the eventual exact 100-card proposal.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
CANONICAL = "corymstover/grixis-commander-encyclopediaGPT"
ENGINEERING = "corymstover/GrokBotMTGCompanion"
HEX40 = re.compile(r"^[0-9a-f]{40}$")
HEX64 = re.compile(r"^[0-9a-f]{64}$")
ROW = re.compile(r"^\s*(\d+)x\s+(.+?)\s*$")
GROK_FIRST_PASSES = {
    "Kefka__Court_Mage": 673,
    "Kess__Dissident_Mage": 674,
    "Grixistax___October_2026": 675,
    "Loki__the_Deceiver": 676,
    "Lord_of_Tresserhorn": 677,
    "Lord_Xander__the_Collector": 678,
    "Lynde__Cheerful_Tormentor": 679,
    "Mai_and_Zuko": 680,
}
BLUEPRINT_BRANCH = "chatgpt-cycle76-m6-refinement"
# Verified punctuation/spacing-only legacy ID spellings. A card identity/name
# change (e.g. future-release rename) is not an alias without provenance.
BLUEPRINT_ID_ALIASES = {
    "Anhelo_the_Painter": "Anhelo__the_Painter",
    "Ashad_the_Lone_Cyberman": "Ashad__the_Lone_Cyberman",
    "Be_lakor_the_Dark_Master": "Be_lakor__the_Dark_Master",
}


class IntakeError(RuntimeError):
    pass


def need(value, detail):
    if not value:
        raise IntakeError(detail)
    return value


def github_get(url: str) -> bytes:
    headers = {"User-Agent": "grixis-m7-one-command-source-verifier",
               "Accept": "application/vnd.github+json"}
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    with urlopen(Request(url, headers=headers), timeout=20) as response:
        return response.read()


def json_from(url: str):
    return json.loads(github_get(url).decode("utf-8"))


def choose(registry: dict, requested: str):
    ids = list(registry["decks"])
    need(len(ids) == 62, "Canonical roster is not exactly 62")
    if requested.lower() in ("next", "auto"):
        pending = [i for i in ids if "_M7_" not in
                   str(registry["decks"][i].get("approved_list_artifact", ""))]
        need(pending, "All 62 current decks already have M7 approval artifacts")
        return pending[0], ids.index(pending[0]) + 1
    normalized = requested.removeprefix("#")
    if normalized.isdecimal():
        index = int(normalized)
        need(1 <= index <= len(ids), "Deck number outside 1–62")
        return ids[index - 1], index
    need(requested in registry["decks"], f"Not a canonical deck ID: {requested}")
    return requested, ids.index(requested) + 1


def quantity_check(raw: bytes) -> dict:
    try:
        data = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise IntakeError("Canonical deck bytes are not UTF-8") from exc
    items = []
    for line in data.splitlines():
        need(ROW.fullmatch(line), f"Non-decklist line in canonical source: {line[:80]}")
        m = ROW.fullmatch(line)
        items.append((int(m.group(1)), m.group(2)))
    # The explicitly authorized Lutri companion exists outside the 100.
    physical = sum(n for n, name in items if "[Companion]" not in name)
    need(physical == 100, f"Canonical deck has {physical} cards, expected 100")
    need(items and "[Commander]" in items[0][1], "Commander not identified first")
    return {"physical_commander_deck_cards": physical,
            "text_rows": len(items),
            "outside_100_companions": sum(n for n, s in items if "[Companion]" in s),
            "commander": items[0][1]}


def plan_inventory(root: Path, deck_id: str, *, source: bytes | None = None,
                   pinned_ref: str | None = None, blueprint_id: str | None = None):
    expected_id = blueprint_id or BLUEPRINT_ID_ALIASES.get(deck_id, deck_id)
    path = root / "data/grixis/m6/test_blueprints" / (expected_id + ".json")
    if deck_id == "Abaddon_the_Despoiler":
        return {"plan": "ABADDON_EXCLUDED_OWN_EXISTING_M6_WORK", "P0": [], "P1": [],
                "designed_not_executed": True}
    need(source is not None or path.is_file(), f"Missing M6 commander-effect plan for {deck_id}")
    plan = json.loads(source.decode("utf-8") if source is not None
                      else path.read_text(encoding="utf-8"))
    need(plan.get("deck_id") == expected_id,
         f"M6 blueprint ID does not match requested deck: {deck_id}")
    cases = plan.get("cases", plan.get("tests"))
    need(isinstance(cases, list), f"Unrecognized M6 plan schema for {deck_id}")
    get_id = lambda x: x.get("id") or x.get("case_id") or x.get("test_id")
    groups = {priority: [get_id(c) for c in cases if c.get("priority") == priority]
              for priority in ("P0", "P1")}
    need(all(groups[p] and all(groups[p]) for p in groups),
         f"Missing P0/P1 identifiers in {deck_id} plan")
    need(len(set(groups["P0"] + groups["P1"])) == len(cases),
         f"Duplicate or unclassified M6 cases in {deck_id} plan")
    return {"plan": str(path.relative_to(root)), "pinned_source_commit": pinned_ref,
            "engineering_blueprint_id": expected_id,
            "P0": groups["P0"],
            "P1": groups["P1"], "designed_not_executed": True}


def classify_grok_files(files: list, deck_id: str):
    paths = [x["filename"] for x in files]
    certs = [p for p in paths if p.startswith("data/grixis/m6/ij/certificates/")
             and p.endswith(".json")]
    mechanics = [p for p in paths if p.startswith("tests/test_m6_")
                 and ("mechanics" in p or "ij" in p)]
    decisions = [p for p in paths if p == f"data/grixis/m7/decision_reviews/{deck_id}.json"]
    return {"scoped_ij_receipts": certs, "mechanics_test_files": mechanics,
            "first_pass_m7_decision_packets": decisions,
            "old_evidence_is_not_final_candidate_certification": True}


def build_packet(*, registry: dict, deck_id: str, order: int,
                 canonical_sha: str, raw_deck: bytes, plan: dict,
                 grok_pr: int | None, grok_head: str | None = None,
                 grok_changed_files: list | None = None):
    deck = registry["decks"][deck_id]
    approved_sha = deck.get("approved_list_sha256", "")
    need(HEX64.fullmatch(approved_sha), f"Missing approved SHA for {deck_id}")
    need(hashlib.sha256(raw_deck).hexdigest() == approved_sha,
         f"Canonical deck bytes do not match approved raw SHA for {deck_id}")
    counted = quantity_check(raw_deck)
    need(HEX40.fullmatch(canonical_sha), "Canonical GitHub main commit is not pinned")
    grok = {"pr": grok_pr, "head": grok_head, "available": bool(grok_head),
            "status": "EXISTING_FIRST_PASS_REQUIRES_INDEPENDENT_REVIEW" if grok_head
                      else "FIRST_PASS_NOT_FETCHED_OR_NOT_AVAILABLE"}
    if grok_head:
        need(HEX40.fullmatch(grok_head), "Unpinned Grok research PR head")
        grok.update(classify_grok_files(grok_changed_files or [], deck_id))
    return {
        "contract": "Grixis M7 ONE_COMMAND_SOURCE_INTAKE_V1",
        "status": "RESEARCH_INTAKE_ONLY_NOT_OWNER_READY",
        "deck_order": order, "deck_id": deck_id,
        "canonical": {"repo": CANONICAL, "commit": canonical_sha,
                      "approved_raw_sha256": approved_sha,
                      "approved_artifact": deck.get("approved_list_artifact"),
                      **counted},
        "m6_plan": plan, "grok_original": grok,
        "must_reuse": ["M6 deep review", "Pass C owner-equivalent with waiver",
                       "existing phase B and scoped I/J", "Grok saved alternatives",
                       "Scryfall Oracle and EDHREC Top/High Lift", "M7 decision gate"],
        "finalization_requires": ["complete 100-card strategy and additions/cuts",
                                  "actual required P0 passes and P1 dispositions",
                                  "exact-final-list IJ case scope transfer",
                                  "final M7 decision gate and current Oracle legality",
                                  "explicit owner approval of raw SHA-256",
                                  "canonical M7 provenance gate + exact-head CI"],
        "next_action": "Independent commander-first final optimization and case-bound verification, one final owner packet; no research treadmill.",
    }


def render_brief(packet: dict) -> str:
    c = packet["canonical"]
    p = packet["m6_plan"]
    grok = packet["grok_original"]
    return (f"# Deck #{packet['deck_order']} — {packet['deck_id']}\n\n"
            f"- Source: canonical `{c['commit']}`, approved raw `{c['approved_raw_sha256']}`\n"
            f"- Exactly {c['physical_commander_deck_cards']} commander-deck cards, first `{c['commander']}`\n"
            f"- M6 blueprint: {len(p['P0'])} P0, {len(p['P1'])} P1 designed cases; **not assumed executed**\n"
            f"- Grok first pass: PR #{grok['pr'] or 'none'}, {grok['status']}\n"
            f"- Status: **RESEARCH INTAKE ONLY — not owner-ready, not mechanically certified**\n\n"
            "Next: reuse evidence, decide genuine upgrades, verify complete final 100, "
            "run M6/IJ/M7 gates, present one list + hash for Cory's approval.\n")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--deck", default="next", help="next, #25, 25 or exact canonical deck ID")
    ap.add_argument("--grok-pr", type=int, default=None, help="Override discovered first-pass PR number")
    ap.add_argument("--output", type=Path, help="Optional JSON evidence artifact (no canonical write)")
    args = ap.parse_args()
    try:
        branch = json_from(f"https://api.github.com/repos/{CANONICAL}/branches/main")
        sha = branch["commit"]["sha"]
        registry = json_from(f"https://raw.githubusercontent.com/{CANONICAL}/{sha}/state/current_deck_overrides.json")
        deck_id, order = choose(registry, args.deck)
        rel = registry["decks"][deck_id]["approved_list_artifact"]
        need(isinstance(rel, str) and not rel.startswith("/") and ".." not in rel.split("/"),
             "Unsafe canonical source path")
        raw = github_get(f"https://raw.githubusercontent.com/{CANONICAL}/{sha}/{rel}")
        blueprint_id = BLUEPRINT_ID_ALIASES.get(deck_id, deck_id)
        local_blueprint = ROOT / "data/grixis/m6/test_blueprints" / (blueprint_id + ".json")
        # The original comprehensive M6 blueprints live on the established
        # engineering integration branch; the GitHub button is on default main.
        # Pin to a full commit SHA, and never treat design-only cases as passes.
        if local_blueprint.is_file() or deck_id == "Abaddon_the_Despoiler":
            plan = plan_inventory(ROOT, deck_id)
        else:
            engineering_branch = json_from(
                f"https://api.github.com/repos/{ENGINEERING}/branches/{BLUEPRINT_BRANCH}")
            blueprint_sha = engineering_branch["commit"]["sha"]
            need(HEX40.fullmatch(blueprint_sha), "M6 blueprint source not pinned")
            index = json_from(
                f"https://raw.githubusercontent.com/{ENGINEERING}/{blueprint_sha}/data/grixis/m6/test_blueprints/index.json")
            matches = [item for item in index["roster"] if item["deck_id"] == blueprint_id]
            need(len(matches) == 1,
                 f"No unique M6 index blueprint for {deck_id}; possible changed commander identity requires explicit reconciliation")
            blueprint_rel = matches[0]["path"]
            need(blueprint_rel.startswith("data/grixis/m6/test_blueprints/")
                 and ".." not in blueprint_rel.split("/"), "Unsafe M6 index path")
            blueprint_bytes = github_get(
                f"https://raw.githubusercontent.com/{ENGINEERING}/{blueprint_sha}/{blueprint_rel}")
            plan = plan_inventory(ROOT, deck_id, source=blueprint_bytes,
                                  pinned_ref=blueprint_sha, blueprint_id=blueprint_id)
            need(len(plan["P0"]) == matches[0]["P0"] and
                 len(plan["P1"]) == matches[0]["P1"],
                 "M6 blueprint case counts contradict pinned index")
        pr = args.grok_pr or GROK_FIRST_PASSES.get(deck_id)
        head = None
        files = []
        if pr:
            metadata = json_from(f"https://api.github.com/repos/{ENGINEERING}/pulls/{pr}")
            head = metadata["head"]["sha"]
            for page in range(1, 6):
                new_files = json_from(
                    f"https://api.github.com/repos/{ENGINEERING}/pulls/{pr}/files?per_page=100&page={page}")
                need(isinstance(new_files, list), "Unexpected research PR file list")
                files.extend(new_files)
                if len(new_files) < 100:
                    break
            else:
                raise IntakeError("Research PR has 500+ changed files; manual review needed")
        packet = build_packet(registry=registry, deck_id=deck_id, order=order,
                              canonical_sha=sha, raw_deck=raw, plan=plan,
                              grok_pr=pr, grok_head=head, grok_changed_files=files)
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(render_brief(packet))
    except (IntakeError, KeyError, ValueError, OSError) as exc:
        ap.exit(1, f"M7 SOURCE INTAKE BLOCKED: {exc}\n")


if __name__ == "__main__":
    main()
