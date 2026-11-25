#!/usr/bin/env python3
"""Build the static browse site into _site/ (published with GitHub Pages).

    pip install pyyaml markdown
    python3 scripts/build_site.py

Reads entries/, references/references.json, index.json, docs/for-tools.md. Self-contained
output: one CSS file, one small JS file, no external requests. Citation keys such as
[acr-renal-2018], [fleischner-2017, Table] or [a; b, p. 3] become links to references.html.
Fails (exit 1) if an entry cites a key that is not in references.json.
"""
import html
import json
import re
import shutil
import sys
from pathlib import Path

import markdown
import yaml

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "_site"
REPO = "https://github.com/winroque/radref"
SITE = "https://winroque.github.io/radref/"
KEY = re.compile(r"[a-z][a-z0-9]*(-[a-z0-9]+)+")
AREAS = {"abdomen": "Abdomen", "pelvis-obstetrics": "Pelvis & obstetrics", "breast": "Breast",
         "thyroid-neck": "Thyroid & neck", "chest": "Chest", "neuro": "Neuro", "vascular": "Vascular",
         "msk-spine": "MSK & spine", "pediatrics": "Pediatrics", "oncology": "Oncology",
         "general": "General"}
TYPES = {"classification": "Classification", "scale": "Scale", "reference-values": "Reference values",
         "guideline": "Guideline", "terminology": "Terminology"}
POP = {"adults": "Adults", "children": "Children", "pregnant": "Pregnant patients", "all": "All ages"}
DRAFT_LONG = "Draft — awaiting radiologist sign-off; do not cite in reports"
E = html.escape


def front_matter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    meta = yaml.safe_load(m.group(1))
    meta = {k: (v.isoformat() if hasattr(v, "isoformat") else v) for k, v in meta.items()}
    return meta, text[m.end():]


def area_label(a):
    return AREAS.get(a, a)


# ---------- rendering ----------

def render_body(body, refs, entry_id, problems):
    """Markdown -> HTML, with citation keys turned into links to references.html."""
    body = re.sub(r"^\s*# .*\n", "", body, count=1)          # page title is rendered by the template
    cites = []

    def cite(m):
        parts_out, found = [], False
        for part in m.group(1).split(";"):
            toks = [t.strip() for t in part.split(",")]
            out = []
            for i, t in enumerate(toks):
                if i == 0 or KEY.fullmatch(t):
                    if KEY.fullmatch(t):
                        found = True
                        if t in refs:
                            out.append(f'<a href="../references.html#{E(t)}">{E(t)}</a>')
                        else:
                            problems.append(f"{entry_id}: citation key '{t}' not in references.json")
                            out.append(f'<span class="missing">{E(t)}</span>')
                        continue
                out.append(E(t))
            parts_out.append(", ".join(out))
        if not found:
            return m.group(0)
        cites.append('<span class="cite">[' + "; ".join(parts_out) + "]</span>")
        return f"RADREFCITE{len(cites) - 1}ZZ"

    # citations inside headings stay plain text (they would end up in the heading ids / contents list)
    body = "\n".join(line if line.startswith("#") else re.sub(r"\[([^\[\]\n]+?)\]", cite, line)
                     for line in body.split("\n"))
    body = body.replace("<", "&lt;")                         # no raw HTML from entry text
    md = markdown.Markdown(extensions=["tables", "toc"],
                           extension_configs={"toc": {"toc_depth": "2-3"}})
    out = md.convert(body)
    out = re.sub(r"RADREFCITE(\d+)ZZ", lambda m: cites[int(m.group(1))], out)
    out = out.replace("<table>", '<div class="tw" role="region" tabindex="0" aria-label="Table, scrolls sideways">'
                                 "<table>").replace("</table>", "</table></div>")
    toc = [t for t in md.toc_tokens]
    return out, toc


