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
        tail = c["passes"][-r["stop_after_non_material"]:]
        assert all(p["kind"] == "expansion" and not p["material"] for p in tail)


def test_screening_never_excludes():
    for f in gs.OUT.glob("*.json"):
        c = json.loads(f.read_text())
        assert set(c["hard_exclusions"]) <= set(c["hard_exclusion_kinds"])
        u = json.loads(gzip.decompress((gs.ROOT / c["universe"]["file"]).read_bytes()))
        assert len(u) == c["universe"]["size"]
        assert any(x["tier"] == "C" for x in u)  # low-scoring cards stay in the universe
        assert {x["test_tier"] for x in u} <= {"paired_test", "screen_only"}
        assert all(x["test_tier"] == "paired_test" for x in u if x["tier"] == "A" or x["escalation"])


def test_materiality_rule():
    assert not gs.is_material(gs.MATERIAL_K - 1, 0)
    assert gs.is_material(gs.MATERIAL_K, 0)
    assert gs.is_material(0, 1)
