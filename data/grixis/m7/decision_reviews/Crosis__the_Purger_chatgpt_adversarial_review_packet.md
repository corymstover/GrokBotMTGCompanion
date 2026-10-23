# Crosis, the Purger — ChatGPT adversarial review packet (M7, 2026-10-23)

**Status:** REVIEW CANDIDATE — NOT APPROVED, NOT CANONICAL. REVIEW_READY_NOT_OWNER_APPROVED. Only Cory can approve.

**Reviewer instruction:** attack this list. Show any rules error, illegal card, unpayable line, unsupported combo claim, or a
candidate that clearly beats an incumbent. No win rates were measured, and EDHREC prevalence is discovery evidence only.

## Provenance
- **Canonical source (read-only):** `corymstover/grixis-commander-encyclopediaGPT`,
  `refinement/decklists/Crosis_the_Purger_Approval_Candidate_2026-10-14.txt` (commit 1836b97; the file name says "candidate", but it is the approved list).
  - Raw SHA-256: `a59150c323aa1e21cbda65291a3b172d08ecc3b83266b708768f4e14f0b07ec1`.
  - Vendored byte-exact at `data/grixis/m7/baseline_sources/Crosis__the_Purger_approved_source_2026-10-14.txt`.
- **Hashes:** the registry's `recorded_sha256` equals the raw bytes (`recorded_matches_raw: true`), so **no provenance exception** is used.
  - Logical `lh1:0cbe60a0…1f09` = registry `baseline_hash` = `current_canonical_hash` = canonical project list hash.
  - The registry export `exports/grixis-archidekt/crosis-the-purger.txt` is the same 100 with a `1 ` quantity prefix
    (different raw bytes, same logical hash).
- **Tracker note discrepancy (documented, not repaired):** the tracker CSV note says "Only change: Brotherhood Regalia -> Blizzard Specter".
  The bound approved list actually contains both cards. The bound bytes are authoritative.
- **Count convention:** 100 = 1 commander + 99 library; no companion. 36 lands (Island x4, Mountain x3, Swamp x4 + 25 nonbasic), 13 mana rocks.
- **Candidate:** `data/grixis/m7/candidate_lists/Crosis__the_Purger.txt` (commander first, then alphabetical; five substitutions).
  - Raw: `244f19b9465e499c390bcac10eb96ad04d73f4b760a09cfef1d526f47be98347`.
  - Logical: `lh1:f856372319521a23d334f454dc68f1efca141f65ca7c1273c7b84b0eec2b1668`.
- **Live data:** live Scryfall (2026-10-23, /cards/collection) is only in the candidate snapshot and research files. The frozen cache was not written.
  - Oracle text and oracle_id show zero differences against the frozen `oracle-cards-20261016090200` for all 198 names.
- **Legality:** every card is Commander-legal on live Scryfall and within UBR. No project exception is used.
  - Hullbreacher and Hymn of the Wilds (banned) and Valgavoth's Onslaught (green) were evaluated and excluded.
- **Game Changers (14, unchanged):** Ancient Tomb, Chrome Mox, Cyclonic Rift, Demonic Tutor, Fierce Guardianship, Force of Will,
  Gamble, Mana Vault, Mox Diamond, Mystical Tutor, Notion Thief, Orcish Bowmasters, Tergrid, Vampiric Tutor → **Power Bracket 4**
  (registry ceiling 4).
- **Archidekt tags:** Discard, Dragons, Extra Combats.

## Commander model (attack this first)
- **Crosis, the Purger** ({3}{U}{B}{R}, 6/6 flying Dragon): "Whenever Crosis deals combat damage to a player, you may pay {2}{B}. If you do,
  choose a color, then that player reveals their hand and discards all cards of that color."
- **Painter's Servant** makes every card in hand the chosen color, so a paid purge empties the hand.
- **Per-card punishers (CR 603.2c):** Megrim (2 damage), Liliana's Caress (2 life) and Raiders' Wake (2 life) each trigger once per card
  discarded, including each card of one multi-card discard.
  - A 5-card Painter purge with all three costs that player 30. A 7-card wheel with all three costs each opponent 42.
  - Baseline with Caress only: 10 and 14.
  - All of these are finite, need the enchantments to survive, and do nothing against empty hands.
- **Sword of Feast and Famine + Aggravated Assault (Spellbook 900-3750):** when Crosis with the Sword connects, order the triggers (CR 603.3b)
  so the Sword resolves first and untaps all lands. Then the Crosis trigger can be paid ({2}{B}). In the next main phase, {3}{R}{R}
  gives another combat (CR 500.8).
  - A purge plus a loop needs 8 land mana per combat; with 5–7 it is Assault only.
  - The loop ends the first time Crosis fails to connect (blockers with reach or flying, fog, prevention, removal).
  - Disclosed as conditional, not as a deterministic win.
- **Deadly Rollick** is free while we control a commander (CR 903.3d: a commander on the battlefield).

