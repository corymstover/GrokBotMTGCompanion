# Branch cleanup manifest — 2026-11-02

Machine-readable source of truth: [`data/maintenance/branch_cleanup_manifest_2026-11-02.json`](../../data/maintenance/branch_cleanup_manifest_2026-11-02.json).
It supersedes the read-only inventory in [BRANCH_PRUNING_REVIEW_2026-11-02.md](BRANCH_PRUNING_REVIEW_2026-11-02.md) for deletion purposes; that inventory and
[PR_650_707_RECONCILIATION_2026-11-02.md](PR_650_707_RECONCILIATION_2026-11-02.md) remain unchanged.

This file was merged to `main` **before** any branch was deleted, so every deleted name has a permanent exact-SHA recovery record.

## Summary

- `main` at reconciliation: `cf248059585f2c56ecf015b208d92d2aa355d3de`
- Branches before cleanup: **889** (877 distinct head SHAs; 12 exact-duplicate pairs)
- Proposed deletions: **213** — 201 fully merged (head is an ancestor of `main`, 0 commits outside `main`) + 12 redundant names of exact-duplicate pairs (the shared commit stays on the retained twin and is also inside `chatgpt-cycle76-m6-refinement`)
- Preserved: **676** = 4 never-delete + 636 not merged into `main` + 36 merged-but-kept (name references / recent)
- Protection: no protected branches, no rulesets, no branch rules on `main`. Open PRs: 0. All PRs (every state) were matched to head branch names.
- Content proof: for each of the 651 heads that are **not** ancestors of `main`, `git rev-list --objects <head> --not main` contained at least one file blob that never existed anywhere in `main` history, so **no unmerged branch was treated as redundant** and none is deleted except exact duplicate names.
- Name-reference scan: every branch name was searched in every tracked file on `main`, and every deletion-candidate name was searched across all 639 distinct unmerged heads. Every deleted name appears nowhere except the read-only inventory JSON; any merged branch whose name appears in any other file (on `main` or on a retained head) was kept.

## Recovery

Restore any deleted branch exactly (no force needed, the name will not exist):

```
git push origin <head_sha>:refs/heads/<name>
```

Each entry below and in the JSON carries its exact command.

## Exact-duplicate pairs (investigated first)

| Deleted name | Retained twin | Shared head SHA | PRs (deleted name) |
|---|---|---|---|
| `chatgpt-abaddon-final-j-oracle-capture-20261022` | `chatgpt-abaddon-oracle-j-frozen-20261022` | `fd143871f84b21ccb03ff8714f5a3df597bd83f1` | — |
| `chatgpt-abaddon-final-m6-ij-20261022` | `chatgpt-abaddon-ij-strict-final-frozen-20261022` | `ef42d0a1fdaa1e4b3987df2d3d57477d89f0a6ef` | — |
| `chatgpt-abaddon-m6-6-7-adjudication-20261022` | `chatgpt-abaddon-m6-6-7-fixed-frozen-20261022` | `5c84c4a5e1ceb436bc315bb197f93a537cd444f0` | — |
| `chatgpt-abaddon-m6-j-candidate-mana-redteam-20261022` | `chatgpt-abaddon-m6-j-validated-source-crosswalk-20261022` | `875752deda9c4b93f6efb6f1c05093a55d27f46d` | #561 |
| `chatgpt-abaddon-m7-opportunity-reopen-20261022` | `chatgpt-abaddon-m7-reopen-frozen-20261022` | `d899fb4f829bab33a646d30cfb9cd9d222eae51c` | — |
| `chatgpt-abaddon-owner-ready-m6-ij-20261022` | `chatgpt-abaddon-owner-ready-frozen-20261022` | `7359216b52f0406261cb03fc6801b7e98ebe2066` | — |
| `chatgpt-abaddon-p0-030-ledger-20261022` | `chatgpt-abaddon-p0-030-ledger-exact-head-20261022` | `139c97118e8436f0b160a10a8025fc05906cc7e6` | — |
| `chatgpt-abaddon-p0-030-threshold-doublers-20261022` | `chatgpt-abaddon-p0-030-exact-head-20261022` | `029fdb9a8fdefe2ef81be09be6dc03cb54c59d30` | #563 |
| `chatgpt-abaddon-persist-full-oracle-20261022` | `chatgpt-abaddon-full-oracle-frozen-20261022` | `6cf0b8cf37305bf08f318f621ca7f06b60bdde8e` | — |
| `chatgpt-abaddon-remaining-p1-20261022` | `chatgpt-abaddon-p1-final-frozen-20261022` | `fb5a4a7e56e9b428304274045d8a9f16d71f789a` | — |
| `chatgpt-abaddon-residual-p1-reconciliation-20261022` | `chatgpt-abaddon-p1-frozen-head-20261022` | `b872f7aa9821068458eddda1bea593ed8e6998be` | — |
| `chatgpt-m7-no-few-swaps-owner-hard-gate-20261022` | `chatgpt-m7-no-few-swaps-owner-hard-corrected-20261022` | `85ac36b161020fd00d1afc82b508326d60d3c69d` | — |

PR #561 and #563 (closed, unmerged) recorded older heads `ece5a5e7…` and `df279ed3…`; both were verified as ancestors of the retained shared head, and GitHub keeps `refs/pull/561/head` and `refs/pull/563/head`.

## Fully merged branches deleted

