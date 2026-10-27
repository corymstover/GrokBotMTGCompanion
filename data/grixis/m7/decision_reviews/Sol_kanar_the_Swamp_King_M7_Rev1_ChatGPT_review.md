# Deck #52 — Sol'kanar the Swamp King — M7 Rev1 owner-review candidate

**Status:** REVIEW / NOT OWNER-APPROVED. Do not merge this PR or mutate canonical approval/lock state before Cory explicitly approves the exact raw SHA.
**Date:** 2026-10-27 (America/Chicago)
**Canonical predecessor:** `corymstover/grixis-commander-encyclopediaGPT`, `refinement/decklists/Solkanar_the_Swamp_King_Approved_2026-10-15.txt`; original raw SHA-256 `7d39fff42b91263e83415feef1e69d048c54f8b4e2226b8430fb584076d19106`.
**Proposed M7 raw SHA-256:** `f7ff68f912839accc7177c288536c9abf9deefc8332d975236ef6f028b6f0e02`.
**Candidate:** `data/grixis/m7/candidate_lists/Sol_kanar_the_Swamp_King_M7_Rev1.txt`.
**Source-bound oracle metadata:** `data/grixis/m7/oracle_snapshots/Sol_kanar_the_Swamp_King_M7_Rev1_2026-10-15.json` (Scryfall oracle_cards snapshot, not a live October 27 mass query).

## The commander-first reconstruction

Sol'kanar is {2}{U}{B}{R}, 5/5 Demon, swampwalk, and **gains 1 life whenever ANY player casts a black spell** (but not when Sol'kanar itself is cast). Maximize the frequency and payoff of those gain events, preserve Painter's Servant naming black plus Demon's Horn, turn opponent Swamps into unblockable 21-damage combat, and use paid life as a resource rather than only accumulating life. Retain Cabal Coffers/Crypt Ghast/Urborg/Blanket/typed Swamps, both gain-loss feedback families, Grindstone, Top/Citadel/Aetherflux and graveyard interaction. Do not convert into an unrelated Thoracle/Breach shell.

## Seven material one-for-one replacements

| Cut | Add | Commander-specific value and cost |
|---|---|---|
| Alhammarret's Archive | Necropotence | 5→3 MV black draw engine. The lifegain engine can replenish life paid to see cards. Real cost: no draw step, discard exile, and delayed cards only at next end step rather than immediately; Archive's doubling of life gain/draws is lost. |
| Underworld Dreams | Orcish Bowmasters | BBB passive wheel damage becomes 1B flash black interaction, creature/Army board presence and opponent extra-draw punishment. Pairing with Windfall/Wheel also starts Exquisite Blood gain chains. Loses unconditional passive damage on normal opponent draw steps. |
| Bontu's Monument | Rowan, Scion of War | Original 3-MV colorless Monument discounts only black creatures and drains on creature casts (low creature density). 3-MV BR Rowan converts the *life lost this turn* through Necropotence, K'rrik, Ancient Tomb, pain lands or Black Market Connections into generic-mana reduction for black/red spells, including Exsanguinate/Torment. Requires surviving a turn, tapping at sorcery speed, and does not discount colored pips. |
| Bloodletter of Aclazotz | Hatred | Swampwalk plus 5-power Sol'kanar gives a commander-centric kill with +16 power if a defending player controls a Swamp (Urborg/Blanket supply it). Black instant also triggers Sol'kanar while present. Costs five mana **and 16 life up front**, exposes the caster to removal/counterplay; do not represent as guaranteed. Loses Bloodletter's on-turn life-loss multiplier. |
| Dimir Signet | Yawgmoth's Will | Trade a blue/black 2-mana rock for a 2B spell that reuses cheap black spells, Dark Ritual, tutors and artifacts in one turn, allowing more Sol'kanar and Horn triggers. Strong recovery and sequencing, but removes persistent colored ramp and Will exiles cards that would enter graveyard that turn. |
| Rakdos Signet | Mindcrank | Replace a second color-fixing 2-mana rock with a 2-mana artifact that converts every opponent life-loss event into mill; pairs with already-included Bloodchief Ascension at three quest counters for a library-bounded life-loss/mill feedback finish. This is an *additional* compact payoff, not falsely presented as an unlimited loop or the core commander identity. Loses persistent BR fixing. |
| Talisman of Creativity | Bubbling Muck | Replace off-black UR ramp with a B spell that doubles black production when Swamps are tapped that turn, scaling the existing 15 Swamp-typed land/fetch infrastructure and Urborg/Blanket conversion into X-drain spells. It is temporary and symmetrical for players who tap Swamps during that turn; not a permanent rock. |

**Net structural effects:** 100 physical / 95 distinct names; exactly Swamp×6 repeats, one commander; 35 front-face lands plus 1 Fell Mire back-face (36 land-capable); 92 of 99 noncommander physical slots retained, 7 changed. 15 current archived Game Changers; all allowed for Bracket 4. No extra project legality exception.

