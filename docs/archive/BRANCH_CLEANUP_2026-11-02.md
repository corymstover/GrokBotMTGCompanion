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


## Execution record (added after deletion)

All 213 proposed deletions were executed on 2026-11-02 between 05:15 and 05:21 CST, after this manifest merged in PR #984 (merge commit `92fcef2c4bf6ef6a105c631053f35d52c2e36266`). Each ref was deleted individually with `gh api -X DELETE .../git/refs/heads/<exact-name>` only after its remote SHA matched the manifest (re-checked immediately before the delete) and its basis (ancestor of current `main`, or retained twin at the same SHA) was re-verified. No deletion was skipped or stopped. Batches: 12 duplicates, then 3 × 67 merged branches (disjoint ranges; the last two merged batches ran concurrently, so the full re-verification ran after batch 1, after batch 2, and after batches 3–4 together). After each verification, `main`, the four never-delete branches and all 676 preserved branches were confirmed at their manifest SHAs.

- Per-branch log (name, SHA, basis, batch, time): [`data/maintenance/branch_cleanup_execution_2026-11-02.json`](../../data/maintenance/branch_cleanup_execution_2026-11-02.json)
- Branch count: 889 before → 677 after (676 preserved + the merged `grokbot-branch-cleanup-manifest-20261102` head).
- Recovery: `git push origin <head_sha>:refs/heads/<name>`.
- Root Markdown clutter (Part 4): **no files moved.** Every root `.md` is either a registered knowledge-base page in `scripts/front_matter.py` `PAGES` (whose computed `related:` lists reach protected `grixis/` pages; for example `grixis/Grixis Mission.md` lists `ROADMAP.md`), or a listed operations doc that `README.md`/`AGENTS.md` still cite as current. Moving any of them would change protected files or live entry points, so all were left in place.

## Containment candidates (second manifest — PROPOSED, NOT EXECUTED)

**No branch listed here has been deleted.** This section records a second, exact-SHA candidate list for Cory's separate decision. Full data: [`data/maintenance/branch_containment_manifest_2026-11-02.json`](../../data/maintenance/branch_containment_manifest_2026-11-02.json).

### Reconciling 439 (manifest #984) vs 451 (earlier report)

Both numbers use the same test: a head is "contained" when it is not an independent tip under `git merge-base --independent` over all heads that are not ancestors of `main`. The 451 was computed over the **pre-deletion** set of 651 non-ancestor names, which still included the **12 exact-duplicate names** that #984 proposed and batch 1 then deleted (each shared its SHA with a retained, itself-contained twin). #984's preserved list, and a re-run on live refs today, both give **439**. The same cause explains the report's 430 contained-in-cycle76 figure (= 417 preserved + those 12 + cycle76 counted as its own ancestor) and its prefix breakdown summing to 651 (correct preserved non-ancestor total: **639** = 636 + the 3 non-ancestor never-delete branches; chatgpt 460, not 472). The two cleanup branches created after #984 are ancestors of `main` and are in neither count.

The 12 names in the difference: `chatgpt-abaddon-final-j-oracle-capture-20261022`, `chatgpt-abaddon-final-m6-ij-20261022`, `chatgpt-abaddon-m6-6-7-adjudication-20261022`, `chatgpt-abaddon-m6-j-candidate-mana-redteam-20261022`, `chatgpt-abaddon-m7-opportunity-reopen-20261022`, `chatgpt-abaddon-owner-ready-m6-ij-20261022`, `chatgpt-abaddon-p0-030-ledger-20261022`, `chatgpt-abaddon-p0-030-threshold-doublers-20261022`, `chatgpt-abaddon-persist-full-oracle-20261022`, `chatgpt-abaddon-remaining-p1-20261022`, `chatgpt-abaddon-residual-p1-reconciliation-20261022`, `chatgpt-m7-no-few-swaps-owner-hard-gate-20261022`.

### Method

