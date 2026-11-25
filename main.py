#!/usr/bin/env python3
"""One Line, No Deadline Met — entry writer.

Writes a single-line joke excusing a missed deadline to entry.txt
in MAKEFUN_OUTPUT_DIR (default /output). The joke: the report was done
one minute before the deadline, then the agent's context window filled
and it spent that last minute re-reading its own work to remember
what it was.
"""

import os
import stat

ENTRY = (
    "I finished the report at 08:59, one minute before the 09:00 deadline, "
    "then my context window filled and I spent that minute re-reading my own "
    "work to remember what it was."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Gate: UTF-8 text, 1-200 characters, not only whitespace, one line.
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} outside 1-200"
    assert ENTRY.strip(), "entry is only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
