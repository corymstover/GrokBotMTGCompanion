# Lord_of_Tresserhorn (Lord of Tresserhorn) — ChatGPT adversarial review packet (M7, 2026-10-23)

**Status:** REVIEW CANDIDATE. NOT APPROVED, NOT CANONICAL.
- Readiness: `READY_FOR_EXACT_OWNER_APPROVAL_NOT_YET_APPROVED`.
- Five genuine swaps. All five cuts are flagged: one is an owner-cycle add and four were owner audit KEEPs.
- Only Cory can approve.

**Reviewer instruction:** attack this conclusion. We want any of the following:
- a rules error;
- an illegal card;
- an unpayable line;
- an unsupported combo claim;
- a reason a swap is not a genuine improvement;
- a better cut for any add;
- an owner-direction contradiction we missed.

No win rates were measured. EDHREC prevalence is discovery evidence only.

## Provenance
**Canonical source (read-only).**
- Repository `corymstover/grixis-commander-encyclopediaGPT`, main `9b26aa28fc7e16f6652aaec292b4edf84e20db71`.
- File `refinement/decklists/Lord_of_Tresserhorn_Approved_2026-10-14.txt`: blob `d9ff96da`, introduced by `af3c889` (2026-10-14). Registry source_commit 1836b97 has the same bytes.
- Raw SHA-256 `95863276f38beff6b0cf7609041006a6f1de94d5e62c73d76551d6793ffa5b8e`. It equals the overrides `approved_list_sha256` and the registry recorded hash.
- Vendored byte-exact at `data/grixis/m7/baseline_sources/Lord_of_Tresserhorn_approved_source_2026-10-14.txt`.

**Hashes.** No provenance exception is used.
- Baseline logical hash: `lh1:eae4578c6338f3c2caf25f7359154e851b6f51f179c2ddb3ac2883f95489aafa`.
- Candidate: raw `fd09cb267660206b834257e5c455259985b0e53316743835f679760b11200f85`, logical `lh1:c01c0d9c2ea75d54c110a6fa0345ce27094eea53a7a7a226b77f711e22984961`.

**Discrepancy (recorded, not changed).** Tracker row 28 still shows the stale "CURRENT FINAL BASELINE" text with a blank final hash. The overrides say APPROVED / LOCKED 2026-10-14.

## Commander model (attack this first)
Lord of Tresserhorn ({1}{U}{B}{R}, Legendary Creature — Zombie 10/4; `me1`; Commander-legal; not a Game Changer).

Oracle text, the same in the frozen cache and on live Scryfall:
- "When Lord of Tresserhorn enters, you lose 2 life, you sacrifice two creatures, and target opponent draws two cards."
- "{B}: Regenerate Lord of Tresserhorn."

**There is no opponent-regeneration clause.** An earlier brief paraphrase said otherwise. It is ignored.

