#!/usr/bin/env python3
"""Read-only Phase 1B audit entry point replacing dated per-family Actions.

The source-specific audit modules remain separately usable and source-grading
rules stay intact. This runner only consolidates their existing read-only CI
invocations; it deliberately never passes --write or --fetch-write.
"""
import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CHECKS = (
    ("audit_apac_lunar_year_promos_sources.py",),
    ("audit_art_series_primary_sources.py",),
    ("audit_boxed_precon_sources.py",),
    ("audit_boxed_special_lair_global_sources.py",),
    ("audit_boxed_specialty_sources.py",),
    ("audit_commander_modern_sources.py",),
    ("audit_commander_series_sources.py",),
    ("audit_commander_set_linked_sources.py",),
    ("audit_set_cross_category.py",),
    ("audit_draft_starter_batch2.py",),
    ("audit_draft_starter_sources.py",),
    ("audit_duel_decks_sources.py",),
    ("audit_event_collab_promos_sources.py",),
    ("audit_phase1b_fasttrack.py",),
    ("audit_phase1b_export_acceptance.py",),
    ("audit_historical_promo_series_sources.py",),
    ("publish_historical_set_index.py",),
    ("audit_inserts_clash_spellbook_sources.py",),
    ("audit_masterpiece_memorabilia_sources.py",),
    ("audit_product_family_triage.py",),
    ("audit_phase1b_functional_release.py",),
    ("audit_phase1b_release_scope.py",),
    ("audit_reprint_curated_sources.py",),
    ("audit_set_product_links.py", "--check"),
    ("audit_token_families_primary_sources.py",),
    ("audit_wotc_early_sets.py",),
    ("audit_wotc_mid_sets.py",),
    ("audit_wotc_premier_sets.py",),
    ("product_family_lookup.py", "--summary"),
)


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--check", action="store_true", help="run every registered read-only source audit")
    args = p.parse_args(argv)
    names = [x[0] for x in CHECKS]
    if len(names) != len(set(names)) or any(not (ROOT / "scripts" / n).is_file() for n in names):
        raise SystemExit("duplicate or missing Phase 1B CI script")
    if any("write" in arg or "fetch" in arg for entry in CHECKS for arg in entry[1:]):
        raise SystemExit("mutating Phase 1B argument forbidden")
    if not args.check:
        print(f"Phase 1B: {len(CHECKS)} read-only audit commands registered; use --check to run")
        return 0
    failures = []
    for entry in CHECKS:
        cmd = [sys.executable, str(ROOT / "scripts" / entry[0]), *entry[1:]]
        result = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, timeout=120)
        if result.returncode:
            failures.append((entry[0], result.returncode, (result.stdout + result.stderr)[-1600:]))
        else:
            print(f"PASS {entry[0]}")
    for name, rc, details in failures:
        print(f"FAIL {name} ({rc}): {details}", file=sys.stderr)
    print(f"Phase 1B family read-only audit: {len(CHECKS)-len(failures)}/{len(CHECKS)} PASS")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
