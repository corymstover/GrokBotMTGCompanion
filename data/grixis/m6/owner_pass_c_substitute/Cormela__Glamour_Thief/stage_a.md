# Josh-Lee-Kwai formal Pass C — Stage A: Cormela, Glamour Thief

- Deck sequence: **#9/62**
- Deck ID: `Cormela__Glamour_Thief`
- Reviewer alias: **Josh-Lee-Kwai**; actual evaluator: **ChatGPT / OpenAI GPT-6**.
- Classification if subsequently evidenced: **FORMAL_PASS_C_OWNER_EQUIVALENT**, by October 20, 2026 owner authorization. Technically independent third-model execution: **NO**; waived for project formal Pass C only.
- Input boundary: exact canonical 100-card TXT and approved source SHA-256, neutral commander/card Oracle and release notes, neutral card roles. **No prior ChatGPT comprehensive review, GrokBot advisory, two-model reconciliation, existing recommendation, ranking, or prior test verdict was opened or consulted for this Stage A.** Prior-session context cannot be erased and prevents an assurance of cognitively independent judgment.
- Exact canonical source: `corymstover/grixis-commander-encyclopediaGPT/main/refinement/decklists/Cormela_Glamour_Thief_Approved_2026-10-14.txt`
- Independently recomputed **source byte SHA-256: `80f4bdef2b8b140aeae23775cfdf87fda81e7215038b8db9b1746c806f366e0b`**, matching approval authority. Source Git blob `ee008725234c917af858de5a9c237fc2acf6781d`.
- Count: **100 total entries, 100 distinct names, one commander, 99 other cards, 30 lands**. No repeated basics. This is list enumeration, **not** a fresh card-by-card official legality / complete Oracle audit.
- Authorized canonical state: **APPROVED / LOCKED**. Stage A cannot and does not change it.

## Commander-first identity and ceiling

Cormela costs `{1}{U}{B}{R}`, is a hasty 2/4 legendary creature, has `{1}, {T}: Add {U}{B}{R}. Spend this mana only to cast instant and/or sorcery spells`, and on death returns up to one target instant or sorcery card from the controller's graveyard to hand. She is **not** simply a mana dork: the extra generic activation payment and spend restriction are decisive. Haste makes a newly returned/recast Cormela useful immediately. Her death trigger converts intentional sacrifice, cloning/legend collisions, and kill spells into spell recursion. The commander-native plan is spell-chain mana and recursive death loops, **not** merely generic Grixis goodstuff.

Bracket **5 / cEDH-capable** is plausible from this shell, independent of any previous project scores: Ad Nauseam; fast zero/one-mana artifacts; free interaction; Oracle/Consultation/Pact; Breach/LED/Brain Freeze; and commander-native loops. Whether Cormela improves expected tournament outcomes over other commanders requires adversarial matchup and mulligan evidence; a plausible ceiling is not a measured win rate.

## Resource, curve, and source audit

Exactly **30 lands**: seven traditional fetchlands (Bloodstained Mire, Marsh Flats, Misty Rainforest, Polluted Delta, Scalding Tarn, Wooded Foothills, Flooded Strand); Grixis original duals/shocks, City of Brass/Mana Confluence, pain and multiplayer lands, three basics, utility lands including Ancient Tomb, Gemstone Caverns, Phyrexian Tower and Otawara, and surveil land Undercity Sewers. Colors are broadly accessible with fetch/shock/dual coverage, but the proposed inventory has not been independently goldfished for turns 1–3. Undercity Sewers always entering tapped is a real tempo cost, though its Surveil 1 and fetchability assist graveyard plans. Phyrexian Tower provides a sacrifice outlet and black mana, at the expense of immediate universal fixing.

Acceleration: Chrome Mox, Mox Diamond, Mox Opal (metalcraft-dependent), Mana Vault, Sol Ring, Lotus Petal, Lion's Eye Diamond, Arcane Signet, three Talismans; rituals Dark/Cabal Ritual, Rite of Flame, Seething Song, Jeska's Will and Culling the Weak. Cormela must itself be cast for four mana, and **pay one more mana per activation**; her `{U}{B}{R}` cannot pay altar activations, transmute, reanimation abilities, artifact casts, or a replacement commander cast. Ad Nauseam and Necropotence demand meaningful life, black source access, and stack discipline. Quantitative curve and colored-pip simulations have **not** been run in Stage A.

