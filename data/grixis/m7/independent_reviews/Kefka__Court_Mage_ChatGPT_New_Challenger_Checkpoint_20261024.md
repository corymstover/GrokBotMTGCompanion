# Deck #25 Kefka, Court Mage — independent M7 challenger research checkpoint

Date: 2026-10-24 (America/Chicago). **RESEARCH_ONLY. No owner-presentable M7 list, no new owner approval, no canonical change.**

## Authority and provenance

- Canonical main historical October 14 deck: `corymstover/grixis-commander-encyclopediaGPT/refinement/decklists/Kefka_Court_Mage_Approved_2026-10-14.txt`; **100 cards**, **28 printed lands**, **100 distinct**, no terminal LF, raw SHA-256 `cd36192fedda7a4f54570fb8b8e4605147b40f9254e6985729097fc998f17b03`. Historical APPROVED/LOCKED; not yet a NEW M7 lock.
- Grok preliminary research [PR #673](https://github.com/corymstover/GrokBotMTGCompanion/pull/673), exact head at this checkpoint `ee2abd0a4f9c4729371c16233c5979c1331ae1a8`, proposed **only +Dualcaster Mage / −Culling the Weak** (research, not approved); **12 staged 100s** and 228-card archived Oct23 Scryfall audit. Do not merge the stacked Grok PR.
- Independently discovered EDHREC commander-specific High Lift candidates after reading current [Kefka cEDH commander page](https://edhrec.com/commanders/kefka-court-mage/cedh) and [combo variant](https://edhrec.com/commanders/kefka-court-mage/cedh/combo). High Lift and popularity are discovery, not intrinsic power proof.
- Independent research stages **14 complete exact-100 alternatives, including normalized baseline, pairings and explicit stress versions** in `data/grixis/m7/independent_candidates/Kefka__Court_Mage_M7_*Research_20261024.txt`. The companion `Kefka__Court_Mage_M7_Independent_Oracle_Index_20261024.json` pins **106 archived Scryfall source names** plus one externally researched Chameleon. Archive excludes the newly found Chameleon, so an eventual candidate containing it needs fresh exact oracle/legality verification before owner presentation.
- Kefka-only waiver **does not exist**. The ordinary five-swap minimum applies if an owner-ready M7 candidate is ever presented. Never pad.

## Commander and baseline challenge

`Kefka, Court Mage // Kefka, Ruler of Ruin` is `{2}{U}{B}{R}` and is a Human Wizard. Kefka's **enter and attack** triggers each ask every player to discard one card, then draw per **different card type** among the cards discarded *in that trigger*. A transformed Kefka costs `{8}` at sorcery timing and rewards opponents' actual life loss during the controller's turn; this isn't a front-face turbo shortcut.

Keep the owner-approved original identity: `Harmonic Prodigy`, `Essence Flux`, `Displacer Kitten`, `Anger`, `Arena of Glory`, `Gogo, Mysterious Mime`, `Molten Duplication`, `Phantasmal Image`, `Phyrexian Metamorph`, `Saw in Half`, `Tinybones, Bauble Burglar`, `Waste Not`. Preserve fast mana and genuine Oracle/Breach win-line access. Existing Oct14 owner cuts of generic tribal, discard drain, expensive draw and bounce-combo packages stay respected.

## New hypotheses requiring independent whole-100 judgment

### 1. Chameleon, Master of Disguise — **genuinely overlooked; promising, not certified**

- **Official source** [Gatherer MSC #148](https://gatherer.wizards.com/MSC/en-us/148/chameleon-master-of-disguise), [Scryfall MSC #148](https://scryfall.com/card/msc/148/chameleon-master-of-disguise) and Wizards' [Spider-Man mayhem design notes](https://magic.wizards.com/en/news/feature/spider-man-swinging-into-design). Not among Grok's archived 228 candidates.
- Normal `{3}{U}` creature; mayhem `{2}{U}` from graveyard **only if discarded that turn**, with regular creature casting timing. Chameleon may enter as a creature you control and **keeps Chameleon's own name**, so a Kefka copy remains on the battlefield beside original Kefka without the same-name legend-rule collision. This potentially compounds ongoing attack triggers, unlike one disposable copy.
- **Direct Kefka interaction:** Kefka's own discard can move Chameleon from hand to graveyard, permitting a discounted mayhem cast *that turn* in a legal main phase. **Vital caveat:** Kefka already costs five; from a fresh hand, casting Kefka and Chameleon mayhem together ordinarily needs **eight mana total**, before other acceleration. If Chameleon was discarded on Kefka's earlier turn and not cast that turn, mayhem is no longer available next turn simply because it remains in graveyard. The trigger does not allow casting during its resolution or bypass sorcery timing.
- Staged over `Demonic Counsel`; **material loss:** an eventually broad one-mana tutor enabled by delirium. The candidate is not assumed better merely from high EDHREC lift.

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

## Rejected or unresolved comparisons

- `Entomb` can tutor Anger into graveyard and double a narrow early haste window, but normal Kefka discards Anger already, a single tutor doesn't solve the Mountain/power/mana requirements, and `Demonic Counsel` or `Borne Upon a Wind` sacrifices potent win-enabling functions.
- `Samut, Tyrant of Naktamun` provides split second to controlled instants and sorceries at 1U, but that **also stops its controller from adding non-mana actions to those spell stacks**; compare to retaining open interaction and Kefka's creature spell protection. Not forced.
- `Flash Photography` can copy permanent with flashback, but `{2}{U}{U}` / flashback `{4}{U}{U}` is a heavy cEDH commander-copy investment, especially alongside existing `Molten Duplication`.
- Prior explicit owner-cut `Faerie Mastermind`, `Opposition Agent`, `Dauthi Voidwalker`, `Liliana's Caress`, `Sheoldred, the Apocalypse`, `Windfall`, `Cyclonic Rift` should not be blindly reintroduced merely because they top EDHREC inclusion.
- `Vexing Bauble` shuts down too many of the deck's own free spells. Off-color hybrid `Manamorphose` and banned `Dockside Extortionist` invalid.

## Evidence boundaries and next audit decision

The files are **entire 100-card structural hypotheses only**. None currently passes a demonstrated five-or-more positive-swap M7 strategic gate, and no owner waiver has been requested or given for Kefka. Perform whole-100 source-bound legality/mechanics verification, actual competing-slot opportunity-cost review, and bounded mana/turn sequencing for Chameleon mayhem, Generator Servant and Glasspool tapped land before promoting any. Preserve the historical canonical Kefka deck.

No paid Grok run, Google Colab, win-rate simulation, independent third-model review, or full Magic stack engine was used.
