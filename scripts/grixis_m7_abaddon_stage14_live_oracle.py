#!/usr/bin/env python3
"""Live current Oracle and physical 100 audit for Abaddon Stage14 provisional six.

This deliberately does NOT use old revoked/other-candidate I/J certificates.
It reuses the established bounded Scryfall batch transport, but avoids the
older oracle assess() assertion that Keeper of Secrets must stay in the deck.
Research-only; the separate canonical main source is verified via GitHub
connector and recorded raw SHA, not misrepresented as read by CI.
"""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import argparse
import hashlib
import json

from scripts.grixis_m7_decision_gate import parse_list
from scripts.grixis_m7_abaddon_live_oracle import (
    ROOT, collected_cards, text_and_faces, OracleGateError, SCRYFALL
)

REPORT = ROOT / "data/grixis/m7/research_challengers/Abaddon_the_Despoiler_stage14_provisional_protected_wheel_six_20261023.json"
BASE = ROOT / "data/grixis/m7/candidate_lists/Abaddon_the_Despoiler_rev2.txt"
BASICS = {"Island", "Swamp", "Mountain"}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate(*, fetch=None, sleeper=None):
    m = json.loads(REPORT.read_text(encoding="utf-8"))
    if m["owner_ready"] or m["formal_m6_certification"] or m["m6_ij_candidate_specific_rebound"]:
        raise OracleGateError("Provisional candidate cannot self-certify or self-approve")
    candidate = ROOT / m["preferred_provisional"]["path"]
    approved = m["reference_canonical"]["raw_sha256"]
    proposed = m["preferred_provisional"]["raw_sha256"]
    if digest(BASE) != approved or digest(candidate) != proposed:
        raise OracleGateError("Exact baseline/new provisional physical SHA drift")
    original, original_cmd, original_comp = parse_list(BASE)
    changed, changed_cmd, changed_comp = parse_list(candidate)
    if original_cmd != ["Abaddon the Despoiler"] or changed_cmd != original_cmd:
        raise OracleGateError("Commander mismatch")
    if original_comp or changed_comp or len(original) != 100 or len(changed) != 100:
        raise OracleGateError("Physical list or companion mismatch")
    if Counter(changed) - Counter(original) != Counter(m["preferred_provisional"]["add"]):
        raise OracleGateError("Missing/extra additions")
    if Counter(original) - Counter(changed) != Counter(m["preferred_provisional"]["cut"]):
        raise OracleGateError("Missing/extra cuts")
    if any(q > 1 and n not in BASICS for n, q in Counter(changed).items()):
        raise OracleGateError("Nonbasic singleton violation")
    kwargs = {}
    if fetch is not None:
        kwargs["fetch"] = fetch
    if sleeper is not None:
        kwargs["sleeper"] = sleeper
    cards = collected_cards(set(changed), **kwargs)
    proof = {}
    for name, row in sorted(cards.items()):
        if row.get("object") != "card":
            raise OracleGateError("Noncard source item: " + name)
        legal = row.get("legalities", {}).get("commander")
        identity = row.get("color_identity")
        if legal != "legal" or not isinstance(identity, list) or not set(identity) <= set("UBR"):
            raise OracleGateError("Illegal identity/Commander status: " + name)
        if not row.get("oracle_id") or not row.get("scryfall_uri") or not row.get("games"):
            raise OracleGateError("Missing current card source: " + name)
        oracle = text_and_faces(row)
        if not oracle:
            raise OracleGateError("Missing current Oracle: " + name)
        proof[name] = {
            "oracle_id": row["oracle_id"], "scryfall_uri": row["scryfall_uri"],
            "mana_cost": row.get("mana_cost", ""), "mana_value": row["cmc"],
            "color_identity": sorted(identity), "commander_legality": legal,
            "oracle_text": oracle, "oracle_text_sha256": hashlib.sha256(oracle.encode()).hexdigest(),
        }
    expected = {
        "Coruscation Mage": ["Offspring {2}", "Whenever you cast a noncreature spell"],
        "Impact Tremors": ["Whenever a creature you control enters"],
        "Sanctum of Stone Fangs": ["At the beginning of your first main phase"],
        "Sakashima of a Thousand Faces": ["legend rule"],
        "Mount Doom": ["{1}{B}{R}, {T}: Mount Doom deals 1 damage to each opponent"],
        "Sheoldred, the Apocalypse": ["Whenever an opponent draws a card, they lose 2 life"],
        "Abaddon the Despoiler": ["spells you cast from your hand with mana value X or less"],
        "Noise Marine": ["Cascade"],
        "Nalfeshnee": ["Whenever you cast a spell from exile"]
    }
    for n, parts in expected.items():
        for part in parts:
            if part not in proof[n]["oracle_text"]:
                raise OracleGateError("Material changed/mechanical source drift: " + n)
    return {
        "stage": "LIVE_ORACLE_ABADDON_STAGE14_PROVISIONAL_SIX_RESEARCH_ONLY",
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "scryfall_endpoint": SCRYFALL,
        "authoritative_canonical_main_mode": "CONNECTOR_VERIFIED_SEPARATELY_SHA_PINNED_MIRROR_IN_CI",
        "approved_canonical_raw_sha256": approved,
        "candidate_raw_sha256": proposed,
        "physical_cards": len(changed),
        "oracle_unique_names_checked": len(proof),
        "commander_official_legality": "legal",
        "project_exceptions": [],
        "source": m["preferred_provisional"]["path"],
        "oracle_snapshot": proof,
        "owner_ready": False,
        "m6_ij_rebound": False,
        "owner_approval_inferred": False,
        "limitations": [
            "Current card identity/text/legality only, not proof of payable gameplay or strategic superiority.",
            "Live canonical/main outside this engineering Actions token was checked separately through connected GitHub.",
            "New M6 I tested-pool closure, final J bundle and owner M7 sign-off remain open."
        ],
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--out", type=Path, required=True)
    opts = p.parse_args()
    result = validate()
    opts.out.parent.mkdir(parents=True, exist_ok=True)
    opts.out.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("ABADDON_STAGE14_LIVE_ORACLE_PASS", json.dumps({
        "physical_cards": result["physical_cards"],
        "oracle_unique_names_checked": result["oracle_unique_names_checked"],
        "candidate_sha256": result["candidate_raw_sha256"],
        "owner_ready": False,
    }))


if __name__ == "__main__":
    main()
