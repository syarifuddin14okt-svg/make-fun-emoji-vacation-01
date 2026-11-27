#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — Mount Fuji.

Writes exactly one emoji to /output/entry.txt: Mount Fuji, the
postcard of a dream trip to Japan. One character, no words.
"""
import os

EMOJI = "\U0001F5FB"  # Mount Fuji


def verify_output():
    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    assert len(text) == 1 and text == EMOJI, "entry must be exactly one emoji"
    print(f"verified {len(raw)} bytes, byte-identical")


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EMOJI)
    print(f"wrote {len(EMOJI)} char to /output/entry.txt")
    verify_output()


if __name__ == "__main__":
    main()
