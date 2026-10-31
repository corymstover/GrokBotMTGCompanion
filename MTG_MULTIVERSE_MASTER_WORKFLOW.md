# MTG Multiverse Companion — Master Workflow & Progress Checklist

**Version:** 2.73
**Checkpoint date:** 2026-10-31
**Repository:** [corymstover/GrokBotMTGCompanion](https://github.com/corymstover/GrokBotMTGCompanion)  
**Purpose:** Durable project roadmap and handoff document. Update this file after verified milestone work; do not treat historical figures as live counters.

**v2.53 OWNER DIRECTIVE — FOUNDATION FIRST (2026-10-30):** Cory has explicitly
deferred **all new lore-first deck construction, pilot refinement, deck approval
requests and deck-specific optimization** until the rest of the Multiverse
Companion knowledge foundation has been completed and independently certified
for its documented release scope. The execution order is **Phases 1/1B–5 →
Phase 7 → Phase 8 foundation certification → Phase 6 deckbuilding**. Phase 6
retains its historical name and checklist so previous work is never lost, but
is **PARKED / POST-FOUNDATION**, not an active gate or next-step priority.
Existing Pilots 1–3 are preserved as **UNAPPROVED, historical drafts**; their
approval is not a prerequisite for the knowledge-foundation release. Focus
now on source-graded chronology, comprehensive plane/character/faction and
cross-plane histories, graph quality, card/printing/rules lookups, difficult
Q&A, reproducibility, and an honest coverage/limitation audit. A finite
foundation release may document inherently unresolved canon and future
maintenance; it must never claim exhaustive knowledge of all MTG history.
The 62 approved Grixis decks, their hashes and all owner gates remain intact.
Only a new explicit request from Cory can override the Phase 6 hold.

**v2.73 official source-cache provenance replay and complete checklist triage (2026-10-31):**
The complete **660-URL** official Wizards story/feature/format source inventory
was rebuilt in the ignored local cache and passed the independent strict
source-URL, nonempty body, minimum-length and no-collision checks. Of these,
**652 recovered extractions have the exact historical SHA-256** from the
October 29 provenance archive; **eight changed extracts are quarantined**
for source review (seven older Planeswalker's Guide/feature pages each add ten
extracted words; the Commander format page changed its extract hash without
changing word count). None is silently regraded as lore evidence. The official
**September 25, 2026 Comprehensive Rules** text and existing pinned Scryfall
Default Cards/Rulings bulk restored independent quote verification:
**2,726 quotations across 27 documentation pages**, with **zero unexplained
failures**. The replay stores URLs, sizes, hashes and diagnoses, not
copyrighted article bodies; portable CI validates the report without source
downloads, and a full local cache invokes all 660 SHA checks. The complete
Wizards citation audit also refreshed **920 distinct URLs** against the official
sitemap or direct redirects/archival records, while checking **776 distinct
Comprehensive Rules references**, with **zero citation-audit problems**.
The complete
137-task triage now distinguishes Completed, Under review, Blocked and Not
started; it explicitly parks all ten Phase 6 deck tasks. Strict story-source
recovery and truthful four-state checkpoint maintenance are now checked as
engineering tasks: **88/137 checked, 49 open**, including parked and
continuing work. **Foundation release remains NOT_RELEASE_READY** due to
independently unresolved research, qualified release gates and exact-release
CI. Cory's conditional automatic acceptance remains recorded but not yet
effective; no new decks or protected approval records were changed. See
`research/STORY_CACHE_RECOVERY_2026-10-31.md` and
`research/FULL_CHECKLIST_TRIAGE_2026-10-31.md`.

**v2.72 pinned historical Scryfall recovery and printing/art replay (2026-10-31):**
The **exact** previously unavailable `default-cards-20261028090549.jsonl.gz`
source was recovered from its dated Scryfall URL and independently matched its
recorded SHA-256 `c7c6d738…1e2` (**80,216,061 compressed bytes**). Rebuilding
`printing_lore.sqlite3`, all **105 printing shards** and the full export manifest
from that original source produced **byte-for-byte identical** committed files:
**119,509 printing IDs, 1,062 set codes and 107,700 English-paper printings**.
The original Grixis October 15–16 Oracle, Default Cards and Rulings files were
also recovered and each matched the existing `snap-20261016` lock; the lock and
all 62 approved decks are unchanged. The separate October 29 Companion Oracle,
Default Cards and Rulings archive passed its full three-file size, SHA-256 and
JSONL record-count verification. Replay against its exact Default Cards bulk
independently matched metadata for **570 officially labeled story-art printings,
six previously visually reviewed art pairs and 20 recorded same-illustration
printings**; seven unresolved story image labels remain unresolved. It did not
repeat any human visual comparisons or infer new event scenes. A missing-source
fallback previously concealed stale derived evidence: rebuilding added seven
claim-card pairs and updated Alara shard/plane card-name anchors, then rebuilt
the cited graph. `scripts/replay_pinned_scryfall.py` generates the reproducible
evidence at `data/scryfall_snapshots/historical_bulk_replay_2026-10-31.json`,
and its portable check preserves immutable sources without committing bulk
files. The source-recovery, historical index audit and snapshot-byte metadata
boxes are now mechanically complete: **86/137 checked**, with **51 still open**
across all phases (including deliberately deferred Phase 6). The foundation is
**NOT_RELEASE_READY** because cited historical coverage, qualified release
gates, rule freshness, independent release CI and remaining research all still
require work. Cory's October 31 automatic foundation-only acceptance is
recorded as **conditional, not yet effective**; no second approval prompt is
needed once the actual gates pass. Phase 6 remains parked.

**v2.71 Phase 4 source-corroborated cross-ledger chronology bridges (2026-10-31):**
Seven explicit `SAME_EVENT` identity links now join the formerly isolated
Packs A–C legacy timeline and the separate Thran/Rath source-local strand
**only where both ledgers cite the same official Wizards historical passage**:
the original Phyrexian creator's death, Dyfed bringing Yawgmoth, closure
of the Thran-Phyrexia portal, Thran defeat, the Sisay rescue on Rath,
the Weatherlight crew's arrival on Mercadia, and the Rathi overlay.
The bridge links are **not** BEFORE edges and are one-to-one; a combined
proof must also traverse an independently cited strict BEFORE edge before
answering a mixed-ledger order. The composite audit rejects cycles, an
equivalent event is answered `SAME_EVENT` rather than as earlier/later,
and unrelated or unbridged accounts remain `UNKNOWN`. All **67 excerpts,
including seven new bridge quotations, passed live validation** against
seven official Wizards pages. Three added positive/identity/unknown Q&A
cases bring the preliminary foundation packet to **49 questions**. The two
chronology universes retain **56 legacy events** and **74 source-local
events** with **seven explicit shared event identities**—no false
global-completion fraction is reported. Other lore totals stay **1,259
claims, 5,290 nodes, 8,473 edges**; checklist **83/137** and readiness
**NOT_RELEASE_READY**. The missing historical Scryfall source, complete
history and owner decisions remain blockers. All 62 protected decks and
Phase 6 pilots remain unchanged. See
`research/PHASE4_SOURCE_LOCAL_EVENT_SEQUENCES_2026-10-30.md`.

**v2.70 Phase 4 Thran, Old Phyrexia and Serra's Realm chronology (2026-10-31):**
Added **23 source-local historical events, 20 strict BEFORE relations and one
non-ordering overlap** from the official Wizards 2008 *Known Multiverse*
retrospective. This ties the Thran decline, Yawgmoth's rise, the closing of the
Phyrexian portal, his long-term invasion plan, Rath, and the Weatherlight's
first-Invasion-era actions into one bounded proof chain. A second qualified
strand follows Urza's refuge and the eventual powerstone collapse of Serra's
Realm. The shared source **does not state whether Old Phyrexia's soul-bomb
devastation preceded Yawgmoth's destruction**, or whether Radiant's
administration ended before the realm's powerstone extraction; both stay
`UNKNOWN`. The two outcomes are not silently sorted by paragraph position.
All **60 source-relationship excerpts from seven Wizards pages passed live
verification**. The independent source-local ledger now contains **eight
strands, 74 events, 57 strict edges, three non-ordering relations and
180/2,701 ordered pairs** (separate from the unchanged 56-event Packs A–C
legacy ledger). Four additional positive/negative chronology questions expand
the Phase 8 foundation packet to **46 cases**. Engineering remains **83/137**,
the foundation is **NOT_RELEASE_READY**, and no owner decision or missing
pinned Scryfall source is magically resolved. The 62 approved decks remain
untouched; Phase 6 stays deferred. Details in
`research/PHASE4_SOURCE_LOCAL_EVENT_SEQUENCES_2026-10-30.md`.

**v2.69 Phase 4 Muraganda and Meditation Realm source-local chronology (2026-10-31):**
Expanded the qualified source-local event ledger with **20 events and 15
source-quoted relations**, using the existing v2.68 registered Wizards
references: *Planeswalker's Guide to Aetherdrift, Part 2* (Muraganda) and
*Chronicle of Bolas: The Unwritten Now* (Ugin's early Meditation Realm
memory). All **39 chronology excerpts from six official Wizards pages passed
live quotation verification**. The ledger now has **six separately scoped
strands, 51 events, 37 strict edges, two non-ordering relations and 101/1,275
comparable pairs**. The Muraganda collapse versus moon-shattering, the
overlapping moon-strike decline and survivor cultures, and Bolas's removal
versus Ugin's restoration remain explicitly unproven where no strict edge
exists. This does not import the later post-*Tarkir: Dragonstorm* Realm
status into Ugin's remembered early story. The legacy 56-event ledger stays
separate. Four new positive/negative direct chronology Q&A cases expand the
Phase 8 packet to **42 representative questions**. Other foundation
coverage stays at **1,259 graded claims, 5,290 nodes, 8,473 edges** and
**83/137** checked items; readiness is **NOT_RELEASE_READY**. The missing
pinned Scryfall bulk, incomplete lore and owner acceptance remain open.
All 62 approved decks and the three unapproved lore pilots are untouched;
Phase 6 stays deferred. See
`research/PHASE4_SOURCE_LOCAL_EVENT_SEQUENCES_2026-10-30.md`.

**v2.68 Phase 5 last four thin-plane dossier pass (2026-10-31):**
Added **13** narrowly scoped and live-excerpt-checked direct historical
relations from **eight** official Wizards pages or source-context references:
**Bablovia** (1→5), **Meditation Realm** (3→5), **Muraganda** (1→5) and
**Skalla** (2→5). The Bablovia batch carries explicit
`ALTERNATE_CONTINUITY` grades and the Wizards silver-border Un-set versus
black-border distinction; the inherited `SSX020` grade from the older
Unstable story is disclosed as a provenance debt, **not silently
reclassified without the original source-cache audit**. Other histories
distinguish Madaran-era Bolas meetings and early Ugin contemplation from
the realm's later fate; Muraganda's ancient collapse, shattered moons and
survivor societies from current politics; and Vivien's remembered Skalla
ecology and Arkbow legacy from surviving living life. No cross-source AR
dates or exhaustive outcomes are invented. All 33 registered plane dossiers
now reach at least five direct cited claims (**0 thin**), but **0 complete
histories are certified**. Graph: **1,259 graded claims, 5,290 nodes,
8,473 edges**, with **640/640** registered Character/Faction nodes incident
to a cited claim. The Phase 8 foundation review packet has **38 unique
Q&A cases** and remains explicitly preliminary. Source-safe append mode
accounts for **1,259 claims and 4,118 name anchors** without changing
historical printing/art tiers while the pinned Scryfall bulk is absent.
The engineering checklist remains **83/137**, readiness is
**NOT_RELEASE_READY**, owner acceptance is ungranted, and the three
unapproved lore pilots and 62 protected Grixis decks are unchanged.
See `research/PHASE5_LAST_FOUR_THIN_PLANES_2026-10-31.md`.

**v2.67 Phase 5 four further plane histories (2026-10-31):**
Twelve additional direct, source-quoted `CANON_CONFIRMED` incidents and
geography facts from seven Wizards pages enrich **Fiora** (4→7),
**Kaldheim** (4→7), **Lorwyn-Shadowmoor** (3→6) and **Thunder Junction**
(2→5). The record distinguishes Marchesa's partisan proclamation from
proof of legitimacy; the earlier, roughly 300-year Great Aurora cycle
from modern adjacent aurora boundaries; and the 2024 Thunder Junction
heist setup from its outcome. Drakestown's attackers, the vault's makers
and later world-state claims remain unresolved. All seven pages passed
the live quotation audit. The thin-plane count is **4/33**, not four
complete histories. Graph: **1,246 claims, 5,259 nodes, 8,421 edges**;
**633/633** registered people/factions have at least one directly
cited relation. The packet has **34 distinct qualified Q&A examples**;
the master checklist remains **83/137**, release is **NOT_RELEASE_READY**,
and owner certification, Phase 6 hold, three unapproved pilots and all
62 approved Grixis decks are unchanged. The snapshot-free append-only
anchor pass accounts for 1,246 claims and 4,109 card-name anchors without
replaying unavailable frozen Scryfall bulk. See
`research/PHASE5_FOUR_MORE_PLANE_HISTORIES_2026-10-31.md`.

**v2.66 Phase 5 history and Q&A follow-through (2026-10-31):**
Added **12** direct `CANON_CONFIRMED` claims from five official Wizards pages
covering Arcavios (2→5), Vryn (2→5), Serra's Realm (2→5) and Regatha
(2→5). Unknown Arcavios parent-plane identities, Vryn mage-ring origin
and final factional outcome, relative university age, and Serra's Realm's
historical destruction are explicitly qualified. The registered thin-plane
queue declines from **12 to 8**, not to zero complete histories.
Graph: **1,234 claims, 5,232 nodes, 8,372 edges**; **633/633**
registered people and factions have a direct claim, without implying
exhaustive biographies. The foundation review packet has **30 unique**
questions after correcting the duplicated New Capenna review-case ID.
The engineering checklist remains **83/137** and release readiness
**NOT_RELEASE_READY**; Phase 6 and all protected decks remain parked.
The new non-set pack was appended to claim-card anchors (all 1,234 claims
accounted for, 4,104 anchors) using the existing snapshot-free append
protocol. Earlier printing/art tiers were preserved; full pinned-bulk
replay remains a source-level gate. See
`research/PHASE5_FOUR_PLANE_HISTORIES_2026-10-31.md`.

**v2.65 Phase 5 thin-plane history depth (2026-10-31):**
Added **11** direct, source-quoted and `CANON_CONFIRMED` geographic/historical
claims across four previously thin registered planes: **Argentum** (1→5),
**Eldraine** (3→5), **Ikoria** (4→6), and **New Capenna** (2→5). The six
official Wizards overview/guide sources explicitly distinguish the human
Realm from all of Eldraine, Old Capenna's **unidentified** invaders from
later attribution, mobile Ikorian sanctuaries from permanent fixed cities,
and Argentum/Mirrodin's historical names from current world politics.
There are now **12** registered plane dossiers with fewer than five direct
claims (down from 16), but **no complete plane history is asserted**.
Graph: **1,222 claims, 5,209 nodes, 8,324 edges**; all **630/630**
registered people/factions have some directly cited relation, including
one newly named historical group in Old Capenna and the already registered
Old Capenna archangels. The foundation review
packet now exercises **26 qualified Q&A examples**. This is bounded,
preliminary history enrichment, not complete lore research, owner approval,
foundation certification or permission to restart deckbuilding. The
engineering checklist remains **83/137**. See
`research/PHASE5_THIN_PLANE_SOURCE_PASS_2026-10-31.md`.

**v2.64 Phase 5/7 registered character and faction evidence gaps (2026-10-31):**
Five already registered nodes with no directly incident cited relation now
have source-graded historical relationships in the new preliminary
`pack_p5_isolated_entity_history_2026-10-31.json`: **Eric and Hazel
Kenrith**, **Lyra Dawnbringer**, **Valentin**, and **the Cabaretti**.
The supporting sources are original Wizards Eldraine, Dominaria,
Strixhaven and New Capenna guides/stories, and all claims have explicit
date/currentness boundaries. The 2019 official spelling **Eric** is
preserved; a later **Erec** spelling is **not** silently reconciled. The
derived graph has **1,211 claims, 5,186 nodes, 8,279 edges**. Exactly
**629/629 registered characters and factions** now have at least one
direct cited graph relation (483 characters, 146 factions including the
Angels of Serra). This **is not** a census of all Magic characters or
proof of complete histories; five short claims do not resolve narrative
gaps, chronology, contested identities or current leadership. The
foundation acceptance packet now exercises **22** representative questions,
including all five repaired histories. The original historical snapshot
and qualified gates stay intact; this does **not** certify the foundation
or resume Phase 6. The checklist remains **83/137**. See
`research/PHASE5_CHARACTER_FACTION_HISTORY_LOOKUP_2026-10-30.md`.

**v2.63 Phase 4 New Phyrexia source-local chronology (2026-10-31):**
Extended the separately qualified Phase 4 source-local event ledger with
**seven** existing claim-backed early-Mirrodin/New Phyrexia event labels and
**six** source-quoted strict BEFORE edges from Wizards' official
[New Phyrexia plane history](https://magic.wizards.com/en/story/new-phyrexia-plane).
The evidence tracks Karn bringing the oil, underground corruption, the
active conquest, Mirran resistance and the later restoration of Karn;
its two branching paths **do not** invent whether the Mirran forces were
overwhelmed before or after Venser's sacrifice. The ledger now contains
**4 separate strands, 31 events, 23 strict edges, one non-ordering overlap,
and 52/465 ordered pairs**; the 56-event legacy ledger remains separate.
The normal `mv_ask.py ask` route can retrieve four-step cited proof and
returns `UNKNOWN` for unsupported comparisons. The deterministic
knowledge-only acceptance packet now checks **17 representative Q&A cases**,
including a new positive and negative chronology example. This is a bounded
source-evidence improvement, **not** complete L244 chronology, post-March of
the Machine current politics, owner acceptance or foundation certification.
The **83/137** checked engineering items are unchanged. No deckbuilding.

**v2.62 Phase 7 published-rulings and keyword-rules Q&A (2026-10-30):**
`scripts/ask_rules_evidence.py` connects the standard `mv_ask.py ask`
interface to existing dated Scryfall-published card rulings and the
source-hashed official **2026-09-25** Comprehensive Rules 701/702 keyword
excerpt. It answers direct card rulings, card keyword mechanics, named
keyword definitions, and **two-card published-ruling interactions**, with
exact rule numbers and source URLs. For example, the committed **2021-06-18**
Urza's Saga ruling explicitly says it does not interact with Urza's Tower;
Serra Angel's Flying/Vigilance keywords cite **702.9/702.20**. All answers
remain **QUALIFIED** because the card ruling shard dates to **2026-10-15**,
not the current Oracle snapshot, and this is **not game simulation** or
proof that uncited interactions do not exist. Seven focused regressions
cover positive/negative routes and preserve lore, set and Commander routing.
The reproducible knowledge-only foundation acceptance packet now exercises
**15** cited Q&A cases, including Alpha counts, Black Lotus printing history
and Urza's Saga/Tower. The Phase 8 dry-run preserves its two engineering
blockers (unmodelled interactions and qualified historical atlas provenance),
so neither rules completeness nor foundation certification is asserted.
**83/137** checklist items are now verified; deckbuilding stays parked.

**v2.61 Phase 7 bounded set and printing questions (2026-10-30):**
`scripts/mv_ask.py ask` now routes explicit natural-language set/printing
questions to `scripts/ask_set_atlas.py` and the fully committed, frozen
Phase 1B historical shards. Supported answers distinguish **1,062 catalogued
set codes** across qualified categories, including **136** source-reviewed
historical regular/mainline codes (not a universal official expansion total);
give complete or classified debut/reprint set card lists; distinguish stable
Oracle identities from printing IDs; and report a card's dated printing
history and earliest recorded set(s). Example: Alpha's **290** identities vs.
**295** English-paper printing records; Black Lotus has **13** eligible
printing records across **8** set codes in the snapshot, earliest Alpha
(1993-08-05). All results are **QUALIFIED** with the **2026-10-29** cutoff,
source file links, paper/language scope, original bulk-source absence, and
explicit separation of product dates from in-universe time. Nine regression
tests cover category policy, full lists, debut/reprint filtering, ambiguous
sources, unknowns and existing rule/lore routes. This closes the *bounded*
Phase 7 set-answering checklist capability, **not** the Phase 1B source-bulk
gap, live freshness, comprehensive Q&A, or foundation certification.
Phase 6 remains parked.

**v2.60 Phase 8 foundation acceptance evidence and blocker reconciliation (2026-10-30):**
`scripts/build_foundation_acceptance_packet.py` now reproducibly assembles
the source-graded **knowledge-only** review surface at
`data/release/foundation_acceptance_packet_2026-10-30.json` and
`research/FOUNDATION_ACCEPTANCE_PACKET_2026-10-30.md`. It records two
**separate, non-additive** partial chronological ledgers; 33 registered
plane dossiers, 16 thin; 623/628 character/faction nodes with direct cited
claims; two strictly non-temporal graph-navigation examples; and 12 bounded
end-to-end lore/chronology/continuity/Commander-rules Q&A cases with source
references, flags and response digests. This is **NOT** owner review or final
certification, and the packet explicitly names unverified scope and source
gaps. The Phase 8 dry-run no longer falsely calls the already scheduled
weekly source monitor unscheduled, or the updated progress tracker stale.
`Progress Tracker.md` now separately triages all 14 first-release/Phase 8
gates as Completed / Under review / Blocked / Not started with typed
blockers, distinct from the 137-item engineering checklist. The packet
itself awaits exact-release CI and owner scope review; two genuine remaining
technical blockers (lookup/rules and qualified Phase 1B limits), plus
missing historical sources, are **not** declared solved. Deckbuilding stays
parked and the checklist remains **81/137**.

**v2.59 Phase 5/7 partial character and faction history retrieval (2026-10-30):**
The normal `mv_ask.py ask` route now surfaces direct source-graded graph claims
for registered Characters and Factions when asked for their history or lore.
The unchanged graph registers **483 characters and 145 factions**; **623 of
628** have at least one directly incident cited claim. Example distinct
direct-claim counts: Nicol Bolas 51, Gatewatch 22, Izzet League 5. Replies
group multi-edge claims only once and carry original grade, limitations,
official URLs, relations and quoted dates when available. Every nonempty
answer remains **QUALIFIED, partial and explicitly unordered**. The five
registered entities without direct claims are not declared noncanonical.
The new exhaustive-on-registered-entities regression suite checks all 628
nodes against graph incidence and source provenance. No new facts, date
inferences or deck approvals were made. **Comprehensive histories and
foundation certification remain open; the checklist count is unchanged.**
See `research/PHASE5_CHARACTER_FACTION_HISTORY_LOOKUP_2026-10-30.md`.

**v2.58 Phase 5 source-graded contextual history retrieval (2026-10-30):**
Reused **53 existing official-story claims** from four registered claim
packs as a separately labeled *contextual* layer in plane history queries:
Eldraine 10, Arcavios 16, New Capenna 15, Lorwyn–Shadowmoor 12.
These are **not 53 new claims**, not direct plane-node edges, and not
evidence of a complete plane history. All source grades, quoted evidence,
URLs, relations and limitations remain attached. Excluded off-plane scenes,
overlaps with existing direct claims and uncertain geographic cases. An
official Wizards statement that Strixhaven is on Arcavios passed a live
source check. Regenerated dossier counts: **33 planes, 183 direct edges,
16 thin by direct-claim threshold, four planes with 53 contextual claims**.
Main `mv_ask` plane-history responses and command-line history lookup keep
the two evidence layers separate, retaining QUALIFIED and unknown timeline
status. Master Workflow, tracker, regression tests and CI are updated.
Full historical coverage and foundation certification remain OPEN; Phase 6
stays parked. See `research/PHASE5_CURATED_ON_PLANE_CONTEXT_2026-10-30.md`.

**v2.57 Phase 7 natural-language chronology route (2026-10-30):**
`scripts/mv_ask.py ask` now understands bounded two-event questions such as
“Which happened first, Konda imprisons a part or breaks the barrier?” and
“Did War of Cinders happen before Wildsear appears?” It delegates to the
already verified v2.56 source-local and legacy chronology proof layers,
returns exact event IDs, cited relationships, links and QUALIFIED results,
and never upgrades an in-world legend or a DURING relation to objective
historical BEFORE. Cross-plane/cross-ledger order returns UNKNOWN; duplicate
label fragments return NOT_FOUND rather than guessing. Nine dedicated Q&A
regressions preserve earlier unrelated question routes. **This answers a
bounded supported class of comparisons, not the open requirement for all
obscure chronology questions or all MTG history.** No deck work was done.

**v2.56 Phase 4 source-local chronological evidence (2026-10-30):** New
deterministic, quote-gated event sequences supplement the untouched Packs
A–C 56-event chronology. Kamigawa's Kami War/Imperial origins (7 events),
Bloomburrow Valley's **narrated legend** (9 events), and Duskmourn's
House/Marina Ascension (8 events) yield **24 source-local nodes**, **17
strict BEFORE edges**, **1 qualified during-war relation** and **37 of 276
strictly ordered event pairs**. All 18 relationship quotes were matched
to three live Wizards pages. The shared chronology command now returns
cited proof or UNKNOWN across these strands and retains uncertainty about
cross-plane dates and missing internal links. This is a distinct event set:
its pair counts must not be added to the legacy 177/3,074 figure. L244,
comprehensive history and final certification remain OPEN; Phase 6 remains
deferred. See `research/PHASE4_SOURCE_LOCAL_EVENT_SEQUENCES_2026-10-30.md`.

**v2.54 Phase 4/5 plane-history expansion (2026-10-30):** Added two
source-conservative historical packs with **20 new CANON_CONFIRMED claims**:
12 on Kamigawa's two realms, the Kami War, Konda, Kyodai, the realm merger,
Imperial origins and Saiba Futurists; eight on Mirrodin's corruption and the
early New Phyrexian conquest, resistance and rival praetor factions. All
short excerpts and two quoted relative time phrases were checked **live**
against three Wizards primary pages; earlier source identities were reused.
The **1,200 years ago** reference is relative to the Neon Dynasty 2022
guide's narrative context, never a converted AR date. This early New
Phyrexia profile does **not** establish its present-day ruler after *March
of the Machine*. The regenerated graph has **1,181 claims**; 33 official
plane dossiers remain explicitly partial, with thin dossiers reduced
**20 → 18**. Verified histories and tests are preliminary research, not
deck approval or a completed history census. Phase 6 remains DEFERRED.
See `research/PHASE5_KAMIGAWA_NEW_PHYREXIA_HISTORIES_2026-10-30.md`.

**v2.55 Phase 5 legendary-origin and horror-plane histories (2026-10-30):**
Added **25 cited claims** from the official 2024 guides for *Bloomburrow*
and *Duskmourn*. Valley's Season of Chaos, legendary Order of the Holly
Leaf, War of Cinders, Lily's Seed Flame and the history of weaving are
**CANON_IMPLIED**, not promoted to unquestionable history, because the
guide explicitly frames the Order as legend and tells the past through a
resident's account. Valley's council governance is explicitly regional,
not a claim about every polity on Bloomburrow. The Duskmourn records
document the forgotten original plane, possible lost advanced culture
(IMPLIED), its old realms, Marina's involvement, expanding House and
recurring Valgavoth cycles. All three reused Wizards guide identities
and all 25 excerpts passed **live official-source checks**. The two
planes now clear the arbitrary five-direct-claim *thin* threshold but
neither has comprehensive history. The only new time metadata is the
verbatim **two generations** in Valley's narrated War of Cinders;
no AR year or link to other planes' calendars was fabricated. Source
provenance, Q&A qualification and the Phase 6 hold are retained.
See `research/PHASE5_BLOOMBURROW_DUSKMOURN_ORIGINS_2026-10-30.md`.

**v2.52 Phase 7 plane-history Q&A (2026-10-30):** The main
`scripts/mv_ask.py ask` route now answers plain-language plane-history
questions with the generated Phase 5 dossiers. Each response groups multiple
relations under their original cited claim, preserves claim grades and source
URLs, and is always **QUALIFIED** with explicit incomplete-history and
unknown-total-chronology flags. Unknown plane names fall back to regular
lookup without being presented as nonexistent. Dedicated regression tests
cover Alara, Theros, Old Phyrexia, unknown names and characters.
**Audit correction:** v2.51's prose undercounted Theros's directly incident
claims: the exact generated dossier contains **6, not 5** (prior 3 plus
`THP001`, `THP002` and `THP010`). The generated counts/graph were correct;
the historical note and report below are corrected. No source grade or
chronology claim changed. See
`research/PHASE7_PLANE_HISTORY_QA_2026-10-30.md`.

**v2.51 Phase 5 Theros history expansion (2026-10-30):** Ten more concise
claims from the official [Theros plane profile](https://magic.wizards.com/en/story/theros-plane)
were independently verified verbatim against Wizards' live page. The new
`P5-THEROS` pack covers the gods' broad influence, Meletis/Akros/Setessa as
major poleis, minotaur/giant/kraken/siren threats, civic ideals and defensive
outposts. It preserves existing Theros claims, including `TS037`, and reuses
the precise official source identity `ths_plane`. Theros's directly incident
claims rose **3 → 6**; thin plane dossiers now **20/33** (down from 22 before
Alara and Theros). Current graph: **5,094 nodes / 8,063 edges / 1,161 claims**,
and 160 direct plane-claim edge incidences. No inferred chronology, mythic
hierarchy, or complete-polis census was asserted. This remains
**PRELIMINARY_RESEARCH_NOT_OWNER_APPROVED**. See
`research/PHASE5_THEROS_PLANE_PROFILE_2026-10-30.md`.

**v2.50 Phase 5 Alara history expansion (2026-10-30):** The official
[Alara plane primer](https://magic.wizards.com/en/story/alara-plane) was
independently read and all ten new short excerpts verified against the live
Wizards page. New Pack `P5-ALARA` records the five shards, their three-color
isolation, reunion into a five-color plane, inter-shard conflicts, and the
specific documented motives of Esper, Grixis undead, Jund, Naya and Bant.
The earlier Bolas role `UP001` is **not duplicated or overridden**. Alara's
direct official claims rose **from 1 to 5**, and thin plane-history dossiers
fell **from 22 to 21**. Current graph: **5,072 nodes / 8,019 edges / 1,151
claims**; 33 plane dossiers and 155 direct plane-claim edge incidences.
No unstated chronological relation or AR date was inserted. All new facts
are preliminary, source-graded research, **not** owner approval or
certification. See `research/PHASE5_ALARA_SHARDS_PROFILE_2026-10-30.md`.

**v2.49 Phase 5 queryable plane histories (2026-10-30):** The direct-claim
plane priority counter now has a complementary, reproducible *reading and
querying* layer. `scripts/build_plane_history_dossiers.py` compiles the
current graph's **33 registered planes and 147 direct claim-edge incidences**
into official-citation-backed, grade-preserving partial histories, and
`scripts/query_plane_history.py Dominaria` (or `Phyrexia --json`) retrieves
their claim summaries, participants, sources, limitations and any explicitly
quoted dates. **22/33 planes have fewer than five direct claims**, so this is
not comprehensive history or an inventory of every Magic plane. No era label,
publication date or card-set date becomes a new chronological ordering.
`--check` and tests enforce exact derivation from the current graph.
See `research/PHASE5_QUERYABLE_PLANE_HISTORIES_2026-10-30.md`.

**v2.48 Phase 4/5 C5 official invasion-outcome evidence (2026-10-30):**
Two new **CANON_CONFIRMED editorial-source attributions** were verified live,
with short direct excerpts, against Wizards' 2008 *The Known Mutliverse* recap:
the Weatherlight crew used Legacy artifacts to destroy Yawgmoth on Dominaria,
and an unnamed planeswalker group decimated Old Phyrexia with soul bombs. The
source names no individual soul-bomb attackers and **does not order the two
outcomes against each other**. Other official attributions to Gerrard/Karn/Urza
are retained, not overridden. Source-graded Pack C5 adds two claims to the
graph (**1,141 total**); the story inventory and live Progress Tracker now
derive from current claim packs rather than the archived Batch 14 recount.
The claim-card anchor sidecar now counts all 1,141 claims; its snapshot-free,
append-only update adds one **named-participant** Yawgmoth link, not a claim
that the printed card depicts the invasion or a new inferred set attribution.
Historical 4,050 card-anchor rows and their tiers were preserved unchanged.
L244 still awaits a genuinely quoted ordering. The pack is preliminary and
owner-unapproved. See `research/PACK_C5_PHYREXIAN_INVASION_OUTCOME_2026-10-30.md`.

**v2.47 Phase 8 source-change monitoring (2026-10-30):** A read-only weekly
GitHub Actions monitor now checks the official Wizards Magic Story listing,
advertised Scryfall default/oracle/rulings bulk timestamps, and official Wizards
rules/Commander pages. It compares against the committed October 30 source
inventory, a known official Comprehensive Rules PDF link and the SHA-pinned
active October 29 Scryfall manifest. It emits a review-only artifact; it does
not auto-download bulk, alter approvals, amend historic snapshots, or pretend
that a dynamic page ETag represents a real rules/ban update. In the first
live probe there were **zero new story links on the current listing page** and
three **newer Scryfall bulk metadata** signals; the official Comprehensive
Rules PDF link was unchanged. The Commander-page ETag varied even during the
same observation session and is informational only. Limited page coverage and
rules-announcement interpretation remain open. See
`research/PHASE8_OFFICIAL_SOURCE_UPDATE_WATCH_2026-10-30.md`.

**v2.46 Phase 2/3/7 printing-specific card representation checkpoint (2026-10-30):**
Graph `CardRepresentation` nodes now use *exact Scryfall printing UUIDs*, not
ambiguous title slugs. The committed Wizards story-page image-label crosswalk
provides **560 unique printing identities / 570 official image-page associations**;
each independently resolves to the **same printing UUID, set, number, card name and
Oracle UUID** in the historical Phase 1B index. Seven unresolved image labels are
excluded, not forced. New graph: **5,040 nodes / 7,963 edges**, 1,139 unchanged
claims, zero builder errors or prefix mismatches. The new `printing SET NUMBER`
query exposes the exact printing and relevant official art-page link, explicitly
labelled navigation rather than evidence that the card depicts a story event.
This establishes stable *printing-specific IDs for represented printings*, not a
claim that all 119,701 printings are lore mapped, that exact cross-snapshot ID
parity holds for the entire catalog, or that all art depicts canon moments.
See `research/PHASE3_PRINTING_IDENTITY_BRIDGE_2026-10-30.md`.

**v2.45 graph display-name integrity (2026-10-30):** The graph now records all
source-pack name variants attached to the *same stable entity ID* (36 nodes,
including the 22 cross-pack examples flagged by the entity audit). Search can
retrieve those variants and explicitly disambiguate by entity type; no unrelated
entities are merged by similar spelling. Existing node IDs, canonical first names,
edge counts, grades, and source links remain stable. Ambiguous names still require
type or ID selection. The 16 orphan nodes and six candidate *different-ID* aliases
remain open rather than being silently joined or deleted.

**v2.44 Phase 2–8 research/navigation checkpoint (2026-10-30):**
`scripts/query_lore_chronology.py` gives user-facing sourced BEFORE/AFTER/UNKNOWN
comparisons from the *existing* official-story chronology (56 events, 177/3,074
comparable pairs, 13 disconnected components). Proofs retain official source quotes,
and the 2,897 unorderable pairs remain unknown, not inferred from publication dates.
`scripts/build_plane_history_priorities.py` generates a source-conservative Phase 5
coverage queue: 33 currently registered Plane nodes, all with at least one direct
claim edge but **22 with fewer than five**; it is NOT an inventory of every plane or
an assertion of exhaustively researched histories. The same report preserves all three
Phase 6 pilot decks as **UNAPPROVED** with lore tier breakdowns. These scripts have
dedicated CI and regression tests; further primary-source chronology, participant and
mechanical research remains open. See
`research/PHASE5_CHRONOLOGY_AND_PLANE_COVERAGE_2026-10-30.md`.

**v2.43 post-overnight integrity checkpoint (2026-10-30):** The Phase 7 Q&A layer now marks
questions about *current* leaders as QUALIFIED unless independently established in canon;
the most recently cited leader is not guaranteed to be the present incumbent. A cited
death of that leader is surfaced, and events confined to rewritten/original timelines
(such as Ugin's death at Bolas's hands) are qualified. The graph separates Urza and
Mishra as the two subjects of C023 and restores five *unique normalized-title* legacy
artifact index bridges without guessing identity by similarity. Current graph:
**4,231 nodes / 6,833 edges / 1,139 cited claims / 126 curated bridges**, 14 literal
objects; 16 orphan nodes and 22 cross-pack display-name variants remain explicitly
unresolved. Exact pinned Scryfall archive replay now fails with a clear missing-file
message and hash reference when the bulk is absent; saved qualified reports are not
relabelled as independently replayed. `Progress Tracker.md` contains a generated current
checkpoint; the older historical metrics remain for provenance. **No deck, lore-pack,
Grixis, owner-approval, or release certification was granted by these changes.**

## Mission

Develop a comprehensive, evidence-backed Magic: The Gathering companion spanning cards, rules, mechanics, lore, the timeline, characters, planes, factions, relationships and lore-first Commander deckbuilding. Reuse and improve existing repository records and tools. Preserve the finished Grixis Commander Encyclopedia as a separate, approved collection.

**Owner preferences:** Prioritize English/default-language card and printing data. There is **no need to ingest every foreign-language printing**. Keep lore fidelity and maximum realistic strategic optimization together in future decks. Explain uncertainties; never elevate a name match or thematic proxy into canonical fact without evidence.

## Verified status at this checkpoint

| Area | Verified checkpoint | Meaning / caveat |
| --- | --- | --- |
| Grixis Encyclopedia | **62/62 finalized** | Historical approvals and exact lists remain protected. |
| Oracle Cards snapshot | **39,164 Oracle IDs** | October 29 Scryfall source includes digital/special objects; not all are tabletop-playable cards. |
| Individual card index | **33,894 records** | The 5,270 Oracle IDs outside the index are now classified from the verified October 29 Oracle snapshot: 4,154 excluded layouts, 811 outside paper/eternal scope, 305 future-dated eligible objects, **0 already-released eligible omissions**. |
| Set/printing inventory | **1,062 set codes; 119,701 default-language printings; 107,898 English paper printings** | Verified October 29 Scryfall Default Cards snapshot and new `data/set_atlas/` Phase 1B pilot. The October 28 shard manifest held 119,509 / 107,700; five set codes changed. Includes **1,051 future-dated printings**, not 1,051 newly released cards. Set/product and shard certification remains incomplete. |
| Phase 1B fast-track released-card gate | **106,855 released English paper printings; 1,062/1,062 per-set counts agree** | Read-only October 28 published index vs. October 29 aggregate audit at October 29 cutoff. Net +198 newer English paper printings are future-dated count increases, not missing released set inventory. **Individual printing-ID parity is not proven** by count parity. |
| Phase 1B full export acceptance | **1,062/1,062 sets export; 119,509/119,509 historical printing IDs bidirectionally joined** | Both printing and unique-identity modes validated from the October 28 published historical index. **39,099 stable Oracle IDs** reverse-join; **106,855 released English-paper printing rows** serialize for the October 29 cutoff. This does **not** establish exact October 29 versus October 28 printing-ID parity. |
| Phase 1B scope and story bridge | **1,062/1,062 set codes categorized; 12 direct Wizards-named story series linked** | Source-graded mutually exclusive classes: **136 historical regular/mainline**, **4 documented exceptions**, **2 provisional localized**, **848 other released paper category codes**, **62 digital-only**, **10 future**. Not an all-time premier-set census or a 1,062-story-lore mapping. |
| Phase 1B functional release gate | **QUALIFIED_OFFLINE_FUNCTIONAL_RELEASE_READY** | Deterministic dated report combines the existing full export, category, story-title and historical-index audits. Scope is released English-paper queries, 1,062-code lookups and explicit opt-ins; cross-snapshot exact printing-ID parity and complete premier/lore certification remain **not claimed**. |
| First Ugin/Bolas/Elder Dragon research pack | **12 source-graded claims; 13 entity nodes; 10 official sources** | First primary-source-reviewed foundation: twins, disputed Bolas account, original/revised Tarkir history, 2019 prison, 2025 escape, uncertain spark, separate Echoverse. **Not a finished genealogy/card representation map or Commander list.** |
| Elder Dragon War Pack A2 extension | **12 additional source-graded claims; 10 new entities; 8 verified official URLs; 9 name-to-historical-printing joins** | Independently adds Piru and Chromium as survivors, records Bolas's incomplete account, differentiates later Dihada/Dakkon/Piru events, traces Crosis and Rith lineages. **Names and printing IDs do not certify art depicting battle scenes or a new legal EDH deck.** |
| Tarkir story/card Pack A3 | **8 further claims; 7 entities; 6 Wizards sources; 6 graded card-art contexts** | `Crux of Fate` independently anchored by an official illustrated duel scene; five other printed card names graded as time-travel device, tomb location or character art. Six Oracle IDs/English-paper printing joins confirmed; **exact art-variant printing match and current Commander legality not claimed.** |
| Tarkir exact printing art Pack A4 | **6 visually compared official-story/printing art pairs; 20 same-illustration printing IDs** | Six Wizards image crops independently compared with exact Scryfall printing IDs/artist/illustration UUIDs. `frf/1` Raymond Swanland Ugin—not earlier `ugin/1` Chris Rahn promo—is the actual duel-story picture. All six cards Commander-legal on 2026-10-30 Scryfall API; **not a complete deck or live CI image classifier**. See [Pack A4](research/PACK_A4_Exact_Tarkir_Story_Illustrations_and_Deck_Pilot.md). |
| Phase 6 Pilot 1 (Ugin & Bolas duality) | **Complete 100-card proposal, UNAPPROVED; CI-verified** | [PR #823](https://github.com/corymstover/GrokBotMTGCompanion/pull/823): Nicol Bolas, the Ravager commander, with three Ugin planeswalkers in the 99. Planner validation passed against the Oct 29 modern snapshot (UBR, 100 cards, 35 lands, 0 hard issues); `evaluate_decklist` hard checks PASS, 1 Game Changer, bracket 3. Tiers: 6 direct / 54 canon reference / 8 lore-inspired / 15 mechanical, plus 17 basics. **Awaiting Cory's approval; not locked or certified.** See [Pilot 1](research/PHASE6_PILOT1_Ugin_Bolas_Elder_Dragon_Duality.md). |
| Phase 3 claim graph v1 | **305 nodes · 488 edges · 78 graded claims · 37 sources (0 non-Wizards)** | [PR #825](https://github.com/corymstover/GrokBotMTGCompanion/pull/825) built it, and [PR #826](https://github.com/corymstover/GrokBotMTGCompanion/pull/826)/[PR #828](https://github.com/corymstover/GrokBotMTGCompanion/pull/828) added Packs B/C (merges `096486c6`, `8ebe31e9`, `185b5146`). `scripts/build_multiverse_graph.py --check` makes CI fail on a stale graph, broken links, duplicate edges or uncited claims. Edge grades: 69 confirmed · 4 disputed · 2 implied · 2 open · 1 alternate continuity. Every pack is still PRELIMINARY_RESEARCH. |
| Pack B (Thran → Yawgmoth → Brothers' War) v1 | **18 claims · 23 entities · 8 Wizards sources** | [PR #826](https://github.com/corymstover/GrokBotMTGCompanion/pull/826), merge `8ebe31e9`. PRELIMINARY_RESEARCH; 1 disputed claim. |
| Pack C (Weatherlight → Invasion → New Phyrexia) v1 | **28 claims · 26 entities · 6 Wizards sources** | [PR #828](https://github.com/corymstover/GrokBotMTGCompanion/pull/828), merge `185b5146`. PRELIMINARY_RESEARCH. Yawgmoth's defeat is graded DISPUTED (C012), and Old Phyrexia's creator is OPEN (C010). |
| Pack C2 (*Return to Dominaria*, Episodes 1–12) | **39 claims · 46 entities · 12 official episodes · 50/50 quotes verbatim** | [PR #841](https://github.com/corymstover/GrokBotMTGCompanion/pull/841), merge `943e06e4`. PRELIMINARY_RESEARCH, not owner approved. Three claims are DISPUTED: Belzenlok's Blackblade claim (RTD006), whether Phyrexia is contained (RTD021) and the Sylex's origin (RTD033). Four are IMPLIED. Audit: `scripts/audit_lore_pack_rtd.py --check`. |
| Pack C3 (*Assault on New Phyrexia*, Episodes 1–5) | **19 claims · 21 entities · 5 official episodes · 27/27 quotes verbatim** | [PR #847](https://github.com/corymstover/GrokBotMTGCompanion/pull/847), merge `b313494f`. PRELIMINARY_RESEARCH, not owner approved. Covers Realmbreaker, the Seedcore, Karn's imprisonment, the compleations (Ajani, Tibalt, Vraska, Nahiri, Nissa, Jace in progress) and Elspeth's escape with the sylex. Claims assert no deaths or fates beyond the text; Elspeth's 'Ajani destroyed the last one' line is left unmodelled because that earlier sylex is not identified. Audit: `scripts/audit_lore_pack_c3.py --check`. |
| Pack C4 (*March of the Machine*, Episodes 1–10) | **21 claims · 26 entities · 10 official episodes · 41/41 quotes verbatim** | Branch `grokbot-c4-mom-20261030` (PR and merge SHA recorded in the overnight handoff). PRELIMINARY_RESEARCH, not owner approved. Covers Norn's assignments (Lukka to Ikoria, Tamiyo to Kamigawa, Atraxa to New Capenna, Ajani to Theros), Sheoldred's execution, Tamiyo's fall on Kamigawa, Chandra and Nissa, Elspeth's rebirth, Wrenn's portal to Zhalfir, Karn's killing of Elesh Norn, and Melira's death and Karn's lost spark. Five inferential claims are graded CANON_IMPLIED with limitations; Wrenn's death and Ajani's restoration are not asserted. Audit: `scripts/audit_lore_pack_c4.py --check`. |
| Pack A5 (Ugin's allies, Pilot 3 research) | **16 claims · 13 entities · 10 official stories · 24/24 quotes verbatim** | [PR #842](https://github.com/corymstover/GrokBotMTGCompanion/pull/842), merge `74a0d7a4`. PRELIMINARY_RESEARCH. Covers Ugin with Sorin and Nahiri (the Eldrazi seal and the broken promise), Sarkhan, Narset, Jace (the Eye and the directives), and Tarkir: Dragonstorm. U016 (Elspeth) is IMPLIED. No deck yet; any Pilot 3 deck stays UNAPPROVED. |
| Story-art caption atlas | **1,060 verified captions · 823 cards · 165 official pages** | [PR #843](https://github.com/corymstover/GrokBotMTGCompanion/pull/843), merge `6917bc86`. `scripts/build_story_art_captions.py` keeps a `<card> \| Art by <artist>` caption only when the card name exactly matches the Scryfall snapshot and the artist is credited there. It rejected 70 captions rather than guessing. In the graph, 143 `art_captioned_in_story` edges link registered sources (including Pack C2's RtD episodes) to cards. Navigation only, not canon. |
| Phase 7 companion `mv_ask` | **Card + lore Q&A with VERIFIED / QUALIFIED / NOT_FOUND confidence** | [PR #827](https://github.com/corymstover/GrokBotMTGCompanion/pull/827) (merge `d9611cd6`), extended in [PR #828](https://github.com/corymstover/GrokBotMTGCompanion/pull/828)/[PR #829](https://github.com/corymstover/GrokBotMTGCompanion/pull/829). An unknown entity exits with code 3 rather than guessing. Card answers are VERIFIED only when the Oracle drift report covers the current snapshot. |
| Commander rules checks | **Deck construction built (CR 2026-09-25); gameplay interaction evidence checks built (rulings + CR 701/702); no game simulation** | [PR #836](https://github.com/corymstover/GrokBotMTGCompanion/pull/836) (merge `84130ca8`): `scripts/commander_rules.py` covers 903.3–903.5d and 702.124 partner variants. The eligibility audit agrees with the index on all 33,894 cards. Interaction checks (PR for `scripts/rules_interactions.py`): `pair A B` returns published rulings of either card that name the other, keyword rulings, and verbatim CR 701/702 text. The excerpt is 266 sections and 801 rules from the same sha `8d860e45` TXT. An audit over all 5 draft decklists finds 12 direct ruling links, such as Urza's Saga with the Urza's Tron lands. Cards with no published ruling are not modelled. The lookup/rules release criterion stays PARTIAL. |
| Lore pilots | **Pilots 1, 2 and 3 are UNAPPROVED proposals** | [PR #823](https://github.com/corymstover/GrokBotMTGCompanion/pull/823) (Ugin & Bolas) and [PR #832](https://github.com/corymstover/GrokBotMTGCompanion/pull/832) (Original & Primeval Dragons) and Pilot 3 (Ugin's Allies and Heroes, [PR #844](https://github.com/corymstover/GrokBotMTGCompanion/pull/844), merge `0344cd53`) use the generic spec builder. |
| Oracle text drift (Oct 28 shards vs Oct 29 snapshot) | **0 changes across 33,894 cards** (Oracle text, name, type, identity, Commander legality, Game Changer) | [PR #829](https://github.com/corymstover/GrokBotMTGCompanion/pull/829), merge `b5ff3a2f`. This independently confirms the existing 5,270-ID classification. 305 new paper IDs are future-dated (`trk`/`trc` release on 2026-11-13). |
| Phase 8 release-readiness check | **NOT_RELEASE_READY: MET 1 · PARTIAL 3 · NOT_MET 1 · EXTERNAL 2** | [PR #830](https://github.com/corymstover/GrokBotMTGCompanion/pull/830), merge `f6a91349`. A read-only evaluation of the 7 first-release criteria (`data/release/readiness_2026-10-30.json`). It never approves or certifies. |
| Priority card enrichment | **5,362 / 5,362 (100%)** | Batch 38 ([PR #848](https://github.com/corymstover/GrokBotMTGCompanion/pull/848), merge `f65fe727`) adds the remaining **1,953** records from caches rebuilt from public EDHREC JSON and Commander Spellbook data, using the pinned Scryfall 2026-10-29 snapshot. The 3,409 earlier records are byte-identical. Of the new records, 202 carry official-story links (201 presented-on, 1 spotlight), 462 carry only an outside-canon flag (276 Un-/playtest, 186 Universes Beyond) and 1,289 carry neither. All 1,751 records without a link say plainly that no lore is linked yet (synergy batch), which is not a claim that the card has no story. *(Corrected 2026-10-30 batch 4: the earlier "664 lore-linked" figure wrongly counted flag-only records as linked.)* **Batch 4 story links (2026-10-30):** 123 records now carry *Named verbatim in official story text* (full card name, case-sensitive, in Magic Story or Planeswalker's Guide prose; fallback only), and 24 gain artist-matched *Card art shown on* evidence from the Phase 1B caption atlas. This newly links 136 records (b35 73, b36 22, b38 41). Unlinked records fall from 2,971 to 2,835. For batch 38 the split is now 243 linked, 456 flag-only and 1,254 neither. All changes are additive. |
| Official Wizards story inventory | **660/660 recovered and strictly audited** | Hash/URL provenance committed; full article text was cached outside Git and must be refetched/audited in a new environment. |
| Uncertain character links | **341 name-only links triaged** | Two official-page leads warrant review; triage is not canon approval. |
| Cards without a linked lore entry | **2,835** ❓ cards (the earlier ~1,220 was stale); **208** linked by the story overlay (Batch 13 UB-detection fix, [#903](https://github.com/corymstover/GrokBotMTGCompanion/pull/903)), **2,626** "no lore yet" (1,304 Universes Beyond excluded); a separate printed-flavor overlay links **23** more (+6 name-only, 11 speaker-is-card-character), leaving **1,282** non-UB cards with no lore | Investigate or preserve as documented unknowns; never fabricate lore. |
| Historical Scryfall lock | **Preserved** | `data/grixis/dev_snapshot_lock.json` records `snap-20261016`; exact old bulk bytes remain unconfirmed. |
| Active Scryfall release | **Archived, re-downloaded, verified** | [snap-20261029-40848334824-1](https://github.com/corymstover/GrokBotMTGCompanion/releases/tag/snap-20261029-40848334824-1): Oracle Cards, Default Cards, Rulings and SHA-256 manifest. |
| Snapshot reconciliation | **Passed read-only** | [PR #784](https://github.com/corymstover/GrokBotMTGCompanion/pull/784) and [report workflow](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40848889092): 0 previously indexed/enriched IDs disappeared; 0 differences in indexed type, color identity, Commander legality, Game Changer status or ruling counts. It is **not** a complete historical Oracle-text diff. |

Infrastructure checkpoint: [PR #783](https://github.com/corymstover/GrokBotMTGCompanion/pull/783) separated current Multiverse ingestion from the historical Grixis lock, added the durable snapshot capture/verification workflow, and passed CI. [PR #784](https://github.com/corymstover/GrokBotMTGCompanion/pull/784) added the read-only research reconciliation and passed CI. [PR #789](https://github.com/corymstover/GrokBotMTGCompanion/pull/789) merged the verified first Phase 8 generated batch; [lore/Phase 8 CI](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40858943537), [Multiverse snapshot CI](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40858943744) and [focused Grixis CI](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/40858943638) all passed.

## Phase 1 — Card database and research inputs

- [x] Preserve the original 62 Grixis approved decks separately.
- [x] Archive a current Scryfall Oracle Cards, Default Cards and Rulings snapshot with hashes.
- [x] Independently download the release assets again and verify them.
- [x] Separate historical and modern Scryfall caches and validation modes.
- [x] Compare the new snapshot against the committed card index and enrichment inventory without mutating either.
- [x] Classify the **5,270 currently unindexed Oracle records** against the independently verified October 29 snapshot and existing ingest policy; see `data/multiverse_audits/oracle_index_2026-10-29.json` and `scripts/audit_oracle_index.py`.
- [x] Audit eligible released missing records: **0** under the documented October 29 index predicate. Re-audit future-dated cards after release; do not force-add intentionally excluded objects.
- [x] Finish the **1,953 remaining priority-card lore/synergy enrichments** without flattening existing curated data (batch 38, 2026-10-30: synergy-complete; lore links for 202, outside-canon flag only for 462, and an honest "not linked yet" on all 1,751 unlinked records, 1,289 of which have neither link nor flag; corrected from an earlier "664 linked" miscount).
- [x] Document a repeatable update process for future Scryfall changes, current legality, and official rules. *(v2.37, Batch 9: [UPDATE_PROCESS.md](UPDATE_PROCESS.md) walks through Scryfall snapshot capture and reconciliation, Oracle drift, legality and printing rebuilds, CR excerpt refresh, official story crawl, cache audit, claim extraction, rebuild, recount and publishing, using only scripts already in `scripts/`. This box covers the written process; each refresh still has to be run and verified when new data arrives.)*
- [x] Recount coverage and verify representative lookup queries after each published batch. *(v2.37, Batch 9: `scripts/batch_recount.py` recounts pages cited and reviewed, claims and arcs from the committed inventory and graph. It also re-asks 13 representative questions through `mv_ask`: siblings, killers, creators, mentors, faction leaders with era context, and one unknown entity that must stay NOT_FOUND. It exits 1 on any failure. CI runs it, together with `tests/test_batch_recount_b9.py`, in `phase7-companion-ask.yml`. It runs per PR touching the graph, not yet as a recorded per-batch report, so the box stays unchecked. **v2.38, Batch 10:** the recount is now also recorded per batch: `data/release/batch_recount_2026-10-30_b9.json` ([#888](https://github.com/corymstover/GrokBotMTGCompanion/pull/888)) and `data/release/batch_recount_2026-10-30_b10.json`, written with `python3 scripts/batch_recount.py --json --out …`; 15 representative questions (continuity questions added). Checked as an established practice; it must be repeated each batch.)*

**2026-10-29 first generated batch (cycle 37):** The twelve exact-name notes from the already registered official *Legends of Reality Fracture* source are now present in `data/card_enrichment.json`, `Card Enrichment.md`, and the nine affected card shards. Eight are explicitly labeled Echoverse alternate-continuity portrayals. The current Oracle, Default Cards, and Rulings archives passed SHA-256 manifest verification; all **660/660** official story sources passed strict cache auditing; EDHREC and Commander Spellbook source caches were recovered for the batch. The generator's replay from those offline caches passed with **0** consistency problems. A full JSON record-by-record comparison against the previous 3,397-card baseline found **0 changed, 0 removed, 12 added**; priority coverage is now **3,409/5,362 (63.6%)**. Three new package backlinks were updated without refreshing unrelated prices or EDHREC rankings. Source article text and third-party caches remain uncommitted and must be recovered and verified again in another environment. This is a batch-level verification, not completion of the entire Phase 8 backlog.

**2026-10-29 index-exclusion audit:** The archived Oracle Cards file matches SHA-256 `0358af62f92ac10f685d5ee6ad9ab23dfbff6f41bc32dfe81b5ab18cf3088adb` in the release manifest. The read-only classifier partitions all **5,270** non-indexed IDs into **4,154** intentionally excluded layouts (tokens, art cards, etc.), **811** nonpaper/non-eternal objects, and **305** eligible but future-dated objects; **0** eligible released objects are missing and **0** already indexed IDs disappear or violate the documented predicate. The future-dated set-code distribution is `trk=190`, `trc=112`, `slc=2`, `pf26=1`, based on Scryfall's October 29 release dates. **Do not ingest these future records now**; re-audit after their release using a newly verified snapshot and explicit cutoff. This is an index-policy audit, not a universal card/playability or set census.

## Phase 1B — MTG Set & Printing Atlas (official milestone)

**Goal:** Make every recorded MTG release independently discoverable, countable, and searchable by set, while retaining accurate card-by-card printing histories. This is a distinct catalog/data-quality milestone within Phase 1, not a replacement for the existing card and lore work.

**Existing foundation:** Reuse `Printing History.md`, `data/printings_summary.csv`, `data/printing_lore/manifest.json`, its per-set printing shards, and the independently archived Scryfall Default Cards snapshot. The October 28 manifest reports **1,062 Scryfall set codes**, **119,509 default-language printing records**, and **107,700 English paper printing records**. These are historical input counts, **not** a verified number of main expansions, unique cards, or newly introduced designs.

**2026-10-29 first Phase 1B catalog/audit checkpoint:** `scripts/audit_set_printing_atlas.py` verifies the independently archived October 29 Default Cards file's SHA-256 and count against its release manifest, then compares its full **119,701** printings to the older manifest's **119,509**. Both snapshots cover **1,062 Scryfall set codes**. The older manifest's set and shard row arithmetic is internally consistent; **105 historic shard file bytes were not available to hash here**. Only **five** set-code totals changed (`trk`, `trc`, `sds`, `pf26`, `pw26`); the net differences are **+192** printing records and **+198** English paper records. The source has **107,898** English paper printings, of which future previews must be excluded when asking what was released as of October 29; **1,051 total printing records** have future `released_at` dates. See `data/set_atlas/audit_2026-10-29.json` for Scryfall `set_type` category counts and `data/set_atlas/catalog_2026-10-29.json` for a dated all-1,062-code set catalog with English-paper distinct Oracle IDs, single-set debuts, same-day tied debuts, and reprints. A verified read-only `scripts/set_atlas_lookup.py` supports **set → cards** and **card → chronological printings/sets**, including exact card-name/Oracle-ID queries. These are first-pass, explicitly snapshot-dated measures; not yet a certified classification of premier releases or canonical set/product associations.

**2026-10-29 historical-shard publication checkpoint:** The 105 committed October 28 shard files are now **all verified against their saved SHA-256 hashes, byte counts, row counts and manifest set links**. A deterministic read-only validator, `scripts/publish_historical_set_index.py`, reconstructs **119,509 distinct printing IDs**, **1,062 set codes**, **107,700 English paper printing records**, and **39,099 stable Oracle identities**; it finds **0 missing Oracle IDs in the normalized historical shards**. As of October 29, the historical snapshot has **106,855 released English paper printings** and **859 future-dated printings across all media**. The generated 32 compact `data/set_atlas/historical_sets_*.json` and `historical_cards_*.json` buckets are now committed and the independent read-only `scripts/historical_set_lookup.py` works without an uncommitted Scryfall bulk download. See `data/set_atlas/historical_shard_audit_2026-10-29.json` for exact per-file hashes and per-set totals. This certifies **the committed historical shards**, not the missing October 28 original bulk file; cross-source byte/ID reconciliation remains unverified. The separate October 29 Scryfall atlas remains authoritative for its later snapshot date.

**2026-10-29 sourced set/product metadata checkpoint:** Scryfall's official `/sets` API supplied a dated Set-object metadata snapshot (UTC 2026-10-29 23:38:34); all **1,062** codes from the October 29 card-printing atlas matched set metadata with **0 conflicts/missing codes**. The API listed **1,063** codes at fetch time; the one extra, `nau` (2027-02-05), was not in the earlier bulk and is kept out of that snapshot's printing totals. Scryfall explicitly supplies **560 `parent_set_code` relations** and **10 future-dated set codes**. Under the strict cutoff of October 29, **142** non-digital entries were typed `expansion` or `core`; that is a *source category candidate count*, **not** a Wizards-certified number of premier sets. No unnamed or inferred product links were created. Immutable source metadata: `data/set_atlas/scryfall_set_metadata_2026-10-29.json`; normalized joins and audit: `data/set_atlas/product_catalog_2026-10-29.json`, `data/set_atlas/product_audit_2026-10-29.json`. Read-only `scripts/set_product_lookup.py` filters by code/name/year/type/date/parent without network access. `scripts/audit_set_product_links.py --check` and `tests/test_set_product_links.py` validate reproducibility. Human index: `SET_ATLAS.md`. Scryfall Set API metadata was fetched later than the archived same-day Default Cards bulk; source times and counters are not interchangeable.

**2026-10-29 Wizards release-family classification checkpoint:** A bounded **30-code** exact-match review now cross-references Wizards' primary product archive, release notes and official product-family explanations against the October 29 1,062-code Scryfall product catalog. It verifies **21 officially documented main releases from 2023 through October 29, 2026** (13 first-party main set releases, six Universes Beyond main releases, and two earlier 2023 main-set release notes). It explicitly separates `mat` (Standard-legal epilogue micro set), `big` (OTJ's subset), `om1` (digital Universes Within counterpart), four special products (`mh3`, `acr`, `pip`, `inr`) and two future main releases (`trk`, `mdd`). A **142**-entry full-history, released, non-digital Scryfall expansion/core category contains **21 reviewed regular main releases**, **two documented auxiliary exceptions** and **119 not-yet-reviewed category candidates**. This is **not** an all-time premier release count. Sources and per-code evidence: `data/set_atlas/wotc_reviewed_release_evidence_2026-10-29.json`; deterministic result: `data/set_atlas/wotc_release_classification_2026-10-29.json`. Rebuild/check with `scripts/audit_wotc_premier_sets.py`; user guide `SET_ATLAS.md`. Future history must be explicitly reviewed against Wizards evidence instead of automatically accepting Scryfall's `set_type`.

**2026-10-29 historical release-census checkpoint (1993–2002):** Wizards' [Looking Back, Part 1](https://magic.wizards.com/en/news/making-magic/looking-back-part-1) lists year-by-year historical randomized booster products; its [official core set enumeration](https://magic.wizards.com/en/news/making-magic/trivial-pursuit-more-or-less) explicitly recognizes 21 regular core editions over the historical span. Against the Oct. 29 Scryfall metadata, all **38** eligible 1993–2002 `expansion`/`core` codes received a bounded review: **35 historically regular expansion/core releases**, **1 direct-source excluded discarded printing** (`sum`, Summer Magic/Edgar; [Wizards](https://magic.wizards.com/en/news/making-magic/25-more-random-things-about-magic-2016-06-20)), and **2 provisional foreign-border variants** (`fbb`, `4bb`; *not yet directly source-certified*). The 1993–2002 classification uses historical **regular expansion/core release**, not the modern term *premier set*, and preserves the region-dependent Arabian Nights 1993/1994 release caveat. Combined across the two primary-source batches, **56** qualifying released mainline editions/sets are source-reviewed, **3** products are directly documented auxiliary/discarded, **2** foreign-border variants remain provisional and **81** candidates dated 2003–2022 remain unreviewed. These are qualified evidence partitions of **142** Scryfall non-digital released `expansion`/`core` codes; the **all-time premier count is NOT yet certified**. Evidence and reproducible report: `data/set_atlas/wotc_early_release_evidence_1993_2002.json`, `data/set_atlas/wotc_early_release_audit_1993_2002.json`, `scripts/audit_wotc_early_sets.py`, `tests/test_wotc_early_sets.py`; `SET_ATLAS.md` records the interpretation.

**2026-10-29 historical release-census checkpoint (2003–2022):** [Wizards' Looking Back, Part 1](https://magic.wizards.com/en/news/making-magic/looking-back-part-1), [Part 2](https://magic.wizards.com/en/news/making-magic/looking-back-part-2), and the [official core edition enumeration](https://magic.wizards.com/en/news/making-magic/trivial-pursuit-more-or-less) corroborate all **81** remaining released/non-digital `expansion`/`core` codes from 2003–2022: **80 historical regular expansions/core editions** and one specifically documented **Time Spiral Timeshifted (`tsb`) bonus sheet**, not a standalone main release. The complete 142-code Scryfall category reconciles as **136 source-reviewed historically regular or contemporary mainline releases**, **4 directly documented auxiliary, discarded, or integrated bonus-product codes** (`mat`, `big`, `sum`, `tsb`), and **2 provisional localized printing variants** (`fbb`, `4bb`). **Zero** of the 142 codes remain wholly unreviewed, but those two variants still lack independent primary-source certification. This **does not** certify the total number of all-time premier sets across all Scryfall categories or reconcile retroactive terminology; treat 136 only as the defined **regular/mainline-within-Scryfall-expansion/core candidate subset**. Per-code primary sources and exact reproducible audits: `data/set_atlas/wotc_mid_release_evidence_2003_2022.json`, `data/set_atlas/wotc_mid_release_audit_2003_2022.json`, `scripts/audit_wotc_mid_sets.py`, `tests/test_wotc_mid_sets.py`. The separate 1,062-code set/printing atlas continues to catalog all supplemental sets.

**2026-10-29 cross-category product-family checkpoint:** A deterministic whole-catalog audit (`scripts/audit_set_cross_category.py`, `data/set_atlas/cross_category_audit_2026-10-29.json`) divides all **1,062** Scryfall set codes into **142** released non-digital expansion/core candidates, **848** released non-digital codes in other `set_type` categories, **62** already-released digital-only codes and **10** future-dated codes; no overlap or omissions. A **12-product** bounded Wizards source review now distinguishes the substantial Modern-legal but non-Standard-2023 `ltr` (Lord of the Rings), Modern-only `acr`, the `mh1`/`mh2`/`mh3` Modern Horizons supplemental line, `cmm`, `inr`, `rvr`, `j22`, `pip`, `ltc`, and `cmr`. The **836** other released, non-digital non-expansion/core codes have **not** each had official individual-product review and MUST NOT be called 836 additional premier sets. Key sources: [Wizards 2022 premier/Standard description](https://magic.wizards.com/en/news/announcements/magic-the-gathering-pricing-update), [2025 forward-only Universes Beyond policy](https://magic.wizards.com/en/news/announcements/aligning-the-universes-making-all-our-sets-legal-in-all-our-formats), plus exact Wizards product/release links in `data/set_atlas/cross_category_evidence_2026-10-29.json`. External specialist [Cardmarket Core Sets](https://help.cardmarket.com/en/CoreSets) corroborates `fbb` and `4bb` as foreign-language black-border versions of existing core editions, but they **remain provisional** pending a Wizards primary citation. This is a **cross-category scope and exception audit**, not a certified all-time premier-set census; don't reinterpret the separate 136 historical regular/mainline expansion/core count as every standalone Magic booster release.

**2026-10-29 complete outside-category research triage checkpoint:** The read-only, deterministic `scripts/audit_product_family_triage.py` generated `data/set_atlas/product_family_triage_2026-10-29.json` from the **frozen October 29** Scryfall product catalog and the prior official-example ledger. All **848** released non-digital set codes outside `expansion`/`core` now have exactly one explicit **Scryfall-type-derived research cohort**: **645** promotional/records/extras, **112** preconstructed/boxed, **51** draft/starter variants, **34** reprint/curated products, **6** special inserts/Eternal subsets. The previously **12 individually Wizards-reviewed** codes retain their primary-source links; **836** remain individually source-pending, with a reproducible sortable priority queue and distinct known exceptions (`plst`, localized Chronicles border variants, Universes Within, Modern-only LTR and Modern Horizons). These cohorts are **research triage**, NOT Wizards' official product classification, an additional premier-set count, or a proven list of physically standalone booster products. Explicit `parent_set_code` is retained; absence of parent does not prove standalone. A separate `scripts/product_family_lookup.py` offers offline `--summary`, `--cohort`, `--type`, `--parent`, `--priority` and `--only-pending` lookups. Five focused integrity tests and a dedicated CI rebuild protect the entire 1,062-code partition and forbid silently upgrading the 836 unreviewed entries into official facts. This is a source-preserving triage milestone; **source review remains necessary** for each officially certified product-family or premier claim.

**2026-10-29 first 23-product Wizards primary-source draft/starter batch:** A bounded, per-code evidence ledger (`data/set_atlas/draft_starter_primary_sources_2026-10-29.json`) cites Wizards' own official product/design/release notes for **23 of the 44** previously source-pending `draft_and_starter_variants` records (Portal and Starter, supplemental Un- booster sets, preconstructed Unsanctioned, 2014–2016 Conspiracy, Battlebond, Jumpstart and Foundations Jumpstart, Innistrad Double Feature, Commander Legends: Battle for Baldur's Gate, Ravnica Clue Edition, Mystery Booster playtest sheets/2021 return, Magic Origins Clash Pack, and Mystery Booster Commander Edition). The exact-source replay audit (`scripts/audit_draft_starter_sources.py`, `data/set_atlas/draft_starter_primary_audit_2026-10-29.json`) conserves **848** released, non-digital outside-category codes and the original **12** reviews; now **35** individually Wizards-reviewed, **813** still source-pending, with **21** remaining within the draft/starter research cohort. An overlay in `scripts/product_family_lookup.py` displays the newer 35/813 status without overwriting the frozen v2.1 12/836 baseline. Important source difference: Wizards' `mbc` product page lists new-to-Magic card **Commander legality November 13, 2026** and other Eternal formats **January 1, 2027**, even though Scryfall's historical set-level release/first-card date is **October 19, 2026**. Never translate the earlier set date into an assertion of new-card legality. `cmb1`/`cmb2` are convention playtest sheets, `sunf` is the Unfinity sticker-sheet code, and the older Un- products have differing tournament legality. **No new premier sets were inferred.** Automated evidence and overlay tests protect all earlier approvals, source links, and count conservation; **21 draft/starter** codes remain individual-primary-source pending.

**2026-10-29 second bounded draft/starter research batch:** Eight further exact Scryfall set codes (`h17`, `h1r`, `h2r`, `hho`, `ptg`, `ulst`, `unk`, `w17`) have individually cited Wizards **product-family** evidence. Crucially the ledger distinguishes **2 exact codes explicitly named in the Wizards source** (`h2r`, `w17`) from **6 exact set-code mappings provided by the dated Scryfall catalog**, where Wizards directly documents the product or printing *family* but not its Scryfall code. Examples: `h1r`/`h2r` are retro reprint treatments in the Modern Horizons 2/3 products; `ulst` reprints occur within Unfinity Collector Boosters, not as a separately released edition; `hho` is Wizards' holiday gift-card tradition; `ptg` was a limited charitable product; `unk` tracks Gavin Verhey Unknown-event playtest cards. The deterministic `scripts/audit_draft_starter_batch2.py` and `data/set_atlas/draft_starter_batch2_audit_2026-10-29.json` now reconcile all **848** outside-category paper codes as **43 with primary Wizards product-family evidence** and **805 source-pending**, of which **13** remain in draft/starter (`cp1`, `cp2`, `itp`, `ph17`–`ph23`, `phtr`, `punk`, `w16`). `scripts/product_family_lookup.py` now applies the source-graded second evidence batch atop the original 12 and subsequent 23, without rewriting earlier frozen data. **Nothing new was certified as a premier release** or individually card-legal just because the official article discusses a family. Pending codes stay unresolved. `tests/test_draft_starter_batch2.py` and focused CI enforce conservative grade claims, source URLs, uniqueness and exact count conservation.

**2026-10-29 Wizards reprint/curated 28-code checkpoint:** A reviewed [Wizards source ledger](data/set_atlas/reprint_curated_sources_2026-10-29.json), [reproducible 28-code audit](data/set_atlas/reprint_curated_source_audit_2026-10-29.json), test and read-only lookup overlay extend the outside-category classification **from 43 to 71 evidence-backed product-family records**, reducing the **source-pending** pool **from 805 to 777** across 848 released non-digital outside-category set codes. Of the **31** formerly unreviewed `reprint_and_curated_products` records, **28** have Wizards product-name/family support, and exactly **3 remain**: `bchr` (Chronicles Foreign Black Border), `rin` (Rinascimento), `ss2` (Signature Spellbook Gideon). The 28 comprise all **ten** From the Vault installments explicitly enumerated by [Wizards](https://magic.wizards.com/en/news/making-magic/trivial-pursuit-more-or-less), eight historical Masters products directly traced in [Double Deal](https://magic.wizards.com/en/news/making-magic/double-deal-2020-07-20), three further randomized reprint products in [Looking Back, Part 2](https://magic.wizards.com/en/news/making-magic/looking-back-part-2), Mystery Booster 2, early Chronicles/Renaissance, The List/Universes Within, and the **Jace/Chandra** Signature Spellbooks. **Evidence grades matter:** `slx` is an actual code explicitly printed in its [Wizards source](https://magic.wizards.com/en/news/announcements/whats-new-on-the-list-for-wilds-of-eldraine); the other 27 exact set-code mappings come from the frozen Scryfall catalog with official **product names/families**, not Wizards printing that exact code. The provenance-aware `scripts/product_family_lookup.py` now overlays this review without rewriting the 12-, 23-, and eight-code historical source audits. Distinguish randomized reprint boosters, fixed From the Vault/Signature Spellbook products and **embedded** The List/Universes Within card distribution. **Do not** count 71 as premier releases or infer card legality from set-level dates. 13 draft/starter records, three curated/reprint, and other categories remain source-pending.

**2026-10-29 boxed/preconstructed product-source checkpoint:** Wizards primary product guides now support **15 more exact Scryfall codes** in the `preconstructed_and_boxed` research cohort: ten independently packaged games/collections (`arc`, `e01`, `hop`, `pc2`, `pca`, `cma`, `cm2`, `cc1`, `cc2`, `cm1`) and five **oversized scheme or planar-card component archives** with **explicit Scryfall parents** (`oarc`→`arc`, `oe01`→`e01`, `ohop`→`hop`, `opc2`→`pc2`, `opca`→`pca`). This prevents a separate Scryfall code for a scheme/plane card sheet from becoming an invented new standalone set. Wizard sources include [Archenemy 2010](https://magic.wizards.com/en/news/feature/archenemy-rules-revealed-2010-05-17), [Archenemy: Nicol Bolas Release Notes](https://magic.wizards.com/en/news/feature/archenemy-nicol-bolas-release-notes-2017-06-16), [Planechase 2012 gallery](https://magic.wizards.com/en/news/card-image-gallery/card-image-gallery-2012-05-21), [Planechase Anthology](https://magic.wizards.com/en/news/feature/planechase-anthology-celebration-magics-history-2016-11-14), [Commander Anthology II](https://magic.wizards.com/en/news/announcements/commander-anthology-vol-ii-legends-and-decklists-2018-05-08), [Commander Collection Green](https://magic.wizards.com/en/news/card-preview/commander-collection-green-packaging-and-contents-2020-08-22), [Black](https://magic.wizards.com/en/news/announcements/commander-collection-black-packaging-and-contents-2021-08-24), and [Commander's Arsenal](https://magic.wizards.com/en/news/making-magic/command-2012-10-25). Preserve explicit boundary: Wizards certifies the product contents/type, the exact code and parent mapping are the frozen Scryfall catalog, **not Wizards printing each code**. The deterministic report `data/set_atlas/boxed_precon_source_audit_2026-10-29.json`, primary-source ledger `data/set_atlas/boxed_precon_sources_2026-10-29.json`, and `scripts/audit_boxed_precon_sources.py`/CI verify **86 source-backed codes / 762 remaining** across the original 848 outside-category paper codes; **95** boxed/preconstructed codes remain source-pending (down from 110). The offline lookup now overlays this review atop the frozen previous datasets. Do not infer current card legality or count these products/sheets as 15 premier expansions.

**2026-10-29 historical Duel Decks checkpoint:** The official [Wizards Japanese product archive](https://mtg-jp.com/products/other/) independently identifies all **21 original Duel Decks matchup products** sold from 2007 through 2018; [Duel Decks: Anthology](https://mtg-jp.com/products/0000095/) establishes a **single additional 2014 box (official `DD3`)** with eight decks drawn from the first four matchups. The archived Scryfall snapshot splits this one box into **four catalog codes** (`dvd`, `evg`, `gvl`, `jvc`) **without explicit `parent_set_code` values**. Their one-box relationship is verified independently by Wizards and does not overwrite Scryfall metadata. Thus **25 source-reviewed Scryfall codes represent 22 sold products**, not 25 newly launched expansions. Ledger: `data/set_atlas/duel_decks_sources_2026-10-29.json`; reproducible partition: `data/set_atlas/duel_decks_source_audit_2026-10-29.json`; script/tests: `scripts/audit_duel_decks_sources.py`, `tests/test_duel_decks_sources.py`. The cumulative 848-code research status advances from **86/762 to 111 source-backed / 737 source-pending**, of which **70** remain boxed/preconstructed. `GS1` Global Series remains separately pending despite Scryfall `duel_deck` typing. No Grixis deck record or historical Scryfall snapshot was changed.

**2026-10-29 annual Commander family checkpoint:** The [official Wizards product archive](https://mtg-jp.com/products/other/) confirms *Commander 2011* and *Commander 2013–2020* as nine annual preconstructed release families (each may contain multiple individually packaged Commander decks). Nine exact Scryfall `commander` code records `cmd`, `c13`–`c20` now have per-code source URLs in `data/set_atlas/commander_series_sources_2011_2020.json`. The deterministic `data/set_atlas/commander_series_source_audit_2026-10-29.json`, `scripts/audit_commander_series_sources.py`, five focused tests and the offline lookup overlay preserve all prior reviews and advance to **120 source-backed / 728 pending** across the original 848 outside-category paper records; **61** remain boxed/preconstructed. Do not equate one annual family code with one physical boxed deck or a new premier expansion. The official Japanese product page supplies the release-family evidence; Scryfall provides the code/date. The series from `C21` onward remains pending. No Grixis approvals or frozen snapshots changed.

**2026-10-29 set-linked Commander 2020–2022 checkpoint:** Twelve additional exact Scryfall `commander` codes (`znc`, `khc`, `c21`, `afc`, `mic`, `voc`, `nec`, `ncc`, `dmc`, `40k`, `brc`, `scd`) are individually sourced to Wizards product announcements or official Commander decklist articles. Primary links: `data/set_atlas/commander_set_linked_sources_2020_2022.json`. Reproducible report and offline overlay: `data/set_atlas/commander_set_linked_source_audit_2026-10-29.json`, `scripts/audit_commander_set_linked_sources.py`; five targeted regressions and scoped GitHub Action. The source verifies the Commander preconstructed product family, **not** exact printable cards—Wizards cautions that dynamically displayed Gatherer decklists can reflect other printings. Keep the exact Scryfall code/date/parent join independent and do not infer new-card counts, premiere status or legality. This advances the original 848 released non-digital other-category Scryfall record census to **132 source-backed / 716 pending**, with **49** boxed/preconstructed pending; 19 newer `commander` codes remain pending. The frozen Grixis snapshot and 62 approved decks remain untouched.

**2026-10-29 modern Commander 2023–2026 checkpoint:** All **19** remaining `commander`-type Scryfall records now have individually linked Wizards decklist sources: `onc`, `moc`, `woc`, `who`, `lcc`, `mkc`, `otc`, `m3c`, `blc`, `dsc`, `fdc`, `drc`, `tdc`, `fic`, `eoc`, `ecc`, `soc`, `msc`, `frc`. The first-party source ledger is `data/set_atlas/commander_modern_sources_2023_2026.json`, derived report `data/set_atlas/commander_modern_source_audit_2026-10-29.json`, replay script `scripts/audit_commander_modern_sources.py`, targeted tests and CI. **Important FDC exception:** frozen Scryfall `fdc` set-level earliest-card date is November 15, **2024**, whereas the [Wizards Foundations Commander decklists](https://magic.wizards.com/en/news/announcements/foundations-commander-decklists) announce five boxed decks released alongside *Reality Fracture* on October 2, **2026**. Both dates remain independent and visible: the 2026 boxed products are **not** falsely dated to 2024, and the 2024 Scryfall metadata is not overwritten. No article is taken as certification of the code, exact printed cards, new-design counts, or legality. The overall outside-category partition advances to **151 source-backed / 697 pending** (848 total), with **30** boxed/preconstructed records still pending and **zero** `commander`-type records pending. No Grixis decklists or historical snapshot bytes changed.

**2026-10-29 specialty box and premium deck checkpoint:** Fourteen further non-Commander `box`/`premium_deck` codes now have original Wizards product/decklist or official Japanese catalog sources: `cst`, `h09`, `pd2`, `pd3`, `md1`, `e02`, `gk1`, `g18`, `gnt`, `gk2`, `gn2`, `q06`, `q07`, `gn3`. Official Wizards Japan prints the exact **H09, PD2, PD3, MD1** three-letter codes, while the other ten are graded **named-family crosswalks**, not proof Wizards explicitly named each Scryfall code. [The 2018 Game Night + Gift Pack announcement](https://magic.wizards.com/en/news/announcements/introducing-magic-game-night-and-updated-gift-pack-2018-08-27) supports two **different products** (`gnt` and `g18`), not a duplicate box. `gn3` has a [Wizards printed decklist-insert correction](https://magic.wizards.com/en/news/announcements/game-night-free-for-all-contents-update), so no exact card-printing inventory is certified. Source ledger `data/set_atlas/boxed_specialty_sources_2006_2022.json`, reproducible audit `data/set_atlas/boxed_specialty_source_audit_2026-10-29.json`, replay script `scripts/audit_boxed_specialty_sources.py`, guarded lookup/test/CI. New tally **165 source-backed / 683 pending** of 848, with **16** boxed/preconstructed pending; no frozen data or Grixis deck changes.

**2026-10-29 Secret Lair and Global Series checkpoint:** Five further bounded source reviews cover `gs1`, `sld`, `slu`, `slc`, and `slz`: the [Global Series two introductory Planeswalker decks](https://mtg-jp.com/products/0000172/) (Wizards Japan explicitly prints **GS1**); the [2019 Secret Lair Drop Series launch](https://magic.wizards.com/en/news/announcements/secret-lair-recap-2019-11-25), an **ongoing collection, not one box**; [Secret Lair Ultimate Edition](https://magic.wizards.com/en/news/announcements/making-fetch-happen-secret-lair-ultimate-edition-2020-03-13), a retail five-land display; the [30th Anniversary Countdown Kit](https://magic.wizards.com/en/news/announcements/kicking-magics-30th-anniversary-celebration-2022-10-04), 30 themed packets in one collection; and [Chaos Vault's Zeta Set](https://magic.wizards.com/en/news/announcements/chaos-vault-the-zeta-set-puts-the-playtest-in-your-hands), whose Pauper treatment later received an official update and is **not** certified by this family audit. Ledger `data/set_atlas/boxed_special_lair_global_sources_2018_2026.json`, deterministic report `data/set_atlas/boxed_special_lair_global_audit_2026-10-29.json`, audit script and guarded lookup/CI. **170 of 848 source-backed, 678 pending, 11 boxed/preconstructed pending.** The last eleven boxed codes are `rqs`, `mgb`, `ath`, `brb`, `btd`, `dkm`, `psal`, `phuk`, `dpa`, `ps11`, `g17`; these remain research-pending rather than being falsely source-certified from third-party descriptions or unrelated digital products.

**2026-10-29 exact insert and Clash Pack/Spellbook checkpoint:** Nine additionally source-reviewed codes: six `eternal`-typed integrated card subsets `bot`, `rex`, `spe`, `tle`, `tmc`, `hoc`, all **explicitly coded** in individual [Wizards Brothers' War](https://magic.wizards.com/en/news/feature/whats-inside-the-brothers-war-boosters), [Ixalan/Jurassic World](https://magic.wizards.com/en/news/feature/collecting-the-lost-caverns-of-ixalan), [Spider-Man](https://magic.wizards.com/en/news/feature/collecting-marvels-spider-man), [Avatar](https://magic.wizards.com/en/news/feature/collecting-avatar-the-last-airbender), [TMNT](https://magic.wizards.com/en/news/feature/collecting-teenage-mutant-ninja-turtles) and [Hobbit](https://magic.wizards.com/en/news/feature/collecting-the-hobbit) articles; plus `cp1`/`cp2` two-deck Clash Packs and `ss2` Gideon Signature Spellbook. **SS2** is explicitly shown as a *card printing code* on [Wizards' own card gallery](https://mtg-jp.com/products/card-gallery/0000183/470542/) while its boxed product page does not itself claim an official product code. The `cp2` earliest Scryfall card date **January 23, 2015** stays separate from the [Japanese boxed Clash Pack's January 30 sale date](https://mtg-jp.com/reading/products/individual/0011836/). The six exact Eternal subset codes are **not** six additional premier expansions. Ledger `data/set_atlas/inserts_clash_spellbook_sources_2014_2026.json`, deterministic audit `data/set_atlas/inserts_clash_spellbook_source_audit_2026-10-29.json`, script/tests/CI and guarded lookup. **179 of 848 source-backed / 669 pending**; **zero** codes in the special-inserts/Eternal research cohort still source-pending, **11** draft/starter and **2** reprint/curated pending. All 11 prior boxed records remain pending; no frozen snapshot or Grixis approved lists changed.

**2026-10-29 all-Masterpiece supplemental-sheet and historic collectibles checkpoint:** Source-review the complete **17-code** Scryfall `masterpiece` group and two commemorative historical `memorabilia` records (`30a`, `ced`) using individual Wizards articles. Stronger evidence: **12 articles print their exact set code** (examples: [STA](https://magic.wizards.com/en/news/feature/strixhaven-school-mages-and-commander-2021-edition-release-notes-2021-04-16), [BRR](https://magic.wizards.com/en/news/feature/the-brothers-war-release-notes), [SOA](https://magic.wizards.com/en/news/feature/secrets-of-strixhaven-release-notes)); seven official sources identify a named product family only, with the code supplied by Scryfall. `med`, `mar`, `spg` represent **multiple boxes/releases or recurring subsets**, not a single sold product; [30th Anniversary Edition](https://magic.wizards.com/en/news/announcements/celebrate-30-years-magic-gathering-30th-anniversary-edition-2022-10-04) is expressly non-tournament-legal. The separate International Collector's Edition (`cei`) has not been individually certified. A 19-row ledger `data/set_atlas/masterpiece_memorabilia_sources_1993_2026.json`, immutable 848-code cumulative report `data/set_atlas/masterpiece_memorabilia_source_audit_2026-10-29.json`, guarded lookup, tests and focused CI reproduce **198 source-backed / 650 pending**. All **17 masterpiece records now source-backed**, while **626** promo/extras codes remain pending, including 457 with explicit Scryfall parent and 169 without. These source citations do not prove exact card inventories, card debuts, updated legality, or a new premier-set total.

**2026-10-29 historical event-promo and Worlds collectible checkpoint:** Ten new individually sourced named-family records: one historical oversized [Vanguard](https://magic.wizards.com/en/news/feature/vanguard-2008-08-14) supplement (`pvan`), **five** officially referenced World Championship Decks years `wc97`, `wc98`, `wc99`, `wc00`, `wc04` from Japanese Wizards [1997](https://mtg-jp.com/reading/iwashowdeck/0016981/) through [2004](https://mtg-jp.com/reading/iwashowdeck/0019017/) retrospectives, and four contemporary Love Your Local Game Store programs `plg20`, `plg21`, `plg22`, `plg24` with WPN/Wizards primary articles. The five World Championship sources are **retrospective product mentions**, not restored original box pages, and the local-store articles document dated event-promo families, not complete printing inventories. **None of these ten articles prints the exact Scryfall set code.** Their names/years are crosswalked to the frozen Scryfall catalog with explicit lower evidence grade. Ledger `data/set_atlas/historical_promo_series_sources_1997_2024.json`, reproducible report `data/set_atlas/historical_promo_series_source_audit_2026-10-29.json`, offline guarded lookup, focused tests/CI. **208 source-backed / 640 pending** among 848; **616** promotional extras remain, with 457 Scryfall explicit-parent links and 159 without. Keep `wc01`/`wc02`/`wc03`, `plg25` and other missing years pending rather than filling from secondary material or matching tournament results. No cards, rule files, historical snapshots, or approved Grixis decks changed.

**2026-10-29 Lunar New Year APAC event-program checkpoint:** Six distinct first-party Wizards annual promo program references now substantiate `pl21` (Ox 2021), `pl22` (Tiger 2022), `pl23` (Rabbit 2023), `pl24` (Dragon 2024), `pl25` (Snake 2025), and `pl26` (Horse 2026). [Wizards 2021](https://magic.wizards.com/en/news/announcements/year-ox-store-challenger-series-2021-promos-2021-05-17), [2022](https://magic.wizards.com/en/news/announcements/celebrate-year-tiger-apac-league-events-and-promos-2022-02-09), [2023](https://magic.wizards.com/en/news/announcements/2023-apac-league-and-the-year-of-the-rabbit), [2024 via Magic.gg](https://www.magic.gg/news/play-standard-get-promos-jump-into-the-action-with-these-year-of-the-dragon), [2025](https://magic.wizards.com/en/news/announcements/earn-sweet-year-of-the-snake-promos-at-your-local-game-store), [2026 Traditional Chinese](https://magic.wizards.com/zh-Hant/news/announcements/celebrate-the-year-of-the-horse-at-your-local-game-store-and-more). The 2026 English article redirects; the accessible Wizards Traditional Chinese article is cited solely as program evidence, **not** foreign card data. All six links are *named-family crosswalks*, **not** articles printing the Scryfall code or proving complete inventory, debuts, legality or premier-set status. The December 2023 article previews a 2024 event; Scryfall's 2024 earliest-card date is not overwritten. Ledger `data/set_atlas/apac_lunar_year_promos_sources_2021_2026.json`, derived audit `data/set_atlas/apac_lunar_year_promos_source_audit_2026-10-29.json`, script, guarded lookup and targeted CI advance to **214/848 source-backed, 634 pending**. **610** promo/extras remain pending, of which **457** have an explicit Scryfall parent link and **153** do not. `plny` 2018 remains pending without a first-party source. Grixis is unchanged.

**2026-10-29 official event and collaboration promo checkpoint:** Seven additional named-program crosswalks sourced individually from first-party Wizards: `gdy` Game Day and `sch` Store Championships as distinct programs in one [2022 WPN promo kit](https://wpn.wizards.com/en/news/whats-coming-dmu-marketing-kit), `prcq` 2022 [Regional Championship Qualifiers](https://wpn.wizards.com/en/news/pro-tour-returns-re-ignite-your-stores-competitive-play), `pr23` 2023 qualifiers [previewed in October 2022](https://wpn.wizards.com/en/news/magic-30th-anniversary-kicks-off-with-promos-products-more), Japan's 2023 [Magic × Duel Masters FNM collaboration](https://mtg-jp.com/reading/kochima/0037149/) `pmda`, the [August 2024–May 2025 Cowboy Bebop Standard Showdown collaboration](https://magic.wizards.com/en/news/announcements/announcing-cowboy-bebop-collaboration-promo-cards) `pcbb`, and [Spotlight Series from January 2025](https://magic.gg/news/announcing-the-magic-spotlight-series) `pspl`. **None** of the cited Wizards pages prints the exact corresponding Scryfall code or certifies full print inventories; `PMDA` official Japanese text supports an event only, not non-English printing ingestion. 2022 and 2024 preview article dates are preserved separately from 2023 and 2025 event dates. Ledger `data/set_atlas/event_collab_promos_sources_2022_2025.json`, deterministic report `data/set_atlas/event_collab_promos_source_audit_2026-10-29.json`, offline overlay, five focused tests and CI advance the bounded 848-code cumulative review to **221 source-backed, 627 pending**. **603** promo/extras remain pending (**457** explicit Scryfall parents and **146** without). No card/deck or Grixis snapshots modified.

**2026-10-29 Art Series collectible-inserts checkpoint (v2.17):** Source-review **38 individual `memorabilia` Art Series codes** using specific Wizards Art Card image galleries, the *Innistrad: Midnight Hunt* product page and [2019 *Modern Horizons* release notes](https://magic.wizards.com/en/news/feature/modern-horizons-release-notes-2019-05-31) that expressly say its art cards are not playable. These remain **named Art Series component crosswalks**, **zero Wizards-declared literal `a...` Scryfall codes**, with each original explicit `parent_set_code` and first-printing date preserved, no full card inventory or legality certifications. With no verified page resolving their exact group boundaries, `atla`, `atle` and `ahoc` stay pending. Ledger `data/set_atlas/art_series_primary_sources_2019_2026.json`, cumulative deterministic report `data/set_atlas/art_series_primary_source_audit_2026-10-29.json`, audit script, guarded offline lookup, five tests and focused CI advance to **259/848 named-family evidence-backed, 589 pending**. **565** promo/extras still need source review (**419** explicit Scryfall parent links, **146** no explicit parent); the **11 boxed**, **11 draft/starter**, **2 curated/reprint** cohorts remain. The current ledger is not a declaration that 259 standalone MTG expansions exist. Grixis decks and their approvals remain untouched.

**2026-10-29 token families checkpoint (v2.18):** First-party Wizards token previews independently substantiate **34 additional Scryfall token-family crosswalks** with **18 specifically matched official token articles** spanning Wilds of Eldraine through Reality Fracture plus Fallout. The [Outlaws of Thunder Junction token article](https://magic.wizards.com/en/news/card-preview/the-tokens-of-outlaws-of-thunder-junction) expressly distinguishes OTJ, OTC, BIG and OTP component tokens; the [Modern Horizons 3 token guide](https://magic.wizards.com/en/news/card-preview/the-tokens-of-modern-horizons-3) separates booster and Commander treatments; [Reality Fracture](https://magic.wizards.com/en/news/card-preview/reality-fracture-tokens-and-art-cards) documents Commander token differences across printings. All **34 are named family references, zero exact Scryfall `t`-code claims**; token counters, emblems and helper cards are **not distinct playable-card expansions**. Preserve existing `parent_set_code` and dates, refrain from declaring exhaustive exact printing manifests or card legality, and hold back regional/uncertain subsets such as `ttmc`. The [34-row token ledger](data/set_atlas/token_families_primary_sources_2023_2026.json), [reproducible cumulative audit](data/set_atlas/token_families_primary_source_audit_2026-10-29.json), guarded lookup and source-regression CI advance to **293 of 848 family-backed / 555 pending**. **531** promotional extras remain (**385** explicit parent-linked, **146** unlinked); **11 boxed**, **11 draft/starter** and **2 curated/reprint** records remain. The exact 62-deck Grixis locks were not modified.

**2026-10-29 accelerated Phase 1B release plan and first acceptance checkpoint (v2.19):** Cory authorizes shifting from sequential first-party research of all 555 remaining promo/other-family records to the *functionally complete, correctly qualified, exportable Set Atlas*. Individually source-reviewed family records remain exactly **293/848**; **555** are a **preserved optional research-depth backlog**, **NOT a Phase 1B completion percentage or release-blocking gate**. Never silently promote those 555 to Wizards-certified status. The reproducible `scripts/audit_phase1b_fasttrack.py`, report `data/set_atlas/phase1b_fasttrack_readiness_2026-10-29.json`, focused tests and CI check both dated aggregates, **32 committed historical index hashes**, the **1,062-code category partition**, the **1,062/1,062 joined Scryfall product metadata entries** and nine diverse live set lookup examples plus Black Lotus chronology. Crucially, **all 1,062 sets have identical 106,855 released English-paper per-set printing counts at the October 29 cutoff**, despite **+192 all-printing records and +198 English-paper records** in the October 29 snapshot; the English-paper net increase exists entirely among **future-dated counts**. The five count-changing set codes are `pf26`, `pw26`, `sds`, `trc`, `trk`. **This is per-set count parity, NOT exact cross-snapshot printing-ID certification**, and neither original bulk's bytes are newly reconstructed by this report. The 555-record source backlog stays open for targeted optional improvements. The release still needs full export/scope acceptance and clear category count labels.

**2026-10-29 full-catalog bidirectional and export acceptance (v2.20):** `scripts/audit_phase1b_export_acceptance.py` replays the **entire 1,062-code historical set index** and the historical card-chronology index, verifies **119,509/119,509 distinct printing IDs** reverse-join exactly and **39,099 stable Oracle identities** are present, and runs both printing-list and deduplicated card-list exports for **every one of 1,062 sets**. The October 29 default filter yields **106,855 released English paper printing rows**. **105 codes have valid header-only/empty default exports**, usually due to digital-only, localized or not-yet-released products; flags explicitly opt into those scopes. CSV serialization, representative cross-era examples and date/medium/language boundary tests have focused automated acceptance. User-facing exporter: `scripts/export_phase1b_set_cards.py` (`--mode printings|unique`, `--format csv|json`, `--as-of`, `--include-future`, `--include-digital`, `--include-foreign`). All data are offline from the **October 28 historically published shards**; the separate October 29 new bulk is reconciled by **released per-set counts only**, not exact printing IDs. Evidence: `data/set_atlas/phase1b_export_acceptance_2026-10-29.json`, `tests/test_phase1b_export_acceptance.py`, and focused CI. Completing this export gate **does not finish Phase 1B**: category-qualified release interpretation, source-limited lore links, any higher-grade cross-snapshot ID claim and final release CI/report still require decisions and verification.

**2026-10-29 category-qualified scope and first-party story bridge acceptance (v2.21):** `scripts/audit_phase1b_release_scope.py` preserves the **entire 1,062-code census** in six exclusive categories, checking the prior 142-code primary-source release reviews and 1,062-code Scryfall partition: **136 historical regular/mainline expansion/core**, **4 documented auxiliary/discarded/integrated codes** (`mat`, `big`, `sum`, `tsb`), **2 provisional regional core printings** (`fbb`, `4bb`), **848 other released nondigital category codes** (including token/promo/supplemental/product components), **62 released digital-only**, and **10 future-announced**. The 136 figure is **NOT a certified all-time Wizards premier-set count**; none of the 848 is silently promoted to independent booster-product status. Twelve **curated, exactly titled Wizards Magic Story series** (including *The Brothers' War*, *Phyrexia: All Will Be One*, *March of the Machine*, and *Tarkir: Dragonstorm*) are associated with their appropriate set code through exact titles and published `magic.wizards.com` story URLs in the recovered official index. These establish a source-backed **story publication/series relationship only**, not in-universe chronological order or individual card/canon connections. The 555 optional unreviewed product-family records remain unverified. Repeatable output and dated provenance: `data/set_atlas/phase1b_release_scope_story_bridge_2026-10-29.json`, focused tests and CI. This closes the initial scope/story-label acceptance, **not** the final release, complete Wizards story-link coverage, optional primary-source backlog or cross-snapshot exact-ID caveat.

**2026-10-29 Phase 1B qualified functional release checkpoint (v2.22):** `scripts/audit_phase1b_functional_release.py` composes five previously dated independent reports and enforces **1,062 full-queryable/exportable and categorized set codes**, **119,509 historical IDs with exact internal bidirectional joins**, **39,099 historical Oracle IDs**, **106,855 released English-paper printing rows**, **32 hashed historical indexes**, **12 exact-first-party-titled story-series bridges**, the **136/4/2/848/62/10 category partition**, and the nonblocking but uncertified **555** source-pending product records. Its auditable artifact is `data/set_atlas/phase1b_qualified_functional_release_2026-10-29.json` and its verdict is `QUALIFIED_OFFLINE_FUNCTIONAL_RELEASE_READY`. A dedicated targeted CI workflow reruns all four functional audits, product links, and three relevant unit-test discovery groups (locally **35 + 80 + 13 executions** passed), with the established GitHub Grixis regression remaining a separate required check. **Scope limit accepted for this functional milestone:** original October 28 bulk bytes cannot be reverified from the committed shards; October 29 vs October 28 exact cross-snapshot printing-ID parity remains unknown despite per-set count equality. A stronger bulk/ID-certification claim and definitive all-history Wizards premier-set enumeration are **not part of this functional release verdict**. The unrelated repository-wide unittest suite cannot be represented as wholly green in this partial local checkout (pytest and unrelated legacy Grixis fixtures unavailable). Continue to treat the 555 product-source reviews and broader lore links as optional ongoing research, not false completions.

**2026-10-30 Phase 1B post-merge evidence:** [PR #818](https://github.com/corymstover/GrokBotMTGCompanion/pull/818) merged to `main` at `f171a185473ef3d57a8f86b1e31b746a14877af6`. All **six exact-head CI** workflows passed, including the [qualified functional release gate](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/41006772243), [all-set export acceptance](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/41006772396), [set atlas validation](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/41006772241), [fast-track readiness](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/41006772411), [category/story bridge](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/41006772516), and [focused Grixis mechanics regression](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/41006772280). Main-branch Workflow v2.22 and the final report were read back after merge. These checks certify the **qualified historical offline functional claim**, not the stronger unresolved cross-snapshot ID claims.

**Fast-track release gates (in order; do not bypass):**

1. **Core parity and provenance:** [x] Verify published historical index hashes, all 1,062 set-code joins, per-set released English-paper count parity and dated preview exceptions; [x] restrict the release to a **qualified historical offline functional claim** with conspicuous **unverified original-bulk bytes and cross-snapshot individual-ID parity**. [ ] Higher-grade exact-ID cross-snapshot archival certification is a separate future evidence upgrade, not implied by this release.
2. **Complete discoverability and export:** [x] Verify every one of the 1,062 set-code lookup/export paths; [x] test reusable English card-list exports and exact historical card → chronological set history joins; [x] preserve digital/foreign/future opt-in and card/debut/reprint semantics, documented against the October 28 historical index.
3. **Acceptance and labeling:** [x] Publish six exclusive category-qualified release-scope labels for all 1,062 codes and associated provenance; [x] disclose localized printing variants and current source/category limits; [x] create a bounded, exact-official-title story-series bridge for 12 named releases with no plot/chronology inference. [ ] Decide/document any broader historical "premier" definition or leave it explicitly uncertified; do not auto-link the other 1,050 products to a Magic story.
4. **Release and handoff:** [x] Publish a dated, reproducible **qualified functional release report** with full code/export coverage and explicit limits. [x] Verify **six** exact-head GitHub checks and the existing Grixis regression; merge PR #818, reread final report/main and preserve the 555-item nonblocking source queue. Do not claim strong exact cross-snapshot/source-complete certification or a universal premier-set count from this functional verdict.

**Phase 1B pilot checks completed:**

- [x] SHA-256 verification of the October 29 Scryfall Default Cards source and its reported record count; no duplicate printing IDs or conflicting set name/`set_type` values.
- [x] Internal arithmetic and shard-reference audit of the October 28 baseline manifest, with missing historical shard-byte verification explicitly recorded.
- [x] Reproducible `set_type` category totals, all-code dated catalog, and explicit treatment of future-dated printing records.
- [x] First source-backed, bidirectional set/card lookup CLI; Alpha and Black Lotus spot checks, date-gated Star Trek example, and six portable unit tests.
- [x] Verify all 105 **committed** historical shard file hashes, sizes, row counts, printing-ID uniqueness and set joins; reconstruct stable card/set lookup indexes.
- [x] Independently reconcile individual printing IDs against the **original October 28 bulk**. *(v2.72: exact SHA-matched file recovered; SQLite and all 105 committed historical printings shards plus export manifest rebuilt byte-identically. See `data/scryfall_snapshots/historical_bulk_replay_2026-10-31.json`.)*
- [x] Import and freeze Scryfall Set API `released_at`, `digital`, `set_type` and **560 explicit `parent_set_code` links** for all 1,062 printing-atlas codes; validate against the independent October 29 printing catalog.
- [x] Review a bounded 2023–October 2026 official-main-release sample (21 verified), plus nine reviewed exceptions/upcoming/special products, with direct Wizards citations and tests.
- [x] Review all 38 early 1993–2002 Scryfall non-digital expansion/core codes against Wizards' historical booster/core enumerations; certify 35 regular releases, directly document Summer Magic's rejected print run, and flag 2 localized editions as provisional.
- [x] Review all 81 2003–2022 Scryfall non-digital expansion/core codes against Wizards historical annual release retrospectives and core enumerations; classify 80 as regular sets and `tsb` as an integrated bonus sheet.
- [x] Partition the **entire** October 29 1,062-code Scryfall Set API catalog by release status, paper/digital, and expansion/core versus other categories without overlap; review 12 major non-expansion/core products against exact official Wizards articles and release notes.
- [ ] Independently corroborate `fbb` and `4bb` foreign-border variants with Wizards primary documentation; third-party Cardmarket corroboration is recorded but does not close this gate.
- [x] Exhaustively triage all **848** released non-digital other-category codes into five transparent Scryfall-metadata research cohorts and a sortable, source-linked queue covering the **836** items still awaiting individual Wizards review; preserve the 12 earlier primary-source examples without reclassification.
- [x] Primary-source-review **23** individual draft/starter codes, preserve 12 prior reviewed codes, publish deterministic updated **35 reviewed / 813 pending** research status and read-only lookup overlay; explicitly record Mystery Booster Commander Edition's delayed Commander legality.
- [x] Publish eight additional source-graded Wizards product-family records (two explicitly coded by Wizards, six Scryfall crosswalks) with a guarded lookup overlay; reconcile 43 reviewed / 805 pending.
- [x] Review and source **28/31** reprint/curated products with two evidence grades; preserve prior 43 evidence records, add 28 and publish the cumulative 71/777 offline source overlay.
- [x] Source-review ten packaged Commander/Archenemy/Planechase collections and **five** associated scheme/planar Scryfall component codes with explicit parent-set assertions and deterministic CI; bring outside-category review to **86/848**.
- [x] Source-review all **21** original Duel Decks products and the **four** catalog components of the one official 2014 Anthology; distinguish 25 Scryfall codes from 22 actual boxes, and advance cumulative evidence to **111/848**.
- [x] Independently source the **nine** original annual Commander preconstructed release-family codes from 2011 and 2013–2020, preserving family-vs-deck-count and source-code boundaries; advance to **120/848**.
- [x] Source-review **12** 2020–2022 set-linked/starter Commander release-family codes against individual official Wizards decklist/announcement pages; advance to **132/848**, preserving the distinction between source-backed product families and exact printing inventories.
- [x] Source-review all **19** remaining 2023–2026 `commander`-type release-family codes against official Wizards decklist pages; advance to **151/848** and **zero** pending `commander`-type records. Preserve the `fdc` 2024 earliest-card versus October 2026 boxed-deck release distinction.
- [x] Review **14** non-Commander boxed/preconstructed or premium-deck releases from 2006–2022 with direct Wizards evidence, including four explicitly printed Japanese Wizards official set codes; advance to **165/848**.
- [x] Verify **5** separately documented Secret Lair/Global Series family codes, distinguishing ongoing series from individual boxes and recording explicit **GS1** code support; advance to **170/848**.
- [x] Verify **9** direct Wizards-sourced Eternal/insert, Clash Pack and Gideon Spellbook records: six exact `eternal`-type code declarations, two family-only Clash Pack citations, and one exact **SS2** Wizards card gallery printing citation; advance to **179/848**.
- [x] Source-review **all 17 Masterpiece-typed code records** and two historical collectible printings with 12 explicit Wizards code statements and seven graded named-family citations; preserve the 848-code census and advance to **198/848** without counting bonus sheets as expansions.
- [x] Review ten named Vanguard, World Championship Deck and Love Your Local Game Store promo-family/year references with individually reviewed Wizards primary publications, explicitly grading all ten as **family-only**, without converting later retrospectives into period product evidence; advance to **208/848**.
- [x] Source-review all six Scryfall-coded 2021–2026 Lunar New Year APAC annual promo families against separately linked contemporary Wizards event announcements, noting the accessible 2026 Traditional Chinese article, the 2024 program's 2023 preview, and **zero** officially printed Scryfall codes; advance to **214/848**, preserving 2018 `plny` as pending.
- [x] Source-review seven distinct 2022–2025 event/collaboration records—Game Day, Store Championships, two RCQ program years, Magic × Duel Masters, Cowboy Bebop and Spotlight Series—from corresponding first-party event-promo articles; advance to **221/848**, preserving program-only evidence grades, separate announcement/event dates and all older certifications.
- [x] Source-review **38** individually matched Wizards Art Series product/gallery entries from 2019–2026 as **collectible, non-playable component families**, retain their pre-existing Scryfall parent/date mappings, and explicitly leave three unverified subgroup codes pending; advance cumulative family-backed review to **259/848** without inflating the expansion count.
- [x] Individually source **34** booster, Commander and named supplemental token groupings against **18** official Wizards token guides; classify OTJ/OTC/BIG/OTP correctly, retain 848-code conservation, and advance cumulative source review to **293/848** without treating emblems and helpers as new cards or sets.
- [x] Adopt the v2.19 **accelerated Phase 1B release gates**: no more per-item promo-source marathon as a release dependency; preserve 555 optional source-research gaps. Establish all-1,062 published set-code and released-English-paper **count parity**, retaining an explicit unverified exact-printing-ID boundary.
- [x] Pass v2.20 complete export acceptance: all **1,062/1,062** sets yield CSV/JSON printing and unique-card exports; **119,509/119,509** committed historical printing IDs reverse-link to the per-card chronology, **39,099** Oracle identities are accounted for, and exactly **106,855** released English paper printing rows export under the October 29 cutoff. Keep cross-snapshot exact-ID claims explicitly unresolved.
- [x] Pass v2.21 complete Scryfall set-code **scope classification** into 136/4/2/848/62/10 documented categories with 142 candidate exception evidence checks; curate **12** direct first-party titled Magic Story release-series links. Keep 136 separate from an uncertified all-time premier count; do not infer lore relationships from cards or genre.
- [x] Generate v2.22 deterministic **qualified functional Phase 1B release report** combining all four acceptance layers, full 1,062-code coverage, 119,509 reverse-linked historical IDs, 12 source-limited story bridges, 555 unchanged optional source gaps and explicit snapshot-ID/source-byte limitations. Its separate targeted GitHub CI runs complete Phase 1B unit-test groups and Grixis regression before merge.
- [ ] Resolve the remaining **2** curated/reprint records (`bchr`, `rin`) and **11** draft/starter codes (`itp`, `ph17`–`ph23`, `phtr`, `punk`, `w16`). Their incomplete original evidence remains explicit; no automatic premier-set or legality inference. *(v2.40, Batch 12: still blocked. The pinned Scryfall snapshot gives only set_type and dates for these codes; classifying them needs first-party Wizards product evidence that is not in any cached source. Real blocker, recorded in SET_ATLAS.md.)*
- [ ] Research the remaining **11** older boxed/preconstructed set codes (`rqs`, `mgb`, `ath`, `brb`, `btd`, `dkm`, `psal`, `phuk`, `dpa`, `ps11`, `g17`). Seek official Wizards primary evidence for physical 1990s/2000s products and regional magazine collections; do not promote third-party descriptions to first-party certification or confuse the 2010 DPA physical decks with digital Duels game. *(v2.40, Batch 12: still blocked for the same reason: 1990s/2000s physical-product evidence is not in the snapshot or cached Wizards pages.)*
- [x] Publish complete, GitHub-readable historical set-to-card and card-to-set indexes without a local bulk snapshot (32 deterministic JSON buckets and read-only CLI); the October 29 current-snapshot lookup remains separately dated.

**Counting rules (mandatory in every answer/export):**

- A **set-code count** includes every Scryfall set code in the selected snapshot; distinguish expansion/core sets, Masters/supplemental, Commander products, promos, tokens, digital and other categories. Never present the all-category count as the number of regular expansion sets.
- A **printing count** counts distinct set/collector-number printing entries (including variants when present); a **unique-card count** deduplicates by the selected stable card identity (normally Scryfall Oracle ID). Report both when relevant and document multi-face/special-object handling.
- **Cards appearing in a set** means all included printings or distinct card identities in that release; **cards first introduced in a set** means identities whose earliest eligible release is that set. Separate debuts from reprints and label any ties, preview/promotional-date ambiguities, or digital-versus-paper differences.
- Respect Cory's preference for **English/default-language cards**. Do not imply exhaustive foreign-language coverage. Distinguish physical from digital, released from announced, and snapshot date from current live data.

**Deliverables and verification gates:**

- [x] Audit the existing printing index and per-set shards against the archived Default Cards snapshot; document missing categories, duplicates, and stable joins. *(v2.72: the exact original Oct 28 source now reproduces all 105 archived shards byte-for-byte, with 119,509 distinct printing IDs and no missing/mismatched source records. The independent Oct 29-to-Oct 28 comparison still documents 192 new IDs, 342 `prm` release-date changes and six `trk` paper-flag changes as **real cross-snapshot differences**, not errors or fabricated field equality. See the historical replay and `data/set_atlas/phase1b_snapshot_gates_2026-10-30.json`. Atlas product and release-date qualifications remain.)*
- [x] Establish a normalized set catalog: canonical name/code, `set_type`, release date, paper/digital status, parent set/product associations and authoritative source provenance. *(v2.40, Batch 12, [#900](https://github.com/corymstover/GrokBotMTGCompanion/pull/900), `data/set_atlas/phase1b_snapshot_gates_2026-10-30.json`: PASS: every parent link resolves (`tnau`→`nau` resolves to the Set API record of the announced 2027-02-05 set, which has no printings yet). Mechanical verification, not owner approval.)*
- [ ] Publish reproducible totals for **all Scryfall set codes** and separately for **premier expansion/core sets**, plus other clearly defined product categories; never report an unqualified "total sets" figure. *(v2.40, Batch 12, [#900](https://github.com/corymstover/GrokBotMTGCompanion/pull/900), `data/set_atlas/phase1b_snapshot_gates_2026-10-30.json`: QUALIFIED: per-set totals reproduce for all 1,062 codes; 136 stays a sourced regular/mainline classification, not an all-time premier census. Mechanical verification, not owner approval.)*
- [x] Publish for **each set** all English/default-language printing records and a deduplicated card inventory, with counts for printings, unique identities, first appearances and reprints. *(v2.40, Batch 12, [#900](https://github.com/corymstover/GrokBotMTGCompanion/pull/900), `data/set_atlas/phase1b_snapshot_gates_2026-10-30.json`: PASS: per-set printing and released English-paper oracle counts match the catalog for every code (0 mismatches). Mechanical verification, not owner approval.)*
- [x] Build bidirectional searches: **set → card list/counts** and **card → first printing, all sets, chronological printing history**. Support set code, name, year, product type and date-range filters. *(v2.40, Batch 12, [#900](https://github.com/corymstover/GrokBotMTGCompanion/pull/900), `data/set_atlas/phase1b_snapshot_gates_2026-10-30.json`: PASS: sample queries replay for lea, leg, c21, pznr and ydmu. Mechanical verification, not owner approval.)*
- [ ] Verify debut/reprint attribution using dated, stable card identities; document edge cases such as promos, same-day releases, digital-first objects, variants, tokens and double-faced cards. *(v2.40, Batch 12, [#900](https://github.com/corymstover/GrokBotMTGCompanion/pull/900), `data/set_atlas/phase1b_snapshot_gates_2026-10-30.json`: QUALIFIED: 37,853 English-paper identities; 0 per-set debut mismatches; edge cases counted (4,087 same-day ties, 364 promo-only debuts, 431 earliest English-paper printings flagged reprint by Scryfall, 1,311 with no English-paper printing). Scryfall dates are not sourced street dates. Mechanical verification, not owner approval.)*
- [ ] Maintain two separately labeled timelines: **real-world set/product release chronology** and **in-universe lore chronology**; link them only with sourced claims, not assumed chronological equivalence. *(v2.40, Batch 12, [#900](https://github.com/corymstover/GrokBotMTGCompanion/pull/900), `data/set_atlas/phase1b_snapshot_gates_2026-10-30.json`: QUALIFIED: real-world chronology exists; the in-universe side is relative spans only (32 verbatim phrases, 0 AR years). Mechanical verification, not owner approval.)* *(v2.41, Batch 13, [#904](https://github.com/corymstover/GrokBotMTGCompanion/pull/904): a separate in-universe relative chronology for Packs A–C now exists, `data/lore_research/relative_chronology_2026-10-30.json`, quote-gated and with no invented years. It is still not linked to the release timeline.)*
- [ ] Connect sets to supported planes, story arcs, factions, characters, mechanics and Commander-relevant releases without inventing lore connections. *(v2.40, Batch 12, [#900](https://github.com/corymstover/GrokBotMTGCompanion/pull/900), `data/set_atlas/phase1b_snapshot_gates_2026-10-30.json`: QUALIFIED: publication-series bridge per arc; per-card canon lives in claim packs. Mechanical verification, not owner approval.)*
- [x] Add automated checks for per-set counts, uniqueness, category totals, date order, broken references, and sample queries (including Alpha, Legends, a Commander product, a promo set and a digital release). *(v2.40, Batch 12, [#900](https://github.com/corymstover/GrokBotMTGCompanion/pull/900), `data/set_atlas/phase1b_snapshot_gates_2026-10-30.json`: PASS: counts, uniqueness, totals, date order (55 codes with an earlier-dated printing, listed), references and the five sample queries, all in `--check`. Mechanical verification, not owner approval.)*
- [x] Publish a user-facing set index with an explicit snapshot date, coverage/exception report, source links and exportable English card lists; keep it maintainable as new releases arrive. *(v2.40, Batch 12, [#900](https://github.com/corymstover/GrokBotMTGCompanion/pull/900), `data/set_atlas/phase1b_snapshot_gates_2026-10-30.json`: PASS: SET_ATLAS.md carries the snapshot date, exceptions, sources and exports, plus the new Batch 12 gate section. Mechanical verification, not owner approval.)*

**Acceptance:** A user can ask "How many sets have been released?" and receive category-specific counts; request every card in any set; distinguish originals from reprints; find every set containing a card; and compare publication history with lore chronology. Counts must be reproducible from the named, verified snapshot.

## Phase 2 — Lore enrichment and primary-source integrity

- [x] Recover and strictly audit all **660** official Wizards source URLs in the original inventory.
- [x] Commit a metadata-only provenance record without republishing copyrighted article bodies.
- [x] Perform initial bounded triage of **341** uncertain name-matched character links.
- [x] Ensure future environments can reliably refetch and strictly audit official story text before using it as evidence. *(v2.73: all 660 inventoried Wizards URLs independently refetched and strictly audited; 652 exact historical extraction hashes and eight explicitly quarantined drifts, with a portable 660-page provenance regression and pinned parser dependencies. The rule is to review changed extracts before applying them as claims, never to trust them automatically. See `data/story_cache_recovery_2026-10-31.json`.)*
- [x] Review the two additional official-source leads (Koth and Wrenn) for exact printing-specific relationships. *(Done 2026-10-30, Batch 4: `scripts/build_koth_wrenn_printing_leads.py` → `data/lore_research/koth_wrenn_printing_leads_2026-10-30.json`. The review found 10 verbatim leads on cached official pages, 6 of them printing-specific, matching 13 printings. The Legends of Reality Fracture image labels give exact collector numbers: Koth, the Geomancer is FRA #248 and Koth of the Homestead is FRA #199. Art captions credit the card name and artist: Koth, Fire of Resistance is Eric Wilkerson (ONE #138, plus its promos), and Wrenn and Seven is Heonhwa Choe (MID #208 and its same-art reprints; Scryfall's credit is the shorter 'Heonhwa'). MOM Episode 8 captions separate regular-frame and borderless Wrenn and Realmbreaker (MOM #217 / #322). Koth of the Hammer is named only in the planeswalker page title, which does not identify a printing. Three 'Wrenn and Six/Seven' strings are character prose, not card references. No grades changed.)*
- [x] Investigate the enriched cards that lack a cited lore entry. *(v2.40, Batch 12, [#899](https://github.com/corymstover/GrokBotMTGCompanion/pull/899): the real pool is **2,835** cards whose Lore line reads "❓ No lore entry", not ~1,220. `scripts/build_card_lore_links.py` writes the separate overlay `data/lore_research/card_lore_links_2026-10-30.json` (card_enrichment.json untouched). Every card was examined: **205 LINKED**, conservatively graded (133 CLAIM_ANCHORED via cited claims; 47 NAMED_IN_OFFICIAL_TEXT with a verbatim ≥25-char snippet; 77 IMPLIED_SAME_SET_NAME with a limitation; 26 of these also have art credited on an official page), 1 ART_ONLY, and **2,629 NO_LORE_YET** (600 Universes Beyond, never text-matched; 2,029 with no official-text match). PRELIMINARY_RESEARCH, not owner approved.)* *(v2.41, Batch 13, [#903](https://github.com/corymstover/GrokBotMTGCompanion/pull/903): fixed a Universes Beyond detection error from #899 that had produced at least one false LINKED card (Peter Parker). The overlay now reads **208 LINKED / 1 ART_ONLY / 2,626 NO_LORE_YET** (1,304 UB; 1,322 no official-text match). A separate printed-flavor overlay, `data/lore_research/flavor_lore_links_2026-10-30.json`, grades Scryfall-printed flavor text and attributions as PRINTED_FLAVOR evidence, distinct from story claims: 23 FLAVOR_LINKED, 6 FLAVOR_NAME_ONLY, 11 FLAVOR_SPEAKER_CHARACTER, 1,282 still NO_LORE_YET.)*
- [ ] Link direct printed depictions, official story references, artwork, flavor text, characters and important events where evidence supports them. *(Partial, v2.33: `scripts/build_story_image_label_printings.py` ([PR #860](https://github.com/corymstover/GrokBotMTGCompanion/pull/860)) links 577 official story-page image labels of the form `NNNN_MTGSET_Kind: Card Name` on 57 pages to exact snapshot printings. 570 match (560 distinct printings), including 159/160 Reality Fracture labels (146 `fra`, 13 `frc`). 6 NAME_MISMATCH and 1 NO_PRINTING are recorded unresolved, not forced. A label shows which printing's art file the page used. It is not a claim about the story event the art depicts.)*
- [ ] Keep unsupported matches explicitly unresolved; track sources and reasoning for changes.
- [ ] Expand the primary-source inventory and rerun targeted reference-integrity checks.

## Phase 3 — Searchable Multiverse relationship graph

- [x] Audit existing repository entity structures before creating redundant schemas. *(v2.42, Batch 14, [#908](https://github.com/corymstover/GrokBotMTGCompanion/pull/908): read-only `scripts/audit_entity_structures.py` → `data/multiverse_audits/entity_structure_audit_2026-10-30.json` and `research/ENTITY_STRUCTURE_AUDIT_2026-10-30.md`. Graph: 4,227 nodes, 6,826 edges, 0 duplicate IDs, 0 dangling edges, 0 type mismatches; 16 orphan nodes (1 card without oracle_id, 15 literal objects); 22 cross-pack name variants; 7 undeclared subjects (C023 `urza;mishra` became a literal); 6 alias candidates; legacy crosswalk 120 bridged, 15 first-word candidates, 34 legacy-only, 10 via declared variants, 5 normalised-but-unbridged. Recommendation: keep `multiverse_graph` as the single schema; no redundant schema created. Mechanical audit, not owner approval. Follow-ups (C023 split, 5 unbridged) are listed in the audit.)*
- [x] Stabilize IDs for Character, Plane, Event, Faction, Artifact, CardRepresentation and Claim records. *(v2.46: stable `printing:<Scryfall UUID>` CardRepresentation keys now identify 560 proven printed-card versions, independently exact-joined against the historical Phase 1B printing/Oracle index; their associated card-name and Wizards art-page edges have explicit non-canon navigation tiers. Supported examples are queryable by `printing SET NUMBER`; seven unmatched labels stay unresolved. Earlier v2.43 correctly reopened this until the type/key scheme existed. **The scheme is now stable**, but mapping all ~119k historical printings into lore graphs is **not** claimed and Phase 2 card/scene depiction evidence remains open.)*
- [ ] Record directional, dated, cited relationships (e.g. allied_with, fought, created, present_at, depicted_by). (Partial: edges are directional, cited and graded, but most are not yet dated in-universe.) *(v2.38, Batch 10: `scripts/build_in_universe_dates.py` writes `data/lore_research/in_universe_dates_2026-10-30.json` (schema `in_universe_dates.v1`) and the graph builder overlays it, re-checking that each value is a verbatim phrase in a quote the claim itself cites. 29 claim edges now carry an in-universe time phrase (e.g. "more than 1,200 years", "Five years ago", "Six thousand years ago"), relative to that story's present and never converted to a calendar year. A phrase may scope its sentence rather than the relation exactly. Most edges are still undated, so this stays unchecked.)* *(v2.39, Batch 11: 32 claim edges carry a verbatim in-universe phrase (new: "over 6,000 years ago", Nahiri seals the Eldrazi; "thousands of years ago", Ob Nixilis trapped on Zendikar). Still partial.)*
  - Era labels (2026-10-30, branch `grokbot-edge-eras-20261030`): all **149/149** claim relationship edges now carry `era` (the claim pack's in-universe story-stage label) plus an `era_basis` disclaimer. **No Dominarian AR year is asserted**, because no pack quotes one. An optional `in_universe_date` is accepted only with a verbatim quote and a cited source_id; there are 0 today. This item stays open until quoted dates exist.
- [x] Separate `CANON_CONFIRMED`, `CANON_IMPLIED`, `CANON_DISPUTED`, `ALTERNATE_CONTINUITY` and hypothetical connections.
- [x] Make relationships searchable in both directions, with canonical source links.
- [x] Add duplicate, broken-link and unsupported-claim regression checks.
  - Evidence (2026-10-30): [PR #825](https://github.com/corymstover/GrokBotMTGCompanion/pull/825), [PR #826](https://github.com/corymstover/GrokBotMTGCompanion/pull/826), [PR #828](https://github.com/corymstover/GrokBotMTGCompanion/pull/828). Prefixed IDs: `character:`, `plane:`, `event:`, `faction:`, `artifact:`, `concept:`. Graded, cited edges with inverse relations. Queries in both directions via `scripts/query_multiverse_graph.py` and `scripts/mv_ask.py`. `--check` runs in CI. Still open: dates on edges and CardRepresentation nodes beyond Pack A4's printing joins.
  - v2.43 integrity follow-up: C023 `urza;mishra` is now **two** cited `discovered` relationships, with no invented composite literal. Five uniquely normalized *item* titles (Blackblade, Chain Veil, Endstone, Helvault, Temporal Anchor) now bridge to their existing artifact IDs. Updated graph/audit checks pass with zero broken endpoints or duplicate edges. The 16 orphans, six cross-pack subject declarations, 22 same-ID display-name variants and broader chronology are still tracked; do not fabricate links merely to zero those counters.

## Phase 4 — Foundational lore research packs

- [x] **Add bounded source-local event order without conflating legend, history or real-world publication dates.** *(v2.56: 24 events across Kamigawa, narrated Valley tradition and Duskmourn; 17 strict BEFORE edges and one explicitly non-transitive DURING_OR_AFTER_START relation; 37/276 source-local pairs ordered. The initial 18 quoted relations were live-checked against three official Wizards guides. **v2.63:** seven further early New Phyrexia events and six official-overview source-quoted edges raise this separate ledger to **31 events, 23 strict edges, 52/465 ordered pairs in four strands**. The 56-event Packs A–C chronology is intact. Comparisons of Mirran overwhelm vs. Venser's sacrifice and all unbridged eras remain `UNKNOWN`. L244's total/cross-plane history is unresolved; no deckbuilding gate is reopened. See `research/PHASE4_SOURCE_LOCAL_EVENT_SEQUENCES_2026-10-30.md`.)*

- [ ] **Pack A: Ugin, Nicol Bolas, Elder Dragon origins and the Elder Dragon War.** Chronology, rivalries, allies, factions, planes, cards and primary sources.
- [x] **Pack A first primary-source claim foundation (2026-10-30):** 12 explicit claim records, 13 stable entity nodes and 10 Wizards sources with narrator-perspective, original/revised Tarkir, prison/escape and Echoverse boundaries. See `research/PACK_A_Ugin_Bolas_Elder_Dragon_Duality.md` and `data/lore_research/pack_a_ugin_bolas_evidence_2026-10-30.json`. This is **partial research progress**, not the completed genealogy, card-to-canon evidence or deck.
- [x] **Pack A2 Elder Dragon War / Primeval lineage extension (2026-10-30):** 12 further graded claims, 10 entities and 8 directly checked Wizards URLs. Source comparisons correct the incomplete four-name Bolas survivor account with the separately attested Piru/Chromium pair; distinguish the *later* Dihada/Dakkon encounter and Piru's death from the ancient war; trace Crosis and Rith; and join 9 exact printed card names to the historical English-paper printing index. Source and audit: `research/PACK_A2_Elder_Dragon_War_and_Primeval_Lineages.md`, `scripts/audit_lore_pack_a_extension.py`, and `data/lore_research/pack_a_elder_dragon_war_audit_2026-10-30.json`. **No card art scenes or current Commander legality are thereby certified.**
- [x] **Pack A3 source-graded Tarkir card-art context (2026-10-30):** eight further claims, seven entities and six primary Wizards sources. [*The Reforged Chain*](https://magic.wizards.com/en/news/feature/reforged-chain-2015-01-21) explicitly captions `Crux of Fate` art at Ugin and Bolas's duel. Five more names are independently graded as time-travel mechanism, character art or tomb-site imagery, never all promoted into direct battle-scene depictions. Six exact Oracle/English-paper printing joins replay from Phase 1B, all historically within Grixis identity, but artist-to-specific-printing correspondence and current Commander rules remain unverified. See `research/PACK_A3_Tarkir_Ugin_Bolas_Story_Card_Connections.md`, `scripts/audit_lore_pack_a_scenes.py`, and its dated audit.
- [ ] Finish Pack A's disputed Elder Dragon War genealogy/participant roster, direct card representations and story-based deck candidates with Oracle/printing verification. *(v2.40, Batch 12: `research/PACK_ABC_DOSSIERS.md` lists 5 non-CONFIRMED Pack A claims, the 5 cards whose art is credited on a cited source, and 21 UNAPPROVED commander candidates with snapshot legality. The genealogy and roster disputes stay open; resolving them needs owner judgement or new sources.)* *(v2.41, Batch 13, [#905](https://github.com/corymstover/GrokBotMTGCompanion/pull/905): owner evidence matrix `research/PACK_A_GENEALOGY_DISPUTES_2026-10-30.md` / `data/lore_research/pack_a_genealogy_disputes_2026-10-30.json` covers 7 disputes with 23 verbatim, hash-checked quotes tagged by voice and stance: GD1 twin status, GD2 Elder Dragon/Ur-Dragon parentage, GD3 survivor roster A003 vs A018, GD4 Vaevictis descendants, GD5 Piru/Chromium/Crosis, GD6 Rith/Palladia-Mors/Darigaaz, GD7 Chromium banished vs murdered. Only GD1 has an official statement that answers it (Wizards editorial plus third-person narration call them twins; Bolas's denial is in-story and ambiguous). No grade was changed. Owner-decision cells are blank.)*
- [ ] **Pack B: Thran civilization → Yawgmoth → Old Phyrexia → Brothers' War.** People, artifacts, conflicts and consequences.
- [ ] **Pack C: Dominaria → Weatherlight → the Legacy → Phyrexian invasion.** Historical transitions and connections.
- [x] **Pack C5 targeted editorial outcome audit (2026-10-30):** Two source-graded claims were independently checked against [Wizards' *The Known Mutliverse* recap](https://magic.wizards.com/en/news/feature/known-mutliverse-2008-03-19). It credits the Weatherlight crew/Legacy with Yawgmoth's destruction and unnamed planeswalkers' soul bombs with Old Phyrexia's decimation. The two outcomes remain **unordered** by that article and other killer-attribution sources remain independently graded; this does not complete the full Pack C chronology. `scripts/audit_lore_pack_c5.py --check` (offline), `--live` (Wizards direct), `research/PACK_C5_PHYREXIAN_INVASION_OUTCOME_2026-10-30.md`. Research PRELIMINARY, not owner approved.
- [x] **Pack B v1 (2026-10-30, [PR #826](https://github.com/corymstover/GrokBotMTGCompanion/pull/826)):** 18 claims, 23 entities, 8 Wizards sources. PRELIMINARY_RESEARCH. Next: per-claim card anchors and the Brothers' War story episodes.
- [x] **Pack C v1 (2026-10-30, [PR #828](https://github.com/corymstover/GrokBotMTGCompanion/pull/828)):** 28 claims, 26 entities, 6 Wizards sources. PRELIMINARY_RESEARCH. Next: *Return to Dominaria* episode extraction, March of the Machine, and card anchors.
- [x] **Pack C2 *Return to Dominaria* extraction (2026-10-30, targeted, not exhaustive):** 39 claims with verbatim quotes from the 12 official episodes. The graph now has 605 nodes and 904 edges, and card-name anchors cover 62 entities. No in-universe AR dates appear in these episodes, so none were inferred. Still open: an exhaustive pass, March of the Machine, and claim-level card anchors.
- [x] **Pack C3 *Assault on New Phyrexia* extraction (2026-10-30, targeted, not exhaustive):** 19 claims quoted verbatim from the 5 official episodes (stage `one_strike_2023`). The graph now has 841 nodes and 1,330 edges. Card-name anchors cover 75 entities. No AR dates are quoted, so none were inferred. Still open: March of the Machine, an exhaustive pass, and claim-level card anchors.
- [x] **Pack C4 *March of the Machine* extraction (2026-10-30, targeted, not exhaustive):** 21 claims quoted verbatim from the 10 official main-story episodes (stage `mom_invasion_2023`); every episode is cited. The graph now has 911 nodes and 1,444 edges, and card-name anchors cover 81 entities. No AR dates are quoted, so none were inferred. Still open: side stories, an exhaustive pass, and claim-level card anchors.
- [x] **Claim-level card anchors (2026-10-30, mechanical, Batch 4):** `scripts/build_claim_card_anchors.py` writes `data/lore_research/claim_card_anchors_2026-10-30.json`, which ties 155 of 173 claims to 884 claim-card pairs across all 9 claim packs. Each pair gets one tier. **ART_IN_CITED_SOURCE** (25 pairs): the card's art is credited by exact name on an official page the claim cites. **PRINTED_IN_STORY_SET** (33 pairs): the card has a paper printing in the story's set; this tier applies only to C2→DOM, C3→ONE and C4→MOM. **NAMED_PARTICIPANT** (826 pairs): everything else. An anchor never says a card depicts the claimed event. C3 and C4 have no art-tier pairs yet, because the caption atlas has no card-credited art captions for those episodes.
- [ ] For each pack, publish a verified chronology, relationship map, source bibliography, explicit uncertainties and lore-deck candidates. *(v2.40, Batch 12, [#901](https://github.com/corymstover/GrokBotMTGCompanion/pull/901): `scripts/build_pack_dossiers.py` publishes, for each of Packs A (48 claims), B (18) and C (107): a relationship map, a bibliography, uncertainties, card representations and UNAPPROVED commander candidates (A 21, B 26, C 68). It also flags the one cross-pack citation (C012→Pack B `urza_profile`). Stays unchecked: stages are in **publication order**, not a verified in-universe chronology, and no candidate is an approved deck.)* *(v2.41, Batch 13, [#904](https://github.com/corymstover/GrokBotMTGCompanion/pull/904): `scripts/build_relative_chronology.py` writes `data/lore_research/relative_chronology_2026-10-30.json` and `research/RELATIVE_CHRONOLOGY_2026-10-30.md`, a partial order built **only** from orderings stated verbatim on cached official Wizards pages. Inputs are before/after statements, spans relative to each page's own story present, and the AR scene headers printed in *The Brothers' War* (e.g. 63 AR, 4562 AR). It has 42 events, 14 story presents (never merged), 47 stated edges, 6 edges derived only from printed AR labels, 0 cycles, and 155 of 1,946 pairs ordered across 12 disconnected chains. Claims placed: A 15/48, B 7/18, C 10/107. **Not enough to close L244.** `l244_closure.missing` records the gaps: story presents on different pages are not anchored to each other; Pack A primordial, Meditation Realm, WAR and TDM claims lack ordering quotes; spans are open-ended; Eldrazi spans conflict (5,000 vs >6,000 years); Pack B has Thran/Yawgmoth/Mishra gaps; C2–C4 have no AR dates and the Weatherlight Saga novels are not ingested; 7 source pages are uncached.)* *(v2.42, Batch 14, [#909](https://github.com/corymstover/GrokBotMTGCompanion/pull/909): the 10 official pages cited by packs but missing from the cache were fetched (metadata-only provenance in `data/lore_research/pack_source_cache_provenance_2026-10-30.json`; bodies stay in the untracked cache). New stated orderings from *The Reforged Chain*, the BRO product page and official summary pages (*The Known Multiverse* 2008, Commander Legends and MH2 legend bios, RTD ep3, *Death and Salvation*). No novel text was ingested. Chronology now: 56 events, 16 presents, 63 stated edges, 177/3,074 pairs ordered, 13 components; the Eldrazi and Tarkir chains merged (18 nodes) and the Weatherlight chain joined the Elder-Dragon/Invasion component. **Still not closed:** presents remain unanchored across pages; the Weatherlight-novel ordering of Yawgmoth's end and Old Phyrexia's decimation is a BLOCKER until an official recap states it.)*

## Phase 5 — Full-history and plane-by-plane expansion

- [x] **Surface existing official on-plane story evidence in plane-history queries without fabricating direct plane edges.** *(v2.58: 53 carefully selected, original-source-cited claims from Eldraine (10), Strixhaven on Arcavios (16), New Capenna (15) and Lorwyn–Shadowmoor (12), each separately marked CONTEXTUAL rather than counted as a newly researched or direct plane claim. New Arcavios geography bridge checked live from Wizards; off-plane and ambiguous cases excluded; eight tests plus inherited source-pipeline checks. Direct plane metrics stay 183 edges and 16 thin dossiers; comprehensive history remains unchecked.)*
- [x] **Research Bloomburrow's Valley origins with legendary-status boundaries.** *(v2.55: 13 source-checked claims on the Order of the Holly Leaf, Calamity era, War of Cinders, Lily's Seed Flame, weaving's aftermath, five Valley biomes and settlement governance. Legendary historical narrative remains CANON_IMPLIED, and Valley is not equated with the entire plane.)*
- [x] **Research Duskmourn's lost original plane and the House's growth.** *(v2.55: 12 source-checked claims on forgotten plane name, pre-Ascension realms, Marina, Valgavoth, the House's expansion, five zones and the Harrowing/Quiescence cycle. Advanced ancient civilization is evidence-inferred; no claim that rumors of an exit are proven.)*
- [x] **Trace Kamigawa's historical transformation using two Wizards sources.** *(v2.54: 12 quoted primary-source claims distinguish the material/spirit worlds, Kami War, Kyodai and Michiko's victory, merger sites, Imperial administration and Futurists; the relative 1,200-year marker is kept verbatim and unconverted. Direct plane claims now eight, not an exhaustive timeline.)*
- [x] **Trace Mirrodin's conversion into early New Phyrexia without present-day regime assumptions.** *(v2.54: 8 primary-source claims on abductions, Karn's oil, infection, Mirran resistance and early praetor factions; direct New Phyrexia claims now nine. Present tense in its undated overview is a historical profile, not a post-*March of the Machine* fact.)*
- [x] **Ask cited plane-history questions through the main Q&A interface.** *(v2.52: `mv_ask.py ask 'What is the history of Theros?'` returns source URLs, original grades, limitations and distinct claims/relations from the 33 current registered plane dossiers, always QUALIFIED, never a full-history or total-chronology assertion. Regression tests cover no-source names, multi-target claims and old Phyrexia's unresolved accounts.)*
- [x] **Deepen Theros's plane history using its official Wizards primer.** *(v2.51: 10 new live-quote-verified claims covering gods, three named poleis, ecological perils, civic ideals and Akros's outpost defenses; existing TS037 and source ID ths_plane preserved. Theros direct claims 3→6; v2.52 corrects the earlier prose-only miscount. This does not verify all gods, myths, poleis or the in-world timeline; exhaustive history remains OPEN.)*
- [x] **Deepen Alara's plane history using the official Wizards primer.** *(v2.50: 10 live-quote-verified, source-graded claims on five shards, convergence, mana environment and the factions' differing conflicts; source register reused, with no duplicate official source node or existing UP001 Bolas claim. Alara now has 5 directly incident distinct claims, but an exhaustive history, specific battle participants and cross-era dates remain OPEN.)*
- [x] **Publish a source-backed, explicitly partial plane-history query layer.** *(v2.49: 33 graph-registered plane dossiers, 147 direct claim-edge incidences, each fact retaining official URL, grade, limitations and optional quoted date. `scripts/query_plane_history.py` supports text/JSON; `scripts/build_plane_history_dossiers.py --check` and dedicated tests enforce provenance and no inferred chronology. 22 dossiers remain thin, so exhaustive plane history, L244 and contradiction reconciliation are **not** closed.)*

- [ ] Expand the Mending, major planeswalkers and the Gatewatch.
- [ ] Expand Bolas's schemes and the War of the Spark. *(Partial, 2026-10-30 Batch 5: a reusable bulk claim-pack pipeline, `scripts/story_claim_pipeline.py`, builds packs from one spec file each in `data/lore_research/claim_specs/`. It gates every quote verbatim (whitespace-normalized) against the cached official page, enforces the closed grade set and requires a limitation for any non-CONFIRMED claim. It also checks that every page is a Wizards page tagged with the spec's arc, and writes a self-hashed audit. CI runs `story_claim_pipeline.py check`, which rebuilds each pack from its spec and verifies the quote hashes without the cache. Three PRELIMINARY_RESEARCH packs were added: KLD/AER, 25 claims (Pia, Baral, Tezzeret, the Planar Bridge, Ajani joining the Gatewatch); XLN/RIX, 16 claims (Azor's Immortal Sun built to imprison Bolas, Bolas hiring Vraska, Huatli meeting Saheeli); and AKH/HOU, 17 claims (the God-Pharaoh, Liliana killing Razaketh, the Gatewatch's defeat, Bolas taking the Planar Bridge). In total: 58 claims, 75/75 quotes verbatim, 31 official pages. Non-canon Rivals alternate endings are graded ALTERNATE_CONTINUITY. Targeted extraction, not exhaustive, and not owner approved. **v2.33:** a fourth pack, NEO (Kamigawa: Neon Dynasty), adds 12 claims with 19/19 quotes verbatim from 6 official pages ([PR #861](https://github.com/corymstover/GrokBotMTGCompanion/pull/861)). It covers the Wanderer being the Emperor, Tezzeret's Reality Chip igniting her spark, Kaito and his sister Eiko, Tezzeret abducting Tamiyo, and Jin-Gitaxias compleating her. 9 claims are CONFIRMED and 3 IMPLIED, each IMPLIED claim with a limitation. Status: PRELIMINARY_RESEARCH.)*
- [ ] Expand Mirrodin/New Phyrexia and March of the Machine. *(Partial: targeted Packs C3 and C4 cover the main-story episodes; side stories and an exhaustive pass are still open, so this stays unchecked.)*
- [ ] Expand Omenpaths and later canonical stories. *(Partial, v2.34, 2026-10-30 Batch 6: PRELIMINARY_RESEARCH claim packs through `scripts/story_claim_pipeline.py` now cover all 33 inventory arcs at least in part — MID/VOW, SNC, EOE ([#863](https://github.com/corymstover/GrokBotMTGCompanion/pull/863)); RF, WOE, MKM ([#864](https://github.com/corymstover/GrokBotMTGCompanion/pull/864)); BLB, DSK, OTJ, LCI, DFT ([#865](https://github.com/corymstover/GrokBotMTGCompanion/pull/865)); KHM, STX, IKO ([#867](https://github.com/corymstover/GrokBotMTGCompanion/pull/867)); THB, THS, MAT, ELD ([#868](https://github.com/corymstover/GrokBotMTGCompanion/pull/868)); SOS, SOI/EMN ([#869](https://github.com/corymstover/GrokBotMTGCompanion/pull/869)). Generator scripts live in `scripts/claim_spec_sources/` with `rebuild.sh`. Coverage: 195/626 pages cited, 0 arcs not started, 26 partial, 7 complete; 501 graph claims.  v2.35, Batch 7: bulk fills and new packs ([#871](https://github.com/corymstover/GrokBotMTGCompanion/pull/871)), 78 untagged pages triaged into arcs plus side-story packs ([#872](https://github.com/corymstover/GrokBotMTGCompanion/pull/872)), and BFZ/OGW, DMU, NEO, DSK, MKM, MOM closed ([#873](https://github.com/corymstover/GrokBotMTGCompanion/pull/873)); every pack now has a generating spec script with a byte-for-byte regeneration test. Coverage: 350/626 pages cited, 0 arcs not started, 13 partial, 20 all pages cited; 711 graph claims; 628/711 claims card-anchored. **v2.36, Batch 8:** LCI, BLB, THB, KLD/AER, DFT, XLN/RIX, DOM/WAR (new `pack_p5_war_spark_ravnica`) closed ([#875](https://github.com/corymstover/GrokBotMTGCompanion/pull/875)); KHM, STX ([#876](https://github.com/corymstover/GrokBotMTGCompanion/pull/876)); MID/VOW, THS ([#877](https://github.com/corymstover/GrokBotMTGCompanion/pull/877)). Coverage: 414/626 pages cited, 31 of 33 arcs with every page cited (still partial: IKO 1/3, whose 2 uncited pages have no lore content, and untagged 17/227); 838 graph claims. **v2.37, Batch 9:** untagged packs: bios and planes ([#883](https://github.com/corymstover/GrokBotMTGCompanion/pull/883)) and Tarkir 2014–2015 plus the Chronicle of Bolas ([#885](https://github.com/corymstover/GrokBotMTGCompanion/pull/885)). The reviewed_no_claim register now holds 36 pages (IKO's 2 pages, [#881](https://github.com/corymstover/GrokBotMTGCompanion/pull/881); 34 untagged pages, [#883](https://github.com/corymstover/GrokBotMTGCompanion/pull/883)). Coverage: 466/626 pages cited, 36 reviewed with no claim, 31 of 33 arcs with every page cited, 32 of 33 cited or reviewed; untagged 69 cited + 34 reviewed of 227; 939 graph claims. Targeted, not exhaustive, not owner approved, so this stays unchecked. **v2.38, Batch 10:** untagged packs ZNR 2020, NPH guides, ISD guides, Conspiracy 2016 ([#889](https://github.com/corymstover/GrokBotMTGCompanion/pull/889), [#890](https://github.com/corymstover/GrokBotMTGCompanion/pull/890)), ORI 2015 and GRN/RNA ([#891](https://github.com/corymstover/GrokBotMTGCompanion/pull/891)), misc 2015–2019 ([#892](https://github.com/corymstover/GrokBotMTGCompanion/pull/892)), 2012–2013 Planeswalker's Guides and 2007 Maelstrom/Torrent ([#893](https://github.com/corymstover/GrokBotMTGCompanion/pull/893)). Coverage: 516/626 pages cited, 40 reviewed with no claim; untagged 119 cited + 38 reviewed of 227 (70 unread); 1,027 graph claims.)*
- [ ] Audit major planes, regions, factions, artifacts and overlooked characters. *(Partial v2.59: character and faction history questions can now retrieve the existing **direct** claim edges for 623 of 628 registered Character/Faction nodes, with citations, grades and no inferred chronology. This is not an exhaustive source-by-source audit or a complete biography; see `research/PHASE5_CHARACTER_FACTION_HISTORY_LOOKUP_2026-10-30.md`.)*
- [ ] Connect cross-plane histories and document contradictions/retcons. *(Partial, v2.38, Batch 10: `mv_ask` continuity route ("explain the continuity of X", "is X canon / a retcon", "conflicting accounts of X") lists every cited CANON_DISPUTED, ALTERNATE_CONTINUITY and OPEN_QUESTION claim and any claim whose limitation names a retcon, timeline rewrite or conflicting account, each with its sources and why it is listed; it never resolves them. Limited to what the packs cite, so this stays unchecked.)* *(v2.39, Batch 11: leader questions union `led`/`leader_of` ([#895](https://github.com/corymstover/GrokBotMTGCompanion/pull/895)); past-era Tarkir leaders tagged "Tarkir's past". Still partial.)*
- [ ] Use the Phase 1B Set & Printing Atlas to navigate published sets and storylines while keeping real-world release dates separate from in-universe event order.
- [ ] Maintain an explicit coverage/gaps inventory as new sets and stories arrive. *(Started 2026-10-30, Batch 4: `scripts/build_story_coverage_inventory.py` generates `data/lore_research/story_coverage_inventory_2026-10-30.json` from the 626-page `primary_sources.csv` and the 9 graph claim packs, and CI rebuilds and compares it. Claim packs cite 57 of the 626 pages. Of the 33 arc buckets, 1 has every page cited (ONE, 6/6), 9 are partial (MOM 10/11, DOM/WAR 12/18, BRO 4/10, BFZ/OGW 3/19, TDM 2/14, SOI/EMN 1/21, DMU 1/6, ECL 1/12, untagged 17/305) and 23 are not started, including KLD/AER, AKH/HOU, XLN/RIX, EOE and RF. "Cited" means the page is used at least once, not that it was read exhaustively. The box stays unchecked because the inventory still has to be refreshed when new stories arrive. **Batch 5 refresh:** 12 claim packs and 231 claims now cite 88 of the 626 pages. 1 arc is fully cited, 12 are partial (now including KLD/AER 14/17, XLN/RIX 10/17 and AKH/HOU 7/16), and 20 are not started. **v2.33 (after NEO):** 13 packs and 243 claims cite 94 of 626 pages. 2 arcs are fully cited, 12 partial and 19 not started. **v2.38, Batch 10 refresh:** 516/626 pages cited, 40 reviewed with no claim, 31 of 33 arcs fully cited; untagged 119 + 38 reviewed of 227.)* *(v2.39, Batch 11: **626/626 pages cited or reviewed** (576 cited, 50 reviewed with no claim, 0 unread); all 33 arcs cited-or-reviewed; 1,139 claims. Stays unchecked: upkeep is ongoing as new stories arrive.)*

## Phase 6 — Lore-first Commander deckbuilding engine (DEFERRED UNTIL FOUNDATION CERTIFICATION)

**Execution hold (v2.53):** The engineering infrastructure and three unapproved
pilot proposals are retained as historical evidence, not active work. Do not
construct, refine, request approval for, or certify lore decks while Phases
1/1B–5, 7 and the Phase 8 knowledge-foundation release are unfinished. Do not
interpret the checked pilot-subtask boxes below as owner approval. This phase
resumes only after the foundation release is independently certified (or Cory
explicitly lifts the hold).

- [ ] Retrieve lore-relevant cards with grades: direct depiction, canon reference, lore-inspired, mechanical stand-in.
- [ ] Compare eligible commander choices with verified color identity and relevant story context.
- [ ] Build mechanically coherent, realistic-power Commander strategies around the narrative.
- [ ] Support optional set/era/first-printed-in restrictions using verified Phase 1B data without confusing reprints with original debuts.
- [ ] Verify each final 100-card list, singleton restrictions, relevant rules/combinations, legality and current bracket.
- [ ] Provide three Archidekt tags and one clean commander-first `1x Name` import list.
- [ ] Pilot 1: **Ugin & Nicol Bolas — Elder Dragon Duality**. Owner approval is pending, so the box stays unchecked until Cory approves.
  - [x] Complete, verified 100-card proposal (2026-10-30, [PR #823](https://github.com/corymstover/GrokBotMTGCompanion/pull/823)). Every card is graded, and three Archidekt tags plus a commander-first import list are provided. A scripted builder (`scripts/build_ugin_bolas_duality_pilot.py`) reads printings from `snap-20261029-40848334824-1`, never from the Grixis lock. The offline audit and tests run in `phase6-pilot1-ugin-bolas-duality.yml`. Status: **UNAPPROVED**.
- [ ] Pilot 2: **Original Primeval Dragons**.
  - [x] Complete, verified 100-card proposal (2026-10-30, [PR #832](https://github.com/corymstover/GrokBotMTGCompanion/pull/832)). The commander is The Ur-Dragon, as a thematic progenitor graded LORE_INSPIRED. It was built with the generic `scripts/build_lore_pilot.py` and audited offline. Tiers: 35 CANON_REFERENCE, 12 LORE_INSPIRED, 38 MECHANICAL_SYMBOL, 15 basics. Status: **UNAPPROVED**.
- [ ] Pilot 3: **Ugin's Allies and Heroes**.
  - [x] Claim research, Pack A5 (2026-10-30): 16 verbatim-quoted claims. Audit: `scripts/audit_lore_pack_a5.py --check`. Next: War of the Spark ally evidence (Kaya, Teyo).
  - [x] Complete, verified 100-card proposal (2026-10-30, [PR #844](https://github.com/corymstover/GrokBotMTGCompanion/pull/844), merge `0344cd53`). The commander is Jace, Multiverse Architect (WUBR, "can be your commander"; the CR 903.3a check passes). Built with `scripts/build_lore_pilot.py` from Pack A5 and the caption atlas. Tiers: 15 CANON_REFERENCE (each cites a CANON_CONFIRMED A5 claim), 32 LORE_INSPIRED (caption-atlas art from the cited stories, plus Elspeth, whose U016 claim is only implied), 40 MECHANICAL_SYMBOL, 13 basics, 0 Game Changers. `tests/test_pilot3_ugins_allies.py` checks every caption statement against the atlas. Status: **UNAPPROVED**.
- [ ] Preserve the original approved 62 decks; a new pilot never overwrites them.

## Phase 7 — Ultimate MTG question-answering companion

- [x] **Answer bounded two-event chronology questions through the main natural-language Q&A interface.** *(v2.57: `mv_ask.py ask` compares recognized event label fragments through v2.56's cited source-local and Packs A–C event orders, returns yes/no/first-event only when justified by strict BEFORE/AFTER evidence, and reports UNKNOWN or unresolved ambiguity without guessing. Explicit flags preserve narrated legends, overlapping war events, and unrelated/unaligned eras. Nine dedicated regressions; not a total chronology or comprehensive open-domain Q&A solution.)*
- [x] **Support bounded, evidence-qualified lookups for card names, Oracle text, types, identities, keyword mechanics, printings and published rulings.** *(v2.62: `mv_ask.py` combines the existing card lookup with v2.61's complete historical printing route and the dated 2026-10-15 published-ruling/official 2026-09-25 keyword-rule excerpt. It answers card rulings, 701/702 keyword definitions, and evidence-backed two-card interaction questions with direct source URLs and negative-case qualifiers. It is **not** a comprehensive mechanics interpreter, current live ruling sync, or game simulator. The lookup capability is verified; more advanced interaction research remains open.)*
- [x] **Answer bounded set and printing questions with category-qualified totals, full set card lists, printing/debut/reprint distinctions and cited snapshot dates from Phase 1B.** *(v2.61: the normal `mv_ask.py ask` entry point serves the frozen 2026-10-29 historical shard index with the exact 1,062-code category breakdown, full per-set English-paper card lists and debut/reprint classes, and printing-ID-level histories. It explicitly marks 136 regular/mainline codes as a scoped research classification, not an official all-time premier count; qualifying flags preserve source-bulk absence and release-date versus lore-date separation. Nine focused regressions. Broader questions and source-level replay remain open.)*
- [ ] Answer obscure lore and chronology questions through cited evidence and dated canon status.
- [x] Explain ambiguous/retconned narratives rather than inventing certainty. *(v2.37, Batch 9: leader answers order cited leaders by the citing page's publication date. Claims whose summary or limitation sets them in a past era or an original or rewritten timeline are now kept as era context and never reported as the most recent leader. The answer carries the flag `ERA_OR_TIMELINE_CONTEXT` and an `era_note` saying that publication order is not in-universe order and that the cited claims do not by themselves establish the present-day leader. For example, Yasova, Tasigur, Alesha and Daghatar are Fate Reforged past-era khans; they are era context behind Surrak, Sidisi, Zurgo and Anafenza. Covered by `tests/test_batch_recount_b9.py`. There is no general retcon explainer beyond leadership yet. **v2.38, Batch 10:** a general continuity explainer (`continuity()` in `mv_ask`, route `ask->continuity`, `tests/test_mv_ask_continuity.py`) returns the conflicting or alternate cited accounts with `QUALIFIED` confidence and a "not resolved" note, or `NO_CITED_CONTINUITY_CONFLICT`. Checked as a capability; its answers are only as complete as the cited packs.)*
- [ ] Integrate card, lore and rules search for difficult research questions; defer deck recommendations and deckbuilding flows until post-foundation Phase 6.
- [ ] Test difficult representative queries, cross-references, and interaction explanations. *(Partial, 2026-10-30 Batch 4: `mv_ask` now answers "who killed X" using the `killed` relation, plus "who is X's mother" and "who struck down X". All three are covered by Pack C4 regression tests, for example Karn → Elesh Norn (MOM017) and Tamiyo → Nashi (MOM010). Unknown names still return NOT_FOUND. A broad hard-query suite is still open. **v2.33:** `tests/test_mv_ask_relations.py` ([PR #859](https://github.com/corymstover/GrokBotMTGCompanion/pull/859)) is data-driven. Every claim edge in the graph must round-trip through `mv_ask` lore with its grade and source URL, confidence must never overstate the grade, and non-CONFIRMED P5 claims must carry limitations. It also checks natural-language questions (Razaketh, the Immortal Sun, Ugin, Heart of Kiran). The router gained `created ← designed/invented` and `defeated_by ← defeated` fallbacks. A broader free-text paraphrase suite is still open, so this box stays unchecked. **v2.36, Batch 8:** `tests/test_mv_ask_rephrased_b8.py` adds 27 cases / 42 phrasings over the Batch 7/8 relations (22 VERIFIED, 5 QUALIFIED CANON_IMPLIED cases that must carry a limitation), and the router gained honest phrasings for "beheaded", "the leader of X", "governs/rules", "mentored"/"X's mentor", "founded", "guards", "fought", "serves", "worships", "attacked", "who did X meet", and friend_of for "X's friends". Unknown entities still return NOT_FOUND. Known gap: faction short names such as "the Izzet" do not resolve. **v2.37, Batch 9:** faction short names now resolve, for example "the Izzet" and "the Temur" ([#882](https://github.com/corymstover/GrokBotMTGCompanion/pull/882), flag `MATCHED_BY_FACTION_ALIAS`). Sibling questions read `sibling_of|twin_sibling_of` together, so Ugin's cited siblings no longer hide the Bolas twin edge ([#885](https://github.com/corymstover/GrokBotMTGCompanion/pull/885)). A 13-question representative set runs in CI through `scripts/batch_recount.py`. Still not a broad hard-query suite, so the box stays unchecked.)* *(v2.42, Batch 14, [#910](https://github.com/corymstover/GrokBotMTGCompanion/pull/910): a probe over all 54 factions with cited leaders found 'guildmaster of', 'in charge of', "who's the leader of" and 'commands' missed 54/54; now 0 misses over 14 phrasings, except 3 factions (dragonlords, Elves of Eldraine, the Twelve) whose only leader edges point outward, which correctly stay NOT_FOUND. `tests/test_mv_ask_leader_phrasings_b14.py`. Still not a broad hard-query suite.)*
- [x] Flag unavailable, stale or low-confidence information explicitly. `mv_ask` returns VERIFIED, QUALIFIED or NOT_FOUND with flags and exits 3 for unknown entities ([PR #827](https://github.com/corymstover/GrokBotMTGCompanion/pull/827), [PR #829](https://github.com/corymstover/GrokBotMTGCompanion/pull/829)).
  - v2.43 correction: confidence now also reflects original/rewritten timeline limits (`TIMELINE_CONTEXT_REQUIRED`), a cited death of a nominally most-recent leader (`LATEST_CITED_LEADER_DEATH_RECORDED`), and present-tense leader requests (`CURRENT_LEADER_NOT_ESTABLISHED`). Verified examples: original-timeline Ugin death and Teysa's confirmed murder. `most_recent_cited` stays explicitly historical, never an unsupported current-office assertion. Regression tests cover all three; broader currentness and timeline verification is still open.

## Phase 8 — Release quality and continuing upkeep

- [ ] Keep targeted CI checks for card counts, source integrity, graph relationships, rules/Q&A and set data; preserve existing deck-legality regression checks without starting new decks.
  - Partial (2026-10-30): claim-graph, companion-ask, oracle-drift and release-readiness workflows were added, alongside the existing focused-validation and pilot audits.
- [ ] Monitor new official stories, Oracle changes, releases, rules and Commander format updates.
  - Partial (2026-10-30): `scripts/oracle_drift_report.py` ([PR #829](https://github.com/corymstover/GrokBotMTGCompanion/pull/829)) diffs the Oracle text against each new snapshot.
  - v2.47 read-only monitoring: `.github/workflows/multiverse-update-watch.yml` executes weekly/on demand, validates its source whitelist and saved current baseline, checks new URLs from Wizards' present Magic Story listing, compares Scryfall bulk *metadata* against the exact pinned active snapshot, and checks whether the Wizards rules hub references a new Comprehensive Rules PDF. The Commander page ETag is informational only because it varies with deployments. The output is an ephemeral review artifact, not automatic source ingestion or a verified rules change. This **remains open** until broader sources, release-time verification and curated update decisions are covered.
  - v2.60 dry-run correction: a weekly monitor **already exists**; it is not an unscheduled engineering gap. The ongoing coverage limits and mandatory human review remain explicit.
- [ ] Rebuild and reconcile the Phase 1B set catalog and bidirectional printing lookups when new sets or printings appear, retaining historical snapshots.
  - v2.43: `scripts/audit_phase1b_snapshot_gates.py` selects exactly the SHA-pinned 2026-10-29 `default-cards` filename from the committed manifest. A missing archive now returns `MTG_PINNED_BULK_MISSING` with its expected SHA and source URL rather than `IndexError` or an accidental newest-bulk substitution. The complete source-level gate is still blocked in a clean clone until those exact bytes are available; the saved dated report stays qualified.
- [x] Update snapshot manifests with actual download bytes and stable hashes. *(v2.72: the original Oct 28 source is now hash-recovered and measured at **80,216,061 compressed bytes**, matching its pre-existing SHA-256. The three original Oct 15–16 locked files and all three active Oct 29 Companion archives also have independently matched bytes and SHA-256, preserved in `data/scryfall_snapshots/historical_bulk_replay_2026-10-31.json` alongside the existing October 29 release manifest. The historical export manifest's deterministic schema stays unchanged.)*
- [x] Maintain an honest progress tracker: completed, under review, blocked, and not started. *(v2.73: a deterministic all-137 task triage documents each open item's source/owner/engineering/ongoing blocker; the checkpoint separately lists 14 foundation release/Phase 8 gates, keeps Phase 6 deferred, and fails CI when either report is stale.)*
  - v2.43 partial: `scripts/update_multiverse_progress_tracker.py` now generates/checks a *current* 2026-10-30 status block at the top of `Progress Tracker.md` from the live Master Workflow, graph, enrichment and recount. Old cycle-36 data remains explicitly historical. The full task-state dashboard (under review/blocked/not started for every item) is still to be built, so this high-level box stays unchecked.
  - v2.60: the current tracker adds a generated four-state **14-gate foundation-release** triage from the dry-run's typed blockers. This does not pretend to classify all 137 engineering tasks or accept continuing maintenance; the broader all-item dashboard remains an open improvement.
- [ ] Define an MTG Multiverse Companion milestone release based on verified features, not an arbitrary percentage of all lore. *(v2.42, Batch 14, [#911](https://github.com/corymstover/GrokBotMTGCompanion/pull/911): certification-checklist dry run `scripts/certification_dry_run.py` → `data/release/certification_dry_run_2026-10-30.json` / `research/CERTIFICATION_DRY_RUN_2026-10-30.md` lists the typed blockers for each release criterion and Phase 8 item (OWNER_APPROVAL 3, OWNER_DECISION 5, EXTERNAL_CI 3, MISSING_SOURCE 2, ENGINEERING_OPEN 4, ONGOING 4). It certifies nothing; accepting the definition is the owner's call.)*
  - Partial (2026-10-30): `scripts/release_readiness.py` ([PR #830](https://github.com/corymstover/GrokBotMTGCompanion/pull/830)) scores each written criterion from committed evidence. Current verdict: NOT_RELEASE_READY.
  - v2.60: a source-graded, 12-case knowledge-only review packet was generated and CI-gated; v2.62 extended it to 15 dated set/printing/ruling cases, v2.63 to 17 with bounded New Phyrexia chronology, v2.64 to 22 with five character/faction histories, **v2.65 to 26** with four newly deepened plane histories, and **v2.66 to 30 unique questions** for four more plane histories and a duplicate-ID correction. The dry-run distinguishes this **completed engineering packet** from pending exact-head release CI and Cory's foundation-scope decision. No release checklist acceptance is inferred.
- [ ] Treat continual future MTG releases as an ongoing maintenance track rather than a permanently finishable backlog.

## Immediate execution queue — v2.66 FOUNDATION FIRST (2026-10-31)

1. **Phase 4 — Verified in-universe chronology:** expand the source-quoted BEFORE/AFTER/UNKNOWN event order, resolve high-value L244 gaps where primary evidence exists, and retain unknown/disputed ordering instead of inventing total dates. Keep release chronology separate.
2. **Phases 2/5 — Comprehensive history:** systematically deepen thin plane dossiers, major factions, characters, wars, artifacts and cross-plane consequences; record both coverage and missing primary sources. Currently thin registered planes remain a priority, not a census of all planes; regenerate the exact count from the dossier rather than treating this prose as a live counter.
3. **Phase 3 — Evidence-safe knowledge graph:** resolve or explicitly qualify orphan nodes, cross-pack aliases, identity/printing links and undated relations. Never merge identities or promote card art/name matches without evidence.
4. **Phase 7 — Advanced Q&A and rules:** expand the new bounded set/printing route to nuanced multi-hop questions, chronology, contradictions, leaders and rules interactions with citations, confidence limits, negative cases and currentness safeguards. No new deckbuilding tests are required here.
5. **Phases 1B/2 — Reproducibility and source integrity:** keep exact snapshot hashes, authoritative story quotations, per-set data and generated indexes testable. Recover original pinned bulk only by hash; do not alter historical Grixis locks. Treat the optional 555-product source queue as nonblocking unless it becomes material to an active knowledge gate.
6. **Phase 8 — Maintenance and focused CI:** synchronize the generated Progress Tracker, monitor newly released official material, run targeted and exact-head checks, and audit actual gaps without calling a static knowledge snapshot permanently exhaustive.
7. **Foundation-only release decision:** independently review chronology/history coverage, graph/search integrity, Q&A/rules, snapshots, known limitations, owner research decisions and protection of the 62 Grixis lists. Release readiness remains **NOT_RELEASE_READY** until its actual gates pass; no deck pilot approval may block this release.
8. **Phase 6 — PARKED:** preserve the existing three **UNAPPROVED** lore-first pilots, tools and notes without working on, approving or refining them. Resume meaningful deck creation **only after** the foundation is certified, unless Cory explicitly changes this direction.

## Archived execution queue — historical batches (not current instructions)

1. **Phase 8 priority pool complete (batch 38, 2026-10-30):** 5,362/5,362 records. Next: deepen lore links for the 1,289 batch-38 records marked "no lore entry linked yet", using official story evidence only.
2. **Index exclusions — completed for the October 29 snapshot:** retain the verified 5,270-record classification and review the 305 future-dated IDs after release, rather than prematurely importing them.
3. **Phase 1B qualified functional release — complete for its stated scope:** full **1,062-set printing/unique-card CSV/JSON exports**, **119,509 exact bidirectional historical printing joins**, **106,855** released English-paper printing-count parity, evidence-qualified category labels, and 12 exact-title official story-series links are published and verified post-merge ([PR #818](https://github.com/corymstover/GrokBotMTGCompanion/pull/818), six green CI checks). Stronger original-bulk/cross-snapshot ID parity and a universal Wizards premier count remain **explicitly uncertified**, optional future upgrades. **293 sourced / 555 source-pending** other-family records remain a nonblocking research queue. Keep chronology separate and all 62 approved Grixis lists protected.
4. **Close meaningful lore gaps:** review the **341** uncertain links and the **2,626** cards still "no lore yet" in the story overlay (208 of 2,835 linked; 1,304 UB excluded), of which the Batch 13 printed-flavor overlay links 23 more while preserving unsupported entries as unknowns.
5. **Relationship layer v1 is built** (graph plus Packs A, B and C; see the status table). Next: edge dates and CardRepresentation nodes. Original item: **Build the relationship layer:** use and extend current schemas for claim provenance, card depictions, people, events and planes.
6. **Advance research Pack A:** A1/A2/A3 preserve **32 graded claims**, Elder Dragon War family links, nine general historical card names and six tiered illustrated Tarkir story contexts. **A4 directly compared all six official story images to six specific Scryfall printing art crops**; 20 distinct printing IDs share those illustration UUIDs. The story-art Ugin printing is `frf/1`, **not** the earlier `ugin/1` promo with different art. The six cards were Commander-legal on the 2026-10-30 API check, but a complete 100-card deck has **not** been built or approved. Next assemble/verify the independent lore-first candidate pool and first complete pilot; preserve the existing Deck #9 proposal and all 62 Grixis locks. Pack A's full ancient genealogy remains incomplete.
7. **Deckbuilder generalized (UNAPPROVED proposals):** Pilot 1 ([PR #823](https://github.com/corymstover/GrokBotMTGCompanion/pull/823)) and Pilot 2 ([PR #832](https://github.com/corymstover/GrokBotMTGCompanion/pull/832)) are waiting for Cory's review. The spec-driven builder and audit can be reused. The Pack A open questions were reviewed (PRs #833 and #835): grades are retained and 4 proposals are unapplied. Commander deck-construction rules checks exist ([PR #836](https://github.com/corymstover/GrokBotMTGCompanion/pull/836)). Next: research Pilot 3's claims (Narset, Elspeth), build Pilot 3 with the generic builder, then add gameplay rules-interaction checks.
8. Expand the timeline, other packs, and everyday MTG question-answering capabilities in subsequent focused milestones.

## Rules for every future work session

1. Read **this checklist** and the latest GitHub state before acting. Check merged PRs, live tracker and current snapshot manifests; do not assume a remembered milestone was published.
2. Work in bounded, reviewable batches with actual artifacts, tests and post-merge verification. Prefer substantive progress to repeated planning cycles.
3. Preserve the canonical `corymstover/grixis-commander-encyclopediaGPT` approved decklists, hashes and exceptions; do not replace them without Cory's explicit new approval.
4. Do not use a newer Scryfall bulk as if it were the missing historical `snap-20261016`. Use the independent modern snapshot path for the broad Companion.
5. Keep official lore citations, confidence and continuity distinctions. Never promote a name match to canon automatically.
6. Keep Oracle text, card legality, format policy and brackets current; annotate dates and rule-version assumptions.
7. After every milestone merge, update the completed checkboxes and checkpoint counts in this file, link the exact PR/commit/CI evidence, and state what remains. If the project Source copy is older, **GitHub's latest verified file is the workflow authority**.
8. Enforce the **v2.53 foundation-first execution hold**: do not shift attention to Phase 6 or ask for approval of existing lore-deck pilots until the knowledge-foundation release gate has been satisfied or Cory explicitly lifts this hold.

## Definition of the first major Companion release

- [ ] Priority-card enrichment backlog fully accounted for (completed or explicitly documented exceptions/gaps).
- [ ] Searchable cited connections across the three foundational lore packs.
- [ ] Reliable lookup and rules checks backed by current Scryfall and official sources.
- [ ] A verified Phase 1B set catalog with category-specific counts, set → card and card → set lookups, debut/reprint identification and English export support.
- [ ] Source-graded in-universe chronology, broad plane/character/faction history and difficult Q&A coverage reviewed for the documented knowledge-foundation scope, with explicit unresolved gaps.
- [ ] No regression in the 62 archived approved Grixis decks.
- [ ] Passing focused CI and an up-to-date, source-backed coverage report.

**Scope boundary:** This is a **knowledge-foundation release**, not a deck
release. Graph-built Commander pilots and the Phase 6 deckbuilding workflow
will be evaluated in their own post-foundation stage. No new lore deck or
owner deck approval is required for this release. Owner research/canon
decisions, foundation sign-off, exact-head CI and Grixis protections still
apply; do not relabel current preliminary research as certified.

*This is a living workflow, not a claim that all of Magic lore can be declared permanently finished. Preserve this file and revise the verified checkpoint after every substantive work batch.*
