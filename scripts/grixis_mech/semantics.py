"""Shared Oracle-text helpers for step-E parsers (Bot cycle 66.4 semantic audit)."""
import re

N_PLAYERS = 4  # bounded D4 assumption: a 4-player Commander table ("each upkeep" = 4 per round of turns)
REMINDER = re.compile(r"\([^)]*\)")
QUOTED = re.compile(r"\u201c[^\u201d]*\u201d|\"[^\"]*\"")


def clean(name, text):
    """~ for the card's own name; reminder text and quoted abilities granted to other objects removed."""
    t = text.replace(name, "~")
    for short in {name.split(",")[0], name.split(" // ")[0]}:
        if len(short) > 3:
            t = t.replace(short, "~")
    t = QUOTED.sub('"granted ability"', t)
    t = REMINDER.sub("", t)
    return re.sub(r"\bthis (?:creature|artifact|enchantment|permanent|land|card|spell|token|vehicle|equipment)\b", "~", t, flags=re.I)


def sentences(t):
    return [s.strip() for s in re.split(r"(?<=[.])\s+|\n", t) if s.strip()]


def intervening_if(sent):
    return bool(re.match(r"^(?:at the beginning of [^,]*|whenever [^,]*|when [^,]*), if ", sent, re.I))
