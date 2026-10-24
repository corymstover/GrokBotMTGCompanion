"""Deck 26 Kess, Dissident Mage M7 research candidate: structural checks only, not approval.

The packet is RESEARCH_ONLY_WITHDRAWN_NOT_OWNER_PRESENTABLE: one genuine swap (+Mana Drain -Personal Tutor), below the
five-swap floor. Personal Tutor is an owner addition from the 2026-10-14 rebuild, so the override is flagged and the
owner-respecting fallback (+Mana Drain -Deadly Rollick) is staged. Pass C's Jeska's Will and Frantic Search lines and
Grim Tutor are staged owner-decision alternatives and are not counted. Nothing is padded."""
from __future__ import annotations
import hashlib
import json
import unittest
from collections import Counter
from pathlib import Path

from scripts import grixis_m7_decision_gate as gate

ROOT = Path(__file__).resolve().parents[1]
D = "Kess__Dissident_Mage"
K = "Kess, Dissident Mage"
PACKET = ROOT / f"data/grixis/m7/decision_reviews/{D}.json"
BASE = ROOT / f"data/grixis/m7/baseline_sources/{D}_approved_source_2026-10-14.txt"
RAW = "93d27d605bbdf0737ebe32c911fafe3a002b06d7d90f00b7bfc402cb1d3faccb"
CAND_RAW = "d8fc71c1ee48948509de155b3b93571c2d9d0e5f426fb5b5679478dadf7ae57b"
LH = "lh1:d89d5778424e5aa61244cd1aea7aa6967ad678860c59cafbb62e14abbe6dfa9b"
CAND_LH = "lh1:066fc59a46090816ed94931d072fec96fd2d511d4590097d930f9be7ce4810b0"
RC = ROOT / "data/grixis/m7/research_challengers"


