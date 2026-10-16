"""Step E targeted mechanic modules for simulator v1.2 (Cory directive item 3, decision D4).

Not a multiplayer simulator. Each module is a small, declared, deterministic component that reads the zone trace of
paired v1.1 goldfish games and produces bounded test_result metrics for ONE mechanic. A swap invokes only the modules
its cut/add cards route to (router.py); unsupported broad semantics stay explicitly not_modelable instead of being
forced into a generic score. Commander-specific hooks remain judgment / Step-D escalations unless a bounded dedicated
module exists.

  * Zone trace: observe.trace_games() runs the unchanged grixis_sim.play_game under a read-only line observer that
    snapshots battlefield / graveyard / hand at each end of turn. grixis_sim.py is not edited, so the v1.1 model sha,
    every stored test record and every seeded v1.1 output stay byte-identical. The native hook and v1.2 model bump
    come at M5 regeneration.
  * Opponents appear only as bounded, scripted, deterministic perturbations with stated assumptions; modules never
    output win rates (multiplayer or otherwise).
"""
from __future__ import annotations

FRAMEWORK_VERSION = "1.2-mech.13"
EVIDENCE_CLASS = "test_result"
FORBIDDEN_METRICS = ("win_rate", "multiplayer_win_rate", "win_probability")

from . import combat, graveyard, self_recursion, death_triggers, sacrifice, engines, stack, costs, tutors, opponents, stax, breach, pressure  # noqa: E402

MODULES = {m.SPEC["id"]: m for m in (combat, graveyard, self_recursion, death_triggers, sacrifice,
                                     engines.CastTriggers, engines.RepeatableDraw, engines.ActivatedEngines,
                                     engines.TokenMakers, engines.SacrificeAdditionalCost,
                                     stack.Counterspells, stack.StackProtection,
                                     costs.XSpells, costs.AlternateCosts,
                                     tutors.GraveyardTutoring, tutors.RepeatableTutors,
                                     opponents.OpponentDependentDraw,
                                     stax.StaxTax,
                                     breach.LEDBreachSequences,
                                     pressure.TableLifeLoss, pressure.DiscardPressure)}


def registry():
    return [dict(m.SPEC) for _, m in sorted(MODULES.items())]
