# Abaddon — commander-first Grinning Ignus / Birgi challenger adjudication

**Date:** 2026-10-21 America/Chicago. **Source:** frozen approved Abaddon 100, SHA-256 `2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf`. **Authority:** approved/locked remains untouched; this is bounded M6.6/M6.7 engineering research, not a new M7 owner decision or I/J certificate.

## Why this candidate merits closer review than its M5 ranking

The source `data/grixis/m6/review_packets/abaddon-the-despoiler.json` contains **98 screening records, only 63 distinct proposed additions**. This inventory contains many nonsensical protected-core cuts, e.g. swapping Birgi/Kessig Flamebreather for creature-only value, or losing Lotus Petal/Rite of Flame to add Grinning Ignus. The original comprehensive author review and owner-equivalent Pass C mentioned Birgi/Ignus as a creature-cast storm loop but stopped at not having a strong enough immediate outlet. The **Abaddon-granted cascade on *each* Ignus hand cast** is a commander-specific outlet in a way not captured by a generic combo-count proxy. That is a material new comparative hypothesis, not proof of actual performance.

`data/grixis/m6/phase_b_plans/abaddon_ignus_birgi_20261021.json` was committed *before* the executable witness at commit `499a9700f36f90c77143a51fb4891a9b5f61f0ff`. It binds the approved physical card identity, immutable 99-card source, existing Birgi, commander-first payoff cards and exactly three unapplied one-slot Ignus challengers. Tests are finite **mana and trigger accounting**, NOT a sampled or complete multiplayer game.

## Exact spell/mana sequence and Abaddon cascade

Grinning Ignus is a {2}{R} creature. Its **{R}, return it to its owner's hand** activation generates **{C}{C}{R}**, activates only at sorcery speed, and is still a **mana ability** that does not use the stack. Wizards' Strixhaven release notes verify this, including that after a normally cast Ignus resolves, you can activate its ability before opponents gain another priority window *if nothing else triggered on entry*. (Birgi itself triggers on *spell cast*, so its trigger must resolve before Ignus resolves.)

With **Birgi's front face** already present, each Ignus cast triggers a delayed-on-stack **{R} mana creation** upon resolution of Birgi's trigger (not a mana ability); Birgi's red does not empty at phase boundaries that turn.

Finite witness starting from Birgi and Ignus on battlefield in your main phase, an available red mana and no restrictions:

1. Spend {R} to return Ignus to hand, generating {C}{C}{R}.
2. Spend {C}{C}{R} to cast Ignus from hand.
3. Resolve Birgi's triggered {R}, then Ignus. You again have Ignus on the battlefield and {R} available.
4. Repeat while the involved permanents and legal sorcery window remain. This produces repeatable *creature casts*, ETBs/LTBs and storm count at **net zero mana** per iteration. It does NOT inherently create infinite free mana, a damage outlet, or a win.

If **Abaddon** is controlled during your turn and opponents have already lost **three or more total life that turn**, each Ignus cast **from hand** (mana value 3) additionally **has cascade**. Every such cast is a new trigger independent of any cards previously cast; it may reveal a lower-MV nonland card and give permission to cast it without paying its mana cost. Real cascade hit availability, legal targets, cast choices, reactive plays and resolution are intentionally not simulated. A card *put onto the battlefield* by an effect is NOT the same as casting it from exile. A cascade trigger is not, by itself, a cast from exile.

The current list already includes **The Lost and the Damned, Prosper, Tome-Bound, Keeper of Secrets, Passionate Archaeologist** and **Brain Freeze**. On properly cast cascade spells from exile, their nonhand-cast benefits may amplify this loop; their actual payoff effects and deck-win conversion are not simulated. **The Lost and the Damned does not trigger on the Ignus casts from hand themselves.** The deck must still produce that initial three life loss on a turn when Abaddon is controlled.

**Important defensive/adverse conditions:**
- Without Birgi's FRONT creature face, the neutral mana loop stops after one recast under the fixed initial-red witness. Its back artifact face Harnfel does not replace Birgi's red-cast trigger.
- If X is below 3, the base Birgi/Ignus storm loop exists but Ignus receives **no cascade** from Abaddon; if Abaddon is not on the battlefield it also receives no such cascade.
- **Rule of Law** or **Arcane Laboratory** stops repeated Ignus recasts during the same turn after the first spell. Activated bounce is not itself a spell.
- **Nightscape Familiar** (in the approved list) reduces Ignus's generic casting cost by {1}. Alongside Birgi, this can make each iteration net **one additional {C}**; cutting Familiar for Ignus forfeits this third-piece synergy and other commander spell reductions.
- Commander removal, creature removal in the loop's cast/trigger window, countering Ignus, hand disruption and loss of one red stop or interfere with the line. Sorcery-speed reentry and commander mana/setup are substantive early-turn limits.