def toc_html(tokens):
    items = []
    for t in tokens:
        items.append(f'<li><a href="#{E(t["id"])}">{E(t["name"])}</a></li>')
        for c in t.get("children", []):
            items.append(f'<li class="sub"><a href="#{E(c["id"])}">{E(c["name"])}</a></li>')
    return "<nav class=\"toc\" aria-label=\"On this page\"><h2>On this page</h2><ul>" + "".join(items) + "</ul></nav>" if items else ""


def status_badge(status, long=False):
    if status == "verified":
        return '<span class="badge verified">Verified</span>'
    return f'<span class="badge draft" title="{E(DRAFT_LONG)}">{E(DRAFT_LONG) if long else "Draft"}</span>'


def ref_block(r, depth="", anchor=True, cited_by=None):
    v = E(r["vancouver"])
    links = []
    if r.get("doi"):
        d = r["doi"]
        links.append(f'<a href="https://doi.org/{E(d)}" rel="noopener">doi:{E(d)}</a>')
    if r.get("url"):
        links.append(f'<a href="{E(r["url"])}" rel="noopener">Source page</a>')
    meta = []
    if not r.get("vancouver_reviewed"):
        meta.append('<span class="badge draft">Citation not yet reviewed</span>')
    if r.get("license_note"):
        meta.append(f'<span class="lic">Licence note: {E(r["license_note"])}</span>')
    extra = ""
    if cited_by:
        extra = '<p class="citedby">Cited in: ' + ", ".join(
            f'<a href="entries/{E(i)}.html">{E(t)}</a>' for i, t in cited_by) + "</p>"
    idattr = f' id="{E(r["id"])}"' if anchor else ""
    return (f'<li class="ref"{idattr}><p class="vanc">{v}</p>'
            f'<p class="rmeta"><code>{E(r["id"])}</code>{" · " + " · ".join(links) if links else ""}</p>'
            f'{"<p>" + " ".join(meta) + "</p>" if meta else ""}{extra}</li>')


NAV = [("index.html", "Entries"), ("references.html", "References"), ("for-tools.html", "For tools")]


def page(title, body, depth=0, desc="", current="", extra_head=""):
    up = "../" * depth
    nav = "".join(f'<a href="{up}{h}"{" aria-current=\"page\"" if h == current else ""}>{E(t)}</a>' for h, t in NAV)
    full_title = title if title == "radref" else f"{title} · radref"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(full_title)}</title>
