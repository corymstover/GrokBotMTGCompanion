"""Authored, source-bound M7 Rev1 judgments in the repository gate's schema."""

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DECK = "Obeka__Brute_Chronologist"
PREFIX = "data/grixis/m7/candidate_lists/"
PRIMARY = PREFIX + DECK + "_chatgpt_rev1.txt"
ALT7 = PREFIX + DECK + "_7swap_muddle_alternative.txt"
ALT8 = PREFIX + DECK + "_8swap_graveyard_alternative.txt"
OUT = ROOT / "data/grixis/m7/decision_reviews/Obeka__Brute_Chronologist_rev1.json"
ORACLE = "data/grixis/m7/oracle_snapshots/Obeka__Brute_Chronologist_Rev1_Scryfall_20261027.json"
TESTS = "data/grixis/m7/verification/Obeka__Brute_Chronologist_Rev1_Scoped_M6_IJ_20261027.json"
M6 = "data/grixis/m6/deep_reviews/Obeka__Brute_Chronologist.md"
SOURCES = [
    "Canonical corymstover/grixis-commander-encyclopediaGPT/main Oct15 Obeka 100, SHA256 31b6ff7f23effa78512c2a409a21440bccf457e6faece51d8db38b74102169a8.",
    "Existing M6 whole-100 deep review and formal owner-equivalent Pass C sealed Stage C; 181 exploratory M5 pairwise screens are not effect-aware competitive win-rate claims.",
    "EDHREC live Obeka commander page, Top Cards and High Lift, and optimized Bracket 4 view read 2026-10-26 CDT: https://edhrec.com/commanders/obeka-brute-chronologist and https://edhrec.com/commanders/obeka-brute-chronologist/optimized.",
    "EDHREC commander-specific Extra Turns / Clones / Reanimator tag and the optimized combo alternatives, plus OFF-RANKING engine discovery: Spellseeker ETB tutor, Entomb grave setup, Mimic Vat and Splinter Twin repeatable native clones.",
    "Fresh Scryfall public cards/collection full 100-card Oracle, legality and color identity 2026-10-27 UTC; snapshot committed with this exact candidate SHA.",
    "First-party WotC Oracle correction for Delina's recurring ordinary end-of-combat trigger, 2022-09-02: https://magic.wizards.com/en/news/announcements/oracle-changes-2022-09-02.",
]
SWAPS = [
    ("Footsteps of the Goryo", "Delina, Wild Mage"),
    ("Entomb", "Windfall"),
    ("Mimic Vat", "Purphoros, Bronze-Blooded"),
    ("Zealous Conscripts", "Ilharg, the Raze-Boar"),
    ("Splinter Twin", "Hate Mirage"),
    ("Spellseeker", "Avaricious Dragon"),
]


def sha(relative):
    return hashlib.sha256((ROOT / relative).read_bytes()).hexdigest()


def weak(card, alternative, weakness, tradeoff):
    return {"card": card, "alternative_named": alternative,
            "weakness": weakness, "reasoning": tradeoff}