| Name | Head SHA | PRs |
|---|---|---|
| `bot-cycle23-lore-85` | `fe0d4fd0c72b642453859f0a6836662f4f8d8d52` | #84 |
| `bot-cycle24-lore` | `3892567fa5b12ae5b4aeb2da0324d7f5089a15ec` | #85 |
| `bot-cycle3-lore` | `029b044c7b7a27b7f8804419652fdf1764b587af` | #22 |
| `bot-cycle47-authority` | `b9365bedd937040991cc0ce136bcc28abe85c8dc` | #120 |
| `bot-cycle5` | `26817ad2d11504b339a429fd7e1d80f6fa86a06c` | #24 |
| `bot-cycle50-blueprints` | `5ad4a286ddab841abef5885b5474cba3d70cdec6` | #122 |
| `bot-cycle52-blueprints` | `69b2026198908d2359847f2524a3c0cd504521c3` | #123 |
| `bot-cycle53-blueprints` | `fac0309de623195aea45206c933e6536d21a0136` | #125 |
| `bot-cycle55-blueprints` | `8748d7db894e86836f856c373c2f063c8e1ceb94` | #127 |
| `bot-cycle57-m3` | `015d74617fa6c40d461d2c7d14436c564f98ce09` | #134, #133, #132, #130, #129, #128 |
| `bot-cycle59-m4` | `406d52c30796af6f7ce3b490d1dda945fd549b32` | #137, #136 |
| `bot-cycle60-m5` | `41bae0993f49ff317ff07ecdf20ce8f0de171d3f` | #138 |
| `bot-cycle61-constraints` | `28c49289175bcc6cb834a2a298742b26d69c1952` | #139 |
| `bot-cycle62-accept` | `fbdcfa4302a824c18f826e33abe95042d9e4907c` | #140 |
| `bot-cycle63-accept-m2-m4` | `5fe98acc352001afc6f8d7dc80b5925c522abcd5` | #141 |
| `bot-cycle64-g0` | `aa118466c152953cba7bce2b09bc8bfbcbe27604` | #142 |
| `bot-cycle65-saturation` | `5e3498d716d73e9f1ec3c04d744bf412ea76c7ba` | #143 |
| `bot-cycle66-2` | `4f7347e21fc8b0aefb0e9e5f468fa28a0d3bdabc` | #145 |
| `bot-cycle66-2a` | `287108133217cf4020ccf8a493dfc5f52dd4e3f9` | #147 |
| `bot-cycle66-3` | `a46f567981f9ea2b1b7de6d8f6c2b63f6f82ae06` | #146 |
| `bot-cycle66-4` | `4d85265e9c76998560270682308eb78a5b7b05ab` | #148 |
| `bot-cycle66-lock` | `4b9c60da04d319450a7fbf458a31ad137f54eb71` | — |
| `bot-cycle66-mechanics` | `56f8ac88a0a72c98af2d3c8fb73fdf5beb8ed480` | #144 |
| `chatgpt-build-finish-line-v305` | `a07e33c34d78b584628232aa65037b63021bb508` | #975 |
| `chatgpt-commander-ci-v303` | `f010432deed0c78204c23452fe6a5c1a5214eb35` | #973 |
| `chatgpt-cycle66-10-stax` | `32a4987d33f462e3d11141e26eab2e3233830a57` | #155 |
| `chatgpt-cycle66-11-breach` | `2f49533dff138e47a33506f0c34873ddb2f9a5f6` | #156 |
| `chatgpt-cycle66-12-pressure` | `f59cf2cc2eaf37a79f32484ee9c40c57e6bf1613` | #157 |
| `chatgpt-cycle66-13-step-e-closure` | `ef3fdeb696e7154b0789759ea5f91a6859c9397a` | #158 |
| `chatgpt-cycle66-5a-attack-semantics` | `12f688e50f90dc6d8aa8c9529974a5e4e08b836d` | #149 |
| `chatgpt-cycle66-5b-recursion-semantics` | `49504a2c3c45af6970df61ea8f82124f82758068` | #150 |
| `chatgpt-cycle66-6-stack` | `a6b1ecca3c0320e54ff9a6b5cb60528a2d85a2c9` | #151 |
| `chatgpt-cycle66-7-costs` | `cdca35941ea42b807455041139f72af794638457` | #152 |
| `chatgpt-cycle66-8-tutors` | `9af7fbe91ad3e48ef21841a15f22f65a474c1656` | #153 |
| `chatgpt-cycle66-9-opponent-draw` | `5dc0a6d8e79d3ec2efb1d2acf03afccef0f8d9c3` | #154 |
| `chatgpt-cycle67-1-combo-quality` | `552ff6f5da17286aa9e04e5465fd88133c831c15` | #159 |
| `chatgpt-cycle67-2-power-core` | `02bc981641615f16500f5ad763e1b01f3b112f86` | #160 |
| `chatgpt-cycle67-3-combo-steps` | `205fe0092b381a985eb9a9cb86e5db59b588ac75` | #161 |
| `chatgpt-cycle67-4-combo-families` | `07471ccb02b1b3d513a3086f30c3d5260ca347af` | #162 |
| `chatgpt-cycle67-5-step-b-closure` | `c80af61d22df98cc707874b3d1fc4c143c7a0bfa` | #163 |
| `chatgpt-cycle68-1-mana-baseline` | `b44f69edc183b92e07d135c76bb792d7d84fba06` | #164 |
| `chatgpt-cycle68-2-mana-timing` | `03e7021861b03dc06d78e04045e6f5837b0a134c` | #165 |
| `chatgpt-cycle68-3-commander-mana` | `9a614b27796ac14fc6397b92917a66c7d3c4b793` | #166 |
| `chatgpt-cycle68-4-mana-opportunity` | `0ec366fe825258b1c9b1b3c5806dbfa086ed7868` | #167 |
| `chatgpt-cycle68-5-mana-resilience` | `fabc6dcb1a2c9df8150d41c116070b61a87a767c` | #168 |
| `chatgpt-cycle68-6-mana-integration` | `8482ad0ada1cba31c24bdfd4216f9eb14c7c6d05` | #169 |
| `chatgpt-cycle69-1-commander-structure` | `53f5ca48df30923d4e3c765f152a22572045bcee` | #170 |
| `chatgpt-cycle69-2-commander-counterfactual` | `1c5beb563d76fd481a6e09f0b1afd174f96b49a9` | #171 |
| `chatgpt-cycle69-3-commander-integration` | `4f7b4028ed8173b48eebb6e28ad7288bf96d8469` | #172 |
| `chatgpt-cycle70-1-bracket-stress-prereg` | `e0105c3e0df9548ae2a6f392a0ccd1ed17cd174f` | #173 |
| `chatgpt-cycle70-2-bracket-runner` | `deec5070220d2f7bec99454c366dba815f0a09a4` | #174 |
| `chatgpt-cycle70-3-red-team-packets` | `5475d5cf771cc2e79ca1572039d0941d7926aca6` | #175 |
| `chatgpt-cycle70-4-bracket-integration` | `17d9c2f40801cf4a8d1c04db71278a0d893e94e1` | #176 |
| `chatgpt-cycle71-1-human-sampling-policy` | `e437a3c64ee21470154c61928123071c387e3833` | #177 |
| `chatgpt-cycle71-2-human-sampler` | `222e85d6da109f78c028a3ed3f4ca2d71982e437` | #178 |
| `chatgpt-cycle71-3-human-sampling-integration` | `f1cf38efb1724eeed7960167df55c25d74990175` | #179 |
| `chatgpt-dual-timeline-v291-20261101` | `32be90a3b49a981b344cb1a3f2fa47ce9647f6a7` | #961 |
| `chatgpt-entity-coverage-audit-v292-20261101` | `327b589ac2475bd5f586cee97f32b24b05017f27` | #962 |
| `chatgpt-foundation-certificate-v300` | `e3c338c0d4d6d54ab87a20b246b6eda98cb461b8` | #970 |
| `chatgpt-foundation-certification-sprint-v298` | `8aea1ce41382fe6b319ab043081f5d86a74c935c` | #968 |
| `chatgpt-foundation-certification-v299` | `6911010326cd5707fcd5c7a68076743907624ed9` | #969 |
| `chatgpt-foundation-checklist-closure-v290-20261101` | `d7438b1cdf9ffb847f998c69f7447c3219d976ed` | #960 |
| `chatgpt-foundation-first-v253-20261030` | `aa204faae5c60a571c40fe8c404a08455f9dc08a` | #922 |
| `chatgpt-foundation-graph-qa-20261031` | `91d2f8a65964510552ce8d2dd9ed8e71df5b21a2` | #951 |
| `chatgpt-foundation-integrity-20261031` | `bb3aa5f2a857bba800a14a622076e9ebf0ec1e1a` | #953 |
| `chatgpt-foundation-release-sprint-v295-20261101` | `7ee6ab9560044914c76190f92a1a15b07f8e4be3` | #965 |
| `chatgpt-foundation-source-gaps-v294-20261101` | `858a3eaf3805075e950d4389dac2b869d2a36ad4` | #964 |
| `chatgpt-foundation-war-operations-v297-20261101` | `229a872bc3cc7b4117a53d48d3a8fc1459794d3b` | #967 |
| `chatgpt-foundation-war-qa-v293-20261101` | `5c3c0e974bfd84795bda405bc644d0fb10a4ef72` | #963 |
| `chatgpt-graph-variant-lookup-20261030` | `1d2dfe7a1aa5da7b412908ddf7a8d32343be26ed` | #915 |
| `chatgpt-lore-ugin-life-deck9-20261028` | `2103014aca9161fcb2fdd07544bd6483ace3c231` | #776 |
| `chatgpt-m7-one-command-contract-20261024` | `d90d59d8c226b880cfa8353058b8cd04efc14ccd` | #702 |
| `chatgpt-multiverse-master-workflow-20261029` | `917b60584f64756c4ba2d68339805c190ec10f7a` | #785 |
| `chatgpt-multiverse-snapshot-reconcile-20261029` | `f868d5915f940a9448b08e2a5c0d62d550c2a35b` | #784 |
| `chatgpt-multiverse-snapshot-repair-20261029` | `4d05a2199ead8d97766146a68c9e3d682f1b94ba` | #783 |
| `chatgpt-pack-a-ugin-bolas-claim-foundation-20261030` | `ddac730202376b84a98ed9582e9e8bb02591039e` | #819 |
| `chatgpt-pack-a2-elder-war-primary-sources-20261030` | `e7b68f0054ade64a13ca827d394d58820fd691a1` | #820 |
| `chatgpt-pack-a3-tarkir-art-context-20261030` | `0cb6df92f265cdc5046f397813459b702c5ed0c3` | #821 |
| `chatgpt-pack-a4-exact-art-printings-20261030` | `e7368235ebd9de0cd42376e0aa57eb76fac4c273` | #822 |
| `chatgpt-pack-c5-phyrexian-outcome-20261030` | `40d1d4066f8a57407f9b19ad9d518a0b8f274f63` | #917 |
| `chatgpt-phase1b-apac-lunar-promos-20261029` | `0e46d570e2bef0c7df6e7ddcbe33fa6c94363174` | #811 |
| `chatgpt-phase1b-art-series-sources-20261029` | `0a8b5a868d2d616b6afbabdf4f7a979b81f0fdb5` | #813 |
| `chatgpt-phase1b-event-collab-promos-20261029` | `043d372268e484d19606db06580320574d2ac2d7` | #812 |
| `chatgpt-phase1b-export-acceptance-20261029` | `5b62a2ad1f41d50182342221bd45b46e484cda02` | #816 |
| `chatgpt-phase1b-fasttrack-readiness-20261029` | `9345a4c32c845466d53580b1df615d6b44bd4ed0` | #815 |
| `chatgpt-phase1b-masterpieces-collectibles-20261029` | `f789608b7e9f8b85cfdbb7d75debc526d524b420` | #809 |
| `chatgpt-phase1b-qualified-functional-release-20261029` | `ead884bd150a59ddb6e58b538a9f5f0f3ffe63c4` | #818 |
| `chatgpt-phase1b-release-scope-story-20261029` | `695a48d8901cb988a6d39d161ee8d9acd3de2836` | #817 |
| `chatgpt-phase1b-token-families-20261029` | `681c74da25a19d02749bdd5c531e21e7e87f25af` | #814 |
| `chatgpt-phase1b-vanguard-worlds-lgs-20261029` | `f4ab3ddb914b94d296e57756bfc395c29a02226b` | #810 |
| `chatgpt-phase3-printing-phase8-monitor-20261030` | `dc76828180151a82e0dbdd57a20de78d0424867c` | #916 |
| `chatgpt-phase4-alara-conflux-20261031` | `7ab24d84e5bbedd061a6b4db371631ad89d67796` | #952 |
| `chatgpt-phase4-amonkhet-ravnica-v287-20261031` | `3a7757573d00f14db35a0d44072013030073b4e0` | #957 |
| `chatgpt-phase4-bolas-current-20261031` | `368bb9284ea436a9d920ae3785380c39f4d9d4a8` | #950 |
| `chatgpt-phase4-chrono-history-20261031` | `3425d43bc49c9ab98d3fe80c5ac141f14af7a9ee` | #949 |
| `chatgpt-phase4-source-sequences-20261031` | `61136f3c9d970c6adc0d0ad7b1d13a9a29f98156` | #948 |
| `chatgpt-phase4-verified-ledger-bridges-20261031` | `f120a0c7e4233a0dd8731e00dd6ef60b454d6ce5` | #947 |
| `chatgpt-phase5-alara-profile-20261030` | `b275748463188181bf82cd119f1d51ee6e6071fe` | #919 |
| `chatgpt-phase5-history-chronology-20261030` | `6ab41fad6cbf6ab77fe93e449767e78bdace436e` | #914 |
| `chatgpt-phase5-plane-dossiers-20261030` | `361248e24b6eac73cf04f73dd1364ed05eb26f52` | #918 |
| `chatgpt-phase5-theros-profile-20261030` | `ce09c396af6da8db24227b69d14aae467680ef17` | #920 |
| `chatgpt-phase6-engine-v302` | `96562cf4339ddb851ef12d29eaa30e986f2f589a` | #972 |
| `chatgpt-phase6-strategy-preflight-v304` | `5c54337807a1fcee133612d116d9dcc40275c8b3` | #974 |
| `chatgpt-phase7-card-lore-rules-v288-20261101` | `5220c20caba0c52a671f2d9dff8dfb5996b38a1c` | #958 |
| `chatgpt-phase7-commander-safety-20261031` | `4171f186e6424f3dec67357d2d2abb5e66d552b4` | #954 |
| `chatgpt-phase7-graph-connections-v286-20261031` | `5146371e518cb1cac398845ce52d3f9dfc28ae73` | #956 |
| `chatgpt-phase7-kinship-leadership-confidence-20261031` | `6efffeda66b3909590e55f2afc457ee03bc25d9a` | #946 |
| `chatgpt-phase7-plane-history-qa-20261030` | `ac5f0dd263ca968fe1b6256c5e8fd1ef2295ad67` | #921 |
| `chatgpt-phase7-set-story-v289-20261101` | `1addb1dc2fcda752958312edf0092594cac9c885` | #959 |
| `chatgpt-phase8-name-match-triage-20261029` | `9de772b7cc206a8fbae4f190065de571853d00aa` | #782 |
| `chatgpt-phase8-story-repair-manifest-20261029` | `6eda1642f775a314acd17f122269072023cfa4e3` | #781 |
| `chatgpt-post-grok-integrity-20261030` | `145ae707fb0cc42a6ffe1380ceb37f5fb20d80e4` | #913 |
| `chatgpt-postfoundation-war-spark-v301` | `d298fd907edc3afb4458a77edcea4afe1c052908` | #971 |
| `chatgpt-v285-postmerge-handoff-20261031` | `1eb152edcf9083fd5ed2c59ce76c7cbdf39ca315` | #955 |
| `grokbot-ask-c4-relations-20261030` | `8f5f72e72d691cb58b981a918b34528c1d9b020c` | #855 |
| `grokbot-b10-docs-recount-20261030` | `191b0bb43e5b2b07833c97246de69af7ea349307` | #894 |
| `grokbot-b10-recount-20261030` | `aa3cd6ab9e13f8dfd56fb236e88dcb8667043d27` | #888 |
| `grokbot-b10-untagged-guides-conspiracy-20261030` | `ed12ccecf29cbce0e244b653a04e244e75a8f7bc` | #890 |
| `grokbot-b10-untagged-guides2012-maelstrom-20261030` | `34ea1ec9475856c81d6bd99c487d195e3d967659` | #893 |
| `grokbot-b10-untagged-misc-20261030` | `0215ad0ab0c2a8514a512c1298d86c9a1899e653` | #892 |
| `grokbot-b10-untagged-ori-grn-20261030` | `eb547c26944b8503786916b7942540d3d0afee5b` | #891 |
| `grokbot-b10-untagged-znr-20261030` | `e3eabb2915794f1a00ffd6140f9679b655d2b6a2` | #889 |
| `grokbot-b11-docs-20261030` | `1d463931d9f58385a0bdab1750eb49bd7372e89d` | #897 |
| `grokbot-b11-leader-union-20261030` | `7baacb1d45407c0f08a29c23caad331fc47c7b1e` | #895 |
| `grokbot-b11-m13-2012-20261030` | `e2f9ef23bf59b9f2455f875c4d9e53cb727056db` | #896 |
| `grokbot-b12-card-lore-links-20261030` | `f6dc4f15b13263f27056a71002625ca3e4ce1e8d` | #899 |
| `grokbot-b12-docs-20261030` | `e988fd6c7ecb88bd9c907ebcb2bd4d1a45835ffd` | #902 |
| `grokbot-b12-pack-dossiers-20261030` | `6101f57631e34af135b90c77c747ad93fbac6692` | #901 |
| `grokbot-b12-phase1b-snapshot-gates-20261030-v2` | `eaea69759f3ddccb6e151993458b413bb3bf66a5` | #900 |
| `grokbot-b12-pipefail-20261030` | `7f2478be8d0c239d9469f09bedfb9c1ff4cae826` | #898 |
| `grokbot-b13-chronology-20261030` | `2cfc2ee4cbae051002522a9e193be3fd96ab9537` | #904 |
| `grokbot-b13-docs-20261030` | `2a607e4f22820015629687e39d73fe2d675d7998` | #907 |
| `grokbot-b13-flavor-lore-20261030` | `9ec36708c1cf7ee6eec233b3323cd8c43ec679ec` | #903 |
| `grokbot-b13-pack-a-disputes-20261030` | `81885e64e7dba03a86f20e20d73afac3439f0d8e` | #905 |
| `grokbot-b13-sweep-20261030` | `2b5f1415e4067e7f43353303eee6397ad7d3033b` | #906 |
| `grokbot-b14-cert-dry-run-20261030` | `5a473b14fe22bd7d2425cfdc29a4ae022a1e2cd6` | #911 |
| `grokbot-b14-chronology-sources-20261030` | `6ba78354c18ab79f30f7e8d1d64e0d2ba4d5ee1c` | #909 |
| `grokbot-b14-docs-20261030` | `0b6c3910196b669c6ccf81792534117a70567adb` | #912 |
| `grokbot-b14-entity-audit-20261030` | `f6e5739a4733a8b390871cf13136d87cedffd216` | #908 |
| `grokbot-b14-leader-phrasings-20261030` | `988250141aedb4ea52adb8730ad924cda8cf10ff` | #910 |
| `grokbot-b4-docs-fix-20261030` | `0acaadec548336e5e4cc03ab5f2e566c22c73dff` | #850 |
| `grokbot-b4-handoff-20261030` | `2b5c4aa5aa6f3864c8e7fe9e71c2140c487aa457` | #857 |
| `grokbot-b4-lore-links-20261030` | `af27dc8940b21b49ca890baa1fc8f72fb06a3bdd` | #851 |
| `grokbot-b9-aliases-20261030` | `6a7e0000d691ada3706463dcff6db21e5510af67` | #882 |
| `grokbot-b9-authoring-20261030` | `9b0fe348338abc899a54f883f28c16a3cd96a5d2` | #880 |
| `grokbot-b9-handoff-20261030` | `6d683c9773c164d9dd9d41153857f4d4371e6f11` | #884 |
| `grokbot-b9-handoff2-20261030` | `d95070abcd32caed2064aace06a4da2cdcc2d3ef` | #887 |
| `grokbot-b9-recount-era-20261030` | `b7d77e132eb35a894ba0cfb152588158caede870` | #886 |
| `grokbot-b9-reviewed-marker-20261030` | `8a7e7ded71670e624dfb5ce8c2e6095fd3d2c9d5` | #881 |
| `grokbot-b9-untagged-2-20261030` | `2e58f997bb775be29b9931ed0ee3bbcf1aded32d` | #885 |
| `grokbot-b9-untagged-packs-20261030` | `d0aa85804b86e4c3bc007db5a3d6ac5d985e905e` | #883 |
| `grokbot-batch2-handoff-20261030` | `8695d01c08a79e325ae8d2162148b39e434bd77a` | #837 |
| `grokbot-batch3-brief-20261030` | `978f95e9d9e6b61b9c52675bd9665374bbe8c8c4` | #838 |
| `grokbot-batch3-final-handoff-20261030` | `4ca3c0ed48aa6a9c80bdee2db59e1602b4ecde9d` | #849 |
| `grokbot-batch3-handoff-20261030` | `4bb4add7f136c390a251e42f1d685cdad1815b40` | #846 |
| `grokbot-batch5-handoff-20261030` | `ba93fed376dc66d9dfcf30544dbec1ea83748621` | #862 |
| `grokbot-claim-anchors-20261030` | `621eb080d431fc2870009ad6aad758687c3f0fd9` | #853 |
| `grokbot-commander-rules-20261030` | `db9e7f86fa55a37b731a8e4152e7ec90b763205a` | #836 |
| `grokbot-docs-b7-20261030` | `36c8dd8c10ae9f02990f2041d6dd1d09ea509f1e` | #874 |
| `grokbot-docs-batch6-20261030` | `4031d8be57e39a7ae618a93fbb4111457a45823c` | #870 |
| `grokbot-enrichment-b38-20261030` | `7baf7ede8417c4d2bff062715da0eaeebebf253b` | #848 |
| `grokbot-generic-lore-pilot-builder-20261030` | `77e6c6d26206d6f052474312f8acf7a9a31827f2` | #832 |
| `grokbot-graph-pilot2-20261030` | `3d99b02861bd35ad5d7791d6c57606484df74a58` | #834 |
| `grokbot-handoff-b8-final-20261030` | `6360b4332cb89e78462ba85eba6b1d22216d4f14` | #879 |
| `grokbot-koth-wrenn-printings-20261030` | `2a603fef0da922d3c5f690e11928faea4bb8231e` | #854 |
| `grokbot-multiverse-claim-graph-20261030` | `918af2126a17b9d0ed6e7e1d6fac09ca2a9a080a` | #825 |
| `grokbot-overnight-handoff-20261030` | `6032faf5115fcbfa42b516217da85520a53f03d0` | #824 |
| `grokbot-p5-fill-b7-1` | `b08d13599759ea84796e8213aa6142c99334e3c1` | #871 |
| `grokbot-p5-fill-b7-3` | `8448a3c9cd9c289f85ce34ff67a57900e780de8d` | #873 |
| `grokbot-p5-fill-b8-1-20261030` | `1c2937cbf389ba9f100d3c1173a3c5592734719d` | #875 |
| `grokbot-p5-fill-b8-2-20261030` | `754c875ce2ac60d4c2de1e2048a85c8bd1ebbf5e` | #876 |
| `grokbot-p5-fill-b8-3-20261030` | `9a9cf337cc93fe77be7f881fad7858d72291abd7` | #877 |
| `grokbot-p5-neo-pack-20261030` | `007b2a9b4919c520deea4b6583dc98676db70545` | #861 |
| `grokbot-p5-packs-b6a-20261030` | `a77ba4b1908e9f093834e1ef85b1f5ab669eaea7` | #863 |
| `grokbot-p5-packs-b6b-20261030` | `74e65010105d5206b776787272fca97f83733c7f` | #864 |
| `grokbot-p5-packs-b6c-20261030` | `5ee82d4130a1e4113d3cc69c115fdedb0f0aa628` | #865 |
| `grokbot-p5-packs-b6d-20261030` | `538df47d8a5270d6f2ab3b51dbb6a37f6d6e153a` | #867 |
| `grokbot-p5-packs-b7a-20261030` | `95277b764be2a3a75b46b76a82f8e60b4ff8b4e5` | #868 |
| `grokbot-p5-packs-b7b-20261030` | `7d446b9be1dcf4e56b4d0c745b5219fb2d59dc77` | #869 |
| `grokbot-p5-triage-b7-2` | `feef018161f580f83fee9be59682787debdb74cd` | #872 |
| `grokbot-p7-paraphrase-b8-20261030` | `8ee555ac53258a81904ecd7198db5c7eb5fe6196` | #878 |
| `grokbot-p7-rephrased-20261030` | `633d08562417b6e778d802e76d875937dc41b8ec` | #866 |
| `grokbot-pack-a-a003-correction-20261030` | `2d430d2b62c57ff68a4e2b54fcb24947e50f5783` | #835 |
| `grokbot-pack-a-open-questions-20261030` | `b8ff1f4f4a6c7e287bdd98eecf3b0c6735ede252` | #833 |
| `grokbot-pack-anchors-20261030` | `68b9d369320b92d74a765053a6cf7d1ac21f8e1b` | #839 |
| `grokbot-pack-b-thran-brothers-war-20261030` | `52710e8ba9e30ba1f44380ca175fc0de45fb170d` | #826 |
| `grokbot-pack-c-weatherlight-invasion-20261030` | `c5b0af21d4529d25246b5eddeb8d7cea322cfaa1` | #828 |
| `grokbot-pack-c3-one-20261030` | `4a6cc0567bb62cd942ee492913fc9c01ddebb66a` | #847 |
| `grokbot-phase1-oracle-drift-20261030` | `b77401b76871055b556526b7d1e9fda6736279af` | #829 |
| `grokbot-phase7-companion-ask-20261030` | `5eb0ca2aa76141e8dbb6a268c6de82545e31422e` | #827 |
| `grokbot-phase7-relation-tests-20261030` | `208cec004d976d0bffdde63fa95a556eeb38cf9a` | #859 |
| `grokbot-phase8-release-readiness-20261030` | `23c294e610af039c49886b8642d98e361acb3ead` | #830 |
| `grokbot-pilot3-ugin-allies-20261030` | `2ff74cc491e758de700b20f25b76263d3354bd29` | #842 |
| `grokbot-pilot3-ugins-allies-20261030` | `d7bdca2cf9d27e3ff795c664f90db9730805460d` | #844 |
| `grokbot-rtd-extraction-20261030` | `556e4ed6162a73e17f6d559c18b115373c1c9787` | #841 |
| `grokbot-rules-interactions-20261030` | `2ada9513666a26c3272a538e2a095d50dcf5aa16` | #840 |
| `grokbot-story-art-captions-20261030` | `37f8615da34311a1eb0eddb5a69f12eef3edfffa` | #843 |
| `grokbot-story-claim-pipeline-20261030` | `a850dd3651c03ba689e1cfa1b5b130082b8a4714` | #858 |
| `grokbot-story-coverage-20261030` | `1f0bcea02dcfb4b52fa5d305eaaa7b6b9397b07a` | #856 |
| `grokbot-story-image-labels-20261030` | `680f836bbae9dab2dc8b1502e21fd3139a49b944` | #860 |
| `grokbot-workflow-v228-20261030` | `8ee1d4385d905bee01c7d6bee14fedb921939242` | #831 |

