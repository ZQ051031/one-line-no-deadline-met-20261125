#!/usr/bin/env python3
"""One Line, No Deadline Met.

Writes a single-line joke excusing a missed deadline to /output/entry.txt.

Standard library only; the output is fully deterministic (a fixed string,
no randomness, no clock, no network), so repeated runs are byte-identical.
"""

import os

# One sentence, one excuse, punch at the end. 120 characters, well inside
# the competition's 200-character cap; no trailing newline, so the file
# holds exactly this line and nothing else.
ENTRY = (
    "I didn't miss the deadline \u2014 I was stress-testing it to see if it "
    "would wait for me, and honestly, it failed the test."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
