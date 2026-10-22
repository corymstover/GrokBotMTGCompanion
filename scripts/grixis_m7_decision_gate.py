#!/usr/bin/env python3
"""Fail-closed, source-bound M7 candidate-review structural gate for all 62 decks.

No deck approval, no game simulation, no Oracle lookup and no M6/M7 acceptance.
Actual strategic merit is an authored judgment; this checks that a finished
owner proposal was subjected to comprehensive documented candidate comparison,
exact source/candidate inventory and bounded research/test practices.
"""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "data/grixis/registry.json"
SCHEMA = ROOT / "data/grixis/schemas/m7_decisive_optimization.schema.json"
DECISIONS = ROOT / "data/grixis/m7/decision_reviews"
BASIC_LANDS = {"Plains", "Island", "Swamp", "Mountain", "Forest", "Wastes"}
ENTRY = re.compile(r"^([0-9]+)x?\s+(.+)$")


class DecisionGateError(ValueError):
    pass


def read(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def safe_file(root: Path, relative: str):
    p = Path(relative)
    if p.is_absolute() or ".." in p.parts:
        raise DecisionGateError("Invalid candidate file path")
    resolved = (root / p).resolve()
    if not resolved.is_relative_to(root.resolve()) or not resolved.is_file():
        raise DecisionGateError("Candidate or baseline file absent/outside repository: " + relative)
    return resolved


def parse_list(path: Path, *, source_markdown=False):
    """Parse canonical source TXT or the archived canonical MD Archidekt block.

    Ignore companion for the *100* Commander card count; preserve it separately.
    Do not parse derived official-legal projections or Bot refined lists.
    """
    body=path.read_text(encoding="utf-8")
    if source_markdown:
        marker="## Decklist (Archidekt import)"
        if body.count(marker)!=1:
            raise DecisionGateError("Canonical source Markdown decklist section missing or ambiguous")
        after=body.split(marker,1)[1]
        if "```text" not in after or "```" not in after.split("```text",1)[1]:
            raise DecisionGateError("Canonical source Markdown fenced list missing")
        body=after.split("```text",1)[1].split("```",1)[0]
    cards=[]
    marked_commanders=[]
    companions=[]
    for line_number,line in enumerate(body.splitlines(),1):
        if not line.strip():
            continue
        m=ENTRY.fullmatch(line.strip())
        if not m:
            raise DecisionGateError(f"Invalid list line {path}:{line_number}")
        amount,raw_name=int(m.group(1)),m.group(2)
        if not 1<=amount<=100:
            raise DecisionGateError("Invalid positive quantity")
        tag=re.search(r"\\s+\\[([^\\]]+)\\]$",raw_name)
        role=(tag.group(1) if tag else "")
        name=(raw_name[:tag.start()] if tag else raw_name)
        if not name or "[" in name or "]" in name:
            raise DecisionGateError("Unsupported source card-name tag or Commander annotation")
        if role.startswith("Commander"):
            marked_commanders.extend([name]*amount)
        elif role=="Companion":
            companions.extend([name]*amount)
            continue
        elif role and not source_markdown:
            raise DecisionGateError("Final candidate must omit role tags except Commander/Companion")
        cards.extend([name]*amount)
    if len(cards)!=100 or not marked_commanders:
        raise DecisionGateError("Exactly 100 main-deck cards including commander(s) required")
    if cards[0]!=marked_commanders[0]:
        raise DecisionGateError("First main card must be Commander")
    if not 1<=len(marked_commanders)<=2:
        raise DecisionGateError("Only one or two commanders supported")
    if any(q>1 and n not in BASIC_LANDS for n,q in Counter(cards).items()):
        raise DecisionGateError("Nonbasic card duplicated or singleton not preserved")
    return cards,marked_commanders,companions


def canonical_source(root: Path, deck: dict):
    """Use explicitly imported approved source, never Bot-refined or projection."""
    exact=f"exports/grixis-archidekt/source-baseline/{deck['slug']}.txt"
    if (root/exact).is_file():
        return safe_file(root,exact),False
    archive=deck["canonical_project_list"]["path"].split("#",1)[0]
    if not archive.startswith("grixis/decks/") or not archive.endswith(".md"):
        raise DecisionGateError("No trusted per-deck source markdown reference")
    return safe_file(root,archive),True


def validate_companion(deck_id, companions):
    if deck_id=="Cecily__Bjorna__Lutri":
        if companions!=["Lutri, the Spellchaser"]:
            raise DecisionGateError("Lutri special companion outside 100 not preserved")
    elif companions:
        raise DecisionGateError("Unexpected companion outside canonical 100")


def check_text(x, label, min_length=30):
    if not isinstance(x, str) or len(x.strip()) < min_length:
        raise DecisionGateError(label + " requires substantive authored explanation")


def verify_packet(packet, *, root=ROOT, registry=None):
    if registry is None:
        registry = read(root / "data/grixis/registry.json")
    schema = read(root / "data/grixis/schemas/m7_decisive_optimization.schema.json")
    failures = sorted(jsonschema.Draft202012Validator(schema).iter_errors(packet),
                      key=lambda x: tuple(str(a) for a in x.absolute_path))
    if failures:
        raise DecisionGateError("M7 packet schema violations: " + "; ".join(
            ".".join(str(s) for s in v.absolute_path) + ": " + v.message
            for v in failures[:6]))
    deck_id = packet["deck_id"]
    r = registry.get("decks", {}).get(deck_id)
    if r is None:
        raise DecisionGateError("Unknown canonical roster deck ID: " + deck_id)
    if packet["canonical_baseline_sha256"] != r["source"]["recorded_sha256"]:
        raise DecisionGateError("M7 baseline does not match registry's exact recorded approved raw SHA")
    if packet["canonical_baseline_logical_hash"] != r["current_canonical_hash"]:
        raise DecisionGateError("M7 baseline does not match canonical logical source hash")
    source, markdown = canonical_source(root, r)
    baseline, commanders, companions = parse_list(source, source_markdown=markdown)
    validate_companion(deck_id, companions)
    final_path = packet["final_candidate"]["path"]
    if not final_path.startswith("data/grixis/m7/candidate_lists/") or not final_path.endswith(".txt"):
        raise DecisionGateError("Final unapproved 100-card candidate must be a separate engineering staging TXT")
    candidate_file = safe_file(root, final_path)
    actual_digest = hashlib.sha256(candidate_file.read_bytes()).hexdigest()
    if actual_digest != packet["final_candidate"]["sha256"]:
        raise DecisionGateError("Final staged candidate SHA-256 mismatch")
    proposed, proposed_commanders, proposed_companions = parse_list(candidate_file)
    validate_companion(deck_id, proposed_companions)
    if proposed_companions != companions:
        raise DecisionGateError("Project-authorized companion unexpectedly changed")
    if commanders != proposed_commanders:
        raise DecisionGateError("Commander substitution or command-zone identity drift")
    before, after = Counter(baseline), Counter(proposed)
    actual_adds = list((after - before).elements())
    actual_cuts = list((before - after).elements())
    requested = packet["final_changes"]
    if Counter(actual_adds) != Counter(requested["adds"]) or Counter(actual_cuts) != Counter(requested["cuts"]):
        raise DecisionGateError("Physical 100-card delta disagrees with claimed adds/cuts")
    if len(requested["adds"]) != len(requested["cuts"]):
        raise DecisionGateError("Adds/cuts not balanced")

    candidates = packet["material_candidates"]
    ids = [x["card"] for x in candidates]
    if len(ids) != len(set(ids)):
        raise DecisionGateError("Duplicate candidate judgment")
    selected = [x for x in candidates if x["judgment"] == "SELECT_ADD"]
    if set(x["card"] for x in selected) != set(requested["adds"]):
        raise DecisionGateError("Selected candidates do not exactly match final adds")
    if any(not set(x["named_cuts"]).intersection(requested["cuts"]) for x in selected):
        raise DecisionGateError("Selected candidate lacks an exact documented real cut")
    if any(x["card"] in baseline for x in selected):
        raise DecisionGateError("Existing baseline card was incorrectly treated as a new addition")
    if any(x["card"] in proposed for x in candidates if x["judgment"] in ("REJECT", "RETAIN_ALTERNATIVE", "EXCLUDE_INVALID") and x["card"] not in baseline):
        raise DecisionGateError("Rejected off-baseline candidate was added")
    if any(x["card"] not in before for x in packet["whole_deck_audit"]["weakest_slots"]):
        raise DecisionGateError("Weak-slot audit names card absent from actual baseline")
    weak_named = {x["card"] for x in packet["whole_deck_audit"]["weakest_slots"]}
    if len(weak_named) != len(packet["whole_deck_audit"]["weakest_slots"]):
        raise DecisionGateError("Duplicate weak slot cannot create review coverage")

    experiment_counts = Counter()
    for study in packet["expensive_experiments"]:
        experiment_counts[study["cluster_id"]] += 1
        if study["precommitted_max_runs"] > 2000:
            check_text(study.get("large_sample_justification"), "Above-2000 trial justification", 100)
        if not (set(study["exact_challenger_adds"]) <= set(ids)):
            raise DecisionGateError("Expensive test does not compare named material candidates")
        if len(study["exact_challenger_adds"]) != len(study["exact_challenger_cuts"]):
            raise DecisionGateError("Experiment variants are not balanced exact 100-card configurations")
        if not study["execution_receipt"].startswith(("https://github.com/", "data/", "grixis/")):
            raise DecisionGateError("Experiment receipt is not an inspectable GitHub/local artifact")
    for cluster, count in experiment_counts.items():
        if count > 1:
            tests = [x for x in packet["expensive_experiments"] if x["cluster_id"] == cluster]
            for subsequent in tests[1:]:
                check_text(subsequent["repeat_exception_reason"],
                           "Repeated expensive testing requires a new decision-changing defect", 65)

    if len(requested["adds"]) <= 1:
        audit = packet["low_swap_heightened_audit"]
        challenged = audit["weakest_slot_challenge"]
        if len({x["card"] for x in challenged}) != len(challenged):
            raise DecisionGateError("Heightened weak-slot audit duplicates an option")
        if len(challenged) < 5:
            check_text(audit.get("fewer_than_five_weak_slots_reason"),
                       "Fewer than five plausible weak slots requires explicit factual rationale", 70)
        if not set(x["card"] for x in challenged) <= weak_named:
            raise DecisionGateError("Heightened weak slots must be grounded in whole-deck audit")
        packages = audit["multi_slot_packages"]
        if len(packages) < 2:
            check_text(audit["no_two_package_reason"],
                       "Fewer than two credible multi-slot packages requires an explicit reason", 90)
        for p in packages:
            if len(p["adds"]) != len(p["cuts"]):
                raise DecisionGateError("Multi-slot portfolio changes lack exact cuts")
            if not set(p["adds"]).issubset(set(ids)):
                raise DecisionGateError("Multi-slot portfolio references unexamined candidate")
        if not any("OFF" in x.upper() or "UNRANK" in x.upper()
                   for x in packet["candidate_sources"]):
            raise DecisionGateError("Low-swap recommendation lacks explicit off-ranking search provenance")
    return {
        "deck_id":deck_id,
        "status":"M7_STRUCTURALLY_DECISION_READY_NOT_OWNER_APPROVED",
        "new_swaps":len(requested["adds"]),
        "material_candidates":len(candidates),
        "expensive_experiments":len(packet["expensive_experiments"]),
        "has_heightened_low_swap_audit":len(requested["adds"]) <= 1,
        "canonical_unchanged":True,
        "m6_certification_not_inferred":True,
    }


def check_all_canonical_source_imports(*, root=ROOT, registry=None):
    """Smoke test authority-backed source inventory for every one of the 62 IDs.

    This validates physical source quantities and known companions, but not
    live external canonical SHA freshness or current Oracle legality.
    """
    registry = registry or read(root / "data/grixis/registry.json")
    if len(registry["decks"])!=62:
        raise DecisionGateError("Canonical roster not 62")
    for deck_id, deck in registry["decks"].items():
        path,md=canonical_source(root,deck)
        cards,cmd,companions=parse_list(path,source_markdown=md)
        validate_companion(deck_id,companions)
        if len(cards)!=100 or not cmd:
            raise DecisionGateError("Not a coherent 100-card source: "+deck_id)
    return len(registry["decks"])


def main():
    ap=argparse.ArgumentParser(description="Review staged M7 decision packets; no automatic approvals")
    ap.add_argument("--check", action="store_true", required=True)
    ap.add_argument("--file", type=Path, help="One staged M7 review JSON")
    ap.add_argument("--check-sources", action="store_true", help="Verify all 62 imported 100-card source mirrors")
    ap.add_argument("--require-complete", action="store_true",
                    help="Demand exactly the 62-authoritative-deck review artifacts")
    args=ap.parse_args()
    registry=read(REGISTRY)
    if len(registry["decks"]) != 62:
        raise SystemExit("Grixis roster size drift")
    if args.file:
        files=[args.file]
    else:
        files=sorted(DECISIONS.glob("*.json")) if DECISIONS.exists() else []
    if args.check_sources:
        print(f"Canonical-source mirror physical audit: {check_all_canonical_source_imports(root=ROOT,registry=registry)}/62 inspected; archived metadata is not a fresh external approval recheck.")
    seen=set()
    for item in files:
        data=read(item)
        result=verify_packet(data, root=ROOT, registry=registry)
        if item.stem != result["deck_id"] or result["deck_id"] in seen:
            raise DecisionGateError("Packet path or duplicate ID mismatch")
        seen.add(result["deck_id"])
        print(json.dumps(result, sort_keys=True))
    if args.require_complete and (len(files) != 62 or seen != set(registry["decks"])):
        raise SystemExit("M7 owner-candidate coverage incomplete: "
                         + str(len(seen)) + "/62.")
    print(f"M7 decisive candidate packet structural coverage {len(seen)}/62; "
          "no owner approvals, current Oracle verification, or M6 certification inferred.")


if __name__=="__main__":
    main()
