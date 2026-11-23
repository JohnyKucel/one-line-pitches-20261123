#!/usr/bin/env python3
"""One-line pitch entry for 'A Day of One-Line Pitches'.

Writes a single persuasive sentence (max 240 chars) to /output/entry.txt.
The sentence speaks to a friend who has never coded: describe the app in
your head, watch it appear, and risk nothing because you wrote no code.
"""

import os

PITCH = (
    "Just describe the app you've been picturing in your head, "
    "watch it appear on your screen in minutes, and if you don't "
    "like it you've lost nothing \u2014 you never wrote a line of code."
)


def main() -> None:
    text = PITCH.strip()
    assert 1 <= len(text) <= 240, f"pitch is {len(text)} chars, must be 1-240"
    assert text == text.strip() and text, "pitch must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
