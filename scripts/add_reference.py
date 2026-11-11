#!/usr/bin/env python3
"""Add (or refresh) a reference in references/references.json from Crossref metadata.

    python3 scripts/add_reference.py <ref-id> <doi>
    python3 scripts/add_reference.py --from-cache cache.json   # bulk, {ref-id: crossref message}

The Vancouver string is a DRAFT built automatically (authors, sentence-case title by
heuristic, journal abbreviation from Crossref). It is saved with "vancouver_reviewed": false.
A human must check it against the article's first page (title capitalization, proper nouns,
journal abbreviation, print year) and then set "vancouver_reviewed": true.
Only references with vancouver_reviewed = true may be printed in a report.
"""
import datetime as dt
import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REFS = ROOT / "references" / "references.json"
UA = "radref/0.1 (reference checker)"

# Words kept capitalized by the sentence-case heuristic (proper nouns, eponyms, acronyms
# written in title case). Extend as needed.
PROTECT = {
    "Alzheimer's", "Alzheimer", "Bosniak", "Fleischner", "Society", "Radiologists", "Ultrasound",
    "American", "College", "Radiology", "Radiology's", "Brazil", "Portugal", "Portuguese",
    "Brazilian", "Committee", "Lancet", "INTERGROWTH-21st", "World", "Health", "Organization", "Fetal", "Medicine", "Foundation", "ISUOG", "Delphi", "O-RADS", "MRI", "Data", "System", "Magnetic", "Resonance", "Imaging", "Ovarian-Adnexal", "Reporting", "Red-Cell", "Doppler",
}

# NLM abbreviations for journals Crossref often returns in full.
JOURNAL_ABBR = {
    "Journal of the American College of Radiology": "J Am Coll Radiol",
    "American Journal of Roentgenology": "AJR Am J Roentgenol",
    "The Lancet": "Lancet",
    "European Urology": "Eur Urol",
    "European Journal of Cancer": "Eur J Cancer",
    "European Journal of Endocrinology": "Eur J Endocrinol",
    "Journal of Cardiovascular Computed Tomography": "J Cardiovasc Comput Tomogr",
    "The Spine Journal": "Spine J",
    "Journal of Neurosurgery": "J Neurosurg",
    "Arquivos Brasileiros de Cardiologia": "Arq Bras Cardiol",
    "American Journal of Respiratory and Critical Care Medicine": "Am J Respir Crit Care Med",
    "Journal of Neurology, Neurosurgery & Psychiatry": "J Neurol Neurosurg Psychiatry",
    "PLoS ONE": "PLoS One",
    "PLOS Medicine": "PLoS Med",
    "Ultrasound in Obstetrics & Gynecology": "Ultrasound Obstet Gynecol",
    "Ultrasound in Obstetrics &amp; Gynecology": "Ultrasound Obstet Gynecol",
    "BJOG: An International Journal of Obstetrics & Gynaecology": "Br J Obstet Gynaecol",
    "BJOG: An International Journal of Obstetrics &amp; Gynaecology": "Br J Obstet Gynaecol",
    "American Journal of Obstetrics and Gynecology": "Am J Obstet Gynecol",
    "New England Journal of Medicine": "N Engl J Med",
    "Obstetrics & Gynecology": "Obstet Gynecol",
    "Obstetrics &amp; Gynecology": "Obstet Gynecol",
    "JAMA Network Open": "JAMA Netw Open",
    "Stroke": "Stroke",
}


def _initials(given):
    parts = re.split(r"[\s.]+", given or "")
    out = ""
    for p in parts:
        if not p:
            continue
        out += "".join(x[0].upper() for x in p.split("-") if x)
    return out


def _authors(msg):
    auth = msg.get("author") or []
    names = []
    for a in auth:
        if a.get("family"):
            fam = re.sub(r"\d+(,\d+)*$", "", a["family"]).strip()   # Crossref sometimes glues affiliation numbers
            names.append(f"{fam} {_initials(a.get('given', ''))}".strip())
        elif a.get("name"):
            names.append(a["name"])
    if len(names) > 6:
        return ", ".join(names[:6]) + ", et al."
    return ", ".join(names)


