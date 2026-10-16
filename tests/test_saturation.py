"""Bot cycle 65.1 (step A): adaptive saturation, no numeric cap, stopping rule, screening never excludes, certificate schema."""
import gzip
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import grixis_saturation as gs  # noqa: E402

SRC = (gs.ROOT / "scripts" / "grixis_saturation.py").read_text()


def test_no_universe_cap_constant():
    code = SRC.split('"""', 2)[2]  # skip the module docstring, which names the old bound
    assert not re.search(r"UNIVERSE_(MIN|MAX)|\[:\s*(200|500)\]|NICHE_RESERVE", code)


def test_certificates_valid_and_saturated():
    assert gs.problems(rerun=False) == []
    certs = list(gs.OUT.glob("*.json"))
    assert len(certs) >= 3
    for f in certs:
        c = json.loads(f.read_text())
        assert c["saturated"] and c["authority"]["can_decide"] is False
        r = c["stopping_rule"]
        assert (r["material_k"], r["material_score"], r["stop_after_non_material"]) == (gs.MATERIAL_K, gs.MATERIAL_SCORE, gs.STOP_N)
        assert c["passes"][-1]["pass"] == "full_pool_sweep"
        tail = [p for p in c["passes"] if p["kind"] != "sweep"][-r["stop_after_non_material"]:]
        assert all(p["kind"] == "expansion" and not p["material"] for p in tail)
        assert c["pool"]["sweep_coverage"] == 1.0 and c["universe"]["size"] == c["pool"]["eligible"]
        assert c["blind_spots"][0]["kind"] == "unreleased_not_yet_legal"


def test_screening_never_excludes():
    for f in gs.OUT.glob("*.json"):
        c = json.loads(f.read_text())
        assert set(c["hard_exclusions"]) <= set(c["hard_exclusion_kinds"])
        u = gs.load_universe(gs.ROOT / c["universe"]["file"])
        assert len(u) == c["universe"]["size"]
        assert any(x["tier"] == "C" for x in u)  # low-scoring cards stay in the universe
        assert {x["test_tier"] for x in u} <= {"paired_test", "escalated_queued", "screen_only"}
        assert all(x["test_tier"] != "screen_only" for x in u if x["tier"] == "A" or x["escalation"])
        q = [x["card"] for x in u if x["test_tier"] == "escalated_queued"]
        assert sorted(q) == sorted(x["card"] for x in c["escalated_untested_queue"])  # overflow is queued, never dropped
        assert sum(x["test_tier"] == "paired_test" for x in u) <= c["universe"]["paired_test_target"]


def test_full_pool_sweep_covers_every_eligible_card():
    import grixis_candidates as gc
    import grixis_authority as ga
    R0, reg, pool, first, almost = gc._ctx()
    slug = "the-valeyard"
    c = json.loads((gs.OUT / f"{slug}.json").read_text())
    did, v = next((k, v) for k, v in ga.summary().items() if v["slug"] == slug)
    D = gc.DeckCtx(did, v, R0, reg, pool, first, almost)
    want = {n for n, x in pool.items() if (x.get("legalities") or {}).get("commander") == "legal"
            and set(x.get("color_identity", [])) <= D.ci and n not in D.names and "Basic Land" not in gc.tline(x)}
    u = {x["card"] for x in gs.load_universe(gs.ROOT / c["universe"]["file"])}
    assert want <= u


def test_materiality_rule():
    assert not gs.is_material(gs.MATERIAL_K - 1, 0)
    assert gs.is_material(gs.MATERIAL_K, 0)
    assert gs.is_material(0, 1)
