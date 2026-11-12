#!/usr/bin/env python3
"""Check that every citation key used in an entry body exists in references.json
and is listed in that entry's `sources:` front matter.

Citation format: [key] or [key, location] or [key1; key2, location].
Front matter (related:, sources:) is not scanned. Exit code 1 on any problem.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KEY = re.compile(r"[a-z][a-z0-9]*(-[a-z0-9]+)+")


def main() -> int:
    refs = {r["id"] for r in json.loads((ROOT / "references" / "references.json").read_text())}
    problems = []
    for path in sorted((ROOT / "entries").glob("*/*.md")):
        text = path.read_text(encoding="utf-8")
        _, front, body = text.split("---", 2)
        m = re.search(r"^sources:\s*\[(.*?)\]", front, re.M)
        sources = {s.strip() for s in m.group(1).split(",")} if m else set()
        for line_no, line in enumerate(body.splitlines(), front.count("\n") + 3):
            for group in re.findall(r"\[([^\[\]\n]+?)\]", line):
                for part in group.split(";"):
                    key = part.strip().split(",")[0].strip()
                    if not KEY.fullmatch(key):
                        continue
                    rel = path.relative_to(ROOT)
                    if key not in refs:
                        problems.append(f"{rel}:{line_no}: '{key}' is not in references.json")
                    elif key not in sources:
                        problems.append(f"{rel}:{line_no}: '{key}' is not in sources:")
    for p in problems:
        print(p)
    print(f"{len(problems)} citation problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
