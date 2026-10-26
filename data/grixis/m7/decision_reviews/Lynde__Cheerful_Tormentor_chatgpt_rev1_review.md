# Deck #31 — Lynde, Cheerful Tormentor, M7 Rev1 independent whole-99 review (2026-10-25)

**State: PRECERTIFICATION / NOT OWNER-APPROVAL-READY.** This review does not change the approved October 14 canonical list. Respect the owner's 2026-10-25 certification-before-approval protocol. The Pass C Stage A seal mismatch for Lynde is preserved and unresolved; a documented versioned correction requires an explicit owner decision.

- Canonical approved baseline: `05d1c4eea023d25e4308f78b109e80b78e0a3f4d655c3df36743ba3afbf04166` (100 physical, 35 lands).
- Current proposed exact raw SHA-256: `6e088891b3c92b632d95e4b6dbd83ffedb06834f812e6728cc5bfa7bdc13556e`.
- Proposed physical: 100 cards, 96 distinct names, Island ×3, Mountain ×2, Swamp ×2 only repeats; 35 lands, Grixis identity, no project exceptions.
- Proposed 8 net swaps (five spell-engine, three mana base); 17 physical cards with a Curse face/type versus 21 in baseline. This reduction is material. The four cut Curses are replaced with direct Curse support and copying that reduces dependence on drawn individual Auras, not generic turbo combo.
- Current receipts: original 93 unique baseline Oracle names and five new spells from the Oct 23 live Scryfall batch in PR #679; three new utility lands individually checked via Oct 25 Scryfall pages. The attached index marks three incomplete full-card-text/ID records; a fresh exact-96-name full Oracle collection receipt remains a certification prerequisite.
- Power target: **Bracket 4 — Optimized**, commander-first Curse recursion, not a cEDH turbo shell. Archidekt tags: **Curses / Enchantress / Control**.
- No statistical win-rate or end-to-end rules-engine result is claimed.

## Eight additions and challenged cuts

| # | ADD | CUT | Independent judgment and cost |
|---|---|---|---|
| 1 | Court of Vantress | Cruel Reality | 4-mana monarchy and repeated Curse copies over 7-mana upkeep sacrifice Curse that can punish your own Lynde after recursion. Court only produces tokens while monarch, so Propaganda and table control matter. |
| 2 | Extravagant Replication | Curse of Death's Hold | Extra upkeep-triggered copies of actual Curses, nonland engines or Obeka; avoids the -1/-1 Curse killing your own support when attached back to you. Six mana and no immediate impact are serious costs. |
| 3 | Barrin, Master Wizard | Torment of Scarabs | Pay {2} and sacrifice your Curse as an **activation cost** to bounce a target creature, then Lynde returns the Curse at the next end step. Losing a 4-mana attrition Curse lowers Curse density; Barrin requires a legal creature target. |
| 4 | Into the Pit | Curse of the Restless Dead | Cast from top by paying normal spell cost plus sacrificing a nonland permanent, often a Curse that Lynde will recur. Replaces a 3-mana decayed-token Curse dependent on opponent land drops. Cannot use a land on top or evade timing restrictions. |
| 5 | Staff of Compleation | Nightscape Familiar | A reusable {T}, 1 life to destroy a permanent you own (including your Aura on another player), plus emergency mana/draw, versus a 2-mana spell discount. Staff is slower to deploy and usually once per turn without an untap effect. |
| 6 | Urza's Saga | Mountain | A land/enchantment that finds **Claws of Gix {0}** or **Despotic Scepter {1}** at chapter III, increasing access to the Curse recycling engine. Loses one unconditional red basic/source and naturally sacrifices itself. |
| 7 | Otawara, Soaring City | Island | Untapped blue source plus a channel bounce spell (can save Lynde or answer a key permanent); replacing a basic weakens the fetchable/basic count by one. Bounce to hand does NOT trigger Lynde's graveyard recursion. |
| 8 | Shizo, Death's Storehouse | Swamp | Untapped black source; {B}, {T} grants Obeka fear, improving the chance that her 2 combat damage yields two more upkeep steps for Lynde. Doesn't bypass black/artifact blockers; loses a fetchable basic. |

## Deliberate KEEP and challenged outsider judgments

