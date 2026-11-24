#!/usr/bin/env python3
"""Two-Sentence Horror — make.fun entry (program/v1).

Writes one horror story of exactly two sentences to /output/entry.txt.
Standard library only: the grading sandbox is plain python:3.13-slim.
"""

import os

STORY = (
    "My grandmother left me her house on one condition: "
    "never open the cellar door. "
    "I opened it this morning and found a second will inside, "
    "in my own handwriting, dated tomorrow."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    # umask 022 so the file is world-readable (the grader collects
    # outputs as another user); chmod explicitly as well.
    os.umask(0o022)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
