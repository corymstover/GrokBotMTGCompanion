---
title: "Lookup Guide"
category: meta
tags: [lookup, retrieval]
issues: [46]
generated_by: hand-written
sources: []
related: ["Front-Matter Schema.md", "Characters Index.md", "EDH Packages.md", "FAQ.md", "Format Legality Matrix.md", "Knowledge Index.md"]
schema: 2
---

# Lookup Guide

> **Bot cycle 14 · issue [#46](https://github.com/corymstover/GrokBotMTGCompanion/issues/46) (Phase 4, first pass).** The fastest way to find each kind of fact in this repo, with commands tested against the current data. Start from the [Knowledge Index](Knowledge%20Index.md) when browsing. Use this page when you know what you want.

## Contents
- [Cards](#cards)
- [Rules](#rules)
- [Commander / EDH](#commander--edh)
- [Lore](#lore)
- [Filtering by front-matter](#filtering-by-front-matter)
- [Retrieval index (kb_find)](#retrieval-index-kb_find)
- [Validating the knowledge base](#validating-the-knowledge-base)
- [Answering a question: which source wins](#answering-a-question-which-source-wins)

## Cards
| I need… | Go to | Fast path |
|---|---|---|
| A card's Oracle text, type, identity, flavor, rulings | its entry in `cards/<L>/<prefix>.md` | `rg -i '^"?Sol Ring,' data/card_index.csv` returns `shard` + `anchor` (e.g. `cards/S/so.md#sol-ring`). Then `rg -n '^### Sol Ring$' cards/S/so.md` |
| Placeholder links in hand-written pages | `scripts/resolve_card_links.py` | write `[[Card Name]]`, then run the script on the file |
| Legality in any format | [Format Legality Matrix](Format%20Legality%20Matrix.md) · `data/legality_matrix.csv` | `rg -i '^"?Sol Ring,' data/legality_matrix.csv` (column order = CSV header; L/N/B/R) |
| Banned or restricted lists | [Format Legality Matrix → lists](Format%20Legality%20Matrix.md#banned-and-restricted-lists) | one section per format key |
| Printings, first/latest set, reprint gaps, Reserved List | [Printing History](Printing%20History.md) · `data/printings_summary.csv` | `rg -i '^"?Sol Ring,' data/printings_summary.csv` |
| Who illustrated what | [Artist Index](Artist%20Index.md) · `data/artists.csv` | `rg -i '^"?Rebecca Guay,' data/artists.csv` |
| Tokens, emblems, dungeons (🚫 not cards) | [Tokens, Emblems & Dungeons](Tokens%2C%20Emblems%20%26%20Dungeons.md) · `data/tokens.json` | `python3 -c "import json;print([o for o in json.load(open('data/tokens.json'))['objects'] if o['name']=='Treasure'])"` |
| Where a card is discussed (decks, guides, rules, lore) | [Reverse card index](references/README.md) · the card entry's *Referenced in* line | `python3 scripts/kb_find.py "Sol Ring"` prints the count and the index anchor; `data/card_refs.json` |
| Which cards have entries (coverage) | [Card Index](Card%20Index.md) · `data/card_index.csv` | 33,894 rows, one per card |

## Rules
| I need… | Go to |
|---|---|
| What a keyword does (CR text, examples, rulings, evergreen status) | [Keyword Encyclopedia](Keyword%20Encyclopedia.md): jump by letter, abilities (CR 702) and actions (CR 701) |
| How two rules interact (layers, replacement effects, commander damage…) | [Rules Interactions](Rules%20Interactions.md) |
| A specific card's official rulings | the card entry (rulings are inlined), found via `data/card_index.csv` |
| The exact CR wording | `.cache/MagicCompRules-*.txt` locally (`rg -n '^702\.21' .cache/MagicCompRules-*.txt`); the pages above quote it verbatim |

## Commander / EDH
| I need… | Go to |
|---|---|
| Deck-building rules (identity, singleton, brackets) | [EDH Standards](EDH%20Standards.md) |
| Staples for an identity or role | [EDH Staples](EDH%20Staples.md) |
| An archetype plan | [EDH Archetypes](EDH%20Archetypes.md) → [EDH Packages](EDH%20Packages.md) → [EDH Win Conditions](EDH%20Win%20Conditions.md) / [EDH Interaction](EDH%20Interaction.md) |
| Lands for an identity | [EDH Mana Bases](EDH%20Mana%20Bases.md) |
| Partner / Background pairs | [EDH Pairings](EDH%20Pairings.md) |
| Which decks run a package (and which packages a deck runs) | [EDH Packages](EDH%20Packages.md) *Used in decks* lines · each deck's *Cross-references* block |
| A full list to start from | [decks/](decks/) (46 validated) · [EDH Themed Decks](EDH%20Themed%20Decks.md) · [EDH Upgrade Paths](EDH%20Upgrade%20Paths.md) |
| Competitive (Bracket 5) | ⚠️ [cEDH Primer](cEDH%20Primer.md) only |
| A refined Grixis (U/B/R) list with the reasoning behind it | [grixis/](grixis/README.md) (40 decks) · `rg -l '^kind: grixis' grixis/decks/` |
| Why a deck has its bracket floor, how to play it a bracket lower, pilot tips | the deck's *Bracket calibration & pilot notes* · all decks: [EDH Bracket Calibration](EDH%20Bracket%20Calibration.md) · `rg -l '^bracket_floor: 2' decks/ grixis/decks/` |
| Is my list legal, and what's its bracket floor? | `python3 scripts/evaluate_decklist.py my.txt --combos` · method: [EDH Deck Evaluation Checklist](EDH%20Deck%20Evaluation%20Checklist.md) |
| How to build or refine a deck step by step | [EDH Deck Template](EDH%20Deck%20Template.md) |

## Lore
| I need… | Go to |
|---|---|
| A character's current status | [Characters Index](Characters%20Index.md) (status at a glance) |
| Cards named after a character | [Characters Index → Character cards](Characters%20Index.md#character-cards-name-matched) · [Planeswalker Dossiers → Character cards](Planeswalker%20Dossiers.md#character-cards-name-matched) (name matches, not canon claims) |
| A Planeswalker's life story / spark | [Planeswalker Dossiers](Planeswalker%20Dossiers.md) |
| What happened in a set's story | [Story Arc Summaries](Story%20Arc%20Summaries.md) (beats with citations) → [Conflicts & Arcs](Conflicts%20%26%20Arcs.md) (one entry per arc, incl. older arcs) |
| When something happened | [Master Timeline](Master%20Timeline.md) |
| A plane | [Planes Index](Planes%20Index.md) · travel between planes: [Omenpath & Multiverse Connections](Omenpath%20%26%20Multiverse%20Connections.md) |
| Which card shows a story moment | [Art & Flavor Story Links](Art%20%26%20Flavor%20Story%20Links.md) |
| Novels, comics and other media | [Side-Media Index](Side-Media%20Index.md) |
| The original official story page | [Story Archive Index](Story%20Archive%20Index.md) · `data/story_index.csv` (`date,title,source,words,url`) |
| An item, artifact or world-scale spell | [Items & Artifacts Index](Items%20%26%20Artifacts%20Index.md) |
| Where official sources disagree, or a fact was retconned | [Contradictions & Retcons Log](Contradictions%20%26%20Retcons%20Log.md) |
| Which official pages the lore rests on | [Lore Primary Sources](Lore%20Primary%20Sources.md) |
| **A card's story context and synergies** (which lore entries depict / feature it, Story Spotlight, KB decks, combos, EDHREC commanders, packages) | the card entry's **Lore** and **Synergy** lines (Bot cycle 33, [#99](https://github.com/corymstover/GrokBotMTGCompanion/issues/99)) · [Card Enrichment](Card%20Enrichment.md) (format, by lore entry, by package, clusters) · `data/card_enrichment.json` |
| **Any single lore entry** (arc, arc summary, era, dossier, character, plane, item, retcon), with its tags, citation count and links | [Lore Entry Index](Lore%20Entry%20Index.md) (Bot cycle 31, [#92](https://github.com/corymstover/GrokBotMTGCompanion/issues/92)) · `data/lore_entries.json` · `python3 scripts/kb_find.py <words> --kind item` |

**Lore cross-references** (Bot cycle 32, [#93](https://github.com/corymstover/GrokBotMTGCompanion/issues/93)): every lore entry ends with a generated *Cross-references* block listing the dossiers, characters, planes, items, arcs, arc summaries, eras and retcons related to it (by a hand-written link or a name mention, in either direction), the lore decks whose story map uses it, and — for items — cards with the same name. If A's text points at B, B's block points back at A; `check_lore.py` enforces it. Pointers only: the facts stay in the entry text.

**Lore entry tags** (computed by `scripts/build_lore_index.py`; Bot cycle 31): the kind (`arc`, `summary`, `era`, `dossier`, `character`, `plane`, `item`, `retcon`); `has-secondary` ⚠️, `has-unknowns` ❓, `has-non-canonical` 🚫, `has-retcon` 🔄 when the entry carries that flag; spark state from the Characters Index (`planeswalker`, `spark-lost`, `spark-faded`, `spark-given-up`, `dead`, `alive-or-active`, `status-unknown`); `has-cards` when the entry links card entries.

| I want… | Command |
|---|---|
| Every lore entry about the sylex | `python3 scripts/kb_find.py sylex --category lore` |
| Only item entries | `python3 scripts/kb_find.py stone --kind item` |
| Characters/dossiers whose spark is lost | `python3 scripts/kb_find.py --tag spark-lost --limit 30` |
| Entries with open ❓ questions | `python3 scripts/kb_find.py --tag has-unknowns --limit 100` |
| Entries that touch the Echoverse (🚫) | `python3 scripts/kb_find.py --tag has-non-canonical` |
| Lore pages with entry counts | `rg -n '^entries: ' *.md` |

## Filtering by front-matter
Every major page and every deck starts with YAML front-matter (Bot cycle 15, [#44](https://github.com/corymstover/GrokBotMTGCompanion/issues/44); `scripts/front_matter.py`). Pages carry `title, category (lore/edh/rules/cards/meta), tags, issues, generated_by, sources`. Decks carry `kind (core/plane/theme), commander, color_identity, bracket_floor, game_changers, validated`.

| I want… | Command |
|---|---|
| All lore pages | `rg -l '^category: lore' *.md` (every lore page also carries the `lore` tag since Bot cycle 31) |
| Lore pages made of entries, and what kind | `rg -n '^entry_kind: ' *.md` |
| Pages built by a script (safe to regenerate) | `rg '^generated_by: scripts/' *.md` |
| Pages for an issue | `rg -l '^issues: .*\b39\b' *.md` |
| Decks at bracket 4 or more | `rg -l '^bracket_floor: [45]' decks/` |
| Decks with no Game Changers | `rg -l '^game_changers: 0$' decks/` |
| Decks for a color identity (e.g. Sultai; always WUBRG order since Bot cycle 17) | `rg -l '^color_identity: UBG$' decks/ grixis/decks/` |
| Decks with a two-card infinite | `rg -l '^tags: .*two-card-infinite' decks/ grixis/decks/` |
| Card shards built from an older bulk | `rg -L '^bulk: 2026-10-15' -g '*.md' cards/` |
| Plane-restricted decks | `rg '^plane: ' decks/` |
| Grixis decks at the bracket floor 3 | `rg -l '^bracket_floor: 3' grixis/decks/` |

Every key, type and tag is documented in [Front-Matter Schema](Front-Matter%20Schema.md) (schema v2, Bot cycle 17, [#65](https://github.com/corymstover/GrokBotMTGCompanion/issues/65)), which the script generates from the same table `--check` enforces. Card shards carry front-matter too (`kind: shard`, `prefix`, `cards`, `bulk`).

After running any generator, re-apply with `python3 scripts/front_matter.py`. `--check` fails if any page or deck is missing front-matter or has a stale value.

## Retrieval index (kb_find)
`data/kb_index.json` lists every page and deck with its front-matter and every `##`/`###` heading with its anchor (Bot cycle 17, [#65](https://github.com/corymstover/GrokBotMTGCompanion/issues/65)), plus, since Bot cycle 31 ([#92](https://github.com/corymstover/GrokBotMTGCompanion/issues/92)), one record per lore entry (260) with its computed tags. `scripts/kb_find.py` ranks entries by title, tag, commander and heading matches, and also returns the card entry when the query is an exact card name.

| I want… | Command |
|---|---|
| Where a topic is covered, down to the section | `python3 scripts/kb_find.py commander damage` |
| Only rules pages | `python3 scripts/kb_find.py layers --category rules` |
| Everything with a tag | `python3 scripts/kb_find.py --tag two-card-infinite` |
| A card entry by exact name | `python3 scripts/kb_find.py "Sol Ring"` |
| Lore entries of one kind | `python3 scripts/kb_find.py ashiok --kind retcon` |

Rebuild after editing pages: `python3 scripts/kb_find.py --build` (`validate_all.py` fails while it is stale).

## Validating the knowledge base
`python3 scripts/validate_all.py` runs every check in one go (Bot cycle 17, [#67](https://github.com/corymstover/GrokBotMTGCompanion/issues/67)): links and anchors, front-matter schema, retrieval-index freshness, citations (every Wizards URL is in the official sitemap, resolves, or is a resolving Internet Archive copy; every `CR nnn.nx` rule number exists in the cached Comprehensive Rules), Oracle drift (every card entry verbatim vs the Scryfall bulk), deck re-checks (legality, identity, 100 cards, singleton, Game Changer count still matches Scryfall), and generator freshness. Since Bot cycle 31 ([#94](https://github.com/corymstover/GrokBotMTGCompanion/issues/94)) two lore steps run as well. **lore-entries** (`scripts/check_lore.py`) checks that every arc, era, dossier, character, plane, item and retcon entry cites an official page, that dossier timeline rows and retcon statement rows are cited, that entry anchors resolve, that spark state agrees across the Characters Index, the dossier summary and the retcon log, and that the Lore Entry Index is current. Since Bot cycle 32 ([#93](https://github.com/corymstover/GrokBotMTGCompanion/issues/93)) lore-entries also checks that the generated cross-reference blocks are current and that every entry→entry link and lore-deck pointer is reciprocal. **lore-quotes** (`scripts/lore_quotes.py --check`) checks that every quotation on 13 lore pages appears verbatim in the cached official page it cites, or in Scryfall card text. Since Bot cycle 32 ([#96](https://github.com/corymstover/GrokBotMTGCompanion/issues/96)) it also covers 12 rules/FAQ/EDH pages, whose quotes may match the cached Comprehensive Rules, Scryfall rulings, cached Wizards articles (`.cache/story/articles/`) or, for the two Grixis-derived method pages, the read-only Grixis source. The only allowed exceptions are those documented in `data/lore_quote_exceptions.json` (image-only text, non-Wizards sources, labels or code in quotation marks). Without the gitignored story cache, it compares quote fingerprints with `data/lore_quotes.json` instead. Default is offline; `--online` re-checks citations live and verifies against Scryfall's newest bulk; `--only` / `--skip` take step names.

## Answering a question: which source wins
1. **Card text and legality:** the card entry and the legality matrix (Scryfall bulk, checked by `scripts/verify_cards.py`). Re-check B&R after announcements ([#17](https://github.com/corymstover/GrokBotMTGCompanion/issues/17)).
2. **Rules:** the Comprehensive Rules quotes and official rulings beat any summary.
3. **Lore:** cited magic.wizards.com pages. Follow the flags: ✅ sourced · ❓ unverified · ⚠️ caveat · 🚫 non-canonical (e.g. Echoverse).
4. **EDH advice:** the generated guides are data-derived (EDHREC/Scryfall). Every recommendation must also pass color identity and Commander legality.
