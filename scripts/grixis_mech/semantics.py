"""Shared Oracle-text helpers for step-E parsers (Bot cycle 66.4 semantic audit)."""
import re

N_PLAYERS = 4  # bounded D4 assumption: a 4-player Commander table ("each upkeep" = 4 per round of turns)
REMINDER = re.compile(r"\([^)]*\)")
QUOTED = re.compile(r"\u201c[^\u201d]*\u201d|\"[^\"]*\"")


def _replace_name(t, name):
    """Replace a printed card-name phrase only when it is not embedded inside a larger word."""
    if not name:
        return t
    return re.sub(rf"(?<![\w]){re.escape(name)}(?![\w])", "~", t)


def clean(name, text):
    """~ for the card's own name; reminder text and quoted abilities granted to other objects removed.

    Name replacement is phrase-bounded. A raw str.replace() can corrupt unrelated Oracle words when a short synthetic
    or real card name is a substring (for example name='C' would turn 'Counter' into '~ounter').
    """
    t = _replace_name(text, name)
    for short in {name.split(",")[0], name.split(" // ")[0]}:
        if len(short) > 3:
            t = _replace_name(t, short)
    t = QUOTED.sub('"granted ability"', t)
    t = REMINDER.sub("", t)
    return re.sub(r"\bthis (?:creature|artifact|enchantment|permanent|land|card|spell|token|vehicle|equipment)\b", "~", t, flags=re.I)


def sentences(t):
    return [s.strip() for s in re.split(r"(?<=[.])\s+|\n", t) if s.strip()]


def intervening_if(sent):
    return bool(re.match(r"^(?:at the beginning of [^,]*|whenever [^,]*|when [^,]*), if ", sent, re.I))
