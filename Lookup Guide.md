---
title: "Lookup Guide"
category: meta
tags: [lookup, retrieval]
issues: [46]
generated_by: hand-written
sources: []
---

# Lookup Guide

> **Bot cycle 14 · issue [#46](https://github.com/corymstover/GrokBotMTGCompanion/issues/46) (Phase 4, first pass).** The fastest way to find each kind of fact in this repo, with commands tested against the current data. Start from the [Knowledge Index](Knowledge%20Index.md) when browsing. Use this page when you know what you want.

## Contents
- [Cards](#cards)
- [Rules](#rules)
- [Commander / EDH](#commander--edh)
- [Lore](#lore)
- [Filtering by front-matter](#filtering-by-front-matter)
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
| A full list to start from | [decks/](decks/) (46 validated) · [EDH Themed Decks](EDH%20Themed%20Decks.md) · [EDH Upgrade Paths](EDH%20Upgrade%20Paths.md) |
| Competitive (Bracket 5) | ⚠️ [cEDH Primer](cEDH%20Primer.md) only |
| A refined Grixis (U/B/R) list with the reasoning behind it | [grixis/](grixis/README.md) (40 decks) · `rg -l '^kind: grixis' grixis/decks/` |
| Is my list legal, and what's its bracket floor? | `python3 scripts/evaluate_decklist.py my.txt --combos` · method: [EDH Deck Evaluation Checklist](EDH%20Deck%20Evaluation%20Checklist.md) |
| How to build or refine a deck step by step | [EDH Deck Template](EDH%20Deck%20Template.md) |

## Lore
| I need… | Go to |
|---|---|
| A character's current status | [Characters Index](Characters%20Index.md) (status at a glance) |
| A Planeswalker's life story / spark | [Planeswalker Dossiers](Planeswalker%20Dossiers.md) |
| What happened in a set's story | [Story Arc Summaries](Story%20Arc%20Summaries.md) (beats with citations) → [Conflicts & Arcs](Conflicts%20%26%20Arcs.md) (one entry per arc, incl. older arcs) |
| When something happened | [Master Timeline](Master%20Timeline.md) |
| A plane | [Planes Index](Planes%20Index.md) · travel between planes: [Omenpath & Multiverse Connections](Omenpath%20%26%20Multiverse%20Connections.md) |
| Which card shows a story moment | [Art & Flavor Story Links](Art%20%26%20Flavor%20Story%20Links.md) |
| Novels, comics and other media | [Side-Media Index](Side-Media%20Index.md) |
| The original official story page | [Story Archive Index](Story%20Archive%20Index.md) · `data/story_index.csv` (`date,title,source,words,url`) |

## Filtering by front-matter
Every major page and every deck starts with YAML front-matter (Bot cycle 15, [#44](https://github.com/corymstover/GrokBotMTGCompanion/issues/44); `scripts/front_matter.py`). Pages carry `title, category (lore/edh/rules/cards/meta), tags, issues, generated_by, sources`. Decks carry `kind (core/plane/theme), commander, color_identity, bracket_floor, game_changers, validated`.

| I want… | Command |
|---|---|
| All lore pages | `rg -l '^category: lore' *.md` |
| Pages built by a script (safe to regenerate) | `rg '^generated_by: scripts/' *.md` |
| Pages for an issue | `rg -l '^issues: .*\b39\b' *.md` |
| Decks at bracket 4 or more | `rg -l '^bracket_floor: [45]' decks/` |
| Decks with no Game Changers | `rg -l '^game_changers: 0$' decks/` |
| Decks for a color identity (e.g. Sultai) | `rg -l '^color_identity: BGU$' decks/` |
| Plane-restricted decks | `rg '^plane: ' decks/` |
| Grixis decks at the bracket floor 3 | `rg -l '^bracket_floor: 3' grixis/decks/` |

After running any generator, re-apply with `python3 scripts/front_matter.py`. `--check` fails if any page or deck is missing front-matter or has a stale value.

## Answering a question: which source wins
1. **Card text and legality:** the card entry and the legality matrix (Scryfall bulk, checked by `scripts/verify_cards.py`). Re-check B&R after announcements ([#17](https://github.com/corymstover/GrokBotMTGCompanion/issues/17)).
2. **Rules:** the Comprehensive Rules quotes and official rulings beat any summary.
3. **Lore:** cited magic.wizards.com pages. Follow the flags: ✅ sourced · ❓ unverified · ⚠️ caveat · 🚫 non-canonical (e.g. Echoverse).
4. **EDH advice:** the generated guides are data-derived (EDHREC/Scryfall). Every recommendation must also pass color identity and Commander legality.
