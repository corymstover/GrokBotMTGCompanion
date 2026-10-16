---
title: "EDH Commander-First Deckbuilding"
category: edh
tags: [commander-first, methodology, blueprints, simulator, deckbuilding-rules]
issues: []
generated_by: hand-written
sources: [cr, wotc-articles, edhrec, spellbook, scryfall]
related: ["EDH Lift and Synergy.md", "EDH Standards.md"]
schema: 2
---

# EDH Commander-First Deckbuilding

> **Bot cycle 57.5 (M3).** Commander-first means the commander's colour identity and abilities define the deck, and every other card is judged by what it does *with this commander*. This page separates the **rules (fact)**, Wizards' **description of the format (official)**, and the **method this companion follows (guidance)**, with the tools that implement each step.

## Contents
- [The rules (fact)](#the-rules-fact)
- [The format's intent (official)](#the-formats-intent-official)
- [The method (guidance)](#the-method-guidance)
- [What the evidence can and can't say](#what-the-evidence-can-and-cant-say)
- [Sources](#sources)

## The rules (fact)

From the Comprehensive Rules (cached CR, `.cache/MagicCompRules-*.txt`):

- **CR 903.3:** "Each deck has a legendary card designated as its commander."
- **CR 903.4:** "The Commander variant uses color identity to determine what cards can be in a deck with a certain commander."
- **CR 903.5a:** "Each deck must contain exactly 100 cards, including its commander."
- **CR 903.5b:** "Other than basic lands, each card in a Commander deck must have a different English name."
- **CR 903.5c:** "A card can be included in a Commander deck only if every color in its color identity is also found in the color identity of the deck's commander."
- **CR 903.8:** "A commander cast from the command zone costs an additional {2} for each previous time the player casting it has cast it from the command zone that game."

Legality and brackets are covered in [EDH Standards](EDH%20Standards.md). The colour identity of the commander is the hard boundary of the card pool; nothing else on this page is a rule.

## The format's intent (official)

Wizards' [Commander format page](https://magic.wizards.com/en/formats/commander) describes the format as picking a hero and building the deck around them: you choose a legendary creature or artifact as your commander, then build the rest around its colour identity and its unique abilities. The same page presents the **Commander Brackets** as an optional matchmaking tool for the pregame conversation, with each bracket's *intent and philosophy* as its most important part. Game Changers, two-card infinites, extra turns and mass land denial serve as barometers. The [October 21, 2025 brackets update](https://magic.wizards.com/en/news/announcements/commander-brackets-beta-update-october-21-2025) set out per-bracket expectations, and the [February 9, 2026 update](https://magic.wizards.com/en/news/announcements/commander-brackets-beta-update-february-9-2026) kept the system unchanged and stressed that brackets guide the conversation rather than gate who may play whom.

So *commander-first* is the format's own premise. The aim is a deck that plays like *its commander* at the bracket its commander naturally reaches, not the strongest pile in those colours.

## The method (guidance)

The companion's pipeline, in order. Each step leaves a record and an evidence class.

1. **Read the commander.** Oracle text, mana value, colour identity, partner or companion rules (Scryfall Oracle bulk; `fact`).
2. **Write the blueprint** ([blueprints](grixis/blueprints/README.md), M2). Contents:
   - the identity core (what this commander does that others don't);
   - anti-goals;
   - required packages with minimum counts;
   - win conditions, failure modes, tutor targets and construction rules;
   - a ceiling estimate with evidence.

   Every field carries an evidence class and confidence.
3. **Gather evidence per card** ([EDH Lift and Synergy](EDH%20Lift%20and%20Synergy.md), M3). Sources:
   - EDHREC lift, inclusion and sample size (`derived_metric`);
   - the Oracle hook to the commander (`heuristic`);
   - Commander Spellbook combos and the interaction review (`fact`);
   - blueprint package membership (`strategic_judgment`).

   High lift with a real Oracle hook is the commander-first signal. High inclusion with lift ≈ 1 is a staple, to be judged on raw power and the bracket.
4. **Test, don't assert** (M3 simulator). Paired goldfish games on identical shuffles compare a champion and a challenger: commander turn, curve, package access, combo assembly. Pre-registered metrics, CI95s and limitations come with each result, and differences inside the noise are reported as *no detectable difference*. Scripted stress scenarios ask how the deck recovers when the commander is removed twice, the board is wiped, or the colours or lands are screwed. There is no multiplayer win-rate simulation, because opponent-dependent claims never become simulated percentages.
5. **Decide with a person.** A change needs evidence beyond diagnostics (the decision rule), a disposition with refs, and Cory's approval. APPROVAL_READY, APPROVED and CANONICAL_LOCKED are separate states ([authority model](grixis/Grixis%20Authority%20Model.md)).

**Rules of thumb** (guidance, labelled as such):
- Count what the commander *does*. If a slot wouldn't change with a different commander of the same colours, it is a staple slot. Fill those slots for function, at the bracket's level.
- Prefer redundancy for the identity core over raw power elsewhere. A blueprint package below its minimum count is a bigger problem than one weak card.
- Plan for the commander's removal. The stress records show a median cost of about 2 commander turns per removal across the 62 Grixis decks. A deck that needs its commander every turn needs protection, a cheap recast curve, or a backup engine.

## What the evidence can and can't say

| Question | Evidence | Can it decide? |
|---|---|---|
| Is the card legal in this deck? | CR 903.5 + Scryfall legality (`fact`) | Yes (hard rule) |
| Does it interact with the commander? | Oracle text, interaction review (`fact`), regex hook (`heuristic`) | Facts support a decision; the hook is a pointer |
| Do builders pair it with this commander? | EDHREC lift / inclusion (`derived_metric`) | No: diagnostics only |
| Does the list develop better with it? | Paired goldfish record (`test_result`) | Supports a decision, within the model's limitations |
| Does it win more games? | Not simulated (opponent-dependent) | Not claimed |
| Is the change accepted? | Cory's approval record | Yes (the only approval) |

## Sources

- Comprehensive Rules, section 903 (Commander), quoted verbatim above from the cached CR.
- Wizards of the Coast, [Commander format page](https://magic.wizards.com/en/formats/commander) (format description, colour identity, command zone, brackets, Game Changers).
- Wizards of the Coast, [Commander Brackets Beta Update – October 21, 2025](https://magic.wizards.com/en/news/announcements/commander-brackets-beta-update-october-21-2025) and [February 9, 2026](https://magic.wizards.com/en/news/announcements/commander-brackets-beta-update-february-9-2026).
- EDHREC on lift and synergy, see [EDH Lift and Synergy → Sources](EDH%20Lift%20and%20Synergy.md#sources).
- Companion records: `data/grixis/blueprints/`, `data/grixis/evidence/`, `data/grixis/tests/`, `data/grixis/stress/`.
