# Cycle 126 — Nicol Bolas, the Ravager: source-paid Mox Diamond versus Aetheric Amplifier

**Verdict-neutral bounded evidence, NOT a user-approved deck swap.** This experiment responds to GrokBot's conditional Pass C **REPLACE** recommendation for Aetheric Amplifier by directly comparing real source-card physical mana support, early Bolas deployment, and the conditional later planeswalker counter payoff.

## Exact authority and preregistration

- Preregistration first committed at `8e71a598e1a8a90953e5a25197c10b6b54bc96d8` on branch `chatgpt-cycle126-bolas-source-mana-loyalty-pressure`, from M6 integration `aa3a18821b908b62b5dc7e80a5a77ae5ab896429`.
- Approved baseline 99 + Nicol Bolas commander and single physical slot Mox Diamond → Aetheric Amplifier challenger were verified against the current engineering approved deck block, the exact canonical logical hash `lh1:c2b4559a1e5f0415decb48a9f496f1f780af715f6f763d3fcb166753dbfda293` and recorded approved TXT SHA-256.
- Frozen 2026-10-16 Scryfall archive hash `ea7abac9906633415553b585b32c4071c79d42ba23d7e3163a0c4e9c265a7483`; the Mox, Amplifier, and front/back Nicol Oracle cost/text and starting loyalty were checked.
- 1,024 *paired same-98-slot shuffles*, each with 7 opening cards and 1 draw per own turn through turn 8. Three fixed source-pilot policies produce 3,072 policy views; **these are correlated paired observations, not 3,072 independent deck trials**.
- Printed land mana uses only 19 previously Oracle-gated nonbasics + basic lands; unsupported fetches, pathways, City of Brass, Ancient Tomb, tutors, treasures, rituals and other rocks do not generate mana. Deterministic color-neutral land play policy, shock-life choices, and nominal three-player bondland conditions are not optimized strategies.
- Actual physically held land cards are moved to graveyard to enter a Mox after an available land play. Mox cannot enter if no eligible land remains; its own same-turn any-color mana is modeled and cannot tap twice. Amplifier is physically paid for {3}; its {T}: add mana any color and {4},{T} counter doubler **share a tap**. No double may be paid using Amplifier's own mana tap at the same moment.

## Exact modeled results

| Bounded metric | Baseline Mox: commander-first | Challenger Amp: cast early | Challenger Amp: commander-first |
|---|---:|---:|---:|
| Physical paired samples | 1024 | 1024 | 1024 |
| Source-backed Mox entries / paid Amplifier casts | 137 | 65 | 18 |
| Uncontested source-payable Nicol Bolas casts by turn 8 | **300** | 296 | 267 |
| Bolas casts by turn 3 | **13** | 0 | 0 |
| Bolas transforms (paying {4}{U}{B}{R}) | 3 | 3 | 3 |
| Amplifier {4},{T} loyalty doubling paid | N/A | 1 | 1 |
| Hypothetical surviving planeswalkers after 3 damage | 3 | 3 | 3 |
| Hypothetical surviving after 8 damage | 0 | 1 | 1 |
| Hypothetical surviving after 13 damage | 0 | 1 | 1 |

First eligible commander-turn counts (total casts, turn 3–8):
- Baseline Mox: T3 13; T4 88; T5 49; T6 50; T7 43; T8 57.
- Amp cast-early: T3 0; T4 98; T5 45; T6 56; T7 42; T8 55.
- Amp commander-first: T3 0; T4 89; T5 41; T6 45; T7 36; T8 56.

**Interpretation:** The baseline's earliest T3 opportunities illustrate Mox's unique free acceleration, but 137 Mox entries do not all imply early casting. The paid {3} Amplifier can tap for mana immediately as a **noncreature artifact**, and the early policy nearly matches baseline by T8 *within this restricted model*. The commander-first challenger defers Amplifier and has fewer payable commander deployments; this sensitivity is part of the result, not a deck ranking.

## Late planeswalker payoff is not statistically established

Bolas is required to be source-paid {1}{U}{B}{R} first, then transformed in a later modeled own main phase by paying the seven-mana activated cost {4}{U}{B}{R}. He enters his transformed planeswalker face with **seven** loyalty. Amp's doubling is only attempted after it is cast, untapped, in own main phase, and four **other** physically modeled mana sources pay its activated cost. No extra loyalty ability is granted. Only 3 transformations per policy and 1 source-paid candidate doubling were seen, making any real power claim unsubstantiated.

The reported 3-, 8-, and 13-damage survival columns are **hypothetical immediate loyalty thresholds**, not sampled attacks, combat, turn-by-turn multiplayer pressure, or actual wins. No ETB discard events, loyalty +2/-3/-4/-12 abilities, interaction, commander deaths, recast tax, land filtering, tutors, opponent spell/tutor timing, or phase structure beyond the narrow main-phase resource policy are simulated.

The conditional result **does not overturn** the currently approved Mox Diamond inclusion, and does not disprove Amp's potential benefit in real prolonged superfriends games. The only responsible disposition is **KEEP approved list / REQUIRES FURTHER TESTS**, independent M6 judgment still unresolved. GrokBot's conditional REPLACE proposal is preserved as an external perspective.

## Evidence verification and milestones

[GitHub Actions #39203646384](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/39203646384): 16 adversarial/positive tests PASS; frozen Oracle checksum PASS; 1,024 paired sampled source states across three registered policies built **and replayed identically**, with explicit printed metrics. Source JSON artifact `cycle126-bolas-source-paid-mox-amplifier-pressure-receipt` (ID `12165141015`). Original source and candidate hash/tracker gates unmodified.

- M6 remains **in progress**: secondary **3/10 named completed gates** (two partial), formal 0/62 M6-certified.
- M7 **not started**: secondary **0/6**; 0/62 second-cycle decisions.
- Canonical 62/62 approved and locked untouched. M8-certified 0/62.
- No independent Pass C completion, full Phase B paired gameplay assessment, tournament win rate, approval or automatic swap.

**Next gate:** introduce source-verified interaction and opponent pressure **with explicit actual modeled turn sequences**, preserve the commander-specific value of ETB hand disruption and loyalty trajectories, and obtain independent review of any changed optimization verdict. Avoid repeated speculative percentages from resource-only models.
