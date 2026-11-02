# Archived Phase 1B workflows (2026-11-02)

> These 28 dated GitHub Actions YAML entry points were consolidated into `.github/workflows/phase1b-family-validation.yml`. Their source-audit scripts and regression tests were **not deleted**. Git retains the exact old workflow versions at main commit `156fd7cbca64756884660b894ae2e0b5ae145b7a`.

## Preserved checks

- `python3 scripts/audit_phase1b_family_ci.py --check`: 29 read-only source/product-family audit commands, 29/29 passed locally before consolidation.
- The consolidated Action also runs the legacy `test_*sources.py` suite; the new full-Python-suite Action runs all discoverable tests.
- `phase1b-set-atlas-validation.yml` remains separate because the exact nine-domain CI certification references it.
- Obsolete branch-specific artifact-committing/fetch-writing steps were intentionally **not** carried forward; future source updates must be deliberate and separately reviewed.

## Archived Actions

| Historical file | Original version |
|---|---|
| `phase1b-apac-lunar-year-promos.yml` | [v3.09 YAML](https://github.com/corymstover/GrokBotMTGCompanion/blob/156fd7cbca64756884660b894ae2e0b5ae145b7a/.github/workflows/phase1b-apac-lunar-year-promos.yml) |
| `phase1b-art-series-sources.yml` | [v3.09 YAML](https://github.com/corymstover/GrokBotMTGCompanion/blob/156fd7cbca64756884660b894ae2e0b5ae145b7a/.github/workflows/phase1b-art-series-sources.yml) |
| `phase1b-boxed-precon.yml` | [v3.09 YAML](https://github.com/corymstover/GrokBotMTGCompanion/blob/156fd7cbca64756884660b894ae2e0b5ae145b7a/.github/workflows/phase1b-boxed-precon.yml) |
| `phase1b-boxed-special-lair-global.yml` | [v3.09 YAML](https://github.com/corymstover/GrokBotMTGCompanion/blob/156fd7cbca64756884660b894ae2e0b5ae145b7a/.github/workflows/phase1b-boxed-special-lair-global.yml) |
| `phase1b-boxed-specialty.yml` | [v3.09 YAML](https://github.com/corymstover/GrokBotMTGCompanion/blob/156fd7cbca64756884660b894ae2e0b5ae145b7a/.github/workflows/phase1b-boxed-specialty.yml) |
| `phase1b-commander-modern.yml` | [v3.09 YAML](https://github.com/corymstover/GrokBotMTGCompanion/blob/156fd7cbca64756884660b894ae2e0b5ae145b7a/.github/workflows/phase1b-commander-modern.yml) |
| `phase1b-commander-series.yml` | [v3.09 YAML](https://github.com/corymstover/GrokBotMTGCompanion/blob/156fd7cbca64756884660b894ae2e0b5ae145b7a/.github/workflows/phase1b-commander-series.yml) |
| `phase1b-commander-set-linked.yml` | [v3.09 YAML](https://github.com/corymstover/GrokBotMTGCompanion/blob/156fd7cbca64756884660b894ae2e0b5ae145b7a/.github/workflows/phase1b-commander-set-linked.yml) |
| `phase1b-cross-category.yml` | [v3.09 YAML](https://github.com/corymstover/GrokBotMTGCompanion/blob/156fd7cbca64756884660b894ae2e0b5ae145b7a/.github/workflows/phase1b-cross-category.yml) |
| `phase1b-draft-starter-batch2.yml` | [v3.09 YAML](https://github.com/corymstover/GrokBotMTGCompanion/blob/156fd7cbca64756884660b894ae2e0b5ae145b7a/.github/workflows/phase1b-draft-starter-batch2.yml) |
| `phase1b-draft-starter-sources.yml` | [v3.09 YAML](https://github.com/corymstover/GrokBotMTGCompanion/blob/156fd7cbca64756884660b894ae2e0b5ae145b7a/.github/workflows/phase1b-draft-starter-sources.yml) |
| `phase1b-duel-decks.yml` | [v3.09 YAML](https://github.com/corymstover/GrokBotMTGCompanion/blob/156fd7cbca64756884660b894ae2e0b5ae145b7a/.github/workflows/phase1b-duel-decks.yml) |
| `phase1b-event-collab-promos.yml` | [v3.09 YAML](https://github.com/corymstover/GrokBotMTGCompanion/blob/156fd7cbca64756884660b894ae2e0b5ae145b7a/.github/workflows/phase1b-event-collab-promos.yml) |
| `phase1b-fasttrack-readiness.yml` | [v3.09 YAML](https://github.com/corymstover/GrokBotMTGCompanion/blob/156fd7cbca64756884660b894ae2e0b5ae145b7a/.github/workflows/phase1b-fasttrack-readiness.yml) |
| `phase1b-full-set-export-acceptance.yml` | [v3.09 YAML](https://github.com/corymstover/GrokBotMTGCompanion/blob/156fd7cbca64756884660b894ae2e0b5ae145b7a/.github/workflows/phase1b-full-set-export-acceptance.yml) |
| `phase1b-historical-promo-series.yml` | [v3.09 YAML](https://github.com/corymstover/GrokBotMTGCompanion/blob/156fd7cbca64756884660b894ae2e0b5ae145b7a/.github/workflows/phase1b-historical-promo-series.yml) |
| `phase1b-historical-shards.yml` | [v3.09 YAML](https://github.com/corymstover/GrokBotMTGCompanion/blob/156fd7cbca64756884660b894ae2e0b5ae145b7a/.github/workflows/phase1b-historical-shards.yml) |
| `phase1b-inserts-clash-spellbook.yml` | [v3.09 YAML](https://github.com/corymstover/GrokBotMTGCompanion/blob/156fd7cbca64756884660b894ae2e0b5ae145b7a/.github/workflows/phase1b-inserts-clash-spellbook.yml) |
| `phase1b-masterpiece-memorabilia.yml` | [v3.09 YAML](https://github.com/corymstover/GrokBotMTGCompanion/blob/156fd7cbca64756884660b894ae2e0b5ae145b7a/.github/workflows/phase1b-masterpiece-memorabilia.yml) |
| `phase1b-product-family-triage.yml` | [v3.09 YAML](https://github.com/corymstover/GrokBotMTGCompanion/blob/156fd7cbca64756884660b894ae2e0b5ae145b7a/.github/workflows/phase1b-product-family-triage.yml) |
| `phase1b-qualified-functional-release.yml` | [v3.09 YAML](https://github.com/corymstover/GrokBotMTGCompanion/blob/156fd7cbca64756884660b894ae2e0b5ae145b7a/.github/workflows/phase1b-qualified-functional-release.yml) |
| `phase1b-release-scope-story-acceptance.yml` | [v3.09 YAML](https://github.com/corymstover/GrokBotMTGCompanion/blob/156fd7cbca64756884660b894ae2e0b5ae145b7a/.github/workflows/phase1b-release-scope-story-acceptance.yml) |
| `phase1b-reprint-curated.yml` | [v3.09 YAML](https://github.com/corymstover/GrokBotMTGCompanion/blob/156fd7cbca64756884660b894ae2e0b5ae145b7a/.github/workflows/phase1b-reprint-curated.yml) |
| `phase1b-set-products.yml` | [v3.09 YAML](https://github.com/corymstover/GrokBotMTGCompanion/blob/156fd7cbca64756884660b894ae2e0b5ae145b7a/.github/workflows/phase1b-set-products.yml) |
| `phase1b-token-families-sources.yml` | [v3.09 YAML](https://github.com/corymstover/GrokBotMTGCompanion/blob/156fd7cbca64756884660b894ae2e0b5ae145b7a/.github/workflows/phase1b-token-families-sources.yml) |
| `phase1b-wotc-early-sets.yml` | [v3.09 YAML](https://github.com/corymstover/GrokBotMTGCompanion/blob/156fd7cbca64756884660b894ae2e0b5ae145b7a/.github/workflows/phase1b-wotc-early-sets.yml) |
| `phase1b-wotc-mid-sets.yml` | [v3.09 YAML](https://github.com/corymstover/GrokBotMTGCompanion/blob/156fd7cbca64756884660b894ae2e0b5ae145b7a/.github/workflows/phase1b-wotc-mid-sets.yml) |
| `phase1b-wotc-premier.yml` | [v3.09 YAML](https://github.com/corymstover/GrokBotMTGCompanion/blob/156fd7cbca64756884660b894ae2e0b5ae145b7a/.github/workflows/phase1b-wotc-premier.yml) |