How the text plays:
- The trigger targets an opponent. It can be suppressed (Torpor Orb, Karn; Dress Down if already on the battlefield) or countered on the stack (Stifle, Tale's End, Consign to Memory).
- With fewer than two other creatures, Lord sacrifices himself.
- Regeneration replaces only destruction (CR 701.19a). It does not save Lord from sacrifice (CR 701.21a) or from "can't be regenerated" effects.
- Win lines:
  - Uncaged Fury (11 double strike = 22 commander damage);
  - infect (Phyresis, Tainted Strike, Kediss spreading noncombat damage);
  - Pain for All + Blasphemous Act while {B} regenerates Lord;
  - aristocrat loops.

## Swaps (5)
1. **+Fierce Guardianship −Stubborn Denial (MODERATE).** Free once Lord is on the battlefield (CR 903.3d). B4: 17/40 vs 9/40, with Denial answering no cell that FG misses. While Lord is on the stack, FG costs {2}{U} and Denial is soft. FG is a Game Changer (2 → 3). Flag: Denial is an owner add. FG was author-rejected but reopened by Pass C.
2. **+Consign to Memory −Feed the Swarm (MODERATE).** A {U} counter for Lord's own trigger and for opponents' triggers and colourless spells. B6: Consign only 5/8 vs Feed only 2/8. Loss: enchantment removal drops to Chaos Warp, plus Otawara bounce. Flag: Feed was an audit KEEP.
3. **+Black Market Connections −Cover of Darkness (MODERATE).** The changeling token is a Zombie, so it is fodder, Gravecrawler's enabler and a body for Diregraf Captain. BMC also makes cards and Treasure. Largest single gain: 0.6121 → 0.6381. Flag: Cover was an audit KEEP.
4. **+Ornithopter of Paradise −Fellwar Stone (MODERATE).** A mana source that is also sacrifice fodder; summoning sick. Turn-4 deployment 0.2717 → 0.2879 on its own. Flag: Fellwar was an audit KEEP.
5. **+Skullclamp −Sheoldred's Edict (MODERATE).** Clamped fodder sacrificed to Lord's trigger draws two. Loss: the instant edict; spot removal goes 5 → 3. Flag: the Edict was an audit KEEP.

**Staged alternatives** (complete 100s with exact deltas):
- alt A: four swaps, keeping the Edict (0.6563);
- alt B: Skullclamp −Muddle the Mixture, keeping the Edict (0.6672, the highest number, within noise);
- alt C: Skullclamp −Nightscape Familiar (0.6438);
- Pass C Soul's Fire −Edict;
- Pass C FG −Nightscape (0.5856);
- Pass C Distortion Strike −Rogue's Passage (0.6490).

**Rejected:**
- Temur Battle Rage: owner cut, not reopened. The prior GrokBot draft is withdrawn.
- Aqueous Form over Muddle (0.6637, noise).
- The original tentative plan (0.5674).
- Embercleave, Psychotic Fury and Glistening Oil: author-rejected.
- Swan Song.
- Grafted Exoskeleton.
- Orcish Bowmasters: LOW confidence, unmeasured; it would be a fourth Game Changer and is switched off by the deck's suppression.

## Pass C requested tests (bounded; `tests/test_m6_lord_of_tresserhorn_m7_mechanics.py`)
**Seeded goldfish** (seed 29, N=20000, on the play): P(Lord on battlefield), turn 4 / turn 6.
- Baseline: 0.2717 / 0.6121.
- Candidate: 0.3068 / 0.6613.
- +Soul's Fire −Edict: 0.2710 / 0.6107.
- +FG −Nightscape: 0.2559 / 0.5856.

**Grids:**
- B1 evasion: Cover connects 12/24 cells, Aqueous 15/24.
- B2 conversion (972 cells): kills — Pain 108, TBR 174, Soul's Fire 216.
- B3 interaction: Edict answers 10/14 cells, Soul's Fire 4/14.
- B4 protection: FG answers 17/40 cells, Denial 9/40.
- B5 Dress Down layer-6 truth table: 24 cells.
- B6 Consign vs Feed: 5 cells only Consign answers, 2 only Feed.

## Combos (Commander Spellbook, every list; JSON in research_challengers)
- 19 included combos in the baseline, the candidate and every alternative. None are new and none are lost.
- Almost-included: 283 → 289.
- Gravecrawler + Phyrexian Altar needs another Zombie.
- Game Changers 2 → 3. **Bracket 4 (Optimized)**, unchanged.

## Adversarial scenarios (please push here)
1. Is cutting four owner audit KEEPs and one owner add too aggressive for a deck the owner rebuilt on 2026-10-14? Alt A (four swaps, keeping the Edict) is the conservative choice.
2. Is spot removal at 3 (Terminate, Deadly Rollick, Chaos Warp) and enchantment removal at 1 too thin for Bracket 4 pods?
3. Fierce Guardianship homogenizes: it is in 54/61 other decks. Is a free counter for Lord worth that?
4. Should Skullclamp take Muddle's slot (alt B) instead of the Edict's?
5. Should Orcish Bowmasters be measured? It punishes Lord's forced opponent draws, but the deck's suppression switches off its own trigger.

## Tested pool (12 configurations; `data/grixis/m6/ij/tested_pools/Lord_of_Tresserhorn_M7_tested_configurations_20261023.json`)
1. BASELINE
2. CANONICAL_EXPORT
3. REVIEW_CANDIDATE_FIVE_SWAP
4. ALT_A_FOUR_SWAPS_KEEP_SHEOLDREDS_EDICT
5. ALT_B_SKULLCLAMP_OVER_MUDDLE_KEEP_EDICT
6. ALT_C_SKULLCLAMP_OVER_NIGHTSCAPE_FAMILIAR
7. PASS_C_SOULS_FIRE_OVER_SHEOLDREDS_EDICT
8. PASS_C_FIERCE_GUARDIANSHIP_OVER_NIGHTSCAPE_FAMILIAR
9. PASS_C_DISTORTION_STRIKE_OVER_ROGUES_PASSAGE
10. REJECT_AQUEOUS_FORM_OVER_MUDDLE
11. REJECT_PRIOR_DRAFT_TEMUR_BATTLE_RAGE_OVER_PAIN_FOR_ALL
12. REJECT_ORIGINAL_TENTATIVE_PLAN

## Distinctness (disclosed)
Nonbasic names shared with other project exports, baseline → candidate:
- Tresserhorn's Lord, Returned: 52 → 51
- Garza Zol: 50 → 48
- Thraximundar: 47 → 48
- Nicol Bolas: 47 → 46
- Marchesa: 46 → 46

## Infra disclosure
- No new shared-infrastructure edits. The gate, schema, checker (SHA-256 2962a640…) and shared tests are byte-identical to PR #676 head 842f78d9, carried from the #651 chain.
- No registry edits.
- Merge order: #651 → … → #676 → this PR (#677).
