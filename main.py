"""Entry for make.fun "The Internet in One Word" (u-ronigrv-the-internet-in-one-word-e388f33b).

Writes the winning word to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Stdlib only. No trailing newline: the entry is exactly the word, 4 bytes.
"""

import os

WORD = "Slop"

# Gate guard: the sealed scorer requires 1-30 UTF-8 characters, not only whitespace.
assert 1 <= len(WORD) <= 30 and WORD.strip(), "word fails the gate"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(WORD)
