#!/usr/bin/env python3
"""Classify Birthday-snapshot impact before any fresh M5 regeneration.

This is a conservative dependency audit, not an optimizer.  It compares the fresh
Birthday authority/evidence bundle with the frozen snap-20261016 M5 corpus and says
which deck-level artifacts actually need refresh.  It never mutates frozen A-F/M5,
never decides a swap, and never approves/locks a deck.

Inputs are committed artifacts only; raw fresh Scryfall is represented by the
hash-bound semantic delta written by grixis_birthday_snapshot.py.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import grixis_authority as ga  # noqa: E402
import grixis_evidence as ge  # noqa: E402

VERSION = 1
AUTH = ROOT / "data/grixis/birthday_authority"
MANIFEST = AUTH / "manifest.json"
DELTA = AUTH / "delta_vs_snap-20261016.json"
FRESH_EDH = AUTH / "edhrec_current.json.gz"
FRESH_TOUR = AUTH / "tournament"
OLD_TOUR = ROOT / "data/grixis/candidates/tournament"
FROZEN_M5 = ROOT / "data/grixis/m5_regen/candidates"
OUT = ROOT / "data/grixis/birthday_m5/impact.json"


def hfile(p: Path) -> str:
    return "sha256:" + hashlib.sha256(p.read_bytes()).hexdigest()


def read_m5(slug: str):
    p = FROZEN_M5 / f"{slug}.json.gz"
    return json.loads(gzip.decompress(p.read_bytes()).decode("utf-8"))


def deck_names(slug: str):
    out = set()
    for line in ga.deck_block_text(slug).splitlines():
        m = re.match(r"^\s*(\d+)x?\s+(.+?)(?:\s+\[[^]]+\])?\s*$", line)
        if m:
            out.add(m.group(2).strip())
    return out


def fresh_edhrec():
    d = json.loads(gzip.decompress(FRESH_EDH.read_bytes()).decode("utf-8"))
    out = {}
    for slug, rec in d.get("decks", {}).items():
        pages = rec.get("pages", [])
        by = {}
        for page in pages:
            for n, v in page.get("rows", {}).items():
                if v.get("synergy") is None or not v.get("potential_decks"):
                    continue
                by.setdefault(n, []).append(v)
        method = "pooled" if len(pages) > 1 else "single_page"
        out[slug] = {n: ge.edh_row(vs, method) for n, vs in by.items()}
    return out


def old_edhrec(slug: str):
    d = json.loads((ROOT / f"data/grixis/evidence/{slug}.json").read_text(encoding="utf-8"))
    return {x["card"]: x.get("edhrec") for x in d.get("vectors", []) if x.get("edhrec") is not None}


def edh_changed(a, b):
    """Material for M5 input identity means any stored field changed, not a judgment threshold."""
    return a != b


def tournament_delta(slug: str):
    a = OLD_TOUR / f"{slug}.json"
    b = FRESH_TOUR / f"{slug}.json"
    if not a.exists() and not b.exists():
        return None
    if not a.exists() or not b.exists():
        return {"changed": True, "reason": "file_added_or_removed", "old": a.exists(), "fresh": b.exists()}
    old = json.loads(a.read_text(encoding="utf-8")); new = json.loads(b.read_text(encoding="utf-8"))
    keys = ("status", "sample_size", "window", "commander", "cards")
    changed = [k for k in keys if old.get(k) != new.get(k)]
    return {"changed": bool(changed), "fields": changed,
            "old_sample_size": old.get("sample_size"), "fresh_sample_size": new.get("sample_size")}


def build():
    for p in (MANIFEST, DELTA, FRESH_EDH):
        if not p.exists():
            raise SystemExit(f"missing fresh Birthday input: {p.relative_to(ROOT)}")
    man = json.loads(MANIFEST.read_text(encoding="utf-8"))
    delta = json.loads(DELTA.read_text(encoding="utf-8"))
    if man.get("status") != "ready" or man.get("hard_blockers"):
        raise SystemExit(f"Birthday authority snapshot is not ready: {man.get('hard_blockers')}")
    if delta.get("baseline") != "snap-20261016":
        raise SystemExit(f"wrong M5 delta baseline: {delta.get('baseline')}")

    oracle = delta["scryfall_oracle"]
    changed_oracle = {x["name"] for x in oracle.get("changed", []) if x.get("name")}
    removed_oracle = {x.get("name") for x in oracle.get("removed", []) if x.get("name")}
    added_rows = oracle.get("added", [])
    added_eligible = {x.get("name") for x in added_rows
                      if x.get("name") and x.get("commander_legality") == "legal"
                      and set(x.get("color_identity") or []) <= {"U", "B", "R"}
                      and "Basic Land" not in (x.get("type_line") or "")}
    legality_names = {x["name"] for x in oracle.get("commander_legality_changes", []) if x.get("name")}
    ruling_names = {x.get("name") for x in delta.get("scryfall_rulings", {}).get("affected_cards", []) if x.get("name")}
    rules_changed = bool(delta.get("comprehensive_rules", {}).get("changed_vs_frozen"))
    spell = delta.get("commander_spellbook", {}).get("decks", {})
    fresh_edh = fresh_edhrec()

    rows = []
    summary = {k: 0 for k in ("no_change", "evidence_refresh", "candidate_refresh", "structural_refresh", "blocked")}
    for did, v in sorted(ga.summary().items(), key=lambda kv: kv[1]["slug"]):
        slug = v["slug"]; rid = ga.registry_id(did)
        m5 = read_m5(slug)
        canon = deck_names(slug)
        cand = {x["card"] for x in m5.get("candidates", [])}
        relevant = canon | cand

        canonical_oracle = sorted(canon & (changed_oracle | removed_oracle | legality_names))
        canonical_rulings = sorted(canon & ruling_names)
        candidate_oracle = sorted(cand & (changed_oracle | removed_oracle | legality_names))
        current_legality = man["canonical_deck_legality"]["decks"].get(slug, {})
        blocked = current_legality.get("status") == "blocked"

        oe = old_edhrec(slug); ne = fresh_edh.get(slug, {})
        edh_names = sorted(n for n in relevant | set(ne) | set(oe) if edh_changed(oe.get(n), ne.get(n)))
        # Distinguish changes that can alter M5 comparisons/scores from irrelevant page churn.
        edh_m5 = sorted(set(edh_names) & relevant)
        sp = spell.get(slug, {})
        sp_changed = bool(sp.get("added_variant_ids") or sp.get("removed_variant_ids"))
        td = tournament_delta(slug)
        tour_changed = bool(td and td.get("changed"))

        structural_reasons = []
        if rules_changed:
            structural_reasons.append("comprehensive_rules_hash_changed")
        if canonical_oracle:
            structural_reasons.append("canonical_oracle_or_legality_changed")
        if canonical_rulings:
            structural_reasons.append("canonical_rulings_changed")
        candidate_reasons = []
        if added_eligible:
            candidate_reasons.append("new_eligible_oracle_cards")
        if candidate_oracle:
            candidate_reasons.append("existing_candidate_oracle_or_legality_changed")
        if sp_changed:
            candidate_reasons.append("spellbook_near_miss_changed")
        if edh_m5:
            candidate_reasons.append("edhrec_m5_inputs_changed")
        evidence_reasons = []
        if tour_changed:
            evidence_reasons.append("tournament_evidence_changed")

        if blocked:
            status = "blocked"
        elif structural_reasons:
            status = "structural_refresh"
        elif candidate_reasons:
            status = "candidate_refresh"
        elif evidence_reasons:
            status = "evidence_refresh"
        else:
            status = "no_change"
        summary[status] += 1
        rows.append({
            "deck_id": rid, "slug": slug, "canonical_hash": m5.get("list_hash") or m5.get("canonical_hash"),
            "status": status,
            "structural_reasons": structural_reasons,
            "candidate_reasons": candidate_reasons,
            "evidence_reasons": evidence_reasons,
            "canonical_oracle_or_legality_cards": canonical_oracle,
            "canonical_ruling_cards": canonical_rulings,
            "candidate_oracle_or_legality_cards": candidate_oracle,
            "new_eligible_pool_cards_global": sorted(added_eligible),
            "edhrec_changed_m5_names": edh_m5,
            "edhrec_changed_m5_count": len(edh_m5),
            "spellbook_delta": sp,
            "tournament_delta": td,
            "fresh_legality_status": current_legality.get("status"),
            "authorized_nonlegal": current_legality.get("authorized_nonlegal", []),
        })

    doc = {
        "schema_version": 1, "kind": "birthday_m5_impact", "generated_by": f"scripts/grixis_birthday_m5_impact.py v{VERSION}",
        "birthday_snapshot": man["snapshot_id"], "frozen_m5_baseline": "snap-20261016",
        "frozen_m5_summary_sha256": hfile(ROOT / "data/grixis/m5_regen/summary.json"),
        "birthday_manifest_sha256": hfile(MANIFEST), "birthday_delta_sha256": hfile(DELTA),
        "authority": {"can_decide": False, "can_approve_or_lock": False,
                      "note": "Dependency/refresh classification only. It cannot choose a swap or accept M5."},
        "global": {"rules_changed": rules_changed, "new_eligible_pool_cards": sorted(added_eligible),
                   "oracle_changed_names": len(changed_oracle), "ruling_affected_names": len(ruling_names),
                   "commander_legality_changes": len(legality_names)},
        "summary": summary, "decks": rows,
        "refresh_policy": {
            "blocked": "resolve authority/legality blocker before M5 delta",
            "structural_refresh": "regenerate affected structural A-F evidence before fresh M5 delta; never reuse stale canonical semantics",
            "candidate_refresh": "regenerate current candidate screening/triage and affected challenger tests while preserving frozen corpus",
            "evidence_refresh": "refresh non-deciding review evidence; do not reopen structural A-F solely for observational metric movement",
            "no_change": "hash-bind frozen M5 result into fresh delta as unchanged; do not rewrite it"
        },
        "limitations": [
            "Exact historical EDHREC raw pages are unavailable; the old side uses the committed 2026-10-16 M3 derivative vectors.",
            "An EDHREC metric difference is an input-identity change, not evidence that a card became strategically better or worse.",
            "New current cards are candidate-pool inputs only; this audit does not promote them or decide a swap.",
        ],
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(doc, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"snapshot": doc["birthday_snapshot"], "summary": summary, "global": doc["global"]}, indent=2))
    return 0


def check():
    p = []
    if not OUT.exists():
        p.append("impact artifact missing")
    else:
        d = json.loads(OUT.read_text(encoding="utf-8"))
        if d.get("frozen_m5_baseline") != "snap-20261016": p.append("wrong frozen M5 baseline")
        if len(d.get("decks", [])) != 62: p.append(f"coverage {len(d.get('decks', []))}/62")
        if sum((d.get("summary") or {}).values()) != 62: p.append("summary does not total 62")
        if d.get("authority", {}).get("can_decide") is not False: p.append("impact audit became decision-capable")
        if d.get("authority", {}).get("can_approve_or_lock") is not False: p.append("impact audit became approval-capable")
        for r in d.get("decks", []):
            if r.get("status") not in {"no_change", "evidence_refresh", "candidate_refresh", "structural_refresh", "blocked"}:
                p.append(f"{r.get('slug')}: invalid status")
            if r.get("status") == "blocked" and r.get("fresh_legality_status") != "blocked":
                p.append(f"{r.get('slug')}: blocked without fresh legality blocker")
    print(f"birthday-m5-impact: {'PASS' if not p else 'FAIL'}; {len(p)} problem(s)")
    for x in p: print("  -", x)
    return 1 if p else 0


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--build", action="store_true"); ap.add_argument("--check", action="store_true")
    a = ap.parse_args();
    if not a.build and not a.check: ap.error("choose --build or --check")
    rc = build() if a.build else 0
    if a.check: rc = max(rc, check())
    return rc

if __name__ == "__main__":
    raise SystemExit(main())
