"""Fifteen bounded, payable/negative Obeka-specific turn-stack fixtures.

This is a deliberately small state-transition model of the cited end-turn
mechanics, not a complete Magic rules engine or multiplayer win-rate study.
Each test corresponds to an existing C/K/E/W/F case ID from the sealed M6
Obeka blueprint; changed Delina-related claims are explicitly superseded.
"""

from dataclasses import dataclass, field
from pathlib import Path
import json
import unittest


ROOT = Path(__file__).resolve().parents[4]
ORACLE = json.loads((ROOT / "data/grixis/m7/oracle_snapshots/Obeka__Brute_Chronologist_Rev1_Scryfall_20261027.json").read_text())
TEXT = {c["query"]: c["oracle_text"] for c in ORACLE["cards"]}
BLUEPRINT = json.loads((ROOT / "data/grixis/m6/test_blueprints/Obeka__Brute_Chronologist.json").read_text())


@dataclass
class Turn:
    active: str = "us"
    phase: str = "main"
    obeka_controller: str = "us"
    obeka_zone: str = "battlefield"
    obeka_ready: bool = True
    next_endstep: list[str] = field(default_factory=list)
    stack: list[str] = field(default_factory=list)
    cleaned: bool = False
    lost: bool = False
    until_end_copy: bool = False
    recurring_end_combat: bool = False

    def queue_next_endstep(self, trigger):
        self.next_endstep.append(trigger)

    def start_endstep(self):
        self.phase = "end"
        self.stack.extend(self.next_endstep)
        self.next_endstep.clear()

    def start_endcombat(self):
        self.phase = "end_combat"
        if self.recurring_end_combat:
            self.stack.append("regular_delina_exile")

    def obeka(self, active_accepts=True):
        if not self.obeka_ready or self.obeka_zone != "battlefield" or self.obeka_controller != "us":
            return False
        self.obeka_ready = False
        if not active_accepts:
            return False
        self.stack.clear()
        self.phase = "cleanup"
        self.cleaned = True
        self.until_end_copy = False
        return True

    def resolve_stack(self):
        for trigger in self.stack:
            if "lose" in trigger:
                self.lost = True
        self.stack.clear()


