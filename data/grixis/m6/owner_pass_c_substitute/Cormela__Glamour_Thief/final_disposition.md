# Josh-Lee-Kwai formal Pass C — final disposition: Cormela, Glamour Thief (#9/62)

## Formal provenance and authority

- **Final disposition: KEEP** exactly approved 100; **NO proposed card swap**; no owner action now; not an M6/I/J certificate.
- **Exact approved canonical source SHA-256:** `80f4bdef2b8b140aeae23775cfdf87fda81e7215038b8db9b1746c806f366e0b`. Canonical TXT Git blob `ee008725234c917af858de5a9c237fc2acf6781d`, `corymstover/grixis-commander-encyclopediaGPT/main/refinement/decklists/Cormela_Glamour_Thief_Approved_2026-10-14.txt`. Canonical owner status APPROVED/LOCKED unchanged. 100 cards/100 names, one commander/99 other, 30 lands; all distinct for Tainted Pact.
- **Review path:** `data/grixis/m6/owner_pass_c_substitute/Cormela__Glamour_Thief`.
- **Neutral Stage A first commit:** `1ded0407879a81539ea6feca9137201b69372390`.
- **Separate cryptographic seal commit:** `f254824ccf249bae61cde93f6898f924163a28f5`, immediate child of first commit; **verified before unblinding**. Stage A file SHA256s: MD `97243c9c2fb49de33e70c0b836dbc84c56abb967e8ce11cdc638359d96baec88`; JSON `3076b281a1715dabc80ce25a6b6a1053dc664531c0347211c8005a06720c3cc3`. Both immutable.
- **Evaluator provenance:** alias Josh-Lee-Kwai; actual evaluator ChatGPT/OpenAI GPT-6, **not a technically independent third model**. Owner formally waived independence 2026-10-20. On verified CI/merge record this as `FORMAL_PASS_C_OWNER_EQUIVALENT`. Prior context familiarity cannot be erased; neutral source/view boundary followed.
- Prior ChatGPT deep review `ccd48cf2d8f9a5d21ea3a2d9968d177b92374ca7` KEEP; GrokBot advisory `44bd745f01a5fffdd0ba6789d5af7eb39d89898a` KEEP (advisory only); reconciliation `c4f21ed7080af6d9f885891d673f818a24f7e8d2` KEEP. Controlled comparison is documented in `stage_b_reconciliation.md`. Stage A independently and provisionally recorded NEEDS TESTING, not altered.

## Commander-first decision

Cormela's 4-mana haste, extra `{1}` activation tax, instant/sorcery-**only** UBR, and death-trigger spell recursion are deeply embodied by Demonic Gifts with both Altars, Saw in Half legend-rule double recursion, hasty reanimation via Goryo's Vengeance/Shallow Grave, Birgi and Molten Duplication spell chaining. The noncommander backup wins Oracle/Consultation/Pact, Underworld Breach/LED/Brain Freeze, and Dualcaster/Molten Duplication support a real natural high-Bracket-5 cEDH ceiling while retaining commander-specific wins.

The full prior card audit and October 14 canonical gate substantiate legality/color/100-card history; Stage A independently repeated source byte hash/count, reviewed selected Oracle/rules with WotC release notes, and found no exception. **This review is not a new exhaustive live Oracle / official banned-list scan** and does not upgrade historical approval gate into a final M6 certificate.

## Adversarial verdict and competing conclusion

The most credible new challenger was **Muddle the Mixture for Seething Song**, which converts a net-positive, Cormela-recurable red ritual into a two-blue counterspell or an **unrestricted-mana-only 3MV sorcery-speed transmute** for MV2 engines. It can tutor Demonic Gifts/Breach/Duplication/Oracle, but the additional two-mana cast and blue pip after transmute materially slow fast combo and commander access. With 30 lands, color-tax and speed matter. **No evidence demonstrates that exchange beats the approved Song**, so no exact swap is recommended. Abrade against resolved artifact hate is a plausible but narrower side hypothesis without a justified cut or universal answer to enchantment Rule of Law. KEEP is not passive: it rejects replacing Cormela-native speed with unproven tutor/hate slots given actual paid tempo and source constraints.

The strongest argument *against* KEEP is that 4MV Cormela is interactable and the list has few clean answers after hate permanents resolve; another targeted answer might win some games. But adding that answer necessarily removes proven ritual, fixing, protection or combo redundancy. No tested net-positive pair has emerged. The existing ChatGPT/GrokBot unanimous KEEP is corroborating **advisory/source evidence, not measured match outcome**.

## Rules and limitations

- `{1}, {T}` to make UBR, not free; UBR only pays costs for casting instant/sorcery spells, not activated mana costs, creature/artifact/enchantment casts. LED and both Altars have **nonmana** activation costs (tap/sacrifice/discard, or creature sacrifice); earlier wording about 'paying for LED activation' was technically imprecise and is explicitly corrected in Stage B.
- Demonic Gifts gives a **single** return for each affected creature object, not permanent immortality. Cormela's death return can target Gifts after it has resolved; stack ordering and graveyard availability are necessary. Ashnod's Altar produces unrestricted CC while Phyrexian Altar produces one unrestricted mana of a chosen color, paying a future Cormela `{1}` activation. No unjustified unrestricted UBR claim.
- Saw in Half: two copied legendary 1/2 Cormelas after destroying original, legend-rule one death, two total death-return triggers. Reanimation needs commander left in grave at relevant moment. Molten Duplication+Dualcaster requires an original legal target and responding on stack; copies are not casts. All lines are interruptible.
- The project has **no applicable authorized illegality exception** for this deck. Nothing in the approved 100 is altered.
- No new randomized gameplay, goldfish win-rate, effect-aware exhaustive Phase B, full current Oracle check, I tested-pool zero-improvement proof, J reproducibility bundle, or M6/M7/M8 acceptance is claimed.

## Specific downstream targeted tests (only when required for valid certification)

1. Verify graveyard-target, dying-trigger and mana-restriction sequence of **Cormela + Demonic Gifts + each Altar** with response windows, including replacement/exile and known stopping conditions.
2. Audit 30-land hand/mulligan color-source access and four-mana commander deployment versus pre-combo pressure when crafting M6 certificate, reusing source-bound evidence.
3. Recheck current Oracle/Commander legality and locked SHA at certificate generation. Where existing reproducible evidence meets Phase B and I/J criteria, reuse it; otherwise identify missing receipts honestly.
4. Test Muddle/Seething or an Abrade-based pair **only if** tangible tournament/opponent evidence or targeted source weakness makes the comparison consequential. No universal second candidate sweep.

**Progress gating:** this final disposition counts as formal owner-equivalent Pass C **only after** its evidence PR exact-head CI succeeds, the PR merges, and the separately CI-verified progress ledger PR merges. Prior to that no new completion may be claimed. Formal Pass C is distinct from source approval, genuine third-model execution, Phase B, I/J, M6, M7 and M8.
