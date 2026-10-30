"""Batch 11 authoring aid: top proper names and opening text of cached pages (reading aid only)."""
import re, sys, collections
from pathlib import Path
T = Path(__file__).resolve().parents[4] / ".cache/story/text22"
STOP = set("The She He They His Her But And Art When That This There What Magic Story It In As If We You I My Then So For With Not No All One Its At On By Of To A An Or Now Their Was Is Our Yes Oh Who How Why Where Even Just Still Some More Like From After Before".split())
for s in sys.argv[2:]:
    t = re.sub(r"\s+", " ", (T / f"{s}.txt").read_text(encoding="utf-8"))
    c = collections.Counter(w for w in re.findall(r"\b[A-Z][a-z'’]{2,}(?: [A-Z][a-z]{2,})?", t) if w.split()[0] not in STOP)
    print(f"## {s} ({len(t.split())}w): " + ", ".join(f"{w}:{n}" for w, n in c.most_common(14)))
    print("   " + t[:int(sys.argv[1])])
