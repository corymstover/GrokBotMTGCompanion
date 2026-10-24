# Deck #25 Kefka, Court Mage — independent M7 challenger research checkpoint

Date: 2026-10-24 (America/Chicago). **RESEARCH_ONLY. No owner-presentable M7 list, no new owner approval, no canonical change.**

## Authority and provenance

- Canonical main historical October 14 deck: `corymstover/grixis-commander-encyclopediaGPT/refinement/decklists/Kefka_Court_Mage_Approved_2026-10-14.txt`; **100 cards**, **28 printed lands**, **100 distinct**, no terminal LF, raw SHA-256 `cd36192fedda7a4f54570fb8b8e4605147b40f9254e6985729097fc998f17b03`. Historical APPROVED/LOCKED; not yet a NEW M7 lock.
- Grok preliminary research [PR #673](https://github.com/corymstover/GrokBotMTGCompanion/pull/673), exact head at this checkpoint `ee2abd0a4f9c4729371c16233c5979c1331ae1a8`, proposed **only +Dualcaster Mage / −Culling the Weak** (research, not approved); **12 staged 100s** and 228-card archived Oct23 Scryfall audit. Do not merge the stacked Grok PR.
- Independently discovered EDHREC commander-specific High Lift candidates after reading current [Kefka cEDH commander page](https://edhrec.com/commanders/kefka-court-mage/cedh) and [combo variant](https://edhrec.com/commanders/kefka-court-mage/cedh/combo). High Lift and popularity are discovery, not intrinsic power proof.
- Independent research stages **34 complete exact-100 alternatives, including normalized baseline, pairings and explicit stress versions** in `data/grixis/m7/independent_candidates/Kefka__Court_Mage_M7_*Research_20261024.txt`. The companion `Kefka__Court_Mage_M7_Independent_Oracle_Index_20261024.json` pins **108 archived Scryfall source names** plus two separately sourced cards—Chameleon and Irma—from official Wizards/Gatherer research. Neither external card is retroactively represented as an Oct23 Scryfall snapshot entry; eventual promotion requires a fresh whole-deck legality check.
- Kefka-only waiver **does not exist**. The ordinary five-swap minimum applies if an owner-ready M7 candidate is ever presented. Never pad.

## Commander and baseline challenge

`Kefka, Court Mage // Kefka, Ruler of Ruin` is `{2}{U}{B}{R}` and is a Human Wizard. Kefka's **enter and attack** triggers each ask every player to discard one card, then draw per **different card type** among the cards discarded *in that trigger*. A transformed Kefka costs `{8}` at sorcery timing and rewards opponents' actual life loss during the controller's turn; this isn't a front-face turbo shortcut.

Keep the owner-approved original identity: `Harmonic Prodigy`, `Essence Flux`, `Displacer Kitten`, `Anger`, `Arena of Glory`, `Gogo, Mysterious Mime`, `Molten Duplication`, `Phantasmal Image`, `Phyrexian Metamorph`, `Saw in Half`, `Tinybones, Bauble Burglar`, `Waste Not`. Preserve fast mana and genuine Oracle/Breach win-line access. Existing Oct14 owner cuts of generic tribal, discard drain, expensive draw and bounce-combo packages stay respected. **Fresh inspection of the [historical owner decision ledger](https://github.com/corymstover/grixis-commander-encyclopediaGPT/blob/main/refinement/decisions/Kefka_Court_Mage_Current_Cycle_Decisions_2026-10-14.md) confirms that Demonic Counsel was consciously ADDED over Opposition Agent for proactive tutor density, and the cheap Image/Metamorph clones were deliberately ADDED/RETAINED. Their replacement therefore needs explicit comparative justification, not a stale-rank autopick.**

## New hypotheses requiring independent whole-100 judgment

### 1. Chameleon, Master of Disguise — **genuinely overlooked; promising, not certified**

- **Official source** [Gatherer MSC #148](https://gatherer.wizards.com/MSC/en-us/148/chameleon-master-of-disguise), [Scryfall MSC #148](https://scryfall.com/card/msc/148/chameleon-master-of-disguise) and Wizards' [Spider-Man mayhem design notes](https://magic.wizards.com/en/news/feature/spider-man-swinging-into-design). Not among Grok's archived 228 candidates.
- Normal `{3}{U}` creature; mayhem `{2}{U}` from graveyard **only if discarded that turn**, with regular creature casting timing. Chameleon may enter as a creature you control and **keeps Chameleon's own name**, so a Kefka copy remains on the battlefield beside original Kefka without the same-name legend-rule collision. This potentially compounds ongoing attack triggers, unlike one disposable copy.
- **Direct Kefka interaction:** Kefka's own discard can move Chameleon from hand to graveyard, permitting a discounted mayhem cast *that turn* in a legal main phase. **Vital caveat:** Kefka already costs five; from a fresh hand, casting Kefka and Chameleon mayhem together ordinarily needs **eight mana total**, before other acceleration. If Chameleon was discarded on Kefka's earlier turn and not cast that turn, mayhem is no longer available next turn simply because it remains in graveyard. The trigger does not allow casting during its resolution or bypass sorcery timing.
- Staged over `Demonic Counsel`; **material loss:** an eventually broad **two-mana {1}{B} tutor** enabled by delirium. The candidate is not assumed better merely from high EDHREC lift.

### 2. Flesh Duplicate — **strong low-cost direct commander clone, cut disputed**

- Existing frozen source: `{U}{U}` 0/0 that enters as another creature, except it has **vanishing 3** if source lacks vanishing. A Kefka copy immediately produces an ETB trigger (twice with Harmonic Prodigy), then the controller must resolve the **same-name legend rule**. It is *not* a persistent second Kefka, unlike Chameleon.
- Much lower mana value than many clones, but double blue is real colored demand and vanishing is real eventual sacrifice. Staged over `Demonic Counsel`, with the same tutor-density loss. Competes with Chameleon and Glasspool for the same vulnerable slot; these are **alternatives**, not three independent upgrades.

### 3. Glasspool Mimic // Glasspool Shore — **spell/land flexibility, tempo caution**

- Frozen Oct23 Scryfall verifies Commander legal, `{2}{U}` front-face copy of creature **you control**; land back is a **tapped-only blue** mana source. Copying Kefka produces an ETB trigger but does not evade the legend rule.
- Over `Demonic Counsel` it leaves 28 printed land-front cards plus one MDFC playable as a 29th land mode, potentially helping five-mana deployment, but a tapped land in cEDH exact-color windows is a real cost and the front-face can be dead without a creature. Do **not** count its spell face as guaranteed land or its land face as an untapped blue source.
- Evaluate separately from Flesh/Chameleon; do not count multiple candidates for one cut.

### 4. Generator Servant — **real Kefka mana+haste but needs a turn**

- `{1}{R}` creature; `{T}`, sacrifice it for `{C}{C}`; if **any** of the produced mana is spent on a creature spell, that spell's creature gains haste. [Wizards' September 2026 updated wording](https://magic.wizards.com/en/news/announcements/reality-fracture-update-bulletin) resolves the spend-any-mana ambiguity.
- Cast on turn two, untap on turn three, sacrifice for two generic toward five-mana Kefka **and haste**, provided three lands/other sources pay the U/B/R colored requirements. This can yield enter **and attack** Kefka triggers in the same turn. Cannot normally tap the turn it enters without other haste.
- Staged **over Culling the Weak**, the exact slot already used by Dualcaster in Grok's candidate: they are competing alternatives, not two addable independent swaps. Culling remains a fast `{B}` ritual if a creature is available; Servant requires advance deployment and is more vulnerable to creature removal.

### 5. Dualcaster Mage — **conditional combo package, not free value**

- Grok's one researched swap: `+Dualcaster Mage / −Culling the Weak`. Its flash Wizard ETB can copy existing `Molten Duplication`, `Saw in Half` or `Essence Flux` loops, with conditional Kefka ETBs if Harmonic Prodigy gives an extra copy trigger.
- Molten Duplication can make many hasty Dualcaster copies **without Kefka**. This is a serious owner-direction concern because it introduces a generic win line, though one slot synergizes with three already approved Kefka cards; no automatic acceptance.
- Culling's real loss includes potential net black mana and sacrifice interactions. Adding Dualcaster does **not** by itself make the three combo partners automatically accessible in hand.

### 6. Fire Covenant — **possible preservation upgrade, asymmetric loss**

- Staged `+Fire Covenant / −Toxic Deluge`. Instant selective damage can kill Drannith or blockers while retaining a five-mana Kefka and follow-up attack, but each point of damage requires one life and cannot solve untargetable/indestructible threats the way Deluge's -X/-X can; from hand it requires B/R rather than one B. It is Commander-legal in the frozen Oracle source.
- Similar tactical argument to Jeleva, but this is evaluated on **Kefka's whole 100 independently**. An earlier deck's accepted change never forces a later commander to adopt it.

### 7. Naban, Dean of Iteration — **ETB doubler; lower priority**

- Two-mana Wizard increases triggers caused by Wizard ETBs, including Kefka; does **not** multiply Kefka's **attack** trigger. Together with Harmonic Prodigy, expect additive extra triggers in relevant cases, not unverified infinite doubling. Losing `Demonic Counsel` and exposure to ordinary creature removal remain costs. Staged as research only.

### 8. Step Through — **promising unconditionally online Wizard tutor, new independent positive challenger**

- The source-bound Oct23 Scryfall Oracle and Wizards' [Modern Horizons 2 notes](https://magic.wizards.com/en/news/feature/modern-horizons-2-release-notes-2021-06-04) confirm **Wizardcycling {2}**. From hand, pay two generic and discard Step Through to search for a **Wizard card** and put it into hand. This is a nonspell activated cycling ability, not conditional on delirium, and can happen at instant timing. Its printed `{3}{U}{U}` bounce-two sorcery is a high-cost late fallback, not the primary reason to play it.
- Exactly **four baseline library Wizards** are tutor targets: `Harmonic Prodigy` (multiplies Kefka's enter/attack triggers), `Gogo, Mysterious Mime` (name-preserving extra Kefka combat), `Valley Floodcaller` (spell-timing access), and `Thassa's Oracle` (secondary win). If adding `Dualcaster Mage` and/or `Spellseeker`, those are additional Wizard targets, making Step Through even more valuable in the candidate's **whole-100 context**. Kefka itself is in the command zone, so Wizardcycling does **not** fetch Kefka.
- Compared to `Demonic Counsel` `{1}{B}`, which searches only for a Demon until delirium, Step Through is usable immediately for those four relevant Wizards even when graveyards are empty and can find Oracle as one compact win half. Counsel becomes substantially broader once **four different card types** are in your graveyard, however, and then can tutor non-Wizards such as Underworld Breach or Demonic Consultation; losing that late any-card flexibility is serious.
- Independent discovery aligns with, but is not proved by, **reported 2026 cEDH Kefka tournament decklists** carrying Step Through, including [October 17 third/fourth place](https://www.mtgtop8.com/event?d=902074&e=92428&f=cEDH) (37-player event). This is one list as contextual validation, never a controlled performance comparison.
- Alternatives explicitly staged over **Demonic Counsel** or **Diabolic Intent**; cutting Intent loses an already-live any-card tutor and sacrifice utility, so that alternative is lower priority. Staged Dualcaster + Step Through pairs preserve the original roles otherwise; no automatic approval or five-swap claim.

### 9. Spellseeker — **strong Wizard clone/tutor synergy, but costs three mana**

- Frozen Oracle: `{2}{U}` Human Wizard; ETB may search for an instant or sorcery with mana value at most **two**. That includes `Demonic Consultation`, `Brain Freeze`, `Molten Duplication`, `Essence Flux`, `Dark Ritual`, `Gamble`, and many protection spells. It enters as a Wizard so `Harmonic Prodigy` can give a **second** ETB tutor and Kefka's blink/copy cards can multiply Spellseeker if the situation supports it. It is also itself fetched by Step Through in packages containing both.
- Unlike `Diabolic Intent`, Spellseeker doesn't sacrifice a creature but costs `{2}{U}` and only finds small instants/sorceries; unlike delirium-enabled `Demonic Counsel`, it cannot find any-card payoffs. At cEDH speed the extra mana and limited target set are material.
- Staged independently over either Counsel or Intent, and paired with Dualcaster/Culling. Spellseeker is not itself an entire additional combo; do not count tutor-target access as a guaranteed win or as a way to fetch Kefka from the command zone.

### 10. Irma, Part-Time Mutant — **new, specifically proactive Kefka copy; replaceability unresolved**

- **Official primary evidence:** [Wizards' TMNT Commander release notes](https://magic.wizards.com/en/news/feature/teenage-mutant-ninja-turtles-release-notes), card **TMC #12**. Irma costs **{2}{U} (three mana)**, is a 1/1 legendary Human Mutant Shapeshifter, and at **the beginning of combat on your turn** becomes a copy of up to one other target creature you control, **except her name stays Irma, Part-Time Mutant and she retains this copy ability**, then puts a +1/+1 counter on herself. Wizards' release notes declare new TMC cards Commander legal and explicitly say this transformation is **no new ETB**: it does not apply the copied creature's enters-the-battlefield ability.
- **Commander-specific payoff:** if Irma was **already controlled since the turn began**, then you cast an un-hasty Kefka in first main phase, at the start of combat Irma can copy Kefka without a **same-name legend rule** collision. Irma is able to be declared an attacker even though Kefka cannot attack without haste, yielding a copied **Kefka attack trigger** (and additional copies if the relevant Harmonic Prodigy conditions hold). Irma **is not a commander**: this attack does not count as commander combat damage. She is also useful for copying another creature, but Kefka is the actual reason for inclusion.
- **Different from Gogo:** `Gogo, Mysterious Mime` costs {3}{R}, copies by combat into a different name **until end of turn**, gives both source and Gogo +2/+0 **and haste**, and forces attacks if able. Irma costs one generic less, can come down the turn before Kefka, keeps the copy past end of turn and accumulates counters, **but does not give the original Kefka haste**, cannot get an immediate Kefka ETB and does not itself generate a second attack if cast too late without haste. Both may justify distinct slots; **Gogo is an explicit historical owner keep and is not cut**.
- **Tested competing cuts:** `Demonic Counsel` sacrifices eventual any-card tutoring and directly **competes** with Step Through's best replacement slot; `Culling the Weak` sacrifices explosive fast-black mana and directly competes with Dualcaster/Generator Servant; `Phantasmal Image` loses a cheaper {1}{U} immediate Kefka ETB and copy-of-opponent utility; `Phyrexian Metamorph` loses artifact/creature copy flexibility and immediate clone ETB. Each can plausibly make Irma a **sidegrade rather than a net improvement** at cEDH speed. This is not yet a certified standalone positive swap.
- **Actual research variants:** Irma over each of those four cards; Irma paired with Step Through, Dualcaster, Spellseeker, or Generator Servant; and three-way Irma/Step Through with Dualcaster, Chameleon, or Fire Covenant, always using non-conflicting exact cuts. Reported [2026-10-17 37-player Kefka third/fourth-place competitive list](https://www.mtgtop8.com/event?d=902074&e=92428&f=cEDH) also carries Irma, useful as discovery, not evidence that this exact original 100 benefits.

## Focused final-stage challenger comparison — generator/Step pair

The exact `GeneratorServant_StepThrough_TwoSwap` hypothesis is staged in addition to all previous alternatives. It is the **most commander-first two-swap candidate**, not an owner-ready approved deck.

| Exact add | Exact cut | Strongest positive | Serious foregone function | Provisional status |
|---|---|---|---|---|
| Step Through | Demonic Counsel | Immediately finds four relevant library Wizards including both Harmonic Prodigy and Thassa's Oracle for `{2}`, with no delirium condition | Owner deliberately chose Counsel as a proactive tuner in October; at delirium it becomes an ANY-card tutor, including Breach | **Probable quality-positive** as an early timing and Wizard-role upgrade, but loss of later breadth matters |
| Generator Servant | Culling the Weak | Play Servant turn two; if it survives to turn three, sacrifice for `{C}{C}` and haste toward five-mana Kefka, allowing immediate ETB+attack | Culling converts `{B}` + sacrificial creature into four black at instant speed, net +3 black, and requires no prior-turn telegraphing | **Plausible quality-positive in commander-first metric**, but not proven better at cEDH tempo across the 100 |
| Irma, Part-Time Mutant | Phantasmal Image, Phyrexian Metamorph, Culling, or Counsel | Extra persistent, name-distinct Kefka attack trigger when predeployed | Every actual cut removes superior immediate ETB, earlier mana, or tutor functionality | **Unresolved / sidegrade**; don't add merely for 2026 inclusion |
| Dualcaster Mage | Culling the Weak | Existing Molten Duplication + Dualcaster combo and added Wizard tutor target | More generic combo infrastructure instead of commander acceleration; competes directly with Generator | **Strong alternate, identity tradeoff** |
| Fire Covenant | Toxic Deluge | Instant selective damage can preserve five-mana Kefka | More colored pips, targeted damage, cannot -X/-X around indestructibility | **Metagame conditional** |
| Spellseeker | Diabolic Intent or Counsel | Wizard-based small instant/sorcery tutor; harmonizes with copy/blink | Three mana and narrower target class than Intent or delirium Counsel | **Unresolved** |

### Bounded mana and draw exposure: why a Culling cut is nontrivial

- The archived 100 contains **13 noncommander creature cards** (one is `Simian Spirit Guide`, often exiled for mana; several others are protected engines or valuable Kefka copy targets). `Culling the Weak` sacrifices a creature as a **cost**, not an optional effect, making actual early fodder availability much narrower than merely counting every creature.
- A simple **mulligan-free**, unordered draw proxy from the 99-card library, before filtering for castability, sees Culling among nine cards by the start of turn three with probability **9/99 = 9.09%** on the play; conditional on seeing Culling, at least one of those 13 creature cards among the other eight occurs **69.42%** of the time. Their conjunction is **6.31%**. This does **not** certify usable black mana or disposable creature status and is **not a commander castability score or win rate**.
- Under the same no-mulligan proxy, Generator Servant is among the first eight cards by start of turn two **8.08%** of the time, but requires two mana including red on that turn and survives into turn three. Three independent other appropriately colored sources must still supply **U, B and R** for Kefka. You cannot normally tap Servant on the turn it enters. These activation sequences are **conditional castability**, not assumed guarantees.
- The replacement trades conditional ritual explosiveness for repeatable **commander-first** usefulness and haste from a creature deployed earlier. Neither proxy covers fast mana, London mulligans, opponents, sequencing, or interaction. No claim of measured gameplay superiority.

## Rejected or unresolved comparisons

- `Entomb` can tutor Anger into graveyard and double a narrow early haste window, but normal Kefka discards Anger already, a single tutor doesn't solve the Mountain/power/mana requirements, and `Demonic Counsel` or `Borne Upon a Wind` sacrifices potent win-enabling functions.
- `Samut, Tyrant of Naktamun` provides split second to controlled instants and sorceries at 1U, but that **also stops its controller from adding non-mana actions to those spell stacks**; compare to retaining open interaction and Kefka's creature spell protection. Not forced.
- `Flash Photography` can copy permanent with flashback, but `{2}{U}{U}` / flashback `{4}{U}{U}` is a heavy cEDH commander-copy investment, especially alongside existing `Molten Duplication`.
- Prior explicit owner-cut `Faerie Mastermind`, `Opposition Agent`, `Dauthi Voidwalker`, `Liliana's Caress`, `Sheoldred, the Apocalypse`, `Windfall`, `Cyclonic Rift` should not be blindly reintroduced merely because they top EDHREC inclusion.
- `Vexing Bauble` shuts down too many of the deck's own free spells. Off-color hybrid `Manamorphose` and banned `Dockside Extortionist` invalid.

## Evidence boundaries and next audit decision

The files are **entire 100-card structural hypotheses only**, not 34 independently improved versions. Among the distinct candidates, **Step Through / Demonic Counsel** currently looks like the clearest early-game role-specific gain at the cost of delirium tutor breadth. `Generator Servant / Culling the Weak` is the second commander-first challenger, conditionally enabling turn-three Kefka with haste but risking removal and telegraphing. `Irma` has compelling proactive Kefka attack-trigger functionality, but an independently defensible cut remains disputed. `Dualcaster/Culling` adds a powerful mostly generic combo while removing fast mana. `Spellseeker/Intent`, the nonpersistent clones, and `Fire Covenant/Deluge` all carry serious mana, speed, combo-access, or control disadvantages. As a result, **no demonstrated five-or-more quality-positive swaps** exist; the maximum number in a stress list is three, and even those are not all validated upgrades.

**Bounded sequencing (rules examples, not simulated win rates):**

1. With Irma cast on a prior turn and Kefka cast first main on the current turn, Irma copies Kefka at beginning of combat. The newly cast original Kefka cannot attack without haste, but the already controlled Irma-copy can attack and cause a Kefka-like attack/discard trigger. If Irma itself entered on the current turn without haste, neither can attack just by becoming a copy.
2. If Irma copies Kefka, its copied combat trigger is separate from and later than Kefka's ETB. Irma's copy action produces **no new ETB**. Irma keeps her printed name, so the same-name legend rule does not sacrifice either; no actual commander damage is dealt by Irma.
3. Step Through's `{2}` Wizardcycling is an activated ability from hand and searches a Wizard without requiring delirium. `Demonic Counsel` costs `{1}{B}` and, before four types exist in the graveyard, cannot fetch a baseline library card because the baseline has no Demons. Once delirium is live, Counsel regains broader payoff access, so the comparison is tempo/selection and not strict dominance.
4. Chameleon's mayhem is `{2}{U}` only **during the same turn discarded**; if Kefka's own five-mana ETB caused that discard in a main phase, casting Chameleon in that main phase can require **eight combined mana**, absent acceleration. A Chameleon discarded on the previous turn cannot be mayhem-cast the following turn merely because it's still in the graveyard.
5. Generator Servant cast for `{1}{R}` on a prior turn can tap and sacrifice for `{C}{C}` toward Kefka's generic two. Three other appropriately colored sources still must produce **U, B and R** for Kefka, and Servant doesn't help if it cannot survive until untap. Glasspool Shore is a tapped-only blue land, so land-mode flexibility does not imply untapped deployment.

None currently passes the full owner-ready M7 strategic gate, and no owner waiver has been requested or given for Kefka. Before promoting any exact candidate, update external-card source evidence where needed, independently verify all 100 cards' current legality, and compare full-deck early-game mana/interaction losses. Preserve historical canonical Kefka unchanged. This PR stays **RESEARCH_ONLY**.

No paid Grok run, Google Colab, win-rate simulation, independent third-model review, or full Magic stack engine was used.