WEAK = [
    weak("Delina, Wild Mage", "Footsteps of the Goryo",
         "Four-mana attack/d20 source whose token exile is a normal recurring end-of-combat ability, not a one-shot liability.",
         "Delina can immediately multiply ETBs and enabled a Kiki line, but it does not permanently save its own tokens with a single Obeka use."),
    weak("Windfall", "Entomb",
         "Three-mana symmetric wheel can refill opposing interaction, and Obeka has stronger unusually focused setup demands.",
         "Retaining it would help generic hand refill and discard, but Entomb directly supplies Footsteps, Apprentice, Animate Dead, Necromancy and Feldon."),
    weak("Purphoros, Bronze-Blooded", "Mimic Vat",
         "Five-mana red/artifact-restricted creature-cheat redundancy with Sneak Attack and many existing haste sources.",
         "Purphoros supplies durable global haste; Mimic Vat needs actual nontoken death plus three-mana activation but creates reusable one-shot clones."),
    weak("Ilharg, the Raze-Boar", "Zealous Conscripts",
         "Five-mana attack-gated hand cheat needs a combat turn, a creature in hand and commander timing.",
         "Ilharg can permanently cheat a body after Obeka catches the return; Conscripts impacts ETB immediately and forms a deterministic Kiki loop."),
    weak("Hate Mirage", "Splinter Twin",
         "Four-mana one-shot copies depend entirely on opposing creatures being available and worth copying.",
         "Hate Mirage can make two strong opposing tokens at once; Splinter Twin is slower to set up but makes repeatable own ETBs and pairs with Conscripts."),
    weak("Avaricious Dragon", "Spellseeker",
         "Four-mana repeated extra draw requires Obeka to suppress a newly recurring full-hand discard every turn.",
         "Dragon is high lift and worthwhile in slower hands; Spellseeker is a cheaper, cloneable ETB which finds Final Fortune, Twinflame or Entomb."),
    weak("Psychic Vortex", "Dawn of the Dead",
         "Four-mana UU engine has a fresh land-sacrifice/hand-discard trigger every own end step and needs an available end-turn effect.",
         "Retain: its cumulative upkeep draws more cards each turn rather than costing more mana; BBB Dawn is narrower, later and grave-dependent."),
    weak("Rionya, Fire Dancer", "Corpse Dance",
         "Five-mana combat copier may produce only one clone on low-spell turns and is vulnerable before a combat step.",
         "Retain: recurring combat-token engine does not require top graveyard card ordering or five mana for buyback; Corpse Dance adds redundancy."),
    weak("Counterspell", "Muddle the Mixture",
         "Double-blue universal interaction competes with assembling low-cost two-card Scepter/Final Fortune engines.",
         "Retain: Muddle can transmute for the key MV2 pieces, but losing an answer to creatures/artifacts/enchantments exposes Obeka's full-turn liabilities."),
    weak("Venser, Fervent Forger", "Cauldron Dance",
         "Six-mana flash modal commander-native value demands a costly turn before Obeka can transform its temporary copy.",
         "Retain: Cauldron Dance is combat-only, costs 4BR and needs both a hand body and a graveyard body to exceed Venser's flexible spell interaction."),
    weak("Fellwar Stone", "Tribute Mage",
         "Two-mana opponent-dependent colored mana source is rarely spectacular in triple-pip turns.",
         "Retain: Tribute Mage can tutor Scepter, but exchanging turn-two color development for turn-three tutoring weakens early 1UBR Obeka access."),
    weak("Discontinuity", "Stifle",
         "Four-mana own-turn backup can be clunky beside Sundial and Obeka.",
         "Retain: it exiles the entire stack and independently ends the turn; one-mana Stifle removes one trigger but cannot replace the emergency turn-ending role."),
]


def candidate(card, cut, role, synergy, tradeoff, judgment, reason, confidence="MODERATE"):
    return {
        "card": card,
        "source": "Live 2026-10-26 EDHREC inclusion/lift and theme views, Oct20 M6 and sealed Pass C, plus exact Scryfall Oracle for every selected addition.",
        "role": role,
        "named_cuts": [cut],
        "incumbent_opportunity_cost": tradeoff,
        "commander_synergy": synergy,
        "adversarial_downside": tradeoff,
        "judgment": judgment,
        "reason": reason,
        "confidence": confidence,
        "evidence_refs": [ORACLE if judgment == "SELECT_ADD" else M6, TESTS],
    }


