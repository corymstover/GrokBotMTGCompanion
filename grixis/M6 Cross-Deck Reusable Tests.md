# M6 cross-deck reusable test suites — verified source-bound cache

This is a **small adapter atop the repository's existing simulation architecture**. It does NOT replace the M6 single-deck authored workflow, rewrite existing Magic mechanics, rerun research, or change any canonical decklist. It takes three existing *generic* test suites, fingerprints their registered source/test files, and **skips an unchanged suite only when a positive prior test result remains linked to the exact same code and frozen inputs**. All changed inputs rerun automatically. Failures and zero-test runs never enter cache.

## What we already had

- `scripts/grixis_m6_state_kernel.py`: reusable physical UID ledger, zone conservation, basic-land mana, deliberately rejects unmodeled effects; all 62 deck imports exercised with `grixis_m6_state_kernel_62.py`.
- `scripts/grixis_m6_transactional_stack.py`: bounded transactional stack with cast/mana/rollback, **only six registered card effects**, not a complete stack engine or realistic opponent behavior.
- `scripts/grixis_paired.py` and `grixis_sim.py`: reproducible paired-seed source alignment and older v1.1 goldfish **proxy** results. `grixis_paired` already keeps its own model/list/seed preregistration-aware record IDs. Its coverage is incomplete for many commander-specific effects, and the old development `.cache/` was lost in a prior machine restoration.
- `grixis_m6_model_coverage.py`, M6 I/J bundles and schemas: prohibit unmodeled-goldfish improvement claims; exact hashes source-bind reproducible evidence.
- The later Abaddon series (#511–#533) substantially extends **commander-specific** effect coverage, but these are not yet generic simulation modules guaranteed valid for another commander.

## New low-risk reusable dispatcher

`data/grixis/m6/reusable_test_suites.json` declares suites, **all known code and data dependencies**, and each suite's strict coverage limits. `scripts/grixis_m6_reuse.py` enumerates that manifest and computes SHA-256 over the **byte content** of the runner, manifest, registered implementation modules, test files, registry/snapshot files and (where registered) all 62 frozen baseline exports. If every byte is unchanged AND a prior receipt is a `PASS` with more than zero executed tests AND all authority flags remain false, the test result is safely marked `REUSED_VALIDATED_PASS`. If inputs change, the runner invokes the exact registered Python `unittest` pattern again. A suite with missing/malformed inputs, a failed test, a zero-test collection, an unknown suite or forged authority does not enter the cache. An optional deck ID validates frozen engineering registry/source-export hashes; it **does not claim that the current external canonical GitHub approval was live-fetched**.

Three starter shared suites, each still limited:

| Suite | Reusable fact | **Not** tested |
| --- | --- | --- |
| `physical-zones` | Identity and zone conservation, deterministic cross-62 source draws | Card abilities, legality, real mana sequencing and wins |
| `transactional-stack` | Registered bounded spell stack, payment/rollback invariants | Arbitrary cards, Abaddon effects not explicitly implemented, opponents |
| `model-coverage` | Fail-closed detection of unsupported positive simulator claims | Whether a challenger actually improves any deck |

### Usage

Plan and show cache decisions **without running tests**:

`python scripts/grixis_m6_reuse.py --deck-id Abaddon_the_Despoiler`

Execute all absent/stale generic suites, keeping verified pass receipts in `.cache/grixis_m6_reuse`:

`python scripts/grixis_m6_reuse.py --deck-id Abaddon_the_Despoiler --run --json-out m6_reuse_receipt.json`

For a later commander, replace the `--deck-id`. **The same unchanged cross-deck suite pass is reusable**, because the foundation test and source snapshot are shared. The per-deck registry binding is checked every time, separately. This is how we avoid rerunning the **same global invariants** 62 times, while refusing to transfer a commander-specific test outcome to an unrelated deck.

Run one suite only: `--suite transactional-stack --run`. Require a fresh run: `--run --force`. The read-only runner never issues a `swap`, `certify`, `approve` or `lock` action.

## GitHub CI integration and limitations

The dedicated workflow `.github/workflows/m6-reusable-suites.yml` runs the new cache-invalidation tests, then validates the existing three suites. It caches successful receipts via GitHub Actions cache for integration-branch reuse. An updated `test_`, `script`, `data` or tracked baseline export that is **declared as a suite input** invalidates its digest regardless of cache restore. Cache hits are **not verified fresh game outcomes**; they are reproducible prior unit tests of the exact same bytes.

New cross-deck tests can be added by **registering an already verified pure-rule suite and its complete relevant dependency set** in the JSON manifest. Commander-first behavior still needs card-specific Oracle modeling and adversarial tests. Do not register Abaddon's Ignus/Ruinous fixtures as generic evidence for another deck unless their underlying effect is independently applicable and source-verified.

**Authority: all false:** The M6.5 owner-equivalent Pass C waiver remains in effect, while M6.6/M6.7 still require actual effect-aware game evidence and authored judgment. This cache does not reduce the number of 62 commanders requiring individualized review, grant M6 I/J certificates, claim game win rates, or create M7 owner approvals.

## Efficiency claim

The intended speed-up is **real but bounded**: skipping identical generic foundation unit tests and avoiding manual rebuild of the same invariant checks. This first implementation has no validated multi-deck wall-clock benchmark and does not promise that future full-deck effect-aware simulations become instant. The right future extension is incremental **mechanic-family adapters** (e.g., graveyard, sacrifice, cascade, exile-cast, artifact tap/activation), each with accurate effect coverage, source hashes and context-aware tests, rather than replacing Commander-specific conclusions with a single generic score.
