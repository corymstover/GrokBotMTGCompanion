# Cycle 99 — Abaddon Oracle-tutor coverage critique (preliminary, not independent Pass C)

**Phase:** M6, evidence-only. **Status:** fixed-seed CI successfully rebuilt and independently replayed the candidate comparison. **Author:** ChatGPT engineering-cycle self-review; NOT formal independent judgment.

## Frozen authority and research
- Approved Abaddon list remains unchanged: logical `lh1:5a1e5e5bb86ba35d7dbf712fbc3a7d29c3e05a17569c05e8a11976321699b793`, raw authorized SHA-256 `2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf`.
- Full source 100-card list export SHA-256 `5448d76193923a3f9e3d4c41a327eaeaa9c6326d484d8e5a9abaf3852db2efff`.
- [Preregistration](../phase_b_plans/abaddon_tutor_state_01.json) precedes implementation; [Cycle 99 evidence](../phase_b_bounded/abaddon_tutor_state_01.json) stores four frozen-Oracle digests, updated paired hit coverage, tutor zone-resolution totals and matching baseline trace digests across both swaps.
- Seeds, sampled residual libraries, fixed hand/turn six/turn seven mana, scripted opponent life and two response profiles are identical to the prior cycle. Samples are 240 shuffles per candidate per response profile; **these are not 240 multiplayer games**.

## Actual additional effects (4)
Demonic Tutor searches a card into hand; Mystical Tutor searches instant/sorcery only to top of library; Imperial Seal and Vampiric Tutor search any card to top and cost the controller 2 life on resolution. Each uses deterministic, preregistered target selection, actual library removal and shuffle, and explicit destination; no cards are conjured or effects fabricated. A tutored top card can be the next eligible cascade hit, as demonstrated by adversarial tests.

## Comparable, fixed no-removal replay coverage

| Scripted configuration | Cycle 98 modeled/offered | Cycle 99 modeled/offered | Cycle 99 unmodeled |
|---|---:|---:|---:|
| Approved Bituminous Blast baseline | 140/480 (29.2%) | 173/480 (36.0%) | 307/480 (64.0%) |
| Heartless Hidetsugu replacing Blast | 141/475 (29.7%) | 191/475 (40.2%) | 284/475 (59.8%) |
| Tree of Perdition replacing Blast | 142/474 (30.0%) | 194/474 (40.9%) | 280/474 (59.1%) |

Under source-removed-before-activation, the baseline remains 173/480 supported, Heartless 79/240 and Tree 86/240. **None of these coverage fractions measures card quality or improvement**; the mana values and trigger multiplicities differ, and tutor target policy is highly constrained.

## Tutor audit (no-removal)
- Approved baseline 28 tutor spells resolved over 240 scripted trials (9 to hand, 19 to top; total 30 pilot life paid across Vampiric/Imperial resolutions).
- Heartless variant 46 tutor resolutions (5 to hand, 41 to top; pilot 54 life paid).
- Tree variant 49 tutor resolutions (6 to hand, 43 to top; pilot 56 life paid).
- These are aggregate event counts, not game win probabilities or optimized tutor choice evidence. They must not be used to rank variants.

## Limitations and open gates
1. A majority of cascade hits still have **unmodeled** effects. Real-life Magic often casts them; this conservative interpreter always declines them and so cannot calculate gameplay value or win rate.
2. Script starts with Abaddon deployed, fixed Boltwave/slot/Flame Rift in hand, injected mana, target availability and artificially scripted source removal. It does not model likelihood of these conditions.
3. Search choice is one deterministic priority list, not a rational deck-specific tutor strategy, state-search optimizer or opponent-responsive policy. Card selection can alter follow-up hand access; the scripted model now respects this where supported, but does not play subsequent tutored hand cards autonomously.
4. The engine does not resolve most blockers, counters, alternative costs, the full multiplayer priority system, attack triggers, recursion, all timing edge cases, or opponent survival probabilities. Some existing supported effects rely on deliberately chosen coarse simplifications.
5. Authoring-cycle test/review is **not** an independent Pass C critic. No Phase B closeout, improvement/zero-improvement certificate, I/J formal receipts, user card-swap approval, M6 acceptance or M7/M8 completion follows.

## Recommended next engineering gate
Stop interpreting the % supported as the primary success metric. Before further proliferation of individual card handlers, build a **generalized zone/hand/stack/mana policy** with full 99-card actual draw-state and interaction windows; test its source-hash, deterministic replay, card-count conservation, opponent policy and zero fabricated effects. Expose an explicit 'cannot evaluate' outcome when completeness is insufficient. If extending individual effects, prioritize commander marginal value and impact on meaningful decisions, not raw hit coverage. Continue across all 62 commanders only after appropriate safeguards generalize.
