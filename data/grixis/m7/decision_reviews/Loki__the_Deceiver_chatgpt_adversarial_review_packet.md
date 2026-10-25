# Loki__the_Deceiver (Loki, the Deceiver) — ChatGPT adversarial review packet (M7, 2026-10-23)

**Status:** RESEARCH ONLY — NOT APPROVED, NOT CANONICAL, NOT OWNER-PRESENTABLE. Readiness `RESEARCH_ONLY_WITHDRAWN_NOT_OWNER_PRESENTABLE`.
- Blocker: two genuine swaps were found (+Ultimo, Civilization's End −Crimson Cowl, Master of Evil; +Elektra, Daughter of the Hand −Killmonger, Ruthless Usurper), and the five-swap floor was not met without padding.
- Only Cory can approve.

**Reviewer instruction:** attack this conclusion. Show any of the following:
- a rules error;
- an illegal card;
- an unpayable line;
- an unsupported combo claim;
- a reason either swap is not a genuine improvement, or a genuine swap we missed;
- an owner-direction contradiction we missed.

No win rates were measured. EDHREC prevalence is discovery evidence only, and it is against both adds.

## Provenance
**Canonical source (read-only).**
- Repository `corymstover/grixis-commander-encyclopediaGPT` main `9b26aa28fc7e16f6652aaec292b4edf84e20db71`.
- File `refinement/decklists/Loki_the_Deceiver_Approved_2026-10-14.txt`, git blob `456d62d45e6e5ffb283a97b5603997a4d1d74c3e`, introduced by canonical commit `d97bc2b` (2026-10-14).
- Canonical commit record: 9b26aa28fc7e16f6652aaec292b4edf84e20db71 (blob 456d62d4, introduced by d97bc2b 2026-10-14; registry source_commit 1836b97 same bytes).
- Raw SHA-256 `5079291c08c5af212b3d90d63ac5b01849d45c7700b1d64100ef57fb13458062`. This equals the overrides `approved_list_sha256`, the registry recorded hash and the tracker `final_list_hash`.
- Vendored byte-exact at `data/grixis/m7/baseline_sources/Loki__the_Deceiver_approved_source_2026-10-14.txt`.

**Hashes.** No provenance exception is used. Logical hash `lh1:1af6ee049bf73721081d3bed599d91b174e2487b42630b8b1c51827301e49c68`. The registry Archidekt export `exports/grixis-archidekt/loki-the-deceiver.txt` has the same logical hash.

**Identity and discrepancies (recorded, not changed).**
- Tracker index 27 (Deck 28): deck ID `Loki__the_Deceiver`, commander Loki, the Deceiver, APPROVED / LOCKED 2026-10-14, final_list_hash equal to the raw SHA.
- The overrides agree. There is no material mismatch; the tracker notes keep an older "current NOT STARTED state" sentence.
- The GrokBot advisory labelled the deck B3 while counting 5 Game Changers. That is inconsistent, and it is corrected to B4.

## Commander model (attack this first)
Loki, the Deceiver ({1}{U}{B}{R}, Legendary Creature — God Sorcerer Villain 4/4; `msc`, released 2026-06-26; Commander-legal; not a Game Changer):
- "Whenever Loki attacks, create a tapped and attacking token that's a copy of another target Villain you control, except it isn't legendary and it's an Illusion in addition to its other types. Sacrifice that token at the beginning of the next end step."
- "Whenever one or more Villains you control deal combat damage to a player, draw a card."

How the copy behaves:
- The copy was never declared as an attacker (CR 508.4), so its attack triggers do not fire.
- Its enters triggers (CR 603.6a), static abilities and combat-damage triggers do.
- It uses copiable values (CR 707.2), with X=0 (CR 107.3m).
- If the target Villain leaves in response, the trigger fizzles (CR 608.2b). Lightning Greaves' shroud blocks Loki's own target; Swiftfoot Boots' hexproof does not.
- The Master, Multiplied stops the delayed sacrifice. Roaming Throne (Villain) doubles both Loki's trigger and the copied enters triggers.
- The frozen rulings have no entries for the 2026 Marvel cards; the analysis rests on the Comprehensive Rules.

## Swaps (2 — below the five-swap floor; RESEARCH_ONLY)
**+Ultimo, Civilization's End −Crimson Cowl, Master of Evil (MODERATE).**
- Every Loki copy of Ultimo makes each opponent sacrifice a creature.
- Cowl's copy is a blank 1/3, because its trigger needs nontoken Villains declared as attackers.
- Costs: six mana against three; P(MV ≤3 Villain by turn 3) 0.3005 → 0.2834.
- EDHREC: 131/2281 for Ultimo, absent from the Loki commander pages, against Cowl's 862/2281 (optimized 5/25).
- Staged alternative: cut Kang Prime instead.

**+Elektra, Daughter of the Hand −Killmonger, Ruthless Usurper (MODERATE).**
- Every Loki copy of Elektra destroys an opponent's creature with power 3 or less. Sneak {1}{B}{B} (CR 702.190) returns an unblocked attacker and casts her tapped and attacking.
- Loss: Killmonger's copy keeps its combat-damage artifact sacrifice plus Treasure. Its attack pump is dead on a copy.
- EDHREC: 530/2355 (optimized 4/26) against Killmonger's 796/2258 (6/25).
- Staged alternative: cut Iron Monger, Sadistic Tycoon instead.

**Pass C requested, staged or rejected:**
- +Strionic Resonator −Swiftfoot Boots: staged, not counted.
- +Seize the Day −Black Market Connections / −Urza's Incubator: rejected.

**Staged, not counted:** Victor Timely, Wily Tycoon over Kang Prime. It needs graveyard fuel, has 53/2281 adoption, and Kang Prime's enters half already works on a copy.

**Rejected:**
- Kingpin, Wilson Fisk over Madame Hydra.
- Secluded Courtyard over Path of Ancestry: marginal, about +1 point, with restricted colours.
- Tri-Sentinel, Act of Vengeance: dominated by Ultimo.
- Lady Loki, Agent of Chaos: a cast trigger, dead on a copy.
- Kindred Charge, Twinflame and Helm of the Host: owner-rejected extra clone effects.
- Glorious Purpose: a Plan.
- Archnemesis.
- Vampiric Tutor.
- Ancient Tomb.
- Terminate and Bedevil.
- Hostage Taker: not a Villain.

**Invalid:**
- Hela, Mistress of Darkness // Dark Tutor (unreleased, 2027-04-09).
- Mirror Universe Intrusion (unreleased, 2026-11-13).
- Dockside Extortionist and Jeweled Lotus (banned).

## Pass C requested tests (bounded; `tests/test_m6_loki_the_deceiver_m7_mechanics.py`)
**Seeded goldfish** (seed 28, N=20000 per configuration; P(Loki attacks with a valid target), turns 4/5/6):
- Baseline: 0.1803 / 0.5849 / 0.7069.
- +Strionic −Boots: 0.1801 / 0.5867 / 0.7082. Strionic is payable on an attack turn 0.0164 by turn 5 and 0.0393 by turn 6.
- +Seize −BMC: 0.1772 / 0.5764 / 0.7044. Seize is castable postcombat 0.0219 by turn 6.
- Candidate: 0.1682 / 0.5696 / 0.7003.

**Exhaustive rules grid:**
- Strionic gives more copies in 80/756 paired cells.
- Seize gives more copies in 42/756, but fewer total draws in 630/756.
- Boots adds a combat in 144/342 and more copies in 48.

## Combos (Commander Spellbook find-my-combos, every list, JSON in research_challengers)
- Included combos: 0 in the baseline, the candidate and all eight alternatives.
- Almost-included: 28 (baseline), 28 (candidate), 31 (Strionic) and 29 (Seize).
- Game Changers 5 → 5. Bracket 4 (Optimized).

## Adversarial scenarios (please push here)
1. Is Crimson Cowl better than modelled because its nontoken trigger fires when Loki himself attacks? It does: Loki is a nontoken Villain, so a real Cowl makes one 2/1 per Loki attack. The cut gives that up for an each-opponent edict per attack. Is that trade right?
2. Is Killmonger's connect-for-artifact-sacrifice copy worth more than Elektra's power ≤3 destroy in real pods?
3. Does the curve cost (two three-drops out, P(MV ≤3 Villain by turn 3) 0.3005 → 0.2567) outweigh the removal gain?
4. Should Victor Timely replace Kang Prime despite low adoption?
5. Should the owner revisit Lightning Greaves, whose shroud blocks Loki's own target?

## Tested pool (11 configurations; `data/grixis/m6/ij/tested_pools/Loki__the_Deceiver_M7_tested_configurations_20261023.json`)
1. BASELINE
2. CANONICAL_EXPORT
3. RESEARCH_TWO_SWAP
4. PASS_C_STRIONIC_RESONATOR_OVER_SWIFTFOOT_BOOTS
5. PASS_C_SEIZE_THE_DAY_OVER_BLACK_MARKET_CONNECTIONS
6. PASS_C_SEIZE_THE_DAY_OVER_URZAS_INCUBATOR
7. ALT_ULTIMO_OVER_KANG_PRIME_KEEP_CRIMSON_COWL
8. ALT_ELEKTRA_OVER_IRON_MONGER_KEEP_KILLMONGER
9. STAGED_VICTOR_TIMELY_OVER_KANG_PRIME
10. REJECT_KINGPIN_OVER_MADAME_HYDRA
11. REJECT_SECLUDED_COURTYARD_OVER_PATH_OF_ANCESTRY

Configurations 4–11 are complete 100s built on the candidate, so each differs from it in exactly one slot. The goldfish rows for Strionic and Seize above compare single swaps on the baseline.

## Distinctness (disclosed)
Nonbasic names shared, candidate/baseline (registry Archidekt exports):
- Doctor Doom, King of Latveria 53/53
- Be'lakor, the Dark Master 42/42
- Admiral Brass, Unsinkable 40/40
- Nathan Drake, Treasure Hunter 40/40

The swaps leave overlap unchanged: none of the four swap cards is in any of the four decks. Twenty-four Loki-unique names (see the decision review) carry the copy plan.

## Infra disclosure
- No new shared-infrastructure edits. The gate, schema, checker and shared tests on this branch are byte-identical to PR #675 head 3465b542 and PR #674 head b505d828 (carried from the #651 chain). There are no registry edits.
- New files are deck-scoped artifacts, three deck tests and the workflow `.github/workflows/m7-loki-the-deceiver.yml`.
- Merge order: #651 → … → #674 → #675 → this PR (#676).
