# Post-foundation v3.01: two missing War of the Spark web-story chronology chapters

**Status:** `PRELIMINARY_SOURCE_LOCAL_RESEARCH`. The independently certified v3.00 knowledge foundation is unchanged. K099 (broader Bolas/War of the Spark history) and K103 (cross-plane chronology/retcons) remain **UNDER REVIEW**.

## Source-specific event evidence

Two of the six already registered official *War of the Spark: Ravnica* chapters had story claims but no events in the original four-chapter operational chronology `Y`. This is a separate, versioned supplement using only those two previously omitted chapters.

| Official primary chapter | New bounded chain | Boundary |
| --- | --- | --- |
| [*The Path to Opulent* (May 15, 2019)](https://magic.wizards.com/en/news/magic-story/war-spark-ravnica-path-opulent-2019-05-15) | Rat mourns Hekara → Kaya invites Rat and Teyo → the Orzhova journey → Domri's Gruul rescue → later Simic/Izzet encounter | Kaya *seeks* Orzhov help; her plan is not proof that the guild joined. Domri's in-scene role does not settle modern guild leadership. |
| [*Desperate Operatives* (May 29, 2019)](https://magic.wizards.com/en/news/magic-story/war-spark-ravnica-desperate-operatives-2019-05-29) | Kaya receives the four-guild assignment → seeks Emmara/Selesnya → Rat appeals to Gruul → Vraska returns to the Golgari → Vraska aids an evacuation | Rat's narration does not resolve Vraska's prior betrayal or establish her current office, and does not date other Ravnica war fronts. |

The source-registered, UTF-8-hashed input pack is `data/lore_research/pack_p5_war_spark_ravnica_2026-10-30.json`. The spec and deterministic output are `data/lore_research/war_spark_chapter_gap_spec_2026-11-01.json` and `data/lore_research/war_spark_chapter_gap_2026-11-01.json`.

**Measured additions:** 2 official source pages, 10 event nodes, 8 directly quoted ordering edges, 20 transitively proved **source-local** ordered pairs. All 8/8 short source excerpts were checked against the live Wizards pages on November 1; the CLI offers an optional `--live` recheck. CI replays exact spec/source hashes, quote digests, cycle checks, and both positive and negative event queries. It never has to fetch a live website to reproduce the committed report.

## Important unknowns preserved

- No edge joins the end of *The Path to Opulent* to the assignment at the start of *Desperate Operatives* merely because the web chapters were published in that order.
- Neither Vraska's return nor the Golgari evacuation is chronologically joined to the certified `Y:blackblade_shatters` or `W:bolas_imprisoned` nodes without a specific cited event identity or ordering link.
- The 2019 office accounts do not establish current Ravnica guild leadership, and nothing in this supplement resolves Bolas's final fate or the order of every War of the Spark mission.

Run:

```bash
python3 scripts/audit_war_spark_chapter_gap.py --check
python3 scripts/audit_war_spark_chapter_gap.py --compare DO:kaya_commissioned DO:golgari_rescue
python3 scripts/audit_war_spark_chapter_gap.py --compare DO:vraska_returns Y:blackblade_shatters
python3 -m unittest tests.test_war_spark_chapter_gap -q
```

This is post-certification research, not an assertion that the 137-task project or all War of the Spark history is finished. The 62 approved Grixis decks and all three unapproved lore pilots are untouched.