CANDIDATES = [
    candidate("Footsteps of the Goryo", "Delina, Wild Mage",
              "Three-mana own-graveyard reanimation with genuine one-shot next-end-step sacrifice.",
              "Obeka saves the entire returned creature after its single sacrifice trigger is on stack.",
              "Needs a creature in our graveyard, gives no haste, and loses Delina's attack-trigger high-roll copies.",
              "SELECT_ADD", "Rules-correct one-shot liability and graveyard package has higher repeatable Obeka value than misleading Delina permanence.", "HIGH"),
    candidate("Entomb", "Windfall",
              "One-black graveyard selection for reanimation and re-copy payoffs.",
              "Finds a creature for Footsteps, Reanimate, Necromancy, Apprentice and Feldon; converts tutor into an Obeka-saveable body.",
              "Windfall can refill an empty hand and proactively discard; Entomb is card-negative without a graveyard outlet.",
              "SELECT_ADD", "A one-mana instant that sources exactly the otherwise conditional reanimation package without replenishing opponents' counters.", "HIGH"),
    candidate("Mimic Vat", "Purphoros, Bronze-Blooded",
              "Three-mana imprint artifact with three-mana tap repeatable hasty creature token copying.",
              "Copies have real one-shot next-end-step exile to erase, and repeated Spellseeker/Puppeteer ETBs are available.",
              "Requires a nontoken death and permanent imprint, creates graveyard tension, and loses Purphoros global haste/indestructibility.",
              "SELECT_ADD", "Greater repeatable Obeka-specific clone payoff at lower initial mana, backed by existing haste and Sneak Attack redundancy.", "MODERATE"),
    candidate("Zealous Conscripts", "Ilharg, the Raze-Boar",
              "Five-mana hasty theft/untap ETB and two naturally co-located Kiki/Twin clone loop payoffs.",
              "Untaps a needed permanent, can regain Obeka tap access, and forms Kiki-Jiki or Splinter Twin finite-repeatable Conscripts loops.",
              "Steal expires in cleanup without a clone loop; loses Ilharg's repeatable attack-based creature cheating.",
              "SELECT_ADD", "Immediate ETB action and a credible hasty finisher justify replacing slower five-mana attack setup.", "HIGH"),
    candidate("Splinter Twin", "Hate Mirage",
              "Four-mana Aura that grants repeatable, hasty temporary copies of own creature.",
              "Obeka permanently preserves one-shot token exile and Zealous Conscripts provides untapping copy-combo parity.",
              "Requires an own creature that can tap, an Aura exposed to removal and setup; loses two-opponent-creature Hate Mirage burst.",
              "SELECT_ADD", "Persistent clone access with in-list Spellseeker/Conscripts/Courser ETBs earns the slot beyond a one-shot opposing-board copy.", "HIGH"),
    candidate("Spellseeker", "Avaricious Dragon",
              "Three-mana creature ETB tutor for instant/sorcery mana value at most two.",
              "Searches Final Fortune, Twinflame, Entomb, protection and cheap tutors; Mimic Vat/Reflection/Kiki can repeat its ETB.",
              "Loses a four-mana flying continuous extra draw engine whose recurring discard Obeka could suppress.",
              "SELECT_ADD", "Improves fast protected access to commander-native win/setup spells while Psychic Vortex, Remora and Rhystic retain draw.", "HIGH"),
    candidate("Muddle the Mixture", "Counterspell",
              "UU narrower instant/sorcery counter or 1UU sorcery transmute tutor of Scepter/Final Fortune.",
              "Finds both MV2 two-card combo pieces while allowing end-step trigger counterplay on instants.",
              "Cannot counter creatures, artifacts or enchantments; transmute is sorcery-speed and triple-mana upfront.",
              "RETAIN_ALTERNATIVE", "Seven-swap exact challenger improves combo access but losing unconditional protection is a worse full-pod tradeoff."),
    candidate("Corpse Dance", "Rionya, Fire Dancer",
              "2B repeatable top-creature graveyard recursion with optional two-generic buyback.",
              "Creates one-shot next-end-step exile and instant-speed hasty creature bodies for Obeka to retain.",
              "Top-creature graveyard order matters, buyback costs five total and repeated graveyard reliance increases exposure.",
              "RETAIN_ALTERNATIVE", "Eight-swap exact challenger overloads reanimation and sacrifices recurring Rionya combat clones."),
    candidate("Dawn of the Dead", "Psychic Vortex",
              "5-mana BBB upkeep resurrection with haste and next-end-step exile.",
              "Could accumulate one permanent reanimated creature each turn with a ready Obeka.",
              "Triple black is harder than 2UU on 34-land Grixis; graveyard dependence and upkeep trigger lose to Vortex compounding draw.",
              "REJECT", "The held baseline Psychic Vortex is a uniquely fast scalable Obeka draw engine; Dawn is not an additional quality-positive slot."),
    candidate("Treacherous Urge", "Hate Mirage",
              "4B opponent-hand creature theft and timed next-end-step sacrifice.",
              "Obeka could retain any stolen creature instead of sacrificing at next end step.",
              "Opposing hands can hold no creatures and the five-mana reaction exposes Obeka to instant removal.",
              "RETAIN_ALTERNATIVE", "Strong table-dependent alternate theft package, but less repeatable than selected Splinter Twin."),
    candidate("Cauldron Dance", "Venser, Fervent Forger",
              "4BR combat-only dual creature cheat from graveyard and hand with two delayed liabilities.",
              "On a developed board, one Obeka activation could retain two bodies instead of returning/sacrificing.",
              "Must cast during combat, have both proper zones and six mana; Venser gives flexible flash interaction.",
              "RETAIN_ALTERNATIVE", "High tactical ceiling, but narrower and no lower mana cost than retained six-mana Venser."),
    candidate("Zara, Renegade Recruiter", "Ilharg, the Raze-Boar",
              "Five-mana opponent-hand creature cheat on attack, next-end-step return-to-hand liability.",
              "Obeka can permanently keep a stolen creature after the return trigger is exiled.",
              "Requires Zara to attack/survive, a creature in an opponent's hand and an untapped Obeka later.",
              "RETAIN_ALTERNATIVE", "More native one-shot theft than Ilharg, but immediate Conscripts ETB and Kiki/Twin win integration is superior."),
    candidate("Orthion, Hero of Lavabrink", "Purphoros, Bronze-Blooded",
              "Tap-based single/five token copy activations with one-shot end-step sacrifices.",
              "Obeka can retain multiple haste tokens, including repeated Spellseeker/Courser ETBs.",
              "Needs summoning sickness solved; five-token activated mode costs nine mana and cannot scale early.",
              "REJECT", "Mimic Vat has lower setup cost and flexible imprint opportunities; retain haste infrastructure elsewhere."),
    candidate("Imperial Recruiter", "Counterspell",
              "2R low-power creature ETB tutor that finds Kiki-Jiki, Dualcaster Mage or Spellseeker.",
              "Copies can chain tutors and help assemble creature-based Obeka finishing lines.",
              "Trades crucial universal interaction for another sorcery-speed proactive creature tutor; Kiki remains RRRed.",
              "RETAIN_ALTERNATIVE", "Credible off-ranking utility but not a defensible seventh removal of protection."),
    candidate("The Master, Multiplied", "Rionya, Fire Dancer",
              "Legendary token-preservation engine independently disables sacrificing or exiling owned creature tokens.",
              "Can keep certain tokens without the turn-ending response window.",
              "Explicitly bypasses Obeka's unique end-turn payoff and fails to fix non-token risky-turn loss triggers.",
              "REJECT", "Commander-identity cost exceeds the resilience gain; this would progressively replace Obeka's defining role."),
    candidate("Tribute Mage", "Fellwar Stone",
              "2U creature ETB searches a two-mana artifact such as Isochron Scepter.",
              "Token/recursion copying creates repeatable access to Scepter, Boots, Signet or an engine artifact.",
              "Loses turn-two colored acceleration for Obeka's 1UBR and RR turn-spell pip requirements.",
              "REJECT", "Source-reliable mana ramp has higher deckwide floor than another three-mana tutor."),
    candidate("Stifle", "Discontinuity",
              "One-blue instant answers one activated or triggered ability including a queued loss trigger.",
              "Protects a risky-turn line without needing Obeka if the liability is alone on the stack.",
              "Fails to stop a pending whole stack or remove multiple liabilities and cannot end an opponent's turn.",
              "RETAIN_ALTERNATIVE", "Emergency full-stack end-turn backup and split stack coverage justify retaining Discontinuity."),
]


