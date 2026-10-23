# Lynde__Cheerful_Tormentor (Lynde, Cheerful Tormentor) — ChatGPT adversarial review packet (M7, 2026-10-23)

**Status:** RESEARCH ONLY and BLOCKED — NOT APPROVED, NOT CANONICAL, NOT OWNER-PRESENTABLE. Readiness `RESEARCH_ONLY_WITHDRAWN_NOT_OWNER_PRESENTABLE`.
- Blocker 1 (seal): the existing M6 Pass C Stage A seal does not match the committed Stage A file, so the shared J checker rejects any bundle for this deck. Exact cause below. The sealed evidence and the checker are not edited.
- Blocker 2 (floor): two genuine swaps were found, below the five-swap floor; nothing was padded.
- No owner keep or owner add is cut. Single-swap alternatives A and B are staged as complete 100s.
- Only Cory can approve.

**Reviewer instruction:** attack this conclusion. Show any of the following:
- a rules error;
- an illegal card;
- an unpayable line;
- an unsupported combo claim;
- a reason either swap is not a genuine improvement, or a genuine swap we missed;
- an owner-direction contradiction we missed.

No win rates were measured. EDHREC prevalence is discovery evidence only, and it is against both swaps (Lynde page, 7774 decks: Cruel Reality 5703, Curse of Death's Hold 5548, Extravagant Replication 2712, Court of Vantress 1705).

## Seal blocker (exact cause)
- File: `data/grixis/m6/owner_pass_c_substitute/Lynde__Cheerful_Tormentor/seal.json`, added by commit `c4c5fa5df5d55114c5f7e773d103d8490e60b67b` (2026-10-21 10:19:04 -05:00), merged via #436 (ledger #437).
- It records `stage_a.md` SHA-256 `59f2dc10eedec5797f3f5dcfdb0a206b380a037e9b17a29e740d6ca94829c12e` and git blob `b253ed9c4c7543b4c369dba957b2b4971c059133`.
- The committed `stage_a.md` (Stage A commit `b4c985688c4bee3db76d18bb0c3ada940ec79c98`, 2026-10-21 10:18:40 -05:00) is that same blob `b253ed9c`, but its SHA-256 is `02adfb85db19aa42d5dfe36b96906874ea1abd232b6f8bfc3861c1108035b72a` (13276 bytes, ending `.\n\n`). The file has not changed since.
- **Exact cause:** the sealed value `59f2dc10…` is the SHA-256 of the file without its final newline byte (bytes `[:-1]`). The seal was computed over the text with one trailing newline, while the committed file has two. The recorded blob matches the committed bytes, so the seal record is internally inconsistent. `tests/test_m6_lynde_cheerful_tormentor_m7_ij.py` asserts this.
- `stage_a.json` matches its seal (`d2b968bb…`, blob `1d5660ce`).
- `final_disposition.md` and `stage_b_reconciliation.md` repeat the sealed MD hash.
- Effect: `scripts/grixis_m6_bundle_check.py` (sha `2962a640…3bf3b`, unchanged) raises "Stage A source diverged from separately sealed byte commitment" in `validate_pass_c`. A mock that substitutes only the sealed hash for `stage_a.md` makes the bundle validate, so the seal is the only failure. The checker's `--check` scans only `data/grixis/m6/bundles/*.json`; the M7 bundle for this deck is at `data/grixis/m6/ij/revision_bundles/lynde-cheerful-tormentor-m7.json` and is **not** covered by `--check` (the same location PR #677 and #678 use). The corpus test already expects decks 30 and 31 to be rejected.
- Fix (owner decision, NOT done here): re-seal Stage A under a new, disclosed seal record, or record a documented hash-correction exception. Either way, the owner has to authorise touching sealed M6 evidence.

## Provenance
**Canonical source (read-only).**
- Repository `corymstover/grixis-commander-encyclopediaGPT` main `9b26aa28fc7e16f6652aaec292b4edf84e20db71`.
- File `refinement/decklists/Lynde_Cheerful_Tormentor_Approved_2026-10-14.txt`, git blob `5731e689`, introduced by canonical commit `7258398` (2026-10-14 22:46:40 -05:00).
- Canonical commit record: 9b26aa28fc7e16f6652aaec292b4edf84e20db71 (blob 5731e689, introduced by 7258398 2026-10-14; registry source_commit 1836b97 same bytes).
- Raw SHA-256 `05d1c4eea023d25e4308f78b109e80b78e0a3f4d655c3df36743ba3afbf04166`. This equals the overrides `approved_list_sha256` and the registry recorded hash.
- Vendored byte-exact at `data/grixis/m7/baseline_sources/Lynde__Cheerful_Tormentor_approved_source_2026-10-14.txt`.

**Hashes.** No provenance exception is used. Logical hash `lh1:7359723b249d034d4496f17f16bd6f061e7a14c9eb4ac6bb70ae7f058711a5d7`. The registry Archidekt export `exports/grixis-archidekt/lynde-cheerful-tormentor.txt` (raw `f1d4ed17…`) has the same logical hash.

**Identity and discrepancies (recorded, not changed).**
- Tracker Deck 31 (index 30); tracker, canonical and engineering deck ID are all `Lynde__Cheerful_Tormentor`, matching the overrides and registry (APPROVED / LOCKED 2026-10-14).
- Tracker row 30 detailed-gate sub-fields are still PENDING, and the decisions document header hashes (e72576fb…, aa021e79…) are the pre-change source values, not the approved list. The overrides are the lock authority. Nothing is changed.

## Commander model (attack this first)
Lynde, Cheerful Tormentor ({1}{U}{B}{R}, Legendary Creature — Human Warlock 2/4; `mic`, released 2021-09-24; Commander-legal; not a Game Changer):
- "Deathtouch"
- "Whenever a Curse is put into your graveyard from the battlefield, return it to the battlefield attached to you at the beginning of the next end step."
- "At the beginning of your upkeep, you may attach a Curse attached to you to one of your opponents. If you do, draw two cards."

How the deck uses this:
- Send your own Curses to the graveyard (Despotic Scepter, Claws of Gix, Perilous Research, Braids, Arisen Nightmare, Demon of Fate's Design); Lynde returns them attached to you; each upkeep Lynde moves one for two cards. Extra upkeeps (Paradox Haze, The Ninth Doctor, Obeka) and Curse copies (Copy Enchantment, Mirrormade, Estrid's Invocation, Clever Impersonator) scale it.
- A returned Curse sits on you from the end step to your upkeep. A Curse that triggers in your upkeep still affects you after Lynde moves it (CR 503.1a; "that player" is fixed). That is the weakness both cuts share.
- Token Curses cease to exist in the graveyard (CR 704.5d), so Lynde never returns Court or Replication tokens.

## Swaps (2 — below the five-swap floor; RESEARCH_ONLY)
**1. +Court of Vantress −Cruel Reality (MODERATE).**
- Neither card is an owner keep or add.
- Court as monarch makes a token copy of a Curse each upkeep; the token Aura enters attached to the player you choose (CR 303.4f). Put it on yourself and Lynde moves one for two cards, or put it straight on an opponent. It also copies Paradox Haze and other enchantments or artifacts, and the monarch draws.
- Cruel Reality returned to you: its sacrifice trigger hits you at your upkeep even after Lynde moves it. Grid B1: Lynde is the forced sacrifice in 42/96 Cruel Reality cells, 0 without it.
- Costs: Cruel Reality is the strongest table lock and the more popular card; Court needs you to keep the monarchy (not-monarch Court only becomes a copy).

**2. +Extravagant Replication −Curse of Death's Hold (MODERATE).**
- Neither card is an owner keep or add.
- Unconditional upkeep copy of another nonland permanent you control.
- Curse of Death's Hold returned to you kills your X/1s (Nightscape Familiar, CR 704.5f) and shrinks Lynde to 1/3 until your upkeep. Grid B1: 32/96 cells.
- Costs: six mana with no immediate effect; loses the anti-token lock; the cut is the more popular card.

**Single-swap alternatives (complete 100s):** alt A, Court only (keeps Death's Hold); alt B, Replication only (keeps Cruel Reality).

**Staged, not counted:** Staff of Compleation over Nightscape Familiar. "{T}, Pay 1 life: Destroy target permanent you own" sends a Curse you own to the graveyard each turn; outlet coverage by turn 7 rises 0.2716 → 0.3379, but turn-4 Lynde falls 0.629 → 0.6179.

**Pass C requested comparisons:**
- Curse of Chaos over Curse of Echoes: rejected. The owner removed Curse of Chaos on 2026-10-14, and Echoes is an owner add.
- Author hypotheses Strionic Resonator (over Nightscape Familiar) and Beseech the Mirror (over Curse of the Restless Dead): rejected, both owner-rejected on 2026-10-14. Compare-only complete 100s are staged.

**Rejected (dominated):** Disturbing Mirth over Trespasser's Curse; Teferi's Ageless Insight over Curse of Unbinding; Thoughtrender Lamia over Bitterheart Witch; Curse of the Bloody Tome over Maddening Hex (mill Curse class, owner removed Fraying Sanity); Grievous Wound (an Aura, not a Curse); Witchbane Orb, Price of Knowledge, Mogis, God of Slaughter, Painful Quandary, Swiftfoot Boots, Reliquary Tower, Cloud Key, Silent Arbiter.

**Invalid:** The Unluckiest Planeswalker and Jabs, Mistress of Mockery (both not_legal on live Scryfall; owner also declined them).

## Pass C requested tests (bounded; `tests/test_m6_lynde_cheerful_tormentor_m7_mechanics.py`)
**Seeded goldfish** (seed 31, N=20000 per configuration, 12 configurations). By turn 7:
- P(Lynde cast) 0.8681 for baseline and candidate (turn 4 0.629).
- P(Lynde plus Court or Replication) 0 → 0.1381; P(Lynde plus Cruel Reality or Death's Hold) 0.1051 → 0.
- Staff and Strionic variants: turn-7 cast 0.8601.

**Exhaustive rules grids:** B1 self-Curse upkeep stacks (246 cells), B2 rules cases (12: own-Curse outlets in your main phase, Braids end-step timing, an opponent destroying a Curse on their turn, exile before the end step, Accursed Witch // Infectious Curse, Copy Enchantment / Mirrormade copies, Court or Replication token Curses and their graveyard behaviour, Court while not the monarch, Replication copying Paradox Haze, copying a legendary permanent, Cruel Reality attached to you at your upkeep), B3 extra-upkeep and copy-engine supply (180 cells: draws 82 → 204, tokens 0 → 102), B4 cut versus add (72 cells).

## Combos (Commander Spellbook find-my-combos, every list, JSON in research_challengers)
- Included combos: 0 in the baseline, the candidate and every alternative.
- Almost-included: 17 → 22 (Strionic variant 24, Teferi variant 23).
- Game Changers 8 → 8. Bracket 4 (Optimized).

## Adversarial scenarios (please push here)
1. Is Cruel Reality's lock worth the Lynde self-sacrifice risk in your pods? Alt B keeps it.
2. How often can Lynde's controller keep the monarchy in a four-player pod at Bracket 4?
3. Is a six-mana do-nothing-this-turn enchantment (Replication) too slow for Bracket 4?
4. Would Staff of Compleation be worth the Nightscape Familiar cost reduction?
5. Should the owner reconsider Strionic Resonator now that two upkeep copy engines raise the number of Curses on you?

## Tested pool (13 configurations; `data/grixis/m6/ij/tested_pools/Lynde__Cheerful_Tormentor_M7_tested_configurations_20261023.json`)
1. BASELINE
2. CANONICAL_EXPORT
3. RESEARCH_TWO_SWAP
4. ALT_A_COURT_ONLY
5. ALT_B_REPLICATION_ONLY
6. STAGED_STAFF_OF_COMPLEATION_OVER_NIGHTSCAPE
7. PASS_C_CURSE_OF_CHAOS_OVER_ECHOES
8. PASS_C_STRIONIC_RESONATOR_OVER_NIGHTSCAPE
9. PASS_C_BESEECH_THE_MIRROR_OVER_RESTLESS_DEAD
10. REJECT_DISTURBING_MIRTH_OVER_TRESPASSERS
11. REJECT_TEFERIS_AGELESS_INSIGHT_OVER_UNBINDING
12. REJECT_THOUGHTRENDER_LAMIA_OVER_BITTERHEART
13. REJECT_CURSE_OF_THE_BLOODY_TOME_OVER_MADDENING_HEX

## Distinctness (disclosed)
Nonbasic names shared (registry Archidekt exports, the same for baseline and candidate; 90 nonbasic names):
- Garza Zol, Plague Queen 42
- Solkanar the Swamp King 41
- Nicol Bolas 40
- Solkanar the Tainted 39
- Mai and Zuko 39

The overlap is the Grixis mana base and staples. Court of Vantress and Extravagant Replication each appear in 1 other export; Cruel Reality and Curse of Death's Hold in none.

## Infra disclosure
- No new shared-infrastructure edits. The gate, schema, checker and shared tests on this branch are byte-identical to PR #678 head d2132bfb (itself identical to #677 head e117a5ca, carried from the #651 chain). There are no registry, tracker or overrides edits, and the sealed M6 evidence is untouched.
- New files are deck-scoped artifacts, three deck tests and the workflow `.github/workflows/m7-lynde-cheerful-tormentor.yml`.
- Merge order: #651 → … → #677 → #678 → this PR (#679).
