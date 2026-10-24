# Inalla, Archmage Ritualist — independent M7 second research pass (2026-10-24)

**Disposition: RESEARCH_ONLY; below five defensible material upgrades. No owner approval. No canonical changes.**

This is a source-bound follow-up to PR #698's first independent review and Grok PR #671, not a retroactive edit of the October 14 owner decisions. As of this pass, decks #1–22 are newly M7 owner-approved and canonical locked. Inalla's historical exact 100 remains the approved source (raw SHA-256 `81333ac71d483b667af968bf2ab221e1fa0de6edd7c2395170d15786e5b15fa3`, **no final LF**). All three complete alternatives here are **research artifacts, not approval candidates**.

## Why this second pass was necessary

Grok's 2026-10-23 candidate-specific Scryfall/EDHREC archive covered 204 cards, but did **not** contain the printed 2026 `Flashback` instant. The first ChatGPT pass focused on the weaker `Dualcaster Mage` reverse-owner-cut proposal and missed a much more efficient Spellseeker-compatible recursion tool. Fresh sources: 250 oracle-normalized six-month Inalla tournament decks aggregated through **2026-10-17** by [cEDHStats](https://cedhstats.org/commanders/inalla-archmage-ritualist/cards), plus **five individual independently listed 100-card October 4–12 tournament submissions** on [MTGTop8](https://mtgtop8.com/archetype?a=1209&f=cEDH&meta=344). Tournament aggregation, selections and correlation **do not prove causal card quality or win rate**.

### High-conviction addition — Flashback / Kefka

