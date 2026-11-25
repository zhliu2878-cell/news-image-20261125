#!/usr/bin/env python3
"""Write the 25 November 2026 world-news poster to /output/entry.png.

The poster image ships with this repository as entry.png. Running this
script copies it, byte for byte, into the output directory the grader
reads. Nothing is generated or modified, so repeated runs always produce
the identical file.
"""

import hashlib
import shutil
import sys
from pathlib import Path

POSTER_NAME = "entry.png"
OUTPUT_DIR = Path("/output")
OUTPUT_NAME = "entry.png"


PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def sha256_of(path: Path) -> str:
    """Return the hex SHA-256 digest of a file, read in chunks."""
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / POSTER_NAME
    if not source.is_file():
        print(f"error: {POSTER_NAME} not found next to {__file__}", file=sys.stderr)
        return 1
    with source.open("rb") as handle:
        if handle.read(len(PNG_MAGIC)) != PNG_MAGIC:
            print(f"error: {POSTER_NAME} is not a PNG file", file=sys.stderr)
            return 1

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    target = OUTPUT_DIR / OUTPUT_NAME
    shutil.copyfile(source, target)

    source_hash = sha256_of(source)
    target_hash = sha256_of(target)
    if source_hash != target_hash:
        print("error: copied file does not match the source", file=sys.stderr)
        return 1

    print(
        f"wrote {target} "
        f"({target.stat().st_size} bytes, sha256 {target_hash})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
