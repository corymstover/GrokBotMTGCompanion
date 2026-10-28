# Deck #48 — Saruman, the White Hand M7 Rev1 — owner review only

**NOT OWNER-APPROVED. NOT CANONICAL. NO LOCK OR APPROVAL STATE MUTATION.**

- Cycle: `global-restart-2026-10-13`; canonical archive: `corymstover/grixis-commander-encyclopediaGPT/main`.
- Preserved October 15 approved 100-list SHA-256: `4981499230898c8b36c6f46b0f60a5277630d92abe477d48ed77091e2203ffe2`.
- October 27 M7 Rev1 proposed 100-list SHA-256: `dbf71bc86caec1be73c4333bf43e4104cccb5f91a06d2766e8b586adabd9724b`.
- Versioned source and proposed list: `Saruman_Approved_2026-10-15_Preserved_Source.txt` and `Saruman_M7_Rev1_Candidate_2026-10-27.txt`.
- Proposed bracket: **4 — Optimized**; no project exceptions. Tags **Spellslinger / Amass / Orc Army**.
- Review is a whole-99 challenger pass, not a claim that seven swaps were forced by a quota. Existing M6 comprehensive KEEP judgment and its risks were re-examined; this M7 review prefers a different, more cast/Army-driven play pattern.

## Strategy judgment: seven exact swaps

| CUT | ADD | Why this is a Commander-first upgrade; honest cost |
|---|---|---|
| Kazuul's Fury // Kazuul's Cliffs | **Valakut Awakening // Valakut Stoneforge** | Maintain a red MDFC/35 land-capable slots. Fury sacrifices the Army as an **additional cost** before Saruman can enlarge it; Awakening is a castable noncreature instant that improves a clunky hand and triggers amass 3, while its land face retains red access. Lost: emergency fling-type finisher when a huge Army already exists. |
| Black Waltz No. 3 | **Tainted Strike** | Strike turns the actual built-up Orc Army into an instant-speed infect finisher. When an Army with 10+ power deals damage to an opponent, ten poison counters are lethal; combined with **Chandra's Ignition**, infect damage can reach every opponent. Strike itself triggers a Saruman amass1 on cast. Lost: the repeatable 2-per-opponent noncreature ping of the 4-drop creature; Strike requires an Army and a successfully resolving damage effect. |
| Commence the Endgame | **Mind's Desire** | Both have MV6; Mind's Desire supplies storm copies that exile playable top cards and permit **casting** them free, generating additional Saruman triggers for noncreature hits. It transforms a costly amass+draw spell into a genuine multi-spell turn. Lost: uncounterable instant draw2/amass to hand size; storm copies themselves are NOT cast and do NOT trigger Saruman. Need meaningful earlier spell count, and free X spells set X=0. |
| Sauron, the Dark Lord | **Arcane Bombardment** | Replaces a 6-MV **creature** that does not trigger Saruman on cast with a 6-MV **noncreature** that immediately amasses6. On later turns the enchantment casts copies of exiled instant/sorcery cards from a graveyard, giving Saruman fresh amass triggers. Lost: powerful flavorful back-up threat and extra card selection; Bombardment is slow, random at first, relies on a graveyard, and its first-spell-per-turn trigger is not retroactive. |
| Feed the Swarm | **Chaos Warp** | Upgrade sorcery-speed creature/enchantment answer to instant-speed any-permanent answer, including indestructible/exile-sensitive threats. Both are noncreature casts; Saruman amasses 3 instead of 2. Lost: unconditional destruction when Feed is valid; Warp can reveal and deploy another permanent for the opponent. |
| Mana Geyser | **Temporal Trespass** | Mana value **11** for Saruman even after delve lets a stocked graveyard plus UUU produce an 11-counter Army burst and a **full extra untap/attack turn**. This makes the huge Army immediately actionable. Lost: Geyser's occasional enormous red-mana burst; Trespass needs UUU, graveyard fuel, and competes with Treasure Cruise, Dig Through Time and Mizzix's Mastery. This is the closest tradeoff: choose the stronger commander-specific payoff at cost of red storm funding. |
| The Ozolith | **March of Swirling Mist** | Replace post-death counter recovery that waits for a future attacking creature with live instant-speed phase-out protection for **both Saruman and the Army** against destruction/exile/bounce, or phase blockers for lethal. Chosen X contributes to mana value on stack; blue pitch can reduce actual payment. Lost: permanent counter salvage when Army dies and a later creature can attack. |