## Swaps (5 — the floor, not padded)
| Add | Cut | Why |
|---|---|---|
| Megrim | Jet Medallion | 2 damage per opponent discard, the signature Crosis payoff and Pass C's top hypothesis. Medallion only discounts black spells and is the weakest of 13 rocks. |
| Rankle, Master of Pranks | Blizzard Specter | Hasty flyer with three combat-damage modes we choose. Blizzard Specter has no haste and one mode. |
| Aggravated Assault | Dream Salvage | Extra combats mean more Crosis triggers, and with the incumbent Sword it is Spellbook 900-3750. Salvage only draws after a purge. |
| Raiders' Wake | Oppression | Asymmetric 2 life per opponent discard, plus a raid discard when we attack. Oppression taxes our own 25 instants/sorceries and empties hands before the purge. |
| Deadly Rollick | Izzet Signet | Free exile while Crosis is out, so {2}{B} stays up for the trigger. Izzet is the least-needed third Signet in a 36-land list. |

**Net:** lands 36 → 36 (always tapped: Xander's Lounge only); rocks 13 → 11; library creatures and instants/sorceries unchanged (25 instants/sorceries);
enchantments +2. Curve by MV 0/1/2/3/4/5: 3/10/27/14/7/2 → 3/9/25/15/9/2. Average nonland MV 2.286 → 2.381.
Heuristic B/R/U sources 22/18/20 unchanged. P(2–5 lands in 7) 0.790 → 0.790.
**Losses:** black cost reduction, a Signet, Blizzard Specter's bounce mode, Dream Salvage's post-purge draw, and Oppression's symmetric stax.

## Combos (Commander Spellbook find-my-combos, both lists, JSON in research_challengers)
- Baseline: 1 included combo, **2286-3221** (Notion Thief + Teferi's Puzzle Box draw-step lock), kept.
- The candidate has 2: **+900-3750 (Sword of Feast and Famine + Aggravated Assault, "infinite combat phases")**.
  Infinite claims are limited to that Spellbook line and its connection condition above.

## Weakest points (please push here)
1. **Two mana rocks lost:** two fewer 2-mana rocks slow a turn-4 Crosis. The mana memo covers this, and Pass C itself treated Medallion and the
   Specters as the flexible slots.
2. **Punisher redundancy:** Megrim and Wake are the second and third copies of the Caress effect. Against empty hands all three are inert.
   Pass C's Phase B request (hand depletion 0/3/5/7) is answered only with finite arithmetic, not a measured delta.
3. **Aggravated Assault without Sword** costs five mana per extra combat. It is weak until the Sword or a big board is out.
4. **Rankle's modes are symmetric.** We choose which modes apply, but each one also hits us.
5. **Pass C** (owner-equivalent, NOT technically independent) final disposition was **NEEDS TESTING / KEEP-LOCKED pending evidence**,
   leading with Megrim over Sedraxis Specter. This candidate takes Megrim but cuts Jet Medallion. Pass C's exact pairing is staged and rejected,
   so it needs owner review.

## Tested pool (7 configurations; `data/grixis/m6/ij/tested_pools/Crosis__the_Purger_M7_tested_configurations_20261023.json`)
- BASELINE (raw 100) and CANONICAL_EXPORT (registry export, same logical hash).
- PREFERRED_FIVE (selected).
- FOUR_KEEP_OPPRESSION (REJECT: symmetric tax fights our spells and the purge).
- FIVE_PASS_C_MEGRIM_OVER_SEDRAXIS (REJECT: Sedraxis is a cheaper recursive flyer; Medallion is the weaker slot).
- SIX_BLOODCHIEF_OVER_DARK_DEAL (RETAIN_ALTERNATIVE, staged, not selected: needs three end steps).
- SEVEN_QUANDARY_OVER_BOTTOMLESS_PIT (REJECT: five mana, opponents choose).

Other named rejections: Blazing Specter, Dauthi Voidwalker (anti-synergy with Tergrid and Tinybones, Bauble Burglar), Snuff Out (cannot hit
black creatures), Whispersilk Cloak, Counterspell, Sulfurous Springs, Hypnotic Specter.

## Distinctness
This deck differs from the other UBR decks. Nekusar punishes draws and wheels from the command zone, Kess recasts instants and sorceries from the graveyard, and the Marchesas are creature-recursion decks.
Crosis is a six-mana Dragon whose plan is connecting in the air and converting the paid color purge into per-card damage.
Extra combats (Aggravated Assault, with the Sword) multiply the commander's own trigger.

## Infra disclosure
- No shared-infrastructure change in this PR. The gate, schema, gate test, Pass C corpus test and `scripts/grixis_m6_bundle_check.py`
  (SHA-256 `2962a640…`) are byte-identical to PR #657 head 257dac33 (vendored from the #651–#657 stack; not modified here). This deck's preserved Pass C receipt
  ("technically independent **false**") passes the checker's existing strict explicit-FALSE disclosure path. It is not added to the per-deck table.
- The focused CI workflow step names contain no `#` characters (the #656/#657 step-name truncation is fixed for this deck).
- **Merge order:** #651 → #652 → #653 → #654 → #655 → #656 → #657 → this PR.
- Pass C is FORMAL_PASS_C_OWNER_EQUIVALENT under the owner waiver and is **not** technically independent.
- CI run URLs are recorded in the PR body, not in hashed files.
