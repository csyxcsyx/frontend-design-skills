#!/usr/bin/env python3
"""Verify the standalone package; Python standard library only."""
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent


def run(*args):
    subprocess.run([sys.executable, "-X", "utf8", *map(str, args)], check=True, cwd=ROOT)


def main():
    skills = ROOT / "skills"
    links = 0
    for name in ("ui-ux-pro-max", "design-taste-frontend"):
        folder = skills / name
        assert f"name: {name}\n" in (folder / "SKILL.md").read_text(encoding="utf-8")
        assert (folder / "LICENSE").is_file()
        json.loads((folder / "upstream-source.json").read_text(encoding="utf-8"))
        for path in folder.rglob("*.md"):
            for link in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
                if "://" not in link and not link.startswith("#"):
                    assert (path.parent / link.split("#")[0]).exists(), (path, link)
                    links += 1
    print(f"Verified skill structure and {links} local reference links.", flush=True)
    core = skills / "ui-ux-pro-max/scripts"
    run(core / "validate_data.py")
    result = subprocess.run([sys.executable, "-X", "utf8", str(core / "search.py"),
                             "error summary validation", "--domain", "ux", "-n", "1", "--json"],
                            text=True, encoding="utf-8", capture_output=True, check=True, cwd=ROOT)
    data = json.loads(result.stdout)
    assert data["count"] > 0 and data["domain"] == "ux", data
    print("Verified local search returns applicable UX results.", flush=True)
    run("-m", "unittest", "discover", "-s", core / "tests", "-p", "test_core.py")
    print("Standalone package checks passed.")


if __name__ == "__main__":
    main()
