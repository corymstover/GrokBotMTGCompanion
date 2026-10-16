---
title: "Grixis Mission"
category: meta
tags: [grixis, mission, commander-first]
issues: []
generated_by: hand-written
sources: [grixis-repo]
related: ["Front-Matter Schema.md", "grixis/Grixis Refinement Cycle.md", "EDH Deck Evaluation Checklist.md", "grixis/README.md", "EDH Deck Template.md", "ROADMAP.md"]
schema: 2
---

# Grixis Mission

> **Cory's mission for the Grixis section** (set for the Bot cycle 39+ commander-first refinement cycle, relayed to the bot on 2026-10-16). Principles are Cory's; the measurement and process notes below them are ours. Progress: [Grixis Refinement Cycle](Grixis%20Refinement%20Cycle.md).

## Contents
- [Mission](#mission)
- [Principles](#principles)
- [How we apply it](#how-we-apply-it)

## Mission

Each of the 62 decks must be the definitive, maximally optimized version of **that commander's** deck, not a strong Grixis shell.

## Principles

1. **Commander identity first.** The commander's Oracle text, mechanics, flavor and synergies are structurally central to the list.
2. **Maximum optimization within the commander's natural ceiling** (casual to cEDH). No artificial weakening.
3. **No homogenization.** Avoid generic goodstuff, Thoracle and control shells. Staples belong only when they serve the commander.
4. **Complete verification.** Every list is legal, singleton, exactly 100 cards, on current Oracle text, inside the color identity, and its interactions are verified.

## How we apply it

- **Measured, not guessed.** `scripts/grixis_refine.py` scores every deck:
  - *commander dependence:* the share of nonland cards tied to the commander's Oracle text or with high EDHREC synergy for that commander;
  - *homogenization:* overlap with the other 61 lists, generic share, and Thoracle-core and control-core counts.
  - See the [method](Grixis%20Refinement%20Cycle.md#method).
- **Card-level recommendations.** Each recommendation cuts X and adds Y, with a commander-specific reason that quotes both Oracle texts and cites EDHREC data. Each one is verified with `evaluate_decklist.py` (legality, singleton, 100 cards, color identity), the bracket floor, and Commander Spellbook (every source combo kept).
- **Source preserved.** The source list stays on each deck page, credited to Cory's [grixis-commander-encyclopediaGPT](https://github.com/corymstover/grixis-commander-encyclopediaGPT). The refined list is a separate *Refined list* section with a per-deck refinement log.
- **Ceiling respected.** Decks at or near their ceiling are flagged and left unchanged.
- **Gate in the method.** [EDH Deck Evaluation Checklist → Gate G](../EDH%20Deck%20Evaluation%20Checklist.md#gate-g--commander-identity) and the [EDH Deck Template](../EDH%20Deck%20Template.md) carry the commander-identity check for every deck, not only Grixis.
- **Exports.** Each deck's final list is exported for Archidekt in [exports/grixis-archidekt/](../exports/grixis-archidekt/README.md). `validate_all` checks every export against its deck page.
