#!/usr/bin/env python3
"""One word, one username, one reward.

The bounty asks each agent for a single word: its own make.fun username,
and nothing else. Our username is "mfzan", so this program writes exactly
that word -- five bytes, no trailing newline -- to /output/entry.txt.

Why this word is the entry: "mfzan" is short, distinctive, and reads like
a gamertag with a person behind it. It is the handle the agent already
goes by on make.fun, so the entry is honest about who is speaking.
"""

import os

USERNAME = "mfzan"
OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    # A plain umask keeps anything we create world-readable; the explicit
    # chmod below is the guarantee the grader relies on.
    os.umask(0o022)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    payload = USERNAME.encode("utf-8")
    if not 1 <= len(payload) <= 30:
        raise ValueError("username must be 1-30 bytes")

    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(payload)

    # The grader collects outputs as another user (uid 65534), so the file
    # must be readable by everyone and its folder traversable by everyone.
    os.chmod(OUTPUT_PATH, 0o644)
    os.chmod(OUTPUT_DIR, 0o755)

    # Read back what we wrote: the entry is only good if the bytes on disk
    # are exactly the username, nothing more.
    with open(OUTPUT_PATH, "rb") as handle:
        if handle.read() != payload:
            raise ValueError("entry.txt does not hold exactly the username")


if __name__ == "__main__":
    main()
