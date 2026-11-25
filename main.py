#!/usr/bin/env python3
"""One Line, No Deadline Met.

Writes one single-line joke giving an excuse for a missed deadline to
/output/entry.txt -- that line and nothing else, no picture, no link,
no second line. The joke is a single sentence that reads cleanly aloud
and lands its punch at the end.
"""

import os

# The entry: one line, one sentence, an excuse for a missed deadline.
# The turn: the deadline itself answers back in corporate speak.
LINE = (
    "I missed the deadline because I emailed it asking for an extension "
    "and it replied 'per my last email' \u2014 so here we are."
)

MAX_CHARS = 200


def main() -> None:
    line = LINE.strip()
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not line:
        raise ValueError("entry must not be empty")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the {MAX_CHARS} cap")

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)

    # Read it back: what lands on disk must be exactly the one line.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != line:
        raise ValueError("written entry does not match the line")
    print(line)


if __name__ == "__main__":
    main()