class KessDissidentMageM7Tests(unittest.TestCase):
    def setUp(self):
        self.packet = json.loads(PACKET.read_text())
        self.registry = json.loads((ROOT / "data/grixis/registry.json").read_text())
        self.judged = {c["card"]: c for c in self.packet["material_candidates"]}

    def cand(self):
        return Counter(gate.parse_list(ROOT / self.packet["final_candidate"]["path"])[0])

    def test_gate_passes_as_withdrawn_research_only_not_approval(self):
        result = gate.verify_packet(self.packet, root=ROOT, registry=self.registry)
        self.assertFalse(result["owner_presentable"])
        self.assertEqual(result["new_swaps"], 1)
        self.assertEqual(result["status"], "M7_WITHDRAWN_RESEARCH_ONLY_NOT_OWNER_PRESENTABLE")
        self.assertEqual(self.packet["readiness"], "RESEARCH_ONLY_WITHDRAWN_NOT_OWNER_PRESENTABLE")
        reason = self.packet["withdrawal_reason"]
        self.assertIn("one genuine swap (+Mana Drain -Personal Tutor)", reason)
        self.assertIn("not met without padding", reason)
        self.assertIn("NOT owner approved", reason)
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

    def test_exactly_one_swap_against_vendored_and_canonical_source(self):
        cand = self.cand()
        path, md = gate.canonical_source(ROOT, self.registry["decks"][D])
        for base in (Counter(gate.parse_list(BASE)[0]), Counter(gate.parse_list(path, source_markdown=md)[0])):
            self.assertEqual(sorted((cand - base).elements()), ["Mana Drain"])
            self.assertEqual(sorted((base - cand).elements()), ["Personal Tutor"])
        self.assertEqual(self.packet["final_changes"]["adds"], ["Mana Drain"])
        self.assertEqual(self.packet["final_changes"]["cuts"], ["Personal Tutor"])

    def test_single_commander_first_and_100_physical_singleton_no_basics(self):
        lines = [x for x in (ROOT / self.packet["final_candidate"]["path"]).read_text().splitlines() if x.strip()]
        self.assertEqual(lines[0], f"1x {K} [Commander]")
        self.assertEqual(sum(1 for x in lines if x.endswith("[Commander]")), 1)
        self.assertFalse(any("[Companion]" in x for x in lines))
        self.assertEqual(sum(int(x.split("x ", 1)[0]) for x in lines), 100)
        self.assertEqual([x for x in lines if not x.startswith("1x ")], [])
        for basic in ("Island", "Swamp", "Mountain"):
            self.assertNotIn(f"1x {basic}", lines)
        rest = [x.split("x ", 1)[1] for x in lines[1:]]
        self.assertEqual(rest, sorted(rest, key=str.lower))
        self.assertEqual(len(set(rest)), 99)

    def test_distinctness_note_and_commander_first_identity_recorded(self):
        note = self.packet["commander_identity"]["anti_homogenization"]
        self.assertIn("Commander-first to Kess's Oracle", note)
        for s in ("Kefka, Court Mage 80/80", "Jeleva, Nephalia's Scourge 77/78", "Inalla, Archmage Ritualist 71/71",
                  "Evelyn, the Covetous 71/71", "Mana Drain is in none of the four"):
            self.assertIn(s, note)
        self.assertIn("Owner-removed or rejected cards and classes", note)
        plan = self.packet["commander_identity"]["mechanical_plan"]
        self.assertIn("once during each of your turns, you may cast an instant or sorcery spell from your graveyard", plan)
        self.assertIn("Displacer Kitten blinks Kess for a new permission", plan)

    def test_owner_direction_removed_not_readded_core_kept_and_alternatives_staged(self):
        cand = self.cand()
        for card in ("Consider", "Jeska's Will", "Flame of Anor", "Past in Flames", "Yawgmoth's Will",
                     "Mizzix's Mastery", "Thousand-Year Storm", "Professor Onyx", "Talrand, Sky Summoner",
                     "Guttersnipe", "Young Pyromancer", "Hoarding Broodlord", "The One Ring", "Opposition Agent",
                     "Dauthi Voidwalker", "Frantic Search", "Chaos Warp", "Sensei's Divining Top", "Cursed Totem",
                     "Manamorphose", "Silence", "Personal Tutor"):
            self.assertNotIn(card, cand)
        for keep in self.packet["commander_identity"]["protected_core"]:
            if keep != K:
                self.assertEqual(cand[keep], 1, keep)
        md = self.judged["Mana Drain"]
        self.assertEqual(md["judgment"], "SELECT_ADD")
        self.assertEqual(md["confidence"], "MODERATE")
        self.assertEqual(md["named_cuts"], ["Personal Tutor", "Deadly Rollick"])
        for c in ("Grim Tutor", "Jeska's Will", "Frantic Search"):
            self.assertEqual(self.judged[c]["judgment"], "RETAIN_ALTERNATIVE", c)
        for rej in ("Spell Pierce", "Praetor's Grasp", "Cyclonic Rift", "Notion Thief", "Undercity Sewers",
                    "Mnemonic Betrayal", "Lim-Dûl's Vault", "Snap", "Muddle the Mixture", "Dispel",
                    "Narset, Parter of Veils", "Urza's Saga", "Timetwister", "Hexing Squelcher", "Lightning Bolt",
                    "Exotic Orchard", "The One Ring", "Opposition Agent", "Dauthi Voidwalker"):
            self.assertEqual(self.judged[rej]["judgment"], "REJECT", rej)
        for inv in ("Manamorphose", "Silence"):
            self.assertEqual(self.judged[inv]["judgment"], "EXCLUDE_INVALID", inv)
        self.assertEqual(len(self.judged), 25)
        self.assertEqual([c for c, v in self.judged.items() if v["judgment"] == "SELECT_ADD"], ["Mana Drain"])
        audit = self.packet["low_swap_heightened_audit"]
        weak = {x["card"] for x in audit["weakest_slot_challenge"]}
        self.assertEqual(len(weak), 15)
        for card in ("Personal Tutor", "Deadly Rollick", "Demonic Counsel", "Ledger Shredder", "Displacer Kitten",
                     "City of Traitors", "Ponder", "Into the Flood Maw", "Fellwar Stone", "Windfall"):
            self.assertIn(card, weak)
        pk = sorted((sorted(p["adds"]), sorted(p["cuts"])) for p in audit["multi_slot_packages"])
        self.assertEqual(pk, [(["Frantic Search", "Jeska's Will"], ["Ledger Shredder", "Personal Tutor"]),
                              (["Mana Drain", "Spell Pierce"], ["Fellwar Stone", "Personal Tutor"])])

    def test_power_bracket_tags_game_changers(self):
        v = self.packet["verification"]
        self.assertEqual(v["power_bracket"], 5)
        self.assertEqual(v["archidekt_tags"], ["cEDH", "Spellslinger", "Graveyard"])
        self.assertIn("Game Changers: 21 in both baseline and candidate", self.packet["commander_identity"]["natural_ceiling"])

    def test_alternatives_staged_as_complete_hundreds(self):
        def load(name):
            return Counter(gate.parse_list(RC / f"{D}_{name}_20261023.txt")[0])
        cases = {
            "one_ManaDrain_over_DeadlyRollick": (["Mana Drain"], ["Deadly Rollick"]),
            "one_SpellPierce_over_PersonalTutor": (["Spell Pierce"], ["Personal Tutor"]),
            "two_ManaDrain_SpellPierce_over_PersonalTutor_FellwarStone":
                (["Mana Drain", "Spell Pierce"], ["Fellwar Stone", "Personal Tutor"]),
            "one_GrimTutor_over_PersonalTutor": (["Grim Tutor"], ["Personal Tutor"]),
            "one_GrimTutor_over_DemonicCounsel": (["Grim Tutor"], ["Demonic Counsel"]),
            "one_PraetorsGrasp_over_Ponder": (["Praetor's Grasp"], ["Ponder"]),
            "one_CyclonicRift_over_IntoTheFloodMaw": (["Cyclonic Rift"], ["Into the Flood Maw"]),
            "one_NotionThief_over_LedgerShredder": (["Notion Thief"], ["Ledger Shredder"]),
            "one_UndercitySewers_over_CityOfTraitors": (["Undercity Sewers"], ["City of Traitors"]),
            "PassC_plus_JeskasWill_minus_LedgerShredder": (["Jeska's Will"], ["Ledger Shredder"]),
            "PassC_plus_FranticSearch_minus_PersonalTutor": (["Frantic Search"], ["Personal Tutor"]),
        }
        base = Counter(gate.parse_list(BASE)[0])
        for name, (adds, cuts) in cases.items():
            a = load(name)
            self.assertEqual(sum(a.values()), 100, name)
            self.assertEqual(sorted((a - base).elements()), sorted(adds), name)
            self.assertEqual(sorted((base - a).elements()), sorted(cuts), name)

    def test_commander_legal_released_no_exception(self):
        snap = json.loads((ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json").read_text())
        g = [c for c in snap["cards"] if c["name"] == K][0]
        self.assertEqual(g["commander_legality"], "legal")
        self.assertIs(g["game_changer"], False)
        self.assertEqual((g["set"], g["released_at"]), ("ncc", "2022-04-29"))
        self.assertEqual(snap["project_exceptions"], "0")
        cand = set(gate.parse_list(ROOT / self.packet["final_candidate"]["path"])[0])
        gc = sorted(c["name"] for c in snap["cards"] if c["name"] in cand | {K} and c["game_changer"])
        self.assertEqual(len(gc), 21)
        for n in gc:
            self.assertIn(n, snap["game_changers_in_candidate"])

    def test_no_approval_or_lock_markers_in_new_artifacts(self):
        for p in [PACKET, ROOT / self.packet["final_candidate"]["path"]]:
            text = p.read_text()
            self.assertNotIn("CANONICAL_LOCKED", text)
            self.assertNotIn('"APPROVED"', text)


if __name__ == "__main__":
    unittest.main()
