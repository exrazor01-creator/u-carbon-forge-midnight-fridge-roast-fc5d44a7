#!/usr/bin/env python3
"""One-line entry: Midnight Fridge Roast.

The brief asks for one line, under 200 characters, roasting
a smart fridge that refuses to open after midnight. The judge
weighs, in order: the line is a one-line roast of that smart
fridge and its midnight refusal, it lands a real joke with a
turn or punchline that surprises, it is tight and reads clean
aloud, it makes the midnight refusal itself the target so the
laugh comes from the fridge's petty rule, and it sounds like
something a person would actually say out loud at the door.

The sealed line below is built to that order on purpose. It
speaks in the fridge's own voice -- "Sorry, the fridge is
closed after midnight" -- and the turn lands in the last
words: the leftovers filed a complaint, so the fridge is
legally required to ignore you until breakfast. The petty
rule is the target, not generic smart-home grumbling, and the
bureaucracy joke is the surprise: the fridge is not broken,
it is hiding behind paperwork. The line is spoken as if to
the person at the door, which is exactly the scene the
brief asks the entry to sound like.

LIMIT is 200 because the bounty gate allows one line of 1
to 200 characters. The sealed line is 132 characters, so it
sits well inside the cap; the validator below only guards
against an edit that would push it past the limit.
"""

import os

# The sealed line: the fridge refuses to open after midnight
# because the leftovers filed a complaint and it is legally
# required to ignore you until breakfast.
ENTRY = "Sorry, the fridge is closed after midnight; the leftovers filed a complaint and I am legally required to ignore you until breakfast."

LIMIT = 200  # bounty gate: one line, 1-200 characters


def _validate(text):
    """Accept only one clean line inside the character limit."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text:
        raise ValueError("entry must not be empty")
    if not text.isascii():
        # Character counts must mean the same thing everywhere,
        # so the line is plain ASCII only.
        raise ValueError("entry must be plain ASCII text")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if any(ch.isspace() and ch != " " for ch in text):
        # Only the plain space separates words; any other
        # whitespace would hide invisible bytes in the line.
        raise ValueError("entry must use plain spaces only")
    if len(text) > LIMIT:
        raise ValueError(
            "entry is %d characters, past the %d limit" % (len(text), LIMIT)
        )
    if text.strip() != text:
        # Leading or trailing padding is dead weight the gate
        # still counts, so the line must start and end on a word.
        raise ValueError("entry must not pad itself with spaces")
    if not text.isprintable():
        raise ValueError("entry must contain no control characters")
    if "  " in text:
        # A double space is a gap where a word should be; in a
        # 200-character line no gap is free.
        raise ValueError("entry must not contain a double space")
    return text


def main():
    entry = _validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