## Spell and win-engine topology

1. **Cormela + Demonic Gifts + Ashnod's Altar**: pay `{1}` and tap Cormela for spell-restricted UBR; cast Demonic Gifts targeting Cormela for `{1}{B}`; sacrifice Cormela to Ashnod's Altar for `{C}{C}`. Both granted return trigger and Cormela death trigger arise; Cormela's ability can target Demonic Gifts once the instant finishes resolving and is in the graveyard. Choose stack order to return Demonic Gifts and Cormela, then pay `{1}` of altar's unrestricted colorless to re-activate the hasty, returned Cormela. Iteration can net restricted U/R and unrestricted colorless, along with arbitrarily many deaths/casts/ETB and storm count. **Do not incorrectly count restricted UBR as freely spendable generic mana for abilities.** Requires all named cards to be available, the creature to be a legal Gifts target, spell-resolution and death-trigger continuity, and an actual win outlet. Protection, graveyard exile, exile-on-death replacements, countering Gifts, or removing the sacrifice artifact can break the line.
2. **Cormela + Demonic Gifts + Phyrexian Altar**: the sacrifice adds one unrestricted colored mana that can pay Cormela's next `{1}` activation, while Cormela's restricted UBR casts Gifts. Can accumulate restricted U/R and storm/death triggers, but **does not** also generate Ashnod's unrestricted colorless. Exact mana ledger and priority sequencing deserve an executable trace before certification.
3. **Saw in Half targeting Cormela**: the original 2/4 dies and two legendary 1/2 Cormela tokens enter if destruction actually causes death. Legend rule makes one token die. Original and token death triggers can return **two distinct** instant/sorcery cards, including a resolved Saw in Half once in the graveyard when targets are selected after resolution. Original commander replacement to command zone does not erase a valid death trigger. The survivor can tap with haste for colored spell mana, at an extra one generic activation cost. Opponent responses and copying a token under continuous effects must be modeled; this is recursion/value, not automatically infinite.
4. **Dualcaster Mage + Molten Duplication**: cast Molten Duplication on a legal owned artifact/creature (e.g., Cormela), then flash Dualcaster Mage to copy and retarget the still-on-stack sorcery to Dualcaster. New hasty nonlegendary Dualcaster tokens enter and each copies/retargets the still-pending spell, allowing arbitrarily many hasty bodies if the stack sequence holds. Must actually have a legal initial target; sorcery timing is normally main phase, and blockers/interaction still matter. A copied sorcery is not a **cast** for cast-trigger/storm accounting.
5. **Underworld Breach + Lion's Eye Diamond + Brain Freeze** and **Thassa's Oracle + Demonic Consultation/Tainted Pact** provide compact backup finishes. Tainted Pact is supported by 100 unique names, but Oracle timing / Demonic Consultation naming and opposing counterplay are critical. The backup axes are powerful and may be appropriate here because spell recursion, tutors and instant/sorcery-only ramp help reach/protect them; avoid claiming they are themselves Cormela-specific.

## Interaction and opponent counterplay

The current list supports proactive disruption with Force of Will, Force of Negation, Fierce Guardianship, Pact of Negation, Flusterstorm, Mental Misstep, Mindbreak Trap, Swan Song, An Offer You Can't Refuse, Pyroblast, Red Elemental Blast, Deflecting Swat, Chain of Vapor and Otawara. Rhystic Study/Mystic Remora and wheels find resources; tutors locate engines. These are justifiable protection for an exposed four-mana sacrifice engine. Vulnerabilities: Deafening Silence/Rule of Law effects limit multispell chains; Grafdigger's Cage / graveyard exile / Dauthi Voidwalker-type replacements attack Breach or recursion differently; instant-speed creature exile breaks death-based returns; tax effects inflate one-mana activations; Stifle-like effects stop recursion; fast creature pressure and Ad Nauseam life loss compete. Bowmasters helps police draws but does not remove permanent-based rule-setting hate. Chain of Vapor and Otawara are useful yet few unconditional answers to a resolved hate enchantment/artifact; actual counterspell timing may compensate.

## Adversarial slot review and unranked challengers

