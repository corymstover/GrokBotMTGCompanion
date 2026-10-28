# Deck #57 — The Rani M7 Rev1, independent owner-review packet

**Disposition: approval-ready candidate; UNAPPROVED.** No canonical update, no engineering merge prior to Cory's explicit approval of the exact raw 100. The separately approved Deck #56 revision and its unrelated global historical-transfer gate remain separate work.

## Authority and full-list reconciliation

- Canonical source: `corymstover/grixis-commander-encyclopediaGPT/main/refinement/decklists/The_Rani_Approved_2026-10-15.txt`, raw SHA-256 `7220937ed5817b4ef9cacd2463a3434b98ae58690ffa1d7ef440881ba97d729c`; reconciled byte-for-byte to the supplied Oct15 Archidekt ZIP with the canonical `[Commander]` tag restored.
- Revised proposal: `data/grixis/m7/candidate_lists/The_Rani_M7_Rev1.txt`, exact raw LF SHA-256 **`924296ed24fdc5e79431821d31a77134c5ed5c089a92cb5e69c78f78bde4fe27`**.
- Each is exactly **100 physical cards / 94 distinct names**, with only Island/Mountain/Swamp (3 each) duplicated. 33 lands unchanged. Commander identity U/B/R, 1 commander and no companion. Every selected name in the proposal is Commander-legal and Grixis according to the archived **104 distinct Scryfall source records collected 2026-10-27**; no project exception applies.
- Companion files: 99-library-physical-slot review CSV, 8/9/10-swap full alternative texts, decision JSON validated against the versioned M7 schema, source-bound `verify.py`, Scryfall source snapshot and dedicated exact-PR-head CI workflow. Historical M6 deep review covers all original 99 roles and 80 ranked pairings; M7 independently adjudicates the missing off-ranking challengers.

## Commander-first strategy

The Rani is not merely Grixis control. Her enter-or-attack creates a Mark of the Rani (+2/+2 and goad) on **another** creature; **any goaded creature**, regardless of goad source or controller, that deals combat damage to one of our opponents yields an investigate trigger. The plan points opponents at each other, gives those attacks evasion, and turns Clues into cards, artifact mana, Time Sieve turns or a finish. Thassa/Displacer Kitten create extra Marks; Academy Manufactor and Erdwal Illuminator multiply the tokens. This remains **Power Bracket 4 — Optimized**, not asserted cEDH.

## Eight selected one-for-one changes

| Add | Cut | Net gain and honest loss |
|---|---|---|
| **Frenzied Gorespawn** | Death Kiss | Five mana, goads one target from each opponent at entry, then grants menace to creatures attacking our opponents. Six-mana Death Kiss can yield larger damage in particular combat boards but is slower and lacks a 3-target immediate goad. |
| **Curse of Verbosity** | Maestros Confluence | One-blue low-cost political incentive: when the cursed player is attacked, we draw. Its attacker also draws when an opponent, so opponents may find answers. Confluence's flexible high-cost spell utility is sacrificed. |
| **Mirkwood Bats** | Grenzo, Havoc Raiser | Creation **or sacrifice** of every Clue/Food/Treasure/Mark token drains each opponent, converting the native engine into a win condition. Grenzo requires our own combat connections for goad/exile value and is a different risk profile. |
| **Cyberdrive Awakener** | Tangletrove Kelp | Costs six rather than seven, turns established Clues/artifacts into flying 4/4s for one explosive combat, and gives artifact creatures flying. **It does not grant haste**: artifacts newly created this turn cannot attack without independent haste. Kelp's 6/6 conversion is repeatable every combat and is lost. |
| **Alexios, Deimos of Kosmos** | Mocking Doppelganger | Mark Alexios so its compulsory opponent-turn attacks can investigate; it passes between players, gains counters/haste and cannot attack its owner. Loses an instant flash copy of an opponent's high-value creature; Alexios needs an actual Mark to be **goaded** for The Rani's Clue trigger. |
| **Marionette Apprentice** | Reanimate | Two-mana ongoing drain when Clue/artifact sacrifices go to graveyard; Time Sieve and clue cracking gain reach. Giving up one-mana creature recursion weakens recovery after wipes. |
| **Tamiyo's Journal** | Five Hundred Year Diary | Investigates each upkeep even when combat is blocked; three Clues plus tap search for any card. At five mana with a delayed first upkeep trigger it is slower, and loses Diary's large conditional blue-mana conversion. |
| **Roaming Throne** | Hateful Eidolon | Choose **Time Lord** (a single two-word creature subtype): Rani's enter/attack Mark trigger and combat-damage investigate trigger each trigger an additional time. Loses one-mana death-trigger draw for creatures enchanted with our Auras; Throne itself is four mana and Rani-dependent. |