Official/reference card texts: https://media.wizards.com/2021/downloads/STX_Release_Notes/EN_MTGSTX_FAQ_04122021.pdf ; https://media.wizards.com/2021/downloads/KHM_Release_Notes/EN_MTGKHM_ReleaseNotes_20210113.pdf ; https://mtg.wtf/card/40k/171/Abaddon-the-Despoiler ; https://mtg.wtf/card/eld/203/Stormfist-Crusader ; community two-card loop at https://casualplaneswalker.com/combo/birgi-god-of-storytelling-harnfel-horn-of-bounty/grinning-ignus/.

## Separate threshold candidate: Stormfist Crusader

At the **beginning of your upkeep**, Stormfist Crusader makes **each** player draw and lose one life. At a normal four-player table, the three opponents lose a **total of 3**, exactly satisfying Abaddon's MV3 Ignus hand-cascade threshold that turn if Abaddon is in play and survives. **Each opponent draws a card**, so this supplies the enemy table three cards against your one. It is a source-verified zero-combat threshold engine but has a real multiplayer card-disadvantage burden. The M5 **Stormfist-for-Wheel-of-Fortune** cut destroys a core Breach/storm refill outlet and is not justified.

The deck already has other direct same-turn threshold sources (Boltwave, Flame Rift, Loyal Subordinate, Thermo-Alchemist), so Crusader is **HOLD**, not an automatic low-MV addition.

## One-slot incumbent-cut comparison (ALL UNAPPLIED)

| Hypothetical candidate | Identity advantage | Real cost |
|---|---|---|
| +Grinning Ignus / -Rakdos, Lord of Riots | Adds neutral Birgi storm loop; Abaddon might grant repeated cascade without Neheb/Loyal/Assault four-piece board | Removes a six-power flying/trampling creature and opponent-life-loss-scaled generic discounts for 17 *potential* creature identities, including commander recasts; this is the same contested slot for Assault and Warp |
| +Grinning Ignus / -Nightscape Familiar | Retains Rakdos creature discount; lowers nominal casting/setup curve | Removes cost reduction for U/R spell chains, including an Ignus synergy that turns its Birgi loop from mana neutral to colorless positive |
| +Grinning Ignus / -Rite of Flame | An earlier M5 screened pair, but with all core permanents intact | Removes one-mana immediate red acceleration needed to cast Abaddon or other red engine pieces early; turns one-shot tempo into a setup-dependent creature |
| +Stormfist Crusader / -Wheel of Fortune | Own-upkeep threshold 3 for Abaddon and one extra card to pilot | Opponents collectively get three cards per trigger; removes seven-card instant refill and Breach/storm graveyard fuel |

Other finalist challengers retain their earlier bounded positions: Aggravated Assault is a real conditional Neheb/Loyal option, not a proven stronger slot; Chaos Warp is a genuine stax answer, with existing Otawara-channel reservations and on-identity incumbent costs; Lotus Bloom is an MV0 cascade/suspend source with no normal hand cast and loses immediate Familiar discounts if that is its cut; Repercussion + Blasphemous Act risks lethal *self* damage to this creature-based Abaddon board; Chimil is a six-MV end-step exile-discover payoff with a major six-mana setup and the proposed cut of Call Forth the Tempest removes native printed cascade.

**Interim authored conclusion: PRIORITIZE Grinning Ignus as the leading unresolved off-list-identity challenger, but HOLD all swaps.** Its potential for repeated Abaddon cascade is a meaningful discovery; the legal loop alone does not establish that replacing Rakdos (or any other incumbent) improves actual games. The next experiment that could change this decision must model real paid early-turn assembly with Abaddon's colored mana, initial loss access, Birgi front face, competing cast/fetch/shuffle paths, actual under-3 cascade targets and opponent interruption. Do not present a new 100-card replacement as approved without that evidence, updated legal/Oracle checks and Cory's explicit full-deck approval.

**Project authority:** 100-card canonical baseline unchanged, M6.6/M6.7 remain PARTIAL, M6 formal certificates 0/62, M7 new owner decisions 0/62; GPT-6 owner-equivalent Pass C remains 62/62 under the documented narrow waiver. No win rate, actual successful cascade cast total, real Stormfist card advantage or net upgrade measured here.
