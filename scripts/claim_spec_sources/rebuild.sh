#!/bin/bash
set -e
cd "${MV_ROOT:-$(dirname "$0")/../..}"
export MTG_SCRYFALL_MODE=multiverse SCRYFALL_OFFLINE=1
python3 scripts/story_claim_pipeline.py build | head -1 >/dev/null
python3 scripts/story_claim_pipeline.py check
for i in 1 2; do
 for s in build_card_name_anchors build_in_universe_dates build_multiverse_graph build_claim_card_anchors build_story_coverage_inventory; do python3 scripts/$s.py >/tmp/rb_$s.log 2>&1 || { echo "FAIL $s"; tail -5 /tmp/rb_$s.log; exit 1; }; done
done
for s in build_card_name_anchors build_in_universe_dates build_multiverse_graph build_claim_card_anchors build_story_coverage_inventory build_story_image_label_printings; do python3 scripts/$s.py --check >/tmp/rbc_$s.log 2>&1 && echo "ok $s" || { echo "CHECKFAIL $s"; tail -5 /tmp/rbc_$s.log; }; done
for f in /tmp/rb_build_multiverse_graph.log /tmp/rb_build_claim_card_anchors.log /tmp/rb_build_story_coverage_inventory.log; do tail -n 3 $f; done