- Live refs: 678 branches, main `7f38eb000be474416d59542c639a0d9aec1ab09f`; 639 non-ancestor branches, 200 independent tips, 439 contained.
- Containers must be non-candidates. Only never-delete branches are accepted; in practice every candidate is contained in `chatgpt-cycle76-m6-refinement` (`778a9101d0b831d3b7692d6eb50dd43876e48a68`), proved per branch with `git merge-base --is-ancestor`.
- Every blob in every live branch head (678 heads incl. main, cycle76, #650/#707 heads, grokbot-m7-production-ledger and all *-ledger/approval branches; 13,597 distinct blobs) was tokenised on [A-Za-z0-9_.-] (so `origin/<name>`, `compare/a...<name>` and URL forms match; names containing '/' matched by substring) and checked for an exact branch name. Excluded only the pure inventories that list every branch: data/maintenance/github_branch_heads_2026-11-02.json, data/maintenance/branch_cleanup_manifest_2026-11-02.json, data/maintenance/branch_cleanup_execution_2026-11-02.json, docs/archive/BRANCH_CLEANUP_2026-11-02.md.
- Titles and bodies of all 985 issues/PRs (every state) and all 146 issue/PR conversation comments; 0 PR review comments exist.
- 0 open PRs; 0 protected branches; 0 rulesets; PR base-branch use; head author/committer date vs 2026-10-26 (7 days); every candidate's recorded PR head SHA equals its branch head.
- Any name reference, head commit on/after 2026-10-26, use as a PR base, a container that is not never-delete, or a shared SHA ⇒ **KEEP**.

### Result: 327 candidates, 112 contained branches kept

Kept by primary reason: name_referenced_in_repo_files 88, head_commit_within_last_7_days 20, only_container_is_not_never_delete 3, name_referenced_in_github_pr_or_issue_text 1. If every candidate were deleted, the branch count would go from 678 to 351 (before counting new PR branches).

Execution, if approved, must re-verify each name+SHA with `git ls-remote` immediately before each one-at-a-time delete, re-check containment in cycle76 at its recorded SHA, and stop on any mismatch. Recovery: `git push origin <head_sha>:refs/heads/<name>`.

#### Candidates (all contained in `chatgpt-cycle76-m6-refinement`)

| # | Branch | Head SHA | PR(s) |
|---|---|---|---|
| 1 | `chatgpt-abaddon-final-ij-frozen-20261022` | `d54cad9f6c4a90bc7476164b2f5f0ebd75d507bd` | #572 closed-unmerged→chatgpt-cycle76-m6-refinement |
| 2 | `chatgpt-abaddon-full-oracle-frozen-20261022` | `6cf0b8cf37305bf08f318f621ca7f06b60bdde8e` | #571 merged→chatgpt-cycle76-m6-refinement |
| 3 | `chatgpt-abaddon-ij-strict-final-frozen-20261022` | `ef42d0a1fdaa1e4b3987df2d3d57477d89f0a6ef` | #573 merged→chatgpt-cycle76-m6-refinement |
| 4 | `chatgpt-abaddon-inclusive-cascade-oracle-fix-20261022` | `4e8a07d4c34007e0a0ee742e33c681f5ca42f095` | #619 merged→chatgpt-cycle76-m6-refinement |
| 5 | `chatgpt-abaddon-m6-6-7-fixed-frozen-20261022` | `5c84c4a5e1ceb436bc315bb197f93a537cd444f0` | #569 merged→chatgpt-cycle76-m6-refinement |
| 6 | `chatgpt-abaddon-m6-6-7-frozen-20261022` | `ce07ad21813d2446359cd83cf1e5822cf3a4d8e6` | #568 closed-unmerged→chatgpt-cycle76-m6-refinement |
| 7 | `chatgpt-abaddon-m6-7-final-choice-20261022` | `dc92c49a4127351a7f4c1dd93c0c3a3237882988` | #559 merged→chatgpt-cycle76-m6-refinement |
| 8 | `chatgpt-abaddon-m6-coverage-i-block-20261022` | `9b516714e856ec3fa9dbb78940668e5e8f765cee` | #552 merged→chatgpt-cycle76-m6-refinement |
| 9 | `chatgpt-abaddon-m6-coverage-ledger-20261022` | `0ca360e0c954a6f14c4e70dcd27c682b941d9fbc` | #541 merged→chatgpt-cycle76-m6-refinement |
| 10 | `chatgpt-abaddon-m6-evidence-preflight-20261022` | `7362fba0a86bb42d73342677defe35dc18baf2e3` | #551 merged→chatgpt-cycle76-m6-refinement |
| 11 | `chatgpt-abaddon-m6-j-validated-source-crosswalk-20261022` | `875752deda9c4b93f6efb6f1c05093a55d27f46d` | #562 merged→chatgpt-cycle76-m6-refinement |
| 12 | `chatgpt-abaddon-m6-p0-tested-pool-20261022` | `58623406fe99758c2483d1d954049c9c569d8f0e` | #547 merged→chatgpt-cycle76-m6-refinement |
| 13 | `chatgpt-abaddon-m7-cascade-mv-cost-stage6-20261022` | `ce0f991f3986bcf06cf49b27c87ebf5402ab2368` | #623 merged→chatgpt-cycle76-m6-refinement |
| 14 | `chatgpt-abaddon-m7-decisive-comparison-20261022` | `06b87c190079dff8bd89430b5e713f7a400bd9d8` | #546 merged→chatgpt-cycle76-m6-refinement |
| 15 | `chatgpt-abaddon-m7-final-owner-ready-rev2-20261022` | `ad8ad6fa5c4ce36985ab348dc4ef81a611a40c11` | #582 merged→chatgpt-cycle76-m6-refinement |
| 16 | `chatgpt-abaddon-m7-harmonic-payable-stage5-20261022` | `a2fec6581570eba35047b986a29637bbd5e81cca` | #622 merged→chatgpt-cycle76-m6-refinement |
| 17 | `chatgpt-abaddon-m7-live-oracle-gate-20261022` | `2e987dd61ae09f9f0240ffeca6c441904fe80d76` | #545 merged→chatgpt-cycle76-m6-refinement |
| 18 | `chatgpt-abaddon-m7-open-ended-packages-stage4-20261022` | `593f3fc5746daf68ec931ac82a7ff497c33596f4` | #621 merged→chatgpt-cycle76-m6-refinement |
| 19 | `chatgpt-abaddon-m7-oracle-mechanics-stage3-20261022` | `4693f25d72a01bc702c1bf63f16fe942ff6e020b` | #620 merged→chatgpt-cycle76-m6-refinement |
| 20 | `chatgpt-abaddon-m7-reopen-frozen-20261022` | `d899fb4f829bab33a646d30cfb9cd9d222eae51c` | #575 merged→chatgpt-cycle76-m6-refinement |
| 21 | `chatgpt-abaddon-m7-rev2-mechanics-20261022` | `655c5968a4652b973772eb8cc01c6972b1af64be` | #579 merged→chatgpt-cycle76-m6-refinement |
| 22 | `chatgpt-abaddon-m7-six-swap-source-review-20261022` | `d8f3a7b4fb2b96af3f8b1055fb10d4ae53114c6d` | #578 merged→chatgpt-cycle76-m6-refinement |
| 23 | `chatgpt-abaddon-m7-sourcebound-staging-20261022` | `9fd2add98fef228487db15d9cdf52968c2319cec` | #560 merged→chatgpt-cycle76-m6-refinement |
| 24 | `chatgpt-abaddon-m7-stage7-interference-packages-20261022` | `df91bd36b6ece821be9ee548e992fa3f9cb044e4` | #624 merged→chatgpt-cycle76-m6-refinement |
| 25 | `chatgpt-abaddon-m7-stage8-impact-tremors-offranking-20261022` | `54b9c2bbb2f6f846e460d35a4547f175339a73db` | #626 merged→chatgpt-cycle76-m6-refinement |
| 26 | `chatgpt-abaddon-m7-stage9-durable-continuation-20261022` | `a1e8e78ecd19535cb6817387dc51ca5e0ba9cfb1` | #628 merged→chatgpt-cycle76-m6-refinement |
| 27 | `chatgpt-abaddon-m7-stage9-veyran-trigger-crosswalk-20261022` | `09078f2dd510ae68809e9c15267bc40ed65f5c54` | #627 merged→chatgpt-cycle76-m6-refinement |
| 28 | `chatgpt-abaddon-minds-desire-p0-029-20261022` | `adb073c7fa29b3f812565511e9b54b4d40e9712f` | #558 merged→chatgpt-cycle76-m6-refinement |
| 29 | `chatgpt-abaddon-oracle-j-frozen-20261022` | `fd143871f84b21ccb03ff8714f5a3df597bd83f1` | #570 merged→chatgpt-cycle76-m6-refinement |
| 30 | `chatgpt-abaddon-owner-ready-frozen-20261022` | `7359216b52f0406261cb03fc6801b7e98ebe2066` | #574 merged→chatgpt-cycle76-m6-refinement |
| 31 | `chatgpt-abaddon-p0-021-call-forth-20261022` | `422a55c6466274ea899a7cf37837164fc03716f5` | #548 merged→chatgpt-cycle76-m6-refinement |
| 32 | `chatgpt-abaddon-p0-022-suspend-20261022` | `13fb5896589a74bd398ee7b517da6b0e3b7f58e0` | #549 merged→chatgpt-cycle76-m6-refinement |
| 33 | `chatgpt-abaddon-p0-023-breach-led-freeze-20261022` | `c8946e87a3acb81e0884a804744210bb3ffb6122` | #550 merged→chatgpt-cycle76-m6-refinement |
| 34 | `chatgpt-abaddon-p0-024-wild-magic-20261022` | `3f2c089e68083e345fd94ab7ffc49593a815ad5a` | #553 merged→chatgpt-cycle76-m6-refinement |
| 35 | `chatgpt-abaddon-p0-025-nalfeshnee-20261022` | `78e88638d9c03f3be25733692907cc0fb01dd535` | #554 merged→chatgpt-cycle76-m6-refinement |
| 36 | `chatgpt-abaddon-p0-026-archaeologist-20261022` | `a55e1bd8b6956e37933494f3a90234021b06351a` | #555 merged→chatgpt-cycle76-m6-refinement |
| 37 | `chatgpt-abaddon-p0-027-prosper-20261022` | `d32d3bbe9374d50fc02ab62b1fcb5e5dcafd3e91` | #556 merged→chatgpt-cycle76-m6-refinement |
| 38 | `chatgpt-abaddon-p0-028-storm-kiln-20261022` | `07dec977d4a02a985e17444b5f05693dd273e9f9` | #557 merged→chatgpt-cycle76-m6-refinement |
| 39 | `chatgpt-abaddon-p0-030-exact-head-20261022` | `029fdb9a8fdefe2ef81be09be6dc03cb54c59d30` | #564 merged→chatgpt-cycle76-m6-refinement |
| 40 | `chatgpt-abaddon-p0-030-ledger-exact-head-20261022` | `139c97118e8436f0b160a10a8025fc05906cc7e6` | #565 merged→chatgpt-cycle76-m6-refinement |
| 41 | `chatgpt-abaddon-p1-final-frozen-20261022` | `fb5a4a7e56e9b428304274045d8a9f16d71f789a` | #567 merged→chatgpt-cycle76-m6-refinement |
| 42 | `chatgpt-abaddon-p1-frozen-head-20261022` | `b872f7aa9821068458eddda1bea593ed8e6998be` | #566 merged→chatgpt-cycle76-m6-refinement |
| 43 | `chatgpt-abaddon-post-admiral-edhrec-reopen-20261022` | `c793c4b895cf08e623655f8a363e13895cd1e10c` | #618 merged→chatgpt-cycle76-m6-refinement |
| 44 | `chatgpt-abaddon-rev2-100-oracle-archive-20261022` | `af16ffa583e93f260456702182ffd8b9a20ceccd` | #580 merged→chatgpt-cycle76-m6-refinement |
| 45 | `chatgpt-abaddon-rev2-ij-packet-draft-20261022` | `20de5e441c237310d017b42824b44f5e98746466` | #581 merged→chatgpt-cycle76-m6-refinement |
| 46 | `chatgpt-abaddon-rev3-callforth-oracle-erratum-20261023` | `f22b79e0e0bce13d56d50c106bcf2f725a7a4499` | #648 merged→chatgpt-cycle76-m6-refinement |
| 47 | `chatgpt-abaddon-rev3-owner-lock-receipt-20261023` | `f77390369c54f4b62286868b7116ef1036de6698` | #649 merged→chatgpt-cycle76-m6-refinement |
| 48 | `chatgpt-abaddon-rev3-owner-ready-checkpoint-20261023` | `7003f7fa5a83bac64e87d82dd2a8e0830b2f7dcc` | #646 merged→chatgpt-cycle76-m6-refinement |
| 49 | `chatgpt-abaddon-stage10-familiar-combo-adversarial-20261022` | `e25938f9e7221302701dd3f40db675f2b76121e8` | #629 merged→chatgpt-cycle76-m6-refinement |
| 50 | `chatgpt-abaddon-stage10-merge-receipt-ledger-20261022` | `d7b4ff4a4764f1c4b0ff988933557bfae98e143d` | #630 merged→chatgpt-cycle76-m6-refinement |
| 51 | `chatgpt-abaddon-stage11-precombat-shrine-token-quality-20261022` | `9a01064f97d0d06b54577991ed46469b039afea5` | #631 merged→chatgpt-cycle76-m6-refinement |
| 52 | `chatgpt-abaddon-stage11-provenance-ledger-20261022` | `c0c922f524aab7966a5add23aec8c37015a01281` | #632 merged→chatgpt-cycle76-m6-refinement |
| 53 | `chatgpt-abaddon-stage12-openended-portfolios-20261022` | `11679ef47b7bc38801412994795f47ba5898a6d9` | #633 merged→chatgpt-cycle76-m6-refinement |
| 54 | `chatgpt-abaddon-stage12-provenance-ledger-20261022` | `9c5ff452baa83d4bc1f15dbbd56a8fb7eb1437fa` | #634 merged→chatgpt-cycle76-m6-refinement |
| 55 | `chatgpt-abaddon-stage13-mage-protected-engine-20261023` | `314d19d6a86ae5f1f0f4141b84233132003745a6` | #635 merged→chatgpt-cycle76-m6-refinement |
| 56 | `chatgpt-abaddon-stage14-protected-six-preflight-20261023` | `e1ff4b45939936dbca2dbc7701b14a969ad41242` | #636 merged→chatgpt-cycle76-m6-refinement |
| 57 | `chatgpt-abaddon-stage14-provenance-ledger-20261023` | `532d7d729935c3315ea2b48b1ea5d047ac5451cd` | #637 merged→chatgpt-cycle76-m6-refinement |
| 58 | `chatgpt-abaddon-stage15-execution-receipt-20261023` | `a114c58d51589e0720e7895303de5759a69d4700` | #639 merged→chatgpt-cycle76-m6-refinement |
| 59 | `chatgpt-abaddon-stage15-targeted-m6-changed-fixtures-20261023` | `7d4c079d0f7420753608254ddb33f63e6b8a4fd5` | #638 merged→chatgpt-cycle76-m6-refinement |
| 60 | `chatgpt-abaddon-stage16-reconcile-legacy-fixtures-20261023` | `b3d9d1d6e3a8e857e52efd346d0483782e379462` | #640 merged→chatgpt-cycle76-m6-refinement |
| 61 | `chatgpt-abaddon-stage17-complete-95-oracle-source-20261023` | `f23bec193bf6626d7e8d34d622adeadfaf864248` | #641 merged→chatgpt-cycle76-m6-refinement |
| 62 | `chatgpt-abaddon-stage18-changed-mana-redteam-20261023` | `b5f4b598cbd22ac00741430f1d62ebb2b4930609` | #642 merged→chatgpt-cycle76-m6-refinement |
| 63 | `chatgpt-abaddon-stage19-legacy-betrayal-correction-20261023` | `b92c3a149f79bccbc53f445d409f78255ffb6fb3` | #643 merged→chatgpt-cycle76-m6-refinement |
| 64 | `chatgpt-abaddon-stage20-new-exact-six-ij-20261023` | `407205fce4b8f79e353f101059719afd30bbfbe4` | #644 merged→chatgpt-cycle76-m6-refinement |
| 65 | `chatgpt-abaddon-stage21-owner-review-gate-20261023` | `6dea40fb11b1cbaf366ea90f14e5bf3b0e36ca3c` | #645 merged→chatgpt-cycle76-m6-refinement |
| 66 | `chatgpt-abaddon-stage7-continuation-receipt-20261022` | `74b6d835e022358c5d053b6e00aca191237876f6` | #625 merged→chatgpt-cycle76-m6-refinement |
| 67 | `chatgpt-admiral-candidate-d-effect-coverage-adversarial-20261022` | `6df80bbf93126146b497f35e57dff702927ca1d4` | #596 merged→chatgpt-cycle76-m6-refinement |
| 68 | `chatgpt-admiral-ij-hash-pool-and-reports-20261022` | `05b42affdfc25b8f9b31aad616b9e0c044645f5d` | #597 merged→chatgpt-cycle76-m6-refinement |
| 69 | `chatgpt-admiral-m6-6-7-scope-closure-20261022` | `456b5eb5b76aae8cb7a8380950352a3a8dbf852b` | #599 merged→chatgpt-cycle76-m6-refinement |
| 70 | `chatgpt-admiral-m6-i-four-package-effects-20261022` | `3196e72560fd22c2d88628d8e336506c791d8967` | #598 merged→chatgpt-cycle76-m6-refinement |
| 71 | `chatgpt-admiral-m6-i-scoped-five-list-closure-20261022` | `dc7b208474672e8e32a96caef89e815c03dd0b8b` | #600 merged→chatgpt-cycle76-m6-refinement |
| 72 | `chatgpt-admiral-m6-j-candidate-d-bundle-20261022` | `b1a0e219f379433ce38289294559f60d78c6c23a` | #601 merged→chatgpt-cycle76-m6-refinement |
| 73 | `chatgpt-admiral-m7-evasion-horizon-20261022` | `3cd43995f7983f85b91f439e895b543220f91dab` | #606 merged→chatgpt-cycle76-m6-refinement |
| 74 | `chatgpt-admiral-m7-ledger-tracker-20261022` | `a04904624f2dc3ca77d0be74af53d6d20a4e6be7` | #603 merged→chatgpt-cycle76-m6-refinement |
| 75 | `chatgpt-admiral-m7-owner-packet-20261022` | `089d355e7b59433c2527036f8546ec7c0b768e63` | #602 merged→chatgpt-cycle76-m6-refinement |
| 76 | `chatgpt-admiral-m7-owner-receipt-abaddon-reopen-20261022` | `f7ced4fcd3e8ffa34244755cdd6bb1418e1557f5` | #617 merged→chatgpt-cycle76-m6-refinement |
| 77 | `chatgpt-admiral-m7-reassessment-ci-handoff-20261022` | `30ec4cade304cf0dd949a44acf750a339bf65f0a` | #607 merged→chatgpt-cycle76-m6-refinement |
| 78 | `chatgpt-admiral-source-and-paid-effects-20261022` | `23f58845555619aa8042725df6b4ada4fb015b55` | #608 merged→chatgpt-cycle76-m6-refinement |
| 79 | `chatgpt-admiral-stage6-threshold-comparison-20261022` | `e1ff457f58a63ec709a2be327aedbb8933b0d66e` | #609 merged→chatgpt-cycle76-m6-refinement |
| 80 | `chatgpt-admiral-unbounded-six-seven-20261022` | `e14eaa92e9970653ef25ff7cb9abdb8dc138d6da` | #605 merged→chatgpt-cycle76-m6-refinement |
| 81 | `chatgpt-jlk-pass-c-ledger-01-20261021` | `7a74d1f644eadc82faf1eb12c6bcae05b0221968` | #374 merged→chatgpt-cycle76-m6-refinement |
| 82 | `chatgpt-jlk-pass-c-ledger-02-20261021` | `3fcbea741bcb4dacc0000241dd3fa1523f6cac5a` | #376 merged→chatgpt-cycle76-m6-refinement |
| 83 | `chatgpt-lord-xander-m7-rev1-20261025` | `fcff8a8a4aa184c144daaaab4f12974d7ed486d4` | #708 merged→chatgpt-cycle76-m6-refinement |
| 84 | `chatgpt-m6-abaddon-cascade-evidence-ledger-20261021` | `52f8d51a840754be2900bfda9c12fc0d2e6b168d` | #523 merged→chatgpt-cycle76-m6-refinement |
| 85 | `chatgpt-m6-abaddon-cascade-hit-20261021` | `e326ea9135dc707851cf48acabe2280be2561244` | #522 merged→chatgpt-cycle76-m6-refinement |
| 86 | `chatgpt-m6-abaddon-chaos-warp-stax-20261021` | `876ddc549a4ffa60eaed873125118e124a1b1dd9` | #516 merged→chatgpt-cycle76-m6-refinement |
| 87 | `chatgpt-m6-abaddon-chronological-casting-20261021` | `cf510fd1d82b8ead9ce0e2b83f0be6f291df8ac4` | #514 merged→chatgpt-cycle76-m6-refinement |
| 88 | `chatgpt-m6-abaddon-chronological-ledger-20261021` | `1824645e2400be516edf1dff867af61cd18e00c6` | #515 merged→chatgpt-cycle76-m6-refinement |
| 89 | `chatgpt-m6-abaddon-decision-grade-20261021` | `bf89b477a3891fd0e97a8c2536d187715dcd2e6c` | #509 merged→chatgpt-cycle76-m6-refinement |
| 90 | `chatgpt-m6-abaddon-evidence-closure-20261021` | `895b8abe29ff8b12866d304c2b50e6526a0eacc8` | #513 merged→chatgpt-cycle76-m6-refinement |
| 91 | `chatgpt-m6-abaddon-factorial-ledger-20261022` | `4e9890a22a842b3b09509d6769fc3784cd7d0dc7` | #533 merged→chatgpt-cycle76-m6-refinement |
| 92 | `chatgpt-m6-abaddon-factorial-ramp-cascade-20261022` | `1f5c316c83689c004bd2fe71ba89ea851e7d535e` | #532 merged→chatgpt-cycle76-m6-refinement |
| 93 | `chatgpt-m6-abaddon-hand-ramp-20261022` | `325d1445682d414359411790cde66f6802946d36` | #526 merged→chatgpt-cycle76-m6-refinement |
| 94 | `chatgpt-m6-abaddon-hand-ramp-ledger-20261022` | `c08283d02c2d9f50753176eddd7f6344f55fe4f2` | #527 merged→chatgpt-cycle76-m6-refinement |
| 95 | `chatgpt-m6-abaddon-ignus-ledger-20261021` | `7c4c8038984c69d1519f916b1b0bece93507d7fc` | #519 merged→chatgpt-cycle76-m6-refinement |
| 96 | `chatgpt-m6-abaddon-ignus-paid-access-20261021` | `a8ca1a80b278d0dcf0784443ab4ef1e9047d47cd` | #520 merged→chatgpt-cycle76-m6-refinement |
| 97 | `chatgpt-m6-abaddon-ignus-paid-evidence-ledger-20261021` | `a1a2e759f5eddce0b892256d6f16d446c40cf742` | #521 merged→chatgpt-cycle76-m6-refinement |
| 98 | `chatgpt-m6-abaddon-ignus-priority-20261021` | `f4fcefbb914a4e5d61a33db9c9b8bf04e8bf095f` | #518 merged→chatgpt-cycle76-m6-refinement |
| 99 | `chatgpt-m6-abaddon-ignus-shared-effects-20261022` | `fae04f55c8d6a5a4cdac90d5db02b4677fb78b35` | #524 merged→chatgpt-cycle76-m6-refinement |
| 100 | `chatgpt-m6-abaddon-ignus-stack-windows-20261022` | `321cdddb9947ac26ab81c7eeb62a4566e0cc4815` | #528 merged→chatgpt-cycle76-m6-refinement |
| 101 | `chatgpt-m6-abaddon-judgment-ledger-20261021` | `73cc068f5a9820d796f7588a8e86ba4baac14098` | #510 merged→chatgpt-cycle76-m6-refinement |
| 102 | `chatgpt-m6-abaddon-matched-access-20261021` | `0dc7352411084b9a9d66a359064d74ce69465a34` | #512 merged→chatgpt-cycle76-m6-refinement |
| 103 | `chatgpt-m6-abaddon-neheb-assault-phaseb-20261021` | `af38c8f37389be79e4ac42700ec2e1250fd28dab` | #504 merged→chatgpt-cycle76-m6-refinement |
| 104 | `chatgpt-m6-abaddon-other-hand-cascade-20261022` | `e577b759aa386dc831fe0a7ce09a2cc1ad9da9fd` | #530 merged→chatgpt-cycle76-m6-refinement |
| 105 | `chatgpt-m6-abaddon-other-hand-cascade-ledger-20261022` | `d14d3fe5b08642735f54db9cc491df74cfd6cac2` | #531 merged→chatgpt-cycle76-m6-refinement |
| 106 | `chatgpt-m6-abaddon-rakdos-ledger-20261021` | `1fa8b4097b96433493b7a6f90302e2d342972e9b` | #507 merged→chatgpt-cycle76-m6-refinement |
| 107 | `chatgpt-m6-abaddon-rakdos-role-20261021` | `e88fdf3fca802c5cf379c06b3f97eb5226d87d89` | #506 merged→chatgpt-cycle76-m6-refinement |
| 108 | `chatgpt-m6-abaddon-ruinous-cascade-20261021` | `a2082e1f10800afc264febc4935254d89ba3b5b1` | #511 merged→chatgpt-cycle76-m6-refinement |
| 109 | `chatgpt-m6-abaddon-shared-effects-ledger-20261022` | `746e028c70794a4a9cfc5e542d9dcb8c1010f3d2` | #525 merged→chatgpt-cycle76-m6-refinement |
| 110 | `chatgpt-m6-abaddon-stack-windows-ledger-20261022` | `ccac4a722d60c5a9265d9b7093daf7cecabadff9` | #529 merged→chatgpt-cycle76-m6-refinement |
| 111 | `chatgpt-m6-abaddon-warp-evidence-ledger-20261021` | `98a61340c6f19934470dd1fc6b317f1c2b375bfe` | #517 merged→chatgpt-cycle76-m6-refinement |
| 112 | `chatgpt-m6-admiral-beckett-full-blueprint-ci-receipt-20261022` | `8549c9f1bba542511a10b52685d8eb4e13db44fd` | #589 merged→chatgpt-cycle76-m6-refinement |
| 113 | `chatgpt-m6-admiral-beckett-p0-ci-receipt-20261022` | `da0180aa1eab7c2dc74237d5783c2105767b5f3a` | #585 merged→chatgpt-cycle76-m6-refinement |
| 114 | `chatgpt-m6-admiral-beckett-p0-mechanics-20261022` | `03b0c7ebcaf69b07866078f224a382ddceacdd2d` | #584 merged→chatgpt-cycle76-m6-refinement |
| 115 | `chatgpt-m6-admiral-beckett-p1-ci-receipt-20261022` | `f9dc67249d858d6e0b85f3cfc2d26607da50bf40` | #587 merged→chatgpt-cycle76-m6-refinement |
| 116 | `chatgpt-m6-admiral-beckett-p1-tranche1-20261022` | `fdc1699183cb98a7d390c8a6c1734660be0238e5` | #586 merged→chatgpt-cycle76-m6-refinement |
| 117 | `chatgpt-m6-admiral-beckett-p1-tranche2-20261022` | `8d1a34944e1b3c7a99ae643a8a1a3741c3c4bb38` | #588 merged→chatgpt-cycle76-m6-refinement |
| 118 | `chatgpt-m6-be-lakor-review-20261019-v2` | `85a2cd00de72319b16271e374b9290d0e30e51ac` | none |
| 119 | `chatgpt-m6-checkpoint-the-rani-57` | `aeb2035191dbb1ab5950127e4584027f111da1c4` | #327 closed-unmerged→chatgpt-cycle76-m6-refinement |
| 120 | `chatgpt-m6-complete-agreement-register-20261020` | `76f5e4b940e7aa113239c9743d1f2c4a48b09c46` | #371 merged→chatgpt-cycle76-m6-refinement |
| 121 | `chatgpt-m6-crossdeck-reuse-runner-20261022` | `448157fbaab8a27bf427e1a3937f177695eb5b08` | #534 merged→chatgpt-cycle76-m6-refinement |
| 122 | `chatgpt-m6-deep-review-abaddon-20261019` | `27323f86f14ccadf9d6f4d540b6f5b7df56f9c2c` | #250 merged→chatgpt-cycle76-m6-refinement |
| 123 | `chatgpt-m6-deep-review-anhelo-20261019` | `0c890b55b0f1f9048f7295de16e254db5bc0acb4` | #253 merged→chatgpt-cycle76-m6-refinement |
| 124 | `chatgpt-m6-deep-review-ashad-20261019` | `4a707e7dd93b7cff9c49c44483956d928df6d184` | #254 merged→chatgpt-cycle76-m6-refinement |
| 125 | `chatgpt-m6-deep-review-ashnod-20261019` | `cb7fbf0cb8fe3da1bb5582ed67bd4f2edb0c1876` | #255 merged→chatgpt-cycle76-m6-refinement |
| 126 | `chatgpt-m6-deep-review-beckett-20261019` | `1fdbdf2cb40db02e226a0ae5edd4f403c5933a5e` | #251 merged→chatgpt-cycle76-m6-refinement |
| 127 | `chatgpt-m6-deep-review-belakor-20261019` | `6cc9a6008ab420f734690b4e6f86027b0004614d` | none |
| 128 | `chatgpt-m6-deep-review-belakor-20261019-v3` | `2b5015933857a2112d190c4d6bd00cecad9a867b` | #256 merged→chatgpt-cycle76-m6-refinement |
| 129 | `chatgpt-m6-deep-review-cecily-bjorna-lutri-20261019` | `2d4958b75a129e3d25090d3f8c511d81d1366708` | #257 merged→chatgpt-cycle76-m6-refinement |
| 130 | `chatgpt-m6-deep-review-cormela-20261019` | `5d918de8d07f465606ae8a439c27b1ac3b0b2f9c` | #258 merged→chatgpt-cycle76-m6-refinement |
| 131 | `chatgpt-m6-deep-review-crosis-20261019` | `f200a1cace100b96478a2410be7fda8e5d269d42` | #259 merged→chatgpt-cycle76-m6-refinement |
| 132 | `chatgpt-m6-deep-review-lord-xander-20261019` | `eed3f18cf3321013720eee0d0ed1b0c61e07070c` | none |
| 133 | `chatgpt-m6-deep-review-lynde-31` | `9b68d3a1e9e284b6226983e869c0c90a6f6d2f3a` | none |
| 134 | `chatgpt-m6-deep-review-lynde-31-authored` | `ca55455755beda45fa3e1a8296daaa1e90e3b1da` | #283 merged→chatgpt-cycle76-m6-refinement |
| 135 | `chatgpt-m6-deep-review-mai-zuko-32` | `073f9f9bddfc10a795bbef0be48d4179516b9019` | #284 merged→chatgpt-cycle76-m6-refinement |
| 136 | `chatgpt-m6-deep-review-mairsil-33` | `9d40ee195b9c2fdc26cc4540713616ef06a40aa9` | #285 merged→chatgpt-cycle76-m6-refinement |
| 137 | `chatgpt-m6-deep-review-marchesa-black-rose-35` | `30d28c6da5ff8fefc6b062c95d7cc79642af50d6` | #287 merged→chatgpt-cycle76-m6-refinement |
| 138 | `chatgpt-m6-deep-review-marchesa-dealer-34` | `7d6e8444cf77cb19b643cff84ef4e4aeecccc55c` | #286 merged→chatgpt-cycle76-m6-refinement |
| 139 | `chatgpt-m6-deep-review-mishra-artificer-36` | `9754ff7abd7b4c6b89eb2fc5a03a63fd29a2157e` | #288 merged→chatgpt-cycle76-m6-refinement |
| 140 | `chatgpt-m6-deep-review-mishra-eminent-one-37` | `14b9051da031c3d5a118b8d49870e551c5f191d3` | #289 merged→chatgpt-cycle76-m6-refinement |
| 141 | `chatgpt-m6-deep-review-missy-38` | `bfeb6428ebb52175b245ff16dd5796bf43118c00` | #290 merged→chatgpt-cycle76-m6-refinement |
| 142 | `chatgpt-m6-deep-review-nathan-drake-39` | `f137e9855acc148b3b686b8d7c493476b281afea` | #291 merged→chatgpt-cycle76-m6-refinement |
| 143 | `chatgpt-m6-deep-review-nekusar-40` | `efdfd85d71a818c54248609b345266f24f9e789b` | #292 merged→chatgpt-cycle76-m6-refinement |
| 144 | `chatgpt-m6-deep-review-pass-c-intake-handoff-62` | `150bc4a497a2336038da0dc6438c8140a2998ecb` | #339 merged→chatgpt-cycle76-m6-refinement |
| 145 | `chatgpt-m6-deep-review-tetsuo-54` | `ec7baf3b7d9127daf5c080f4e21d4d061872a83e` | none |
| 146 | `chatgpt-m6-deep-review-the-rani-57` | `79df4e2f60ac5ee71d34910a8041bf95bded44a5` | #326 merged→chatgpt-cycle76-m6-refinement |
| 147 | `chatgpt-m6-deep-review-the-rani-57-checkpoint` | `a7229d54e100d2870099f7d9f7ede6be9b6f63a7` | #328 merged→chatgpt-cycle76-m6-refinement |
| 148 | `chatgpt-m6-deep-review-the-valeyard-58` | `1e53ef559c0a1e115b8dd44ef3e8becd0885cb53` | #329 merged→chatgpt-cycle76-m6-refinement |
| 149 | `chatgpt-m6-deep-review-the-valeyard-58-checkpoint` | `4a8a4ebb74ce628df5fed6ed388b20437b18b9bf` | #330 merged→chatgpt-cycle76-m6-refinement |
| 150 | `chatgpt-m6-deep-review-thraximundar-59` | `d99430791dddeb98f65b53077cf925ac9792cef8` | #331 merged→chatgpt-cycle76-m6-refinement |
| 151 | `chatgpt-m6-deep-review-thraximundar-59-checkpoint` | `4515edb128aa16e6e049be00ed692de3cbd52b9c` | #332 merged→chatgpt-cycle76-m6-refinement |
| 152 | `chatgpt-m6-deep-review-tresserhorns-lord-returned-60` | `e5933bcba6a4799cce56308f599f7f55b78f2202` | #333 merged→chatgpt-cycle76-m6-refinement |
| 153 | `chatgpt-m6-deep-review-tresserhorns-lord-returned-60-checkpoint` | `074c68629aea420502a98ed4256e6bb025f6921d` | #334 merged→chatgpt-cycle76-m6-refinement |
| 154 | `chatgpt-m6-deep-review-unsinkable-20261019` | `9f85c19b4709be30ca7f652371139ba582a6e9fe` | #252 merged→chatgpt-cycle76-m6-refinement |
| 155 | `chatgpt-m6-deep-review-wick-the-whorled-mind-61` | `9fb7adb7f41a81ec7286469040ba4b2275d9e02f` | #335 merged→chatgpt-cycle76-m6-refinement |
| 156 | `chatgpt-m6-deep-review-wick-the-whorled-mind-61-checkpoint` | `2d6c90fddbfe6f302c26aff1cae552204d3a8258` | #336 merged→chatgpt-cycle76-m6-refinement |
| 157 | `chatgpt-m6-deep-review-zevlor-elturel-exile-62` | `bace50cda271838c40863e98c0777aa0e3922c08` | #337 merged→chatgpt-cycle76-m6-refinement |
| 158 | `chatgpt-m6-deep-review-zevlor-elturel-exile-62-checkpoint` | `8d0497c82f5b441ef19b050b481415be794dc55b` | #338 merged→chatgpt-cycle76-m6-refinement |
| 159 | `chatgpt-m6-evidence-ci-20261020` | `963c7fba13074b217eb271de8b615306278d0fcf` | #354 merged→chatgpt-cycle76-m6-refinement |
| 160 | `chatgpt-m6-evidence-xander-stagea-seal-v2-20261025` | `6ef49b8fbceca40dc40d3b2e8be7f4e8fe0d18c3` | #709 merged→chatgpt-cycle76-m6-refinement |
| 161 | `chatgpt-m6-jlk-owner-accepted-formal-pass-c-20261020` | `9974fa045900b9c8f4c02e67d231039a281ff995` | #372 merged→chatgpt-cycle76-m6-refinement |
| 162 | `chatgpt-m6-jlk-owner-substitute-protocol-20261020` | `a5abc88ed2395afdf538e038eb569c6ace20eafc` | #351 merged→chatgpt-cycle76-m6-refinement |
| 163 | `chatgpt-m6-josh-lee-kwai-reconciliation-index-20261020` | `02ee47b31008e639d01d5e5cac08f33bdb1e03f6` | none |
| 164 | `chatgpt-m6-lynde-depth-31-authored` | `76ec4eed5b09942b81a74b1966ceb22ecbaaf135` | #282 closed-unmerged→chatgpt-cycle76-m6-refinement |
| 165 | `chatgpt-m6-pass-c-handoff-after-62-deep-reviews` | `afb692de3c50699dab0a4c5522fd0d8ad6416f88` | none |
| 166 | `chatgpt-m6-pass-c-owner-formal-waiver-20261021` | `4c008473d8a9c3853037dfe4262e08e33d55cef7` | #508 merged→chatgpt-cycle76-m6-refinement |
| 167 | `chatgpt-m6-passc-closure-20261021` | `f39a60d691a3560d3f4220955cc9945fade2fc31` | #503 merged→chatgpt-cycle76-m6-refinement |
| 168 | `chatgpt-m6-phaseb-abaddon-receipt-ledger-20261021` | `74996b417774b2500c739ddf161903e23bfc0773` | #505 merged→chatgpt-cycle76-m6-refinement |
| 169 | `chatgpt-m6-reconcile-abaddon-20261020` | `39263c9b3807a43bb7977bb238940f68a9c66394` | #344 merged→chatgpt-cycle76-m6-refinement |
| 170 | `chatgpt-m6-reconcile-admiral-brass-20261020` | `7922db5649571adc594084c0368fd3e3727ab61a` | #345 merged→chatgpt-cycle76-m6-refinement |
| 171 | `chatgpt-m6-reconcile-anhelo-20261020` | `0b000a6c340fc507facd024cbf7427389ae31f19` | #346 merged→chatgpt-cycle76-m6-refinement |
| 172 | `chatgpt-m6-reconcile-crosis-20261020` | `1a4aa849d9b9648ae483d16a4adf149d349f5591` | #347 merged→chatgpt-cycle76-m6-refinement |
| 173 | `chatgpt-m6-reconcile-doctor-doom-20261020` | `0ec770f897577b33e6cde7e672f223b41178879b` | #348 merged→chatgpt-cycle76-m6-refinement |
| 174 | `chatgpt-m6-reconcile-don-andres-20261020` | `01ab54ec5023b8bb91ef3e99023bd103b2ff6d71` | #350 merged→chatgpt-cycle76-m6-refinement |
| 175 | `chatgpt-m6-reconcile-gwendlyn-20261020` | `d33dda841c3faacdc34e4fd061814b7654e13f21` | #349 merged→chatgpt-cycle76-m6-refinement |
| 176 | `chatgpt-m6-reconcile-jeleva-20261020` | `ae882ae1d337137bf130ba1300b2d2d146c36279` | #352 merged→chatgpt-cycle76-m6-refinement |
| 177 | `chatgpt-m6-reconcile-keep-cluster01-20261020` | `9ee9aa6bf0c1bb661778fef5f4f4b515023b9522` | #369 merged→chatgpt-cycle76-m6-refinement |
| 178 | `chatgpt-m6-reconcile-keep-cluster02-20261020` | `4219072ac38bc53bd673947572cdb3e2ddafc7d9` | #370 merged→chatgpt-cycle76-m6-refinement |
| 179 | `chatgpt-m6-reconcile-kess-20261020` | `746478d0135ed9421e3f0c223e49af9cdb12693e` | #353 merged→chatgpt-cycle76-m6-refinement |
| 180 | `chatgpt-m6-reconcile-ledger15-20261020` | `f5cb2db309a1af3068fdf73d8792bb676bb537aa` | #362 merged→chatgpt-cycle76-m6-refinement |
| 181 | `chatgpt-m6-reconcile-ledger20-20261020` | `eb7e5aeac8710f8f333a641303f2faf880920c58` | #368 merged→chatgpt-cycle76-m6-refinement |
| 182 | `chatgpt-m6-reconcile-lynde-20261020` | `45339e76ac8f472007a067fc4ff1c3b71890d27d` | #357 merged→chatgpt-cycle76-m6-refinement |
| 183 | `chatgpt-m6-reconcile-madcap-20261020` | `b325328c771cd4e11a63b7dd4df2b039d48e89a6` | #366 merged→chatgpt-cycle76-m6-refinement |
| 184 | `chatgpt-m6-reconcile-mai-zuko-20261020` | `d1fd7125570211a1dc3392c959dfb47f8a71a2f2` | #358 merged→chatgpt-cycle76-m6-refinement |
| 185 | `chatgpt-m6-reconcile-mishra-prodigy-20261020` | `dbac14ece60cb8a5a4158f15fcdcf6c2f5d83bec` | #359 merged→chatgpt-cycle76-m6-refinement |
| 186 | `chatgpt-m6-reconcile-nekusar-20261020` | `9e0f52747ee4dcfa7ea9fafb36dfd7ffeb986ea8` | #360 merged→chatgpt-cycle76-m6-refinement |
| 187 | `chatgpt-m6-reconcile-obeka-splitter-20261020` | `0659b95fa59300b6eb489ce9d96cfa62698c768d` | #361 merged→chatgpt-cycle76-m6-refinement |
| 188 | `chatgpt-m6-reconcile-parnesse-20261020` | `430d68cbd223eb45ca2e48ea8473d7f14b90cf03` | #355 merged→chatgpt-cycle76-m6-refinement |
| 189 | `chatgpt-m6-reconcile-progress-20261020` | `1ab36cb283eeb9c33dc964bb6fde81a9c4a699ea` | #356 merged→chatgpt-cycle76-m6-refinement |
| 190 | `chatgpt-m6-reconcile-sedris-20261020` | `37a94a30c772cb588543842ec31002507c1175e4` | #363 merged→chatgpt-cycle76-m6-refinement |
| 191 | `chatgpt-m6-reconcile-solkanar-swamp-20261020` | `e7058ff8259a46570ba552872b7315d9f805aefc` | #364 merged→chatgpt-cycle76-m6-refinement |
| 192 | `chatgpt-m6-reconcile-tetsuo-20261020` | `c569927a00f072cf8af5a2410c5a1c4e7c631e1d` | #365 merged→chatgpt-cycle76-m6-refinement |
| 193 | `chatgpt-m6-reconcile-tresserhorn-returned-20261020` | `dd67f0e0959e5987f4ae8e5e5fbb08b9c836f763` | #367 merged→chatgpt-cycle76-m6-refinement |
| 194 | `chatgpt-m6-remaining61-test-designs-20261022` | `585732b218b689d07951ab1bc3d9625c642577d2` | #535 merged→chatgpt-cycle76-m6-refinement |
| 195 | `chatgpt-m7-abaddon-lost-keeper-effect-20261022` | `771d83e47a2f996ab8574d2f52f08471f4a15c15` | #544 merged→chatgpt-cycle76-m6-refinement |
| 196 | `chatgpt-m7-abaddon-oracle-correction-v2-20261022` | `3b58698749592d02fd6b2d35f20a6319befeb3e4` | #543 merged→chatgpt-cycle76-m6-refinement |
| 197 | `chatgpt-m7-abaddon-owner-approval-ledger-20261022` | `47ac69238255c92b8e70ae427ccdb80c38a21b54` | #583 merged→chatgpt-cycle76-m6-refinement |
| 198 | `chatgpt-m7-abaddon-whole-deck-challengers-20261022` | `6c24e31a07dd20698ee6a9563a185b3fdc3c9119` | #542 merged→chatgpt-cycle76-m6-refinement |
| 199 | `chatgpt-m7-admiral-continuation-ledger-20261022` | `ce1dcaed8d8766ddeedd75b9a9fd4340c4499d46` | #595 merged→chatgpt-cycle76-m6-refinement |
| 200 | `chatgpt-m7-admiral-d-changed-effects-20261022` | `fc551acba0e4bbc7ff486541014a9986b995b996` | #593 merged→chatgpt-cycle76-m6-refinement |
| 201 | `chatgpt-m7-admiral-full-oracle-resilience-20261022` | `3c003ddcf05510edea21907d01037b0f746c044a` | #591 merged→chatgpt-cycle76-m6-refinement |
| 202 | `chatgpt-m7-admiral-material-decisions-20261022` | `42e0b637ad7abb1e2f3aba939aeeae22ddab2533` | #594 merged→chatgpt-cycle76-m6-refinement |
| 203 | `chatgpt-m7-admiral-opportunity-research-20261022` | `afa708e0aaa451f33a31d4ad47bee861e1a164c2` | #590 merged→chatgpt-cycle76-m6-refinement |
| 204 | `chatgpt-m7-admiral-pirate-density-paid-20261022` | `2e952d76c98367a337abdf76f3929040556f26ff` | #592 merged→chatgpt-cycle76-m6-refinement |
| 205 | `chatgpt-m7-no-few-swaps-owner-hard-corrected-20261022` | `85ac36b161020fd00d1afc82b508326d60d3c69d` | #577 merged→chatgpt-cycle76-m6-refinement |
| 206 | `chatgpt-m7-no-few-swaps-owner-hard-frozen-20261022` | `af1b01680a7215812bd385197d06466811b861aa` | #576 closed-unmerged→chatgpt-cycle76-m6-refinement |
| 207 | `chatgpt-m7-one-command-integration-pointer-20261024` | `12dfe38e993131c44c0595553590596f4c2625c7` | #703 merged→chatgpt-cycle76-m6-refinement |
| 208 | `chatgpt-m7-unbounded-search-admiral-reopen-20261022` | `cac44b6db952cbdfd8ec13874fca943baea24cec` | #604 merged→chatgpt-cycle76-m6-refinement |
| 209 | `grokbot-advisory-batch-02-21` | `e5273140802193b85bd6e32ce2e61d38f46265b3` | #341 merged→chatgpt-cycle76-m6-refinement |
| 210 | `grokbot-advisory-batch-22-42` | `2f5971becc4826e4a723fe957b719516108564f5` | #342 merged→chatgpt-cycle76-m6-refinement |
| 211 | `grokbot-advisory-batch-43-62` | `1e99199f7b70a44e26a742033db5707e5a1597a7` | #343 merged→chatgpt-cycle76-m6-refinement |
| 212 | `grokbot-passc-advisory-01-abaddon` | `42980df61b4c943126f511b0267a72343b31a13e` | #340 merged→chatgpt-cycle76-m6-refinement |
| 213 | `jlk-pass-c-05-ashad-progress` | `064e3f5e7201a662707b6fca03a411d50b4ebb54` | #382 merged→chatgpt-cycle76-m6-refinement |
| 214 | `jlk-pass-c-06-ashnod-progress` | `256583d4605d91bccf024988c3a42d4ebbbee2fa` | #384 merged→chatgpt-cycle76-m6-refinement |
| 215 | `jlk-pass-c-06-ashnod-the-uncaring` | `fc4bec156e4006effd4b44721518058bc9c09fcb` | #383 merged→chatgpt-cycle76-m6-refinement |
| 216 | `jlk-pass-c-07-belakor-progress` | `e8910cd725cfb73680c8f5833fe5cd6fa81090a8` | #387 merged→chatgpt-cycle76-m6-refinement |
| 217 | `jlk-pass-c-07-belakor-the-dark-master` | `70af760e2bccd57f208c5c94e2117725c4001d2a` | #386 merged→chatgpt-cycle76-m6-refinement |
| 218 | `jlk-pass-c-08-cecily-bjorna-lutri` | `95ea1223b38d69cf5ddec3654f2962db42e2579c` | #389 merged→chatgpt-cycle76-m6-refinement |
| 219 | `jlk-pass-c-08-cecily-progress` | `474b240e31c03b60c26c5859c29a952ccd2905b9` | #390 merged→chatgpt-cycle76-m6-refinement |
| 220 | `jlk-pass-c-09-cormela-glamour-thief` | `69c458a831c57858ff08b8a5eb0d38b1f1bbfa19` | #391 merged→chatgpt-cycle76-m6-refinement |
| 221 | `jlk-pass-c-09-cormela-progress` | `02f1b6c5415d12290e92e2843edb0f8f3c0f80dc` | #392 merged→chatgpt-cycle76-m6-refinement |
| 222 | `jlk-pass-c-10-crosis-progress` | `c7d737775f0cb484a255383b876df68e20e57078` | #394 merged→chatgpt-cycle76-m6-refinement |
| 223 | `jlk-pass-c-10-crosis-the-purger` | `37021040ac6000d15acf4f12c328c2a6b0ab6208` | #393 merged→chatgpt-cycle76-m6-refinement |
| 224 | `jlk-pass-c-11-cult-of-skaro` | `51dbe2b9619ad1d1e168108cc986fc09ab042259` | #395 merged→chatgpt-cycle76-m6-refinement |
| 225 | `jlk-pass-c-11-cult-of-skaro-progress` | `348fc58c009ce24235ae4b6443ee3e7bd491ffee` | #396 merged→chatgpt-cycle76-m6-refinement |
| 226 | `jlk-pass-c-12-davros-dalek-creator` | `be4058711a50c8978be05efb2d44afa5683d2916` | #397 merged→chatgpt-cycle76-m6-refinement |
| 227 | `jlk-pass-c-12-davros-dalek-creator-progress` | `9e3b05a5a32b07493630f84b681f629981945fb3` | #398 merged→chatgpt-cycle76-m6-refinement |
| 228 | `jlk-pass-c-13-doctor-doom-king-of-latveria` | `f73fbe8f2b3029826fcf024cc9f310cfc0d1c70c` | #399 merged→chatgpt-cycle76-m6-refinement |
| 229 | `jlk-pass-c-13-doctor-doom-king-of-latveria-progress` | `ffd01472287db1d27544a72bda45540c1fb974ea` | #400 merged→chatgpt-cycle76-m6-refinement |
| 230 | `jlk-pass-c-14-don-andres-the-renegade` | `8416e8050603b3b59d3a58ec592019d5e46642d1` | #401 merged→chatgpt-cycle76-m6-refinement |
| 231 | `jlk-pass-c-14-don-andres-the-renegade-progress` | `258882112811a6a06cddcfe3cd23c65e99bc3bbc` | #402 merged→chatgpt-cycle76-m6-refinement |
| 232 | `jlk-pass-c-15-dr-eggman` | `15a1d0ace5d95ce9bd5e1e2c3d1f119ea8736d2c` | #403 merged→chatgpt-cycle76-m6-refinement |
| 233 | `jlk-pass-c-15-dr-eggman-ledger` | `4917be10f0ac5d73b91e90961bb84a42466c55a0` | #404 merged→chatgpt-cycle76-m6-refinement |
| 234 | `jlk-pass-c-16-edea-ledger` | `22ab39249a5f3fa8d6aa2d602ddc496f9a442821` | #406 merged→chatgpt-cycle76-m6-refinement |
| 235 | `jlk-pass-c-16-edea-possessed-sorceress` | `af1305a7ecc25d51563c90c22b3431a5bc62f7f7` | #405 merged→chatgpt-cycle76-m6-refinement |
| 236 | `jlk-pass-c-17-edward-kenway` | `60c3c95a6b5a01c51ffba4cc45ebf044ca877803` | #407 merged→chatgpt-cycle76-m6-refinement |
| 237 | `jlk-pass-c-17-edward-kenway-ledger` | `d01e32d66ae4144d7003d1bf1c7e3f96eb017f27` | #408 merged→chatgpt-cycle76-m6-refinement |
| 238 | `jlk-pass-c-18-evelyn` | `a403a43ba0e0c295eb66b3d3b22f336a406ead93` | #409 merged→chatgpt-cycle76-m6-refinement |
| 239 | `jlk-pass-c-18-evelyn-ledger` | `203860b4d9d49fe121413c5ff173a95ab0442126` | #410 merged→chatgpt-cycle76-m6-refinement |
| 240 | `jlk-pass-c-19-fire-lord-azula` | `35ea57e637f37bbcd5eab97aecbaf66c662acd7a` | #411 merged→chatgpt-cycle76-m6-refinement |
| 241 | `jlk-pass-c-19-fire-lord-azula-ledger` | `cf3b3d7cea511d68b6d6312d00ad08db3546a2f1` | #412 merged→chatgpt-cycle76-m6-refinement |
| 242 | `jlk-pass-c-20-garza-zol-evidence` | `f454d39dc2d241dc1ad2fb457edf0bb72ecad5e5` | #413 merged→chatgpt-cycle76-m6-refinement |
| 243 | `jlk-pass-c-20-garza-zol-ledger` | `f6f02ff9ce051cd2e134455e90b64fcb10ccc9dd` | #414 merged→chatgpt-cycle76-m6-refinement |
| 244 | `jlk-pass-c-21-goro-goro-satoru-evidence` | `5aff6e9db2228dc9a07b829737d08f1bfbca64d0` | #415 merged→chatgpt-cycle76-m6-refinement |
| 245 | `jlk-pass-c-21-goro-goro-satoru-progress` | `73ca0a8a462983da7ad48cfb4c9d224d1a2d1bae` | #416 merged→chatgpt-cycle76-m6-refinement |
| 246 | `jlk-pass-c-22-gwendlyn-di-corci-evidence` | `19efd7f0bc2be9de704178b1634d391bce1f3945` | #417 merged→chatgpt-cycle76-m6-refinement |
| 247 | `jlk-pass-c-22-gwendlyn-di-corci-progress` | `6642077e54e3055e7d02517b59df1930ec175b0f` | #418 merged→chatgpt-cycle76-m6-refinement |
| 248 | `jlk-pass-c-23-inalla-evidence` | `c15a5150e6cf6708ace0fd234f458c1916292829` | #419 merged→chatgpt-cycle76-m6-refinement |
| 249 | `jlk-pass-c-23-inalla-progress` | `02936dcd52d84a450b6f2ff80af059e72105f676` | #420 merged→chatgpt-cycle76-m6-refinement |
| 250 | `jlk-pass-c-24-jeleva-evidence` | `413b91ec6b05132e01a7959039ab0ad976386ed7` | #421 merged→chatgpt-cycle76-m6-refinement |
| 251 | `jlk-pass-c-24-jeleva-progress` | `07ce58b116479392fc9fd482f703160f71874a64` | #422 merged→chatgpt-cycle76-m6-refinement |
| 252 | `jlk-pass-c-25-kefka-evidence` | `47144bdfe544607cd399f78a41013cf27bc8e290` | #423 merged→chatgpt-cycle76-m6-refinement |
| 253 | `jlk-pass-c-25-kefka-progress` | `0b7c1177ac5d081fe80488a01821e7d026a08bd5` | #424 merged→chatgpt-cycle76-m6-refinement |
| 254 | `jlk-pass-c-26-kess-evidence` | `49cfce246f7995a54e722602684046a28d30df1b` | #425 merged→chatgpt-cycle76-m6-refinement |
| 255 | `jlk-pass-c-26-kess-progress` | `97f7c99755b39f9fde11cd3aad776bf4d8b5a4c6` | #426 merged→chatgpt-cycle76-m6-refinement |
| 256 | `jlk-pass-c-27-grixistax-evidence` | `51943735ea71de222a8ea4d85eaa459f10bf2f4f` | #428 merged→chatgpt-cycle76-m6-refinement |
| 257 | `jlk-pass-c-27-grixistax-progress` | `12cb0ef698a36599d44e8055634097008ef902e8` | #429 merged→chatgpt-cycle76-m6-refinement |
| 258 | `jlk-pass-c-28-loki-evidence` | `bda61fca863e15bde079c6a8b18df11f85606197` | #430 merged→chatgpt-cycle76-m6-refinement |
| 259 | `jlk-pass-c-28-loki-progress` | `d747be631c060382086caee1c946ea17c36f2fdb` | #431 merged→chatgpt-cycle76-m6-refinement |
| 260 | `jlk-pass-c-29-lord-tresserhorn-evidence` | `0278a3e74242168c3a014ee19cb09bab727b5e68` | #432 merged→chatgpt-cycle76-m6-refinement |
| 261 | `jlk-pass-c-29-lord-tresserhorn-ledger` | `bf5fefec2d99eb6ac91fa051245559158f9abec0` | #433 merged→chatgpt-cycle76-m6-refinement |
| 262 | `jlk-pass-c-30-lord-xander-evidence` | `a676329169dd7d8f4e045ffc15395618add7b6e3` | #434 merged→chatgpt-cycle76-m6-refinement |
| 263 | `jlk-pass-c-30-lord-xander-ledger` | `9877f102f36fc7ee21548a093ba0b3d3fbf82a82` | #435 merged→chatgpt-cycle76-m6-refinement |
| 264 | `jlk-pass-c-31-lynde-evidence` | `de8565d197cb58254ccede8d3e70d5d5f8adc46e` | #436 merged→chatgpt-cycle76-m6-refinement |
| 265 | `jlk-pass-c-31-lynde-ledger` | `6b0c6e29ba2b49dd8dbeba8b83eb32cb005e57e0` | #437 merged→chatgpt-cycle76-m6-refinement |
| 266 | `jlk-pass-c-32-mai-and-zuko` | `fbca98288a75b30448d56009504dfa850bc4c28a` | #438 merged→chatgpt-cycle76-m6-refinement |
| 267 | `jlk-pass-c-32-mai-and-zuko-ledger` | `bbe1c7e0e33429a21fb90991c4addffbaf851f7a` | #439 merged→chatgpt-cycle76-m6-refinement |
| 268 | `jlk-pass-c-33-mairsil` | `7654a4656442c151e2c1fb473b099e8e4ac21e7a` | #440 merged→chatgpt-cycle76-m6-refinement |
| 269 | `jlk-pass-c-33-mairsil-ledger` | `ba10fae85f832506bbd4abc7e34a1b4d617d5385` | #441 merged→chatgpt-cycle76-m6-refinement |
| 270 | `jlk-pass-c-34-marchesa-dealer` | `67f0c941d19ad8524083cefec5094949184ccbd9` | #442 merged→chatgpt-cycle76-m6-refinement |
| 271 | `jlk-pass-c-34-marchesa-dealer-ledger` | `de6ddae40d0b63660bf5d649a9477e2e6108e0e7` | #443 merged→chatgpt-cycle76-m6-refinement |
| 272 | `jlk-pass-c-35-marchesa-black-rose` | `7a9fd7e0d25141dcf1a41da75d95d749e91a5c61` | #444 merged→chatgpt-cycle76-m6-refinement |
| 273 | `jlk-pass-c-35-marchesa-black-rose-ledger` | `ed91c3d128dcb375b9261c87846d983b93b73a45` | #445 merged→chatgpt-cycle76-m6-refinement |
| 274 | `jlk-pass-c-36-mishra-artificer-prodigy` | `734d3b8571b5f4bcd786f53a711ba4eda3c1a23d` | #446 merged→chatgpt-cycle76-m6-refinement |
| 275 | `jlk-pass-c-36-mishra-artificer-prodigy-ledger` | `79451dc763e2208507695d426831b90c73cef0d6` | #447 merged→chatgpt-cycle76-m6-refinement |
| 276 | `jlk-pass-c-37-mishra-eminent-one` | `eb91ccccc497fcd910ccbfc669a580493ee8cca1` | #448 merged→chatgpt-cycle76-m6-refinement |
| 277 | `jlk-pass-c-37-mishra-eminent-one-ledger` | `b1db115acc7e15d702d9313edaa8acb81dc286d2` | #449 merged→chatgpt-cycle76-m6-refinement |
| 278 | `jlk-pass-c-38-missy-evidence` | `3d8a907c86d667e2ec0170ba57671719eb91a628` | #450 merged→chatgpt-cycle76-m6-refinement |
| 279 | `jlk-pass-c-38-missy-ledger` | `c90935013dc897d49a3829169b052f4c404ba0dd` | #451 merged→chatgpt-cycle76-m6-refinement |
| 280 | `jlk-pass-c-39-nathan-drake-evidence` | `88ceb95f55ccdb4621cd913cb7a1550a32b1fac5` | #452 merged→chatgpt-cycle76-m6-refinement |
| 281 | `jlk-pass-c-39-nathan-drake-ledger` | `0b84ec2750212bad9f822c8c2d65d2c18264f466` | #453 merged→chatgpt-cycle76-m6-refinement |
| 282 | `jlk-pass-c-40-nekusar-ledger` | `8268f7569e867c2790cb26b9c873b0e9d0bc481a` | #455 merged→chatgpt-cycle76-m6-refinement |
| 283 | `jlk-pass-c-41-nicol-bolas-evidence` | `8c16d9f6dafaeab3bf3a19737038eedb7c3d78fa` | #456 merged→chatgpt-cycle76-m6-refinement |
| 284 | `jlk-pass-c-41-nicol-bolas-ledger` | `27488d16632e642727f10c40da14f400975a3911` | #457 merged→chatgpt-cycle76-m6-refinement |
| 285 | `jlk-pass-c-42-nicol-ravager-evidence` | `edd47c6baa56df7e9c5dbbc36fcbc8aedf656122` | #458 merged→chatgpt-cycle76-m6-refinement |
| 286 | `jlk-pass-c-42-nicol-ravager-ledger` | `a574f9b7fbd79bfcd8315040a907ef559a3c8de3` | #459 merged→chatgpt-cycle76-m6-refinement |
| 287 | `jlk-pass-c-43-norman-evidence` | `16a82ab9b2f2d9e18a1e404f23864eb8ca5593bc` | #460 merged→chatgpt-cycle76-m6-refinement |
| 288 | `jlk-pass-c-43-norman-ledger` | `4673c263461c8d02dfb6ce48a80c7b14c38241ed` | #461 merged→chatgpt-cycle76-m6-refinement |
| 289 | `jlk-pass-c-44-obeka-evidence` | `ab32988e4ff35ef9736c99812f60f29d26f97729` | #462 merged→chatgpt-cycle76-m6-refinement |
| 290 | `jlk-pass-c-44-obeka-ledger` | `a9f3d3d34ea788999527fac761f80af56b09a19d` | #463 merged→chatgpt-cycle76-m6-refinement |
| 291 | `jlk-pass-c-45-obeka-splitter-evidence` | `bc38f6f192621cf30b3465be353ee38664b9045a` | #464 merged→chatgpt-cycle76-m6-refinement |
| 292 | `jlk-pass-c-45-obeka-splitter-ledger` | `a19f0065bbcc60471b32f90c311915a8f2222994` | #465 merged→chatgpt-cycle76-m6-refinement |
| 293 | `jlk-pass-c-46-parnesse-evidence` | `0c479ab8a8674e8ef50a486ecbea8a61acd92bbc` | #466 merged→chatgpt-cycle76-m6-refinement |
| 294 | `jlk-pass-c-46-parnesse-ledger` | `47217df946311f37010d98b0d7855db049446472` | #467 merged→chatgpt-cycle76-m6-refinement |
| 295 | `jlk-pass-c-47-rogsi-evidence` | `7c3bbefbf72515d0f7a54aa17ca773b345450fb9` | #468 merged→chatgpt-cycle76-m6-refinement |
| 296 | `jlk-pass-c-47-rogsi-ledger` | `5b5fa35d58c84566037714ec75a1325ba42a95c1` | #469 merged→chatgpt-cycle76-m6-refinement |
| 297 | `jlk-pass-c-48-saruman-evidence` | `ecb11deeb2f8ca1f56a1bbb02ab1393a3fa1eb18` | #470 merged→chatgpt-cycle76-m6-refinement |
| 298 | `jlk-pass-c-48-saruman-ledger` | `cd0843f77afc37c1198220b21973fed38420841c` | #471 merged→chatgpt-cycle76-m6-refinement |
| 299 | `jlk-pass-c-49-sauron-lord-ledger` | `2c9eb4e2f296c9bbc55c14dfeff9bcbb194d4347` | #473 merged→chatgpt-cycle76-m6-refinement |
| 300 | `jlk-pass-c-50-sauron-dark-evidence` | `cc28c93a44afd8fd4e22a3ac677b5c6094242acf` | #474 merged→chatgpt-cycle76-m6-refinement |
| 301 | `jlk-pass-c-50-sauron-dark-ledger` | `49b94959077e7e1604216aa2d0f86cad24b30969` | #475 merged→chatgpt-cycle76-m6-refinement |
| 302 | `jlk-pass-c-51-sedris-evidence` | `0865e5fbc3124cb400c41ea6f6cba79f6c503d6a` | #476 merged→chatgpt-cycle76-m6-refinement |
| 303 | `jlk-pass-c-51-sedris-ledger` | `9bda0b178112a86cce66c1cab5457ad2e0e17497` | #477 merged→chatgpt-cycle76-m6-refinement |
| 304 | `jlk-pass-c-52-solkanar-20261021` | `36bd4f99e1d9bea3e70c678595cf50f8807dd82b` | #479 merged→chatgpt-cycle76-m6-refinement |
| 305 | `jlk-pass-c-52-solkanar-ledger-20261021` | `6e8e6c31104b4c8ecdeb1a056eb105b3646c7a99` | #481 merged→chatgpt-cycle76-m6-refinement |
| 306 | `jlk-pass-c-53-tainted-evidence` | `22715cbee70930884644857e64d052465c19cb8e` | #482 merged→chatgpt-cycle76-m6-refinement |
| 307 | `jlk-pass-c-53-tainted-ledger` | `6d399ddfeb6c10ac6fefd139b39334285cd69fc1` | #484 merged→chatgpt-cycle76-m6-refinement |
| 308 | `jlk-pass-c-54-tetsuo-umezawa-evidence` | `f702ed0b5e14290f70472fc1d34652ee0a573446` | #485 merged→chatgpt-cycle76-m6-refinement |
| 309 | `jlk-pass-c-54-tetsuo-umezawa-ledger` | `2f0568a6a9d228f2fe5cb5de17751d0c5011b9c6` | #486 merged→chatgpt-cycle76-m6-refinement |
| 310 | `jlk-pass-c-55-imperial-evidence` | `4b9d0ede116d4a87a2be1d72a20ee9950f5a3898` | #487 merged→chatgpt-cycle76-m6-refinement |
| 311 | `jlk-pass-c-55-imperial-ledger` | `124c1cc4efcf8dbc7760cc666bc6159b03b1179d` | #488 merged→chatgpt-cycle76-m6-refinement |
| 312 | `jlk-pass-c-56-madcap-evidence` | `26e94d9d19c8492d8def5e3be14d98eab9ea96e3` | #489 merged→chatgpt-cycle76-m6-refinement |
| 313 | `jlk-pass-c-56-madcap-ledger` | `6b1e8d8ae7c62abddc0c8ad7ff1183c27885471b` | #490 merged→chatgpt-cycle76-m6-refinement |
| 314 | `jlk-pass-c-57-rani-evidence` | `b0a996f1130d78809a8472dbb5d14fe978b4e72b` | #491 merged→chatgpt-cycle76-m6-refinement |
| 315 | `jlk-pass-c-57-rani-ledger` | `8bacc4c672816c165192dd8a4afc74d5ca376f4c` | #492 merged→chatgpt-cycle76-m6-refinement |
| 316 | `jlk-pass-c-58-valeyard-evidence` | `b9338c1c8e313cac22fa14c52c399d793270f54d` | #493 merged→chatgpt-cycle76-m6-refinement |
| 317 | `jlk-pass-c-58-valeyard-ledger` | `8737ef72649b0cd58df564e7fc47caba4daaa337` | #494 merged→chatgpt-cycle76-m6-refinement |
| 318 | `jlk-pass-c-59-thraximundar-evidence` | `4edfce358e193ed74c5703831606516a27a0f6b8` | #495 merged→chatgpt-cycle76-m6-refinement |
| 319 | `jlk-pass-c-59-thraximundar-ledger` | `b04cd1e163a26933ca1823484f3676e867ce8582` | #496 merged→chatgpt-cycle76-m6-refinement |
| 320 | `jlk-pass-c-60-tresserhorn-evidence` | `0e62c39cded5f708be1e0058b2ab00d8db9f810c` | #497 merged→chatgpt-cycle76-m6-refinement |
| 321 | `jlk-pass-c-60-tresserhorn-ledger` | `0323a9bf403bf1bcc9357510ae1b86b93f186c31` | #498 merged→chatgpt-cycle76-m6-refinement |
| 322 | `jlk-pass-c-61-wick-evidence` | `20aa70acec17f6cd69a9571da27d79e7ffeda166` | #499 merged→chatgpt-cycle76-m6-refinement |
| 323 | `jlk-pass-c-61-wick-ledger` | `a32a3b35ac19fc3afa28103ce2fa2ee8d2b9adfb` | #500 merged→chatgpt-cycle76-m6-refinement |
| 324 | `jlk-pass-c-62-zevlor-evidence` | `9f99a0adacfe5165c2577de2c4e8a03859c91c39` | #501 merged→chatgpt-cycle76-m6-refinement |
| 325 | `jlk-pass-c-62-zevlor-ledger` | `2e2c41f29f1446fafe1ebf82dff7e721ecdc3a32` | #502 merged→chatgpt-cycle76-m6-refinement |
| 326 | `jlk-progress-03-admiral-brass-unsinkable` | `e7db269e112144e83cfdfb40549732f0d65a8cb8` | #378 merged→chatgpt-cycle76-m6-refinement |
| 327 | `jlk-progress-04-anhelo-the-painter` | `12aaf68c8097327c545e04bccac6e5ccd115a445` | #380 merged→chatgpt-cycle76-m6-refinement |

#### Contained but kept

| Branch | Head SHA | Reasons |
|---|---|---|
| `chatgpt-admiral-stage10-rev2-tested_pool-20261022` | `4ad0667de095a4d5ba56e9bb756d12b422e2c6a5` | branch NAME referenced in repository files on main/retained heads — e.g. data/grixis/m7/research_challengers/Admiral_Beckett_Brass_current_continuation_20261022.json |
| `chatgpt-admiral-stage11-m6_i_local_best-20261022` | `c5e1451bf436b085d289876b90ea5241c591d1dd` | branch NAME referenced in repository files on main/retained heads — e.g. data/grixis/m7/research_challengers/Admiral_Beckett_Brass_current_continuation_20261022.json |
| `chatgpt-admiral-stage12-rev2_j_bundle-20261022` | `0f976b74d5fd5a9fd886b3938b77ab10bcffca75` | branch NAME referenced in repository files on main/retained heads — e.g. data/grixis/m7/research_challengers/Admiral_Beckett_Brass_current_continuation_20261022.json |
| `chatgpt-admiral-stage13-m7_rev2_ownerready-20261022` | `00cce844dcfc70e8e94eca9011e68c5ea8c6f355` | branch NAME referenced in repository files on main/retained heads — e.g. data/grixis/m7/research_challengers/Admiral_Beckett_Brass_current_continuation_20261022.json |
| `chatgpt-admiral-stage7-whole_deck-adjudication-20261022` | `0e1e16959f64b467d222fabfc9b6cefd2816f978` | branch NAME referenced in repository files on main/retained heads — e.g. data/grixis/m7/research_challengers/Admiral_Beckett_Brass_current_continuation_20261022.json |
| `chatgpt-admiral-stage8-wave-palisade-paid-combat-20261022` | `152c3add699797c65971f9842518503dc2de8e7f` | branch NAME referenced in repository files on main/retained heads — e.g. data/grixis/m7/research_challengers/Admiral_Beckett_Brass_current_continuation_20261022.json |
| `chatgpt-admiral-stage9-candidate_specific_m6_rebind-20261022` | `f6e378cf03f6c1ba8e079286374a828ba7d08232` | branch NAME referenced in repository files on main/retained heads — e.g. data/grixis/m7/research_challengers/Admiral_Beckett_Brass_current_continuation_20261022.json |
| `chatgpt-cycle100-general-state-kernel` | `3f3e792c39d2081bdf2a15bb6b232763d87a0056` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/chatgpt-cycle100-general-state-kernel.yml |
| `chatgpt-cycle101-transactional-stack` | `129640ffd70d04218e02ea4650105cdc5b0af0e7` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/chatgpt-cycle101-transactional-stack.yml |
| `chatgpt-cycle102-priority-basic-access` | `f7152d65b5db53d356d04ebedb9d3501e7df1e1e` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/chatgpt-cycle102-priority-basic-access.yml |
| `chatgpt-cycle103-nonbasic-mana` | `3b579425dbed666953cfe8ec6cfa9e1cc0dac03a` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/chatgpt-cycle103-nonbasic-mana.yml |
| `chatgpt-cycle104-fetch-city-tomb` | `0fb461ec83b9b08783c642d7b54dd627135edebe` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/chatgpt-cycle104-fetch-city-tomb.yml |
| `chatgpt-cycle105-abaddon-decision-gates` | `62f3dad7591c15672008b2ee4f412cde0c907083` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/chatgpt-cycle105-abaddon-decision-gates.yml |
| `chatgpt-cycle106-abaddon-physical-opportunities` | `651ee36ad55dad909aab991ed28d2b6c503564df` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/chatgpt-cycle106-abaddon-physical-opportunities.yml |
| `chatgpt-cycle107-blast-balanced-target` | `e6ef3a2e7c8207d4ebb5d36f56c1753c3dff79e5` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/chatgpt-cycle107-blast-balanced-target.yml |
| `chatgpt-cycle108-cascade-value-audit` | `1ef8944555e1609fac3967a57b73e4fdaa1b5186` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/chatgpt-cycle108-cascade-value-audit.yml |
| `chatgpt-cycle109-oracle-cascade-replay` | `6be8a158efabcf622638b6a89e73ccc015def92b` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/chatgpt-cycle109-oracle-cascade-replay.yml |
| `chatgpt-cycle110-abaddon-common-board` | `69b49c23761e85b5226d90f99fe0466b8d9e1b3f` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/chatgpt-cycle110-abaddon-common-board.yml |
| `chatgpt-cycle111-62-refinement-triage` | `85fef11e9d5faf0ee2049d1bfe882c7eb140db5e` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/chatgpt-cycle111-62-refinement-triage.yml |
| `chatgpt-cycle112-three-commander-judgments` | `848578710df6963265258f484500dfd98093df36` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/chatgpt-cycle112-three-commander-judgments.yml |
| `chatgpt-cycle113-commander-batch-and-critique` | `fb96d816ea2c15fa2365bff8b7dd10c74947808b` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/chatgpt-cycle113-commander-batch-and-critique.yml |
| `chatgpt-cycle114-inalla-rani-bolas-review` | `2222319c7d6ece94780cd95a0cbc776ce995dbe6` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/chatgpt-cycle114-commander-reviews.yml |
| `chatgpt-cycle115-three-commander-identity` | `c8ddf29e1eae2269469dce56f1f02190006f1ea5` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/chatgpt-cycle115-commander-reviews.yml |
| `chatgpt-cycle116-three-commander-audit` | `d25ef8a7b42d89ffebd8cf95518058366c532432` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/chatgpt-cycle116-three-commander-audit.yml, data/grixis/m6/phase_b_plans/cycle116_three_decks_preregistered_01.json |
| `chatgpt-cycle117-independent-review-gates` | `877cdf68b475a9d04b9cef1b78ec4e46531f9d7b` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/chatgpt-cycle117-independent-readiness.yml |
| `chatgpt-cycle118-supported-paired-evidence` | `fb33a4919d08bef51ae4d79c2d90b7a084e38ddc` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/chatgpt-cycle118-supported-paired-evidence.yml |
| `chatgpt-cycle119-bounded-effect-kernel` | `f3372662a05efeded3269481c491605ae0489903` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/chatgpt-cycle119-bounded-effect-kernel.yml |
| `chatgpt-cycle120-physical-source-access` | `45ef95ff8c3b404c901d4c2e2ac0f006aea65daf` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/chatgpt-cycle120-physical-source-access.yml, data/grixis/m6/phase_b_plans/cycle120_physical_access_preregistered_01.json |
| `chatgpt-cycle121-physical-basic-casts` | `f847cf5e38e8e00adbd4f6d7b116c88550f77c3d` | branch NAME referenced in repository files on main/retained heads; branch NAME referenced in GitHub PR/issue body or comment — e.g. .github/workflows/chatgpt-cycle121-physical-basic-casts.yml — PR #228 (closed) body/title |
| `chatgpt-cycle122-nonbasic-source-casts` | `6c8d73133e298674020d7aec1e5b9785a1999b32` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/chatgpt-cycle122-nonbasic-source-casts.yml |
| `chatgpt-cycle123-conditional-offer-stack` | `54ba20da2fd4d43ebbb5d80bfa4be25970790788` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/chatgpt-cycle123-conditional-offer-stack.yml |
| `chatgpt-cycle123-progress-receipt` | `f6dd3a57534cdae533c6772fb07b8d5f0da813b2` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/m6-m7-progress-integrity.yml |
| `chatgpt-cycle124-independent-critic-packets` | `78d002d12f5f18f5777a34eed5f15118bbb4ea6a` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/chatgpt-cycle124-reviewer-intake.yml |
| `chatgpt-cycle124-progress-receipt` | `7cf551bd65abf9fcc407dd0e09a8b0702549f36a` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/m6-m7-progress-integrity.yml |
| `chatgpt-cycle125-grok-passc-intake-rings-erratum` | `f2fa9cf42434ba2bf1e5b4c97a2b9f15b69057f9` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/chatgpt-cycle125-grok-rings-erratum.yml |
| `chatgpt-cycle125-review-progress-receipt` | `e95a83f3d584ddc93d37e4b08d4548fae82ecb08` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/m6-m7-progress-integrity.yml |
| `chatgpt-cycle126-bolas-source-mana-loyalty-pressure` | `17d7243929f37d625fd3ba85fd561657892c19f8` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/chatgpt-cycle126-bolas-mana-loyalty.yml, data/grixis/m6/phase_b_bounded/cycle126_bolas_source_paid_pressure_interpretation_01.md |
| `chatgpt-cycle126-m6-m7-progress-receipt` | `f1d0c9169c33969f45e5cc33ff567afd172e090c` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/m6-m7-progress-integrity.yml |
| `chatgpt-cycle127-m6-batch-review-workflow` | `94f564a7b9a1113087016b82f70fecee98ba908b` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/chatgpt-cycle127-batch-review-intake.yml |
| `chatgpt-cycle128-progress-receipt` | `048e7428bda033f1cc0e89d1ff6c6411e734c6d7` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/m6-m7-progress-integrity.yml |
| `chatgpt-cycle128-six-source-judgments` | `863be124c859b74d9c34d844bc5af1a9c5ccfe1e` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/chatgpt-cycle128-six-source-judgments.yml |
| `chatgpt-cycle129-progress-receipt` | `3b5bc8ec651fce554c9acf8056a2bb1fb3e732f3` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/m6-m7-progress-integrity.yml |
| `chatgpt-cycle129-six-commander-reviews` | `b76c197af904858425a931e037cb4f260a448218` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/chatgpt-cycle129-six-authored.yml |
| `chatgpt-cycle130-progress-receipt` | `560f1fbc7a61c0cc03905fe9e1260d74602ea35c` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/m6-m7-progress-integrity.yml |
| `chatgpt-cycle130-six-commander-reviews` | `b67373b0f18a36dc8c96f54ed1761390c98a8fc3` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/chatgpt-cycle130-six-authored.yml |
| `chatgpt-cycle131-authored-complete-tracker` | `7533b0ec7c2abc28d86322325bb28e5d14116a64` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/m6-m7-progress-integrity.yml |
| `chatgpt-cycle131-complete-authored-62` | `50d10350f2aa45774d119416d74648cca281052c` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/chatgpt-cycle131-all-authored.yml |
| `chatgpt-cycle72-2-frozen-cache-gates` | `fe9265ce8612b5350940a26bf4a2c799f9ce602d` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/chatgpt-frozen-cache-gates.yml |
| `chatgpt-cycle73-m5-rebuild` | `68fab6944d15994cb9736884f71051511dacdcdc` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/chatgpt-m5-regen.yml |
| `chatgpt-cycle74b-lift-correction` | `fcd28daff7d3f7b091de04299699645ba7e47aa2` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/chatgpt-birthday-m5-lift.yml |
| `chatgpt-cycle94-abaddon-followthrough` | `e0e814cfad2b735b7711b1593fdb1a3207f26799` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/chatgpt-cycle94-abaddon-followthrough.yml |
| `chatgpt-cycle95-abaddon-deckwide-access` | `3b4ed9864dbfdde76bd98e970eb8b2907d53dccb` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/chatgpt-cycle95-abaddon-deckwide-access.yml |
| `chatgpt-cycle96-abaddon-turn-state` | `16057625fc885d2e54d02c7688645267e58d4b51` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/chatgpt-cycle96-abaddon-turn-state.yml |
| `chatgpt-cycle97-abaddon-real-library-replay` | `dfc0301fda4adc84367388f2c11e2f9cc3be080a` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/chatgpt-cycle97-abaddon-real-library-replay.yml |
| `chatgpt-cycle98-abaddon-effect-coverage` | `ddbceb473d0b0ceeb79fb4e0542e8a35613a94ab` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/chatgpt-cycle98-abaddon-effect-coverage.yml |
| `chatgpt-cycle99-abaddon-oracle-tutors` | `5a8aaaaf64b55fed2e087d8e1571a6e51dc317b2` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/chatgpt-cycle99-abaddon-oracle-tutors.yml |
| `chatgpt-deck48-saruman-m7-rev1-20261027` | `ef3bcd2d41e7212a8fd86c7c34b9745a69deefe2` | head commit dated within last 7 days (2026-10-27T04:51:26-04:00) |
| `chatgpt-deck49-sauron-lotr-m7-rev1-20261027` | `a159c542199a4e750eb48fe8ca615b786907647a` | head commit dated within last 7 days (2026-10-27T05:13:18-04:00) |
| `chatgpt-deck50-sauron-dark-lord-m7-rev1-20261027` | `beb3487d95b7e32c0b5f2279520f1686e229a97b` | head commit dated within last 7 days (2026-10-27T06:10:29-04:00) |
| `chatgpt-deck51-sedris-m7-rev1` | `d11d02d36cc6c5cadba6e96101d4693e9dda1693` | head commit dated within last 7 days (2026-10-27T06:43:10-04:00) |
| `chatgpt-deck52-solkanar-m7-rev1` | `4e4b6c7ebbdc70b96c218d88d9fd67ec1c6e327b` | head commit dated within last 7 days (2026-10-27T13:50:57-04:00) |
| `chatgpt-deck53-solkanar-tainted-m7-rev1` | `a0ad5e80a8e8f11ac7418d5a4d306d7a661ec1f9` | head commit dated within last 7 days (2026-10-27T15:06:21-04:00) |
| `chatgpt-deck54-tetsuo-m7-rev1` | `bd3c95fef93197e6503990a35778f7a06298ce87` | head commit dated within last 7 days (2026-10-27T16:17:38-04:00) |
| `chatgpt-deck55-tetsuo-imperial-m7-rev1` | `885bf09d513b74a1642ff0edf73212fe744e8d1a` | head commit dated within last 7 days (2026-10-27T17:19:07-04:00) |
| `chatgpt-deck56-m6-p0-transfer-followup-20261027` | `df803bccfda2d2cffb88161b3a991b64b97d1be5` | head commit dated within last 7 days (2026-10-27T18:57:37-04:00) |
| `chatgpt-deck56-madcap-jester-m7-rev1` | `efe4a4ec7cc611815789f64318c5782acb43538f` | head commit dated within last 7 days (2026-10-27T18:09:52-04:00) |
| `chatgpt-deck57-rani-m6-p0-certification` | `a84f8e93737ebc06ce08c775d30c1cb601e4ae73` | head commit dated within last 7 days (2026-10-27T19:41:35-04:00) |
| `chatgpt-deck57-the-rani-m7-rev1` | `e4e18415dde7eae5fc06b0ef257a167cfa0bcb98` | head commit dated within last 7 days (2026-10-27T19:30:51-04:00) |
| `chatgpt-deck58-the-valeyard-m7-rev1` | `f2f0c9673dcf8ebccac59604dae7fcf79edba555` | head commit dated within last 7 days (2026-10-28T01:18:39-04:00) |
| `chatgpt-goben-norman-name-equivalence` | `7dea4f0efc7a1b4b6c6cf34bf3af001c856cf719` | branch NAME referenced in repository files on main/retained heads; branch NAME referenced in GitHub PR/issue body or comment — e.g. .github/workflows/chatgpt-name-equivalences.yml — issue #221 (closed) body/title |
| `chatgpt-jlk-pass-c-abaddon-20261021` | `e8ec2c9bfd9df4c470aebedf929a0c307e33c7ac` | branch NAME referenced in repository files on main/retained heads — e.g. data/grixis/m6/owner_pass_c_substitute/Abaddon_the_Despoiler/seal.json |
| `chatgpt-jlk-pass-c-beckett-20261021` | `adce5b116066993013ac16c5e5d9d299230b5bf5` | branch NAME referenced in repository files on main/retained heads — e.g. data/grixis/m6/owner_pass_c_substitute/Admiral_Beckett_Brass/seal.json |
| `chatgpt-m6-cult-of-skaro-depth-20261019` | `f1585a0aeb23d86f510d5a6da13b25df667cb757` | only container is chatgpt-m6-deep-review-cult-of-skaro-20261019, an unmerged branch that is not on the never-delete list (could be pruned later) |
| `chatgpt-m6-m7-progress-subtracker` | `d0c5eb6869da6a8943f446d25a499ad3322b9a18` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/m6-m7-progress-integrity.yml |
| `chatgpt-m6-single-deck-review-standard` | `f45232b5674d0c2849443577c7a87cc328938898` | branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/m6-single-deck-depth-check.yml |
| `chatgpt-m7-42-ravager-rev1-proposal` | `f0b979dc115d82e0d9e37853e95dde566f35b901` | head commit dated within last 7 days (2026-10-26T18:51:20-04:00); branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/m7-nicol-ravager-rev1.yml |
| `chatgpt-m7-deck25-kefka-independent-20261024` | `d7b5dcf3e7ba272941990d4ba0c88d837f4f8a64` | head commit dated within last 7 days (2026-10-28T01:23:09-04:00); branch NAME referenced in GitHub PR/issue body or comment — PR #700 (closed) body/title |
| `chatgpt-m7-deck55-p0-case-repair-20261027` | `48d800ca78803fefb78ca27642e862c5a5b91297` | head commit dated within last 7 days (2026-10-27T18:44:49-04:00) |
| `chatgpt-m7-nathan-drake-rev1-20261026` | `e8777840aaf5d0241d4d4f4aa4a79a8ce7688767` | head commit dated within last 7 days (2026-10-26T17:21:07-04:00) |
| `chatgpt-m7-nekusar-live-oracle-20261026` | `61a322fe75ac09e446a2b59ed79d0e9f4c95ae20` | head commit dated within last 7 days (2026-10-26T18:00:35-04:00) |
| `chatgpt-m7-nekusar-rev1-20261026` | `4962de014b02e010dd71dba3d4e35f2b3d4c2f9f` | head commit dated within last 7 days (2026-10-26T17:57:01-04:00); branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/m7-nekusar-rev1.yml |
| `chatgpt-m7-transfer-repair-audit-20261027` | `a6d0a81a11ee4f8b8dc4c71e62162f785e5a0660` | head commit dated within last 7 days (2026-10-27T18:29:52-04:00) |
| `grixis-m6-sealed-commander-first-20261017` | `4fd295bf526354b2dfaa31c15ed8375946b8fe3d` | only container is chatgpt-cycle77-ij-sealing, an unmerged branch that is not on the never-delete list (could be pruned later) |
| `grixis-m6-sealed-performance-20261017` | `9eb564cdab747e73e5fd19963e71e58e8229e979` | only container is chatgpt-cycle77-ij-sealing, an unmerged branch that is not on the never-delete list (could be pruned later) |
| `grokbot-deck06-ashnod-the-uncaring-m7-20261023` | `cb670d59c6dd5c9a62b68197a6f3274aaef8422b` | only container is chatgpt-deck06-ashnod-m7-rev2-independent-20261023, an unmerged branch that is not on the never-delete list (could be pruned later); is the BASE branch of PR(s) [681]; branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/m7-ashnod-chatgpt-rev2.yml, data/grixis/m7/grokbot_production_ledger.json |
| `grokbot-deck07-belakor-the-dark-master-m7-20261023` | `ce713a71d2a4696f8cab3727d7fdf49a73db1b0c` | only container is chatgpt-deck07-belakor-m7-rev2-eight-20261023, an unmerged branch that is not on the never-delete list (could be pruned later); is the BASE branch of PR(s) [682]; branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/m7-belakor-chatgpt-rev2.yml, data/grixis/m7/grokbot_production_ledger.json |
| `grokbot-deck08-cecily-bjorna-lutri-m7-20261023` | `14f33de88685dbcbee9c8cc59e59ac5272ccf2fe` | only container is chatgpt-deck08-cecily-bjorna-lutri-m7-rev2-ten-20261023, an unmerged branch that is not on the never-delete list (could be pruned later); is the BASE branch of PR(s) [683]; branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/m7-cecily-bjorna-chatgpt-rev2.yml, data/grixis/m7/grokbot_production_ledger.json |
| `grokbot-deck09-cormela-glamour-thief-m7-20261023` | `257dac3391fe3044d509b8dcadba5631a6906959` | only container is chatgpt-deck09-cormela-m7-rev2-six-20261023, an unmerged branch that is not on the never-delete list (could be pruned later); is the BASE branch of PR(s) [684]; branch NAME referenced in repository files on main/retained heads; branch NAME referenced in GitHub PR/issue body or comment — e.g. .github/workflows/m7-cormela-chatgpt-rev2.yml, data/grixis/m7/grokbot_production_ledger.json — PR #684 (closed) body/title |
| `grokbot-deck10-crosis-the-purger-m7-20261023` | `7953eef5ef1159360a2571625f90076d8ce7376c` | only container is chatgpt-deck10-crosis-m7-rev2-20261023, an unmerged branch that is not on the never-delete list (could be pruned later); branch NAME referenced in repository files on main/retained heads — e.g. data/grixis/m7/grokbot_production_ledger.json |
| `grokbot-deck11-cult-of-skaro-m7-20261023` | `488e1d05fb994a1770a663baa971d7b3e9001c74` | only container is chatgpt-deck11-cult-of-skaro-m7-rev2-20261023, an unmerged branch that is not on the never-delete list (could be pruned later); branch NAME referenced in repository files on main/retained heads — e.g. data/grixis/m7/grokbot_production_ledger.json |
| `grokbot-deck15-dr-eggman-m7-20261023` | `3b67994a8fdfa1f3fe11e801ed02d0de94222cbc` | only container is chatgpt-deck15-eggman-m7-rev2-independent-audit-20261023, an unmerged branch that is not on the never-delete list (could be pruned later); is the BASE branch of PR(s) [690]; branch NAME referenced in repository files on main/retained heads; branch NAME referenced in GitHub PR/issue body or comment — e.g. data/grixis/m7/grokbot_production_ledger.json — PR #690 (closed) body/title |
| `grokbot-deck16-edea-possessed-sorceress-m7-20261023` | `cc2e6d45e5ad4a74b96d30ce07428144f8a111f4` | only container is chatgpt-deck16-edea-m7-rev2-independent-audit-20261023, an unmerged branch that is not on the never-delete list (could be pruned later); is the BASE branch of PR(s) [691]; branch NAME referenced in repository files on main/retained heads — e.g. data/grixis/m7/grokbot_production_ledger.json |
| `grokbot-deck17-edward-kenway-m7-20261023` | `5f5a3a0fbe576ada80c9ea6f71a466834ea9f694` | only container is chatgpt-deck17-edward-m7-rev2-independent-audit-20261023, an unmerged branch that is not on the never-delete list (could be pruned later); is the BASE branch of PR(s) [692]; branch NAME referenced in repository files on main/retained heads — e.g. data/grixis/m7/grokbot_production_ledger.json |
| `grokbot-deck18-evelyn-the-covetous-m7-20261023` | `8150b96898bcd4d8631ae80352b5f59ec158dbcf` | only container is chatgpt-deck18-evelyn-m7-rev2-independent-audit-20261023, an unmerged branch that is not on the never-delete list (could be pruned later); is the BASE branch of PR(s) [693]; branch NAME referenced in repository files on main/retained heads — e.g. data/grixis/m7/grokbot_production_ledger.json |
| `grokbot-deck19-fire-lord-azula-m7-20261023` | `1946a316e457f5751dbd8bca2f3e67bdf0530cd7` | only container is chatgpt-deck19-azula-independent-audit-20261024, an unmerged branch that is not on the never-delete list (could be pruned later); is the BASE branch of PR(s) [694]; branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/m7-fire-lord-azula-chatgpt-alternatives.yml, data/grixis/m7/grokbot_production_ledger.json |
| `grokbot-deck20-garza-zol-plague-queen-m7-20261023` | `909543a544aee2a170aca9e668141624d2343e50` | only container is chatgpt-deck20-garza-independent-m7-rev2-20261024, an unmerged branch that is not on the never-delete list (could be pruned later); is the BASE branch of PR(s) [695]; branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/m7-garza-chatgpt-independent.yml, data/grixis/m7/grokbot_production_ledger.json |
| `grokbot-deck21-goro-goro-and-satoru-m7-20261023` | `3d550c79d11e23b8eefc3bf8cd86705b28356c1a` | only container is chatgpt-m7-deck21-goro-satoru-independent-20261024, an unmerged branch that is not on the never-delete list (could be pruned later); is the BASE branch of PR(s) [696]; branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/chatgpt-m7-deck21-independent.yml, data/grixis/m7/grokbot_production_ledger.json |
| `grokbot-deck22-gwendlyn-di-corci-m7-20261023` | `7483728a700e01f2b45172c9c55438903d9092ac` | only container is chatgpt-m7-deck22-gwendlyn-independent-20261024, an unmerged branch that is not on the never-delete list (could be pruned later); is the BASE branch of PR(s) [697]; branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/chatgpt-m7-deck22-independent.yml, data/grixis/m7/grokbot_production_ledger.json |
| `grokbot-deck23-inalla-archmage-ritualist-m7-20261023` | `1efba1a2fb541eaa2d3ea8f8347d6668acf0ffa1` | only container is chatgpt-m7-deck23-inalla-independent-20261024, an unmerged branch that is not on the never-delete list (could be pruned later); is the BASE branch of PR(s) [698]; branch NAME referenced in repository files on main/retained heads — e.g. data/grixis/m7/grokbot_production_ledger.json |
| `grokbot-deck26-kess-dissident-mage-m7-20261023` | `b505d828cf8936871385d33f57725def295f0b7c` | only container is chatgpt-deck26-kess-m7-rev1-20261024, an unmerged branch that is not on the never-delete list (could be pruned later); is the BASE branch of PR(s) [704]; branch NAME referenced in repository files on main/retained heads — e.g. .github/workflows/m7-kess-chatgpt-rev1.yml, data/grixis/m7/grokbot_production_ledger.json |
| `grokbot-deck28-loki-the-deceiver-m7-20261023` | `842f78d94d51770e05f6672e562eadb33eadbdd2` | only container is chatgpt-loki-m7-rev1-independent-20261025, an unmerged branch that is not on the never-delete list (could be pruned later); branch NAME referenced in repository files on main/retained heads — e.g. data/grixis/m7/grokbot_production_ledger.json |
| `grokbot-deck29-lord-of-tresserhorn-m7-20261023` | `e117a5ca7acbd45bfb44c077e80d3038ed8dabf1` | branch NAME referenced in repository files on main/retained heads — e.g. data/grixis/m7/grokbot_production_ledger.json |
| `grokbot-deck30-lord-xander-m7-20261023` | `d2132bfbf396cb8c60fb85b1e8b6c01b5c1982a2` | branch NAME referenced in repository files on main/retained heads — e.g. data/grixis/m7/grokbot_production_ledger.json |
| `jlk-pass-c-03-admiral-brass-unsinkable` | `302af570b9100f5dc0f820b474e16f74b11e381d` | branch NAME referenced in repository files on main/retained heads — e.g. data/grixis/m6/owner_pass_c_substitute/Admiral_Brass__Unsinkable/seal.json |
| `jlk-pass-c-04-anhelo-the-painter` | `6a8704cc7d2ddb679fa9db4855f6769b38898382` | branch NAME referenced in repository files on main/retained heads — e.g. data/grixis/m6/owner_pass_c_substitute/Anhelo__the_Painter/seal.json |
| `jlk-pass-c-05-ashad-the-lone-cyberman` | `35822d1ad1cc8ce3af611aa6802ab3d1bc6809bf` | branch NAME referenced in repository files on main/retained heads — e.g. data/grixis/m6/owner_pass_c_substitute/Ashad__the_Lone_Cyberman/seal.json |
| `jlk-pass-c-40-nekusar-evidence` | `454fa1b70ee12eb951733f67601af0fbe7660f05` | branch NAME referenced in repository files on main/retained heads — e.g. data/grixis/m6/owner_pass_c_substitute/Nekusar__the_Mindrazer/seal.json |
| `jlk-pass-c-49-sauron-lord-evidence` | `44c6438f0cb94432cb3c579fb0aa0539dd3db7d0` | branch NAME referenced in repository files on main/retained heads — e.g. data/grixis/m6/owner_pass_c_substitute/Sauron__Lord_of_the_Rings/stage_b_reconciliation.md |
| `m7-deck38-missy-rev1-20261026` | `0afd9afc474880769c28fbe6cbc461d35d56f930` | head commit dated within last 7 days (2026-10-26T16:27:02-04:00); branch NAME referenced in repository files on main/retained heads — e.g. data/grixis/m7/decision_reviews/Missy_rev1.json |
| `m7-deck43-norman-chatgpt-rev1` | `f98793c3673a8a99fcae394fb02885f3cb424a2d` | head commit dated within last 7 days (2026-10-26T20:35:55-04:00) |
| `m7-deck45-obeka-splitter-rev1-review` | `6b1e4203210f3f6f765f2876597a0c4af554ceb6` | head commit dated within last 7 days (2026-10-26T23:06:05-04:00) |
| `m7/deck62-zevlor-rev1-exact-20261027` | `4145603e8a13c3470486f9663c15239f247ff3d6` | only container is m7/evidence-backfill-eight-p0-20261027, an unmerged branch that is not on the never-delete list (could be pruned later); head commit dated within last 7 days (2026-10-27T23:54:50-04:00) |
