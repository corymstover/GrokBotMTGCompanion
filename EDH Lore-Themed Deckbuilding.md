---
title: "EDH Lore-Themed Deckbuilding"
category: edh
tags: [lore-decks, story-first, methodology, template]
issues: [79, 80, 81]
generated_by: hand-written
sources: [scryfall, wizards-story, spellbook, cr]
related: ["Conflicts & Arcs.md", "EDH Deck Evaluation Checklist.md", "Planeswalker Dossiers.md", "EDH Deck Template.md", "Art & Flavor Story Links.md", "Characters Index.md"]
schema: 2
---

# EDH Lore-Themed Deckbuilding

> **Bot cycle 21 ([#79](https://github.com/corymstover/GrokBotMTGCompanion/issues/79)–[#81](https://github.com/corymstover/GrokBotMTGCompanion/issues/81)).** Story-first Commander deckbuilding: every card earns its slot with a narrative, flavor or mechanical story echo. Power is secondary. Hard rules (color identity, legality, 100 cards, singleton) and bracket barometers still apply — they are facts. Strategic choices are **guidance**. Worked examples: [Brothers' War — Urza](decks/lore-brothers-war-urza-lord-high-artificer.md), [Nahiri, the Lithomancer](decks/lore-nahiri-the-lithomancer.md). Rebuild: `python3 scripts/build_lore_decks.py [--online]`.

## Contents
- [Principles](#principles)
- [Deck types](#deck-types)
- [What counts as a story link](#what-counts-as-a-story-link)
- [Playability floor](#playability-floor)
- [Documenting "why this card belongs"](#documenting-why-this-card-belongs)
- [Facts vs guidance](#facts-vs-guidance)
- [Evaluation criteria](#evaluation-criteria)
- [Template & checklist](#template--checklist)
- [Worked examples](#worked-examples)
- [Relation to other deck kinds](#relation-to-other-deck-kinds)

## Principles
1. **Story first.** Prefer flavor text, art, named characters, iconic items, set-era printings and mechanical echoes of the plot over Game Changers, tutors and infinite combos.
2. **No invented lore.** Every story claim cites an official magic.wizards.com page (or a Scryfall flavor quote). Flag ⚠️ secondary (novel not fetched) and 🚫 non-canonical (Universes Beyond, Echoverse).
3. **Every slot justifies itself.** A card without a story link must be labeled a *playability slot (guidance)* and counted against the lore score.
4. **Still a legal, playable deck.** Color identity (CR 903.5c), Commander legality, singleton, 100 cards, a keepable mana base, some interaction and a fun win path.
5. **Deepen, don't overwrite.** Cross-link [Conflicts & Arcs](Conflicts%20%26%20Arcs.md), [Master Timeline](Master%20Timeline.md), [Characters Index](Characters%20Index.md), [Planeswalker Dossiers](Planeswalker%20Dossiers.md) and [Planes Index](Planes%20Index.md).

## Deck types

### Arc-based
Pick one arc (prefer a deepened Conflicts & Arcs entry). The commander should be a named participant or a fitting legendary from that era. Packages map to **story beats** (cause → mid-war machines → finale), not to EDHREC roles alone.
- Example: [The Brothers' War](Conflicts%20%26%20Arcs.md#the-brothers-war) → [Urza, Lord High Artificer](decks/lore-brothers-war-urza-lord-high-artificer.md).

### Character-based
Pick one well-documented character (dossier or Characters Index ✅). Packages map to **personal timeline chapters** (spark/origin, allegiances, rivalries, current status). Cards that belong to a later incompatible color identity are summarized, not forced into the list.
- Example: [Nahiri](Planeswalker%20Dossiers.md#nahiri) → [Nahiri, the Lithomancer](decks/lore-nahiri-the-lithomancer.md).

## What counts as a story link
Any of the following is evidence (facts from Scryfall or a cited Wizards page):
| Evidence | Example |
|---|---|
| **Named for the story** | card name contains Urza, Mishra, Nahiri, Hedron, Helvault… |
| **Flavor text** | a paper printing's flavor mentions the character, place or event |
| **Story-set printing** | printed in the arc's main sets (e.g. `atq`/`bro` for Brothers' War; `zen`/`bfz`/`znr`/`emn` for Nahiri) |
| **Cited story object** | note citing an official story page (sylex, Immortal Sun, Lithoform Core…) |
| **Mechanical echo (guidance)** | the card's rules do what the story does (Kor + Equipment for Nahiri's lithomancy; Constructs/thopters for Urza's war machines). Label as guidance. |
| **Type echo** | Kor, Construct, Artificer, Eldrazi, Equipment when that type is the story's subject |

Art alone (no flavor, name or set link) is not enough unless [Art & Flavor Story Links](Art%20%26%20Flavor%20Story%20Links.md) already ties the piece to a beat — and then cite that page.

## Playability floor
Keep enough lands (~34–38), a little ramp, a little draw, a little interaction and a fun win path so the story can finish. Prefer **Bracket 2–3** floors: cut Game Changers and two-card infinites unless the story itself is about that combo. Sol Ring and similar staples without a story link are allowed only as labeled playability slots.

## Documenting "why this card belongs"
Every non-basic card gets a row:
```text
| Card | Package | Why it belongs | Identity |
```
- **Package** = story beat or chapter (not only "Ramp").
- **Why** = evidence first (quote + source or machine flag), then one guidance sentence if needed.
- Playability slots start with "**Playability slot (guidance)**".

## Facts vs guidance
| Label | Covers |
|---|---|
| **Fact** | Scryfall Oracle, color identity, legality, Spellbook combos, Game Changer flags, hypergeometric odds, quoted flavor text, quoted Wizards story |
| **Guidance** | package cuts, pilot notes, "how the deck tells it", mechanical-echo justifications, bracket target above the floor |
| **⚠️ / ❓ / 🚫** | same flags as [Knowledge Index](Knowledge%20Index.md#canon--verification-flags) |

## Evaluation criteria
Use the [lore Gate L](EDH%20Deck%20Evaluation%20Checklist.md#gate-l--lore-themed-story-first) in addition to Gates A–E.
1. **Story summary** present, cited, matches Conflicts/Dossier.
2. **Lore score ≥ 60%** of non-basic slots story-connected (machine + notes).
3. **Gate A hard checks** pass (`evaluate_decklist.py`).
4. **Bracket floor** stated; Game Changers and two-card infinites disclosed.
5. **Cross-links** to the arc/character/plane pages.
6. **No invented lore**; secondary material flagged.

## Template & checklist
- Blueprint: [EDH Deck Template → §8 Lore-themed](EDH%20Deck%20Template.md#8-lore-themed-story-first-extension).
- Gates: [EDH Deck Evaluation Checklist → Gate L](EDH%20Deck%20Evaluation%20Checklist.md#gate-l--lore-themed-story-first).
- Spec format: `data/lore_decks/lore_decks.json` → `scripts/build_lore_decks.py`.

## Worked examples
| Deck | Type | Commander | Identity | Floor | Story share |
|---|---|---|---|---|---|
| [Brothers' War (Urza)](decks/lore-brothers-war-urza-lord-high-artificer.md) | Arc | Urza, Lord High Artificer | U | 2 | 58/79 (73%) |
| [Nahiri, the Lithomancer](decks/lore-nahiri-the-lithomancer.md) | Character | Nahiri, the Lithomancer | W | 2 | 57/75 (76%) |

## Relation to other deck kinds
| Kind | Priority | Source of cards |
|---|---|---|
| `core` | EDHREC inclusion | community data |
| `plane` / `theme` | plane set codes / EDHREC theme | [EDH Themed Decks](EDH%20Themed%20Decks.md) |
| `grixis` | imported method | Grixis source repo |
| **`lore`** | story evidence | this guide + Scryfall + Wizards story |

A lore deck may share a commander with a core skeleton; they are different lists with different goals.
