#!/usr/bin/env python3
"""Retrieve the four *curator-assigned* lore grades from frozen Phase 6 pilots.

    python3 scripts/lore_deck_candidates.py --stem ugin_bolas_elder_dragon_duality --grade DIRECT_DEPICTION

This is an indexed, reviewed-candidate pool, NOT an automatic assertion that
arbitrary Scryfall flavor matches are canon depictions. Provenance stays with
the exact printed edition and cited source. Drafts remain UNAPPROVED.
"""
import argparse
import json
import re
from pathlib import Path

import audit_lore_pilot as audit

ROOT = Path(__file__).resolve().parents[1]


def retrieve(stem: str, grade: str | None = None, name: str = "") -> dict:
    if not re.fullmatch(r"[a-z0-9_]+", stem):
        raise ValueError("invalid pilot stem")
    specs = {json.loads(path.read_text(encoding="utf-8"))["stem"]: path
             for path in sorted(audit.SPECS.glob("*.json"))}
    if stem not in specs:
        raise ValueError("unknown, unreviewed pilot stem")
    if grade is not None and grade not in audit.TIERS:
        raise ValueError("unknown lore grade")
    audited = audit.audit(specs[stem])
    spec = json.loads(specs[stem].read_text(encoding="utf-8"))
    evidence = json.loads(audit.files(spec)["printing_evidence.json"].read_text(encoding="utf-8"))
    if audited["status"] != spec["status"] or audited["total"] != 100:
        raise ValueError("unapproved pilot evidence failed audit")
    rows = [{"card": c["name"], "grade": c["tier"], "beat": c["beat"],
             "why": c["why"], "source": c["source"], "source_id": c["source_id"],
             "printing_id": c["printing"]["id"], "oracle_id": c["printing"]["oracle_id"],
             "set": c["printing"]["set"], "collector_number": c["printing"]["collector_number"]}
            for c in evidence["cards"] if (grade is None or c["tier"] == grade)
            and (not name or name.casefold() in c["name"].casefold())]
    return {"schema": "lore-deck-curated-candidates/v1", "theme": spec["theme"], "stem": stem,
            "status": spec["status"], "as_of_snapshot": audited["snapshot"],
            "filters": {"grade": grade, "card_name_contains": name}, "count": len(rows),
            "cards": rows, "grade_policy": "Curator-assigned, source-cited exact-printing grades from an offline audited pilot; not arbitrary text inference",
            "limits": ["The three committed pilots are not approved or locked.",
                       "Lore-inspired and mechanical tiers are explicitly not canon depictions.",
                       "New themes require independent source grading, not an automatic grade promotion."]}


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--stem", required=True)
    p.add_argument("--grade", choices=audit.TIERS)
    p.add_argument("--name-contains", default="")
    args = p.parse_args(argv)
    try:
        result = retrieve(args.stem, args.grade, args.name_contains)
    except (ValueError, KeyError, FileNotFoundError) as exc:
        p.error(str(exc))
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
