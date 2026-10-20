# M6 two-model advisory reconciliation — Doctor Doom, King of Latveria (tracker #12)

**Date:** 2026-10-20 · **review class:** transparent two-model engineering evidence, **NOT formal independent Pass C**.
**Canonical status:** APPROVED / LOCKED. NO CHANGES AUTHORIZED OR MADE.
**Exact canonical approved RAW SHA-256:** `c97bd448aa4b18d2f7ed15e5d67006ab320ed67ad3ed267e44150de472e1dc58`.
**Authoritative file:** `corymstover/grixis-commander-encyclopediaGPT/main/refinement/decklists/Doctor_Doom_King_of_Latveria_Approved_2026-10-14.txt`, blob `324fdb3070be086b89a99a1cc3dcab33f92c08e6`; canonical `main/state/current_deck_overrides.json#Doctor_Doom__King_of_Latveria`, blob `81801b2f9d3387b171c01f1fcae255b385a5b698`.
**Logical source SHA:** `lh1:bdc7cc1f7dc0eeb6866bf80ada6790b5d21339bb63058b80321f352a874a3eca`, not RAW SHA.
**Original comprehensive review:** `data/grixis/m6/deep_reviews/Doctor_Doom__King_of_Latveria.md`, blob `7ca85ae5d2176d328b96283fecbbd56f530e952d`; concluded KEEP and examined exact land-discard effects.
**GrokBot advisory:** `data/grixis/m6/grokbot_pass_c_advisory/Doctor_Doom__King_of_Latveria.md`, blob `67f3593e4084081529efe01068627ec37c890418`; NEEDS VERIFICATION, no swap, suspected Dec 18, 2026 future-release and target-Villain assumptions. First pass disclosed prior blueprint/engineering exposure, no qualified independence.
**Verdict: KEEP, rules verified; material advisory legality-date premise CORRECTED.** No owner approval required because there is no change.

**Actual model comparison:** GrokBot's disclosed advisory critic flagged the December promo date, while the prior ChatGPT-authored comprehensive review identified the original June 2026 released commander. This source disagreement is resolved using Wizards' original decklists and printing chronology. Both critics have prior involvement; the present reconciliation is NOT formally independent Pass C.

## Independent exact-source/legality findings

The canonical approved TXT read live from `main` has **100 card lines, all 1x, 100 distinct names**, one commander plus 99 library. Source-based 38 lands includes **Villainous Hideout**, an actual LAND and color-restricted Villain utility source. `Doctor Doom` (short distinct title) is a different listed noncommander card from `Doctor Doom, King of Latveria`; preserve both, and similarly don't alias/rename the literal `Norman Osborn // Green Goblin` card. Current canonical hash matches GrokBot's source and October 14 complete gate. Official Commander legality and UBR identity of all 100 were previously audited on Oct14; this reconciliation independently checks the specific disputed commander's official publication and legality, target rules and core synergies; it does not falsely claim a new 100-card live Scryfall collection audit.

### CRITICAL correction: December 18 is a **later promo printing date**, not this card's initial release / Commander legality date

GrokBot flagged a purported Scryfall `released_at=2026-12-18` for Doctor Doom and questioned the project's earlier `2026-11-13` future exception. This mixes **printings of the same card**:
- Wizards official `Marvel Super Heroes Commander Decklists` names **Doctor Doom, King of Latveria** as the headliner of **Doom Prevails** and states **Magic: The Gathering | Marvel Super Heroes released on June 26, 2026**. The same date appears in Wizards product/release notes.
- The **actual card's MSC #6 first-printed commander edition** records **release June 26, 2026**, its Commander status **legal**, and relevant Oracle.
- A **different media/collaboration promotional printing** of the **same card name**, catalog `pmei/2026-26`, records `released_at=2026-12-18`, a later specific printing, not a new Commander-eligible card debut or reason to downgrade existing MSC printing legality. A Scryfall lookup returning that promo date is not evidence that the Doom commander is unreleased.
- Therefore **as of Oct 20, 2026 the already-released Doctor Doom commander is officially Commander-legal**, not merely project-permitted as future commander. The 2026-11-13 Mystery Booster Commander Edition special treatment refers to *different cards and release chronology* (e.g., Madcap Jester/Tresserhorn); it should NOT be projected onto this prior June 2026 Marvel Commander release. A not-yet-available later promotional *art/printing* may be forthcoming; don't falsely claim it was physically available in October.
- This distinction resolves GrokBot's NEEDS VERIFICATION legality flag. It is a source selection/release-date error, **not** a newly authorized project exception and not a defect in the October 14 canonical deck.

