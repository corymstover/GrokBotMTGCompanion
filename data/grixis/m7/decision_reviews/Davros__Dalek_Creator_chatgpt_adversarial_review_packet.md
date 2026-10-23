# Davros, Dalek Creator — ChatGPT adversarial review packet (M7, 2026-10-23)

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
- File `refinement/decklists/Davros_Dalek_Creator_Approved_2026-10-14.txt`, git blob `ee80a621`.
- Canonical commit record: the bytes were fetched and verified at 9b26aa28. The registry's source commit field says `1836b97`, the import commit, which carries the same bytes.
- Raw SHA-256 `aa6d2d343c6c1f167de8d16b23951940f7d23810c6e7705a6fd0d539a7459adc`. This equals `state/current_deck_overrides.json` `approved_list_sha256` and the registry `recorded_sha256`.
- Vendored byte-exact at `data/grixis/m7/baseline_sources/Davros__Dalek_Creator_approved_source_2026-10-14.txt`.

**Hashes.** The registry `recorded_sha256` equals the raw bytes, so **no provenance exception** is used.
- Logical hash `lh1:ef9b2bd79878dfd9159c9c04cb9c6aa79f02b5e42f723a9fa905dd219d29a39d`.
- The registry export `exports/grixis-archidekt/davros-dalek-creator.txt` (raw `c4d7cc54…`) is the same 100 in export format, with the same logical hash.

**Tracker note discrepancy (documented, not repaired).** The tracker CSV note cites `5c1d4a49`. That hash is the 2026-10-13 `Davros_Dalek_Creator_Proposed_Final_2026-10-13.txt`, which differs from the approved list by 11 swaps. The approved list's hash `aa6d2d34`, recorded in the overrides and the registry, is authoritative.

**Count convention.** 100 = 1 commander + 99 library; no companion.
- 34 lands: Island x2, Mountain x3, Swamp x3, plus 26 nonbasic.
- 7 mana rocks.

**Candidate.** `data/grixis/m7/candidate_lists/Davros__Dalek_Creator.txt`: commander first, then alphabetical; six substitutions.
- Raw `b5c3af5f46b9f4d647b43f1eda93ee19e2704536d6d0e486d7c26302c21156bc`.
- Logical `lh1:bc802d95f8b6dac3fc108e2c5c87250c250137495374944d8726cfa21994787f`.

**Live data.** Live Scryfall `/cards/collection` was queried on 2026-10-23 for 95 baseline rows and 84 candidate names. Two names were not found: Raiders' Wallet and Dalek Patrol.
- The live results are stored only in the candidate snapshot and the research files; the frozen cache was not written.
- Oracle text and oracle_id show zero differences against the frozen `oracle-cards-20261016090200` snapshot.

**Legality.** Every card is Commander-legal on live Scryfall and within UBR. No project exception is used. Kaya's Guile (white) was evaluated and excluded.

**Game Changers.** 5 in the baseline: Ancient Tomb, Cyclonic Rift, Demonic Tutor, Fierce Guardianship, Jeska's Will. 6 in the candidate (+Tergrid, God of Fright). **Power Bracket 4** (registry ceiling 4).

**Archidekt tags.** Villainous Choice, Group Slug, Discard.

## Commander model (attack this first)
**Davros, Dalek Creator** is a {1}{U}{B}{R} 3/4 menace legendary artifact creature, an **Alien Scientist** (not a Dalek). Its Oracle text: "At the beginning of your end step, create a 3/3 black Dalek artifact creature token with menace if an opponent lost 3 or more life this turn. Then each opponent who lost 3 or more life this turn faces a villainous choice — You draw a card, or that player discards a card."

Rules points:
- **603.4.** The condition has no intervening "if" at the start, so it is checked on resolution. Our other end-step triggers that cause life loss, ordered to resolve first, count toward it: Wound Reflection, Perforating Artist's raid and Missy's choice. Tinybones (draws if an opponent discarded this turn) and Sygg (draws if an opponent lost 3+) are payoffs, not enablers; Tinybones should resolve after Davros so that a discard choice turns it on.
- **603.3.** Triggers caused by the Dalek token entering (Purphoros, Ingenious Artillerist) go on the stack only after Davros's trigger has finished resolving. So the token can never create the qualifying loss for the trigger that made it. It can help a *later* Davros trigger the same end step (Roaming Throne naming Alien or Scientist, Strionic Resonator, Scientist Supreme, or Auton Soldier's non-legendary Davros copy).
- **701.55a / 701.55d.** Each qualifying opponent chooses, in APNAP order.
- **701.55b.** An empty-handed opponent may choose "discard a card" and lose nothing. This is a real weakness.
- **701.55c (The Valeyard).** Each choice is faced twice. Tokens are not doubled.
- **Bloodletter of Aclazotz** is a replacement effect (614, 616.1). Each life-loss event to an opponent on our turn is doubled. It is finite and not a loop.
- **608.2b.** Fiery Confluence with its artifact target illegal does nothing at all; the 2-2-2 mode has no target. Unlicensed Disintegration with an illegal target does nothing, including the 3 damage.

