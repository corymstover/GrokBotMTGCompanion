#!/usr/bin/env python3
"""M6 I/J input provenance receipts. Never a decision or certification gate.

Receipt scope is SHA-256 attestation of accepted M5 inputs and current triage
artifacts, not reproduction of a game, an approved swap, or a global optimum.
The eventual Phase-B/strategic-judgment/reproducibility bundle is a separate gate.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import grixis_authority as ga  # noqa: E402

SCHEMA = ROOT / "data/grixis/schemas/m6_input_receipt.schema.json"
REGISTRY = ROOT / "data/grixis/registry.json"
SUMMARY = ROOT / "data/grixis/birthday_m5/summary.json"
OUT = ROOT / "data/grixis/m6/ij/input_receipts"
CORPUS_COMMIT = "fcd28daff7d3f7b091de04299699645ba7e47aa2"
SUMMARY_SHA256 = "sha256:dfa23cab773832927eb0a0877f8b425581efe1b2e51dcd32b90c53a66d549046"
REQUIRED_NEXT = [
    "sealed_independent_A_B_commits",
    "pass_C_critique",
    "phase_B_validated_evidence",
    "judgment_review",
    "final_receipt_bundle",
    "tested_pool_local_optimum_certificate",
]
ROLES = [
    ("candidate_pool", "data/grixis/birthday_m5/candidates/{slug}.json.gz"),
    ("regeneration", "data/grixis/birthday_m5/regen/{slug}.json.gz"),
    ("birthday_evidence", "data/grixis/birthday_m5/evidence/{slug}.json"),
    ("optimizer", "data/grixis/m6/optimizer/{slug}.json"),
    ("review_packet", "data/grixis/m6/review_packets/{slug}.json"),
]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for buf in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(buf)
    return "sha256:" + h.hexdigest()


def assert_frozen_source(rel: str, path: Path) -> None:
    """A receipt may not silently re-attest mutated files as the accepted M5 corpus."""
    original = subprocess.check_output(
        ["git", "rev-parse", f"{CORPUS_COMMIT}:{rel}"], cwd=ROOT, text=True
    ).strip()
    current = subprocess.check_output(
        ["git", "hash-object", str(path)], cwd=ROOT, text=True
    ).strip()
    if original != current:
        raise ValueError(f"accepted Birthday M5 source changed since {CORPUS_COMMIT}: {rel}")


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def dump(obj) -> str:
    return json.dumps(obj, indent=1, ensure_ascii=False, sort_keys=True) + "\n"


def context():
    reg = load(REGISTRY)
    m5 = reg["program"]["milestones"]["M5"]
    if m5.get("status") != "accepted" or m5.get("accepted_by") != "corymstover":
        raise ValueError("M5 acceptance not verified; cannot create I/J receipts")
    if CORPUS_COMMIT not in m5.get("acceptance_evidence", ""):
        raise ValueError("accepted source corpus commit drift")
    summary = load(SUMMARY)
    assert_frozen_source("data/grixis/birthday_m5/summary.json", SUMMARY)
    if sha256(SUMMARY) != SUMMARY_SHA256 or SUMMARY_SHA256 not in m5.get("acceptance_evidence", ""):
        raise ValueError("accepted Birthday M5 summary SHA-256 no longer matches acceptance")
    if len(summary.get("decks", [])) != 62:
        raise ValueError("M5 summary coverage must be 62")
    if summary["authority"].get("accepted_by_cory") is not False:
        raise ValueError("generated M5 evidence cannot self-accept")
    if len(reg["decks"]) != 62:
        raise ValueError("registry inventory not 62")
    by_slug = {d["slug"]: d for d in reg["decks"].values()}
    if len(by_slug) != 62:
        raise ValueError("registry duplicate slugs")
    return m5, summary, by_slug


def record(row, entry, m5, summary):
    slug = row["slug"]
    if row["canonical_hash"] != entry["current_canonical_hash"]:
        raise ValueError(f"{slug}: stale canonical hash in M5 summary")
    paths = []
    for role, template in ROLES:
        rel = template.format(slug=slug)
        p = ROOT / rel
        if not p.is_file():
            raise ValueError(f"{slug}: missing input {rel}")
        if role in ("candidate_pool", "regeneration", "birthday_evidence"):
            assert_frozen_source(rel, p)
        paths.append({"role": role, "path": rel, "sha256": sha256(p), "bytes": p.stat().st_size})
    with gzip.open(ROOT / ROLES[1][1].format(slug=slug), "rt", encoding="utf-8") as f:
        regen = json.load(f)
    if regen.get("list_hash") != row["canonical_hash"] or regen.get("deck_id") != entry["deck_id"]:
        raise ValueError(f"{slug}: M5 regen identity/hash mismatch")
    opt = load(ROOT / ROLES[3][1].format(slug=slug))
    packet = load(ROOT / ROLES[4][1].format(slug=slug))
    for label, obj in (("optimizer", opt["pass_a"]), ("packet", packet)):
        if obj["list_hash"] != row["canonical_hash"]:
            raise ValueError(f"{slug}: {label} hash mismatch")
    if packet["authority"]["can_approve_or_lock"] or packet["authority"]["can_decide"]:
        raise ValueError(f"{slug}: triage packet illegally decision-capable")
    return {
        "schema_version": 1,
        "stage": "M6_IJ_input_receipt",
        "deck_id": entry["deck_id"],
        "slug": slug,
        "list_hash": row["canonical_hash"],
        "birthday_snapshot": summary["birthday_authority_snapshot"],
        "accepted_at": m5["accepted_at"],
        "source_corpus_commit": CORPUS_COMMIT,
        "generator_sha256": sha256(Path(__file__)),
        "schema_sha256": sha256(SCHEMA),
        "inputs": paths,
        "reproduction": {
            "check_command": "python scripts/grixis_m6_ij.py --check",
            "scope": "Bytes, SHA-256, acceptance identity, deck hashes, schemas and authority invariants; not gameplay reproduction.",
            "phase_b_replayed": False,
            "positive_simulator_verdicts_decisive": False,
        },
        "status": "inputs_attested_downstream_incomplete",
        "required_next": REQUIRED_NEXT,
        "authority": {"can_apply_swap": False, "can_decide": False, "can_approve_or_lock": False},
    }


def validate_receipt(receipt):
    errs = ga.validate_file(receipt, "m6_input_receipt.schema.json")
    if errs:
        raise ValueError("receipt schema violation: " + "; ".join(errs[:8]))
    roles = [r["role"] for r in receipt["inputs"]]
    if roles != [x[0] for x in ROLES]:
        raise ValueError("receipt missing or duplicated roles")
    if set(receipt["required_next"]) != set(REQUIRED_NEXT):
        raise ValueError("required downstream obligations modified")
    if receipt["generator_sha256"] != sha256(Path(__file__)) or receipt["schema_sha256"] != sha256(SCHEMA):
        raise ValueError("receipt generator/schema hash drift")
    for row in receipt["inputs"]:
        p = ROOT / row["path"]
        if not p.is_file() or sha256(p) != row["sha256"] or p.stat().st_size != row["bytes"]:
            raise ValueError("receipt input missing/mutated: " + row["path"])
    return True


def run(build: bool, check: bool):
    m5, summary, by_slug = context()
    seen = set()
    if build:
        OUT.mkdir(parents=True, exist_ok=True)
    for row in summary["decks"]:
        slug = row["slug"]
        if slug in seen or slug not in by_slug:
            raise ValueError("duplicate/unknown M5 deck " + str(slug))
        seen.add(slug)
        expected = record(row, by_slug[slug], m5, summary)
        validate_receipt(expected)
        p = OUT / (slug + ".json")
        if build:
            p.write_text(dump(expected), encoding="utf-8")
        if check:
            if not p.exists() or p.read_text(encoding="utf-8") != dump(expected):
                raise ValueError(f"{slug}: missing or stale I/J receipt")
            validate_receipt(load(p))
    if seen != set(by_slug) or len(seen) != 62:
        raise ValueError("incomplete 62-deck coverage")
    if check and {p.stem for p in OUT.glob("*.json")} != seen:
        raise ValueError("unexpected/missing I/J receipt file")
    print(f"M6 I/J input receipts {'built' if build else 'checked'}: {len(seen)}/62; no decisions or Phase-B claims")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--build", action="store_true")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    if not (args.build or args.check):
        ap.error("require --build or --check")
    run(args.build, args.check)
