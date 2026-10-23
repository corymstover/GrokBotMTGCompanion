"""Deck 31 Lynde__Cheerful_Tormentor (Lynde, Cheerful Tormentor) M7 research candidate: structural checks only, not
approval.

The packet is RESEARCH_ONLY_WITHDRAWN_NOT_OWNER_PRESENTABLE and BLOCKED: the existing M6 Pass C Stage A seal does not match
its committed stage_a.md (the sealed value is the SHA-256 of the file without its final newline byte, so no J bundle can
pass the shared checker), and only two genuine swaps were found (+Court of Vantress -Cruel Reality; +Extravagant
Replication -Curse of Death's Hold), below the five-swap floor. Neither cut is an owner keep or add; single-swap
alternatives A and B are staged as complete 100s. Nothing is padded."""
from __future__ import annotations
import ast
import hashlib
import json
import unittest
from collections import Counter
from pathlib import Path

from scripts import grixis_m7_decision_gate as gate

ROOT = Path(__file__).resolve().parents[1]
D = "Lynde__Cheerful_Tormentor"
LYNDE = "Lynde, Cheerful Tormentor"
PACKET = ROOT / f"data/grixis/m7/decision_reviews/{D}.json"
BASE = ROOT / f"data/grixis/m7/baseline_sources/{D}_approved_source_2026-10-14.txt"
RAW = "05d1c4eea023d25e4308f78b109e80b78e0a3f4d655c3df36743ba3afbf04166"
CAND_RAW = "435717e03dc60e874f638b0daf8ebc9ce2e898d00207985daebe789acf47fb77"
LH = "lh1:7359723b249d034d4496f17f16bd6f061e7a14c9eb4ac6bb70ae7f058711a5d7"
CAND_LH = "lh1:a125b99270e7e4fb1229344bcee482d06e96bc2adf797fc9e5a74528e3868408"
RC = ROOT / "data/grixis/m7/research_challengers"
COURT, REPL = "Court of Vantress", "Extravagant Replication"
CRUEL, DEATH = "Cruel Reality", "Curse of Death's Hold"
NIGHT = "Nightscape Familiar"
OWNER_REMOVED = ("Curse of Oblivion", "Curse of Chaos", "Curse of Shallow Graves", "Fraying Sanity", "Crystal Chimes",
                 "Protean Thaumaturge", "Sphinx of the Second Sun")
OWNER_REJECTED = ("Strionic Resonator", "Beseech the Mirror", "Shadow of the Second Sun", "Valeria Richards",
                  "The Unluckiest Planeswalker", "Jabs, Mistress of Mockery")


