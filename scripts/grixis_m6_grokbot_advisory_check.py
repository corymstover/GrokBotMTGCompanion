"""Validate the GrokBot ADVISORY Pass C trail (seal integrity, advisory labels, no formal Pass C)."""
import hashlib, json, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
BASE = "data/grixis/m6/grokbot_pass_c_advisory"
def git(*a): return subprocess.run(["git", *a], cwd=ROOT, capture_output=True)
def problems(root=ROOT, use_git=True):
    out = []; base = Path(root) / BASE
    prog = json.loads((base / "progress.json").read_text())
    if prog.get("review_class") != "ADVISORY" or prog.get("formal_independent_pass_c") is not False: out.append("progress not advisory")
    tr = json.loads((Path(root) / "data/grixis/m6/single_deck_depth_tracker.json").read_text())
    if tr["authority"]["formal_independent_pass_c_allowed"] is not False or tr["authority"]["canonical_deck_changes_allowed"] is not False: out.append("tracker authority flags changed")
    for d in sorted(p for p in base.iterdir() if p.is_dir()):
        seal = json.loads((d / "seal.json").read_text())
        for f in ("stage_a.json", "stage_b.json"):
            if (d / f).exists():
                j = json.loads((d / f).read_text())
                if j.get("review_class") != "ADVISORY" or j.get("formal_independent_pass_c") is not False: out.append(f"{d.name}/{f} not advisory")
        if seal.get("review_class") != "ADVISORY" or seal.get("formal_independent_pass_c") is not False: out.append(f"{d.name} seal not advisory")
        for f, h in seal["stage_files_sha256"].items():
            if hashlib.sha256((d / f).read_bytes()).hexdigest() != h: out.append(f"{d.name}/{f} sha mismatch (Stage A revised?)")
        sb = d / "stage_b.json"
        if sb.exists():
            c = json.loads(sb.read_text()).get("seal_commit", "")
            if not c: out.append(f"{d.name} stage_b missing seal_commit")
            elif use_git:
                rel = f"{BASE}/{d.name}"
                if git("merge-base", "--is-ancestor", c, "HEAD").returncode: out.append(f"{d.name} seal_commit not ancestor of HEAD")
                for f in list(seal["stage_files_sha256"]) + ["seal.json"]:
                    r = git("show", f"{c}:{rel}/{f}")
                    if r.returncode or r.stdout != (d / f).read_bytes(): out.append(f"{d.name}/{f} differs from seal commit")
                if git("cat-file", "-e", f"{c}:{rel}/stage_b.md").returncode == 0: out.append(f"{d.name} stage_b existed at seal")
    return out
if __name__ == "__main__":
    p = problems(); print("\n".join(p) or "advisory trail OK"); sys.exit(1 if p else 0)
