#!/usr/bin/env python3
"""Fail-closed, live Scryfall current Oracle/Commander audit for Abaddon V2.

Scope: the exact canonical approved 100 + four *unapproved* staged 100-card
research challengers. One Scryfall /cards/collection lookup per *unique name*
(up to 75 per request), NOT 500 redundant card-name API calls.
This does not prove gameplay superiority, acceptance or owner approval.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import time
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from scripts.grixis_m7_decision_gate import parse_list

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data/grixis/m7/research_challengers/Abaddon_the_Despoiler_portfolio_v2.json"
SCRYFALL = "https://api.scryfall.com/cards/collection"
CANONICAL_SNAPSHOT = ROOT / "data/grixis/m7/authority_snapshots/Abaddon_the_Despoiler_Approved_2026-10-13.txt"
CANONICAL_SOURCE_MAIN_SHA_AT_SNAPSHOT = "856716a307c0277bb069f2d8f67e28018d4fd596"
CANONICAL = ("https://raw.githubusercontent.com/corymstover/"
             "grixis-commander-encyclopediaGPT/main/refinement/decklists/"
             "Abaddon_the_Despoiler_Approved_2026-10-13.txt")
HEADERS = {
    "User-Agent": "GrixisCommanderEncyclopedia-OracleAudit/1.0 (GitHub Actions; provenance testing)",
    "Accept": "application/json",
}
BASIC = {"Island", "Swamp", "Mountain"}
ALLOWED = {"B", "R", "U"}
SOURCE_ROW = re.compile(r"^(\d+)x\s+(.+?)\s+\([^)]+\)\s+\S+\s+\[([^]]+)\]$")
IDENTIFIER_BATCH_SIZE = 75
EXPECTED_VARIANTS = {
    "engine_only", "engine_answer_keeper", "engine_answer_betrayal",
    "combat_answer_keeper",
}


class OracleGateError(ValueError):
    pass


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def get_json(url, payload=None):
    """Bounded retries, descriptive headers and respectful pacing.

    No 'skip missing card' or stale-cache fallback: fail closed if 403,
    repeated 429, invalid JSON or unavailable connection.
    """
    headers = dict(HEADERS)
    data = None if payload is None else json.dumps(payload, ensure_ascii=False).encode("utf-8")
    if payload is not None:
        headers["Content-Type"] = "application/json"
    for i in range(3):
        req = Request(url, data=data, headers=headers, method="POST" if data else "GET")
        try:
            with urlopen(req, timeout=45) as response:
                return response.read()
        except HTTPError as exc:
            if exc.code not in (429, 500, 502, 503, 504) or i == 2:
                raise OracleGateError("HTTP %s from %s; current verification unavailable" % (exc.code, url)) from exc
        except (URLError, TimeoutError) as exc:
            if i == 2:
                raise OracleGateError("Live source unreachable; current verification unavailable") from exc
        time.sleep((i + 1) * 2)
    raise OracleGateError("Live data unverified")


def parse_approved_raw(data: bytes) -> tuple[list[str], list[str]]:
    cards, cmd = [], []
    for line in data.decode("utf-8-sig").splitlines():
        if not line.strip():
            continue
        match = SOURCE_ROW.fullmatch(line.strip())
        if not match:
            raise OracleGateError("Unrecognized canonical source row: " + line[:90])
        qty, name, role = match.groups()
        n = int(qty)
        cards.extend([name] * n)
        if role.startswith("Commander"):
            cmd.extend([name] * n)
    if len(cards) != 100 or cmd != ["Abaddon the Despoiler"]:
        raise OracleGateError("Live canonical not exact 100 / unexpected commander")
    return cards, cmd


def source_reconcile(manifest, canonical_raw: bytes):
    digest = sha256_bytes(canonical_raw)
    if digest != manifest["canonical_baseline_raw_sha256"]:
        raise OracleGateError("Live canonical source SHA drift: " + digest)
    actual, actual_cmd = parse_approved_raw(canonical_raw)
    base, cmd, companions = parse_list(ROOT / manifest["baseline_source_path"])
    if Counter(actual) != Counter(base) or actual_cmd != cmd or companions:
        raise OracleGateError("Engineering source mirror diverges from exact canonical TXT")
    return base, digest


def staged_variants(manifest, baseline):
    if manifest["stage"] != "M7_SOURCE_CORRECTED_RESEARCH_NOT_OWNER_READY":
        raise OracleGateError("V2 research stage changed; stop live audit")
    vlist = manifest["candidate_variants"]
    if {item["id"] for item in vlist} != EXPECTED_VARIANTS or len(vlist) != 4:
        raise OracleGateError("Registered portfolio changed")
    results = {"baseline": baseline}
    for v in vlist:
        path = v["path"]
        if not path.startswith("data/grixis/m7/research_challengers/") or not path.endswith(".txt"):
            raise OracleGateError("Untrusted challenger path")
        cards, commanders, companions = parse_list(ROOT / path)
        if commanders != ["Abaddon the Despoiler"] or companions or len(cards) != 100:
            raise OracleGateError("Incorrect physical commander/deck list: " + v["id"])
        before, after = Counter(baseline), Counter(cards)
        if (after - before) != Counter(v["adds"]) or (before - after) != Counter(v["cuts"]):
            raise OracleGateError("Physical adds/cuts drift: " + v["id"])
        results[v["id"]] = cards
    return results


def collected_cards(names, *, fetch=get_json, sleeper=time.sleep):
    """Resolve all unique names; reject missing, ambiguous, or stale substitutes."""
    names = sorted(set(names))
    response = {}
    for offset in range(0, len(names), IDENTIFIER_BATCH_SIZE):
        if offset:
            sleeper(0.65)
        chunk = names[offset:offset + IDENTIFIER_BATCH_SIZE]
        # Scryfall collection name identifier matches a DFC by the front
        # face, even when its canonical .name contains both face names.
        queries = [n.split(" // ", 1)[0] for n in chunk]
        if len(set(queries)) != len(chunk):
            raise OracleGateError("Ambiguous double-face lookup identity")
        raw = fetch(SCRYFALL, {"identifiers": [{"name": n} for n in queries]})
        try:
            data = json.loads(raw)
        except (TypeError, ValueError) as exc:
            raise OracleGateError("Non-JSON live Scryfall response") from exc
        if data.get("object") != "list":
            raise OracleGateError("Scryfall did not return card collection")
        if data.get("not_found"):
            raise OracleGateError("Unresolved source cards: " + json.dumps(data["not_found"]))
        rows = data.get("data")
        if not isinstance(rows, list) or len(rows) != len(chunk):
            raise OracleGateError("Scryfall returned incomplete card collection")
        for card in rows:
            key = card.get("name")
            if key not in chunk or key in response:
                raise OracleGateError("Unexpected/duplicate oracle card name: " + str(key))
            response[key] = card
    if set(response) != set(names):
        raise OracleGateError("Live Scryfall lookup omitted source identities")
    return response


def text_and_faces(card):
    if isinstance(card.get("oracle_text"), str):
        return card["oracle_text"]
    faces = card.get("card_faces")
    if not isinstance(faces, list) or not faces:
        raise OracleGateError("No Oracle text or faces: " + card.get("name", "unknown"))
    parts = [face.get("oracle_text", "") for face in faces]
    if not all(isinstance(x, str) for x in parts):
        raise OracleGateError("Malformed Oracle face text")
    return "\n//\n".join(parts)


def assess(cards, all_lists):
    """Validate current legality, color identity and text of *every* named card."""
    evidence = {}
    for name in sorted(cards):
        card = cards[name]
        if card.get("object") != "card":
            raise OracleGateError("Non-card object: " + name)
        legality = card.get("legalities", {}).get("commander")
        if legality != "legal":
            raise OracleGateError("Current Commander legality %s: %s" % (name, legality))
        colors = card.get("color_identity")
        if not isinstance(colors, list) or not set(colors) <= ALLOWED:
            raise OracleGateError("Illegal Grixis color identity for " + name + ": " + str(colors))
        # Scryfall's collection resolves a *printing*, sometimes digital-only
        # (e.g. VMA Badlands) for an otherwise paper-printed, legal card name.
        # Do not conflate chosen printing.games with card-name legality; our
        # pinned source supplies separate paper-printing provenance.
        # Scryfall /cards/collection can now resolve a not-yet-game-enabled
        # printing (games=[]) for an already paper-released card name, e.g.
        # Arcane Signet TRC/485 on 2026-10-26. The pinned independent
        # paper-source provenance and official Commander legality are checked
        # separately; requiring a nonempty printing.games is invalid here.
        if not isinstance(card.get("games"), list):
            raise OracleGateError("Malformed Scryfall printing games field: " + name)
        if not card.get("oracle_id") or not card.get("scryfall_uri"):
            raise OracleGateError("Card provenance missing: " + name)
        oracle_text = text_and_faces(card)
        evidence[name] = {
            "oracle_id": card["oracle_id"],
            "card_id": card.get("id"),
            "scryfall_uri": card["scryfall_uri"],
            "mana_value": card.get("cmc"),
            "mana_cost": card.get("mana_cost", ""),
            "color_identity": sorted(colors),
            "commander_legality": legality,
            "selected_printing_games": card["games"],
            "oracle_text": oracle_text,
            "oracle_text_sha256": sha256_bytes(oracle_text.encode("utf-8")),
            "layout": card.get("layout"),
            "released_at_sample_printing": card.get("released_at"),
        }
    expected_mv = {
        "The Lost and the Damned": 3,
        "Call Forth the Tempest": 8,
        "Keeper of Secrets": 6,
        "The Ruinous Powers": 4,
        "Grinning Ignus": 3,
        "Chaos Warp": 3,
        "Aggravated Assault": 3,
        "Inevitable Betrayal": 0,
    }
    for name, mv in expected_mv.items():
        if evidence[name]["mana_value"] != mv:
            raise OracleGateError("2026-10-22 corrected mana value drift: " + name)
    if "Whenever you cast a spell from anywhere other than your hand" not in evidence["Keeper of Secrets"]["oracle_text"]:
        raise OracleGateError("Keeper trigger text diverged; hand analysis requires update")
    if "Cascade, cascade" not in evidence["Call Forth the Tempest"]["oracle_text"]:
        raise OracleGateError("Printed double cascade Oracle drift")
    for deck_name, card_names in all_lists.items():
        if len(card_names) != 100 or not set(card_names) <= set(evidence):
            raise OracleGateError("Incomplete full-list evidence: " + deck_name)
        bad = {n: count for n, count in Counter(card_names).items()
               if count > 1 and n not in BASIC}
        if bad:
            raise OracleGateError("Illicit source duplicates " + deck_name + ": " + str(bad))
    return evidence


def audit(*, fetch=get_json, sleeper=time.sleep):
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    # GitHub Actions' token cannot read the separate canonical repository.
    # Bind immutable connector-fetched exact bytes to the approved SHA in CI.
    # A separate current canonical live-state check is performed via GitHub
    # connector before integration; NEVER call this a live CI canonical read.
    canonical_raw = CANONICAL_SNAPSHOT.read_bytes()
    baseline, source_digest = source_reconcile(manifest, canonical_raw)
    variants = staged_variants(manifest, baseline)
    all_names = sorted({n for cards in variants.values() for n in cards})
    card_data = collected_cards(all_names, fetch=fetch, sleeper=sleeper)
    evidence = assess(card_data, variants)
    timestamp = datetime.now(timezone.utc).isoformat()
    receipts = {}
    for label, cards in variants.items():
        source_path = (manifest["baseline_source_path"] if label == "baseline" else
                       next(v["path"] for v in manifest["candidate_variants"] if v["id"] == label))
        raw = (ROOT / source_path).read_bytes()
        receipts[label] = {
            "source": source_path, "physical_sha256": sha256_bytes(raw),
            "card_count": len(cards), "distinct_names": len(set(cards)),
            "oracle_rows_covered": len(set(cards)), "checked": True,
            "commander": cards[0],
        }
    return {
        "schema_version": 1,
        "stage": "LIVE_SCRYFALL_ABADDON_100_CARD_ORACLE_LEGALITY_CHECK_NOT_M6_M7_CERT",
        "checked_at_utc": timestamp,
        "scryfall_endpoint": SCRYFALL,
        "canonical_repository_url": CANONICAL,
        "canonical_authority_mode": "SHA_PINNED_CANONICAL_BYTES_NOT_LIVE_CROSS_REPO_READ",
        "canonical_authority_snapshot_path": str(CANONICAL_SNAPSHOT.relative_to(ROOT)),
        "canonical_repository_head_at_snapshot": CANONICAL_SOURCE_MAIN_SHA_AT_SNAPSHOT,
        "approved_canonical_raw_sha256": source_digest,
        "locked_canonical_mutated": False,
        "reviewer_independent": False,
        "owner_m7_approval": False,
        "formal_m6_certificate": False,
        "official_commander_exceptions_for_abaddon": [],
        "card_identity_count": len(evidence),
        "physical_lists": receipts,
        "oracle_snapshot": evidence,
        "limitations": [
            "Scryfall queried live for each unique card identity; this is not a Wizards comprehensive-rules interaction execution.",
            "Canonical raw bytes were copied using the authorized GitHub connector and SHA-pinned; CI does not have direct live read access to canonical main.",
            "Oracle evidence and legality are current only as of checked_at_utc, not permanent assurances.",
            "Card choice/cut superiority, M6 tested-pool I, M6 J final bundle, M7 final candidate and owner approval remain separate.",
            "Scryfall default sample printing can be digital-only or have a future release date even when another printing of the name is already paper Commander-legal.",
            "Current Commander legality and color identity are checked by name, while historical exact-set paper printings remain grounded in the canonical approved Oct 12 audit; a live print-by-print paper release audit is not claimed.",
        ],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    report = audit()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
                        encoding="utf-8")
    print("LIVE_ORACLE_PASS", json.dumps({
        "checked_at_utc": report["checked_at_utc"],
        "unique_oracle_cards": report["card_identity_count"],
        "full_100_card_lists": len(report["physical_lists"]),
        "canonical_source_sha256": report["approved_canonical_raw_sha256"],
        "list_sha256": {k: x["physical_sha256"] for k, x in report["physical_lists"].items()},
        "source": SCRYFALL,
        "report_file": str(args.out),
        "approved_lists_modified": False,
        "m6_m7_approval_inferred": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