## Audit and red-team

- All 99 baseline noncommander physical copies were compared with the commander blueprint (92 RETAIN, 7 REPLACE). Scryfall-source index checked all 95 proposed names: 95 legal Commander entries, 95 within colorless/UBR identities, no unknown/unresolved source name. Current hash is a raw UTF-8 LF file with commander first; only Swamp repeats. Archive timestamp 2026-10-15. **No new 2026-10-27 bulk Oracle pull is claimed.**
- Explicit adversarial cost: cutting three two-mana color-fixing rocks reduces early colored acceleration and makes some hands more reliant on 35 lands, Chrome Mox/Mox Diamond/Arcane Signet, black rituals, Soul Stone and the two remaining Talismans. BMC/Crypt Ghast/Coffers remain. This is a calculated shift to commander-centric black output, not a claim of measured multiplayer win-rate improvement.
- Scryfall Oracle: Necropotence's exiled cards enter hand at next end step; Rowan discounts generic components only and counts gross lost life not net life change; Bubbling Muck affects every player's Swamps; Yawgmoth's Will replacements exile cards moved to graveyards that turn; Hatred pays life as an additional cost that is lost even if countered. Rules tested analytically against archived Oracle/rulings.
- Bloodchief Ascension needs three counters and a card to enter an opponent's graveyard to create life-loss trigger; Mindcrank mills that life loss. If the library is depleted before lethal life loss, no more card-move triggers, so it is not an unbounded infinite.
- Painter's Servant naming black causes all spells (including opponents' nonblack spells) to be black and trigger Sol'kanar and Demon's Horn separately; their life gain creates multiple Vito/Enduring Tenacity/Cleric/Blight-Priest gain events.
- Commander necessity: without Sol'kanar, Demon's Horn/Painter still function, but the deck loses a second opponent-wide black-spell gain trigger and the specific unblockable Hatred commander kill. The two distinct functions preserve a meaningful command-zone advantage.
- Sorin of House Markov was discovered as a superficially attractive lifegain challenger, but **REJECTED ILLEGAL**: its back-face Sorin, Ravenous Neonate has a white/black color indicator. White color identity violates UBR even though the extort symbol in reminder text is ignored.
- REJECTED higher-swap portfolio A: Well of Lost Dreams over Witch of the Moors adds paid card drawing but removes repeat end-step recursion/opponent sacrifice and duplicates existing draw engines; core Witch kept.
- REJECTED higher-swap portfolio B: Lake of the Dead over Bojuka Bog would accelerate black big-mana lines but forces Swamp sacrifice on entry/activation and removes the immediate land-based graveyard exile. Bog kept, with Rakdos Charm still available.
- REJECTED: Sanguine Bond over Demon's Horn (four other gain-to-loss outlets already); generic Thoracle/Breach package; cheaper-only Defile over Consuming Corruption; Roaming Throne over the chosen slots (four-mana colorless setup, dependent on commander); counterspell-to-removal conversions that cut necessary stack defense.
- EDHREC Sol'kanar Lifegain, Optimized, Top and High-Lift compared as discovery input, not mandatory card additions; strong cards were assessed against actual cuts and commander necessity.
- An eight-swap variant making the above Well/Witch substitution and a nine-swap variant additionally replacing Bog with Lake were both judged weaker due lost control/recursion and land/hate stability. No actual matched-start multiplayer games, Monte Carlo win rates or independent third-model outcomes are claimed.

## Source receipts and limits

- Canonical Oct15 list/whole-list audit and Pass C #52 research: engineering PRs #315, #364, #479; Pass C *NEEDS TESTING* flagged Necropotence/Archive, assessed here as M7 higher-tempo trade rather than pretending historical Pass C was final approval.
- Archive `data/card_index.csv` git blob `c84463e9fa4708165027404d4ca54af5dcf5774b`, generated from Scryfall full oracle_cards bulk 2026-10-15; seven new card name IDs and 95 identity/legalities bound in JSON source.
- Official Wizards Commander rules/ban list and MH3 release notes for double-faced identity; EDHREC commander pages: https://edhrec.com/commanders/solkanar-the-swamp-king and https://edhrec.com/commanders/solkanar-the-swamp-king/optimized.
- A fresh live full-deck Scryfall bulk request has **not** been executed; card metadata archive is 12 days old. This evidence supports a source-bound proposed list but must not be called an October 27 full live sweep or an independent gameplay performance proof.

## Approval boundary

Owner review requested for **exact 100-card raw SHA-256 `f7ff68f912839accc7177c288536c9abf9deefc8332d975236ef6f028b6f0e02`**, M7 Rev1, seven net swaps. Keep prior approved Sol'kanar and all other canonical files locked and byte-identical; do not merge engineering candidate or update canonical state until Cory approves the exact candidate. No M6.10/M7/M8 aggregate acceptance implied.
