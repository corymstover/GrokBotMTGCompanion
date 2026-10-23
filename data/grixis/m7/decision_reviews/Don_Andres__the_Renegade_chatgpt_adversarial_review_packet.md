# Don Andres, the Renegade — ChatGPT adversarial review packet (M7, 2026-10-23)

**Status:** REVIEW CANDIDATE — NOT APPROVED, NOT CANONICAL. REVIEW_READY_NOT_OWNER_APPROVED. Only Cory can approve.

**Reviewer instruction:** attack this list. Show any of the following:
- a rules error;
- an illegal card;
- an unpayable line;
- an unsupported combo claim;
- a candidate that clearly beats an incumbent.

No win rates were measured, and EDHREC prevalence is discovery evidence only.

## Provenance
**Canonical source (read-only).**
- Repository `corymstover/grixis-commander-encyclopediaGPT` main `9b26aa28fc7e16f6652aaec292b4edf84e20db71`.
- File `refinement/decklists/Don_Andres_the_Renegade_Approved_2026-10-14.txt`, git blob `1d20d4887565d2765f914ea0a9c33a14d9df03f2`, frozen by canonical commit `255c328`.
- Canonical commit record: the bytes were fetched and verified at 9b26aa28. The registry's source commit field says `1836b97`, the import commit, which carries the same bytes.
- Raw SHA-256 `a6022fddd295d7c671690fbce5e25dc6fed47ca7fa77bf1d8a86ebadb2d927bb`. This equals `state/current_deck_overrides.json` `approved_list_sha256` and the registry `recorded_sha256`.
- Vendored byte-exact at `data/grixis/m7/baseline_sources/Don_Andres__the_Renegade_approved_source_2026-10-14.txt`.

**Hashes.** The registry `recorded_sha256` equals the raw bytes, so **no provenance exception** is used.
- Logical hash `lh1:012d9c8c9f3127dbfc1ed86dbd8db88ac5f00ee810f841c90a74e5d385faff48`.
- The registry export `exports/grixis-archidekt/don-andres-the-renegade.txt` (raw `3c5a31e6cf23e2b81d7d4e85d28426231de10d714aae769da886aeff384c7e03`) is the same 100 in export format ("1 " instead of "1x ", sorted), with the same logical hash.

**Discrepancies.** None in the hashes. The approved source file is not alphabetical; the candidate is written commander-first, then alphabetical.

