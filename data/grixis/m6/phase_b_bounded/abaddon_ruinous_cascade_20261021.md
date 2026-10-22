# Abaddon — targeted Phase B Ruinous Powers owner-loss and cascade timing

**Date:** October 21, 2026 (America/Chicago). **Deck:** `Abaddon_the_Despoiler`.
**Canonical authority:** `corymstover/grixis-commander-encyclopediaGPT/main/state/current_deck_overrides.json`; approved/locked original list SHA-256 `2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf`. **No list changes or M7 owner approval.**

## Why test this slot

The M6.7 judgment considered cutting **The Ruinous Powers** for **Aggravated Assault** but decided to retain its commander-first exile engine. Its apparent liability (a five-mana randomly selected opponent-card engine) must be evaluated against its actual interaction with Abaddon's life-loss threshold. A rules error here could cause a false cut.

Official source: [Wizards, Warhammer 40,000 Commander release notes — The Ruinous Powers](https://magic.wizards.com/en/news/feature/warhammer-40000-commander-release-notes-2022-09-19). Baseline Abaddon and Ruinous Oracle were previously audited in the canonical Oct 13 card-audit CSV. Abaddon grants cascade only to spells cast **from your hand** whose mana value is no greater than the total life lost by opponents **this turn**.

## Bounded executable evidence

`scripts/grixis_m6_abaddon_ruinous.py` and `tests/test_m6_abaddon_ruinous.py` trace 14 deterministic assertions about *where a card came from*, *who owns it*, *legal timing*, *spell versus land*, *the trigger's life-loss amount* and *later hand-cast cascade*. Opponents and their cards are scripted; the Ruinous trigger is assumed to resolve without interaction. Actual mana payment, card acquisition, random opponent choice, cascade flips, opponent response likelihood, color availability and real gameplay are not modeled.

- When you **cast** a spell exiled from an opponent's library through Ruinous, the **opponent who owns it**, not its caster, loses life equal to its mana value **when Ruinous's trigger resolves**. Thus casting an opponent-owned mana-value-5 spell can move the **later** hand-spell cascade threshold from 0 to 5 during the same turn.
- **The exiled spell itself does not receive Abaddon's cascade**, even if Abaddon is on battlefield, because it was cast from exile rather than your hand. This avoids incorrectly counting a double payoff.
- Playing an exiled **land** is not casting a spell and produces no Ruinous owner-loss trigger. Legal timing, available land play, and normal mana payment remain real restrictions; the enchantment allows color-flexible payment but does not make the spell free.
- The effect does **not** carry last turn's life loss into the current turn. Without Abaddon, the owner-loss still occurs but no commander-granted hand cascade happens.
- These branches support *preserving Ruinous as a credible synergy slot*, **not** a measured superiority claim or a KEEP certification. Five-mana setup, randomness, opponent deck composition, legal access to the exiled card, and opportunity cost remain unresolved.

**Classification:** effect-aware *bounded deterministic rules/interaction fixture* only; **not** 100-card simulation, real opponent gameplay, goldfish win rate, multiplayer win rate, all-rules verifier, final M6.6/M6.7 certification, or permission to touch a canonical deck. The 62/62 owner-equivalent Pass C waiver does not waive these remaining requirements.
