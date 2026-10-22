# Abaddon — qualifying *other* hand spells gain cascade

**M6.6 source-bound limited extension; no M6 or M7 approval.** Preregistered before implementation at `cd5fa6775ed0a65ce3640badd86eaa341bad620f`. Frozen, approved Abaddon SHA-256 `2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf`; one commander plus 99 real physical cards. No canonical cards are altered.

## Why this matters

PRs #524/#526 tested only Ignus's granted cascade; they **recorded but omitted** other paid hand spells which also qualify for Abaddon's static ability once opponents have collectively lost at least their printed mana value on that same turn. This distorts the source of real mana, extra cards, and cascade access in an Abaddon-first deck. The same physical library, land payments, pool, graveyard and frozen 12-source-verified hit effect subset must be shared with all eligible triggers, rather than count those spells as if they do nothing. **This branch expands only the already implemented named core hand spells.** It neither invents card effects nor completes every spell in the 99.

## Newly modeled cast-trigger windows

- Original **Boltwave** (printed MV1): only cascades if 1 or more opponent life has *already* been lost when it is cast; its own damage resolves **after** cascade, so cannot retroactively trigger its own ability. First eligible physical hit can only be MV0.
- **Flame Rift** (MV2): needs prior opponent loss of at least 2; can hit MV0 or MV1. Its source opponent damage and pilot damage happen after hit effect resolves.
- **Nightscape Familiar** (MV2), **Birgi front** (MV3), **Rakdos, Lord of Riots** (MV4), or challenger **Aggravated Assault** (MV3): whenever these are truly paid and cast from hand with Abaddon already controlled and same-turn opponent loss at least printed MV, cascade occurs before each original spell resolves. Birgi does not add red for its *own* cast if not already controlled. Discount effects change amount paid, never source mana value.
- **Grinning Ignus** remains MV3; its original cascade and later bounce/recasts are maintained exactly as PR #524. Abaddon itself is cast from the **command zone**, so its own cast is never given its hand-only cascade.
- Zero-MV spells such as **Lotus Petal** still *have* cascade if cast from hand while Abaddon is controlled, since `0 <= X` always holds. But no card has negative mana value: such a mandatory cascade exiles **the entire remaining library** and puts those cards back on the bottom in seeded random order. That is a library-reordering event, **not** a free spell or ramp. This is tested adversarially as a conditional case rather than added to the restricted core hand-spell policy.

For every qualifying named core hand spell the test now invokes the same physical cascade resolution on the paid original spell's stack, using strictly **lower printed mana value**, optional cast of the first eligible hit, proper return of other exiles, no free Abaddon cascade on a hit cast from exile, and a resolved 12-card hit subset. The counterfactual enhanced path preserves exact physical zone counts at every turn checkpoint; the original path still delegates unchanged to the earlier simulator. **Reporting caveat:** the predecessor exposes per-seed *whether* any Ignus cascade or supported effect happened at each checkpoint, not exact counts of those events. Paired conclusions must compare seed-level incidence fields only. Exact event counts for Ignus and supported hit resolutions are reported **only in the enhanced mode**, not falsely backfilled with boolean 0/1 values from the predecessor.

## Registered paired experiment and limits

Five exact 100-card single-slot variants (approved; Ignus/-Rakdos, Ignus/-Nightscape, Ignus/-Rite; Assault/-Rakdos), two deterministic named-spell cast priorities (engine-first or burn-first), two modes (original unchanged Ignus-only vs plus qualifying other named hand cascades), **500 matched seeds per variant/policy/mode** through ten own turns (10,000 restricted trajectories). Conditional focused stack tests supply life loss using an assumed existing damage source and a physically payable hand-cast spell; these are not random board-access estimates.

**Not modeled:** most other spells in the 99; all hand ramp/Chrome Mox/LED/full artifact decisions and card-draw choices other than existing limited subset; cascade on conditional spells omitted from cast priorities; other cascade sources, Storm-Kiln, exile payoff enchantments, tutors beyond the fixed prioritization, counterplay, life-total wins, commander deaths/tax, and Neheb/Loyal postcombat play. The cascade of a **hand-cast zero-MV spell** is individually tested for mandatory full-library exile but not incorporated into whole-game trajectory counts, because hand casting Lotus Petal is outside the named core policy.

Consequently these results can identify **real additional qualifying cascade opportunities** under paid-color restrictions and a specific fixed pilot; they **cannot** establish overall Abaddon game win probability or the net superiority of a single replacement for Rakdos, Familiar, or Rite. All candidate judgments remain HOLD/RETAIN as recorded; 62 canonical deck approvals remain untouched. M6.6/M6.7 PARTIAL, M6-certified 0/62, new M7-approved 0/62.

## Authoritative rules and source references

- [Wizards Commander Legends release notes: cascade on cast, printed mana value, trigger resolves before source, counter doesn't erase trigger](https://magic.wizards.com/en/news/feature/commander-legends-release-notes-2020-11-06).
- [Magic Rules Tips: cascade is mandatory to exile but casting last hit is optional](https://blogs.magicjudges.org/rulestips/2011/01/how-cascade-works/).
- Frozen Abaddon 99 approved source, physical graph `data/grixis/graph/abaddon-the-despoiler.json`, exact printed mana costs registered in `scripts/grixis_m6_abaddon_ignus_paid_chronology.py`, and `refinement/tests/Abaddon_Current_Card_Audit_2026-10-13.csv` in canonical repository.
