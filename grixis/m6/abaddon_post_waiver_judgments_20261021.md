# Abaddon — post-waiver M6.7 judgment synthesis (not M6/M7 approval)

**Date:** 2026-10-21 (America/Chicago)  
**Author:** ChatGPT/OpenAI GPT-6, original same-family source reviewer (not independent)  
**Status:** **INTERIM named strategic judgments**: all proposed changes **HOLD**, no canonical edit, no full M6.7 gate promotion.  
**Exact owner-approved baseline raw SHA-256:** `2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf`; `APPROVED / LOCKED`, 100 cards (94 distinct names, 34 lands).  
**Governance:** Cory's 2026-10-21 independent-review waiver is recorded at `data/grixis/m6/governance/pass_c_owner_waiver_20261021.json`. It qualifies owner-equivalent Pass C for M6.5 **without** making this review independent or completing Phase B/M6.

## Why this follows the comprehensive review, rather than replacing it

This is a narrowly scoped synthesis of the [complete 100-card authored review](../../data/grixis/m6/deep_reviews/Abaddon_the_Despoiler.md), the [sealed owner-equivalent Pass C final disposition](../../data/grixis/m6/owner_pass_c_substitute/Abaddon_the_Despoiler/final_disposition.md), the [Neheb/Assault/Loyal effect-aware finite trace](../../data/grixis/m6/phase_b_bounded/abaddon_neheb_assault_20261021.md), and the [Rakdos opportunity-cost audit](abaddon_rakdos_opportunity_cost_20261021.md). The original review compared the meaningful 98 M5 records and 60 legacy candidate decisions, plus multiple off-ranking alternatives. The new finding changes the *weight* of the incumbent's role but not the authority of any old card swap.

### 1. Assault vs Rakdos is not a one-sided upgrade

**Aggravated Assault's real upside:** An unopposed four-permanent setup (Abaddon + Loyal Subordinate + Neheb, the Eternal + Assault) can drain at every extra combat. Each Loyal trigger loses three life per opponent with Abaddon continuously present; Neheb adds red at each postcombat main based on aggregate current-turn opponent life loss; Assault spends `{3}{R}{R}` to add another combat and main phase. Ten exact deterministic rules tests passed CI in PR #504. It is *a genuine combo interaction*, not a measured availability or win-rate claim.

**Rakdos's real opportunity cost:** With Rakdos resolved and sufficient same-turn opponent life loss, its cost reduction applies to **creature spells**, including Neheb, Loyal, and Abaddon commander casts; generic commander tax can also be reduced after cost increases, but colored costs remain. The locked list has 17 **potential** Rakdos-beneficiary creature identities (including Abaddon), not 17 guaranteed discounted cast events. Eleven cost/inventory tests passed CI in PR #506. [Wizards' official Rakdos rulings](https://magic.wizards.com/en/news/feature/ravnica-remastered-release-notes) confirm this generic-only, post-increase reduction. Rakdos itself costs `{B}{B}{R}{R}`, needs an opponent to have lost life to cast, and does not discount itself.

**Judgment:** Keep `+Assault/-Rakdos` as a **material but unapproved challenger**, NOT an established net upgrade. Assault needs Neheb/life-loss/combat-phase resolution; Rakdos is demanding to cast and vulnerable to creature removal but can accelerate many otherwise ordinary creature spells and recasts. Candidate comparisons must include actual source-paid sequencing and realistic opponent interference. Do not let the Pass C `NEEDS TESTING` disposition or the conditional loop auto-apply a swap.

### 2. A critical alternative-cut correction: The Ruinous Powers

**Do not casually cut `The Ruinous Powers` to keep Rakdos.** Its precise text exiles the top card of a **random opponent's** library on your upkeep and lets you play it that turn. If you cast that exiled opponent-owned spell, the spell's **owner (that opponent)** loses life equal to its mana value. That is **not automatically your own life loss**. It can increase Abaddon's same-turn cascade threshold, and casting from exile triggers the deck's nonhand-cast payoffs. See [Wizards' Warhammer 40,000 release notes](https://magic.wizards.com/en/news/feature/warhammer-40000-commander-release-notes-2022-09-19) and the canonical per-card Oracle audit. A land reveal or an unaffordable spell is a real failure case; the upkeep setup is slower. Neither drawback justifies treating this as dead generic five-mana enchantment filler.

Likewise, `The Lost and the Damned` produces 3/3 Spawn tokens when spells are cast from outside your hand. Exiling and casting through cascade makes this a commander-identity payoff; its high setup cost is contestable, but losing it has a genuine cost. Neither of these 40K cards should be sacrificed as an automatic accounting fix for a combo addition.

### 3. Chaos Warp's role is distinct, cut still unresolved

The locked list is strong against stack-based interaction and many creatures, but has limited permanent answers once a hostile **nonblue artifact/enchantment** resolves. `Chaos Warp` (`{2}{R}`, instant) can target such a permanent, shuffle it into its owner's library and reveal that library's top card, potentially putting a different permanent onto the battlefield. It is broad interaction, **not guaranteed permanent eradication**. [Oracle reference](https://www.mtg.wtf/card/sta/36/Chaos-Warp).

Do not cut `Pyroblast`, `Mystic Remora`, the compact Breach/LED/Brain Freeze route, or distinctive cascade/exile pieces merely to make room. A defensible concrete cut and net mana/identity justification remain open. This is a serious M7 role-balancing candidate, not an approved substitution.

## Decision table

| Material item | Interim judgment | Why not already finalized |
|---|---|---|
| `+Aggravated Assault / -Rakdos` | **HOLD challenger** | Four-piece payoff verified conditionally; lost creature-cast discount and true setup likelihood unresolved |
| `+Aggravated Assault / -The Lost and the Damned` | **HOLD alternate cut** | Preserves Rakdos but removes source-native nonhand-cast token engine |
| `+Chaos Warp / -high-cost payoff` | **HOLD** | Real removal gap, but no sufficiently justified named cut |
| `-The Ruinous Powers` | **RETAIN for now** | Casting opponents' cards causes *their owners* to lose life, which helps Abaddon on your turn |

No swap count is required; a verified **KEEP** remains possible, but cannot be determined from the one original Pass C challenger alone. The bracket remains the baseline **Bracket 4 — Optimized** pending final verification.

## Accountability / M6.7 status

The accompanying machine-readable `data/grixis/m6/judgment_reviews/abaddon_phase_b_decisions_20261021.json` contains three named `agent_judgment` receipts with decision-class factual and strategic evidence; it explicitly disallows final deck decisions or certification. These judgments resolve immediate *rules and role* confusion, but still identify decision-relevant access gaps. They do **not** mark M6.7 62/62 complete, certify Abaddon Phase B, pass tested-pool local optimality, change a card, or present a partial M7 deck for owner approval.