- `Flashback` (SOS #115) is a **{R} instant**: target instant/sorcery card in your graveyard gains flashback for the turn at its mana cost. It can be found by the already-essential `Spellseeker` (mana value 1) or generic tutors, and lets the deck recast spent `Culling the Weak`, `Burnt Offering`, `Unearth`, `Entomb`, `Reanimate` or protective stack interaction when their targeting and timing conditions are met.
- The card is official Commander-legal, red identity, released April 2026. Source card: [official Gatherer SOS #115](https://gatherer.wizards.com/SOS/en-us/115/flashback), [Scryfall card](https://scryfall.com/card/sos/115/flashback), [Wizards SOS Commander legality and flashback timing notes](https://magic.wizards.com/en/news/feature/secrets-of-strixhaven-release-notes).
- **Loss:** Cut `Kefka, Court Mage // Kefka, Ruler of Ruin` removes a five-mana Wizard with Inalla-copyable discard/draw ETB and repeatable attack card advantage. It was an intentional October 14 owner addition. One mana accessible via Spellseeker is a stronger *combo-resilience* role than that five-mana value role, but no outcome simulation was performed.
- Flashback's granted cost is **paid**, not free; the flashback-cast card is exiled instead of returning to the graveyard; sorcery timing still applies. A generic extra spell does **not** automatically fix every disrupted Spellseeker chain.
- Adoption clues: 115/250 (46%) tournament Inalla lists used Flashback; 109/250 (43.6%) used Kefka; **2/5** sampled fresh recent lists used Flashback. This is contextual, not decision by popularity.

### Serious commander-relevant alternate line — Corpse Dance / Final Fortune

- `Corpse Dance` {2}{B} instant with **{2} buyback** reanimates the **top creature card** of the graveyard, gives haste and exiles that creature at next end step if still on battlefield.
- With `Scholar of the Ages` on battlefield, `Burnt Offering` and Corpse Dance in hand, enough black/other mana and no creature-graveyard reorder, sacrificing Scholar to Burnt Offering and recasting Corpse Dance **with buyback** returns Scholar; its ETB returns Burnt Offering plus another instant/sorcery. This is a documented repeatable, net-positive mana, storm and recursion loop. [Commander Spellbook / EDHREC indexed exact three-card combo](https://edhrec.com/combos/grixis/313-813-1777). Inalla's Eminence can exploit repeated Wizard ETBs where mana permits.
- **Loss:** `Final Fortune` {R}{R} is an unusually cheap extra turn and lets a turbo line win before the loss trigger. Corpse Dance has a higher upfront price (five with buyback), graveyard-order fragility, and overlap with `Shallow Grave`. Both roles are powerful; a matchup-agnostic **net upgrade is not established**. Owner explicitly added Final Fortune October 14.
- Corpse Dance appeared in **151/250 (60.4%)** tournament Inalla lists, 3/5 new sampled lists; Final Fortune **136/250 (54.4%)**, 3/5 sampled. Not decisive, but stronger than a popularity-only bluff.

### Mana sensitivity swaps (conditionally promising)

1. **Forbidden Orchard / Exotic Orchard:** Orchard makes any color unconditionally and enters untapped, unlike Exotic's colors depending on opponents. The price is giving an opponent a **1/1 blocker / sacrifice resource** each time it makes colored mana, which can interfere with the retained `Ragavan` or help an opposing combo. The five Oct lists used Forbidden in 3, Exotic in 1. Different table composition changes the answer.
2. **Starting Town / Island:** Town offers any color on turns one through three at one life and enters untapped then, fixing early U/B/R requirements; after turn three, an unplayed Town enters tapped. Cutting the basic Island loses a fetchable untapped blue and resilience to nonbasic hate. 4/5 fresh Oct lists used Town and 0/5 used basic Island, but this does **not** measure a turn-four miss probability.
3. The joint 27-land replacement is **not** a free increase in raw mana sources: 27 stays 27 and the remaining basic `Swamp` stays. Such swaps should be compared with actual early-turn color need and board-state costs; no multiplayer win rate is claimed.

### Fifth-slot challenge rejected — Pyroblast / Red Elemental Blast

- Both cost {R} and answer blue spells/permanents. `Pyroblast` can legally target nonblue objects and still counts as a cast toward storm/Breach, but does nothing to a nonblue target; `Red Elemental Blast` can only target blue, making some hostile redirection of its target illegal. Pyro is not strictly better.
- In cEDHStats, `Red Elemental Blast` was in 190/250 (76%), vs `Pyroblast` 82/250 (32.8%), and **all five** fresh lists kept REB while **two** also played Pyro. The evidence weighs against replacing the existing REB just to hit a numeric minimum. The 5-swap file is therefore stress only.
- Reopening the October 14 `Dualcaster Mage` cut also became less attractive: only 21/250 (8.4%) tournament decks used it, and the raw association was **−0.47 PPG** with stated 90% interval [−0.78, −0.13]; this is confounded observational data, **not proof Dualcaster lowers match performance**. It does yield two Commander Spellbook variants with already-retained Saw in Half/Essence Flux, but unlike Flashback it costs {1}{R}{R}, requires a copy target, and its reversal would override an express owner cut. No longer our lead upgrade.

### Other high-signal challengers not worth forcing in

- **Gifts Ungiven / Ad Nauseam:** a 3U Gifts pile of `Spellseeker`, `Step Through`, `Reanimate`, `Unearth` guarantees a *nominal* Spellseeker-access route across any two/two split (if all four are in library and graveyard access/casts are available). But Ad Nauseam is a uniquely powerful mass refuel/fast win engine; deleting it on mere 47.6% vs 39.2% tournament inclusion would be false certainty.
- **Buried Alive / Lim-Dûl's Vault or acceleration:** Buried Alive assembles multiple graveyard Wizards but costs three, is sorcery speed and depends on recursion; Vault finds **any** needed card at instant speed for UB. No clean cut.
- **Apprentice Necromancer / Corpse Dance:** Apprentice is an intentional owner-retained **Wizard**, and Inalla's hasty token copy can activate its tap/sac reanimation ability immediately. Not a clean 1:1 upgrade.
- **Defense Grid / Hexing Squelcher:** Grid taxes off-turn spells including our own responses; Squelcher stops countering proactively and is an owner-selected shield. Not a clean 1:1 upgrade.
- **Exhibition Tidecaller / Blood Pet:** Tidecaller fuels Breach but removes a creature/sac mana resource and costs an extra Eminence payment to double up.

## Whole-100 staged alternatives — exact, not canonical

| Artifact | Source-bound swaps | 100 / singleton / lands | Exact raw SHA-256 | Disposition |
|---|---|---|---|---|
| `Inalla__Archmage_Ritualist_M7_Flashback_One_Swap_20261024.txt` | Flashback over Kefka | 100 / 100 / 27 | `0bbe50e990f58ea36c9cb0a0c442dba3cc41fe9cf9580fffe08d095834b75e51` | strong single challenger; below floor |
| `Inalla__Archmage_Ritualist_M7_Four_Swap_Combat_20261024.txt` | Flashback/Kefka; Corpse Dance/Final Fortune; Forbidden Orchard/Exotic Orchard; Starting Town/Island | 100 / 100 / 27 | `fa7e1434332b0abdf5cdbd656c4483c02ce76f7431342116a0e9b0c426633d00` | conditional quality-positive contenders; **below floor** |
| `Inalla__Archmage_Ritualist_M7_Five_Swap_Stress_NotApproved_20261024.txt` | above plus Pyroblast/REB | 100 / 100 / 27 | `0327b8413ca38182b4710346087d7f35f5e0c6cfee1bd0af90fc61c757c181bb` | explicit **reject**: fifth not established |

All files use LF-terminated one-card-per-line `1x` format, commander on first line, and preserve Inalla's Spellseeker/Scholar/Finale, Bloodline/Ruthless and Breach/Oracle cores. The Oct23 Scryfall source binds every non-Flashback card, and the newly found Flashback is separately documented by current official Wizards and Scryfall sources. There is **no** new canonical 100 SHA authorized by Cory. Existing October 14 list and all 22 newer locks are untouched.

**Final research gate:** structural/mechanical review yields at most four context-dependent credible replacements, with fewer wholly proven net gains. The five-swap floor is **not met**. Keep Deck #23 at **RESEARCH_ONLY** until a genuinely better fifth and complete approval gate. Do not turn a fifth mediocre change into a fake optimization. Power Bracket **5 — cEDH**; Archidekt tags **Spellseeker Combo / Reanimator / Turbo**. No exception, no simulated multiplayer win-rate, no independent third-model signoff.