These are eight *substantive* role replacements, not basic-land relabels or eight versions of a generic Grixis staple. Artifacts/tokens remain the primary closing resource; the new aerial route and drain lines do not require independent Oracle/Consult packages.

## Unselected serious challengers and complete higher-swap portfolios

- **Nine-swap alt** adds Spark Double over Slicer on top of all eight. Another nonlegendary Rani copies Mark/investigate triggers but loses Slicer's autonomous goaded attacks during opposing turns; that reduces baseline activation frequency if Rani is removed. Full valid 100 SHA: `a1538f965b4e5e641ce6e46e7c2dc436d720387fcac134e21e3cdd1ecd4b4db5`.
- **Ten-swap alt** additionally adds Idol of Oblivion over Mystical Tutor. Mark creation enables Idol tap-draw, but losing instant tutor access to Cyclonic Rift, Disrupt Decorum and protection while also removing Slicer harms recovery against combo/removal. Full valid 100 SHA: `91ffe20a97ba0f8813f50684c33d3ade48f77da80af1cc72848a5eff1f596fa6`.
- **Renegade Silent** over Vengeful Ancestor: recurring phased-out goad is real, but sacrifices Ancestor's flying and goad/attack damage output and is unavailable during opponents' turns.
- **Komainu Battle Armor** over Bloodthirsty Blade: mass goad through combat-damage ceiling, but much more mana and required connection versus Blade's immediate paid goad transfer.
- **Thopter Assembly** over Time Sieve would remove its own payoff and is incoherent. The Assembly/Sieve combo can take repeated extra turns if six mana is available **each** extra turn; its existence does not justify sacrificing goad/Clues or claiming one initial six-mana payment is infinite.

## Rules and adversarial scenario tests

1. **Mark target:** another creature must remain legal through resolution. Mark is an Aura token put attached without being cast; it can target a friendly creature. Marks survive Rani blink if attached elsewhere. Goad follows real attack restrictions, including attack taxes and available opponent choices.
2. **Throne:** choosing Time Lord doubles only the *triggered abilities of another qualifying creature* you control, including Rani. A goaded creature hitting an opponent causes two Rani investigate triggers, not two combat damage events. The Rani plus Erdwal Illuminator plus Academy Manufactor, on the **first goaded-hit event in a turn**, produces three investigations and **nine** artifacts (three each Clue/Food/Treasure); each further qualifying hit supplies two investigates/triples per investigate while Illuminator's first-time condition is spent.
3. **Bats/Apprentice:** Manufactor-generated Clue/Food/Treasure each count as separate token creation for Mirkwood Bats. When five artifacts are sacrificed to Time Sieve, each sacrificed **token** triggers Bats; Marionette Apprentice triggers for artifacts actually going to a graveyard. No automatic Clue card draw from Sieve sacrifices; each artifact gets spent once.
4. **Alexios:** own Mark goads Alexios even after it passes to other controllers; no assumption Alexios is inherently goaded. It must actually deal *combat damage* to our opponent for investigation. An opponent may still have blockers; Alexios cannot attack its **owner**, independently from the Mark restriction.
5. **Cyberdrive:** already-controlled noncreature Clues become artifact creatures 4/4 for this turn and have flying while Awakener is present. These do not gain haste; only artifacts controlled since the start of the turn (or receiving haste elsewhere) can attack. The card does not produce Clues or grant guaranteed lethal.
6. **Opponent counterplay:** a creature-poor fast combo table can deprive Rani of targets and damage; the protected Swan Song/Force/Mana Drain/Fierce/Deflecting package remains necessary. Pillowfort blocks goad; attack taxes need not be paid. Targeted enchantment/artifact removal breaks the engine. No full match win-rate or exhaustive opponent-agent simulation was run.
7. **Force of Will source correction retained:** twenty-three actually blue alternative nonland cards in the original deck, not the historically misreported twenty-eight; colorless mana rocks with blue identity are not blue pitch cards.

## Approval and merge boundary

This packet is a fully formed proposal for Cory's exact-list review. CI can verify structural/source-bound rules, but **does not approve** a deck. Do not alter the canonical approved source, owner receipt or `state/current_deck_overrides.json` until Cory explicitly approves **the exact 100-card raw SHA above**. If approved, merge the engineering evidence after exact-head checks, open a separate canonical approval PR, wait for its required certification gate and verify main without waiving historic errors or touching the other 61 locks.
