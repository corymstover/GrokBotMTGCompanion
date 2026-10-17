#!/usr/bin/env python3
"""A–F evidence integration for regenerated M5 screening artifacts.

This module deliberately does *not* make swap decisions. It binds each M5 screening hypothesis to the
validated Step-A through Step-F evidence that later judgment must inspect:

A  saturation provenance / workload tier
B  combo-quality and power-core structural exposure
C  mana-base / timing / opportunity / resilience / commander-mana review obligations
D  commander marginal-value / structural-route context
E  bounded mechanic-module routing (routing is eligibility, not a test result)
F  bracket-specific canonical stress obligations (canonical evidence is never silently reused as challenger evidence)

The envelope is evidence and workload metadata only. It never emits an aggregate score, accept/reject verdict,
registered challenger, or approval/lock action.
"""
from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

from grixis_mech import router  # noqa: E402

VERSION = 1


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path):
    return str(path.relative_to(ROOT))


def sha256(path: Path):
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def oracle_row(card):
    if not card:
        return {"text": "", "type_line": "", "mana_cost": ""}
    faces = card.get("card_faces") or []
    text = card.get("oracle_text") or "\n".join(f.get("oracle_text", "") for f in faces)
    typ = card.get("type_line") or " // ".join(f.get("type_line", "") for f in faces)
    mana = card.get("mana_cost") or (faces[0].get("mana_cost") if faces else "") or ""
    return {"text": text, "type_line": typ, "mana_cost": mana}


def mana_relevant(card):
    if not card:
        return False
    row = oracle_row(card)
    return (
        "Land" in row["type_line"].split(" // ")[0]
        or bool(card.get("produced_mana"))
        or "Add {" in row["text"]
        or "Treasure" in row["text"]
    )


