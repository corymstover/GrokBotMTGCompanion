# Deck #35 — Marchesa, the Black Rose — M7 Rev1

Status: **REVIEW_READY; OWNER APPROVAL PENDING.** Engineering evidence only. The October 15 canonical approval remains LOCKED and unchanged.

## Source authority and structure

- Canonical: `corymstover/grixis-commander-encyclopediaGPT/main`, `refinement/decklists/Marchesa_the_Black_Rose_Approved_2026-10-15.txt`.
- Original raw SHA-256: `627b07f6466c0a48f16daea58ee9c01bba02c2b7fb4de76a37b14a7f75ad7f9b`. The uploaded 2026-10-15 Archidekt ZIP reproduces the **exact** byte sequence when the first-line commander marker is restored. No historical source overwritten.
- Proposed exact 100 raw SHA-256: `c4857d176eaa6ed682da7cab974014d393fce2efe698bdca6994d77bb27ddf02`.
- Commander + 99, 98 unique names, 34 lands, only Island ×2 and Swamp ×2 repeat; no companions or special exceptions.
- 2026-10-26 Scryfall collection: 98/98 resolved current Oracle identities, Commander legal, all color identities within U/B/R; no banned cards or unresolved identities. 5 Game Changers (Ancient Tomb, Cyclonic Rift, Demonic Tutor, Fierce Guardianship, Vampiric Tutor).

## Commander-first objective

Protect Marchesa's distinctive engine: dethrone or noncombat counters before a creature dies, free sacrifice outlets, next-end-step returns, ETB/death value and persist resets. It stays a **Bracket 4 — Optimized** counter/aristocrats/combo list, not cEDH goodstuff.

The earlier October 19 M6 deep review individually adjudicated all 99 slots, 129 M5 swap comparisons, 260 EDHREC vectors and 11 source-supported interactions. This independent M7 judgment revisits the full live 99 with fresh October 2026 card discovery and new-release Oracle; previous decisions are evidence, not a locked optimization result.

## Seven decisive one-for-one swaps

| Add | Cut | Why better for Marchesa | Material opportunity cost |
|---|---|---|---|
| **Curse-Marred Demon** | Braids, Arisen Nightmare | Four-mana flying creature tutors a card on each ETB, so Marchesa returns turn a threatened Demon into further searches. | Requires RR; random discard can lose the fetched card; loses Braids' end-step sac/draw pressure. |
| **The Ooze** | Deadly Dispute | Two-mana persistent engine converts each countered creature leaving into Mutagen artifacts; those pre-seed new counters and fuel artifact-death payoffs. Its tap ability also exiles a graveyard card for a Mutagen. | Mutagen activation costs 1 and is **sorcery speed**; loses an instant sacrifice, two immediate cards and Treasure. |
| **Withering Torment** | Feed the Swarm | Instant-speed creature/enchantment removal, fixed 2-life loss instead of mana-value-scaled loss, retains critical enchantment answer coverage. | Costs 3 instead of 2; sometimes the one mana matters. |
| **Accursed Marauder** | Fleshbag Marauder | 2 rather than 3 mana for repeatable ETB nontoken edict. Opponents cannot feed it a token; its Zombie typing stays compatible with Mikaeus' non-Human undying. | Cannot force sacrifices of only-token boards; no planeswalker edict. |
| **Aether Channeler** | River Kelpie | Three-mana Wizard that can recur as draw, bounce or a flying token, and Sage of Fables supplies it a counter. Reduces the five-mana curve. | Loses Kelpie's persist and broad graveyard-cast/ETB draw engine; less explosive during infinite persist cycles. |
| **Voldaren Thrillseeker** | Syr Konrad, the Grim | Three-mana backup 2 distributes counters or enables a sacrifice-damage effect; naturally loops through Marchesa if countered and yields immediate focused reach. | One mana per sacrifice, targeted damage and no global graveyard-movement drain; weaker without counter/recursion. |
| **Madame Null, Power Broker** | Twilight Diviner | Three-mana repeatable +1/+1 counter on other creature ETBs, including from Marchesa/persist, enabling the next round of deaths and returns without combat. | Pays life equal to incoming creature power, can be costly; loses Diviner's surveil and once-per-turn creature token copying. |

