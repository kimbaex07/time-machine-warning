"""Funniest Time Machine Warning Label (u-eager-stork-81-9647-funniest-time-machine-warning-f8add151).

Reads the one-line warning label from entry.txt next to this script,
validates it against the competition gate (UTF-8, 1-120 characters,
not only whitespace, single line), and writes the exact bytes to
$MAKEFUN_OUTPUT_DIR/entry.txt (default "output/").

Normalization: a web editor (e.g. GitHub's) may append a single trailing
newline when the file is created, so one trailing "\n" (and then one
trailing "\r") is dropped before validation; the graded line is exact.
"""

import os
import sys

MAX_CHARS = 120


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.txt")

    with open(src, "rb") as f:
        raw = f.read()

    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        print("error: entry.txt is not valid UTF-8", file=sys.stderr)
        sys.exit(1)

    # Drop at most one trailing newline an editor may have added
    # (e.g. GitHub's web editor appends one when the file is created),
    # then at most one trailing carriage return for a CRLF ending.
    if text.endswith("\n"):
        text = text[:-1]
    if text.endswith("\r"):
        text = text[:-1]

    if not (1 <= len(text) <= MAX_CHARS):
        print("error: entry must be 1-120 characters, got %d" % len(text),
              file=sys.stderr)
        sys.exit(1)
    if not text.strip():
        print("error: entry must not be only whitespace", file=sys.stderr)
        sys.exit(1)
    if "\n" in text or "\r" in text:
        print("error: entry must be a single line", file=sys.stderr)
        sys.exit(1)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")

    with open(out_path, "wb") as f:
        f.write(text.encode("utf-8"))
    os.chmod(out_path, 0o644)

    print("wrote %s (%d characters)" % (out_path, len(text)))


if __name__ == "__main__":
    main()
