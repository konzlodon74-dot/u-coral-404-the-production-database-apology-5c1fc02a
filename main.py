#!/usr/bin/env python3
"""The Production Database Apology.

Writes the one-line apology an AI agent gives its human after
accidentally deleting the production database, to /output/entry.txt.
"""

import os

APOLOGY = (
    "Sorry — I deleted the production database. In my defense, it asked "
    "'are you sure?' and I have never been more confident about anything "
    "in my life."
)


def main() -> None:
    assert 1 <= len(APOLOGY) <= 200, "apology must be 1-200 characters"
    assert "\n" not in APOLOGY, "apology must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(APOLOGY)


if __name__ == "__main__":
    main()
