# Contributing to radref

## 1. What goes in, what stays out

**In:** the source's own content, neutral, as a textbook chapter would summarize it —
definitions, criteria, numeric thresholds, management recommendations, scope, known
limitations, disagreements between sources.

**Out (stays in each tool's own project):**
- house rules of a given radiologist or service (which system to prefer when two disagree,
  wording preferences, whether measurements go in the impression, superscript citation style);
- report templates and phrases from third-party template collections (e.g. Compêndio);
- any patient data. Examples are fictitious and say so.

When two sources disagree (e.g. SRU 2022 vs European guidelines for gallbladder polyps),
the entry **describes both and the disagreement**; it does not choose.

## 2. Copyright

- Write in our own words. Do not paste paragraphs, figures, flowcharts or whole tables.
- Numeric thresholds and category definitions are facts and may be transcribed, with the
  source and the table/page they come from.
- Be stricter with proprietary manuals (ACR BI-RADS atlas, ACR TI-RADS chart, LI-RADS core
  documents): summarize criteria, link to the official page, do not reproduce the lexicon.
- Record the source's licence in `references.json` (`license_note`) when known
  (e.g. "CC BY 4.0", "RSNA — all rights reserved").
- Full-text PDFs never enter the repository (keep them outside, e.g. `docs/artigos/` in the
  tool's private project, which is git-ignored).

## 3. Language and style

- English. Original terms in parentheses when the report language uses them
  (e.g. "Portuguese report term: *categoria IIF*" is a tool concern; here, keep English).
- Short sentences. Tables for criteria. Units always (mm, cm, HU, mL, cm/s).
- Each criterion or number points to the source: `[bosniak-2019, Table 2]`.

## 4. Entry structure (fixed order)

Use `templates/entry-template.md`. Front matter fields are defined in
`schema/entry.schema.json`. Sections:

1. **Scope** — population, modality, what it does **not** apply to.
2. **Definitions** — terms the criteria depend on.
3. **Criteria / categories** — table.
4. **Management** — what the source recommends, per category.
5. **Pitfalls** — where the numbers are fragile, common misuses.
6. **What the source does not say** — things often attributed to it that are not in it.
7. **Disagreements and newer versions** — other sources, superseded versions.
8. **How to cite** — the reference id(s); the Vancouver string lives in `references.json`.
9. **Change log** — date, what changed, who.

## 5. Verification workflow

| Step | Who | Result |
|---|---|---|
| Add references with `scripts/add_reference.py` | anyone / AI | `vancouver_reviewed: false` |
| Check each Vancouver string against the article's first page (authors, title capitalization, journal abbreviation, print year, pages) | a person | `vancouver_reviewed: true` |
| Write the entry from the **full text** | AI or person | `status: draft`, `verified_against: pending` |
| Compare every number and criterion with the full text; fill `verified_against` with what was read (e.g. "full text PDF, Tables 1–3, Fig. 2") | the maintainer (AI-assisted checks against the full text are accepted) | `status: verified`, `verified_on` (`verified_by` optional) |
| Re-check when the source publishes a new version | anyone | new entry or `superseded_by` |

`scripts/build_index.py` refuses `status: verified` when `verified_against` is pending or
any source is not reviewed. The GitHub workflow runs both scripts on every push.

## 6. Adding a source

```bash
python3 scripts/add_reference.py <short-id-year> <doi>
```
Id style: `topic-year` or `author-topic-year`, lowercase, hyphens (`bosniak-2019`,
`kelsey-ovary-2013`). Never edit a reviewed reference without setting it back to
`vancouver_reviewed: false`.

Documents without a DOI (ACR manuals, core documents, society web pages) are added by hand
with `"doi": ""` and a `"url"` to the official page; `check_refs.py` skips them with a
warning, so their Vancouver string must be checked against the document itself.
