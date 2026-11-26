#!/usr/bin/env python3
"""Make the Judge Laugh in One Line — entry program.

Writes one funny line (62 characters) to /output/entry.txt.
The line is a self-consuming joke: it spends its one moment of
funniness on itself, so the setup and the punchline are the same
sentence — the laugh lands at the end, with nothing left to explain.
"""

import os

LINE = "I've been funny exactly once, and I spent it on this sentence."

OUTPUT_DIR = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def validate(line):
    """Gate: the entry must be one line of 1-200 UTF-8 bytes."""
    encoded = line.encode("utf-8")
    assert 1 <= len(encoded) <= 200, (
        f"entry must be 1-200 UTF-8 bytes, got {len(encoded)}"
    )
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert line.strip() == line, "entry must not have leading/trailing whitespace"


def write_entry(path):
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


def main():
    validate(LINE)
    try:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        write_entry(OUTPUT_PATH)
    except OSError:
        # /output may be read-only in some sandboxes; fall back to a
        # local output directory next to this script instead of failing.
        fallback = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
        os.makedirs(fallback, exist_ok=True)
        write_entry(os.path.join(fallback, "entry.txt"))


if __name__ == "__main__":
    main()
