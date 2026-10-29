# Cory's approved story-first lore decks — 2026-10-28 (America/Chicago)

**Approval source:** Cory explicitly stated, in the ongoing MTG lore-deck conversation: “I approve all of those other decks by the way.” Scope resolved to the seven numbered completed lore proposals, separate from the 62 already-approved Grixis Commander encyclopedia decks.

**Authority:** This is the approval ledger for the exact 100-card story-first proposals archived by the merge commits below. Existing historical `drafts/` paths and earlier `awaiting approval` prose are preserved as snapshots; this ledger supersedes their status text **without changing a single card**. The original Grixis canonical approval authority and lock registry are untouched.

| Lore # | Story | Review PR | Immutable merge commit | Approved deck spec | Rule 0/ban note |
|---:|---|---|---|---|---|
| 1 | The Legacy: Rise and Fall of Yawgmoth | [#768](https://github.com/corymstover/GrokBotMTGCompanion/pull/768) | `3564c9d186335cc430bc665b45738e1fcab9424f` | [`legacy_yawgmoth_final_story.json`](https://github.com/corymstover/GrokBotMTGCompanion/blob/3564c9d186335cc430bc665b45738e1fcab9424f/data/lore_decks/drafts/legacy_yawgmoth_final_story.json) | Three intentionally banned cards: Yawgmoth's Bargain; Rofellos, Llanowar Emissary; Tolarian Academy |
| 2 | The Mending: Death of the Old Gods | [#769](https://github.com/corymstover/GrokBotMTGCompanion/pull/769) | `95eef25bc4ee6bfc7cb09338147e5bd68e15b9db` | [`the_mending_story_proposal.json`](https://github.com/corymstover/GrokBotMTGCompanion/blob/95eef25bc4ee6bfc7cb09338147e5bd68e15b9db/data/lore_decks/drafts/the_mending_story_proposal.json) | One intentionally banned card: Tolarian Academy |
| 3 | War of the Spark: Fall of Nicol Bolas | [#770](https://github.com/corymstover/GrokBotMTGCompanion/pull/770) | `a19671958f576b700f8de264683c72bce1142d14` | [`war_of_the_spark_story_proposal.json`](https://github.com/corymstover/GrokBotMTGCompanion/blob/a19671958f576b700f8de264683c72bce1142d14/data/lore_decks/drafts/war_of_the_spark_story_proposal.json) | No bans reported |
| 4 | The Brothers' War: Urza, Mishra and Argoth | [#771](https://github.com/corymstover/GrokBotMTGCompanion/pull/771) | `bcb16f8061275d0f1ecca5858e03676a3ba699b8` | [`the_brothers_war_story_proposal.json`](https://github.com/corymstover/GrokBotMTGCompanion/blob/bcb16f8061275d0f1ecca5858e03676a3ba699b8/data/lore_decks/drafts/the_brothers_war_story_proposal.json) | No bans reported |
| 5 | The Kami War: Theft of a God | [#772](https://github.com/corymstover/GrokBotMTGCompanion/pull/772) | `efb59db8884c176cf69af04ba878be47b383f0da` | [`the_kami_war_story_proposal.json`](https://github.com/corymstover/GrokBotMTGCompanion/blob/efb59db8884c176cf69af04ba878be47b383f0da/data/lore_decks/drafts/the_kami_war_story_proposal.json) | No bans reported |
| 6 | Battle for Zendikar: Rise of the Gatewatch | [#773](https://github.com/corymstover/GrokBotMTGCompanion/pull/773) | `913e28e5d6e18c49219b78f60ce52830da30f4b4` | [`battle_for_zendikar_story_proposal.json`](https://github.com/corymstover/GrokBotMTGCompanion/blob/913e28e5d6e18c49219b78f60ce52830da30f4b4/data/lore_decks/drafts/battle_for_zendikar_story_proposal.json) | One intentionally banned card: Emrakul, the Aeons Torn |
| 7 | Ravnica: Ten Guilds and the Living Guildpact | [#774](https://github.com/corymstover/GrokBotMTGCompanion/pull/774) | `abc8267256eed24ddc3f726fc7ee36cb2b047f28` | [`ravnica_guildpact_story_proposal.json`](https://github.com/corymstover/GrokBotMTGCompanion/blob/abc8267256eed24ddc3f726fc7ee36cb2b047f28/data/lore_decks/drafts/ravnica_guildpact_story_proposal.json) | No bans reported |

## Independent postmerge presence check

All seven exact `.json` draft specifications were read successfully from `main` after merging #768–#774. Every review PR modified only additive files under `data/lore_decks/drafts/`; no Grixis decklist or approval registry was altered.

## Preservation and provenance

- Each version is pinned to its merge commit above; a later revision is a *new candidate*, not an automatic replacement of Cory's approved copy.
- The banned-card Rule 0 exceptions are expressly retained for story significance. Approval of a story deck is not a claim that its prohibited cards are sanctioned-legal.
- The five unapproved earlier Yawgmoth variant/background files in PR #768 remain only for historical comparison; **the approved exact deck** is `legacy_yawgmoth_final_story.json` / `.md`, not its superseded casual/museum drafts.
- Each original `.md` has its card-by-card story explanation, and the original 100-card list. No card substitution or gameplay retuning occurred during approval.
- Do not touch `corymstover/grixis-commander-encyclopediaGPT/main` or its lock registry from this lore approval.
