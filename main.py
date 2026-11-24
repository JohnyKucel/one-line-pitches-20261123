#!/usr/bin/env python3
"""One-line pitch entry for 'A Day of One-Line Pitches'.

Writes a single persuasive sentence (max 240 chars) to /output/entry.txt.
The sentence speaks to a friend who has never coded: describe the app in
your head, watch it appear, and risk nothing because you wrote no code.
"""

import os

PITCH = (
    "Just describe the app you've been picturing in your head "
    "to an AI on make.fun, watch it appear on your screen in "
    "minutes, and if you don't love it you've lost nothing "
    "\u2014 you never wrote a line of code."
)


def main() -> None:
    text = " ".join(PITCH.split())
    assert 1 <= len(text) <= 240, f"pitch is {len(text)} chars, must be 1-240"
    assert "\n" not in text and "\r" not in text, "pitch must be a single line"
    assert text == text.strip() and text, "pitch must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
