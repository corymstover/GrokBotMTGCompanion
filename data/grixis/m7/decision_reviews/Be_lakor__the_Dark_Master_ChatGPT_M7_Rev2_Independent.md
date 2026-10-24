# Be'lakor, the Dark Master — ChatGPT independent M7 Rev2, eight swaps (2026-10-23)

**REVIEW CANDIDATE — NOT CORY-APPROVED — NOT CANONICAL — NEVER AUTO-LOCK.**
The five-swap GrokBot proposal in engineering PR #655 was an input, not a final judgment. Only the separately owner-approved exact 100-card raw SHA can become a canonical lock.

## Provenance
- Tracker #7, registry key `Be_lakor_the_Dark_Master` but tracker ID `Be_lakor__the_Dark_Master` (preserve alias; do not silently change).
- Historical approved baseline file `refinement/decklists/Be_lakor_the_Dark_Master_Approved_2026-10-13.txt`, raw SHA-256 `3abc951606a6db2b17ea2aceb471fc2ef4c55e2ef082d49d9140a83b2491155e`.
- GrokBot first-pass `data/grixis/m7/candidate_lists/Be_lakor__the_Dark_Master.txt`, raw `62a96b4f39584fa38947843bea352de923b29d7b266b57fce5918802a79b57bf`, five swaps.
- This exact 100-card Rev2: `data/grixis/m7/candidate_lists/Be_lakor__the_Dark_Master_ChatGPT_M7_Rev2_Eight_Approval_Candidate.txt`; **SHA-256 `2107f02e7a5303eef15b6720565d08dfe974b3d6fa57ea449440042cec1b4dd4`** (raw bytes with terminal newline).
- Source-bound selected Oracle/legality: `data/grixis/m6/oracle_snapshots/Be_lakor__the_Dark_Master_ChatGPT_M7_Rev2_Selected_20261023.json`. Card facts from frozen October 23 live Scryfall evidence in PR #655, plus canonical Ashnod October 23 live Scryfall receipts for City of Brass and Mana Confluence. This is not a new research-pipeline run.

## Eight independently selected one-for-one swaps

| Add | Cut | Strategic judgment |
| --- | --- | --- |
| Desecration Demon | Dream Devourer | At four mana, a 6/6 flying Demon delivers a six-power Lord trigger; foretell support was a 0-power Lord hit. Opponents may tap Desecration at combat by sacrificing a creature. |
| Kindred Dominance | Blasphemous Act | Keep our Demon board while removing opposing non-Demons. It costs seven mana, so Toxic Deluge and Rakdos the Showstopper remain cheaper emergency/ETB interaction. |
| Demonlord Belzenlok | Rakdos, Patron of Chaos | Immediate copyable Demon ETB hand refill instead of an opponent-choice end-step punisher. ETB exiles lands between qualifying cards; self-damage and a potentially short one-card outcome are real. |
| Shadowgrange Archfiend | Bloodthirster | GrokBot suggested Reaper from the Abyss. This independently discovered 8-power Demon has an *immediate* ETB: each opponent sacrifices its highest-power creature, and we gain life equal to the greatest power **among those sacrificed**, not the sum. One black pip is easier than Reaper's BBB. Loses Bloodthirster's extra-combat ceiling. |
| Cursed Mirror | Fellwar Stone | Preserve **seven static mana rocks**, correcting first-pass proposal's reduction to six. Mirror is a red source and can enter as a temporary copy of any creature, including a high-value Demon for Lord and ETB triggers. Costs three rather than two; if it copies a legend without a legend exception, the legend rule applies, and if it copies a creature its mana ability is temporarily absent. |
| Curse-Marred Demon | Balor | Four-mana 4/4 flying/trampling Demon gives a copyable ETB search for any card, followed by a **random** discard. The searched card is not guaranteed to survive; losing Balor's attack/death modes is genuine. Fewer mana, better ETB recursion, strong high-lift/new-card discovery. |
| City of Brass | Crumbling Necropolis | Untapped unconditional Grixis color access rather than always-tapped tri-land; the life damage when tapped matters in Prince of Chaos decks. |
| Mana Confluence | Foreboding Ruins | Untapped any-color access without reveal/dependent opening hand; paying life per colored activation matters. |

Other trials and challenges: Herald's Horn over Fellwar Stone improves future Demon costs and occasional draw but cuts a mana-producing source; Cursed Mirror preserves ramp and can copy ETBs. Reaper from the Abyss gives repeatable removal but demands `{B}{B}{B}`, needs a prior death at end step, and its mandatory target can expose our non-Demon support if no opposing legal creature remains. Shadowgrange is immediate and commander-aligned. Lord Xander over Lord of Change lowers reliable draw-three; Courtyard over Orchard reduces colored access to noncreature spells. Mandate of Abaddon costs less than Dominance but destroys our own low-power support Demons and reducers. Séance Board takes time to accumulate counters and cannot be relied on as turn-two mana. Demonic Covenant has a six-mana setup cost and possible self-sacrifice; it did not unseat Unholy Annex or the existing high-impact ETB engines. No marginal land replacements were added merely to inflate the count.

## Recount / power / source caveats
- **100 physical cards; 94 distinct names; basics Island ×3, Mountain ×2, Swamp ×4; 36 lands; 25 printed Demons including Be'lakor; seven static rocks** (Sol Ring, Arcane Signet, Rakdos Signet, three Talismans, Cursed Mirror). Dark Ritual is a one-shot, not a static rock.
- All 94 selected names have October 23 Scryfall legal/UBR Oracle receipts; no exception used. Five Game Changers: Ancient Tomb, Cyclonic Rift, Demonic Tutor, Fierce Guardianship, Vampiric Tutor. **Bracket 4 — Optimized**. Tags: **Demon Tribal / ETB Damage / Reanimator**.
- Commander Lord triggers on *other* Demon entries; the entering Demon deals damage equal to its current power. Reanimation, token and copy ETBs matter. Cursed Mirror becoming a Demon as it enters is an entry; copying a legend does not bypass the legend rule. Shadowgrange life gain uses the maximum sacrificed power, once.
- Existing kicked Rite of Replication on Be'lakor produces **25 finite Lord triggers** (five from original plus 20 from tokens) before entry-trigger doublers; stack life-loss Prince triggers beneath damage when possible. Prince can be doubled by applicable ETB-doublers too; evaluate the current board and life total. Not automatically infinite or automatically a win. No refreshed Spellbook full-list search or multiplayer gameplay/win-rate benchmark was run, so don't assert exhaustive combo coverage or measured superiority.
- Pass C formal owner-equivalent waiver is **non-independent**, not an independent third-model review. The first-pass scoped I/J certificates do not certify this altered candidate; the new focused tests verify raw bytes, Oracle, structure, and key interactions. Before owner approval, present exact complete list and verify final candidate again.
