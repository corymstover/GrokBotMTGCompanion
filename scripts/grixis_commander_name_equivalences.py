#!/usr/bin/env python3
"""Resolve canonical versus engineering deck IDs with source-declared name equivalence.

Official interchangeable printing names are NOT project legality exceptions.
No modifications to either registry and no authority promotion.
"""
from __future__ import annotations
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ALIASES = ROOT / "data/grixis/commander_name_equivalences.json"
REGISTRY = ROOT / "data/grixis/registry.json"
SHA64 = re.compile(r"^[0-9a-f]{64}$")

def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def normalize(identifier):
    return re.sub(r"[^a-z0-9]", "", identifier.casefold())

def reconcile(data, engineering_registry):
    canonical = data["canonical_deck_ids"]
    engineers = engineering_registry["decks"]
    exceptions = data["interchangeable_names"]
    if data["schema_version"] != 1 or len(canonical) != 62 or len(set(canonical)) != 62:
        raise ValueError("Canonical roster must contain exactly 62 unique deck IDs")
    if len(engineers) != 62:
        raise ValueError("Engineering registry must contain exactly 62 decks")
    if len(exceptions) != 1:
        raise ValueError("Only the source-verified Norman/Goben equivalence is registered")
    by_norm = {}
    for key in engineers:
        nk = normalize(key)
        if nk in by_norm:
            raise ValueError("Ambiguous normalized engineering IDs")
        by_norm[nk] = key
    alias_keys = {}
    used_targets = set()
    for item in exceptions:
        source = item["canonical_deck_id"]
        target = item["engineering_deck_id"]
        if source in alias_keys or target in used_targets:
            raise ValueError("Duplicate interchangeable-name alias")
        if source not in canonical or target not in engineers:
            raise ValueError("Alias must refer to actual canonical and engineering deck IDs")
        if item["rules_status"] != "official_interchangeable_names_not_project_exception":
            raise ValueError("Interchangeable name must not be recorded as a project legality exception")
        if not(item["preserve_canonical_deck_id"] and item["preserve_approved_list_sha256"] and item["count_as_one_deck"]):
            raise ValueError("Interchangeable printing cannot add a deck or override an approval")
        if source != "Goben__Gene_Splice_Savant" or target != "Norman_Osborn_Green_Goblin":
            raise ValueError("Only verified Norman/Goben alias mapping is allowed")
        recorded = item["original_card_approved_list_sha256"]
        if not SHA64.fullmatch(recorded) or engineers[target]["source"]["recorded_sha256"] != recorded:
            raise ValueError("Locked approved source SHA-256 differs from alias provenance")
        if not engineers[target]["source"]["recorded_matches_raw"]:
            raise ValueError("Engineering source byte/hash integrity has not been recorded")
        if engineers[target]["source"]["path"] != item["canonical_approved_list_artifact"]:
            raise ValueError("Approved source artifact drift")
        alias_keys[source] = target
        used_targets.add(target)
    mapping = {}
    for key in canonical:
        target = alias_keys.get(key) or by_norm.get(normalize(key))
        if target is None or target in mapping.values():
            raise ValueError("Missing, duplicate or ambiguous canonical deck reconciliation: " + key)
        mapping[key] = target
    if set(mapping.values()) != set(engineers):
        raise ValueError("Reconciliation cannot silently add or omit a commander")
    if data["certification_claims"]["full_m8_certification"] or data["certification_claims"]["independent_pass_c"]:
        raise ValueError("Name alignment is not milestone or independent review certification")
    if data["certification_claims"]["approved_card_swaps"] != 0:
        raise ValueError("Name reconciliation must never imply a card swap")
    return mapping

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--check",action="store_true")
    args=p.parse_args()
    if not args.check:
        p.error("--check required; script is read-only")
    m=reconcile(load(ALIASES),load(REGISTRY))
    print("Commander name equivalences: PASS; 62 unique canonical keys -> 62 unique engineering keys")
    print("Norman/Goben are one interchangeable-name commander; approvals and list hashes unchanged")
    print("No decklist swap, formal Pass C or M8 certification")
if __name__=="__main__":
    main()
