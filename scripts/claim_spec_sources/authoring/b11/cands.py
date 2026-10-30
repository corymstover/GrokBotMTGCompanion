"""Batch 11 authoring aid: print candidate relation sentences from cached official page text (reading aid only)."""
import re, sys
from pathlib import Path
T = Path(__file__).resolve().parents[4] / ".cache/story/text22"
KW = re.compile(r"\b(sister|brother|daughter|son|father|mother|wife|husband|mentor\w*|apprentice|student|teacher|leader|leads|led|guildmaster|captain|chief|khan|queen|king|lord|founded|created|built|forged|killed|slew|murdered|destroyed|imprison\w*|trapped|bound|betray\w*|serv\w+|member|joined|allied|ally|enemy|rival|friend|rescued|freed|captured|kidnap\w*|summoned|sent|hired|ordered|worship\w*|patron|god|goddess|planeswalker|spark|plane of|born|home)\b", re.I)
def sents(t):
    t = re.sub(r"\s+", " ", t)
    return re.split(r"(?<=[.!?\"”])\s+(?=[A-Z“\"])", t)
def main(slugs, n=6):
    for s in slugs:
        t = (T / f"{s}.txt").read_text(encoding="utf-8")
        out = []
        for x in sents(t):
            caps = set(re.findall(r"(?<!^)(?<![.!?] )\b[A-Z][a-z]{2,}", x)) - {"The", "She", "He", "They", "His", "Her", "But", "And", "Art", "When", "That", "This", "There", "What", "Magic", "Story"}
            k = len(KW.findall(x))
            if k and len(caps) >= 2 and 30 < len(x) < 260:
                out.append((k + len(caps) / 2, x))
        out.sort(key=lambda z: -z[0])
        print(f"## {s}")
        for _, x in out[:n]:
            print("  -", x)
if __name__ == "__main__":
    a = sys.argv[1:]; n = 6
    if a and a[0].isdigit(): n = int(a[0]); a = a[1:]
    main(a, n)
