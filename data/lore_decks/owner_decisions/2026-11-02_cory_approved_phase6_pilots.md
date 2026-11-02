# Cory's exact owner approval — three original Phase 6 lore pilots

**Decision date:** 2026-11-02. **Owner:** Cory. **Outcome:** all three **original historical decklists approved**, as-is, without card substitutions.

> Approve these three exact historical decklists — record approval against the three source SHA-256 hashes shown above, without changing cards.

Cory additionally stated: **“We will make changes later. I just want to get this checked off the liat for now.”** This explicitly supersedes the earlier intention to rebuild the pilots *before* individual owner acceptance. It authorizes **approval of these exact revisions**, not an optimized rebuild or advance acceptance of later revisions.

The exact source files were reviewed on repository `main` at `e620fd60a75abf8e1b966a89a518ff105d8aa7df`. The associated original proposals, evidence, decklists, import lists and three unapproved-era spec files remain **byte-for-byte untouched by this approval**. Their old `UNAPPROVED PROPOSAL` fields are historical draft metadata, **not current owner approval authority**; this newer, SHA-bound record overrides only their owner-decision status.

| Checklist | Approved pilot | Commander | Exact raw decklist SHA-256 | Original source |
|---|---|---|---|---|
| K112 | Pilot 1 — Ugin & Nicol Bolas: Elder Dragon Duality | Nicol Bolas, the Ravager | `01d087aa2819b1ed3c7ac1f64843f76f36b551b72fda62d64218d19c40b0ab45` | [100-card decklist](../drafts/ugin_bolas_elder_dragon_duality_decklist.txt) · [PR #823](https://github.com/corymstover/GrokBotMTGCompanion/pull/823) |
| K113 | Pilot 2 — Original & Primeval Dragons | The Ur-Dragon | `6ef1af37c371891b7d3e60a08c2d1bcee1d1205f2c01e5c3093a220fb4414888` | [100-card decklist](../drafts/original_primeval_dragons_decklist.txt) · [PR #832](https://github.com/corymstover/GrokBotMTGCompanion/pull/832) |
| K114 | Pilot 3 — Ugin's Allies and Heroes | Jace, Multiverse Architect | `05cd56bd3d58b153f35ad86f896d6c383f99bca9722e6124e627daad74641c6c` | [100-card decklist](../drafts/ugins_allies_and_heroes_decklist.txt) · [PR #844](https://github.com/corymstover/GrokBotMTGCompanion/pull/844) |

The machine-readable [approval register](2026-11-02_cory_approved_phase6_pilots.json) and `scripts/audit_lore_pilot_owner_approvals.py --check` independently require the exact hashes, 100 cards, original pilot audits, and unchanged historical draft approval flags. K112–K114 are now owner-approved and can be checked off; K105/K125/K126 remain genuinely recurring upkeep.

**Limitations:** The original October 29 Scryfall printing/legality evidence and November 1 strategy preflight still apply. Owner approval does **not** certify current banned-list legality, 2026-11-02 interactions, a current Commander bracket, playtesting, realistic power, or unknown lore. No new Rule 0 exception is invented. The high mana curves and casual-power weaknesses remain documented. Future card changes require a **new** exact owner approval and a separately audited revision; these approved historical hashes remain recoverable.

The separate nine numbered lore decks (#1–8 and #10), the unapproved Ugin biography Deck #9, and all 62 canonical Grixis decks are unaffected.
