# Four official-source entity-gap repairs — 2026-11-01

## Verified source claims

The November 1 source-graded entity census exposed four and only four
registered Plane/Place/Faction/Object/Character graph nodes with **no direct
cited claim**. This repair addresses all four within existing Phase 5 packs:

| Claim | Registered node | Conservative claim | Official Wizards source |
| --- | --- | --- | --- |
| `EL012` | `place:ardenvale` | Castle Ardenvale was home to High King Kenrith and his family | [Planeswalker's Guide to Eldraine](https://magic.wizards.com/en/news/feature/planeswalkers-guide-eldraine-2019-10-31) |
| `EL013` | `artifact:great_henge` | The Great Henge is Garenbrig's relic, situated there | [Planeswalker's Guide to Eldraine](https://magic.wizards.com/en/news/feature/planeswalkers-guide-eldraine-2019-10-31) |
| `SE037` | `place:riders_lock` | Gisa was held captive at Rider's Lock after Odric captured her | [Games](https://magic.wizards.com/en/news/magic-story/games-2016-04-27) |
| `EO031` | `place:sotheran_supervoid` | The Dawnsire was intended to reignite the Sotheran supervoid | [The Legends of Edge of Eternities](https://magic.wizards.com/en/news/magic-story/the-legends-of-edge-of-eternities) |

The precise quotations and source identifiers are retained in the corresponding
`claim_specs` and generated citation-bearing packs. **Every one of the 113
quotations in the three regenerated packs was checked as a verbatim substring
of the downloaded official Wizards pages** (ELD 15/15, SOI/EMN 46/46,
EOE 52/52; zero failures). The full copyrighted source-page text remains in
an ignored, reproducible cache, not in the repository.

## Consequences and boundaries

- Registered evidence coverage: **835/839 → 839/839** with at least one direct
  first-party cited claim; **4 → 0** without any. This is a finite registered
  entity census, **not** the population of all canon characters and places.
- The updated graph has **1,263 cited claims**, **5,310 nodes**, **8,505
  edges** (previously 1,259 / 5,306 / 8,489). New claim and assertion nodes
  contribute to graph connectivity; they do not establish chronology.
- All four repaired nodes currently have **exactly one** direct cited claim.
  Another **139** entities have only qualified (implied, disputed, unknown or
  alternate-continuity) claims; registration alone does not mean a complete
  biography or multi-plane history.
- `SE037` documents historical imprisonment only, not Rider's Lock's present
  use. `EO031` documents an intended outcome only, not an accomplished ignition.
  `EL012` documents the guide's period, not a current ruler or the Kenrith
  family's later status.
- No source found here attests a strict global order between Old Phyrexia's
  destruction and Yawgmoth's defeat. The localized printed-set identifiers
  `fbb`, `4bb`, `rin` still lack exact primary proof. No new checkboxes,
  release certification, owner approvals or Phase 6 deck permissions follow.
- The one new claim with named card participants (`SE037`/Gisa) reuses two
  preexisting **same-pack, same-official-page** `NAMED_PARTICIPANT` tiers.
  The other three new claims produce no card-name anchors. The new
  `--append-same-source-claims` command fails closed if any new card needs
  fresh set-printing or art evaluation, so the absent full Scryfall snapshot
  never leads to guessed stronger ties. Anchor counts are now **4,127**,
  versus **4,125** previously.

## Reproduction

Run the three `scripts/claim_spec_sources/{eld,soi,eoe}.py` authoring scripts,
fetch their respective registered official story arcs with
`scripts/fetch_story_pages.py --arc`, and run
`scripts/story_claim_pipeline.py build` for exactly those three packs.
The resulting pack audits record each quote hash and its `VERBATIM` status.
Then rebuild graph, story-coverage, entity-census, plane-history, foundation
acceptance and progress artifacts using the checked-in `scripts/` entrypoints.
CI can revalidate committed hashes without retaining the page cache.
