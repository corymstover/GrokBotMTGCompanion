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
try:
    from scripts import grixis_authority as ga
except ModuleNotFoundError:  # direct python scripts/grixis_m7_decision_gate.py invocation
    import grixis_authority as ga

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "data/grixis/registry.json"
SCHEMA = ROOT / "data/grixis/schemas/m7_decisive_optimization.schema.json"
DECISIONS = ROOT / "data/grixis/m7/decision_reviews"
BASIC_LANDS = {"Plains", "Island", "Swamp", "Mountain", "Forest", "Wastes"}
# Named Oracle deck-building exceptions. These are *not* general Commander
# singleton waivers; actual card identity/text must still be verified at M7.
SINGLETON_LIMITED = {"Nazgûl": 9, "Seven Dwarves": 7}
SINGLETON_UNLIMITED = {
    "Relentless Rats", "Rat Colony", "Shadowborn Apostle",
    "Persistent Petitioners", "Dragon's Approach", "Slime Against Humanity",
    "Hare Apparent", "Templar Knight",
}
ENTRY = re.compile(r"^([0-9]+)x?\s+(.+)$")
# Owner supersession 2026-10-22: a tiny M7 delta may remain honest research,
# but must NEVER be presented for final owner approval as a complete deck.
MIN_OWNER_PRESENTABLE_SWAPS = 5
MIN_OWNER_PRESENTABLE_CANDIDATES = 10
MIN_OWNER_PRESENTABLE_WEAK_SLOTS = 8
WITHDRAWN_RESEARCH_STATUS = "RESEARCH_ONLY_WITHDRAWN_NOT_OWNER_PRESENTABLE"
READY_STATUS = "READY_FOR_EXACT_OWNER_APPROVAL_NOT_YET_APPROVED"
# Exception limited to exact 2026-10-22 owner-approved Abaddon M7 historical bytes.
# Never grandfather a new revision or a deck merely because its name matches.
LEGACY_OWNER_APPROVED_M7 = {
    ("Abaddon_the_Despoiler", "data/grixis/m7/candidate_lists/Abaddon_the_Despoiler_rev2.txt",
     "0d9f6df80cafc2a380199b7aec8112e4e54ccfec70024679607032cdf10f5790"):
    "data/grixis/m7/owner_approvals/Abaddon_the_Despoiler_M7_20261022.json",
}


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
        tag=re.search(r"\s+\[([^\]]+)\]$",raw_name)
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
    unexpected_repeats={
        n:q for n,q in Counter(cards).items()
        if q>1 and n not in BASIC_LANDS and n not in SINGLETON_UNLIMITED
        and q>SINGLETON_LIMITED.get(n,1)
    }
    if unexpected_repeats:
        raise DecisionGateError(f"Nonbasic singleton violation in {path}: {unexpected_repeats}")
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


def already_owner_approved_legacy_packet(packet, root):
    identity = (packet["deck_id"], packet["final_candidate"]["path"],
                packet["final_candidate"]["sha256"])
    receipt_path = LEGACY_OWNER_APPROVED_M7.get(identity)
    if not receipt_path:
        return False
    file = root / receipt_path
    if not file.is_file():
        return False
    approved = read(file)
    return (
        approved.get("owner_decision") == "APPROVE_EXACT_CANDIDATE"
        and approved.get("approved_raw_sha256") == identity[2]
        and approved.get("candidate_source") == identity[1]
        and approved.get("candidate_decision_review") ==
            "data/grixis/m7/decision_reviews/Abaddon_the_Despoiler_rev2.json"
        and approved.get("canonical_verified") is True
        and approved.get("canonical_approval_status") == "APPROVED"
        and approved.get("canonical_lock_status") == "LOCKED"
    )