9. **KEEP Curse of Misfortunes:** repeatable Curse tutor on its controller's upkeep (even when the enchanted player differs) is the principal density multiplier.
10. **KEEP Despotic Scepter and Claws of Gix:** both directly enable battlefield-to-your-graveyard movement of owned Curses; Saga increases tutor access.
11. **KEEP Braids, Arisen Nightmare / Demon of Fate's Design / Perilous Research:** distinct paid sacrifice windows and resilience, none displaced by speculative generic tutors.
12. **KEEP The Ninth Doctor, Paradox Haze, Obeka:** upkeep multiplication is the deck's unique strategic secondary axis; Shizo supports the hardest of these to trigger.
13. **KEEP Curse of Thirst, Curse of Fool's Wisdom, Curse of Obsession, Curse of Shaken Faith and Maddening Hex:** actual closing pressure, not incidental filler.
14. **KEEP Propaganda:** especially important to defending Court's monarchy; do not exchange protection for a generic value permanent.
15. **REJECT Court of Ambition for now:** a strong all-opponent upkeep attrition engine, but has no Curse-copy or recursion function, competing with the selected Court and existing finishing Curses.
16. **REJECT Balemurk Leech:** economical Eerie attrition, but Grim Guardian and Wicked Visitor already occupy payoffs; the scarce slots are more valuable as reset outlets.
17. **REJECT Displacer Kitten:** an interesting enchantment blink enabler, but relies on further noncreature spells, and copies/reassignments are not themselves Lynde graveyard events.
18. **REJECT Magmaw:** can sacrifice Curses for damage, but five-mana red-intensive fragile body plus {1} per trigger loses the efficiency comparison to Barrin/Staff/Claws.
19. **REJECT owner-removed Curse of Chaos and owner-rejected Strionic Resonator, Beseech the Mirror, Shadow of the Second Sun:** do not silently reverse owner decisions. None proved necessary.

## Two complete 100-card alternatives

`Lynde__Cheerful_Tormentor_ChatGPT_Rev1_Alternatives_20261025.json` contains both full lists, not sketches:

- **A (seven swaps, ramp-preserving):** Keep Nightscape Familiar; do not add Staff. Upside: easier early multispell turns and a faster turn-four commander; downside: one less proactive Curse reset and lower outlet redundancy.
- **B (six swaps, Curse-density-preserving):** Keep Torment of Scarabs and Curse of the Restless Dead; omit Barrin and Into the Pit. Upside: 19 Curse cards and more native attrition/fodder; downside: two fewer flexible methods to place real Curses in the graveyard on demand.

Both retain the exact canonical commander, the complete original mana-rock suite except selected changes, 35 lands, and the other immutable baseline names. Neither alternative is approved.

## Rules-first P0/P1 priorities and failure conditions

1. **C1/K1:** Lynde only triggers from owned Curse permanents entering **your** graveyard from battlefield; exile/bounce/mill and Curse tokens ceasing to exist do not produce repeatable original cards.
2. **K2/K3:** moving one Curse at each upkeep is optional, does not target, and grants exactly two draws if it moves. Ordering an upkeep copy engine before Lynde allows a new Curse token to be moved that upkeep.
3. **K4/K5:** Cruel Reality, Death's Hold and Torment can backfire when they return attached to you. Retained Fool's Wisdom/Surveillance/Unbinding ordering must still be assessed for trigger ownership, not deemed universally harmless without context.
4. **E1/E2:** Barrin's {2} and sacrifice are both paid before response; Staff requires untapped activation and 1 life; Into the Pit pays a sacrifice as additional casting cost; Urza's Saga tutor only {0}/{1} **mana cost**, not mana value alone. Obeka needs actual combat damage; Shizo fear isn't unblockable.
5. **W1/W2:** copy engines enhance the retained curse attrition route; Curse tokens that die cannot be returned repeatedly as cards. No claimed infinite loop or guaranteed lethal.
6. **F1/F2:** instant exile replacement effects can defeat Lynde's graveyard-return line; land/basic reductions and blue-pip increase are real costs.

## Evidence/provenance blocker

Existing sealed Stage A MD bytes (unchanged, git blob `b253ed9c`) SHA `02adfb85db19aa42d5dfe36b96906874ea1abd232b6f8bfc3861c1108035b72a` differ from the historical `seal.json` recorded `59f2dc10eedec5797f3f5dcfdb0a206b380a037e9b17a29e740d6ca94829c12e` by a final-newline hashing convention. This is analogous to Lord Xander's separately owner-authorized correction. Lynde has **no specific owner authorization** to correct its sealed evidence yet; do not edit or waive it, and do not certify while the checker rejects it. The source ledger and original seal stay intact.

## Outstanding before owner approval

- [ ] Obtain fresh complete Oracle name/ID/text/legality index including three lands.
- [ ] Run source-paid P0/P1 mechanical cases and mana/resilience scenarios on exact candidate SHA.
- [ ] Complete M6 I/J certification transfer, preserving the original Pass C seal and obtaining owner authorization for any versioned hash correction.
- [ ] Run exact-head GitHub Actions and attach green receipt for the exact candidate.
- [ ] Only then request explicit owner approval for the exact SHA.