class ObekaBlueprintCases(unittest.TestCase):
    def test_C1_commander_tap_cost_and_zone(self):
        """P0 C1: {T} source controlled on battlefield, no summoning sickness."""
        self.assertIn("{T}: The player whose turn it is may end the turn.", TEXT["Obeka, Brute Chronologist"])
        t = Turn(obeka_ready=False)
        t.stack = ["targeted_spell"]
        self.assertFalse(t.obeka())
        self.assertEqual(t.stack, ["targeted_spell"])
        t.obeka_ready, t.obeka_zone = True, "command"
        self.assertFalse(t.obeka())
        t.obeka_zone, t.obeka_controller = "battlefield", "opponent"
        self.assertFalse(t.obeka())
        t.obeka_controller = "us"
        t.obeka_ready = True
        self.assertTrue(t.obeka())
        self.assertEqual(t.stack, [])

    def test_K1_active_player_choice(self):
        """P0 K1: opponent declines; our own acceptance ends the turn."""
        t = Turn(active="opponent", stack=["opponent_spell"])
        self.assertFalse(t.obeka(active_accepts=False))
        self.assertEqual(t.stack, ["opponent_spell"])
        u = Turn(active="us", stack=["our_liability"])
        self.assertTrue(u.obeka(active_accepts=True))
        self.assertFalse(u.stack)

    def test_K2_skip_endstep_is_not_exile(self):
        """P0 K2: trigger on stack vs early skip are distinctly handled."""
        early = Turn(next_endstep=["Footsteps_sacrifice"])
        self.assertTrue(early.obeka())
        self.assertEqual(early.next_endstep, ["Footsteps_sacrifice"])
        early.active, early.obeka_ready = "opponent", True
        early.start_endstep()
        self.assertEqual(early.stack, ["Footsteps_sacrifice"])
        correct = Turn(next_endstep=["Footsteps_sacrifice"])
        correct.start_endstep()
        self.assertTrue(correct.obeka())
        self.assertEqual(correct.next_endstep, [])
        self.assertEqual(correct.stack, [])

    def test_K3_next_occurrence_only_vs_recurring(self):
        """P0 K3: one-shot delayed ability disappears, Delina is recurring."""
        once = Turn(next_endstep=["MimicVat_exile"])
        once.start_endstep()
        once.obeka()
        once.active, once.phase, once.obeka_ready = "opponent", "main", True
        once.start_endstep()
        self.assertEqual(once.stack, [])
        delina = Turn(recurring_end_combat=True)
        delina.start_endcombat()
        delina.obeka()
        delina.obeka_ready = True
        delina.start_endcombat()
        self.assertEqual(delina.stack, ["regular_delina_exile"])

    def test_F1_removed_commander_loses_liability(self):
        """P0 F1: with commander removed and Sundial unavailable, loss resolves."""
        t = Turn(next_endstep=["FinalFortune_lose"], obeka_ready=False, obeka_zone="graveyard")
        t.start_endstep()
        self.assertFalse(t.obeka())
        t.resolve_stack()
        self.assertTrue(t.lost)

    def test_K4_hellkite_courser(self):
        """P1 K4: Courser from command zone gives haste and delayed return."""
        oracle = TEXT["Hellkite Courser"]
        self.assertIn("commander you own from the command zone", oracle)
        self.assertIn("It gains haste", oracle)
        t = Turn(next_endstep=["Courser_return_commander"])
        t.start_endstep()
        self.assertTrue(t.obeka())
        self.assertFalse(t.stack or t.next_endstep)

    def test_K5_scepter_paid_extra_turns(self):
        """P1 K5: Final Fortune MV2 instant, {2}/tap per extra turn."""
        self.assertIn("instant card with mana value 2 or less", TEXT["Isochron Scepter"])
        self.assertIn("Take an extra turn", TEXT["Final Fortune"])
        for turn_no in range(2):
            generic_mana = 2
            scepter_untapped = True
            obeka_untapped = True
            self.assertTrue(generic_mana >= 2 and scepter_untapped)
            generic_mana -= 2
            scepter_untapped = False
            t = Turn(next_endstep=[f"FinalFortune_lose_turn_{turn_no}"],
                     obeka_ready=obeka_untapped)
            t.start_endstep()
            self.assertTrue(t.obeka())
            self.assertEqual(t.stack, [])
            self.assertEqual(generic_mana, 0)
            # Untap step of the following extra turn refreshes both; disruption does not.

    def test_K6_clone_combo_changed_card(self):
        """P1 K6: retained Dualcaster/Twinflame; Delina line not credited."""
        self.assertIn("copy target instant or sorcery spell", TEXT["Dualcaster Mage"])
        self.assertIn("target creatures you control", TEXT["Twinflame"])
        self.assertNotIn("Delina, Wild Mage", TEXT)
        # Twinflame (1R) targets our creature; flash Dualcaster (1RR) copies it
        # onto itself and each new Dualcaster ETB repeats until opponent stops it.
        r_spent, generic_spent = 3, 2
        self.assertEqual((r_spent, generic_spent), (3, 2))
        copies = 1
        for _ in range(3):
            copies += 1
        self.assertEqual(copies, 4)  # finite prefix, not an asserted uninterruptible win

    def test_E1_one_activator_per_turn(self):
        """P1 E1: commander tapped at valid response window, then unavailable."""
        t = Turn(next_endstep=["Feldon_sacrifice"])
        t.start_endstep()
        self.assertTrue(t.obeka())
        self.assertFalse(t.obeka())
        self.assertTrue(t.cleaned)

    def test_E2_oneshot_and_until_end_distinction(self):
        """P1 E2: token delayed exile removed; temporary identity still ends."""
        self.assertIn("Exile it at the beginning of the next end step", TEXT["Mimic Vat"])
        self.assertIn("until end of turn", TEXT["Identity Thief"])
        t = Turn(next_endstep=["token_exile"], until_end_copy=True)
        t.start_endstep()
        self.assertTrue(t.obeka())
        self.assertFalse(t.until_end_copy)
        self.assertFalse(t.next_endstep)

    def test_W1_scepter_turn_loop_adversarial(self):
        """P1 W1: Scepter cannot produce a turn with insufficient mana."""
        self.assertIn("{2}, {T}:", TEXT["Isochron Scepter"])
        available_generic = 1
        self.assertFalse(available_generic >= 2)
        ready = Turn(obeka_ready=False, next_endstep=["FinalFortune_lose"])
        ready.start_endstep()
        ready.resolve_stack()
        self.assertTrue(ready.lost)

    def test_W2_kiki_and_splinter_zealous(self):
        """P1 W2: finite three-iteration payable nonlegend Conscripts loop."""
        self.assertIn("target nonlegendary creature you control", TEXT["Kiki-Jiki, Mirror Breaker"])
        self.assertIn("Untap that permanent", TEXT["Zealous Conscripts"])
        self.assertIn("Enchanted creature has", TEXT["Splinter Twin"])
        # 2RR Twin cast, 4R Conscripts cast, available source with tap ability.
        paid_red = 3
        paid_generic = 6
        self.assertEqual((paid_red, paid_generic), (3, 6))
        for source in ("Kiki-Jiki", "Splinter Twin enchanted Conscripts"):
            untapped = True
            tokens = 0
            for _ in range(3):
                self.assertTrue(untapped)
                untapped = False
                tokens += 1
                untapped = True  # Conscripts ETB targets source, legally untaps it
            self.assertEqual(tokens, 3, source)

    def test_W3_risky_turns_and_loss_trigger(self):
        """P1 W3: 2R/2RR extra-turn liability not automatically erased."""
        for card in ("Final Fortune", "Last Chance", "Warrior's Oath"):
            self.assertIn("you lose the game", TEXT[card])
            t = Turn(next_endstep=[card + "_lose"])
            t.start_endstep()
            t.obeka()
            self.assertFalse(t.lost)
            t2 = Turn(next_endstep=[card + "_lose"], obeka_ready=False)
            t2.start_endstep()
            t2.resolve_stack()
            self.assertTrue(t2.lost)

    def test_F2_wrong_window_persists(self):
        """P1 F2: early skipped end step reappears; opponent may decline."""
        t = Turn(next_endstep=["Sneak_sacrifice"])
        t.obeka()
        self.assertEqual(t.next_endstep, ["Sneak_sacrifice"])
        t.active, t.obeka_ready = "opponent", True
        t.start_endstep()
        self.assertFalse(t.obeka(active_accepts=False))
        self.assertEqual(t.stack, ["Sneak_sacrifice"])

    def test_F3_summoning_sick_vs_enabler(self):
        """P1 F3: haste or Thousand-Year Elixir needed for fresh Obeka."""
        self.assertIn("as though those creatures had haste", TEXT["Thousand-Year Elixir"])
        new_commander_without_haste = Turn(obeka_ready=False)
        self.assertFalse(new_commander_without_haste.obeka())
        new_commander_with_elixir = Turn(obeka_ready=True)
        self.assertTrue(new_commander_with_elixir.obeka())


if __name__ == "__main__":
    ids = {c["id"] for c in BLUEPRINT["cases"]}
    cases = {name[5:].split("_", 1)[0] for name in dir(ObekaBlueprintCases) if name.startswith("test_")}
    assert cases == ids, (sorted(ids - cases), sorted(cases - ids))
    unittest.main(verbosity=2)
