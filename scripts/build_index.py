#!/usr/bin/env python3
"""Validate every entry and regenerate index.json.

    python3 scripts/build_index.py          # validate + write index.json
    python3 scripts/build_index.py --check  # validate only; fail if index.json is out of date

Checks: required front-matter fields and allowed values (schema/entry.schema.json, without
needing a JSON-schema library), id == file name, sources exist in references.json, fixed
section headings present, and the "verified" rule: status verified needs verified_against,
verified_on, and every source with vancouver_reviewed = true.
"""
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SCHEMA = json.loads((ROOT / "schema" / "entry.schema.json").read_text())
REFS = {r["id"]: r for r in json.loads((ROOT / "references" / "references.json").read_text())}
SECTIONS = ["## 1. Scope", "## 2. Definitions", "## 3. Criteria", "## 4. Management", "## 5. Pitfalls",
            "## 6. What the source does not say", "## 7. Disagreements", "## 8. How to cite", "## 9. Change log"]


def front_matter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        raise ValueError("missing YAML front matter")
    return yaml.safe_load(m.group(1)), text[m.end():]


def check_field(name, value, spec, errs):
    if "enum" in spec and value not in spec["enum"]:
        errs.append(f"{name}: '{value}' not in {spec['enum']}")
    if spec.get("type") == "array":
        if not isinstance(value, list):
            errs.append(f"{name}: must be a list")
            return
        if len(value) < spec.get("minItems", 0):
            errs.append(f"{name}: needs at least {spec['minItems']} item(s)")
        item = spec.get("items", {})
        for v in value:
            if "enum" in item and v not in item["enum"]:
                errs.append(f"{name}: '{v}' not in {item['enum']}")
    if spec.get("type") == "string" and value is not None and not isinstance(value, str):
        errs.append(f"{name}: must be text (quote it in YAML)")
    if "pattern" in spec and isinstance(value, str) and not re.match(spec["pattern"], value):
        errs.append(f"{name}: '{value}' does not match {spec['pattern']}")


def validate(path):
    errs = []
    meta, body = front_matter(path.read_text(encoding="utf-8"))
    # YAML turns 2026-11-06 into a date object; keep everything as text
    meta = {k: (v.isoformat() if hasattr(v, "isoformat") else v) for k, v in meta.items()}
    for f in SCHEMA["required"]:
        if meta.get(f) in (None, "", []):
            errs.append(f"missing field: {f}")
    for f, v in meta.items():
        if f in SCHEMA["properties"]:
            check_field(f, v, SCHEMA["properties"][f], errs)
        else:
            errs.append(f"unknown field: {f}")
    if meta.get("id") != path.stem:
        errs.append(f"id '{meta.get('id')}' differs from file name '{path.stem}'")
    for s in meta.get("sources") or []:
        if s not in REFS:
            errs.append(f"source '{s}' not in references.json")
    for h in SECTIONS:
        if h not in body:
            errs.append(f"missing section: {h}")
    if meta.get("status") == "verified":
        if str(meta.get("verified_against", "pending")).startswith("pending"):
            errs.append("verified entry needs verified_against (what was read)")
        if not meta.get("verified_on"):
            errs.append("verified entry needs verified_on")
        for s in meta.get("sources") or []:
            if s in REFS and not REFS[s].get("vancouver_reviewed"):
                errs.append(f"verified entry cites unreviewed reference '{s}'")
    return meta, errs


def main():
    entries, failed = [], False
    for p in sorted((ROOT / "entries").rglob("*.md")):
        meta, errs = validate(p)
        if errs:
            failed = True
            print(f"✗ {p.relative_to(ROOT)}")
            for e in errs:
                print(f"    - {e}")
            continue
        if p.parent.name != meta["area"]:
            print(f"! {p.relative_to(ROOT)}: folder '{p.parent.name}' differs from area '{meta['area']}'")
        entries.append({
            "id": meta["id"], "title": meta["title"], "type": meta["type"], "area": meta["area"],
            "modalities": meta["modalities"], "population": meta["population"],
            "source_version": meta["source_version"], "status": meta["status"],
            "sources": meta["sources"], "superseded_by": meta.get("superseded_by", ""),
            "path": str(p.relative_to(ROOT)), "last_reviewed": str(meta["last_reviewed"]),
        })
    index = {"entries": entries,
             "counts": {"entries": len(entries),
                        "verified": sum(e["status"] == "verified" for e in entries),
                        "references": len(REFS),
                        "references_reviewed": sum(bool(r.get("vancouver_reviewed")) for r in REFS.values())}}
    new = json.dumps(index, ensure_ascii=False, indent=1) + "\n"
    out = ROOT / "index.json"
    if "--check" in sys.argv:
        if not out.exists() or out.read_text() != new:
            print("index.json is out of date: run scripts/build_index.py")
            failed = True
    else:
        out.write_text(new)
    print(f"{len(entries)} entries ({index['counts']['verified']} verified); "
          f"{len(REFS)} references ({index['counts']['references_reviewed']} reviewed)")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