<meta name="description" content="{E(desc or 'Source-checked radiology reference summaries for AI reporting tools.')}">
<meta name="color-scheme" content="light dark">
<link rel="stylesheet" href="{up}assets/style.css">
{extra_head}</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="top"><div class="wrap bar">
<a class="brand" href="{up}index.html"><span class="mark" aria-hidden="true">r</span>radref</a>
<nav class="menu" aria-label="Main">{nav}<a href="{REPO}" rel="noopener">GitHub</a></nav>
</div></header>
<main id="main" class="wrap">
{body}
</main>
<footer class="foot"><div class="wrap">
<p><strong>Supports, does not replace, the judgment of the physician who signs the report.</strong>
Entries are summaries in our own words with attributed numbers; they are not the sources.
Always check the primary source before relying on a threshold.</p>
<p>Licence: summaries <a href="https://creativecommons.org/licenses/by/4.0/" rel="noopener">CC BY 4.0</a>;
scripts MIT. Cited articles and classification systems belong to their authors and publishers.
<a href="{REPO}/blob/main/LICENSE.md" rel="noopener">Details</a>.</p>
<p><a href="{REPO}" rel="noopener">Source repository</a> ·
<a href="{up}llms.txt">llms.txt</a> · <a href="{up}index.json">index.json</a> ·
<a href="{up}references.json">references.json</a> · <a href="{up}for-tools.html">For tools</a></p>
</div></footer>
</body>
</html>
"""


# ---------- pages ----------

def build_entry(meta, body, refs, titles, problems, cited_in):
    html_body, toc = render_body(body, refs, meta["id"], problems)
    for s in meta["sources"]:
        cited_in.setdefault(s, []).append((meta["id"], meta["title"]))
    rows = [("Type", TYPES.get(meta["type"], meta["type"])),
            ("Area", area_label(meta["area"])),
            ("Modalities", ", ".join(meta["modalities"])),
            ("Population", POP.get(meta["population"], meta["population"])),
            ("Source version", meta["source_version"]),
            ("Status", status_badge(meta["status"], long=True)),
            ("Verified against", E(str(meta.get("verified_against", "")))),
            ("Last reviewed", meta["last_reviewed"])]
    if meta.get("status") == "verified":
        if meta.get("verified_by"):
            rows.append(("Verified by", E(str(meta.get("verified_by", "")))))
        rows.append(("Verified on", E(str(meta.get("verified_on", "")))))
    if meta.get("superseded_by"):
        rows.append(("Superseded by", f'<a href="{E(meta["superseded_by"])}.html">{E(titles.get(meta["superseded_by"], meta["superseded_by"]))}</a>'))
    if meta.get("supersedes"):
        rows.append(("Supersedes", ", ".join(f'<a href="{E(i)}.html">{E(titles.get(i, i))}</a>' for i in meta["supersedes"])))
    if meta.get("related"):
        rows.append(("Related", "<ul class=\"rel\">" + "".join(
            f'<li><a href="{E(i)}.html">{E(titles.get(i, i))}</a></li>' for i in meta["related"]) + "</ul>"))
    dl = "".join(f"<dt>{k}</dt><dd>{v if k in ('Status', 'Related', 'Superseded by', 'Supersedes', 'Verified against', 'Verified by', 'Verified on') else E(v)}</dd>" for k, v in rows)
    banner = ""
    if meta["status"] != "verified":
        banner = (f'<p class="banner" role="note"><strong>{E(DRAFT_LONG)}.</strong> '
                  "Checked by AI against the source, not yet signed off by a radiologist. "
                  "Use as background reading only.</p>")
    refs_html = "".join(ref_block(refs[s], anchor=False) for s in meta["sources"])
    body_out = f"""
<p class="crumb"><a href="../index.html">Entries</a> / {E(area_label(meta["area"]))}</p>
<h1>{E(meta["title"])}</h1>
{banner}
<div class="entry-grid">
<aside class="side"><h2 class="vh">Metadata</h2><dl class="meta">{dl}</dl>{toc_html(toc)}</aside>
<article class="prose">
{html_body}
<section class="refbox" aria-labelledby="refs"><h2 id="refs">References</h2>
<p class="note">Vancouver strings as stored in the repository. Copy them exactly; cite only references marked reviewed.</p>
<ol class="reflist">{refs_html}</ol>
<p><a href="{REPO}/blob/main/{E(meta["_path"])}" rel="noopener">View this entry on GitHub</a></p></section>
</article>
</div>"""
    desc = f'{meta["title"]} — {area_label(meta["area"])}, {", ".join(meta["modalities"])}. {DRAFT_LONG if meta["status"] != "verified" else "Verified summary"}.'
    (OUT / "entries" / f'{meta["id"]}.html').write_text(page(meta["title"], body_out, 1, desc), encoding="utf-8")


def card(m):
    mods = " ".join(m["modalities"])
    hay = " ".join([m["title"], m["id"], area_label(m["area"]), m["area"], mods, TYPES.get(m["type"], "")]).lower()
    chips = "".join(f'<span class="chip-s">{E(x)}</span>' for x in m["modalities"])
    return (f'<li class="card" data-area="{E(m["area"])}" data-mod="{E(mods)}" data-search="{E(hay)}">'
            f'<a class="cardlink" href="entries/{E(m["id"])}.html"><span class="ctitle">{E(m["title"])}</span></a>'
            f'<p class="cmeta"><span>{E(area_label(m["area"]))}</span><span>{E(TYPES.get(m["type"], m["type"]))}</span>'
            f'<span>{E(m["source_version"])}</span></p>'
            f'<p class="cmods">{chips}</p>'
            f'<p>{status_badge(m["status"])}</p>'
            f'{"<p class=cnote>Not for citing in reports until verified.</p>" if m["status"] != "verified" else ""}</li>')


def build_index(entries, nrefs):
    areas = sorted({m["area"] for m in entries}, key=lambda a: area_label(a))
    mods = sorted({x for m in entries for x in m["modalities"]})
    n_ver = sum(m["status"] == "verified" for m in entries)
    entries = sorted(entries, key=lambda m: m["title"].lower())
    area_chips = '<button type="button" class="chip" data-area="" aria-pressed="true">All areas</button>' + "".join(
        f'<button type="button" class="chip" data-area="{E(a)}" aria-pressed="false">{E(area_label(a))} '
        f'<span class="n">{sum(m["area"] == a for m in entries)}</span></button>' for a in areas)
    mod_opts = '<option value="">All modalities</option>' + "".join(f'<option value="{E(x)}">{E(x)}</option>' for x in mods)
    body = f"""