def verified_superseding_owner_approved_source(packet, root):
    """Resolve later canonical owner-approved exact source, with fail-closed hash bindings.

    This offline engineering gate authenticates the owner receipt, the exact
    approved source bytes, the recorded canonical Git blob, and current Oracle
    logical baseline; separately recheck external canonical main for freshness.
    A proposed candidate can NEVER impersonate the approved baseline.
    """
    binding = packet.get("superseded_canonical_approval")
    if binding is None:
        return None
    receipt = read(safe_file(root, binding["approval_receipt_path"]))
    if (receipt.get("deck_id") != packet["deck_id"]
            or receipt.get("owner_decision") != "APPROVE_EXACT_CANDIDATE"
            or receipt.get("canonical_verified") is not True
            or receipt.get("canonical_approval_status") != "APPROVED"
            or receipt.get("canonical_lock_status") != "LOCKED"
            or receipt.get("authority", {}).get("m7_exact_owner_approval") is not True):
        raise DecisionGateError("Superseding source lacks an exact verified owner APPROVED/LOCKED receipt")
    source_path = receipt.get("candidate_source", "")
    if not source_path.startswith("data/grixis/m7/candidate_lists/"):
        raise DecisionGateError("Approved source must be the separately staged historical final M7 list")
    source = safe_file(root, source_path)
    raw = source.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    git_blob = hashlib.sha1(b"blob " + str(len(raw)).encode("ascii") + b"\x00" + raw).hexdigest()
    if (digest != receipt.get("approved_raw_sha256")
            or digest != packet["canonical_baseline_sha256"]
            or git_blob != receipt.get("canonical_approved_deck_git_blob_sha")
            or git_blob != binding["canonical_live_git_blob_sha"]):
        raise DecisionGateError("Superseding approved source failed SHA256/live Git blob/receipt binding")
    oracle = read(safe_file(root, binding["source_bound_oracle_snapshot_path"]))
    historical = read(safe_file(root, binding["approved_oracle_snapshot_path"]))
    inventory, marked_commanders, companions = parse_list(source)
    known = historical.get("oracle_snapshot", {}).copy()
    newer = oracle.get("oracle_cards", {})
    for name, card in newer.items():
        if name in known and known[name].get("oracle_id") != card.get("oracle_id"):
            raise DecisionGateError("Current and historical Scryfall Oracle identity mismatch for " + name)
    known.update(newer)
    if any(name not in known or not known[name].get("oracle_id") for name in inventory):
        raise DecisionGateError("Approved baseline lacks complete source-bound Oracle IDs")
    # The source-bound Oracle-ID hash is a *different* authority from raw bytes.
    expanded = [("commander" if name in marked_commanders else "main",
                 known[name]["oracle_id"], quantity)
                for name, quantity in Counter(inventory).items()]
    if ga.logical_hash(expanded) != packet["canonical_baseline_logical_hash"]:
        raise DecisionGateError("Superseding baseline logical Oracle hash mismatch")
    return source, False


def verify_baseline_provenance_exception(packet, deck, root):
    """Fail-closed handling of a registry digest that is NOT the physical source hash.

    Only when the registry explicitly records ``recorded_matches_raw: false``
    may (and must) a packet carry ``baseline_provenance_exception``. The
    historical digest and physical raw SHA-256 are bound separately; the packet
    baseline must be the physical bytes, which must be vendored byte-for-byte.
    Returns the vendored source path, or None when the ordinary rule applies.
    No match between the two hashes is ever manufactured or implied.
    """
    source = deck.get("source", {})
    exception = packet.get("baseline_provenance_exception")
    if source.get("recorded_matches_raw") is not False:
        if exception is not None:
            raise DecisionGateError(
                "Baseline provenance exception is forbidden unless the registry records a digest/raw mismatch")
        return None
    if exception is None:
        raise DecisionGateError(
            "Registry digest does not match physical source bytes; a source-bound baseline provenance exception is required")
    raw = str(source.get("raw_sha256", ""))
    raw = raw[len("sha256:"):] if raw.startswith("sha256:") else raw
    if (not re.fullmatch(r"[0-9a-f]{64}", raw)
            or exception["historical_registry_digest"] != source.get("recorded_sha256")
            or exception["physical_raw_sha256"] != raw
            or exception["historical_registry_digest"] == exception["physical_raw_sha256"]
            or packet["canonical_baseline_sha256"] != raw
            or exception["source_repository"] != source.get("repository")
            or exception["source_path"] != source.get("path")):
        raise DecisionGateError("Baseline provenance exception does not bind the registry's separate digest and raw hash")
    check_text(exception["discrepancy_explanation"], "Baseline digest/raw discrepancy explanation", 80)
    vendored = safe_file(root, exception["vendored_source_copy"])
    if hashlib.sha256(vendored.read_bytes()).hexdigest() != raw:
        raise DecisionGateError("Vendored canonical source bytes do not match the registry physical raw SHA-256")
    return vendored


