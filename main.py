#!/usr/bin/env python3
"""Two-sentence horror entry for make.fun.

Produces exactly one two-sentence horror story and writes it to
/output/entry.txt. Standard library only: the grading sandbox is plain
python:3.13-slim, so no third-party packages are available or used.
"""

import os
from pathlib import Path

SENTENCE_ONE = (
    "My grandmother left me her house on one condition: "
    "never open the cellar door."
)
SENTENCE_TWO = (
    "I opened it this morning and found a second will inside, "
    "in my own handwriting, dated tomorrow."
)

ENTRY_PATH = Path("/output/entry.txt")


def assemble_story() -> str:
    """Glue the two sentences together with a single space."""
    return " ".join([SENTENCE_ONE, SENTENCE_TWO])


def save_entry() -> None:
    """Write the story to /output/entry.txt, world-readable.

    The grader collects outputs as another user, so the file must be
    readable by everyone: set a permissive umask before creating it
    and chmod it explicitly afterwards.
    """
    ENTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    os.umask(0o022)
    ENTRY_PATH.write_text(assemble_story(), encoding="utf-8")
    os.chmod(ENTRY_PATH, 0o644)


if __name__ == "__main__":
    save_entry()
