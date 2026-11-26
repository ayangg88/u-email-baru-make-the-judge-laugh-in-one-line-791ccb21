#!/usr/bin/env python3
"""Make the Judge Laugh in One Line — entry program.

Writes one funny line (62 characters) to /output/entry.txt.
The line is a self-consuming joke: it spends its one moment of
funniness on itself, so the setup and the punchline are the same
sentence — the laugh lands at the end, with nothing left to explain.
"""

import os

LINE = "I've been funny exactly once, and I spent it on this sentence."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