- **Shallow Grave and Goryo's Vengeance** are conditional: graveyard order and legendary target respectively matter, and Cormela must be in the graveyard rather than the command zone. They nevertheless provide burst access to a hasty death/recursion engine. Do not call either a free cut without sequencing trials.
- **Seething Song** offers +2 burst red but requires red access and can be clunky under Ad Nauseam/lower land counts. An alternative **Muddle the Mixture** supplies a counterspell and transmute access to MV2 Demonic Gifts, Underworld Breach, Thassa's Oracle and Molten Duplication; however its `{1}{U}{U}` transmute cost is an **activated ability**, so Cormela's restricted mana cannot pay it, and its sorcery-speed search can cost a pivotal turn. This is a bounded *test candidate*, not a demonstrated improvement.
- **Arcane Signet / Talisman of Indulgence** are two-mana rocks with turn-two tempo opportunity costs but shore up Grixis pips, Cormela activation tax and early keepable hands. Cutting them without opening-hand evidence might worsen commander access.
- **Undercity Sewers** is a tapped land despite very high tempo needs, but surveil plus dual fetchability can stock graveyard; compare exact opening sequences before recommending a swap.
- **Abrade**, **Beseech the Mirror**, and **Muddle the Mixture** are plausible unranked challengers to probe interaction, tutor density and access, respectively; Beseech strains triple-black sourcing and bargain material. No candidate ranking or previous model's recommendation was consulted.

## Strongest counterargument

Cormela is a potentially fragile **four-mana** commander in a 30-land shell. Three-card loops with a targetable creature lose to one well-timed removal/stack counter, and redundant Oracle/Breach win axes risk making the deck look like generic Grixis cEDH. There is a credible position that cutting a conditional reanimator/ritual for early hate interaction is necessary, **but** displacing commander-native resurrection may make the deck both less distinctive and less resilient. The stack-interaction density already present might mitigate permanent hate if exercised correctly; no measured comparative game record resolves this.

## Stage A decision and boundary

**Provisional: NEEDS TESTING** — narrow independent question: whether `+Muddle the Mixture / -Seething Song` meaningfully improves two-mana engine access and interaction without losing viable turbo-Cormela lines; alternatively test `+Abrade` against the most vulnerable conditional role if permanent hate creates real pre-board losses. Neither is an approved or favored swap. A rigorous KEEP is credible if specific tests fail to demonstrate gain. Prioritize rules trace for Cormela/Demonic Gifts/Phyrexian Altar and Saw in Half stack/death targets, plus opening-hand colored sources, commander casting, and hate-board answers.

**Stage A limitation:** observed source enumeration and selected neutral Oracle/release-ruling review, not randomized playtests, effect-aware simulation, a complete fresh legality scan, or independent third-model execution. No victory or win-rate result asserted. No canonical change made.

## Neutral citations consulted prior to seal

- WotC, *Streets of New Capenna*, official Cormela profile: https://magic.wizards.com/en/news/feature/the-legends-youll-find-in-streets-of-new-capenna
- WotC, *Kaldheim Release Notes*, Demonic Gifts and its once-per-return limitation: https://magic.wizards.com/en/news/feature/kaldheim-release-notes-2021-01-22
- WotC, *Unfinity Release Notes*, Saw in Half requirements/copy behavior: https://magic.wizards.com/en/news/feature/unfinity-release-notes-2022-10-07
- WotC, *Outlaws of Thunder Junction / The Big Score release notes*, Molten Duplication: https://media.wizards.com/2024/downloads/OTJ_Release_Notes_nwYBwey2D91L/EN_MTGOTJ_ReleaseNotes_20240307.pdf
- WotC, *Ultimate Masters Release Notes*, Goryo's Vengeance: https://magic.wizards.com/en/news/feature/ultimate-masters-release-notes-2018-11-29
- Neutral Oracle display / legality snapshot, Cormela: https://mtg.wtf/card/snc/177/Cormela-Glamour-Thief
- Neutral Oracle display / legality snapshot, Molten Duplication: https://mtg.wtf/card/big/14/Molten-Duplication

Do not unblind earlier model opinions until this exact Stage A markdown and machine record are committed and a **separate** immutable hash/first-commit seal is committed.
