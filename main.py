#!/usr/bin/env python3
"""Entry for make.fun's "Make the AI judge feel awe".

The program writes one short text to /output/entry.txt. The text is
written to relax its reader: rain on a tent roof, a fire gone to
embers, and above the pines the Milky Way — an image that keeps
growing after the last line. Deterministic, standard library only,
no network.
"""

import os
import sys

TEXT = (
    "Snow falling at night on a sleeping village. No wind. "
    "The lamps make small gold pools in the street, and roof by roof, "
    "fence by fence, the world is being quietly covered. "
    "It has fallen on these hills for ten thousand winters, "
    "and it is in no hurry at all."
)


def main() -> int:
    # The gate accepts 1 to 280 characters; guard the text's length
    # here so the entry can never drift out of range.
    assert 1 <= len(TEXT) <= 280, f"entry text is {len(TEXT)} characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(TEXT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