## Swaps (6 — five floor swaps plus one post-floor)
| Add | Cut | Why |
|---|---|---|
| Bloodletter of Aclazotz | Death in Heaven | Doubles every opponent life loss on our turn, so 2 becomes 4. Found only on EDHREC's optimized page (14/103). Death in Heaven is a two-turn Saga with no life loss. |
| Unlicensed Disintegration | Weeping Angel | Pass C's first pairing. Instant kill plus 3 to the controller with an artifact out. The Angel is a defensive flash body. |
| Tergrid, God of Fright | The Cyber-Controller | Steals the permanents that opponents sacrifice or discard to Davros, Court, Torment of Hailfire, Perforating Artist, Sycorax, The Dalek Emperor and Doomsday Confluence. Game Changer. The Cyber-Controller is an X-cost Cyberman lord shared with Deck #11. |
| Purphoros, God of the Forge | Blasphemous Act | OFF-RANKING. 2 to each opponent per creature entry (Dalek tokens, myriad copies); indestructible. Blasphemous Act kills our own Daleks. |
| Fiery Confluence | Vandalblast | OFF-RANKING. 2-2-2 deals 6 to each opponent (12 with Bloodletter). The artifact mode replaces Vandalblast. |
| Tectonic Giant | Swan Song | Post-floor. Each attack deals 3 to each opponent before blocks: a repeatable table qualifier. Swan Song gives an opponent a flying blocker. |

**Net:**
- Lands 34 → 34; rocks 7 → 7.
- Creatures 23 → 25; instants/sorceries 24 → 23.
- Artifacts in the 99: 24 → 22 (23 counting Davros).
- Curve by MV 0/1/2/3/4/5/6/7+: 1/5/24/11/13/2/6/3 → 1/3/24/10/16/3/6/2. Average nonland MV 3.185 → 3.231.
- Heuristic U/B/R land sources 19/18/18, unchanged. P(2–5 lands in 7) 0.758 → 0.758.

**Losses:**
- Blasphemous Act. Toxic Deluge, Their Name Is Death and Cyclonic Rift remain.
- Vandalblast's one-sided overload.
- Swan Song.
- Weeping Angel's flash body.
- Death in Heaven's delayed theft.
- The Cyber-Controller.

## Pass C requested tests (bounded; `tests/test_m6_davros_dalek_creator_m7_mechanics.py::PassCBoundedMeasuredTests`)
**Unlicensed Disintegration: 16-case grid.** The axes are legal/illegal target, artifact/no artifact, our turn/other turn, and prior loss/no prior loss.
- 8 kills.
- It newly qualifies an opponent in exactly 1 of the 16 cases, and only one opponent.

**Ingenious Artillerist vs Purphoros: five entry patterns.** The patterns are none, 1, a batch of 3, 3 separate, and a myriad batch of 2.
- Purphoros qualifies all opponents in 3 of the 5 patterns; Artillerist in 2.
- Artillerist deals 0 if it is removed in response.
- Davros's own token arrives too late for its own trigger.
- With two Davros triggers on the base board A3/B1/C1 (opponent life lost so far), the first token's Purphoros damage qualifies B and C for the second check, giving 2 tokens and 4 choices. Artillerist gives 2 tokens and 2 choices, because 1+1 is less than 3.

**Fiery Confluence (MV 4) vs Boltwave (MV 1, 3 to each opponent) and Maestros Charm (MV 3, 3 to each opponent).**
- Fiery 2-2-2 deals 6.
- Fiery 2-2-artifact deals 4, or 0 if the artifact target becomes illegal.

**Not done.** There was no matched-hand, mana or opponent sample, no removal-response rates, and no multiplayer simulation. No simulator here models villainous choices or multiplayer life totals.

## Combos (Commander Spellbook find-my-combos, both lists, JSON in research_challengers)
- Baseline: **0 included combos**. Candidate: **0 included combos**.
- Almost-included lines need cards that are not in the list.
- No infinite is claimed. Bloodletter + Wound Reflection is a finite doubling.

## Adversarial scenarios (please push here)
1. **Hellbent table (701.55b).** Opponents with no cards in hand choose "discard" and lose nothing.
   - What still works:
     - Tinybones' {4}{B}{B} activation: each opponent with no cards in hand loses 10.
     - Entropic Battlecruiser at 8+: each opponent who can't discard on its attack loses 3.
     - Tergrid's Lantern (Tergrid's back face): 3 life, or a nonland permanent sacrificed when they cannot discard.
   - What fails: Sycorax deals damage equal to hand size, which is 0 here.
   - The 2026-10-13 proposal's hellbent punishers (Bottomless Pit, The Rack, Oppression, Liliana's Caress) were removed by the owner's approved list. Megrim is rejected for the same reason.
