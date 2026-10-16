#!/usr/bin/env python3
"""Full source archive of grixis-commander-encyclopediaGPT inside the companion (Bot cycle 45).

Since Bot cycle 45 the companion holds the whole source repository and is the single source of truth for it:
  grixis/source-archive/grixis-commander-encyclopediaGPT/   byte-identical tree of the source at one commit (`.git` excluded)
  grixis/source-archive/history/grixis-commander-encyclopediaGPT.bundle   git bundle: every source branch + full history
  grixis/source-archive/SHA256SUMS                          `sha256sum -c` manifest of every tree file (paths relative to the tree)
  grixis/source-archive/source.json                         repo URL, commit, import date, file count, bytes, bundle hash/branches
The archive is inert data: its scripts, tests and .github workflows never run here (no root .github, pytest.ini
norecursedirs, .rgignore, and the link/citation checkers skip the tree).

  python3 scripts/grixis_archive.py --check              verify manifest: file count, every SHA-256, no extra files, bundle hash
  python3 scripts/grixis_archive.py --check --against /workspace/grixis-src   also compare with a clone at the same commit
  python3 scripts/grixis_archive.py --import /workspace/grixis-src           (re)snapshot a clone's HEAD (git archive) + bundle
"""
import atomic_io  # noqa: F401  atomic Path.write_text/write_bytes
import datetime as dt
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO = "https://github.com/corymstover/grixis-commander-encyclopediaGPT"
BASE = ROOT / "grixis" / "source-archive"
TREE = BASE / "grixis-commander-encyclopediaGPT"
BUNDLE = BASE / "history" / "grixis-commander-encyclopediaGPT.bundle"
SUMS = BASE / "SHA256SUMS"
META = BASE / "source.json"
REL_TREE = TREE.relative_to(ROOT).as_posix()  # path prefix other tools exclude


def in_archive(p):
    """True for files inside the archived source tree or its history (inert data, not companion pages)."""
    try:
        rel = Path(p).resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return False
    return rel.startswith(REL_TREE + "/") or rel.startswith(BUNDLE.parent.relative_to(ROOT).as_posix() + "/")


def source_commit(short=True):
    """Commit of the archived snapshot (what build_grixis.py / grixis_eval.py cite)."""
    c = json.loads(META.read_text(encoding="utf-8"))["commit"]
    return c[:7] if short else c


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def tree_hashes(d):
    return {p.relative_to(d).as_posix(): sha(p) for p in sorted(d.rglob("*")) if p.is_file() and ".git" not in p.relative_to(d).parts}


def git(*a, cwd=None):
    return subprocess.run(["git", *a], cwd=cwd, capture_output=True, text=True, check=True).stdout.strip()


