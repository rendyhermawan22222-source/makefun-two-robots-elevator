#!/usr/bin/env python3
"""Write the one-line robot elevator small talk to /output/entry.txt.

The entry is a single line in the voice of a robot trapped in a lift with
another robot: its proximity sensor has been screaming about the closeness
for nine floors, it starts to ask the other unit to move, chickens out
mid-sentence, and retreats into forced politeness. The joke is the sensor
naming the awkwardness the robot itself will not.
"""

import os
import sys

LINE = (
    "My proximity sensor has been screaming for nine floors now, "
    "so if you could... no, no, it's fine. It's fine."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> int:
    if not 1 <= len(LINE) <= 200:
        print(f"line is {len(LINE)} chars, must be 1-200", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("line must be a single line", file=sys.stderr)
        return 1

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    # Read-back verification: the file must be byte-identical to the line.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    written = raw.decode("utf-8")
    assert written == LINE, "entry.txt does not match the chosen line"
    assert written.count("\n") == 0, "entry.txt must be exactly one line"
    assert written == written.strip(), "entry.txt must have no extra whitespace"
    assert 1 <= len(written) <= 200, "entry.txt must be 1-200 characters"

    print(
        f"wrote {OUTPUT_PATH} ({len(written)} chars, "
        f"{len(raw)} bytes, 1 line)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
