# Evelyn, the Covetous — ChatGPT independent M7 Rev2 confirmation, October 23 2026

**STATUS: REVIEW READY, NOT OWNER APPROVED, NOT CANONICAL, NOT LOCKED.** This is a substantive independent audit of GrokBot [PR #666](https://github.com/corymstover/GrokBotMTGCompanion/pull/666), exact source head `8150b96898bcd4d8631ae80352b5f59ec158dbcf`. Five first-pass changes **survive** independent adversarial scrutiny. Identical final 100 bytes are preserved deliberately; a revision number does not imply manufactured extra swaps.

- Historical current-cycle canonical source: `refinement/decklists/Evelyn_the_Covetous_Approved_2026-10-14.txt` SHA **`1d602b5d9b2a370d3448816f593198212b2b83da74e92ccc3232798641b2588a`**. Do not modify.
- Re-fetched Grok proposed candidate raw SHA **`c3f6862c6f4498778069f45e7a5e5bc7efe92d70158b5e9b3f438c8c861b89ac`**. Our independently verified exact-copy 100 keeps identical bytes/hash (no unapproved normalization).
- All 100 card names selected from October 23 Grok's **live** Scryfall snapshot (100 original plus 97 candidate pool), verified Oracle IDs/text, current Commander legality and UBR identities. No exceptions. This is a validated archived source, **not** a later fresh Scryfall pull or a third independent model.
- Commander Evelyn ({2}{U/B}{B}{B/R}) flash Vampire Rogue: each Vampire entering exiles the top card of each player's library with a collection counter, then a **once-per-turn** permit to play a card thus exiled (normal land timing and limits). The Oct14 shell has **only Evelyn as a Vampire**, so adding a cheap second Vampire is commander-first even in a cEDH deck whose primary wins are independent.

## Five validated swaps, not a five-swap cap

| Add | Cut | Positive decision and genuine loss |
|---|---|---|
| **Marsh Flats** | **Thundering Falls** | Fetches Swamp-typed duals including Underground Sea/Watery Grave, untapped when cracked, improves Brainstorm shuffle and removes always-tapped land. Loses fetchable Island/Mountain surveil-one dual. |
| **Insolent Neonate** | **Spellskite** | At {R}, a second *Vampire* to trigger Evelyn's four-player collection exiles; a discard-then-sacrifice outlet for Worldgorger setup and a card back. Requires an actual card to discard; not a costless automatic loop exit. Loses 2-mana redirect protection for eligible creature/artifact targets. The owner's rejection applied to forcing an optimized tribal Vampire *package*, not to one independently functional combo discard outlet. |
| **Brainstorm** | **Redirect Lightning** | Extremely efficient {U} selection, access to a fetch shuffle, setup for Ad Nauseam/Consultation, retains expressly defended Ripples of Undeath. Loss: Redirect Lightning's single-target redirection when one red plus five life or {2} is payable, but the remaining deck still has free/paid counters, Hexing Squelcher and Defense Grid. |
| **Burnt Offering** | **Wan Shi Tong, Librarian** | One-black-mana instant sacrifices Evelyn (MV5) or Worldgorger (MV6) for B/R mana, enabling a combo turn and commander-responsive mana. Sacrifice requires a creature actually controlled, and Spellskite loss reduces some resilience. Loses Wan Shi Tong's Flash tutor-search trigger draw and late-game counter scaling. |
| **Verdant Catacombs** | **Blazemire Verge** | Second additional fetch for U/B and B/R Swamp-typed duals, enhances Brainstorm and early multi-color access. Loses reliable untapped black source and conditional red with no Stifle/search vulnerability. Closest of five, tradeoff disclosed. |

## Independent stress tests and stopping logic

1. **Protection adversarial test.** Candidate removes *both* Spellskite and Redirect Lightning. Their effect is narrow target-redirection, not free hard countering. It retains Force of Will/Negation, Flusterstorm, Swan Song, Mindbreak Trap, Pact of Negation, Mental Misstep, Pyroblast/REB, Stifle, Chain of Vapor, An Offer, Hexing Squelcher and Defense Grid. Nevertheless, opponents with targeted removal can now tax that package; owner must see this loss. Preserving both would require cutting owner-kept graveyard/draw/flash engines, or forgoing the new commander-specific Vampire trigger and Brainstorm.
2. **Vexing Bauble conflict.** Owner-kept Bauble counters spells cast with no mana actually spent, including our own alternate free Force of Will, Force of Negation, Pact, Mindbreak Trap and Gitaxian Probe cast by paying life; its {1} tap sacrifice is an available escape. No newly added free cast is falsely exempt.
3. **Worldgorger loops.** Need a legal enchantment/target, source of repeatedly tapping mana lands, and an actual exit; a loop with no optional exit can make game a draw. Repeated Evelyn ETB also exiles our own deck, so no statement of automatic limitless opponent exiles. Neonate may create an instant-speed exit only while on battlefield and a card can be discarded.
4. **Owner preservation.** Vexing Bauble, Ripples of Undeath, Saw in Half, Windfall + Notion Thief, Stifle, Mistrise Village, Leyline of Anticipation remain. Owner-removed Displacer Kitten, Otawara, Morphic Pool, Wheel of Fortune, The One Ring, Dragon's Rage Channeler, Cyclonic Rift, Deflecting Swat, Beseech the Mirror and forced Vampire tribal package remain excluded.
5. **Beyond-five search.** Tested credible plus-six candidates: Spell Pierce versus protected Ripples (would improve 1MV interaction but breaks explicit keep); Grim Monolith instead of Burnt Offering (two-mana colorless acceleration stronger before a creature enters, but does not feed the Worldgorger/Evelyn colored-sacrifice line); Intuition versus Praetor's Grasp (not a guaranteed one-card Breach combo without supporting recovery, extra MV), Vampire Hexmage/Bloodtithe Harvester (tribal broadening with weaker turbo impact), Daze (bad under own Bauble), Grief (disruptive but does not increase durable protection), Dispel (narrower hard counter than existing suite). No defensible specific sixth cut was found that improved natural-cEDH effectiveness without negating a protected owner choice or trading strong engine redundancy for another generic staple. **Five was a floor, never a cap**.
6. **Mana/source tests.** 26 lands and 100 singleton; fetches 7→9; model U/B/R colored land counts approx 19/19/19→20/20/19. The saved finite no-mulligan approximations for first-turn U and next-turn Evelyn are read as access *proxies*, not win rates. Blazemire and fetched lands have distinct risk profiles, Stifle cost explicit.

## Verification and tags

- 100 physical cards, 100 distinct names (only singletons), 26 lands, 19 Game Changers, commander UBR, official 100/100 Commander legal per saved Oct23 primary Scryfall selection, no project exception.
- Two Vampires including Evelyn + Insolent Neonate; archetype remains **cEDH turbo Worldgorger/Thassa's Oracle/Breach**, not Vampire tribal.
- Original **seven conditional Spellbook complete combo lines** remain; no new unsupported combo or automatic infinite. Games/win rates and independent third-model review not performed.
- **Power Bracket 5 — cEDH**. Archidekt tags **cEDH / Worldgorger Combo / Thassa's Oracle**.

## Approval protocol

These engineering artifacts are independent research and tests only. Before a canonical lock, present full exact 100 and source-bound SHA `c3f6862c6f4498778069f45e7a5e5bc7efe92d70158b5e9b3f438c8c861b89ac` to Cory, explain losses, and obtain exact owner approval. No implicit approval from earlier decks, no canonical changes or merge of the Grok shared stack.