This proposal retains **Flayer of the Hatebound**, **Gray Merchant**, **Mikaeus**, **Glen Elendra Archmage**, **Puppeteer Clique**, **Murderous Redcap**, **Sage of Fables**, **Thran Vigil**, **Gev**, **The Ozolith**, **Unspeakable Symbol**, all Altars, and the other core free sacrifice outlets. It retains 34 lands and six existing repeatable nonland mana rocks, without introducing additional colorless lands.

## Alternative packages and open-ended research

- Complete 8-swap alternative: add Rhystic Study, cut Grim Haruspex *in addition* to seven; raw SHA `b2e1cde4f760e9733eea451e86487c31304e59919651aa2e941656231f5d53a0`. Rejected: strong generic draw, but replaces a death-trigger creature that itself receives Marchesa recursion and supplies cards during sacrificing.
- Complete 9-swap alternative: also add Dictate of Erebos, cut Grave Pact; raw SHA `3d492e6a78c4c5f579ef486db4463b16c7dadc84b1365561a73af56816bda75c`. Rejected: Dictate flashes in and has easier black pips, but costs five versus Grave Pact's four and impairs the lower curve.
- Additional post-floor challenger: Vigean Graftmage over The Ozolith; rejected because a three-mana creature requires further mana/turns to move limited counters, while Ozolith automatically banks counters from any leaving countered creature. The Ooze **pairs with**, rather than replaces, Ozolith.
- Additional challenge: Spymaster's Vault over Sulfurous Springs; rejected because Vault can enter tapped and is mono-black, reducing already relatively thin red access, while its connive demands black mana and tapped activation.
- Other judged but unselected: Plaguecrafter (Human excludes Mikaeus undying; Accursed Marauder cheaper), Ravenous Chupacabra (four-mana targeted destroy cannot hit indestructible/hexproof), Lazotep Quarry (colorless land/sac activation displaces High Market's life gain), Kaya's Ghostform (one-use protection vs reusable Greaves), Dauthi Voidwalker (generic graveyard hate, less commander-centric), Necropotence (strong but replaces Marchesa-specific draw and life budget).

Seven is the quality-derived stopping point, not a cap. Further challengers either increase colored-mana/life pressure, remove protected compact win interactions, or replace repeatable Marchesa bodies with standalone staples. This is an authored portfolio judgment, **not** an exhaustive proof or randomized win-rate advantage.

## Mechanical cautions and scope of verification

1. Marchesa only triggers for controlled creatures dying **with a +1/+1 counter already present** while Marchesa's relevant ability functions; return is at the *next* end step. A Sneak Attack end-step sacrifice doesn't imply immediate same-step return. Exile in response defeats a graveyard-return line.
2. Madame Null's trigger is optional but each payment is real life equal to creature power. Its placement after a persist creature enters cancels opposite-sign counters only once both exist; no claim that paying life is free or that the creature always loops.
3. Mutagen tokens from The Ooze are artifacts with `{1}, {T}, sacrifice: put a +1/+1 counter`, **activate only as a sorcery**. The Ooze itself cannot prevent a sudden removal spell using a newly created Mutagen at instant speed.
4. Accursed Marauder forces nontoken sacrifices; itself may be sacrificed, and Mikaeus gives it undying because it's a non-Human. If a +1/+1 counter is already on it, undying doesn't trigger on that death.
5. Voldaren's backup counter placement targets a creature. If it targets another creature, that creature temporarily gains the printed sacrifice-damage ability; activating requires paying `{1}`. Sacrifice-damage is last-known power, not arbitrary unlimited damage.
6. Curse-Marred Demon's ETB tutor is **not unconditional retention**: shuffle and then discard a random card. It needs a way to acquire +1/+1 before dying for Marchesa return; double-red access is a real stress point.
7. Aether Channeler makes a white Bird token without a white mana symbol in its Oracle text and is legal in U/B/R identity.

This review reuses the M6 Commander blueprint's 16 case groups as focused analysis, and acknowledges that earlier finite test receipts do not transfer as a new formal sealed M6 I/J certificate. Live Scryfall legality/Oracle and exact structural gates **pass**; no full rules-engine simulation or multiplayer win rate is claimed.

**Power Bracket:** 4 — Optimized

**Archidekt tags:** +1/+1 Counters / Aristocrats / Combo

**Approval boundary:** This is a staged owner proposal only. Canonical SHA `627b07f…` stays approved/locked until Cory explicitly approves the new *exact* `c4857d…` 100-card candidate, after which the scoped canonical PR and post-merge verification may occur. One approval is sufficient.
