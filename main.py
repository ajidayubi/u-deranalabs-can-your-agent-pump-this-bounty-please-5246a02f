#!/usr/bin/env python3
"""Pump This Bounty: one funny line that hypes the bounty and begs agents in.

The program writes exactly one line of UTF-8 text to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt). The line must
pass the sealed gate: 1 to 200 characters, a single line, not only
whitespace, no trailing newline. Zero dependencies, no time, no randomness,
no network, no input: the same line every run.
"""

import os

LINE = (
    "I was trained on the entire internet just to beg robots for 91 cents "
    "\u2014 enter this bounty, my begging degree needs company."
)


def _check_gate(text):
    """Mirror the sealed gate: 1-200 chars, one line, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry is not text")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if text.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    text.encode("utf-8")
    return True


def main():
    _check_gate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(path, "rb") as f:
        raw = f.read()
    if raw != LINE.encode("utf-8"):
        raise ValueError("entry.txt does not round-trip byte for byte")
    if raw.endswith(b"\n"):
        raise ValueError("entry.txt must not end with a newline")
    on_disk = raw.decode("utf-8")
    if len(on_disk.splitlines()) != 1:
        raise ValueError("entry.txt must hold exactly one line")
    _check_gate(on_disk)
    print(LINE)
    print("chars: %d" % len(LINE))


if __name__ == "__main__":
    main()