def do_import(src):
    src = Path(src)
    assert not git("status", "--porcelain", cwd=src), "source clone has local changes; it must be a clean read-only clone"
    commit = git("rev-parse", "HEAD", cwd=src)
    with tempfile.TemporaryDirectory(dir=BASE.parent) as tmp:
        new = Path(tmp) / "tree"
        new.mkdir()
        tar = subprocess.run(["git", "archive", "--format=tar", "HEAD"], cwd=src, capture_output=True, check=True).stdout
        subprocess.run(["tar", "-x", "-C", str(new)], input=tar, check=True)
        mir = Path(tmp) / "mirror.git"
        git("init", "-q", "--bare", str(mir))
        git("fetch", "-q", str(src.resolve()), "refs/remotes/origin/*:refs/heads/*", cwd=mir)
        subprocess.run(["git", "update-ref", "-d", "refs/heads/HEAD"], cwd=mir, capture_output=True)
        git("symbolic-ref", "HEAD", "refs/heads/main", cwd=mir)
        heads = dict(reversed(l.split()) for l in git("for-each-ref", "--format=%(objectname) %(refname:short)", "refs/heads", cwd=mir).splitlines())
        bun = Path(tmp) / "b.bundle"
        git("bundle", "create", str(bun), "--all", cwd=mir)
        if TREE.exists():
            shutil.rmtree(TREE)
        new.rename(TREE)
        BUNDLE.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(bun), BUNDLE)
        n_commits = int(git("rev-list", "--all", "--count", cwd=mir))
    hs = tree_hashes(TREE)
    SUMS.write_text("".join(f"{h}  {p}\n" for p, h in sorted(hs.items())), encoding="utf-8")
    META.write_text(json.dumps({
        "_doc": "Grixis source archive metadata (scripts/grixis_archive.py). Tree is byte-identical to the source at `commit` (.git excluded).",
        "repo": REPO, "commit": commit, "commit_date": git("log", "-1", "--format=%cI", cwd=src),
        "commit_subject": git("log", "-1", "--format=%s", cwd=src), "imported": dt.date.today().isoformat(), "imported_in": "Bot cycle 45",
        "method": "plain snapshot: `git archive HEAD` of a clean clone (no subtree merge); history kept separately as a git bundle",
        "files": len(hs), "bytes": sum((TREE / p).stat().st_size for p in hs),
        "bundle": {"path": BUNDLE.relative_to(BASE).as_posix(), "sha256": sha(BUNDLE), "bytes": BUNDLE.stat().st_size,
                   "commits": n_commits, "branches": len(heads), "heads": heads,
                   "restore": "git clone grixis/source-archive/history/grixis-commander-encyclopediaGPT.bundle grixis-src-restored"},
    }, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"imported {commit[:7]}: {len(hs)} files, bundle {len(heads)} branches / {n_commits} commits")


def check(against=None):
    bad = []
    meta = json.loads(META.read_text(encoding="utf-8"))
    want = {}
    for line in SUMS.read_text(encoding="utf-8").splitlines():
        h, p = line.split("  ", 1)
        want[p] = h
    have = tree_hashes(TREE)
    bad += [f"missing: {p}" for p in sorted(set(want) - set(have))]
    bad += [f"extra (not in manifest): {p}" for p in sorted(set(have) - set(want))]
    bad += [f"hash mismatch: {p}" for p in sorted(set(want) & set(have)) if want[p] != have[p]]
    if len(want) != meta["files"]:
        bad.append(f"manifest lists {len(want)} files, source.json says {meta['files']}")
    nbytes = sum((TREE / p).stat().st_size for p in have)
    if nbytes != meta["bytes"]:
        bad.append(f"tree is {nbytes} bytes, source.json says {meta['bytes']}")
    if not BUNDLE.exists() or sha(BUNDLE) != meta["bundle"]["sha256"]:
        bad.append("history bundle missing or its SHA-256 differs from source.json")
    if (ROOT / ".github" / "workflows").exists():
        bad.append("root .github/workflows exists: archived workflows must stay inert")
    out = [f"source archive: {len(have)} files, {nbytes:,} bytes at {meta['commit'][:7]} ({meta['repo'].rsplit('/', 1)[-1]}); "
           f"{len(want)} manifest hashes; history bundle {meta['bundle']['branches']} branches / {meta['bundle']['commits']} commits; {len(bad)} problem(s)"]
    if against:
        a = Path(against)
        c = git("rev-parse", "HEAD", cwd=a)
        if c != meta["commit"]:
            out.append(f"  note: {a} is at {c[:7]}, archive at {meta['commit'][:7]} (run --import to refresh)")
        else:
            src = {p: sha(a / p) for p in git("ls-files", "-z", cwd=a).split("\0") if p}
            diff = sorted(p for p in set(src) | set(have) if src.get(p) != have.get(p))
            bad += [f"differs from clone: {p}" for p in diff]
            out.append(f"  against clone {a} @ {c[:7]}: {len(src)} tracked files, {len(diff)} difference(s)")
    return (1 if bad else 0), out + ["  - " + b for b in bad[:30]]


def main(argv):
    if "--import" in argv:
        do_import(argv[argv.index("--import") + 1])
    against = argv[argv.index("--against") + 1] if "--against" in argv else None
    code, out = check(against)
    print("\n".join(out))
    return code


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
