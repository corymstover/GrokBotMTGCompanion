#!/usr/bin/env python3
"""Run the unit-test suite in tests/ (Bot cycle 47, M0).

Uses pytest when it is installed; otherwise a small stdlib runner imports every tests/test_*.py, calls each
test_* function, and treats unittest.SkipTest as a skip. The tests use plain asserts and no fixtures, so both
runners see the same suite. Exit 0 only when no test fails. Called by validate_all step "unit-tests".
"""
import importlib.util
import subprocess
import sys
import traceback
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TESTS = ROOT / "tests"


def fallback():
    sys.path.insert(0, str(TESTS))
    ok = fail = skipped = 0
    for f in sorted(TESTS.glob("test_*.py")):
        spec = importlib.util.spec_from_file_location(f.stem, f)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        for name in sorted(n for n in dir(mod) if n.startswith("test_") and callable(getattr(mod, n))):
            try:
                getattr(mod, name)()
                ok += 1
            except unittest.SkipTest as e:
                skipped += 1
                print(f"  SKIP {f.name}::{name}: {e}")
            except Exception:  # noqa: BLE001
                fail += 1
                print(f"  FAIL {f.name}::{name}\n" + "".join("    " + l for l in traceback.format_exc().splitlines(True)[-6:]))
    print(f"unit tests (stdlib runner): {ok} passed, {fail} failed, {skipped} skipped")
    return 1 if fail else 0


def main():
    try:
        import pytest  # noqa: F401
    except ImportError:
        return fallback()
    r = subprocess.run([sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", str(TESTS)], cwd=ROOT, capture_output=True, text=True)
    tail = [l for l in r.stdout.strip().splitlines() if l.strip()]
    print("unit tests (pytest): " + (tail[-1] if tail else "no output"))
    if r.returncode:
        print(r.stdout[-4000:] + r.stderr[-2000:])
    return r.returncode


if __name__ == "__main__":
    sys.exit(main())
