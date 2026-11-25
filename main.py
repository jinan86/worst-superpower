"""Worst Superpower — a make.fun entry.

The program writes one line to /output/entry.txt: the most useless
superpower imaginable, stated in a single breath together with the
reason it is useless.

The power: breathing underwater — but only in puddles. A hero who can
hold a dramatic pose in a rain puddle, and nowhere else.
"""

import os

# The entry, exactly as submitted. 48 characters, one line, no newline.
ENTRY = "I can breathe underwater, but only in puddles."

# The competition gate: 1 to 140 characters of UTF-8 text, not only
# whitespace, written to this path with no trailing newline.
OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 140


def validate(text: str) -> None:
    """Check the entry against the gate before writing anything."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(ENTRY)
    # Create the output directory if the sandbox has not made it yet.
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Write exactly the entry bytes: no trailing newline, UTF-8.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
