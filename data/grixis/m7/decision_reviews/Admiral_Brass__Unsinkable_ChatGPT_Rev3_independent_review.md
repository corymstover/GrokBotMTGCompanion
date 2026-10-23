# Admiral Brass, Unsinkable — ChatGPT independent M7 Rev3 owner candidate

**Date:** 2026-10-23. **Status:** PROPOSED, NOT APPROVED, NOT CANONICAL.  
**Canonical authority:** `corymstover/grixis-commander-encyclopediaGPT@main`; do not edit until Cory explicitly approves exact candidate SHA.  
**Research PR:** https://github.com/corymstover/GrokBotMTGCompanion/pull/651 (GrokBot Rev2 preserved verbatim).  
**Rev3 file:** `data/grixis/m7/candidate_lists/Admiral_Brass__Unsinkable_ChatGPT_Rev3.txt`.  
**Raw SHA-256:** `dfa192cce0d925621e1cfa3f6444fb9da04c995700ca886e95a75c7347d4c7f7`.

## Eight proposed baseline changes — quality-derived, not a swap-count target

| Add | Remove | Concrete commander-first case | Opportunity cost |
| --- | --- | --- | --- |
| Kitesail Larcenist | Enterprising Scallywag | Brass reanimates a hasty 4/4 flier with an ETB that can turn an artifact/creature **for each player** into a Treasure. A repeatable reanimation-control target, doubly triggered by Roaming Throne. | Scallywag's conditional descend Treasure. |
| Timestream Navigator | Francisco, Fowl Marauder | A reanimated Navigator gets haste, can pay `{2}{U}{U}` and tap immediately *if city's blessing (10 permanents)*, then goes to the bottom of its owner's library and grants an extra turn and extra Brass combat trigger. | Francisco's explore and cheap evasive body; Navigator cannot immediately be reanimated again after its activation. |
| Warkite Marauder | Fathom Fleet Captain | Free attack-trigger blocker neutralization and flying; doubled by Throne. | Fathom Fleet's repeatable but paid `{2}` 2/2 menace Pirate tokens. |
| Jhoira, Weatherlight Corsair | Pitiless Plunderer | Brass returns a 4/4 hasty Pirate with ETB **and** attack triggers; each can steal an opponent's historic permanent from their deck at life cost equal to MV. | Plunderer still generates Treasure on **normal** creature deaths, stolen creatures and tokens. Its loss is real; this is the most debatable creature swap. |
| Siren's Ruse | Crumbling Necropolis | `{1}{U}` instant saves/resets a Pirate, clears its finality counter as a new object, retriggers ETB, and draws if Pirate. The 34th land was an always-tapped nonfetchable tri-land. | Candidate has 33 physical lands/8 rocks, not 34. Opening land and turn-four source odds dip; the returned creature loses temporary base-4/4 and haste. |
| Ripples of Undeath | Forerunner of the Coalition | `{1}{B}` enchantment mills three at the beginning of *each* first main phase, before Brass selects a graveyard Pirate for combat; may pay `{1}` and three life to reclaim a milled card. Importantly, **Faithless Looting stays in the deck.** | Forerunner was itself a Pirate, tutored a Pirate to the top on ETB, and drained each opponent for other Pirate ETBs. Losing that tutor and a Pirate is meaningful, but repeated precombat setup plus existing Entomb/Buried Alive wins this comparison. |
| Thassa, Deep-Dwelling | Wonder | Indestructible `{3}{U}` end-step blink each turn: reset finality, retrigger Brass's mill-four/other Pirate ETBs, and convert **Coercive Recruiter's** temporary stolen nontoken creature into a permanent steal by returning it under your control. With **Zara**, stack Thassa's end-step blink above Zara's delayed return trigger; the new object escapes that delayed return. | Wonder, if milled/discarded with an Island in play, gave the whole team flying. It is weak as an unrecurrable, four-mana non-Pirate in hand; Thassa has proactive value and is itself not a Pirate. Thassa cannot blink a stolen *token* back. |
| City of Brass | Path of Ancestry | Both fix U/B/R, but City enters untapped and casts Brass/interactions on curve. | City deals one damage whenever tapped; Path's tapped entrance bought scry 1 on *cast* Pirate spells. Actual reanimation does not trigger Path's scry. Given many life payments in this deck, City's damage is a deliberate cost. |

**Faithless Looting — retained, not cut:** GrokBot Rev2 mistakenly characterized it as one-shot. It costs `{R}`, draws two then discards two, and has **flashback `{2}{R}`**. Those two controlled discard opportunities can move expensive Pirates stranded in hand to the graveyard *before that turn's combat*, whereas Ripples randomly mills the library and cannot select cards from hand. Running both has a role distinction and is stronger here than cutting Looting. Forerunner is the cut to make room for Ripples, after an independent 99-slot review.

## Targeted challenger comparisons