<section class="hero">
<p class="eyebrow">Open reference base for AI radiology reporting</p>
<h1>Radiology classifications and reference values, with the sources attached.</h1>
<p class="lead">radref holds structured, source-checked summaries of radiology classification systems
(RADS, Bosniak, Fleischner…), reference measurements and guideline recommendations. Each entry says
what the system covers, the criteria, the management, the pitfalls, and <em>what the source does not say</em>,
and gives a checked Vancouver reference to cite.</p>
<p class="sub" lang="pt">Base de referência aberta para laudos de radiologia assistidos por IA: resumos com fonte, sem texto integral.</p>
<ul class="stats" aria-label="Counts">
<li><strong>{len(entries)}</strong> entries</li><li><strong>{nrefs}</strong> references</li>
<li><strong>{len(areas)}</strong> areas</li><li><strong>{n_ver}</strong> verified</li>
</ul>
{"" if n_ver == len(entries) else f'<p class="banner" role="note"><strong>Status: {len(entries) - n_ver} of {len(entries)} entries are drafts.</strong> {E(DRAFT_LONG)}.</p>'}
</section>

<section aria-labelledby="browse">
<h2 id="browse">Browse entries</h2>
<div class="filters" role="search">
<div class="field"><label for="q">Search title, id, area or modality</label>
<input id="q" type="search" placeholder="e.g. bosniak, CT, thyroid" autocomplete="off"></div>
<div class="field"><label for="mod">Modality</label><select id="mod">{mod_opts}</select></div>
</div>
<div class="chips" role="group" aria-label="Filter by area">{area_chips}</div>
<p id="count" class="count" aria-live="polite">{len(entries)} entries</p>
<ul class="cards" id="cards">{"".join(card(m) for m in entries)}</ul>
<p id="empty" class="empty" hidden>No entries match. Clear the search or filters.</p>
</section>

<section class="rules" aria-labelledby="rules">
<h2 id="rules">The rules</h2>
<ul class="rulegrid">
<li><h3>Our own words</h3><p>Summaries and the numbers needed to apply each system, with attribution. Never the full text, figures or verbatim tables of the articles.</p></li>
<li><h3>Every number has a source</h3><p>Each source is in the references file, checked against Crossref. A reference is cited in a report only when its Vancouver string is marked reviewed.</p></li>
<li><h3>Draft vs verified</h3><p>Draft means written but not yet checked. Verified means every number and criterion was compared with the full text of the source (AI-assisted, in several review rounds) and approved by the maintainer. It supports, and does not replace, the judgment of the physician who signs the report.</p></li>
<li><h3>What the source does not say</h3><p>Every entry lists claims that must not be attributed to the source, so tools do not invent them.</p></li>
</ul>
</section>

