# Contract for tools that consume radref

1. **Pin a release.** Use a git tag (e.g. `v0.3.0`), copied into the tool's own environment
   (git submodule, vendored copy or periodic pull). Do not fetch the live repository while a
   report is being generated: it adds a network dependency and an injection surface.
2. **Record the version.** Store the radref tag used for each report (e.g. in the batch
   metadata). This keeps reports auditable (Res. CFM 2.454/2026 asks for auditability of AI
   tools in medicine).
3. **Verified only.** A categorization, threshold or recommendation in a report must come from
   an entry with `status: verified`. Draft entries may be read for background, never cited.
4. **Cite exactly.** Copy the Vancouver string from `references/references.json` by id. Never
   rebuild a citation from memory. Only `vancouver_reviewed: true` references may be printed.
5. **Respect scope.** Check the entry's scope and exclusions before applying it. Out of scope:
   describe the finding without the category and say why.
6. **Do not extrapolate.** "What the source does not say" lists claims that must not be
   attributed to the source.
7. **Dictation prevails.** If the physician dictates a category or recommendation, keep it; if
   it seems inconsistent with the entry, flag it for the physician instead of changing it.
8. **House rules live in the tool.** Report language, phrasing, superscript style, which of two
   disagreeing systems to use: those are the tool's (or the service's) configuration, not
   radref's.
9. **No patient data** ever goes into this repository, its issues or its pull requests.