def verify_post_floor_search(packet, baseline, commanders, companions, material_ids, root):
    """Prospective owner rule: five is presentation floor, not research target.

    Check genuine additional role challenges and full-100 higher-swap evidence;
    this cannot itself prove strategic optimum or multiplayer win rates.
    """
    audit = packet.get("open_ended_optimization_audit")
    if not audit:
        raise DecisionGateError(
            "OWNER POST-FLOOR HARD BLOCK: missing open-ended optimization audit; five is not a target or stop rule")
    if audit["floor_not_target"] is not True:
        raise DecisionGateError("The five-swap minimum was used as an optimization target")
    check_text(audit["remaining_99_review"], "Additional post-floor 99-card audit", 100)
    check_text(audit["quality_based_stop_reason"], "Count-independent quality-based stop rationale", 120)
    challenged = audit["post_floor_challenges"]
    incumbents = [entry["incumbent"] for entry in challenged]
    if len(set(incumbents)) < 2:
        raise DecisionGateError("Post-floor review must challenge two additional distinct retained incumbents")
    original = set(baseline)
    cuts = set(packet["final_changes"]["cuts"])
    selected = set(packet["final_changes"]["adds"])
    judgments = {x["card"]: x["judgment"] for x in packet["material_candidates"]}
    for entry in challenged:
        if entry["incumbent"] not in original or entry["incumbent"] in cuts:
            raise DecisionGateError("Extra incumbent challenge absent from baseline or already selected as a cut")
        if entry["challenger"] not in material_ids or entry["challenger"] in selected:
            raise DecisionGateError("Extra challenger unexamined or already among selected adds")
        if judgments[entry["challenger"]] != entry["disposition"]:
            raise DecisionGateError("Post-floor challenger verdict contradicts material judgment")
        check_text(entry["tradeoff"], "Post-floor additional cut tradeoff", 50)
    larger = audit["larger_swap_packages"]
    if not larger:
        check_text(audit.get("no_credible_larger_package_reason"),
                   "No larger credible package must be justified with actual full-deck tradeoffs", 160)
    else:
        if audit.get("no_credible_larger_package_reason") is not None:
            raise DecisionGateError("No-larger-package claim conflicts with supplied higher-count option")
        for alt in larger:
            path = alt["path"]
            if not path.startswith("data/grixis/m7/") or not path.endswith(".txt"):
                raise DecisionGateError("Larger option must be an actual staged M7 100-card TXT")
            source = safe_file(root, path)
            if hashlib.sha256(source.read_bytes()).hexdigest() != alt["sha256"]:
                raise DecisionGateError("Larger 100-card option source SHA mismatch")
            cards, cmds, comps = parse_list(source)
            if cmds != commanders or comps != companions:
                raise DecisionGateError("Larger configuration changes commander or companion")
            adds = list((Counter(cards) - Counter(baseline)).elements())
            cuts2 = list((Counter(baseline) - Counter(cards)).elements())
            if Counter(adds) != Counter(alt["adds"]) or Counter(cuts2) != Counter(alt["cuts"]):
                raise DecisionGateError("Higher-swap option card changes do not match physical source")
            if len(adds) <= len(packet["final_changes"]["adds"]) or len(adds) != len(cuts2):
                raise DecisionGateError("Higher-count alternative must have genuinely more substitutions")
            if not set(adds) <= set(material_ids):
                raise DecisionGateError("Higher-swap alternative includes unexamined candidates")
            check_text(alt["case_for_extra_swaps"], "Case for genuinely larger swap package", 60)
            check_text(alt["why_not_selected"], "Opportunity-cost comparison rejecting larger package", 70)


