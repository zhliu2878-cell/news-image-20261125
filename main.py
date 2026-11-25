#!/usr/bin/env python3
"""Write the 25 November 2026 world-news summary image to /output/entry.png.

The image is bundled with this repository as entry.png; this program copies
it byte-for-byte to /output/entry.png, so every run writes identical bytes.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"


def main():
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
