# Ashad, the Lone Cyberman — ChatGPT independent M7 second-pass research

**Status: RESEARCH CANDIDATES UNDER REVIEW, NOT OWNER-APPROVED, NOT CANONICAL, NOT FINAL M7 VERIFIED.** Date: 2026-10-23 America/Chicago. Engineering first-pass PR [#653](https://github.com/corymstover/GrokBotMTGCompanion/pull/653) is preserved; no canonical repo or historical M6 source seal has been edited.

## Source and adversarial finding

The exact frozen approved Oct13 baseline raw hash is `087e34c2127859111fc08f8d9ec7d66cd3495537cc571d88e829fd27d2823e25`. GrokBot proposed five swaps at `dfd1158c79668c2dcd85137219bd00bdc75cd855697cf31dfb9b5ff93552597d` on PR head `fee682f356c5b7aebe4b4094137bf198215bf875`: 30 lands and **eight** rocks, 38 static sources; its reported exact P(4 or more such sources in 10 draws) = 0.5828. That is **worse** than historical baseline 30 lands + nine rocks, 39 sources, P=0.6099. It is not enough to treat five attractive casualty fodder swaps as final optimization of a four-mana UBR commander with Wurmcoil/Portal and multiple expensive payoffs.

A commander-first counterargument also changes *which* high-ceiling cards should be cut:
- **Retain Marionette Master**: its fabricate +3/+3 mode gives a 4-power drain payoff when artifacts go to graveyard, a premium Ashad artifact-sacrifice finisher with KCI/Altar loops. The first-pass cut loses meaningful kill pressure despite Mayhem Devil/Disciple.
- **Retain Unwinding Clock**: it untaps artifact mana engines across opponents' turns, vital with Shimmer Myr enabling Ashad's once-*each*-turn nonlegendary artifact-casualty trigger. Cutting it for generic ramp can damage this specific commander's ceiling.
- **Retain Ichor Wellspring in nine**: cheap cantrip ETB plus death-draw with KCI, can be doubled with casualty, cushions the original five's cuts of Thoughtcast and Spy Network. Cyberman Patrol is a high-quality, independent 10th candidate, *not automatically an upgrade* over this draw engine.

## Nine-substitution strategic research front-runner — pending verification

Exact 100-card staged full list: `data/grixis/m7/candidate_lists/Ashad__the_Lone_Cyberman_ChatGPT_Rev2_Nine_Research.txt`.
Raw SHA-256: `1a9e875a06971734d7bd7211b3338cb888a3f8135c88530bab7e9e8544402704`. **Not approved.**

| Add | Cut | Independent reason and downside |
| --- | --- | --- |
| Skullclamp | Fellwar Stone | Pay {1} for repeatable sacrificial draw and makes selected 1-power/2-toughness bodies reach casualty 2; losing ninth rock must be repaid in mana base. Equip timing sorcery-speed; first artifact spell may precede equipping. |
| Piggy Bank | Reckless Fireweaver | 2-MV artifact 3/2 fodder that dies to a Treasure, unlike 1-power nonartifact Fireweaver; loses repeated ping win-condition redundancy. |
| Razorlash Transmogrant | Thoughtcast | 2-MV repeatable 3/1 artifact body, conditional two-black recurrence and already-disclosed Pitiless+Phyrexian Altar three-card loop; loses inexpensive affinity draw two. |
| Necron Deathmark | **Noxious Gearhulk** | Five-mana flash copyable 5/3 ETB removal over six-mana Gearhulk with overlapping function. Loses Gearhulk lifegain, menace and one point toughness but keeps *Marionette Master* finishing engine. |
| Royal Warden | Thopter Spy Network | Five-mana artifact 3/2 makes two tapped 2/2 artifact casualties per ETB; a copied Warden makes four; unearth offers second chance. Loses recurring flying 1/1 production and combat-draw; unearthed Warden is exiled when sacrificed, not a death/Plunderer trigger. |
| **Mishra's Workshop** | **Tezzeret, Master of the Bridge** | Adds one 31st land producing up to three colorless **only to cast artifacts**, paying for high-MV copies but not activations/colored Ashad pips. Trades six-mana nonartifact drain/reanimation payoff to protect Marionette and Unwinding. *Game Changer*. |
| **Ancient Tomb** | **Delete** | 32nd land, taps for two colorless at two life, accelerates artifact spells/abilities and generic Ashad cost; drops a niche X-damage sweeper while one-sided Their Name Is Death plus creature-removal ETBs remain. *Game Changer*. |
| City of Brass | Crumbling Necropolis | Untapped three-color fixing instead of tapped triland; pain tradeoff, no land-count change. |
| Mana Confluence | Shipwreck Marsh | Unconditional untapped three-color fixing at 1-life activation cost instead of late-untapped UB-only land; no artifact-condition risk as with Spire of Industry. |

**Preliminary new mana structure:** 32 lands + 8 rocks = **40 static sources**; 9-swap P(≥4 in first 10 of 99 library cards) **0.6363**. This bound counts Workshop as one draw source, but is **not** a probability of casting Ashad because it does not independently meet all three colored pips, and Workshop's spending is restricted. The two rainbow replacements strengthen colored fixing. Extra land density also reduces nonland artifact density, a tradeoff. Five known Game Changers (Cyclonic Rift, Demonic Tutor, Fierce Guardianship, Ancient Tomb, Workshop), so proposed natural power remains **Bracket 4 — Optimized**.

## High-value tenth challenger — retain as full 100 for head-to-head

Exact 100: `data/grixis/m7/research_challengers/Ashad__the_Lone_Cyberman_ChatGPT_Rev2_Ten_Patrol_Alternative.txt`. Raw SHA `daf54f692a508db867d84ef9c047897cfc3669f54c841b23a273af4de925558b`.
**+Cyberman Patrol / −Ichor Wellspring** over the above nine. Patrol is only {2}, a nonlegendary 2/2 artifact casualty body giving all artifact creatures afflict 3; an Ashad casualty copy multiplies the afflict pressure and supports Cybermen Squadron's artifact myriad. Its downside is losing Wellspring's cheap immediate card and repeatable sacrifice draw. The deck already adds Piggy Bank, Razorlash, Royal Warden and Skullclamp; fodder may be sufficient, making Wellspring's resource flow preferable. No padding decision until direct testing.

## Independent M7 Rev3 provisional judgment — 10 nonpadding swaps

Following direct Oracle verification and five complete-list comparisons, **Liberator over Kappa** is the provisional preference among ten-swap options: redundant instant-speed artifact casting is more uniquely Ashad-positive than a single improvise/unblockable combat finisher in this aristocrats/copy shell. Unlike replacing the commander with a generic artifact combo shell, the effect increases access to Ashad's **first nonlegendary artifact each turn** trigger on opponents' turns. Shimmer Myr remains; legend restriction means Liberator itself is *not* copied, and it begins at power 1 so cannot immediately pay casualty 2 without a boost. Kappa's ward-4 and unblockable growth are acknowledged real losses, not dismissed.

**Selected for additional M6 I/J source testing, NOT for owner approval yet:** `data/grixis/m7/candidate_lists/Ashad__the_Lone_Cyberman_ChatGPT_M7_Rev3_Ten_Approval_Candidate.txt`; exact raw SHA-256 `352911498345e78bd55773f4c9d1c49d05599610d5fc806f7b779c85eb5f6267`, logical hash `lh1:9ebaa891f2ff0e7af81ff2856b54a012c915f8d5cb1936a8ca579579aa8cb8c9`. Ten meaningful one-for-one substitutions: the nine detailed above, plus `+Liberator, Urza's Battlethopter / −Kappa Cannoneer`. Full 100, 95 names, five Game Changers, 32 lands + eight rocks. Exact source-bounded 118-name snapshot and five-list tested pool are additive; original approved Ashad baseline and Grok's five-swap certificate remain unchanged.

**Rejected as default:** Cyberman Patrol over Ichor Wellspring loses important ETB/death draw without unlocking a new engine; Technomancer over Kappa is graveyard-conditional at seven mana including {B}{B}, and sacrifices fast pressure for late recursion. Both remain *available alternatives*, not deleted. The other six high-lift cards were scrutinized via Oracle but showed less positive net commander-first impact. This is a **bounded, qualitative** decision. No simulation, game-rate claim, final I/J certification, or owner approval has occurred.

## Additional EDHREC high-lift adversarial challenge — not automatically selected

Beyond the nine initial improvements and Cyberman Patrol tenth option, independently checked primary live Scryfall for **Technomancer**, **Cryptek**, **Canoptek Spyder**, **Liberator, Urza's Battlethopter**, **Anrakyr the Traveller**, **Necron Monolith**, **Mishra, Eminent One**, and **Borg Queen, Perfection Manifest**. EDHREC lift is hypothesis generation, not substitution authority. Borg Queen is Scryfall `not_legal` and rejected. In particular, Canoptek Spyder's triggered ability does not reward **token** artifact creature copies; it triggers only for *nontoken* artifact creatures. Cryptek requires {1}{B} plus tapping for a one-creature delayed death-return; high setup cost. Anrakyr and Mishra are separate legendary engines, not clearly commander-first for Ashad.

Two credible **complete 100** follow-up comparisons are staged, each independently source-bound and each replacing **Kappa Cannoneer** on the nine-swap base while **retaining Ichor Wellspring**:

| Alternative | Raw SHA-256 | Commander-first upside | Opportunity cost |
| --- | --- | --- | --- |
| +Liberator, Urza's Battlethopter / −Kappa Cannoneer | `352911498345e78bd55773f4c9d1c49d05599610d5fc806f7b779c85eb5f6267` | A second three-mana **cast-at-flash-speed** enabler behind Shimmer Myr unlocks more first-artifact-cast triggers on each opponent turn. Legendary Liberator itself cannot be casualty-copied; it starts at power 1 but grows on spells costing more mana than its power. | Losing Kappa's improvise, ward {4}, repeated growth and unblockable pressure. |
| +Technomancer / −Kappa Cannoneer | `afdd6678f2d3e58555bdf67287a040e240057ab488de82fb1625a7dc62593515` | Nonlegendary artifact creature with ETB mill + up to 6 total mana value of reanimated artifact creature cards; an Ashad-copied spell repeats the ETB independently, a potent post-sacrifice rebuild. | Seven-mana spell with {B}{B} and graveyard requirement; loses fast improvise finisher and increases black/curve pressure. |

Files: `data/grixis/m7/research_challengers/Ashad__the_Lone_Cyberman_ChatGPT_{Liberator,Technomancer}_Over_Kappa_Challenge.txt`; direct primary receipt `Ashad__the_Lone_Cyberman_ChatGPT_high_lift_direct_sources.json` in the same folder. This adds **two true candidate trials**, not asserted improvements or a fixed swap quota. **Strategic decision remains open** until rule/mana and source-bound alternatives are explicitly weighed. The nine remains the main research front-runner, and no new approval/lock is implied.

## Rules/legality and remaining gates

**Direct Oracle source gap closed.** Four new lands now have independently retrieved **direct live Scryfall JSON** (named-card API), exact Oracle IDs, text, Grixis color identity, Commander legality and Game Changer status in [direct four-card primary receipt](../research_challengers/Ashad__the_Lone_Cyberman_ChatGPT_Rev2_new_lands_primary_sources.json). New [116-name Rev2 evidence snapshot](../../m6/oracle_snapshots/Ashad__the_Lone_Cyberman_M7_Rev2_Scryfall_20261023.json) preserves the original 112-name discovery source and appends the four verified cards. **The discovery pool itself is not universally legal:** Bio-Asset Allocator (`not_legal`) and Golos, Tireless Pilgrim (`banned`, additionally five-color) remain explicitly labeled rejected research names; **neither appears in either proposed 100**. Both nine- and ten-swap 100s have 100 physical cards, singletons except basics, UBR identities and all candidate entries `commander_legality=legal` according to this sourced snapshot. The newly fetched four are current directly sourced; the old 112 are preserved as their October 23 snapshot (not re-fetched today). This focused source gate is not M6 I/J certification or Cory's approval.

- The original candidate-specific Grok M6 I/J certificates bind `dfd1158c79668c2dcd85137219bd00bdc75cd855697cf31dfb9b5ff93552597d` only and do **not transfer** to `1a9e875a06971734d7bd7211b3338cb888a3f8135c88530bab7e9e8544402704` or `daf54f692a508db867d84ef9c047897cfc3669f54c841b23a273af4de925558b`.
- Ashad casualty 2 is granted on the first nonlegendary artifact spell **each turn**, only if a power-2+ creature is sacrificed as additional cost. Permanent-spell copies resolve as tokens but are not cast or created; no free Worldwalker Helm Map bonus from Ashad's copy. Iron Man copying same artifact works separately.
- Razorlash + Pitiless Plunderer + Phyrexian Altar requires an opponent with **at least four nonbasic lands** and a payoff; it produces neutral mana (not infinite free mana). The tutor-equipped engines have to be verified for casting vs activated-ability spend with Workshop.
- Full 100 and source hash, singleton, open deck locks, source-specific rules and finite mana comparisons are mechanically testable. **No statistically controlled multiplayer win-rate claim.**
- Decision still open: select best final nine/ten or a better replacement after independent test/Oracle and deeper 99-card review. These are not owner-presentable as final verified until gates complete. No approval/lock changes.

Archidekt research tags: **Artifact Copy / Casualty Aristocrats / Artifact Combo**.
