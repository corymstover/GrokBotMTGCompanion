---
title: "Front-Matter Schema"
category: meta
tags: [schema, front-matter, tags, retrieval]
issues: [65]
generated_by: scripts/front_matter.py
sources: []
related: ["EDH Bracket Calibration.md", "Knowledge Index.md", "Lore Primary Sources.md", "Art & Flavor Story Links.md", "Card Data Conventions.md", "Characters Index.md"]
schema: 2
---

# Front-Matter Schema

> **Auto-generated** by `scripts/front_matter.py` (Bot cycle 17, issue [#65](https://github.com/corymstover/GrokBotMTGCompanion/issues/65)) from the `SCHEMA` and `PAGES` tables in the script, so this page cannot drift from what `--check` enforces. Schema version **2**. Do not hand-edit.
> Coverage: **52** registered pages (README.md and GOAL.md are exempt), **110** decks, **684** card shards, **28** reverse-index pages. Related: [Lookup Guide](Lookup%20Guide.md) · [Knowledge Index](Knowledge%20Index.md) · [Card Data Conventions](Card%20Data%20Conventions.md).

## Contents
- [Format](#format)
- [Page keys](#page-keys)
- [Deck keys](#deck-keys)
- [Card-shard keys](#card-shard-keys)
- [Reverse-index keys](#reverse-index-keys)
- [Source keys](#source-keys)
- [Tag vocabulary](#tag-vocabulary)
- [Validation rules](#validation-rules)
- [Filtering examples](#filtering-examples)

## Format

Every entry starts with a YAML block between `---` lines. Values are flat: strings (quoted when free text), ints, `true`/`false`, and inline lists `[a, b]`. This flat subset is readable by any YAML parser and by `rg` line matching. README.md and GOAL.md are exempt.

## Page keys

| Key | Type | Required | Meaning |
|---|---|---|---|
| `title` | string | yes | The page's H1 heading, quoted. |
| `category` | enum: cards/edh/lore/meta/rules | yes | Top-level area of the knowledge base. |
| `tags` | list of tags | yes | Lower-case kebab-case topic tags (vocabulary below). |
| `issues` | list of int | yes | GitHub issues that created or own the page ([] if none). |
| `generated_by` | script path or `hand-written` | yes | Generator to re-run instead of hand-editing. |
| `sources` | list of source keys | yes | Where the facts come from (source keys below). |
| `related` | list of page paths | yes | Up to 6 most strongly linked registered pages (links in + out; meta pages excluded for non-meta pages). Computed. |
| `entry_kind` | enum: arc/summary/era/dossier/character/plane/item/retcon | when applicable | Lore entry pages only (Bot cycle 31, #92): what each entry on the page is (see scripts/lore_lib.py ENTRY_PAGES). |
| `entries` | int | when applicable | Lore entry pages only: number of entries on the page (indexed in data/lore_entries.json and Lore Entry Index.md). |
| `schema` | int | yes | Front-matter schema version (currently 2). |

## Deck keys

| Key | Type | Required | Meaning |
|---|---|---|---|
| `title` | string | yes | The deck page's H1 heading. |
| `category` | `deck` | yes | Always `deck`. |
| `kind` | enum: core/plane/theme/grixis/lore | yes | core = EDHREC skeleton; plane = plane-restricted; theme = EDHREC theme page; grixis = imported from the Grixis repo; lore = story-first lore-themed (Bot cycle 21). |
| `commander` | string | yes | First commander's Scryfall name. |
| `color_identity` | WUBRG-ordered letters or `C` | yes | Commander color identity (CR 903.4), always in WUBRG order. |
| `bracket_floor` | int 1–5 | yes | Minimum bracket by the published barometers (Game Changers, MLD, two-card infinites). |
| `game_changers` | int | yes | Number of official Game Changers in the 100. |
| `combos` | int | yes | Complete Commander Spellbook combos in the list. |
| `two_card_infinites` | int | yes | Two-card infinite combos among them. |
| `validated` | bool | yes | All hard checks pass (legality, identity, 100 cards, singleton). |
| `tags` | list of tags | yes | Computed: kind, identity name, `bracket-floor-N`, Game Changer and combo flags, plane/theme. |
| `plane` | string | when applicable | Plane-restricted decks only. |
| `theme` | string | when applicable | Theme decks only (EDHREC theme). |
| `lore_score` | float 0–100 | when applicable | Lore decks only (Bot cycle 23): % of non-basic cards (commander + non-lands + non-basic lands) that are story-linked. |
| `lore_standard_met` | bool | when applicable | Lore decks only: lore_score ≥ 85 (the Lore-Themed Deckbuilding standard; enforced by `build_lore_decks.py --check`). |
| `source_repo` | string | when applicable | Grixis decks only: the read-only source repository. |
| `legality_status` | enum: pending | when applicable | Bot cycle 38: present only on decks published before some cards are Commander-legal (data/grixis_pending.json). validate_all accepts the listed cards only while legal_from is in the future. |
| `legal_from` | date YYYY-MM-DD | when applicable | Pending decks only: the date Scryfall gives for the not-yet-legal cards' set release. |
| `pending_cards` | list of card names | when applicable | Pending decks only: the cards that are not Commander-legal yet. |
| `schema` | int | yes | Front-matter schema version (currently 2). |

## Card-shard keys

| Key | Type | Required | Meaning |
|---|---|---|---|
| `title` | string | yes | The shard's H1 (`Cards — `prefix``). |
| `category` | `cards` | yes | Always `cards`. |
| `kind` | `shard` | yes | Always `shard`. |
| `prefix` | string | yes | Shard key prefix (see Card Data Conventions → Storage layout). |
| `cards` | int | yes | Number of card entries in the shard. |
| `bulk` | date | yes | Scryfall Oracle bulk date the entries were rendered from. |
| `generated_by` | `scripts/ingest_scryfall.py` | yes | Shards are never hand-edited. |
| `tags` | list of tags | yes | Always `[card-entries, oracle, rulings]`. |
| `schema` | int | yes | Front-matter schema version (currently 2). |

## Reverse-index keys

| Key | Type | Required | Meaning |
|---|---|---|---|
| `title` | string | yes | The page's H1 (`Reverse card index — L`). |
| `category` | `cards` | yes | Always `cards`. |
| `kind` | `reference` | yes | Always `reference`. |
| `letter` | string | yes | Card-shard letter folder the page mirrors (`index` for references/README.md). |
| `cards` | int | yes | Number of cited cards listed on the page. |
| `generated_by` | `scripts/build_crossrefs.py` | yes | Never hand-edited. |
| `tags` | list of tags | yes | Always `[reverse-index, cross-references]`. |
| `schema` | int | yes | Front-matter schema version (currently 2). |

Example (deck):

```yaml
---
title: "Grixis Deck — Cult of Skaro"
category: deck
kind: grixis
commander: "Cult of Skaro"
color_identity: UBR
bracket_floor: 3
game_changers: 3
combos: 1
two_card_infinites: 1
validated: true
tags: [grixis, grixis, bracket-floor-3, game-changers, two-card-infinite]
source_repo: corymstover/grixis-commander-encyclopediaGPT
schema: 2
---
```

## Source keys

| Key | Meaning |
|---|---|
| `scryfall` | Scryfall Oracle/rulings/default-cards bulk |
| `wizards-story` | magic.wizards.com story pages |
| `edhrec` | EDHREC public JSON (community data) |
| `spellbook` | Commander Spellbook API (community data) |
| `cr` | Comprehensive Rules text |
| `wotc-articles` | magic.wizards.com / WPN announcements and documents |
| `grixis-repo` | corymstover/grixis-commander-encyclopediaGPT (read-only source) |

## Tag vocabulary

Tags are lower-case kebab-case (`^[a-z0-9+]+(-[a-z0-9+]+)*$`). Page tags are assigned in the `PAGES` registry; deck tags are computed from the deck body.

### Page tags

| Tag | Pages |
|---|---|
| `archetypes` | [EDH Archetypes](EDH%20Archetypes.md) |
| `arcs` | [Conflicts & Arcs](Conflicts%20%26%20Arcs.md) · [Story Arc Summaries](Story%20Arc%20Summaries.md) |
| `art` | [Art & Flavor Story Links](Art%20%26%20Flavor%20Story%20Links.md) |
| `art-credits` | [Artist Index](Artist%20Index.md) |
| `artifacts` | [Items & Artifacts Index](Items%20%26%20Artifacts%20Index.md) |
| `artists` | [Artist Index](Artist%20Index.md) |
| `background` | [EDH Pairings](EDH%20Pairings.md) |
| `banned-restricted` | [Format Legality Matrix](Format%20Legality%20Matrix.md) |
| `blueprint` | [EDH Deck Template](EDH%20Deck%20Template.md) |
| `bracket-5` | [cEDH Primer](cEDH%20Primer.md) |
| `brackets` | [EDH Bracket Calibration](EDH%20Bracket%20Calibration.md) · [EDH Deck Evaluation Checklist](EDH%20Deck%20Evaluation%20Checklist.md) · [EDH Standards](EDH%20Standards.md) |
| `budget` | [EDH Upgrade Paths](EDH%20Upgrade%20Paths.md) |
| `calibration` | [EDH Bracket Calibration](EDH%20Bracket%20Calibration.md) |
| `canon` | [Contradictions & Retcons Log](Contradictions%20%26%20Retcons%20Log.md) |
| `card-advantage` | [EDH Packages](EDH%20Packages.md) |
| `card-enrichment` | [Card Enrichment](Card%20Enrichment.md) |
| `card-entries` | [Card Data Conventions](Card%20Data%20Conventions.md) |
| `cedh` | [cEDH Primer](cEDH%20Primer.md) |
| `changelog` | [Update Log](Update%20Log.md) |
| `characters` | [Characters Index](Characters%20Index.md) |
| `checklist` | [EDH Deck Evaluation Checklist](EDH%20Deck%20Evaluation%20Checklist.md) |
| `color-identity` | [EDH Mana Bases](EDH%20Mana%20Bases.md) · [EDH Standards](EDH%20Standards.md) · [EDH Staples](EDH%20Staples.md) |
| `combos` | [EDH Bracket Calibration](EDH%20Bracket%20Calibration.md) · [EDH Win Conditions](EDH%20Win%20Conditions.md) |
| `comics` | [Side-Media Index](Side-Media%20Index.md) |
| `competitive` | [cEDH Primer](cEDH%20Primer.md) |
| `conflicts` | [Conflicts & Arcs](Conflicts%20%26%20Arcs.md) |
| `contradictions` | [Contradictions & Retcons Log](Contradictions%20%26%20Retcons%20Log.md) |
| `conventions` | [Card Data Conventions](Card%20Data%20Conventions.md) |
| `corrections` | [Grixis Corrections](grixis/Grixis%20Corrections.md) |
| `coverage` | [Card Enrichment](Card%20Enrichment.md) · [Card Index](Card%20Index.md) |
| `deckbuilding-rules` | [EDH Standards](EDH%20Standards.md) |
| `decks` | [EDH Themed Decks](EDH%20Themed%20Decks.md) · [README](grixis/README.md) |
| `dossiers` | [Planeswalker Dossiers](Planeswalker%20Dossiers.md) |
| `dungeons` | [Tokens, Emblems & Dungeons](Tokens%2C%20Emblems%20%26%20Dungeons.md) |
| `emblems` | [Tokens, Emblems & Dungeons](Tokens%2C%20Emblems%20%26%20Dungeons.md) |
| `entries` | [Lore Entry Index](Lore%20Entry%20Index.md) |
| `eras` | [Master Timeline](Master%20Timeline.md) |
| `evaluation` | [EDH Deck Evaluation Checklist](EDH%20Deck%20Evaluation%20Checklist.md) |
| `evergreen` | [Keyword Encyclopedia](Keyword%20Encyclopedia.md) |
| `faq` | [FAQ](FAQ.md) |
| `flavor` | [Art & Flavor Story Links](Art%20%26%20Flavor%20Story%20Links.md) |
| `follow-ups` | [Grixis Integration Summary](grixis/Grixis%20Integration%20Summary.md) |
| `formats` | [Format Legality Matrix](Format%20Legality%20Matrix.md) |
| `front-matter` | [Front-Matter Schema](Front-Matter%20Schema.md) |
| `game-changers` | [EDH Bracket Calibration](EDH%20Bracket%20Calibration.md) |
| `grixis` | [Grixis Corrections](grixis/Grixis%20Corrections.md) · [Grixis Evaluation](grixis/Grixis%20Evaluation.md) · [Grixis Integration Summary](grixis/Grixis%20Integration%20Summary.md) · [Grixis Packages](grixis/Grixis%20Packages.md) · [README](grixis/README.md) |
| `index` | [Card Index](Card%20Index.md) · [Knowledge Index](Knowledge%20Index.md) · [Lore Entry Index](Lore%20Entry%20Index.md) · [README](grixis/README.md) |
| `interaction` | [EDH Interaction](EDH%20Interaction.md) |
| `interactions` | [Rules Interactions](Rules%20Interactions.md) |
| `items` | [Items & Artifacts Index](Items%20%26%20Artifacts%20Index.md) |
| `keywords` | [Keyword Encyclopedia](Keyword%20Encyclopedia.md) |
| `lands` | [EDH Mana Bases](EDH%20Mana%20Bases.md) |
| `legality` | [Format Legality Matrix](Format%20Legality%20Matrix.md) · [Grixis Corrections](grixis/Grixis%20Corrections.md) · [Grixis Evaluation](grixis/Grixis%20Evaluation.md) |
| `lookup` | [Lookup Guide](Lookup%20Guide.md) |
| `lore` | [Art & Flavor Story Links](Art%20%26%20Flavor%20Story%20Links.md) · [Card Enrichment](Card%20Enrichment.md) · [Characters Index](Characters%20Index.md) · [Conflicts & Arcs](Conflicts%20%26%20Arcs.md) · [Contradictions & Retcons Log](Contradictions%20%26%20Retcons%20Log.md) · [FAQ](FAQ.md) · [Items & Artifacts Index](Items%20%26%20Artifacts%20Index.md) · [Lore Entry Index](Lore%20Entry%20Index.md) · [Lore Primary Sources](Lore%20Primary%20Sources.md) · [Master Timeline](Master%20Timeline.md) · [Omenpath & Multiverse Connections](Omenpath%20%26%20Multiverse%20Connections.md) · [Planes Index](Planes%20Index.md) · [Planeswalker Dossiers](Planeswalker%20Dossiers.md) · [Side-Media Index](Side-Media%20Index.md) · [Story Arc Summaries](Story%20Arc%20Summaries.md) · [Story Archive Index](Story%20Archive%20Index.md) |
| `lore-decks` | [EDH Lore-Themed Deckbuilding](EDH%20Lore-Themed%20Deckbuilding.md) |
| `maintenance` | [Knowledge Index](Knowledge%20Index.md) |
| `mana-base` | [EDH Mana Bases](EDH%20Mana%20Bases.md) |
| `methodology` | [EDH Deck Evaluation Checklist](EDH%20Deck%20Evaluation%20Checklist.md) · [EDH Deck Template](EDH%20Deck%20Template.md) · [EDH Lore-Themed Deckbuilding](EDH%20Lore-Themed%20Deckbuilding.md) |
| `milestones` | [Progress Tracker](Progress%20Tracker.md) |
| `mulligan` | [EDH Mulligans](EDH%20Mulligans.md) |
| `multiverse` | [Omenpath & Multiverse Connections](Omenpath%20%26%20Multiverse%20Connections.md) |
| `not-cards` | [Tokens, Emblems & Dungeons](Tokens%2C%20Emblems%20%26%20Dungeons.md) |
| `novels` | [Side-Media Index](Side-Media%20Index.md) |
| `omenpaths` | [Omenpath & Multiverse Connections](Omenpath%20%26%20Multiverse%20Connections.md) |
| `opening-hand` | [EDH Mulligans](EDH%20Mulligans.md) |
| `oracle` | [Grixis Corrections](grixis/Grixis%20Corrections.md) |
| `packages` | [EDH Packages](EDH%20Packages.md) · [Grixis Packages](grixis/Grixis%20Packages.md) |
| `pairings` | [EDH Pairings](EDH%20Pairings.md) |
| `partner` | [EDH Pairings](EDH%20Pairings.md) |
| `phase-8` | [Card Enrichment](Card%20Enrichment.md) |
| `pilot-notes` | [EDH Bracket Calibration](EDH%20Bracket%20Calibration.md) |
| `plane-restricted` | [EDH Themed Decks](EDH%20Themed%20Decks.md) |
| `planes` | [Omenpath & Multiverse Connections](Omenpath%20%26%20Multiverse%20Connections.md) · [Planes Index](Planes%20Index.md) |
| `planeswalkers` | [Characters Index](Characters%20Index.md) · [Planeswalker Dossiers](Planeswalker%20Dossiers.md) |
| `planeswalkers-guide` | [Lore Primary Sources](Lore%20Primary%20Sources.md) |
| `primary` | [Lore Primary Sources](Lore%20Primary%20Sources.md) |
| `printings` | [Printing History](Printing%20History.md) |
| `progress` | [Progress Tracker](Progress%20Tracker.md) |
| `ramp` | [EDH Packages](EDH%20Packages.md) |
| `releases` | [Knowledge Snapshots](Knowledge%20Snapshots.md) |
| `relics` | [Items & Artifacts Index](Items%20%26%20Artifacts%20Index.md) |
| `removal` | [EDH Interaction](EDH%20Interaction.md) |
| `reprints` | [Printing History](Printing%20History.md) |
| `reserved-list` | [Printing History](Printing%20History.md) |
| `retcons` | [Contradictions & Retcons Log](Contradictions%20%26%20Retcons%20Log.md) |
| `retrieval` | [Front-Matter Schema](Front-Matter%20Schema.md) · [Lookup Guide](Lookup%20Guide.md) · [Lore Entry Index](Lore%20Entry%20Index.md) |
| `roadmap` | [ROADMAP](ROADMAP.md) |
| `rules` | [FAQ](FAQ.md) · [Rules Interactions](Rules%20Interactions.md) |
| `rules-insights` | [Grixis Packages](grixis/Grixis%20Packages.md) |
| `rulings` | [Keyword Encyclopedia](Keyword%20Encyclopedia.md) · [Rules Interactions](Rules%20Interactions.md) |
| `schema` | [Front-Matter Schema](Front-Matter%20Schema.md) |
| `side-media` | [Side-Media Index](Side-Media%20Index.md) |
| `snapshots` | [Knowledge Snapshots](Knowledge%20Snapshots.md) |
| `sources` | [Lore Primary Sources](Lore%20Primary%20Sources.md) · [Story Archive Index](Story%20Archive%20Index.md) |
| `sparks` | [Planeswalker Dossiers](Planeswalker%20Dossiers.md) |
| `sprint` | [ROADMAP](ROADMAP.md) |
| `staples` | [EDH Staples](EDH%20Staples.md) |
| `status` | [Characters Index](Characters%20Index.md) |
| `stax` | [EDH Interaction](EDH%20Interaction.md) |
| `story-archive` | [Story Archive Index](Story%20Archive%20Index.md) |
| `story-beats` | [Story Arc Summaries](Story%20Arc%20Summaries.md) |
| `story-episodes` | [Lore Primary Sources](Lore%20Primary%20Sources.md) |
| `story-first` | [EDH Lore-Themed Deckbuilding](EDH%20Lore-Themed%20Deckbuilding.md) |
| `story-spotlight` | [Art & Flavor Story Links](Art%20%26%20Flavor%20Story%20Links.md) |
| `strategy` | [EDH Archetypes](EDH%20Archetypes.md) |
| `summary` | [Grixis Integration Summary](grixis/Grixis%20Integration%20Summary.md) |
| `swap-ledger` | [EDH Deck Template](EDH%20Deck%20Template.md) |
| `synergy` | [Card Enrichment](Card%20Enrichment.md) |
| `tags` | [Front-Matter Schema](Front-Matter%20Schema.md) · [Knowledge Snapshots](Knowledge%20Snapshots.md) |
| `template` | [EDH Deck Template](EDH%20Deck%20Template.md) · [EDH Lore-Themed Deckbuilding](EDH%20Lore-Themed%20Deckbuilding.md) |
| `themes` | [EDH Themed Decks](EDH%20Themed%20Decks.md) |
| `timeline` | [Master Timeline](Master%20Timeline.md) |
| `tokens` | [Tokens, Emblems & Dungeons](Tokens%2C%20Emblems%20%26%20Dungeons.md) |
| `upgrades` | [EDH Upgrade Paths](EDH%20Upgrade%20Paths.md) |
| `validation` | [Grixis Evaluation](grixis/Grixis%20Evaluation.md) |
| `win-conditions` | [EDH Win Conditions](EDH%20Win%20Conditions.md) |

### Deck tags

| Tag | Decks |
|---|---|
| `abzan` | 1 |
| `azorius` | 1 |
| `bant` | 2 |
| `boros` | 2 |
| `bracket-floor-2` | 12 |
| `bracket-floor-3` | 32 |
| `bracket-floor-4` | 66 |
| `colorless` | 1 |
| `combos` | 26 |
| `core` | 32 |
| `dimir` | 1 |
| `dune` | 1 |
| `esper` | 1 |
| `five-color` | 1 |
| `game-changers` | 95 |
| `glint` | 1 |
| `golgari` | 2 |
| `grixis` | 125 |
| `gruul` | 3 |
| `ink` | 1 |
| `izzet` | 1 |
| `jeskai` | 1 |
| `jund` | 1 |
| `lore` | 2 |
| `mardu` | 3 |
| `mono-black` | 3 |
| `mono-blue` | 2 |
| `mono-green` | 2 |
| `mono-red` | 1 |
| `mono-white` | 3 |
| `naya` | 1 |
| `no-game-changers` | 15 |
| `orzhov` | 1 |
| `pending-legality` | 2 |
| `plane` | 10 |
| `plane-dominaria` | 1 |
| `plane-eldraine` | 1 |
| `plane-innistrad` | 1 |
| `plane-ixalan` | 1 |
| `plane-kamigawa` | 1 |
| `plane-new` | 1 |
| `plane-ravnica` | 1 |
| `plane-tarkir` | 1 |
| `plane-theros` | 1 |
| `plane-zendikar` | 1 |
| `rakdos` | 1 |
| `selesnya` | 1 |
| `simic` | 2 |
| `sultai` | 2 |
| `temur` | 1 |
| `theme` | 4 |
| `theme-landfall` | 1 |
| `theme-lifegain` | 1 |
| `theme-planeswalkers` | 1 |
| `theme-self-mill` | 1 |
| `two-card-infinite` | 52 |
| `witch` | 2 |
| `yore` | 1 |

## Validation rules

`python3 scripts/front_matter.py --check` (also step 2 of `scripts/validate_all.py`) fails when:
- an entry has no front-matter, a required key is missing, a key is not in the schema, or a value is `null` (unparsed);
- a value has the wrong type (int, bool, list, enum, WUBRG order, unknown source key, unregistered related page, missing generator script);
- a tag is not kebab-case;
- the stored block differs from what the script computes now (stale — re-run `python3 scripts/front_matter.py`);
- a top-level or `grixis/` page is not in the registry, or this schema page is stale.

## Filtering examples

| I want… | Command |
|---|---|
| All lore pages | `rg -l '^category: lore' *.md` |
| Lore pages made of entries, with counts | `rg -n '^entries: ' *.md` |
| Every lore entry flagged ❓ unknown | `python3 scripts/kb_find.py --tag has-unknowns --category lore` |
| Dossiers/characters whose spark is lost | `python3 scripts/kb_find.py --tag spark-lost` |
| Pages about brackets | `rg -l '^tags: .*\bbrackets\b' *.md grixis/*.md` |
| Pages related to Rules Interactions | `rg -l '^related: .*Rules Interactions' *.md` |
| Decks with a two-card infinite | `rg -l '^tags: .*two-card-infinite' decks grixis/decks` |
| Grixis-identity decks anywhere | `rg -l '^color_identity: UBR$' decks grixis/decks` |
| Decks at bracket floor 2 | `rg -l '^bracket_floor: 2' decks grixis/decks` |
| Card shards rendered from an older bulk | `rg -L '^bulk: 2026-10-15' -g '*.md' cards` |

