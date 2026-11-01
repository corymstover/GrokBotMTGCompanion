# Foundation v2.93 — War of the Spark Azorius succession and card-lookup freshness

**2026-11-01 · PRELIMINARY_RESEARCH_NOT_OWNER_APPROVED · NOT_RELEASE_READY**

## Source-bounded history

Added strand `X` to the independently checked in-universe event ledger, using
only three already registered official Wizards *War of the Spark: Ravnica*
episodes and five previously registered, source-graded claims (`WR001`,
`WR003`, `WR008`, `WR013`, `WR014`). No new uncited graph claims were created.

| Attested sequence | Primary evidence and boundary |
| --- | --- |
| Isperia holds the Azorius office, then Vraska assassinates her | [Old Friends and New](https://magic.wizards.com/en/news/magic-story/war-spark-ravnica-old-friends-and-new-2019-05-08) identifies Isperia as guildmaster when assassinated; an office status precedes its holder's death, not a newly invented appointment date. |
| Dovin is subsequently called the **new** Azorius guildmaster | [Rallying the Reluctant](https://magic.wizards.com/en/news/magic-story/war-spark-ravnica-rallying-reluctant-2019-05-22) calls Isperia deceased and Dovin the new guildmaster at the war council. The exact moment of appointment is not supplied. |
| Dovin flees and Lavinia is identified as **acting** guildmaster | [Operation Desperation](https://magic.wizards.com/en/news/magic-story/war-spark-ravnica-operation-desperation-2019-06-05) directly ties Dovin's flight to Lavinia's temporary office; the text does not establish a permanent appointment. |

The four strict edges are claim-anchored and quote-backed. They create ten
ordered event pairs within the five-node chain. The separate Amonkhet/Eternals
strand remains unbridged: neither identical set release dates nor the
publication order of the two stories proves a relation between Lavinia's
acting office and the precise shutdown of the Planar Bridge. That comparison
must return `UNKNOWN` rather than invent an ordering.

The source-local corpus moves **15→16 strands**, **139→144 events**,
**112→116 strict edges**, **462→472 ordered pairs** (of **10,296** total), with
five non-ordering relations and eight legacy identity bridges unchanged.
Live verification found all **129 quotes on 21 official Wizards pages**.

## Card-lookup trust boundary

The October 30 release replay had already archived `oracle-cards-20261030210201.jsonl.gz`
and a 33,894-row drift report showing no indexed Oracle text, name, type,
identity, Commander legality or Game Changer mismatches. However, the
`mv_ask.card` route was still checking the October 29 reconciliation.

It now checks the October 30 report only if its schema, date, exact bulk
filename, complete indexed row count, parsed shard count and each comparison
category agree with the committed manifest. A missing field, partial parse,
unattributed changed entry, mismatched snapshot or missing report **fails
closed** to `STALE_ORACLE_VS_CURRENT_SNAPSHOT`. A changed individual card also
stays qualified. This verifies indexed fields **as of October 30**, not all
later printing metadata, current Oracle on November 1, card interactions,
published rulings or updated Commander rules. No Scryfall bulk or card shard
was silently rewritten.

## Bounded checks and unfinished gates

- `python3 scripts/source_event_sequences.py --live` — **PASS**, 129/129 quoted excerpts on 21 pages.
- `python3 -m unittest discover -s tests -p 'test_mv_ask*.py' -q` — **138 tests PASS** locally.
- `python3 -m unittest tests.test_source_event_sequences tests.test_chronology_global_pair_matrix -q` — includes independent all-pair chronology oracle.
- `python3 scripts/build_foundation_acceptance_packet.py` — **92** distinct representative Q&A cases, **NOT CERTIFIED**.
- Additional unit fixtures reject mismatched, incomplete and contradictory drift-report evidence.

The broader historical coverage tasks K099/K103, obscure Q&A K119/K121 and
release gate K133 remain **UNDER REVIEW / BLOCKED** as triaged. An in-scope
history improvement is not proof of a complete War of the Spark history.
Another official Scryfall bulk or new Comprehensive Rules release requires
release-time reconciliation. Do not reopen Phase 6 or touch the 62 locked
Grixis decklists, snapshot locks or owner decisions.
