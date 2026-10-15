"""Atomic file writes for the KB generators (Bot cycle 34).

A generator killed mid-write (cycle 34's first run) used to leave truncated or half-regenerated
tracked files.  Importing this module makes `pathlib.Path.write_text` / `write_bytes` atomic for
the whole process: data goes to a temp file in the same directory, is flushed and fsynced, then
`os.replace`d over the target, so a target is always either the old or the new complete file.
`atomic_open(path, mode="w", ...)` is the same for code that streams (csv.writer, json.dump).
"""
import contextlib
import os
import pathlib
import tempfile

_orig_write_text = pathlib.Path.write_text
_orig_write_bytes = pathlib.Path.write_bytes


@contextlib.contextmanager
def atomic_open(path, mode="w", **kw):
    path = pathlib.Path(path)
    fd, tmp = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=str(path.parent))
    try:
        with os.fdopen(fd, mode, **kw) as fh:
            yield fh
            fh.flush()
            os.fsync(fh.fileno())
        if path.exists():
            os.chmod(tmp, path.stat().st_mode & 0o777)
        else:
            os.chmod(tmp, 0o644)
        os.replace(tmp, path)
    except BaseException:
        with contextlib.suppress(FileNotFoundError):
            os.unlink(tmp)
        raise


def _write_text(self, data, encoding=None, errors=None, newline=None):
    if not isinstance(data, str):
        raise TypeError(f"data must be str, not {type(data).__name__}")
    with atomic_open(self, "w", encoding=encoding or "utf-8", errors=errors, newline=newline) as fh:
        return fh.write(data)


def _write_bytes(self, data):
    with atomic_open(self, "wb") as fh:
        return fh.write(memoryview(data))


def install():
    pathlib.Path.write_text = _write_text
    pathlib.Path.write_bytes = _write_bytes


install()