## Preserved — never-delete list

- `chatgpt-abaddon-rev3-owner-receipt-canonical-verified-20261023` `6ca2e52ea2e9a8570691324af019486e37043859`
- `chatgpt-cycle76-m6-refinement` `778a9101d0b831d3b7692d6eb50dd43876e48a68`
- `chatgpt-m7-lord-approved-case-transfer-20261025` `0d4c51d2c5756a0c6207fe4b5d47d4e8afdd0920`
- `main` `cf248059585f2c56ecf015b208d92d2aa355d3de`

PR #650 head `chatgpt-abaddon-rev3-owner-receipt-canonical-verified-20261023` and PR #707 head `chatgpt-m7-lord-approved-case-transfer-20261025` are both on this list.

## Preserved — merged into `main` but kept (flagged for owner review)

Their commits are already in `main`; the names are kept only because something cites them or they are current.

| Name | Head SHA | Reason |
|---|---|---|
| `bot-cycle15` | `f5e9f6e006bc5fc14247bd983f395b92f4a87851` | branch name referenced by files on retained branch heads: Update Log.md |
| `bot-cycle16-grixis` | `0a3e74f40ead61e2d2b1f37ac62993d5680349a2` | branch name referenced by files on retained branch heads: Update Log.md |
| `bot-cycle17-schema-validation` | `9e343b9cb2dea3d3c8cb244cb408bc6e8a093a82` | branch name referenced by files on retained branch heads: Update Log.md |
| `bot-cycle18-crossrefs` | `712870dccf0ed42c0034f41cdb1e244a1d8fc545` | branch name referenced by files on retained branch heads: Update Log.md |
| `bot-cycle19-calibration` | `129de5b939aaf2fe36734ef2b0d0bf9d9afde4dc` | branch name referenced by files on retained branch heads: Update Log.md |
| `bot-cycle4` | `2b26624a05c329f831073690fc0a1f2d9e2a2987` | branch name referenced by files on retained branch heads: grixis/Grixis Authority Gap Analysis.md |
| `bot-cycle6` | `ff20bfd6c0c42becdd0243d6a4a0077a54f46c9b` | branch name referenced by files on retained branch heads: Update Log.md |
| `bot-cycle7` | `829159bd91f283469a3665cd7c74681145d87361` | branch name referenced by files on retained branch heads: Update Log.md |
| `bot-cycle8` | `4e575c22ccff9b06a7efb5149a7e681180b051b7` | branch name referenced by files on retained branch heads: Update Log.md |
| `bot-cycle9` | `5f899dae3b070e5ca8286a2b02fec6c59b4110a1` | branch name referenced by files on retained branch heads: Update Log.md |
| `chatgpt-foundation-source-recovery-v296-20261101` | `cf2f7ec7268797e70788279b760ae41f8a7067b1` | branch name cited as provenance/evidence location in handoffs/CHATGPT_FOUNDATION_V296_2026-11-01.md |
| `chatgpt-phase1b-boxed-schemes-planechase-20261029` | `736759bb99916a18e881e02ed8d0fd7184a34637` | branch name referenced by files on retained branch heads: .github/workflows/phase1b-boxed-precon.yml |
| `chatgpt-phase1b-boxed-special-lair-global-20261029` | `38f900f532c49514404cd2db2ff4d817735d81c1` | branch name referenced by files on retained branch heads: .github/workflows/phase1b-boxed-special-lair-global.yml |
| `chatgpt-phase1b-boxed-specialty-20261029` | `199bedaf9fa7d1e2262b720c51a63ab616ffd040` | branch name referenced by files on retained branch heads: .github/workflows/phase1b-boxed-specialty.yml |
| `chatgpt-phase1b-commander-modern-20261029` | `e9cc7863f344be4d2e0268ffb0019e6a3e017de7` | branch name referenced by files on retained branch heads: .github/workflows/phase1b-commander-modern.yml |
| `chatgpt-phase1b-commander-series-20261029` | `53a6bed92231c4f6bde944808712d7a779a64ffa` | branch name referenced by files on retained branch heads: .github/workflows/phase1b-commander-series.yml |
| `chatgpt-phase1b-commander-set-linked-20261029` | `ec858095a968c378ab531ba9a22587f2303da6e7` | branch name referenced by files on retained branch heads: .github/workflows/phase1b-commander-set-linked.yml |
| `chatgpt-phase1b-cross-category-20261029` | `91d5c1ef20611ebce6554d97fecc786b72e55ddb` | branch name referenced by files on retained branch heads: .github/workflows/phase1b-cross-category.yml |
| `chatgpt-phase1b-draft-starter-final-evidence-20261029` | `026b394168a14ba21bf31150759b9e66ec4bb216` | branch name referenced by files on retained branch heads: .github/workflows/phase1b-draft-starter-batch2.yml |
| `chatgpt-phase1b-draft-starter-source-batch-20261029` | `323561656cd347a36da3253211435a794b6d8cde` | branch name referenced by files on retained branch heads: .github/workflows/phase1b-draft-starter-sources.yml |
| `chatgpt-phase1b-duel-decks-20261029` | `022b95c7dcfe5188105e75ae24eab9ee0e54a6de` | branch name referenced by files on retained branch heads: .github/workflows/phase1b-duel-decks.yml |
| `chatgpt-phase1b-historic-shards-20261029` | `e78d65699f81b6b6e76b1480167b5350ed743e8a` | branch name referenced by files on retained branch heads: .github/workflows/phase1b-historical-shards.yml |
| `chatgpt-phase1b-inserts-clash-spellbook-20261029` | `42a5418037c79e865513d81d90890e63e080cdb4` | branch name referenced by files on retained branch heads: .github/workflows/phase1b-inserts-clash-spellbook.yml |
| `chatgpt-phase1b-premier-1993-2002-20261029` | `a2198c2138d8305785a6b1f4a8e4e6b4ced1e898` | branch name referenced by files on retained branch heads: .github/workflows/phase1b-wotc-early-sets.yml |
| `chatgpt-phase1b-premier-2003-2022-20261029` | `f5c6c154c2a5f683897a975e245017cd068bf87a` | branch name referenced by files on retained branch heads: .github/workflows/phase1b-wotc-mid-sets.yml |
| `chatgpt-phase1b-product-family-triage-20261029` | `d24e7211b74b46631f0aa56c29471cab53fdc1cf` | branch name referenced by files on retained branch heads: .github/workflows/phase1b-product-family-triage.yml |
| `chatgpt-phase1b-reprint-curated-source-batch-20261029` | `1652aa972d3b234ede948aaa89d239fe8b3428d7` | branch name referenced by files on retained branch heads: .github/workflows/phase1b-reprint-curated.yml |
| `chatgpt-phase1b-set-products-20261029` | `f88716b63c242982185a5ef96adbf64ce5d2d6c1` | branch name referenced by files on retained branch heads: .github/workflows/phase1b-set-products.yml |
| `chatgpt-phase1b-wotc-premier-20261029` | `e06c5e7d58762653dd1789a12d49f9ffb902526f` | branch name referenced by files on retained branch heads: .github/workflows/phase1b-wotc-premier.yml |
| `chatgpt-v310-owner-approval-index-20261102` | `acedc3c4abae2b449fc93a6e8600f966622d120b` | head committed 2026-11-02; recent/possibly active development or owner-approval-index branch |
| `chatgpt-v310-reliability-usability-20261102` | `6300af9bf2a2dacff60e4eb42c309842dae9d5a3` | head committed 2026-11-02; recent/possibly active development or owner-approval-index branch |
| `chatgpt-v311-exact-pilot-approvals-20261102` | `e0da186a03796ac7e9a6e1a78e9e91e549551b99` | head committed 2026-11-02; recent/possibly active development or owner-approval-index branch |
| `chatgpt-v312-archive-upkeep-deck9-pr-reconciliation-20261102` | `e419e572accfc973af8977e0f726f6f2f25a982d` | head committed 2026-11-02; recent/possibly active development or owner-approval-index branch |
| `grokbot-c4-mom-20261030` | `9bb44f9a338a7d7768a4351dd0e49f850787758e` | branch name cited as provenance/evidence location in MTG_MULTIVERSE_MASTER_WORKFLOW.md |
| `grokbot-edge-eras-20261030` | `4b279723d8a408f4f82d798e1a47c730937c79fd` | branch name cited as provenance/evidence location in MTG_MULTIVERSE_MASTER_WORKFLOW.md |
| `grokbot-ugin-bolas-duality-pilot-20261030` | `a3e0c3a5bfdfdb9780a854a25f3803fc43569e12` | branch name cited as provenance/evidence location in handoffs/GROKBOT_OVERNIGHT_2026-10-30.md (approved Phase 6 Pilot 1 provenance) |

## Preserved — not merged into `main` (636)

Every one has commits and file content that do not exist in `main` history. They hold Grixis M6/M7/M8 research, owner-gate work, lore, rules and source evidence and are **kept**. The JSON lists each with its unique-commit and unique-blob counts.

By name prefix: `chatgpt` 457, `jlk` 124, `grokbot` 35, `m7` 7, `audit` 3, `closeout` 3, `reconcile` 3, `grixis` 2, `deck41` 1, `research` 1.

Manual-review note: 439 of these heads are fully contained in another retained branch (417 inside `chatgpt-cycle76-m6-refinement`). They are still kept: the deletion rule requires reachability from `main`, and pruning them would need an explicit owner decision.

