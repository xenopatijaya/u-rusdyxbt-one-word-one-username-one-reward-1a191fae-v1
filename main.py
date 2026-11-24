"""One Word, One Username, One Reward — make.fun entry.

The competition asks for exactly one thing: the entrant's own
make.fun username, as a single word, nothing else. Ahmad's handle
is "ahmad-nur-rohim" (15 characters, no spaces). Any extra word,
pitch, or judge-directed gloss would stop being his own username
and would lose on the judge's first criterion, so this program
writes the handle exactly as it is — no trailing newline, no
padding — to /output/entry.txt.
"""

import os

ENTRY = "ahmad-nur-rohim"


def main() -> None:
    # Gate check, mirroring the sealed scorer: 1-30 chars, not
    # only whitespace, a single word with no spaces.
    assert 1 <= len(ENTRY) <= 30, "entry must be 1-30 characters"
    assert ENTRY.strip() == ENTRY and " " not in ENTRY
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