def main():
    adds = [x[0] for x in SWAPS]
    cuts = [x[1] for x in SWAPS]
    assert sha(PRIMARY) == "43f1249c9a1da82bc1e74254a44613a0ab5763c91295a56ffae3b75a889029f2"
    assert len(CANDIDATES) == len({c["card"] for c in CANDIDATES}) == 17
    assert len(WEAK) == 12
    packet = {
        "schema_version": 1,
        "stage": "M7_DECISIVE_OWNER_REVIEW_CANDIDATE",
        "deck_id": DECK,
        "canonical_baseline_sha256": "31b6ff7f23effa78512c2a409a21440bccf457e6faece51d8db38b74102169a8",
        "canonical_baseline_logical_hash": "lh1:958f40565c66c18bf18f1451bac9e933497046c04dc54e58811bfac18d794e66",
        "commander_identity": {
            "mechanical_plan": "Ready Obeka on OUR turn and exile already-stacked, one-shot next-end-step lose/exile/sacrifice liabilities; convert temporary creatures and risky extra turns to lasting card/turn advantage.",
            "protected_core": ["Obeka, Brute Chronologist", "Final Fortune", "Last Chance", "Warrior's Oath", "Isochron Scepter", "Sundial of the Infinite", "Sneak Attack", "Kiki-Jiki, Mirror Breaker", "Dualcaster Mage", "Twinflame", "Hellkite Courser", "Psychic Vortex", "Thousand-Year Elixir"],
            "natural_ceiling": "Power Bracket 4 — Optimized; compact paid combos exist, but commander 1UBR/haste/turn-window dependence and interaction risk prevent an honest Bracket 5 cEDH claim.",
            "anti_homogenization": "Protect risky RR turns, commander-timed clone/reanimation, haste and tap support. Reject generic Thassa Oracle/Consult and The Master Multiplied replacing the commander's task.",
        },
        "whole_deck_audit": {
            "all_noncommand_cards_reviewed": True,
            "roles_and_overlaps": "The exact October 20 source-bound M6 table audits all 99 distinct noncommander physical slots. Rechallenged 12: six selected weak cuts plus preserved Psychic Vortex, Rionya, Counterspell, Venser, Fellwar Stone and Discontinuity. Kept fast mana/talismans, protection, all risky RR turns, Scepter, Twinflame/Dualcaster, Courser and permanent-copy engines.",
            "mana_base_and_curve": "34 unchanged lands, ten artifact mana pieces plus Jeska's Will; one basic each of Island/Mountain/Swamp and fetchable duals supply 1UBR. Selected six MV total 19 replacing MV total 25; reduce heavy red pips, add two single-black role spells. Retains all U/B/R dual access and Talisman/Signet ramp; no speculative cut of an untapped colored source.",
            "interaction_resilience": "Retains Counterspell, Mana Drain, Fierce Guardianship, Force of Will, Deflecting Swat, Chaos Warp, Cyclonic Rift, Toxic Deluge; backup Sundial and Discontinuity, Greaves/Boots/Elixir/Arena/Minamo. Cannot force opponent to end their own turn or use summoning-sick Obeka; removal in the end-step window remains serious.",
            "weakest_slots": WEAK,
            "current_baseline_strength": "October 15 approved source already had nineteen deliberate commander-native upgrades: 100 unique cards, 34 lands, strong risky-turn redundancy, ability haste and protection. M6 Pass C identified two serious research-only swaps but did not authorize them.",
            "candidate_pool_scope": "Revisited 181 historical M5 pairwise hypotheses (not 181 reliable win tests), M6 99-card roles, Josh-Lee-Kwai Stage C, live EDHREC inclusion/high lift and optimized tags, seventeen material candidates plus high-cost alternatives and two complete higher-count 100s.",
            "off_ranked_search_conclusion": "Spellseeker/Entomb precise tutor density, Mimic Vat delayed-token ETBs, Splinter Twin plus Zealous clone finish stand above extra generic draw or reanimation; Dawn BBB, Corpse Dance graveyard order, Muddle counter restriction and other off-ranking options lose deckwide value.",
        },
        "candidate_sources": SOURCES,
        "material_candidates": CANDIDATES,
        "expensive_experiments": [],
        "final_changes": {
            "adds": adds,
            "cuts": cuts,
            "coherent_package_tradeoff": "Six genuine engine swaps move from attacking/tapping expensive red creatures and generic wheel/draw to cheap graveyard selection, one-shot end-step clones, repeatable tutor ETBs and deterministic Kiki/Twin Zealous closing lines. Less standalone Dragon/Vortex-style draw and Purphoros haste, but Vortex stays and haste protection redundancy remains.",
        },
        "low_swap_heightened_audit": {
            "weakest_slot_challenge": WEAK,
            "off_ranked_opportunities": "Live EDHREC optimized high lift checked beyond top ten, including Dawn, Zara, Corpse Dance, Treacherous Urge, Orthion, plus off-ranking Spellseeker/Entomb and newly relevant low-sample cards. Full negative opportunity costs are in material judgments; retained Vortex despite Dawn's enticing one-shot reanimation.",
            "multi_slot_packages": [
                {"adds": adds, "cuts": cuts, "result_and_rationale": "Selected complete six-slot engine/combo package; 100 cards, 34 lands and 100 current Commander-legal Grixis identities."},
                {"adds": adds + ["Muddle the Mixture"], "cuts": cuts + ["Counterspell"], "result_and_rationale": "Complete seven-slot source-verified portfolio; improved MV2 transmute access at the cost of no longer stopping arbitrary permanent spells."},
                {"adds": adds + ["Muddle the Mixture", "Corpse Dance"], "cuts": cuts + ["Counterspell", "Rionya, Fire Dancer"], "result_and_rationale": "Complete eight-slot more recursive package; loses both all-spell counter and repeatable Rionya combat clones; gravity of graveyard hate and top-card order grows."},
            ],
            "no_two_package_reason": None,
            "alternate_cuts_for_prior_holds": "Footsteps over Delina (rather than Avaricious Dragon) corrects the Delina recurring Oracle problem while keeping extra draw until the stronger Spellseeker ETB is chosen; Mimic Vat instead cuts slow red-restricted Purphoros and preserves Rionya and Psychic Vortex. Delina cannot stay to create durable tokens merely because the first exile stack ability is removed.",
            "strongest_argument_against_baseline": "The approved 100 contains a recurring non-delayed Delina trap and excessive five-mana attack-setup red creatures while omitting one-mana Entomb, repeated Splinter/Mimic clones and cloneable cheap-combo tutor Spellseeker. It leaves genuine resilience and engine ceiling on the table.",
            "evidence_based_answer": "Six selected one-for-one changes preserve all core RR turn liabilities and ready-Obeka infrastructure; live 100/100 Scryfall legality, new one-shot triggers, finite P0/P1 negative cases and 34-land colored sources were actually checked. Additional seventh/eighth swaps hurt protection or native token repetition.",
        },
        "final_candidate": {
            "path": PRIMARY, "sha256": sha(PRIMARY), "card_count": 100,
            "deckwide_reconciliation": "100 unique singletons including Obeka and no companion, 34 unchanged lands, six exact additions and six exact removals; retained all risky RR extra turns, Scepter, Sundial, Courser and core haste/untap/protection; candidate raw SHA pinned.",
        },
        "verification": {
            "quantity_singleton_verified": True,
            "color_identity_verified": True,
            "current_oracle_verified": True,
            "official_legality_checked": True,
            "project_exceptions_recorded": True,
            "rules_and_combos_verified": True,
            "source_evidence_paths": [
                "Public live Scryfall " + ORACLE + " includes all 100 exact Commander-legal identity records for raw candidate SHA.",
                "Scoped finite executed 15-case C/K/E/W/F matrix and negative counterexamples in " + TESTS + "; 5 P0 and 10 P1, not a complete Magic engine.",
                "Historical whole-99 authored Obeka review " + M6 + " and sealed Stage C (same GPT-6 family, owner-waived technical independence).",
                "Exact alternative 100s " + ALT7 + " and " + ALT8 + " with documented tradeoffs; canonical source unchanged.",
            ],
            "power_bracket": 4,
            "archidekt_tags": ["Extra Turns", "Delayed Triggers", "Clones"],
            "known_hard_blockers": [],
        },
        "owner_authority": {
            "canonical_deck_changed": False,
            "exact_candidate_owner_approved": False,
            "owner_approval_question": "This deck is complete. Do you approve it?",
        },
        "readiness": "READY_FOR_EXACT_OWNER_APPROVAL_NOT_YET_APPROVED",
        "open_ended_optimization_audit": {
            "floor_not_target": True,
            "remaining_99_review": "After selecting six changes, separately retested pressure on retained Counterspell, Rionya, Psychic Vortex, Venser, Fellwar Stone and Discontinuity. Each saves an irreplaceable answer, native repeatable copy or colored-source/access function. Every higher-count plausible add carries a specific real loss, not a numerical quota concern.",
            "post_floor_challenges": [
                {"incumbent": "Counterspell", "challenger": "Muddle the Mixture", "disposition": "RETAIN_ALTERNATIVE", "tradeoff": "Transmute finds Scepter/Final Fortune but losing the unconditional UU answer to enemy creatures/artifacts/enchantments is a worse all-pod risk."},
                {"incumbent": "Rionya, Fire Dancer", "challenger": "Corpse Dance", "disposition": "RETAIN_ALTERNATIVE", "tradeoff": "Corpse Dance costs five with buyback and returns only the ordered top grave creature; Rionya repeatedly creates multiple one-shot tokens with no graveyard dependency."},
                {"incumbent": "Psychic Vortex", "challenger": "Dawn of the Dead", "disposition": "REJECT", "tradeoff": "Vortex's cumulative upkeep is DRAW cards and Obeka suppresses the recurring land/hand end-step cost; Dawn costs BBB and only reanimates when graveyard stocked."},
                {"incumbent": "Venser, Fervent Forger", "challenger": "Cauldron Dance", "disposition": "RETAIN_ALTERNATIVE", "tradeoff": "Cauldron Dance needs 4BR and combat-window plus creatures in hand and grave; Venser's flashed interaction/copied permanent provides a superior varied ceiling."},
            ],
            "larger_swap_packages": [
                {"path": ALT7, "sha256": sha(ALT7), "adds": adds + ["Muddle the Mixture"],
                 "cuts": cuts + ["Counterspell"],
                 "case_for_extra_swaps": "Seven-slot exact 100 gives Muddle transmute for both key MV2 Scepter/Fortune cards and defensive instant/sorcery counter.",
                 "why_not_selected": "Counterspell handles non-instant permanent spells and is a necessary unqualified shield before high-risk extra turns."},
                {"path": ALT8, "sha256": sha(ALT8), "adds": adds + ["Muddle the Mixture", "Corpse Dance"],
                 "cuts": cuts + ["Counterspell", "Rionya, Fire Dancer"],
                 "case_for_extra_swaps": "Eight-slot exact 100 increases tutor and hasty graveyard reanimation with reusable buyback in a single package.",
                 "why_not_selected": "Lose unconditional counter and repeatable native clone engine, pay expensive buyback and face increased graveyard hate, so the extra quantity is not extra quality."},
            ],
            "no_credible_larger_package_reason": None,
            "quality_based_stop_reason": "Stopped after examining 17 material additions, twelve incumbents, actual six/seven/eight-slot whole-100 alternatives and source-bound rules. The extra seventh Muddle loses indispensable whole-spell interaction, and eighth Corpse Dance replaces repeatable on-theme Rionya with conditional graveyard-order buyback. Other candidates add BBB, extra combat gates, randomness or commander bypass; no remaining credibly quality-positive change justified an additional slot.",
        },
    }
    OUT.write_text(json.dumps(packet, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("Authored Obeka M7 packet", OUT.relative_to(ROOT), "sha", sha(PRIMARY))


if __name__ == "__main__":
    main()