## Why these and not familiar homogenizing alternatives?

- Preserve **Volcanic Salvo** (MV12, discounted only by creature power measured before its Saruman trigger), **Blood for the Blood God!** (actual MV11, not eight), **Blasphemous Act** (MV9), and **Treasure Cruise/Dig Through Time** (delve keeps MV8); these are Saruman's unique high-MV, low-actual-cost strengths.
- Preserve actual Army support: **Fall of Cair Andros**, **The Great Goblin**, **Mauhúr**, **Orcish Siegemaster** (trample), **Bothersome Noisemaker**, **Harmonic Prodigy**, **Veyran**, **Wizard's Staff**, **Soul's Fire**, **Chandra's Ignition**, **Widespread Brutality**, **Orcish Medicine** and **The Black Gate**.
- Reject generic Thassa's Oracle/Consultation, Ad Nauseam, Breach/Brain Freeze, independent Ob Nixilis/Red Terror or off-plan tutor packages. A strong Saruman deck should win because its noncreature casts build a huge protected Army and convert it to lethal damage, not because it wears a Grixis combo shell.
- Arcane Bombardment and Mind's Desire are distinct from **Storm of Saruman**: actual instructions to **cast copies of cards** or **cast exiled cards** make new Saruman triggers. Copies of *spells* simply placed onto stack do not.
- Seven swaps were selected for concrete roles after comparing all 99 library slots, not from an arbitrary minimum or a model score.

## Re-verification and evidence boundaries

- A bounded independent source→candidate parser passes **100 physical / 97 distinct / Island2, Mountain2, Swamp2 only / 31 printed lands + four spell/land MDFCs / seven exact one-for-one substitutions** and refuses any source or candidate hash drift.
- A separate GitHub Action attempts a **current live all-card Scryfall collection audit**: 97 unique Oracle identities, Commander legalities and UBR color identity. This step must PASS before final owner approval; it is not implied to have passed merely by staging this review.
- No claim of measured win-rate uplift, complete M6 certification, independent third-model Pass C, or M8 milestone acceptance.
- Verify one particularly important combo explicitly: with an Orc Army as Chandra's Ignition's legal creature target and Tainted Strike resolving to give that Army infect, Chandra's Ignition deals damage from the Army to each opponent, thus poison counters rather than normal life loss. Opponents may respond to remove/phase/exile the creature or neutralize spells; it is not a deterministic unconditional win.
- Temporal Trespass: delve does not change printed MV11, but the **UUU colored floor** remains. Its extra turn gives a new combat, not an immediate additional combat that same turn.
- March of Swirling Mist: selected X contributes to mana value on the stack; alternate exile of blue cards reduces generic payment only. A targeted phased creature is treated as absent until phase-in; in particular do not claim a phased Army can attack immediately.
- Document inherited technical errata (do not restate the incorrect source): Blood for the Blood God! MV11; The Black Gate targets only a creature, highest-life eligible player chosen at resolution; Volcanic Salvo reduction uses total existing creature power locked when cast.
- Card Oracle/legality evidence: [Saruman EDHREC](https://edhrec.com/commanders/saruman-the-white-hand) used for *candidate discovery only*, [official Wizards banned list](https://magic.wizards.com/en/banned-restricted-list); primary card references [Tainted Strike](https://scryfall.com/card/som/80/tainted-strike), [Valakut Awakening](https://scryfall.com/card/znr/174/valakut-awakening-valakut-stoneforge), [Mind's Desire](https://scryfall.com/card/c21/123/minds-desire), [Arcane Bombardment](https://scryfall.com/card/otc/154/arcane-bombardment), [Chaos Warp](https://scryfall.com/card/eoc/49/chaos-warp), [Temporal Trespass](https://scryfall.com/card/frf/55/temporal-trespass), [March of Swirling Mist](https://scryfall.com/card/neo/61/march-of-swirling-mist).

**Approval boundary:** Await Cory's single explicit `Approve` for exact proposed hash `dbf71bc86caec1be73c4333bf43e4104cccb5f91a06d2766e8b586adabd9724b`, and only then undertake versioned canonical PR/merge/approval-record/lock and post-merge verification. Until then the October 15 canonical Saruman approval remains unchanged.
