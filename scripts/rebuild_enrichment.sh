#!/usr/bin/env bash
# Bot cycle 35: the Phase 8 regeneration chain in dependency order (each generator writes atomically).
# Card enrichment reads the CHARCARDS tables (crossrefs) and EDH Packages; packages read the enrichment back-links.
set -euo pipefail
cd "$(dirname "$0")/.."
export SCRYFALL_OFFLINE=1
step() { echo "== $*"; "$@"; }
step python3 scripts/grixis_refine.py   # Bot cycle 39: Refined-list blocks, metrics, Archidekt exports
step python3 scripts/build_crossrefs.py >/dev/null
python3 scripts/build_card_enrichment.py | head -1 || true   # package back-link problems are expected until packages run
step python3 scripts/build_packages.py
step python3 scripts/build_card_enrichment.py
step python3 scripts/build_lore_index.py
step python3 scripts/front_matter.py
step python3 scripts/build_crossrefs.py
step python3 scripts/front_matter.py
step python3 scripts/build_card_enrichment.py
step python3 scripts/build_lore_xrefs.py
step python3 scripts/kb_find.py --build
step python3 scripts/lore_quotes.py --build
step python3 scripts/validate_all.py
echo REBUILD_OK
