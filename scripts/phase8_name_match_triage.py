#!/usr/bin/env python3
"""Read-only official-page triage of unconfirmed Phase 8 name matches.

This is a candidate-discovery tool, NOT a canon confirmation or a generator.
It uses the committed enrichment artifact and audited Wizards text cache; no
locked Scryfall bulk, EDHREC or Spellbook cache is needed. It intentionally
omits print-specific flavor/art evidence until those snapshots are available.

  python3 scripts/phase8_name_match_triage.py --json
  python3 scripts/phase8_name_match_triage.py --output /tmp/phase8-triage.json
"""
import argparse
import hashlib
import json
from pathlib import Path

import build_card_enrichment as B
import story_cache_audit as A


ROOT = Path(__file__).resolve().parent.parent
ENRICHED = ROOT / "data" / "card_enrichment.json"
MANIFEST = ROOT / "data" / "story_cache_provenance_2026-10-29.json"


def triage(data, stories, norm):
    pending = []
    candidates = []
    for card in data["cards"].values():
        for relation in card["lore"]["relations"]:
            if relation["relation"] != "name-match":
                continue
            pending.append((card["name"], relation["entry"]))
            # The absent printing metadata is deliberately represented by empty
            # values: this pass can offer official-page/heading leads only.
            result = B.audit_name_match(
                relation, {"name": card["name"]},
                {"name": relation["name"], "text": ""},
                {"flavors": [], "artists": set(), "spotlight": [], "sets": [], "set_types": set()},
                {}, stories, norm)
            evidence = result.get("confirmed")
            if evidence and evidence["by"] in ("page", "legends"):
                candidates.append({"card": card["name"], "character": relation["name"],
                                   "entry": relation["entry"], "evidence_type": evidence["by"],
                                   "source_url": evidence["source"]})
    return {"schema": "phase8-name-match-triage/v1",
            "evidence_is_canon_approval": False,
            "pending_links_examined": len(pending),
            "official_page_candidates": len(candidates),
            "links_without_new_page_candidate": len(pending) - len(candidates),
            "candidates": sorted(candidates, key=lambda x: (x["card"], x["entry"])),
            "limitations": [
                "Official-page co-occurrence is a review lead, not independent proof of a card depiction.",
                "No printing-specific art, flavor, or Story Spotlight checks: frozen Scryfall bulk is unavailable.",
                "Existing approved cards and lore classifications are unchanged."]}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    audit = A.audit(A.inventory())
    if audit["counts"] != {"present": 660} or audit["colliding_cache_paths"]:
        parser.error("requires the complete 660-source strict-audited cache")
    data = json.loads(ENRICHED.read_text(encoding="utf-8"))
    stories, norm = B.story_norm()
    report = triage(data, stories, norm)
    report["official_sources_audited"] = audit["total"]
    report["source_manifest_sha256"] = hashlib.sha256(MANIFEST.read_bytes()).hexdigest()
    result = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(result, encoding="utf-8")
    if args.json:
        print(result, end="")
    else:
        print(f"Phase 8 name-match triage: {report['official_page_candidates']} candidates "
              f"of {report['pending_links_examined']} pending links; no approvals changed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