<section class="use" aria-labelledby="use">
<h2 id="use">Using it in a tool</h2>
<p>Pin a tagged release, read <code>index.json</code>, use only <code>verified</code> entries to support a
category or recommendation, and copy Vancouver strings exactly. See <a href="for-tools.html">the contract for tools</a>,
<a href="llms.txt">llms.txt</a> and <a href="index.json">index.json</a>.</p>
</section>
<script src="assets/site.js" defer></script>
"""
    (OUT / "index.html").write_text(page("radref", body, 0, "Source-checked summaries of radiology classification systems and reference values, for AI reporting tools. Open, CC BY 4.0.", "index.html"), encoding="utf-8")


def build_refs(refs, cited_in):
    items = sorted(refs.values(), key=lambda r: r["vancouver"].lower())
    body = f"""
<h1>References</h1>
<p class="lead">All {len(items)} sources cited by the entries. Vancouver strings are checked against Crossref;
only those marked reviewed may be printed in a report. Links go to the DOI resolver or the publisher's page.</p>
<ol class="reflist big">{"".join(ref_block(r, cited_by=cited_in.get(r["id"])) for r in items)}</ol>"""
    (OUT / "references.html").write_text(page("References", body, 0, "All references cited by radref entries, with Vancouver strings and DOI links.", "references.html"), encoding="utf-8")


def build_tools():
    text = (ROOT / "docs" / "for-tools.md").read_text(encoding="utf-8").replace("<", "&lt;")
    md = markdown.Markdown(extensions=["tables", "toc"])
    inner = md.convert(text)
    body = f"""<div class="prose narrow">{inner}