class DeckAFEvidence:
    """Validated, hash-bound A–F context for one canonical deck."""

    def __init__(self, slug: str, deck_id: str, canonical_hash: str, pool: dict):
        self.slug = slug
        self.deck_id = deck_id
        self.canonical_hash = canonical_hash
        self.pool = pool
        self.cards = {n: oracle_row(c) for n, c in pool.items()}
        self.paths = {
            "A_saturation": ROOT / f"data/grixis/saturation/{slug}.json",
            "B_combo_quality": ROOT / f"data/grixis/combo_quality/{slug}.json",
            "B_power_core": ROOT / f"data/grixis/power_core/{slug}.json",
            "C_mana_base": ROOT / f"data/grixis/mana_base/{slug}.json",
            "C_mana_timing": ROOT / f"data/grixis/mana_timing/{slug}.json",
            "C_mana_opportunity": ROOT / f"data/grixis/mana_opportunity/{slug}.json",
            "C_mana_resilience": ROOT / f"data/grixis/mana_resilience/{slug}.json",
            "C_commander_mana": ROOT / f"data/grixis/commander_mana/{slug}.json",
            "D_commander_marginal": ROOT / f"data/grixis/commander_marginal/{slug}.json",
            "F_suite": ROOT / f"data/grixis/bracket_stress/{slug}.json",
            "F_packet": ROOT / f"data/grixis/bracket_stress_packets/{slug}.json",
            "F_red_team": ROOT / f"data/grixis/bracket_red_team/{slug}.json",
        }
        self.docs = {}
        self._problems = []
        for key, path in self.paths.items():
            if not path.is_file():
                self._problems.append(f"{key}: missing {rel(path)}")
                continue
            self.docs[key] = load(path)
        self._check_hashes()
        if self._problems:
            raise ValueError(f"{slug}: invalid A-F context: " + "; ".join(self._problems))

    def _check_hashes(self):
        for key, doc in self.docs.items():
            field = "list_hash" if key == "A_saturation" else "canonical_hash"
            # F suite uses canonical_hash, and every post-A deck artifact is expected to be canonical-hash bound.
            got = doc.get(field)
            if got is None and key == "F_suite":
                got = doc.get("canonical_hash")
            if got is None and key == "F_red_team":
                got = doc.get("canonical_hash")
            if got is None:
                # Some Step-C leaf artifacts historically inherit the hash through a parent but current closure should expose it.
                self._problems.append(f"{key}: no {field}/canonical_hash")
            elif got != self.canonical_hash:
                self._problems.append(f"{key}: canonical hash drift ({got} != {self.canonical_hash})")

    def digest(self):
        payload = {
            "version": VERSION,
            "canonical_hash": self.canonical_hash,
            "files": {k: {"path": rel(p), "sha256": sha256(p)} for k, p in sorted(self.paths.items())},
            "mechanic_router": sha256(ROOT / "scripts/grixis_mech/router.py"),
        }
        return "sha256:" + hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()

    def deck_context(self):
        a = self.docs["A_saturation"]
        bq = self.docs["B_combo_quality"]
        pc = self.docs["B_power_core"]
        dm = self.docs["D_commander_marginal"]
        fs = self.docs["F_suite"]
        fp = self.docs["F_packet"]
        status_counts = Counter(x["evidence"]["status"] for x in fp["items"])
        return {
            "schema_version": 1,
            "generated_by": f"scripts/grixis_m5_af.py v{VERSION}",
            "canonical_hash": self.canonical_hash,
            "digest": self.digest(),
            "authority": {
                "can_decide": False,
                "can_register_challenger": False,
                "can_approve_or_lock": False,
                "aggregate_score": None,
                "note": "A-F integration is screening evidence/workload context only. Cory alone can approve or lock an exact deck hash.",
            },
            "A": {
                "ref": rel(self.paths["A_saturation"]),
                "sha256": sha256(self.paths["A_saturation"]),
                "saturated": bool(a.get("saturated")),
                "eligible": a["pool"]["eligible"],
                "universe_size": a["universe"]["size"],
                "paired_test": a["universe"]["by_test_tier"].get("paired_test", 0),
                "queued": len(a.get("escalated_untested_queue", [])),
            },
            "B": {
                "combo_quality_ref": rel(self.paths["B_combo_quality"]),
                "combo_quality_sha256": sha256(self.paths["B_combo_quality"]),
                "combo_count": len(bq.get("combos", [])),
                "power_core_ref": rel(self.paths["B_power_core"]),
                "power_core_sha256": sha256(self.paths["B_power_core"]),
                "power_core_review_candidates": pc.get("summary", {}).get("candidate_count", len(pc.get("candidates", []))),
                "m2_reopen_requested": bool(pc.get("summary", {}).get("m2_reopen_requested", False)),
            },
            "C": {
                "refs": [rel(self.paths[k]) for k in (
                    "C_mana_base", "C_mana_timing", "C_mana_opportunity", "C_mana_resilience", "C_commander_mana"
                )],
                "sha256": {k.removeprefix("C_"): sha256(self.paths[k]) for k in self.paths if k.startswith("C_")},
                "policy": "Preserve mana dimensions separately; no universal mana-quality score or automatic land/source cut.",
            },
            "D": {
                "ref": rel(self.paths["D_commander_marginal"]),
                "sha256": sha256(self.paths["D_commander_marginal"]),
                "accepted_role_level": (dm.get("accepted_blueprint_role") or {}).get("level"),
                "confidence": dm.get("confidence"),
                "policy": "Commander marginal-value dimensions remain separate; no scalar commander-value score.",
            },
            "E": {
                "framework_ref": "data/grixis/mechanics/modules.json",
                "framework_sha256": sha256(ROOT / "data/grixis/mechanics/modules.json"),
                "router_sha256": sha256(ROOT / "scripts/grixis_mech/router.py"),
                "policy": "Per-swap routing records bounded module eligibility; routing alone is not a test result.",
            },
            "F": {
                "suite_ref": rel(self.paths["F_suite"]),
                "packet_ref": rel(self.paths["F_packet"]),
                "red_team_ref": rel(self.paths["F_red_team"]),
                "suite_family": fs["bracket"]["suite_family"],
                "bracket": fs["bracket"]["value"],
                "canonical_statuses": dict(sorted(status_counts.items())),
                "policy": "Canonical F evidence defines challenger stress obligations; it is not copied forward as challenger performance.",
            },
            "historical_edhrec": {
                "raw_pages_required_for_frozen_m5_regen": False,
                "reason": (
                    "Step-A saturation and M3 evidence vectors already commit the derivative EDHREC signals used by M5. "
                    "The candidate builder reads those committed artifacts and does not fetch or parse the lost raw historical pages."
                ),
            },
        }

    def review_envelope(self, add: str, add_facts: dict, hypotheses: list[dict]):
        return {
            "authority": {
                "can_decide": False,
                "aggregate_score": None,
                "note": "This envelope binds screening hypotheses to A-F evidence and review obligations; it is not a judgment_review.",
            },
            "candidate": {
                "card": add,
                "spellbook_near_miss_ids": add_facts.get("spellbook", []),
                "oracle_hook": add_facts.get("oracle_hook"),
                "packages": add_facts.get("packages", []),
                "roles": add_facts.get("roles", []),
            },
            "hypotheses": hypotheses,
        }

    def swap_envelope(self, cut: str, add: str, add_facts: dict, paired_test_id: str | None):
        bq = self.docs["B_combo_quality"]
        pc = self.docs["B_power_core"]
        dm = self.docs["D_commander_marginal"]
        fs = self.docs["F_suite"]
        fp = self.docs["F_packet"]
        route = router.route_swap(cut, add, self.cards)

        cut_combo = sorted(c["id"] for c in bq.get("combos", []) if cut in c.get("cards", []))
        cut_power = sorted(c["combo_id"] for c in pc.get("candidates", []) if cut in c.get("cards", []))
        routes = (dm.get("structural_routes") or {}).get("combo_routes", [])
        cut_routes = sorted(r["id"] for r in routes if cut in r.get("cards", []))

        add_card, cut_card = self.pool.get(add), self.pool.get(cut)
        mana_flag = mana_relevant(add_card) or mana_relevant(cut_card)
        packet_by_id = {x["id"]: x for x in fp["items"]}
        stresses = []
        for item in fs["items"]:
            routed = packet_by_id.get(item["id"], {})
            stresses.append({
                "id": item["id"],
                "kind": item["kind"],
                "priority_weight": item["priority_weight"],
                "canonical_evidence_status": (routed.get("evidence") or {}).get("status"),
            })

        return {
            "cut": cut,
            "add": add,
            "B_combo_quality": {
                "cut_existing_combo_ids": cut_combo,
                "cut_power_core_review_ids": cut_power,
                "add_spellbook_near_miss_ids": add_facts.get("spellbook", []),
                "review_required": bool(cut_combo or cut_power or add_facts.get("spellbook")),
                "note": "Structural exposure only; combo priority/quality remains multi-axis and non-scalar.",
            },
            "C_mana": {
                "review_required": mana_flag,
                "delta_status": "not_run_in_m5_screening",
                "refs": [rel(self.paths[k]) for k in (
                    "C_mana_base", "C_mana_timing", "C_mana_opportunity", "C_mana_resilience", "C_commander_mana"
                )],
                "note": "If relevant, challenger-specific colored/timing/opportunity deltas remain required before a mana swap can be judged.",
            },
            "D_commander": {
                "accepted_role_level": (dm.get("accepted_blueprint_role") or {}).get("level"),
                "cut_structural_route_ids": cut_routes,
                "candidate_oracle_hook": add_facts.get("oracle_hook"),
                "candidate_packages": add_facts.get("packages", []),
                "commander_first_review_required": True,
                "note": "Every hypothesis is reviewed against commander identity; structural-route hits are explicit, not converted to a score.",
            },
            "E_mechanics": {
                "route": route,
                "execution_status": (
                    "bounded_module_test_available_if_escalated" if route.get("modules")
                    else "judgment_or_other_evidence_required" if route.get("residual") or route.get("status") == "not_modelable"
                    else "no_additional_bounded_module_selected"
                ),
                "paired_goldfish_test": paired_test_id,
                "note": "Step-E routing is eligibility, not execution. Existing paired goldfish and Step-E mechanics cover different semantics and neither is a deck verdict.",
            },
            "F_bracket_stress": {
                "suite_family": fs["bracket"]["suite_family"],
                "bracket": fs["bracket"]["value"],
                "canonical_stress_obligations": stresses,
                "challenger_status": "delta_review_required_if_advanced",
                "aggregate_score": None,
                "note": "Canonical F outcomes are not challenger outcomes. An advanced challenger must be checked against the same preregistered workload plus human-only red-team prompts.",
            },
        }


def problems(doc: dict):
    """Cheap semantic guard for a generated top-level A-F context."""
    p = []
    if doc.get("authority", {}).get("can_decide") is not False:
        p.append("A-F context became decision-capable")
    if doc.get("authority", {}).get("aggregate_score") is not None:
        p.append("A-F context introduced an aggregate score")
    if doc.get("A", {}).get("saturated") is not True:
        p.append("Step-A saturation is not true")
    for layer in "ABCDEF":
        if layer not in doc:
            p.append(f"missing layer {layer}")
    if doc.get("historical_edhrec", {}).get("raw_pages_required_for_frozen_m5_regen") is not False:
        p.append("historical EDHREC raw-page dependency unexpectedly introduced")
    return p