- **Thassa versus Conjurer's Closet:** both blink a creature each end step and return it under your control, meaning both clear finality and can keep a temporarily stolen nontoken creature. Thassa is one mana cheaper, indestructible and provides a `{3}{U}` tap ability. Closet is a 5-mana artifact and is more exposed to artifact removal. Select Thassa; do not force both costly engines.
- **Thassa versus Wonder:** Wonder's team-wide flying is powerful when in the yard alongside an Island, but it has to be deposited there and adds no Brass ETB/attack value. Thassa is useful when drawn or topdecked, repeatedly mills four by blinking Brass, can reuse Larcenist/Jhoira/Hostage Taker ETBs, and permanently retains Recruiter/Zara steals under the timing conditions above. Select Thassa despite losing a flying enabler.
- **Both setup tools versus Forerunner:** Forerunner's on-ETB tutor-to-top is real, but cannot alone put a Pirate from hand or library into the graveyard before combat. Looting has two precise discard casts; Ripples provides each-turn precombat graveyard feed. Retain both, remove Forerunner.
- **City versus Path:** 33 lands, same overall color access, but one fewer obligatory tapped early land; no claim City is strictly better in every board state. Retain Xander's Lounge as fetchable tri-land with cycling. Do not reduce land count further.
- **Merchant Raiders:** Keep. Its continual Pirate-entry lockdown is distinct from Thassa's end-step blink; reducing Pirate density further is not justified.
- **Unmarked Grave:** Strong `{1}{B}` tutor of a nonlegendary card into the graveyard, but cannot find legendary Jhoira, Zara, or other legends; existing Entomb, Buried Alive, two looting passes, Ripples and Brass ETB provide robust setup. A marginal further add lacks a clearly quality-positive cut.
- **Prismari Command versus Feed the Swarm:** Keep cheap unconditional enemy enchantment or creature removal; the Command is broader tempo but cannot remove large creatures or enchantments.
- **Ragavan versus Changeling Outcast:** Keep the unblockable 4/4 Brass return; Ragavan's payoff is blocker-dependent.
- **Jhoira versus Plunderer:** Retain the higher-ceiling commander-reanimated Pirate at the cost of natural-death Treasure. Avoid overstating this as mathematically established.

## Mechanical and source checks

- 100 physical cards, 97 distinct names; only Island, Mountain and Swamp are doubled (2 each). One commander; no companion.
- **33 actual front-face lands, eight rocks**, approximately 28 Pirates including commander and Changeling Outcast's all-zones changeling. Brass's Tunnel-Grinder is a front-face artifact, not a playable land drop from hand.
- Current Oracle snapshot on PR #651 covers every card except Thassa and City; those two are independently cross-checked against Wizards' Theros Beyond Death release notes and Scryfall card text, with records in `research_challengers/Admiral_Brass__Unsinkable_ChatGPT_Rev3_new_card_oracle.json`. All 100 are within UBR color identity and officially Commander legal; no project exceptions are used.
- No new Game Changers versus Rev2: Ancient Tomb, Cyclonic Rift, Demonic Tutor, Fierce Guardianship, Jeska's Will, Vampiric Tutor — six. **Power Bracket 4 (Optimized)**. **Archidekt tags:** Pirates / Reanimator / Aggro.
- Thassa's relevant ruling is **explicitly confirmed by Wizards**: an until-end-of-turn stolen creature is still controlled during end step, and Thassa returns that card under your control indefinitely; it is a new object and loses counters. [Wizards release notes](https://magic.wizards.com/en/news/feature/theros-beyond-death-release-notes-2020-01-10). Zara's delayed return requires correct trigger ordering; if the card leaves and returns, the trigger cannot track that new object.
- Finality replacement exiles a finality permanent that would die; bouncing/blinking produces a new object without counters. Siren's Ruse returns under **owner's** control, so do not use it to keep a stolen card. Thassa returns under **your** control.
- Candidate SHA, source bytes, eight exact swaps, legality/identity, land/Pirate/rock counts, and representative Oracle interactions are asserted by `tests/test_m7_admiral_brass_unsinkable_chatgpt_rev3.py`. It is not a simulation of multiplayer wins; no win rate is claimed.
- The canonical #3 registry has historical approved digest `e66e3a59…dd39` while the exact approved-source TXT has raw SHA `056f0369…72f5cc`. This known exception remains disclosed, not silently repaired. The Rev2 candidate raw SHA `baf0d451…84e967` is also preserved verbatim.

## Approval boundary

**NO owner approval yet.** No canonical replacement/lock, no merging a proposed review branch as if it were approval. Owner-facing exact Rev3 candidate raw SHA:

`dfa192cce0d925621e1cfa3f6444fb9da04c995700ca886e95a75c7347d4c7f7`

Ask Cory whether to approve **this exact full 100**, after reporting exact-head verification. "Proceed" alone is not approval. 
