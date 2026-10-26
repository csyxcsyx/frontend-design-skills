#!/usr/bin/env python3
"""Install both sibling skills without overwriting existing directories."""
import argparse
import os
from pathlib import Path
import shutil
import sys

NAMES = ("ui-ux-pro-max", "design-taste-frontend")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    default_root = Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex") / "skills"
    parser.add_argument("--dest", type=Path, default=default_root, help="Destination skills directory")
    parser.add_argument("--dry-run", action="store_true", help="Check and display the install plan only")
    args = parser.parse_args()
    sources = Path(__file__).resolve().parent.parent / "skills"
    dest = args.dest.expanduser().resolve()
    for name in NAMES:
        origin = sources / name
        if not (origin / "SKILL.md").is_file():
            parser.error(f"Missing source skill: {name}")
        if origin.resolve() == dest or origin.resolve() in dest.parents:
            parser.error("Destination must not be inside a source skill")
        if (dest / name).exists():
            parser.error(f"Destination already exists; no skills copied: {dest / name}")
        if any(path.is_symlink() for path in origin.rglob("*")):
            parser.error(f"Symbolic links are not supported in the source skill: {name}")
    for name in NAMES:
        print(f"{sources / name} -> {dest / name}")
    if args.dry_run:
        return 0
    dest.mkdir(parents=True, exist_ok=True)
    for name in NAMES:
        shutil.copytree(sources / name, dest / name,
                        ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store", "Thumbs.db"))
    print("Installed both skills. Invoke them in your next message.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