2. **Artifact wipe.** Davros, the Daleks, Roaming Throne, Resonator and the rocks die.
   - What survives: Purphoros, Bloodletter, Tergrid, Tectonic Giant, Wound Reflection and Court of Ambition.
   - Unlicensed Disintegration then needs an artifact to deal its 3.
3. **Purphoros exiled or bounced.** Indestructible does not help here. The fallback enablers are Boltwave, Maestros Charm, Loyal Subordinate, Fiery and Tectonic Giant.
4. **Bloodletter removed.** It is a 2/4 flyer and the obvious target. Without it, 2-point sources (Purphoros, Fiery's 2 mode) need two hits to qualify an opponent.
5. **Dauthi Voidwalker vs Tergrid.** Voidwalker exiles the cards Tergrid would steal. This anti-synergy is disclosed; the Kroxa alternative was rejected.
6. **Counter-light.** With Swan Song cut, the remaining counterspells and protection are Counterspell, Mana Drain, Fierce Guardianship and Deflecting Swat. The five-swap list keeping Swan Song is RETAIN_ALTERNATIVE.
7. **Lifegain decks.** Lifegain does not stop Davros: the condition is life *lost* this turn, not net life.
8. **Pass C disposition.** Pass C was owner-equivalent and **not an actually independent third model**. Its final disposition was **NEEDS TESTING**. Its exact pairings are staged as complete 100s (Fiery over Weeping Angel, Disintegration over This Is How It Ends, Artillerist over Sycorax) and rejected.

## Tested pool (8 configurations; `data/grixis/m6/ij/tested_pools/Davros__Dalek_Creator_M7_tested_configurations_20261023.json`)
- BASELINE (raw 100) and CANONICAL_EXPORT (registry export, same logical hash).
- PREFERRED_SIX (selected).
- FIVE_KEEP_SWAN_SONG: RETAIN_ALTERNATIVE.
- SIX_CUT_ASHAD_KEEP_BLASPHEMOUS_ACT: REJECT.
- SIX_PASS_C_PAIRINGS: REJECT.
- SEVEN_PASS_C_ARTILLERIST_OVER_SYCORAX: REJECT.
- SEVEN_FLAME_RIFT_OVER_ASHAD: REJECT.

Other named rejections: Hellrider, Impact Tremors, Archfiend of Despair, Exsanguinate, Kroxa, Painful Quandary, Sheoldred, Megrim, Pain Magnification, Torment of Scarabs, Rhystic Study, Vampiric Tutor.

## Distinctness vs Deck #11 Cult of Skaro (significant overlap, disclosed)
**Overlap.** Both decks are Grixis Dalek decks.
- The Davros baseline shares **53** nonbasic names with the #11 candidate; this candidate shares **52**. That is 18 lands and 34 nonlands, and Davros himself is one of #11's 99.
- Shared nonlands:
  - Daleks and copies: Cult of Skaro, The Dalek Emperor, Dalek Drone, Dalek Squadron, Genesis of the Daleks, Doomsday Confluence, Exterminate!, Missy, Ashad, Cyberman Patrol, Auton Soldier, Roaming Throne, Strionic Resonator, Scientist Supreme.
  - Protection: Padeem, Greaves, Boots.
  - Interaction: Cyber Conversion, Delete, Their Name Is Death, Mana Drain, Fierce Guardianship, Deflecting Swat, Cyclonic Rift, Deadly Rollick.
  - Mana: Mox Opal, Sol Ring, Arcane Signet, Fellwar Stone, three Talismans, Enthusiastic Mechanaut.
- The Cyber-Controller was shared and is cut here. None of the six adds is in #11.

**Commander-first difference.** #11 multiplies Cult's random attack trigger (extra combats, clones, haste). Davros wants every opponent to have lost 3+ life on our turn, then makes them choose. Davros-only core: Boltwave, Maestros Charm, Loyal Subordinate, Court of Ambition, Torment of Hailfire, Wound Reflection, Perforating Artist, Sygg, Tinybones, Geth's Grimoire, Waste Not, Entropic Battlecruiser, Sycorax Commander, The Valeyard, Ensnared by the Mara, This Is How It Ends, Tezzeret and Labyrinth Raptor, plus all six adds.

## Infra disclosure
**No shared-infrastructure change in this PR.**
- These files are byte-identical to PR #659 head 488e1d05 (vendored from the #651–#659 stack; not modified here):
  - the gate;
  - the schema;
  - the gate test;
  - the Pass C corpus test;
  - `scripts/grixis_m6_bundle_check.py` (SHA-256 `2962a640…`).
- This deck's preserved Pass C receipt ("**not an actually independent third model**; technical independence absent") passes the checker's existing preserved-non-independence path.

**Process notes.**
- The focused CI workflow step names contain no `#` characters.
- **Merge order:** #651 → #652 → #653 → #654 → #655 → #656 → #657 → #658 → #659 → this PR.
- Pass C is FORMAL_PASS_C_OWNER_EQUIVALENT under the owner waiver and is **not** technically independent.
- CI run URLs are recorded in the PR body, not in hashed files.