<h2>Machine-readable files</h2>
<ul><li><a href="llms.txt">llms.txt</a>: short guide for AI tools</li>
<li><a href="index.json">index.json</a>: list of entries with id, title, scope, status and sources</li>
<li><a href="references.json">references.json</a>: every source with checked metadata and Vancouver string</li>
<li><a href="{REPO}" rel="noopener">GitHub repository</a>: entries as Markdown with YAML front matter (<code>entries/&lt;area&gt;/&lt;id&gt;.md</code>)</li></ul></div>"""
    (OUT / "for-tools.html").write_text(page("For tools", body, 0, "Contract for tools that consume radref.", "for-tools.html"), encoding="utf-8")


# ---------- assets ----------

CSS = r"""
:root{--bg:#f7f8f6;--surface:#fff;--ink:#16211f;--muted:#4b5b57;--line:#d9dfdb;--accent:#0b5f5a;--accent-ink:#fff;
--accent-soft:#e1f0ee;--warn-bg:#fff4d6;--warn-line:#e0b341;--warn-ink:#5a3f00;--ok-bg:#dff3e4;--ok-ink:#12522a;--focus:#1a5fd0;
--shadow:0 1px 2px rgba(20,40,35,.06),0 4px 14px rgba(20,40,35,.05)}
@media (prefers-color-scheme:dark){:root{--bg:#0f1514;--surface:#172120;--ink:#e6eeeb;--muted:#a3b3ae;--line:#2b3a37;
--accent:#59c2b8;--accent-ink:#062421;--accent-soft:#16312e;--warn-bg:#33290d;--warn-line:#8a6d1c;--warn-ink:#f3d98a;
--ok-bg:#12331f;--ok-ink:#9fe0b4;--focus:#8ab4ff;--shadow:none}}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.6 Charter,"Iowan Old Style","Palatino Linotype",Georgia,serif}
h1,h2,h3,.brand,.menu,.badge,.chip,label,.eyebrow,.stats,dt,.crumb,.toc,.cmeta,.chip-s{font-family:system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif}
a{color:var(--accent);text-underline-offset:2px}
a:hover{text-decoration-thickness:2px}
:focus-visible{outline:3px solid var(--focus);outline-offset:2px;border-radius:3px}
.wrap{max-width:1120px;margin:0 auto;padding:0 16px}
.skip{position:absolute;left:-999px;top:0;background:var(--accent);color:var(--accent-ink);padding:8px 12px;z-index:10}
.skip:focus{left:8px;top:8px}
.vh{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}
.top{background:var(--surface);border-bottom:1px solid var(--line);position:sticky;top:0;z-index:5}
.bar{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:4px 16px;min-height:56px}
.brand{display:flex;align-items:center;gap:10px;font-weight:700;font-size:1.2rem;color:var(--ink);text-decoration:none}
.mark{display:inline-grid;place-items:center;width:30px;height:30px;border-radius:8px;background:var(--accent);color:var(--accent-ink);font-weight:800}
.menu{display:flex;flex-wrap:wrap;gap:2px 4px;font-size:.95rem}
.menu a{padding:8px 10px;border-radius:6px;color:var(--ink);text-decoration:none}
.menu a:hover{background:var(--accent-soft)}
.menu a[aria-current=page]{background:var(--accent-soft);color:var(--accent);font-weight:600}
main{padding-top:24px;padding-bottom:48px}
h1{font-size:clamp(1.6rem,4.5vw,2.4rem);line-height:1.2;margin:.2em 0 .5em;letter-spacing:-.01em}
h2{font-size:1.4rem;line-height:1.3;margin:1.8em 0 .5em}
h3{font-size:1.1rem;margin:1.4em 0 .4em}
.eyebrow{text-transform:uppercase;letter-spacing:.08em;font-size:.8rem;color:var(--accent);font-weight:700;margin:0}
.hero{padding:16px 0 8px}
.hero h1{max-width:20em}
.lead{font-size:1.1rem;color:var(--muted);max-width:46em}
.sub{color:var(--muted);font-style:italic;margin-top:-.4em}
.stats{display:flex;flex-wrap:wrap;gap:8px 28px;list-style:none;padding:0;margin:18px 0;color:var(--muted)}
.stats strong{font-size:1.7rem;color:var(--ink);margin-right:4px}
.banner{background:var(--warn-bg);border:1px solid var(--warn-line);color:var(--warn-ink);padding:10px 14px;border-radius:8px;font-family:system-ui,sans-serif;font-size:.95rem;line-height:1.5}
.rulegrid{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:14px}
.rulegrid li{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:4px 16px 12px;box-shadow:var(--shadow)}
.rulegrid h3{margin-top:.8em}.rulegrid p{margin:.2em 0;color:var(--muted);font-size:.97rem}
.filters{display:grid;grid-template-columns:1fr 200px;gap:12px;margin:10px 0}
.field label{display:block;font-size:.85rem;font-weight:600;margin-bottom:4px;color:var(--muted)}
input[type=search],select{width:100%;font:inherit;font-family:system-ui,sans-serif;font-size:1rem;padding:10px 12px;border:1px solid var(--muted);border-radius:8px;background:var(--surface);color:var(--ink);min-height:44px}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin:8px 0}
.chip{font-size:.88rem;padding:7px 12px;border:1px solid var(--line);background:var(--surface);color:var(--ink);border-radius:999px;cursor:pointer;min-height:36px}
.chip:hover{border-color:var(--accent)}
.chip[aria-pressed=true]{background:var(--accent);color:var(--accent-ink);border-color:var(--accent)}
.chip .n{opacity:.7;margin-left:3px}
.count{font-family:system-ui,sans-serif;color:var(--muted);font-size:.9rem}
.cards{list-style:none;padding:0;margin:8px 0;display:grid;grid-template-columns:repeat(auto-fill,minmax(290px,1fr));gap:14px}
.card{position:relative;background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:14px 16px;box-shadow:var(--shadow)}
.card:hover,.card:focus-within{border-color:var(--accent)}
.card[hidden]{display:none}
.cardlink{text-decoration:none;color:var(--ink)}
.cardlink::after{content:"";position:absolute;inset:0}
.ctitle{font-family:system-ui,sans-serif;font-weight:650;line-height:1.35;display:block}
.cardlink:hover .ctitle{color:var(--accent)}
.card p{margin:.5em 0 0}
.cmeta{display:flex;flex-wrap:wrap;gap:2px 12px;font-size:.82rem;color:var(--muted)}
.cmods{display:flex;gap:6px;flex-wrap:wrap}
.chip-s{font-size:.75rem;font-weight:600;background:var(--accent-soft);color:var(--accent);padding:2px 8px;border-radius:5px}
.cnote{font-size:.8rem;color:var(--muted);font-family:system-ui,sans-serif}
.badge{display:inline-block;font-size:.78rem;font-weight:650;padding:3px 9px;border-radius:5px;line-height:1.4}
.badge.draft{background:var(--warn-bg);color:var(--warn-ink);border:1px solid var(--warn-line)}
.badge.verified{background:var(--ok-bg);color:var(--ok-ink)}
.empty{padding:20px;text-align:center;color:var(--muted)}
.crumb{font-size:.85rem;color:var(--muted);margin:0}
.entry-grid{display:grid;grid-template-columns:300px minmax(0,1fr);gap:32px;align-items:start;margin-top:16px}
.side{position:sticky;top:72px;max-height:calc(100vh - 88px);overflow:auto}
.meta{margin:0;background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:8px 14px;font-size:.88rem;line-height:1.45}
.meta dt{font-weight:650;color:var(--muted);font-size:.75rem;text-transform:uppercase;letter-spacing:.05em;margin-top:10px}
.meta dd{margin:2px 0 6px;font-family:system-ui,sans-serif;overflow-wrap:anywhere}
.rel{margin:0;padding-left:18px}
.toc{margin-top:16px;font-size:.88rem}
.toc h2{font-size:.8rem;text-transform:uppercase;letter-spacing:.05em;color:var(--muted);margin:0 0 6px}
.toc ul{list-style:none;padding:0;margin:0}.toc li{margin:3px 0}.toc .sub{padding-left:14px}
.toc a{text-decoration:none}.toc a:hover{text-decoration:underline}
.prose{min-width:0;max-width:760px}
.prose.narrow{margin:0 auto}
.prose h2{border-top:1px solid var(--line);padding-top:.9em;font-size:1.3rem}
.prose h2:first-child{border-top:0}
.prose blockquote{margin:1em 0;padding:.2em 1em;border-left:4px solid var(--accent);background:var(--accent-soft);border-radius:0 8px 8px 0}
.prose code,.rmeta code{font:.85em ui-monospace,SFMono-Regular,Menlo,monospace;background:var(--accent-soft);padding:1px 5px;border-radius:4px}
.tw{overflow-x:auto;margin:1em 0;border:1px solid var(--line);border-radius:8px;background:var(--surface)}
table{border-collapse:collapse;width:100%;font-size:.9rem;font-family:system-ui,sans-serif;line-height:1.45}
th,td{padding:8px 10px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top;min-width:90px}
th{background:var(--accent-soft);font-weight:650;white-space:nowrap}
tr:last-child td{border-bottom:0}
.cite{font-size:.78em;font-family:system-ui,sans-serif;color:var(--muted);overflow-wrap:anywhere}
.cite a{white-space:nowrap;text-decoration:none;border-bottom:1px dotted var(--accent)}
.missing{color:#b00020;font-weight:700}
.refbox{margin-top:2.5em;padding:6px 18px 14px;background:var(--surface);border:1px solid var(--line);border-radius:10px}
.refbox h2{border:0;margin-top:.6em}
.note{color:var(--muted);font-size:.9rem}
.reflist{padding-left:24px}
.ref{margin:0 0 14px;padding-left:4px;scroll-margin-top:72px}
.ref:target{background:var(--accent-soft);border-radius:6px;outline:2px solid var(--accent)}
.ref p{margin:.15em 0}
.vanc{overflow-wrap:anywhere}
.rmeta,.citedby,.lic{font-family:system-ui,sans-serif;font-size:.82rem;color:var(--muted)}
.reflist.big>li{border-bottom:1px solid var(--line);padding-bottom:12px}
.use{margin-top:2em}
.foot{border-top:1px solid var(--line);background:var(--surface);padding:20px 0 32px;font-size:.9rem;color:var(--muted);font-family:system-ui,sans-serif}
.foot p{margin:.5em 0}
@media (max-width:860px){.entry-grid{grid-template-columns:1fr}.side{position:static;max-height:none}.toc{display:none}}
@media (max-width:560px){body{font-size:16px}.filters{grid-template-columns:1fr}.menu a{padding:8px}.cards{grid-template-columns:1fr}}
@media print{.top,.filters,.chips,.skip{display:none}body{background:#fff;color:#000}}
"""

JS = r"""(function(){
var q=document.getElementById('q');if(!q)return;
var mod=document.getElementById('mod'),cards=[].slice.call(document.querySelectorAll('#cards .card')),
chips=[].slice.call(document.querySelectorAll('.chip')),count=document.getElementById('count'),empty=document.getElementById('empty'),area='';
function apply(){
var t=q.value.trim().toLowerCase().split(/\s+/).filter(Boolean),m=mod.value,n=0;
cards.forEach(function(c){
var s=c.getAttribute('data-search'),ok=t.every(function(w){return s.indexOf(w)>-1})
&&(!area||c.getAttribute('data-area')===area)
&&(!m||(' '+c.getAttribute('data-mod')+' ').indexOf(' '+m+' ')>-1);
c.hidden=!ok;if(ok)n++;});
count.textContent=n+(n===1?' entry':' entries');empty.hidden=n>0;
try{var p=new URLSearchParams();if(q.value)p.set('q',q.value);if(area)p.set('area',area);if(m)p.set('mod',m);
history.replaceState(null,'',location.pathname+(p.toString()?'?'+p:''));}catch(e){}}
chips.forEach(function(b){b.addEventListener('click',function(){area=b.getAttribute('data-area');
chips.forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false')});apply();});});
q.addEventListener('input',apply);mod.addEventListener('change',apply);
try{var p=new URLSearchParams(location.search);q.value=p.get('q')||'';mod.value=p.get('mod')||'';
var a=p.get('area');if(a){chips.forEach(function(b){if(b.getAttribute('data-area')===a){b.click();}});}}catch(e){}
apply();})();
"""


def main():
    refs = {r["id"]: r for r in json.loads((ROOT / "references" / "references.json").read_text(encoding="utf-8"))}
    parsed = []
    for p in sorted((ROOT / "entries").rglob("*.md")):
        meta, body = front_matter(p.read_text(encoding="utf-8"))
        meta["_path"] = str(p.relative_to(ROOT))
        parsed.append((meta, body))
    titles = {m["id"]: m["title"] for m, _ in parsed}
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "entries").mkdir(parents=True)
    (OUT / "assets").mkdir()
    (OUT / "assets" / "style.css").write_text(CSS.strip() + "\n", encoding="utf-8")
    (OUT / "assets" / "site.js").write_text(JS, encoding="utf-8")
    problems, cited_in = [], {}
    for meta, body in parsed:
        for s in meta["sources"]:
            if s not in refs:
                problems.append(f"{meta['id']}: source '{s}' not in references.json")
        for r in meta.get("related", []) + meta.get("supersedes", []):
            if r not in titles:
                problems.append(f"{meta['id']}: related id '{r}' is not an entry")
        if problems and any(meta["id"] in x for x in problems):
            continue
        build_entry(meta, body, refs, titles, problems, cited_in)
    build_index([m for m, _ in parsed], len(refs))
    build_refs(refs, cited_in)
    build_tools()
    for f in ("llms.txt", "index.json"):
        shutil.copy(ROOT / f, OUT / f)
    shutil.copy(ROOT / "references" / "references.json", OUT / "references.json")
    (OUT / ".nojekyll").write_text("")
    for p in problems:
        print("ERROR:", p, file=sys.stderr)
    print(f"site built: {len(parsed)} entries, {len(refs)} references -> {OUT}")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
