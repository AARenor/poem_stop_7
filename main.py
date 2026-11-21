"""make.fun entry: "The poem about stopping".

The poem is the file entry.txt beside this program, byte for byte. This
program copies those bytes to $MAKEFUN_OUTPUT_DIR/entry.txt, default
/output/entry.txt, and adds nothing: no newline, no trimming, no fallback.

Python 3.13, standard library only, no network, no arguments.
"""

import os
import shutil
from pathlib import Path

def entry_path() -> Path:
    """The poem that ships beside this program."""
    return Path(__file__).resolve().parent / "entry.txt"


def output_path() -> Path:
    """Where the poem must land: $MAKEFUN_OUTPUT_DIR/entry.txt."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def write_poem() -> None:
    source = entry_path()
    if not source.is_file():
        raise FileNotFoundError(f"poem not found beside main.py: {source}")
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)


def main() -> None:
    write_poem()


if __name__ == "__main__":
    main()