**Count convention.** 100 = 1 commander + 99 library; no companion.
- 35 lands: Island ×2, Mountain and Swamp one each, plus 31 nonbasic. Island ×2 is the only repeated card (99 unique rows).
- 9 mana rocks in both lists (Pass C's 35-land figure includes them as a separate count).

**Candidate.** `data/grixis/m7/candidate_lists/Don_Andres__the_Renegade.txt`: commander first, then alphabetical; five substitutions.
- Raw `05e13311bac44898f2c299dca5a6b071133fb30a1c021d496e7de84e56049773`.
- Logical `lh1:d387b103e297de4c405cb044322c889c2e1f9a87cb987ff11aba09ec53b11da2`.

**Live data.** Live Scryfall `/cards/collection` was queried on 2026-10-23 for the 99 baseline rows and 155 evaluated names.
- The live results are stored only in the candidate snapshot and the research files; the frozen cache was not written.
- Oracle text and oracle_id show zero differences against the frozen `oracle-cards-20261016090200` snapshot for all compared names. Mirror Universe Intrusion is absent from the frozen cache and not Commander-legal; excluded.

**Legality.** Every card is Commander-legal on live Scryfall and within UBR. The registry's `official_commander_compliance` is `compliant`. **No project exception is used.**

**Game Changers.** 5 in the baseline and the candidate: Ancient Tomb, Cyclonic Rift, Fierce Guardianship, Opposition Agent, Vampiric Tutor. **Power Bracket 4.**

**Archidekt tags.** Theft, Pirates, Treasure.

## Commander model (attack this first)
**Don Andres, the Renegade** is a {1}{U}{B}{R} 4/3 Legendary Creature — Vampire Pirate. Its Oracle text: "Each creature you control but don't own gets +2/+2, has menace and deathtouch, and is a Pirate in addition to its other types. Whenever you cast a noncreature spell you don't own, create two tapped Treasure tokens."

Rules points:
- **108.3, 110.2, 111.2.** Ownership: the card's owner is the player who started the game with it; a permanent's owner is its card's owner; a token's owner is the player who created it. Tokens and copies we make are ours.
- **707.10.** A copy of a spell is not cast, so copy effects never trigger Don.
- **111.10a.** Treasure: "{T}, Sacrifice this artifact: Add one mana of any color." Don's Treasures enter **tapped**, so they cannot pay for the spell that made them or the next stolen spell that turn without an untap effect.
- **613.1b, 613.4c.** The Pirate type is a layer 4 effect; +2/+2 is layer 7c. Both apply to each stolen creature.
- **608.2h.** Information is determined once on resolution (e.g. Mob Rule's power check).
- **701.40a.** Thieving Amalgam's manifests are face-down cards owned by the opponent, so Don buffs them.
- **702.49a/c.** Fallen Shinobi's ninjutsu returns an unblocked attacker; Shinobi enters tapped and attacking.
- **303.4e.** Treachery's controller controls the enchanted creature; removing the Aura ends the theft.

## Swaps (5 — the floor; no post-floor swap)
| Add | Cut | Why |
|---|---|---|
| Gríma, Saruman's Footman | Professional Face-Breaker | Unblockable; each connection casts an opponent's instant or sorcery free, i.e. a Don trigger. Face-Breaker's impulse draw is our own cards. |
| Fallen Shinobi | Seize the Spotlight | Ninjutsu; each connection plays the opponent's top two free (2 × 30/85 = 12/17 Don triggers per hit in the bounded model; creatures become opponent-owned and get Don's buff). Seize the Spotlight lets the opponent choose. |
| Treachery | Blasphemous Act | Permanent theft (the stolen creature gets Don's static) that untaps five lands. Blasphemous Act kills our stolen army and Don. |
| Gloomlake Verge | Shipwreck Marsh | Untapped U always; UB with an Island or Swamp (9 qualifying names). Shipwreck Marsh's two-basic condition rarely holds with four basics. |
| Blazemire Verge | Smoldering Marsh | Untapped B always; BR with a Swamp or Mountain (9 qualifying names). Same reason. |

**Net:**
- Lands 35 → 35; rocks 9 → 9. Early conditional-or-tapped lands 5 → 3.
- Creatures 28 → 29; instants/sorceries 19 → 17.
- Curve by MV 0/1/2/3/4/5/6/7+: 0/4/21/15/12/6/2/4 → 0/4/21/13/13/8/2/3. Average nonland MV 3.312 → 3.297.
- P(2–5 lands in 7) 0.775 → 0.775.

**Losses:**
- Professional Face-Breaker's combat Treasure and impulse draw.
- Seize the Spotlight.
- Blasphemous Act (Toxic Deluge and Cyclonic Rift remain).
- Shipwreck Marsh and Smoldering Marsh.

## Pass C requested tests (bounded; `tests/test_m6_don_andres_the_renegade_m7_mechanics.py::PassCBoundedMeasuredTests`)
**Mob Rule vs Insurrection (Pass C item 1): 60-cell grid.** The axes are 2 spells × 5 fixed mixed-power tables × 6/7/8 mana × Don present or removed.
- Insurrection is uncastable at 6–7 mana; Mob Rule is castable everywhere.
- At 8 mana Insurrection takes at least as many creatures and as much power as Mob Rule on every table, with or without Don. Mob Rule keeps 115/144 of Insurrection's stolen power and ties on 2/5 tables.
- Don changes power, not the creatures taken, except on the one-big-threat table where Mob Rule's best mode flips.
- Red availability by 13 cards (lands-only): ≥2 red 0.8396 → 0.8169; ≥3 red 0.5901 → 0.5529; identical with the Verge condition met. Red land sources 22 → 21.

**Bribery vs Thieving Amalgam / Jhoira (Pass C item 2):** five opponent creature densities (0/4/8/15/25).
- Bribery: at most one permanent, none at density 0; pays off at once.
- Amalgam: three opponent-owned manifests per round from the first opponent upkeep, six after two rounds.
- Jhoira: one on entering, one per surviving attack.
- None of the three triggers Don.

**Not done.** There was no opponent model for blocks, responses or removal, no matched-opening playtest sample and no multiplayer simulation. No win rates are reported.

## Combos (Commander Spellbook find-my-combos, both lists, JSON in research_challengers)
- Baseline: **0 included combos**. Candidate: **0 included combos**.
- Almost-included lines: 23 → 19. They need cards that are not in the list. **No infinite is claimed.**

## Adversarial scenarios (please push here)
1. **Don removed.** Stolen creatures stay ours but lose +2/+2, menace and deathtouch; Gríma and Shinobi still cast opposing cards without Treasures.
2. **Tapped Treasures.** Do any lines in the list assume a Don Treasure pays for a spell the same turn? None should; please check.
3. **Red-light draws.** Insurrection needs RRR; P(three red lands among the top 13) 0.5529 (Verges at one colour).
4. **Go-wide opponents.** With Blasphemous Act cut, Toxic Deluge and Cyclonic Rift are the resets. The four-swap keeping Blasphemous Act is RETAIN_ALTERNATIVE.
5. **Treachery answered.** Aura removal ends the theft; the five-land untap is already spent.
6. **Owner-removed class.** The owner's 2026-10-14 approval removed the reanimation package (Buried Alive, Living Death, Victimize), Cunning Rhetoric, Share the Spoils, The Ruinous Powers, Revel in Riches, Gonti, Lord of Luxury, Zara and four slow/tapped lands, and rejected Bribery, Agent of Treachery, Captivating Crew and Memory Plunder. Those evaluated here were rejected; none is re-added. Treachery is single-target theft like Hostage Taker and Gilded Drake; please confirm the owner does not see it as a removed class.
7. **Pass C disposition.** Pass C was owner-equivalent; a genuinely independent model was **NO** (not technically independent). Its final disposition was **KEEP**. Its Stage A hypothesis (+Mob Rule −Insurrection) and both Bribery pairings are staged as complete 100s and rejected.

## Tested pool (9 configurations; `data/grixis/m6/ij/tested_pools/Don_Andres__the_Renegade_M7_tested_configurations_20261023.json`)
- BASELINE (raw 100) and CANONICAL_EXPORT (registry export, same logical hash).
- PREFERRED_FIVE (selected).
- FOUR_KEEP_BLASPHEMOUS_ACT_NO_TREACHERY: RETAIN_ALTERNATIVE.
- SIX_PASS_C_MOB_RULE_OVER_INSURRECTION: REJECT.
- SIX_PASS_C_BRIBERY_OVER_THIEVING_AMALGAM: REJECT.
- SIX_PASS_C_BRIBERY_OVER_JHOIRA: REJECT.
- FIVE_DAZZLING_SPHINX_INSTEAD_OF_GRIMA: REJECT.
- SIX_NIGHTVEIL_SPECTER_OVER_LOCKE: REJECT.

Other named rejections: Control Magic, Sower of Temptation, Robber of the Rich, Intellect Devourer, Mass Mutiny, Call for Aid, Stolen Goods, Desertion, Port Razer, Thieving Skydiver, Knowledge Exploitation, Mnemonic Betrayal, Fevered Suspicion, Dream Harvest, Heartless Conscription, Riverpyre Verge, Swiftfoot Boots, and the owner-removed Bribery, Zara, Memory Plunder, Agent of Treachery and Captivating Crew.

## Distinctness (disclosed)
Nonbasic names shared with the most similar Grixis decks (`exports/grixis-archidekt/`), baseline → candidate:
- Nathan Drake, Treasure Hunter 62 → 61.
- Admiral Brass, Unsinkable 55 → 53; Admiral Beckett Brass 54 → 52.
- Edward Kenway 49 → 49; The Madcap Jester 43 → 44.
- Cormela, Glamour Thief 31 → 31; Evelyn, the Covetous 27 → 28.

Gríma is also in the Nathan Drake list and Blazemire Verge in Evelyn. Overlap falls by 0–2 names with the Pirate decks; it is disclosed, not repaired.

**Commander-first difference.** Don rewards controlling creatures we don't own and casting noncreature spells we don't own. The adds cast opposing cards (Gríma, Shinobi) or steal permanently (Treachery), not generic Pirate tribal or our own impulse draw.

## Infra disclosure
**No shared-infrastructure change in this PR.**
- These files are byte-identical to PR #661 head 8bcc4c54 (vendored from the #651–#661 stack; not modified here):
  - the gate;
  - the schema;
  - the gate test;
  - the Pass C corpus test;
  - `scripts/grixis_m6_bundle_check.py` (SHA-256 `2962a640…`).
- This deck's preserved Pass C receipt ("genuinely independent model **NO**") passes the checker's existing preserved-non-independence path.

**Process notes.**
- The focused CI workflow step names contain no `#` characters.
- **Merge order:** #651 → #652 → #653 → #654 → #655 → #656 → #657 → #658 → #659 → #660 → #661 → this PR.
- Pass C is FORMAL_PASS_C_OWNER_EQUIVALENT under the owner waiver and is **not** technically independent.
- CI run URLs are recorded in the PR body, not in hashed files.