def _sentence_case(title):
    title = " ".join((title or "").split()).rstrip(".")
    words = title.split(" ")
    out = []
    for i, w in enumerate(words):
        core = w.strip("()\"'“”:,;")
        if i == 0 or core in PROTECT or not core:
            out.append(w)
        elif re.fullmatch(r"[A-Z][a-z]+(-[a-z]+)*", core):
            out.append(w.replace(core, core.lower()))
        else:
            out.append(w)   # acronyms, mixed case (LI-RADS, MRI, TI-RADS) stay as they are
    return " ".join(out)


def _pages(p):
    if not p:
        return ""
    m = re.fullmatch(r"([A-Za-z]*)(\d+)-([A-Za-z]*)(\d+)", p)
    if not m:
        return p
    pre, a, pre2, b = m.groups()
    if pre or pre2 or len(a) != len(b):
        return p
    i = 0
    while i < len(a) - 1 and a[i] == b[i]:
        i += 1
    return f"{a}-{b[i:]}"


def _year(msg):
    for k in ("published-print", "journal-issue", "issued", "published-online"):
        d = msg.get(k)
        if isinstance(d, dict) and d.get("date-parts"):
            return d["date-parts"][0][0]
        if isinstance(d, dict) and d.get("published-print"):
            return d["published-print"]["date-parts"][0][0]
    return None


def build(ref_id, msg):
    import html as _html
    journal = _html.unescape((msg.get("short-container-title") or msg.get("container-title") or ["?"])[0]).replace(".", "")
    journal = JOURNAL_ABBR.get(journal, journal)
    year = _year(msg)
    vol, issue, pages = msg.get("volume") or "", msg.get("issue") or "", _pages(msg.get("page") or "")
    loc = f"{year};{vol}" + (f"({issue})" if issue else "") + (f":{pages}" if pages else "")
    title = _sentence_case((msg.get("title") or ["?"])[0])
    auth = _authors(msg)
    van = f"{auth}{'' if auth.endswith('.') else '.'} {title}. {journal}. {loc}. doi:{msg['DOI']}"
    return {
        "id": ref_id,
        "doi": msg["DOI"].lower(),
        "first_author": next((re.sub(r'\d+(,\d+)*$', '', a.get('family', '')) for a in msg.get("author") or [] if a.get("family")), ""),
        "title_crossref": " ".join(((msg.get("title") or [""])[0]).split()),
        "journal": journal,
        "year": year,
        "volume": vol,
        "issue": issue,
        "pages": msg.get("page") or "",
        "vancouver": van,
        "vancouver_reviewed": False,
        "crossref_checked": dt.date.today().isoformat(),
        "license_note": "",
        "notes": "",
    }


def crossref(doi):
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="/()")
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    return json.loads(urllib.request.urlopen(req, timeout=30).read())["message"]


def save(new):
    data = json.loads(REFS.read_text()) if REFS.exists() else []
    keep = {r["id"]: r for r in data}
    for r in new:
        old = keep.get(r["id"])
        if old and old.get("vancouver_reviewed"):
            # never overwrite a human-reviewed citation; just refresh the check date
            old["crossref_checked"] = r["crossref_checked"]
            continue
        keep[r["id"]] = r
    out = sorted(keep.values(), key=lambda r: r["id"])
    REFS.parent.mkdir(parents=True, exist_ok=True)
    REFS.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n")


def main():
    if len(sys.argv) == 3 and sys.argv[1] == "--from-cache":
        cache = json.loads(Path(sys.argv[2]).read_text())
        save([build(k, v) for k, v in cache.items() if v])
    elif len(sys.argv) == 3:
        save([build(sys.argv[1], crossref(sys.argv[2]))])
    else:
        sys.exit(__doc__)
    print("ok:", REFS)


if __name__ == "__main__":
    main()
