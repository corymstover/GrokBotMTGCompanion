#!/usr/bin/env bash
# Phase 8: guarded, lore/card-only enrichment. Historical Grixis generators
# intentionally do NOT run here: they can rewrite owner-approved artifacts.
# A no-argument invocation is read-only. Writes require an explicit --apply.
set -euo pipefail
cd "$(dirname "$0")/.."

usage() {
  printf '%s\n' \
    'Phase 8 enrichment: safe controls' \
    '  --plan   read-only status and exact write targets (default)' \
    '  --check  read-only enrichment consistency check' \
    '  --apply  rebuild ONLY card enrichment, card shards and EDH Packages on a clean feature branch' \
    '          Requires existing offline Scryfall, EDHREC, and Spellbook caches.' \
    '  --help   show this message'
}

mode="${1:---plan}"
if [ "$#" -gt 1 ]; then
  usage >&2
  exit 2
fi

case "$mode" in
  --help|-h) usage ;;
  --plan)
    usage
    printf '\n%s\n' 'NO WRITES: the old Grixis refinement, interaction and broad crossref steps are excluded.'
    python3 scripts/phase8_status.py
    ;;
  --check)
    python3 scripts/phase8_status.py
    python3 scripts/build_card_enrichment.py --check
    ;;
  --apply)
    if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
      printf '%s\n' 'Refusing: run from a Git worktree.' >&2
      exit 2
    fi
    branch="$(git branch --show-current)"
    if [ -z "$branch" ] || [ "$branch" = main ] || [ "$branch" = master ]; then
      printf '%s\n' 'Refusing: enrichment writes require a named feature branch (not main/master).' >&2
      exit 2
    fi
    if [ -n "$(git status --porcelain)" ]; then
      printf '%s\n' 'Refusing: commit or stash existing work before running the generator.' >&2
      exit 2
    fi
    if [ ! -f data/card_enrichment.json ] || [ ! -f 'Card Enrichment.md' ]; then
      printf '%s\n' 'Refusing: existing enrichment baseline is missing.' >&2
      exit 2
    fi
    cache_dir='.cache'
    if [ "${MTG_SCRYFALL_MODE:-}" = multiverse ]; then
      cache_dir="${MTG_MULTIVERSE_CACHE:-.cache/multiverse}"
      if [ ! -f "$cache_dir/manifest.json" ] ||
         ! python3 scripts/scryfall_snapshot.py verify --dir "$cache_dir"; then
        printf '%s\n' 'Refusing: modern Scryfall snapshot is not manifest-verified.' >&2
        exit 2
      fi
    fi
    if ! compgen -G "$cache_dir/default-cards-*.jsonl.gz" >/dev/null ||
       [ ! -d .cache/edhrec ] || [ ! -d .cache/spellbook ]; then
      printf '%s\n' 'Refusing: offline Scryfall/EDHREC/Spellbook caches are incomplete.' >&2
      printf '%s\n' 'Recover or refresh caches on the feature branch before generating a new slice.' >&2
      exit 2
    fi
    # Without the verified official story cache a rebuild silently erases
    # previously confirmed lore/backstory links. A read-only comparison on
    # 2026-10-29 would have changed hundreds of existing entries this way.
    if [ ! -d .cache/story/text22 ]; then
      printf '%s\n' 'Refusing: official Wizards story cache is absent.' >&2
      exit 2
    fi
    if ! python3 scripts/story_cache_audit.py --strict; then
      printf '%s\n' 'Refusing: official Wizards source inventory failed strict integrity checks.' >&2
      exit 2
    fi
    export SCRYFALL_OFFLINE=1
    printf '%s\n' 'Rebuilding card enrichment and EDH Packages only; NO Grixis generators.'
    # Newly enriched cards can refer to package sections before the package
    # generator has had a chance to create their reciprocal backlinks.
    # Defer only those transient errors; the final generation/check enforce all.
    python3 scripts/build_card_enrichment.py --defer-package-backlinks
    python3 scripts/build_packages.py --enrichment-backlinks-only
    python3 scripts/build_card_enrichment.py
    python3 scripts/build_card_enrichment.py --check
    python3 scripts/phase8_status.py
    if git diff --name-only -- grixis data/grixis exports/grixis-archidekt decks/grixis | grep -q .; then
      printf '%s\n' 'STOP: protected Grixis paths changed unexpectedly; do not publish this branch.' >&2
      exit 2
    fi
    printf '%s\n' 'Phase 8 card/package pass complete. Review the diff and run full CI before merging.'
    ;;
  *)
    usage >&2
    exit 2
    ;;
esac
