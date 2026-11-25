#!/usr/bin/env python3
"""One Star for Monday — make.fun entry.

Writes a single line: a one-star review of Monday, written as though
Monday were a restaurant. At most 25 words, one line, plain text.

The line: a diner orders the weekend, gets Monday instead, and the
bill turns out to be the whole week. Dish, bill, and a joke that
could only be about Monday.
"""

from pathlib import Path

REVIEW = (
    "One star. I ordered the weekend and got Monday instead \u2014 "
    "cold coffee, burnt toast, and the bill was my whole week."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = REVIEW.strip()
    # Gate guard: the sealed scorer requires UTF-8 text of 1-180 chars,
    # not only whitespace, and the brief caps the line at 25 words.
    words = text.split()
    assert 1 <= len(text) <= 180, f"entry is {len(text)} chars"
    assert len(words) <= 25, f"entry is {len(words)} words"
    assert "\n" not in text, "entry must be a single line"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
