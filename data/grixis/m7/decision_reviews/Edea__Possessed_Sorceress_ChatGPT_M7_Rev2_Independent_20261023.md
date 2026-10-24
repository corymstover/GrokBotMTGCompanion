# Edea, Possessed Sorceress — ChatGPT independent M7 Rev2, 2026-10-23

**STATUS: REVIEW CANDIDATE — NOT CANONICAL, NOT OWNER APPROVED, NOT LOCKED.** This audit challenges GrokBot PR #664's exactly-five swap anchor and preserves specific Oct14 owner keep decisions. The October 14 canonical source remains immutable. Do not blind-merge the inherited #651–#664 stack.

## Source and exactness
- Current canonical main approved baseline: `refinement/decklists/Edea_Possessed_Sorceress_Approved_2026-10-14.txt`. Re-fetched byte-exact against GrokBot's vendored October 14 source; raw SHA-256 **`fd560a9b0777088b3ad1684ded030566c894faa206ddf6763b74d95d82c532e4`**.
- Grok firstpass engineering [PR #664](https://github.com/corymstover/GrokBotMTGCompanion/pull/664), head `cc2e6d45e5ad4a74b96d30ce07428144f8a111f4`. Its unapproved candidate raw `e8680cafc7b7500b6106677e1aaafce6d5035893ea9f0cd335cd1fa1ff5227a2`. Critically, it cut Oct14 owner-kept **Evereth** and **High Market** and also cut **Ayara**, reducing repeatable sac-outlet density from ~10 to ~7 by its own model.
- **ChatGPT independent Rev2** complete list: `data/grixis/m7/candidate_lists/Edea__Possessed_Sorceress_ChatGPT_M7_Rev2_20261023.txt` with raw SHA-256 **`a039a79c6205c3dc61e0e237816d0d6b0168061b850cb8ca4a598483150b3f54`**.
- Archived 2026-10-23 *live* Scryfall from GrokBot's 260-name saved selection, separately filtered across all 94 candidate named entries. Zero Oracle ID/text mismatches against its frozen reference at time of snapshot. This is a current archived primary-source check, not a second independent Scryfall pull. All 94 named cards Commander legal in UBR, no exception.
- EDHREC Edea commander main/top/high lift considered (archived `Edea__Possessed_Sorceress_EDHREC_discovery_20261023.json`, plus today's https://edhrec.com/commanders/edea-possessed-sorceress ). Its high lift for Industrial Advancement, Chaos Shrine's Black Crystal, Illuminor Szeras, Kethek is already represented in the baseline and preserved; popularity never mandates addition. Owner-removed/rejected Marchesa-style line, Conjurer's Closet, Nasty End, Rhystic Study, clone saturation not reintroduced.

## Five material revisions relative to October 14 baseline

| Add | Cut | Strategic logic and disclosed loss |
|---|---|---|
| **Aggravated Assault** | **Mass Mutiny** | Repeatable 5-mana extra combat and full creature untap; Edea steals again at *each* beginning of combat. Mass Mutiny is a potent one-shot 5-mana theft from up to each opponent, sometimes stronger immediately with multiple sacrifice outlets. This consciously trades burst for repeated commander-specific triggers, **retaining owner-kept Evereth** rather than cutting it. |
| **Kaya's Ghostform** | **Zara, Renegade Recruiter** | One-black-mana aura on Edea's temporarily stolen creature plus an in-turn sac outlet yields a permanent steal. Order Ghostform's death trigger to return the card under *our* control before Edea's death trigger; Edea still draws when card no longer exists in graveyard. Zara is a 5-mana attack-based hand creature theft engine; its high ceiling is acknowledged, but it cannot rescue an Edea borrow permanently as efficiently. |
| **Hall of Echoes** | **Shipwreck Marsh** | A late-game **land** with `{5}` activation to copy Edea and temporarily waive legend rule; 2 theft triggers per combat (or more with extra combats). Crucially **High Market remains** as owner's land-based sacrifice outlet. Real cost: lose an untapped-after-two-lands U/B dual and go from approx U19/B19/R18 to **U18/B18/R18** colored sources, with another colorless utility land and vulnerability when Hall becomes a creature. |
| **Geyadrone Dihada** | **Village Rites** | Four-mana planeswalker whose −3 steals target creature or planeswalker (not restricted to already-corrupted objects); +1 prepares permanents for late −7 permanent theft. Edea's player-specific theft density and persistence improve, trading away highly efficient {B} instant sac/draw-two plus Edea's additional death draw. Remaining repeatable sacrifice infrastructure and Corrupted Conviction/Deadly Dispute cover its role. **Ayara is retained** rather than being cut. |
| **Combat Celebrant** | **Seize the Spotlight** | Three-mana repeatable-ish combat source; exert on attack untaps *other* creatures and provides an additional combat, another Edea theft. It skips its next normal untap unless separate untaps intervene and needs an attack to trigger. Spotlight can produce up to three borrowed creatures or cards and Treasures immediately, but opponents choose and its effect happens once. |

### Critical preserved cards

- **Evereth, Viceroy of Plunder**: continuously sacrifices another creature/artifact at sorcery speed, grows, eventually drains all opponents on its death; Oct14 owner KEEP.
- **High Market**: instant-speed land-based sacrifice of Edea's borrowed creature for a death-trigger draw; Oct14 owner KEEP. Edea's prior original land choice is retained.
- **Ayara, Widow of the Realm // Ayara, Furnace Queen**: tapped sacrifice outlet draining target and transforming into a recursive combat engine. Grok also cut her, compounding outlet loss. She is retained.
- Also preserve Ashnod's/Phyrexian Altars, Phyrexian Tower, Goblin Bombardment, Warren Soultrader, Illuminor Szeras, Viscera Seer, Braids and other established death-payoff infrastructure. The candidate removes **no repeatable sacrifice outlet** from the October 14 baseline.

## Quantified gates, mechanical boundaries

- **100 physical**, **94 distinct names/rows**, only Island×3, Mountain×3, Swamp×3; **35 lands**, **six rocks** (Sol Ring, Arcane Signet, Fellwar Stone and three Talismans), **3 Game Changers**: Ancient Tomb, Demonic Tutor, Fierce Guardianship. No project exception. Natural **Power Bracket 4 — Optimized**; Archidekt tags Theft / Extra Combats / Aristocrats.
- Lost Shipwreck Marsh U/B dual, but 35-land count remains intact. Reproducible deterministic 140k no-mulligan, no-sequencing hand-access sample estimates UBR five-mana source feasibility by cards 11/12 ~49.7%/59.7% baseline vs ~49.0%/58.9% Rev2, approximately **0.7–0.8 percentage points** cost. It treats some source availability optimistically and is **not a win rate** or exact cast-by-turn probability.
- Edea is 2/5 ward {2}; at beginning of combat *on your turn*, borrow an opposing creature, untap, haste to EOT. Borrowed creature death -> return under owner's control + draw. If other triggers move it before Edea's resolves, Edea still draws but cannot move a new object.
- Additional combat phases each have a beginning of combat step, so Edea can steal more than once per turn. Aggravated Assault activation only at sorcery speed in a main phase; Combat Celebrant's exert occurs only as it attacks and it does not untap itself with its own ability.
- Ghostform requires controlled creature when enchanting; sacrifice borrowed target *before* temporary control expires or the aura won't remain attached. Ordering two dies triggers matters; no claim of a delayed Marchesa effect.
- Hall of Echoes requires five mana per activation, can only copy a creature you control, and is a targetable creature when copying Edea. It doesn't become a permanent Edea copy through turn end. Legend suppression for the turn means neither Edea is lost solely to the legend rule.
- The five-swap presentation floor was **not** a cap. Other archive-tested candidates and off-ranking high lift were examined; no further honest quality-positive swap of a specific preserved slot cleared the tradeoff threshold.
- **No game engine, no multiplayer win-rate or matched-shuffle simulation, no independent third-model Pass C claim, no blanket full-suite green claim.**

## Required owner approval protocol

This research PR adds source-bound evidence, a separate Rev2 100-card TXT, narrow tests, and review; it does **not** replace GrokBot's saved first-pass candidate or authorize canonical changes. Cory must explicitly approve the complete **exact SHA** `a039a79c6205c3dc61e0e237816d0d6b0168061b850cb8ca4a598483150b3f54` before a separate canonical approval PR/merge/main raw rehash. If he prefers Mass Mutiny, Village Rites, Shipwreck Marsh or any other slot, reopen Edea's Rev2 before locking.
