---
title: "EDH Lift and Synergy"
category: edh
tags: [lift, synergy, edhrec, evidence, methodology]
issues: []
generated_by: hand-written
sources: [edhrec, cr]
related: ["EDH Commander-First Deckbuilding.md"]
schema: 2
---

# EDH Lift and Synergy

> **Bot cycle 57.5 (M3).** What EDHREC's *synergy* and *lift* numbers are, how to read them, and how this companion uses them as evidence. EDHREC numbers describe what deckbuilders put in their lists; they are **community data (`derived_metric`)**. They inform a decision and never make it (the [authority model's](grixis/Grixis%20Authority%20Model.md#evidence-classes) decision rule).

## Contents
- [Definitions (EDHREC's own)](#definitions-edhrecs-own)
- [Worked examples from the cache](#worked-examples-from-the-cache)
- [How to read them](#how-to-read-them)
- [How the companion uses them](#how-the-companion-uses-them)
- [Sources](#sources)

## Definitions (EDHREC's own)

All of this is paraphrased from EDHREC's articles (links under [Sources](#sources)).

- **Inclusion rate:** the share of a commander's eligible decks that run the card. On a commander page this is *decks with the card* / *potential decks*, the number shown under every card.
- **Potential decks:** the decks that *could* hold the card. EDHREC limits them by colour identity and by date: when either card in a pair was spoiled within its two-year data window, only decks saved after the later spoil date count. That is why two cards on one page can show different denominators.
- **Synergy (retired):** inclusion rate with this commander **minus** the card's inclusion rate across all decks of the commander's colour identity. It is a percentage centred on 0. EDHREC's own example: Miirym in 81% of The Ur-Dragon decks and 11% of five-colour decks gives +70%. EDHREC itself now says the score lacked a mathematical basis: it was invented early and kept because the results looked useful. It also favours popular cards.
- **Lift:** how often two cards (or a commander and a card) appear together **relative to what independence predicts**. It is an established association-rule metric: P(A and B) / (P(A)·P(B)). For a commander page it simplifies to *inclusion rate with this commander* / *inclusion rate in potential decks*. It is a ratio centred on 1: above 1 the pairing is more common than chance, below 1 less common. It is bounded below by 0 and unbounded above, and it behaves logarithmically (0.5 is as strong a negative signal as 2.0 is a positive one). It is symmetric, which synergy was not.
- **Timeline:** card pages switched to lift in December 2025. Commander, tag and combo pages followed on 1 October 2026.
- **Ubiquitous staples:** EDHREC names basics, Swords to Plowshares, Arcane Signet, Sol Ring and Command Tower (played in more than 50% of candidate decks). They get lift near 1 everywhere, where synergy gave them extreme values.

## Worked examples from the cache

Numbers from `data/grixis/evidence/` (EDHREC commander pages cached 2026-10-16). Synergy and inclusion are fractions.

| Commander page | Card | Decks | Inclusion | Synergy | Lift | Baseline = inclusion − synergy | inclusion ÷ baseline |
|---|---|---|---|---|---|---|---|
| Abaddon the Despoiler | Sol Ring | 6,227 / 6,744 | 0.923 | +0.026 | 1.029 | 0.897 | 1.029 ✓ |
| Abaddon the Despoiler | Arcane Signet | 5,041 / 6,744 | 0.747 | −0.135 | 0.847 | 0.882 | 0.847 ✓ |
| Wick, the Whorled Mind | Arcane Adaptation | 2,054 / 12,413 | 0.165 | +0.155 | 15.14 | 0.011 | 15.14 ✓ |
| Loki, the Deceiver | Black Market Connections | 1,339 / 2,294 | 0.584 | +0.452 | 3.353 | 0.132 | 4.44 ✗ |

- **Sol Ring** is in 92% of Abaddon decks, but it is in about 90% of Grixis decks anyway. Lift is ≈ 1, so it tells you nothing about Abaddon.
- **Arcane Adaptation** is in only 17% of Wick decks, but that is 15× its Grixis baseline. This is the "hidden gem" lift is built to surface. It is also Wick's identity-core type-changer (blueprint `pkg:type-changers`).
- **The check column:** if synergy and lift use the same baseline, lift = inclusion / (inclusion − synergy). That holds to 0.1% on 51 of the 62 cached pages.
  - On 11 pages it fails for some rows (1,851 rows; Loki's Black Market Connections is one). Those pages are Doctor Doom, Dr. Eggman, Edea, Fire Lord Azula, Kefka, Loki, Mai and Zuko, Nathan Drake, Norman Osborn, The Madcap Jester and Tresserhorn's Lord.
  - On them the two numbers rest on different baselines. Most are recent-set commanders, so the spoil-date limit on potential decks is a plausible cause. That is a hypothesis; EDHREC doesn't publish the per-row baselines.

## How to read them

These are guidance points, not rules:

- **Inclusion shows popularity; lift shows specificity.** A card with high inclusion and lift ≈ 1 is a staple. Its case rests on its own power, not on the commander. A card with low inclusion and high lift is specific to this commander. Its case rests on the commander interaction, so check the Oracle text.
- **Sample size first.** Lift on a page with 40 potential decks, or a card in 8 decks, is noise. The companion marks under 50 potential decks or under 20 decks as `small_sample`.
- **Lift is not quality.** EDHREC itself warns that most decks in the data aren't built optimally. Its numbers also shape the behaviour they measure: cards shown together get played together.
- **Precons and new sets distort it.** Fresh commanders have few decks, many of them precon-shaped.
- **Use filters for your question.** EDHREC commander pages can be filtered by bracket, budget and tag. An unfiltered page mixes Bracket 2 and cEDH lists.
- **Trend** (EDHREC's trend z-score) shows movement, not merit. The companion flags |z| ≥ 2 as rising or falling.

## How the companion uses them

- **Evidence vectors** (`scripts/grixis_evidence.py`, Bot cycle 57.1) store lift, synergy, inclusion, sample size, trend and retrieval date for every canonical card and every EDHREC candidate on the deck's page. The EDHREC part is always `derived_metric`, `moderate` at most, and `low` when the sample is small, when partner pages were pooled, or when lift and synergy disagree (the ✗ case above).
- **Never a deciding vote:** a swap justified only by EDHREC numbers is refused by the decision rule (`decision_support_ok`). It needs a fact (Oracle text, combo, rules) or a test result, and in the end Cory's approval.
- **Candidate generation, not candidate approval:** high-lift cards missing from a list are candidates. They are then checked against the blueprint (identity core, packages, anti-goals), the interaction review and paired goldfish tests. See [EDH Commander-First Deckbuilding](EDH%20Commander-First%20Deckbuilding.md).

## Sources

- EDHREC (Julia Maddalena), [From Synergy to Lift: The Math Behind EDHREC's New Era of Recommendations](https://edhrec.com/articles/from-synergy-to-lift-the-math-behind-edhrecs-new-era), 15 Dec 2025. Definition, symmetry and the log scale, the spoil-date and colour-universe limits on potential decks, ubiquitous staples, and the caveat about suboptimal decks.
- EDHREC (keattz), [Changelog: Replacing Synergy with Lift](https://edhrec.com/articles/changelog-replacing-synergy-with-lift-on-edhrecs-card-pages), 1 Oct 2026. The commander-page formula as inclusion ÷ inclusion in potential decks, and the rollout to commander, tag and combo pages.
- EDHREC, [An Interview with the EDHREC Dev Team on Lift Scores](https://edhrec.com/articles/an-interview-with-the-edhrec-dev-team-on-lift-scores). Commander-page filters, and synergy surfacing popular cards where lift surfaces specific ones.
- EDHREC, [Commander Philosophy – The Difference Between Synergy and Exploiting](https://edhrec.com/articles/commander-philosophy-the-difference-between-synergy-and-exploiting). The old synergy definition and the Miirym example.
- Cached data: `.cache/edhrec/commanders__*.json` (EDHREC public JSON, retrieved 2026-10-16), summarised in `data/grixis/evidence/`.
