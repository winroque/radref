#!/usr/bin/env python3
"""Re-check every reference in references/references.json against Crossref.

    python3 scripts/check_refs.py            # all references
    python3 scripts/check_refs.py bosniak-2019 fleischner-2017

Errors (exit 1): DOI does not resolve; first author differs; volume or first page differs;
the DOI inside the Vancouver string differs from the "doi" field.
Warnings: year differs (Crossref often has only the online year; see the reference's notes),
Vancouver string not reviewed yet.
Known Crossref data errors can be listed per reference in "crossref_exceptions":
e.g. ["pages"] or ["year"].
References without a DOI (e.g. ACR manuals and core documents) must have "doi": "" and a
"url" to the official page; they are skipped here with a warning and checked by hand.
"""
import json
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REFS = ROOT / "references" / "references.json"
UA = "radref/0.1 (reference checker)"


def norm(s):
    s = unicodedata.normalize("NFD", str(s or "")).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]", "", s)


def first_page(p):
    return re.split(r"[-–]", str(p or ""))[0].strip()


def crossref(doi):
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="/()")
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for attempt in range(4):
        try:
            return json.loads(urllib.request.urlopen(req, timeout=30).read())["message"]
        except urllib.error.HTTPError as e:
            if e.code != 429 or attempt == 3:   # 429 = Crossref rate limit: wait and retry
                raise
            time.sleep(5 * (attempt + 1))


def main():
    refs = json.loads(REFS.read_text())
    only = set(sys.argv[1:])
    errors = warnings = 0
    for r in refs:
        if only and r["id"] not in only:
            continue
        exc = set(r.get("crossref_exceptions") or [])
        msgs = []
        if not r.get("doi"):
            # Documents without a DOI (ACR manuals, core documents, society web pages):
            # nothing to check in Crossref; they need a stable URL and a human check.
            if not r.get("url"):
                print(f"✗ {r['id']}: no DOI and no url")
                errors += 1
            else:
                print(f"! {r['id']}: no DOI (document checked by hand against {r['url']})")
                warnings += 1
            continue
        try:
            m = crossref(r["doi"])
        except (urllib.error.URLError, ValueError, KeyError) as e:
            print(f"✗ {r['id']}: DOI {r['doi']} did not resolve ({e})")
            errors += 1
            continue
        fam = next((a.get("family", "") for a in m.get("author") or [] if a.get("family")), "")
        fam = re.sub(r"\d+(,\d+)*$", "", fam)
        if fam and norm(fam) != norm(r.get("first_author")):
            msgs.append(("E", f"first author: Crossref '{fam}' vs '{r.get('first_author')}'"))
        if m.get("volume") and r.get("volume") and norm(m["volume"]) != norm(r["volume"]) and "volume" not in exc:
            msgs.append(("E", f"volume: Crossref {m['volume']} vs {r['volume']}"))
        if m.get("page") and r.get("pages") and first_page(m["page"]) != first_page(r["pages"]) and "pages" not in exc:
            msgs.append(("E", f"first page: Crossref {m['page']} vs {r['pages']}"))
        yr = None
        for k in ("published-print", "issued", "published-online"):
            if m.get(k, {}).get("date-parts"):
                yr = m[k]["date-parts"][0][0]
                break
        if yr and r.get("year") and int(yr) != int(r["year"]) and "year" not in exc:
            msgs.append(("W", f"year: Crossref {yr} vs {r['year']} (see notes)"))
        doi_in_text = re.search(r"doi:(\S+?)\.?$", r.get("vancouver", ""))
        if not doi_in_text or doi_in_text.group(1).lower() != r["doi"].lower():
            msgs.append(("E", "DOI in the Vancouver string differs from the doi field"))
        if not r.get("vancouver_reviewed"):
            msgs.append(("W", "Vancouver string not reviewed against the first page yet"))
        es = [t for k, t in msgs if k == "E"]
        ws = [t for k, t in msgs if k == "W"]
        errors += bool(es)
        warnings += bool(ws)
        mark = "✗" if es else ("!" if ws else "✓")
        print(f"{mark} {r['id']}" + ("" if not msgs else ": " + "; ".join(es + ws)))
        time.sleep(0.2)   # be polite to the Crossref API
    print(f"\n{errors} reference(s) with errors, {warnings} with warnings")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
