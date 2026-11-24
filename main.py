"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original roast line (<= 200 characters) to /output/entry.txt.
Standard library only.
"""

import os
from pathlib import Path

LINE = (
    "My phone dies at 4pm every day, like it clocks out on a union "
    "contract and leaves me doing its job unpaid."
)


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
    # not only white space. Fail loudly here rather than ship an invalid entry.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError(f"entry line is {len(LINE)} chars, must be 1-200")
    output_path = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