def verified_kefka_one_deck_swap_floor_waiver(packet, root):
    """2026-10-24 exact SHA, Kefka only; NOT owner deck approval.

    No other deck, different candidate bytes or missing scoped case receipt can
    bypass the independent mandatory M6 P0/P1, Oracle, source or CI checks.
    """
    expected = "14277f6e9774c5ef02b4f92332b52684794367007abf81bc2d84ef7ad7bcaa7d"
    if not (packet["deck_id"] == "Kefka__Court_Mage"
            and packet["final_candidate"]["sha256"] == expected
            and packet["final_candidate"]["path"] == "data/grixis/m7/candidate_lists/Kefka__Court_Mage_M7_Rev1.txt"):
        return False
    evidence = safe_file(root, "data/grixis/m7/case_transfers/Kefka__Court_Mage_M7_Rev1_Exact_IJ_Transfer_20261024.json")
    data = read(evidence)
    if (data["candidate_raw_sha256"] != expected
            or data["deck_id"] != "Kefka__Court_Mage"
            or not data["kefka_only_owner_waiver"].startswith("I authorize a Kefka-only exception")
            or data["owner_exact_sha_approved"] is not False
            or data["canonical_changed"] is not False):
        raise DecisionGateError("Kefka's narrow floor waiver is not source-bound and unapproved")
    if {x["id"] for x in data["P0"]} != {"C1", "K1", "K2", "K3", "F1"}:
        raise DecisionGateError("Kefka floor-waiver P0 case inventory is incomplete")
    if {x["id"] for x in data["P1"]} != {"K4", "K5", "E1", "E2", "W1", "W2", "W3", "F2", "F3"}:
        raise DecisionGateError("Kefka floor-waiver P1 case inventory is incomplete")
    if any(x["result"] != "PASS_BOUNDED" for x in data["P0"]):
        raise DecisionGateError("Kefka P0 requirement has unverified case")
    return True


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
    superseding = verified_superseding_owner_approved_source(packet, root)
    if superseding is None:
        mismatch = verify_baseline_provenance_exception(packet, r, root)
        if not mismatch and packet["canonical_baseline_sha256"] != r["source"]["recorded_sha256"]:
            raise DecisionGateError("M7 baseline does not match registry's exact recorded approved raw SHA")
        if packet["canonical_baseline_logical_hash"] != r["current_canonical_hash"]:
            raise DecisionGateError("M7 baseline does not match canonical logical source hash")
        source, markdown = canonical_source(root, r)
    else:
        if packet.get("baseline_provenance_exception") is not None:
            raise DecisionGateError("Baseline provenance exception cannot combine with a superseding approval")
        source, markdown = superseding
    baseline, commanders, companions = parse_list(source, source_markdown=markdown)
    if superseding is None and mismatch:
        vendored, vcmds, vcomps = parse_list(mismatch)
        front = lambda cards: Counter(name.split(" // ", 1)[0] for name in cards)
        if front(vendored) != front(baseline) or vcmds != commanders or vcomps != companions:
            raise DecisionGateError(
                "Vendored physical canonical source inventory differs from the registry canonical project list")
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
    # A completed review with only a few changes is not automatically an
    # owner-presentable deck. Keep historical rejected packets source-bound,
    # but prohibit laundering the old recommendation into a ready status.
    ready = packet["readiness"] == READY_STATUS
    if not ready:
        if packet["readiness"] != WITHDRAWN_RESEARCH_STATUS:
            raise DecisionGateError("Unknown owner review disposition")
        check_text(packet.get("withdrawal_reason"),
                   "Withdrawn/historical research packet requires owner-visible reason", 80)
    else:
        if packet.get("withdrawal_reason"):
            raise DecisionGateError("A withdrawn owner-objection packet cannot be owner-ready")
        if len(requested["adds"]) < MIN_OWNER_PRESENTABLE_SWAPS and not verified_kefka_one_deck_swap_floor_waiver(packet, root):
            raise DecisionGateError(
                "OWNER HARD BLOCK: only " + str(len(requested["adds"])) +
                " genuine swaps; 0–4 replacements cannot be presented for M7 owner approval. "
                "Do not pad weak or cosmetic swaps; hold as honest research instead.")
        if len(candidates) < MIN_OWNER_PRESENTABLE_CANDIDATES:
            raise DecisionGateError(
                "Owner-ready M7 packet requires at least ten distinct material candidate judgments")
        if len(weak_named) < MIN_OWNER_PRESENTABLE_WEAK_SLOTS:
            raise DecisionGateError(
                "Owner-ready M7 packet requires eight distinct challenged incumbent roles/slots")
        audit = packet.get("low_swap_heightened_audit")
        if not audit:
            raise DecisionGateError(
                "Owner-ready M7 packet requires the full heightened opportunity audit, regardless of swap count")
        challenged = audit["weakest_slot_challenge"]
        if len({x["card"] for x in challenged}) < MIN_OWNER_PRESENTABLE_WEAK_SLOTS:
            raise DecisionGateError("Owner-ready heightened audit must challenge eight distinct incumbent slots")
        if not {x["card"] for x in challenged} <= weak_named:
            raise DecisionGateError("Owner-ready weak slots must be grounded in whole-deck audit")
        packages = audit["multi_slot_packages"]
        if len(packages) < 2:
            raise DecisionGateError("Owner-ready packet requires at least two distinct complete multiswap portfolios")
        if len({(tuple(p["adds"]),tuple(p["cuts"])) for p in packages}) < 2:
            raise DecisionGateError("Duplicated multiswap packages cannot fake full-deck alternatives")
        for p in packages:
            if len(p["adds"]) != len(p["cuts"]) or not set(p["adds"]) <= set(ids):
                raise DecisionGateError("Owner-ready alternative package lacks complete named adds/cuts")
        if not any("OFF" in x.upper() or "UNRANK" in x.upper() for x in packet["candidate_sources"]):
            raise DecisionGateError("Owner-ready packet lacks provenance of off-ranking/missed-synergy research")
        if not already_owner_approved_legacy_packet(packet, root):
            verify_post_floor_search(packet, baseline, commanders, companions,
                                     set(ids), root)
    return {
        "deck_id":deck_id,
        "status": ("M7_STRUCTURALLY_DECISION_READY_NOT_OWNER_APPROVED"
                   if ready else "M7_WITHDRAWN_RESEARCH_ONLY_NOT_OWNER_PRESENTABLE"),
        "owner_presentable": ready,
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
    owner_presentable=set()
    for item in files:
        data=read(item)
        result=verify_packet(data, root=ROOT, registry=registry)
        # An earlier, expressly withdrawn owner candidate is historical evidence.
        # Preserve that exact deck_id.json and allow a new numbered revision;
        # never permit a second simultaneously owner-ready variant.
        if not (item.stem == result["deck_id"] or
                re.fullmatch(re.escape(result["deck_id"]) + r"_rev[1-9][0-9]*", item.stem)):
            raise DecisionGateError("Packet filename does not match deck ID or numbered revision")
        if item.stem in seen:
            raise DecisionGateError("Duplicate packet path")
        seen.add(item.stem)
        if result["owner_presentable"] and not already_owner_approved_legacy_packet(data, ROOT):
            if result["deck_id"] in owner_presentable:
                raise DecisionGateError("Two simultaneously unapproved owner-ready M7 revisions of the same deck")
            owner_presentable.add(result["deck_id"])
        print(json.dumps(result, sort_keys=True))
    if args.require_complete and (len(owner_presentable) != 62 or owner_presentable != set(registry["decks"])):
        raise SystemExit("M7 owner-presentable coverage incomplete: "
                         + str(len(owner_presentable)) + "/62. Withdrawn research records do not count.")
    print(f"M7 packet historical/structural revisions {len(seen)}, "
          f"owner-presentable packets {len(owner_presentable)}/62; "
          "no owner approvals, current Oracle verification, or M6 certification inferred.")


if __name__=="__main__":
    main()