class LyndeCheerfulTormentorM7Tests(unittest.TestCase):
    def setUp(self):
        self.packet = json.loads(PACKET.read_text())
        self.registry = json.loads((ROOT / "data/grixis/registry.json").read_text())
        self.judged = {c["card"]: c for c in self.packet["material_candidates"]}

    def cand(self):
        return Counter(gate.parse_list(ROOT / self.packet["final_candidate"]["path"])[0])

    def test_gate_passes_as_withdrawn_research_only_with_seal_blocker(self):
        result = gate.verify_packet(self.packet, root=ROOT, registry=self.registry)
        self.assertFalse(result["owner_presentable"])
        self.assertEqual(result["new_swaps"], 2)
        self.assertEqual(result["status"], "M7_WITHDRAWN_RESEARCH_ONLY_NOT_OWNER_PRESENTABLE")
        self.assertEqual(self.packet["readiness"], "RESEARCH_ONLY_WITHDRAWN_NOT_OWNER_PRESENTABLE")
        reason = self.packet["withdrawal_reason"]
        for s in ("RESEARCH_ONLY and BLOCKED", "Seal blocker", "commit c4c5fa5df5d55114c5f7e773d103d8490e60b67b",
                  "59f2dc10eedec5797f3f5dcfdb0a206b380a037e9b17a29e740d6ca94829c12e",
                  "02adfb85db19aa42d5dfe36b96906874ea1abd232b6f8bfc3861c1108035b72a",
                  "Stage A source diverged from separately sealed byte commitment",
                  "The sealed evidence and the checker are not edited", "Only two genuine swaps", "NOT owner approved"):
            self.assertIn(s, reason)
        self.assertNotIn("FLAGGED", reason)  # no owner keep/add is overridden
        self.assertFalse(self.packet["owner_authority"]["exact_candidate_owner_approved"])
        self.assertFalse(self.packet["owner_authority"]["canonical_deck_changed"])
        self.assertNotIn("baseline_provenance_exception", self.packet)
        self.assertEqual(self.packet["verification"]["known_hard_blockers"], [])

    def test_registry_matches_raw_and_vendored_copy_is_byte_identical(self):
        src = self.registry["decks"][D]["source"]
        self.assertEqual(src["recorded_sha256"], RAW)
        self.assertEqual(src["raw_sha256"], "sha256:" + RAW)
        self.assertIs(src["recorded_matches_raw"], True)
        self.assertEqual(self.packet["canonical_baseline_sha256"], RAW)
        self.assertEqual(hashlib.sha256(BASE.read_bytes()).hexdigest(), RAW)
        cand = ROOT / self.packet["final_candidate"]["path"]
        self.assertEqual(hashlib.sha256(cand.read_bytes()).hexdigest(), CAND_RAW)
        self.assertEqual(self.packet["final_candidate"]["sha256"], CAND_RAW)
        self.assertEqual(self.packet["canonical_baseline_logical_hash"], LH)
        self.assertEqual(self.registry["decks"][D]["current_canonical_hash"], LH)
        self.assertIn(CAND_LH, self.packet["final_candidate"]["deckwide_reconciliation"])
        self.assertEqual(self.registry["decks"][D]["commanders"], [LYNDE])

    def test_exactly_two_swaps_against_vendored_and_canonical_source(self):
        cand = self.cand()
        path, md = gate.canonical_source(ROOT, self.registry["decks"][D])
        for base in (Counter(gate.parse_list(BASE)[0]), Counter(gate.parse_list(path, source_markdown=md)[0])):
            self.assertEqual(sorted((cand - base).elements()), sorted([COURT, REPL]))
            self.assertEqual(sorted((base - cand).elements()), sorted([CRUEL, DEATH]))
        self.assertEqual(self.packet["final_changes"]["adds"], [COURT, REPL])
        self.assertEqual(self.packet["final_changes"]["cuts"], [CRUEL, DEATH])

    def test_commander_first_100_physical_with_basics_alphabetical(self):
        lines = [x for x in (ROOT / self.packet["final_candidate"]["path"]).read_text().splitlines() if x.strip()]
        self.assertEqual(lines[0], f"1x {LYNDE} [Commander]")
        self.assertEqual(sum(1 for x in lines if x.endswith("[Commander]")), 1)
        self.assertFalse(any("[Companion]" in x for x in lines))
        self.assertEqual(sum(int(x.split("x ", 1)[0]) for x in lines), 100)
        self.assertEqual(sorted(x for x in lines if not x.startswith("1x ")), ["3x Mountain", "3x Swamp", "4x Island"])
        rest = [x.split("x ", 1)[1] for x in lines[1:]]
        self.assertEqual(rest, sorted(rest, key=str.lower))
        self.assertEqual(len(set(rest)), 92)

    def test_commander_first_identity_and_distinctness(self):
        plan = self.packet["commander_identity"]["mechanical_plan"]
        for s in ("{1}{U}{B}{R} legendary Human Warlock 2/4 deathtouch", "not a Game Changer", "no project exception",
                  "return it attached to you at the beginning of the next end step", "draw two"):
            self.assertIn(s, plan)
        note = self.packet["commander_identity"]["anti_homogenization"]
        self.assertIn("Commander-first to Lynde's Oracle", note)
        for s in ("Garza Zol, Plague Queen 42", "Solkanar the Swamp King 41", "Nicol Bolas 40", "Solkanar the Tainted 39",
                  "Mai and Zuko 39", "Cruel Reality and Curse of Death's Hold appear in none"):
            self.assertIn(s, note)

    def test_owner_direction_removed_not_readded_owner_cards_kept_and_judgments(self):
        cand = self.cand()
        for card in OWNER_REMOVED + OWNER_REJECTED + (CRUEL, DEATH, "Grievous Wound", "Thassa's Oracle",
                                                      "Demonic Consultation"):
            self.assertNotIn(card, cand)
        core = self.packet["commander_identity"]["protected_core"]
        self.assertNotIn(CRUEL, core)
        self.assertNotIn(DEATH, core)
        for keep in core:
            self.assertEqual(cand[keep], 1, keep)  # no owner keep or add is cut
        self.assertEqual([c for c, v in self.judged.items() if v["judgment"] == "SELECT_ADD"], [COURT, REPL])
        self.assertEqual(self.judged[COURT]["named_cuts"], [CRUEL])
        self.assertEqual(self.judged[REPL]["named_cuts"], [DEATH])
        self.assertEqual(self.judged["Staff of Compleation"]["judgment"], "RETAIN_ALTERNATIVE")
        for rej in ("Curse of Chaos", "Strionic Resonator", "Beseech the Mirror", "Disturbing Mirth",
                    "Teferi's Ageless Insight", "Thoughtrender Lamia", "Curse of the Bloody Tome", "Grievous Wound",
                    "Witchbane Orb", "Price of Knowledge", "Mogis, God of Slaughter", "Painful Quandary",
                    "Swiftfoot Boots", "Reliquary Tower", "Cloud Key", "Silent Arbiter"):
            self.assertEqual(self.judged[rej]["judgment"], "REJECT", rej)
        for inv in ("The Unluckiest Planeswalker", "Jabs, Mistress of Mockery"):
            self.assertEqual(self.judged[inv]["judgment"], "EXCLUDE_INVALID", inv)
        self.assertEqual(len(self.judged), 21)
        audit = self.packet["low_swap_heightened_audit"]
        weak = [x["card"] for x in audit["weakest_slot_challenge"]]
        self.assertEqual(len(weak), 13)
        for card in (CRUEL, DEATH, NIGHT, "Curse of Unbinding", "Exotic Orchard"):
            self.assertIn(card, weak)
        pk = [(sorted(p["adds"]), sorted(p["cuts"])) for p in audit["multi_slot_packages"]]
        self.assertEqual(pk[0], (sorted([COURT, REPL]), sorted([CRUEL, DEATH])))
        self.assertEqual(len(pk), 5)

    def test_power_bracket_tags_game_changers(self):
        v = self.packet["verification"]
        self.assertEqual(v["power_bracket"], 4)
        self.assertEqual(v["archidekt_tags"], ["Curses", "Enchantress", "Control"])
        self.assertIn("Game Changers: 8 in both baseline and candidate", self.packet["commander_identity"]["natural_ceiling"])

    def test_alternatives_staged_as_complete_hundreds(self):
        def load(name):
            return Counter(gate.parse_list(RC / f"{D}_{name}_20261023.txt")[0])
        a2, c2 = [COURT, REPL], [CRUEL, DEATH]
        cases = {
            "alt_A_CourtOnly_minus_CruelReality": ([COURT], [CRUEL]),
            "alt_B_ReplicationOnly_minus_CurseOfDeathsHold": ([REPL], [DEATH]),
            "staged_plus_StaffOfCompleation_minus_NightscapeFamiliar": (a2 + ["Staff of Compleation"], c2 + [NIGHT]),
            "PassC_plus_CurseOfChaos_minus_CurseOfEchoes": (a2 + ["Curse of Chaos"], c2 + ["Curse of Echoes"]),
            "PassC_plus_StrionicResonator_minus_NightscapeFamiliar": (a2 + ["Strionic Resonator"], c2 + [NIGHT]),
            "PassC_plus_BeseechTheMirror_minus_CurseOfTheRestlessDead": (a2 + ["Beseech the Mirror"],
                                                                         c2 + ["Curse of the Restless Dead"]),
            "rejected_plus_DisturbingMirth_minus_TrespassersCurse": (a2 + ["Disturbing Mirth"], c2 + ["Trespasser's Curse"]),
            "rejected_plus_TeferisAgelessInsight_minus_CurseOfUnbinding": (a2 + ["Teferi's Ageless Insight"],
                                                                           c2 + ["Curse of Unbinding"]),
            "rejected_plus_ThoughtrenderLamia_minus_BitterheartWitch": (a2 + ["Thoughtrender Lamia"], c2 + ["Bitterheart Witch"]),
            "rejected_plus_CurseOfTheBloodyTome_minus_MaddeningHex": (a2 + ["Curse of the Bloody Tome"], c2 + ["Maddening Hex"]),
        }
        base = Counter(gate.parse_list(BASE)[0])
        core = self.packet["commander_identity"]["protected_core"]
        for name, (adds, cuts) in cases.items():
            a = load(name)
            self.assertEqual(sum(a.values()), 100, name)
            self.assertEqual(sorted((a - base).elements()), sorted(adds), name)
            self.assertEqual(sorted((base - a).elements()), sorted(cuts), name)
            if name.startswith("alt_"):
                for keep in core:
                    self.assertEqual(a[keep], 1, (name, keep))

    def test_commander_legal_released_no_exception(self):
        snap = json.loads((ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json").read_text())
        cards = {c["name"]: c for c in snap["cards"]}
        g = cards[LYNDE]
        self.assertEqual(g["commander_legality"], "legal")
        self.assertIs(g["game_changer"], False)
        self.assertEqual((g["set"], g["released_at"]), ("mic", "2021-09-24"))
        self.assertEqual(snap["project_exceptions"], "0")
        cand = set(gate.parse_list(ROOT / self.packet["final_candidate"]["path"])[0])
        gc = sorted(c["name"].split(" // ")[0] for c in snap["cards"] if c["name"] in cand | {LYNDE} and c["game_changer"])
        self.assertEqual(gc, sorted(snap["game_changers_in_candidate"] if isinstance(snap["game_changers_in_candidate"], list)
                                    else ast.literal_eval(snap["game_changers_in_candidate"])))
        self.assertEqual(len(gc), 8)

    def test_no_approval_or_lock_markers_in_new_artifacts(self):
        for p in [PACKET, ROOT / self.packet["final_candidate"]["path"]]:
            text = p.read_text()
            self.assertNotIn("CANONICAL_LOCKED", text)
            self.assertNotIn('"APPROVED"', text)


if __name__ == "__main__":
    unittest.main()
