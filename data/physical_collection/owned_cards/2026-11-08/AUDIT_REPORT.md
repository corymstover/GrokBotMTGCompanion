# Owned-card knowledge coverage audit — November 8, 2026

**Scope:** Every distinct name in Cory and Stefanie's November 8 physical master
inventory, whether currently free, in Xander, or in Dihada. The owner-confirmed
Xander rebuild was applied to the **availability counts only**, without changing
the Scryfall metadata snapshot. This is a *dated personal card-data overlay*; the protected
62-deck Encyclopedia and repository-wide pinned Scryfall data are unchanged.

## Verified coverage

| Measure | Finding |
| --- | ---: |
| Physical cards in master inventory | 1,332 |
| Distinct owned names audited | **751 / 751** |
| Currently free copies / distinct names | 1,131 / 621 |
| Reserved in the two surviving decks | 201 |
| Owned names already in the original card index | 663 |
| Names **missing from the original card index** | **88**, all covered here |
| Indexed names with detected single-face Oracle-text drift | **0** |
| Indexed names with detected type, color-identity, Oracle-ID, or Commander-status drift | **0** |
| Owned names marked Pauper legal by the source snapshot | **239** |
| Pauper-legal names currently unreserved | **216** |
| Names with no generally released printing by the snapshot date | **137** |

The 88 missing names are predominantly newer *Star Trek* cards. Their Scryfall
printing, face-specific Oracle rules text, mana costs, mana values, colors,
Commander color identity, type, keywords, legalities, rarity history, and
links to card-specific published rulings are now indexed locally. The other
663 names also receive a dated metadata and ownership overlay.

The original index's single-face Oracle text was cross-checked where parsable.
**A zero-drift result is not a claim that every multiface shard, erratum, rule
interaction, or specific physical printing was independently audited.**

## Sources, reproducibility, and scope

- Inventory: [`../../2026-11-08/master_inventory.csv`](../../2026-11-08/master_inventory.csv)
  and [`../../current_available.csv`](../../current_available.csv).
- Scryfall [default-cards bulk API](https://api.scryfall.com/bulk-data/default-cards)
  (`updated_at`: `2026-11-08T10:07:57.464+00:00`). We scanned **120,045**
  printing records from downloaded gzip `default-cards-20261108.jsonl.gz`
  with SHA-256 `5519302320a728699c66cdf4f79d2b4bd898e808531da83fe5aab2c683972682`.
  The **81 MB compressed bulk is not committed**; its provenance is recorded in
  [`manifest.json`](manifest.json), along with each owned shard's SHA-256.
- Records are in `part-001.json` to `part-038.json`. `manifest.json` maps
  exact card names to shards. Oracle, identity, legality, rarity and printing
  values remain source-pinned; physical `copies_available` and `copies_reserved`
  have been refreshed to match the owner-confirmed Xander rebuild.
- WotC [Pauper format reference](https://magic.wizards.com/en/formats/pauper)
  and [2026 format update](https://magic.wizards.com/en/news/announcements/on-the-zeta-set-in-pauper)
  govern format interpretation; Scryfall supplies this **dated** legality
  snapshot. WotC's [*Star Trek* collection details](https://magic.wizards.com/en/news/feature/collecting-star-trek)
  give November 13, 2026 as broad tabletop release.

## Important limitations and guardrails

1. **Do not identify an owned copy's rarity from the card's name.** The master
   CSV has no edition, collector number, foil, or other printing identifier.
   `representative_printing_rarity` means *the chosen Scryfall reference
   printing*, not Cory's copy. `all_recorded_rarities`,
   `regular_common_printings`, and `printings_by_rarity` provide evidence of
   set-specific rarities without making that claim.
2. **Pauper eligibility is not simply “one printing looks common.”** Use the
   dated `legalities.pauper` flag, check for any regular paper/MTGO common
   printing, and check current ban announcements when actually constructing a
   deck. We explicitly exclude memorabilia facsimiles and non-playable product
   cards from common-printing evidence. `Baleful Strix` is an example of
   Pauper-legal downshift; `Sol Ring` remains not Pauper legal.
3. **Prerelease is not broad constructed release.** The 137 names flagged
   `future_only` do not have a generally released printing by November 8;
   their current `not_legal` values cannot be extrapolated into permanent bans.
   Refresh their status after the applicable release. Sealed/prerelease play
   uses its event-specific Limited rules. In particular, *The Unicomplex* is
   reserved in Cory's current Xander deck, but on November 8 the dated source
   still marks that prerelease card `not_legal` in Commander; do not present
   the rebuilt deck as fully sanctioned-legal before the release-date update.
4. **The snapshot is not a full rules interaction proof.** Oracle text, faces,
   current keyword lists, and the official Scryfall `rulings_uri` are indexed.
   Older card shards may contain published rulings, but the newest 88 cards'
   current rulings are **linked, not fully cached**, and there is no exhaustive
   precomputed pairwise card-interaction/combo database. Check up-to-date
   [Comprehensive Rules](https://magic.wizards.com/en/rules) and the specific
   card rulings when a deck decision depends on timing, layers, or a combo.
5. **A dated snapshot stays dated.** Re-run the builder with a new verified
   bulk file and a new dated output path if the collection or card rules
   change; never silently claim this November 8 snapshot is current forever.

## Offline usage

From repository root, with no network connection:

```bash
python3 scripts/build_owned_card_knowledge.py check
python3 scripts/build_owned_card_knowledge.py refresh-availability  # only after physical pool changes
python3 scripts/audit_physical_collection.py --check
python3 scripts/owned_cards.py stats
python3 scripts/owned_cards.py card 'Tenacious Drone'
python3 scripts/owned_cards.py card 'Baleful Strix' --json
python3 scripts/owned_cards.py pauper --available --colors WB --type Creature --limit 30
python3 scripts/owned_cards.py find 'create a token' --available --limit 40
python3 scripts/mv_ask.py card 'The Unicomplex'
python3 scripts/mv_ask.py card 'Baleful Strix' --owned
python3 -m unittest discover -s tests -p 'test_owned_cards.py' -v
```

**Rebuild:** Download the exact Scryfall `default-cards` bulk archive (or use a
new dated bulk when making a new snapshot). For this exact snapshot, invoke:

```bash
python3 scripts/build_owned_card_knowledge.py build \
  --bulk /path/to/default-cards-20261108.jsonl.gz \
  --updated-at '2026-11-08T10:07:57.464+00:00' \
  --as-of 2026-11-08
```

The builder refuses missing owned card names, mismatched ownership totals,
unknown structural identity, or incomplete generated shards. Existing main
Q&A lookups preserve their historical canonical-index responses by default,
which maintains byte-for-byte pinned acceptance evidence. Explicit
`card <name> --owned` requests append the newer personal overlay. Cards absent
from the original index fall back to the dated owned catalogue by default,
with a clearly qualified confidence label.
