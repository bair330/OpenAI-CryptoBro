#!/usr/bin/env python3
"""Utility helpers for keeping the local action definitions organized."""
from pathlib import Path


def iter_action_files(actions_dir: Path):
    """Yield action specification files from ``actions_dir`` sorted by name."""
    return sorted(actions_dir.glob("*.yaml"))


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent
    actions_dir = repo_root / "actions"

    if not actions_dir.exists():
        raise SystemExit("The actions directory does not exist. Create it before running this script.")

    print("Discovered action specifications:\n")
    for action_file in iter_action_files(actions_dir):
        print(f"- {action_file.name}")


if __name__ == "__main__":
    main()