**External primary authority:**
- [Wizards published Marvel Super Heroes Commander decklists with Doctor Doom and the June 26 release](https://magic.wizards.com/en/news/announcements/marvel-super-heroes-commander-decklists).
- [Wizards product and official prerelease/release notes](https://magic.wizards.com/en/news/feature/marvel-super-heroes-release-notes).
- [MSC #6 actual original Doctor Doom printing, June 26, Commander legal](https://mtg.wtf/card/msc/6/Doctor-Doom-King-of-Latveria).
- [Later December 18 promo printing of the same exact card](https://mtg.wtf/card/pmei/2026-26/Doctor-Doom-King-of-Latveria).

## Villain target, connive, and independent land-discard trigger

**Oracle, verified:** Doctor Doom, King of Latveria {1}{U}{B}{R}, 3/3 Human Noble **Villain**:
1. "**Whenever you discard one or more land cards, each opponent loses 2 life.**"
2. "**At the beginning of combat on your turn, target Villain you control gains menace until end of turn. It connives.**"

- **Legal self-target:** Since Doom is itself a Villain and under its owner's control, its triggered ability at own combat can target **Doom itself** (if still on field when triggers are placed). It is false to require a second Villain. GrokBot's bare "always has a target" needs qualification: Doom must still be an eligible controlled Villain when targets are selected; if Doom or chosen other Villain leaves or ceases to be legal *before resolution*, there is **no alternative retargeting** merely because another Villain exists, and if the only target is illegal the ability fails, **no menace or connive/draw/discard**. If another Villain is chosen, removing Doom itself after the trigger may leave the triggered connive able to resolve; however Doom will no longer generate its own land-discard life-loss trigger if absent when that discard occurs.
- **Connive order:** Target Villain **draws one and discards one**, and gains +1/+1 **only if the discarded card was nonland**. If a **land** is discarded with Doom under control, every opponent loses 2 by Doom's independent triggered ability, **but connive gives no +1/+1 counter** from that land discard. The grant of menace does not require entering combat/damage, and the target may be Doom himself for a repeatable once-per-combat discard opportunity. Menace is not guaranteed unblockable.
- **Per-event, not per-land:** One discard event with **3 lands simultaneously**, e.g. a Wheel of Fortune hand discard, creates **one** Doom land-discard trigger, so each opponent loses **2**, not six. Separately activated Seismic Assault discard-a-land costs made three times create **three distinct events** and three Doom triggers, so each opponent loses **6**, barring removal/interactions. The triggers are on the stack and can be answered. The **noncombat life loss** cannot be treated as damage, redirects/damage doublers without specific text or commander combat damage. The targeted Villain connive trigger itself is optional? Trigger happens and requires legal Villain target; connive action is instructed, no optional "may" in Oracle.
- **Land cycle and tech accuracy:** `Tectonic Reformation` gives land cards in hand cycling {R}; cycling Dakmor Salvage discards it as cost, a separate Doom event. `Surly Badgersaur` on discarded land creates Treasure; the cycling draw can be replaced with **dredge 2** *if Dakmor in grave and at least two cards in library*, returning it to hand. The independent cycling sequence is **bounded by library size and ability to continue milling cards**, and separate from opponent loss. No automatically unbounded infinite mana/loss from a finite library. `Monument to Endurance` can only choose each of its three modes once **per turn**, not one Treasure/damage mode per arbitrary discard indefinitely. `Containment Construct` or Currency Converter exiling the same discarded Dakmor from grave interrupts dredge until moved back; don't double count both.
- **Roaming Throne** chooses Villain and may cause an additional Doom trigger on one qualifying land-discard event, but doesn't increase land discards or automatically connive twice unless the relevant triggered ability itself is copied/doubled; ordinary one-land event with Throne+Doom has two life-loss triggers of 2 each, **4 lost per opponent** if both resolve.
- **Villainous Hideout** is a LAND, produces generic colorless or constrained colored for Villain casts/ability costs, and has an activated target-Villain connive option with sorcery timing. It is not a generic any-purpose untapped Grixis source. Source includes on-identity Villains `Baron Strucker`, `Loki`, `Green Goblin` etc., but the only required Villain for the commander combat trigger is Doom himself while present.

### Rules and card source authority

- [Wizards full Marvel Super Heroes release notes](https://magic.wizards.com/en/news/feature/marvel-super-heroes-release-notes) includes Doom's exact text/ruling: illegal target -> no discard.
- [Doctor Doom original legal card Oracle](https://mtg.wtf/card/msc/6/Doctor-Doom-King-of-Latveria).
- [Wizards Comprehensive Rules](https://magic.wizards.com/en/rules).
- Exact original authored 100-row card matrix in `data/grixis/m6/deep_reviews/Doctor_Doom__King_of_Latveria.md`, independently authored Oct 19, contains effective line for `Tectonic Reformation+Badgersaur+Dakmor` and limitation for `Monument`; checked again for conceptual errors here.

## Commander-first strategic reappraisal

The approved 100 deliberately exploits:
- reliable **land discard events** from Doom's self-connive, Seismic Assault, Trade Routes, Tectonic Reformation, Demand Answers, Faithless Looting, Frantic Search and Villain-dependent engines;
- sustained lands-to-hand access, Dakmor dredge and repeatable discard benefits (Bone Miser, Surly Badgersaur, Monument, Moonstone);
- thematic Villain attacks, additional connive engines, repeatable 2-per-opponent attrition and high-density card selection;
- the mana/tutors/protection needed to deploy a four-MV Grixis commander and retain blue/red/black activation access.

The author proposed no forced generic turbo conversion; GrokBot proposed no incumbent swap and explicitly found mana/land-discard suite coherent. A high-rank candidate missing the combined Villain+land-discard requirement cannot be assumed better. No new evidence of a card strictly beating a named incumbent was found from the two records. Legitimate open research axes are timing of land-discard events in realistic games and interruptions to the bounded dredge line; no win-rate or effect-aware replacement evidence exists to justify reopening this approved deck.

**Final disposition: KEEP (rules/legality FLAG RESOLVED).**
- Commander official legal since June 26, 2026; **DO NOT** invent Dec 18 or November 13 future-release exception.
- Target on self legal; targets can fail when gone; connive order and per-discard-event life loss independently verified.
- All 100 copies/100 distinct preserved; no proposed owner swap or additional legality blocker currently demonstrated.
- Keep bracket **4 — Optimized**, land-discard/Villain/connive identity.
- **Remaining formal gates:** independent Pass C remains 0/62; effect-aware Phase B partial; no M6 certificate. No canonical/hash/approval edits, no project-exception rewrite, no prior review/advisory modification.

## Exact-head evidence CI provenance
The M6 evidence-only integrity workflow was established by engineering PR #354, merge `76c8236b8e35657824df65d258e0a5f7a5c51aa6`. It verifies branch-changed path scope, SHA/source and independence disclosures, approved 62/source-ledger integrity and unmodified formal certification fields. **This reconciliation/review protocol is NOT formally independent Pass C, and a CI PASS is NOT an MTG strategy or current Oracle-complete certification.** Canonical deck approvals remain untouched.

## Exact-head evidence CI provenance
The M6 evidence-only integrity workflow was established by engineering PR #354, merge `76c8236b8e35657824df65d258e0a5f7a5c51aa6`. It checks changed-file scope, approved-source SHA receipts, disclosure of reviewer overlap, and preserved formal certification state. **This reconciliation/review protocol is NOT formally independent Pass C; a CI PASS is NOT a strategy or full Oracle certification.** Canonical deck approvals remain untouched.
