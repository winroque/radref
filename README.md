# radref — radiology reference base for AI reporting tools

Structured, source-checked summaries of radiology classification systems (RADS, Bosniak,
Fleischner…), normal/reference measurements and guideline recommendations, written so that
AI reporting assistants can:

1. read the **theory** (definitions, criteria, thresholds, management, pitfalls, scope);
2. know **what the source does not say** (so they do not invent it);
3. cite the source in a report with a **ready, checked Vancouver reference**.

This repository holds **summaries in our own words and the numbers needed to apply each
system** — never the full text, figures or verbatim tables of the articles.

> Status: **private, under construction.** Started 2026-11-06 from the reference files of the
> Digitado-IA reporting tool. Entries marked `status: draft` must not be used to cite in a
> report.

## Layout

```
entries/<area>/<id>.md        one topic per file (YAML front matter + fixed sections)
references/references.json    every cited source: DOI, Crossref metadata, Vancouver string
index.json                    generated list of entries (id, title, scope, status, sources)
llms.txt                      short guide for AI tools: where things are and the rules
templates/entry-template.md   copy this to start an entry
schema/entry.schema.json      required front-matter fields
scripts/                      build_index.py · check_refs.py · add_reference.py
docs/for-tools.md             contract for tools that consume this base
ROADMAP.md                    what is planned, in which order
```

Areas: `abdomen`, `pelvis-obstetrics`, `breast`, `thyroid-neck`, `chest`, `neuro`,
`vascular`, `msk-spine`, `pediatrics`, `oncology`, `general` (reference values that cross areas).

## Rules in one paragraph

Each entry states its scope and exclusions first, then the criteria, then management, then
pitfalls, then **"What the source does not say"**, then how to cite. Every number has a
source. Every source is in `references/references.json`, checked against Crossref, and only
cited in a report when `vancouver_reviewed: true`. An entry is `verified` only when a person
compared it with the primary source (full text) and all its references are reviewed. Tools
use a **tagged release**, copied locally — never the live repository during a report.

See `CONTRIBUTING.md` for the full rules and `docs/for-tools.md` for how tools must use it.

## Commands

```bash
pip install pyyaml
python3 scripts/build_index.py           # validates entries, regenerates index.json
python3 scripts/check_refs.py            # re-checks every DOI against Crossref (needs network)
python3 scripts/add_reference.py <id> <doi>   # adds a reference as an unreviewed draft
```
