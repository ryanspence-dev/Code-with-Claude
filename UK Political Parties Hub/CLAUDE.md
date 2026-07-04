# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the project

```
py -m flask --app app run
```

Requires Flask (see `requirements.txt`). No other build or install step required.

## Architecture

A Flask app (`app.py`) serving an unbiased UK political parties hub:

- `/` - hub page listing all parties as cards, linking to their manifesto page
- `/labour`, `/conservatives`, `/libdems`, `/reformuk`, `/green`, `/snp`, `/plaidcymru` - one page per party, summarizing that party's most recent general election manifesto in neutral, thematic sections, each themed in the party's own colour
- `/glossary` - a searchable, category-filterable glossary of political terms

Templates live in `templates/` (Jinja2, extending `base.html`), styling in `static/css/style.css`, and interactivity (accordion sections, dark mode toggle, glossary search/filter) in `static/js/script.js`. No JS framework or build step - plain HTML/CSS/JS.

Manifesto content must be fact-checked against each party's actual official manifesto (not just recalled from memory) before publishing, and each party page links to its official manifesto source at the bottom.

## What "unbiased" means on this site

This site's whole value is being a neutral reference, so content must stay neutral:

- Describe each party's own stated positions - don't editorialize, praise, or criticize them.
- Use neutral, dictionary-style language, even for loaded terms (e.g. "populism," "nationalism") - define what the term means, don't frame it positively or negatively.
- Never rank, rate, or comparatively judge parties against each other (no "better/worse," "more extreme," "more sensible," etc.). Each party gets its own page/summary on its own terms.
- Keep every party's page to a comparable level of depth and quality - don't give one party's page more detail, more sections, or more favorable framing than another's.

## Inline reference annotations

Manifesto bullets sometimes name a specific law, scheme, or named policy/movement (e.g. "the two-child benefit cap", "the Barnett formula") that a reader may not recognise, even though it isn't general political vocabulary. Mark these up inline so a click reveals a short neutral explanation, instead of leaving the reader to guess or look it up elsewhere.

- When to use it: a specific, named law, scheme, clause, or movement mentioned inside a manifesto bullet that most readers wouldn't be expected to already know. Not for general political vocabulary (first-past-the-post, devolution, nationalisation, etc.) - those belong on the `/glossary` page only, and shouldn't also get an inline pop-up.
- How to use it: add or reuse an entry in `REFERENCE_TERMS` in `app.py` (keyed by a short slug), then wrap the phrase in the party template with the `ref()` macro from `templates/_macros.html`, e.g. `{{ ref('barnett-formula', 'Barnett formula') }}`.
- Reuse, don't duplicate: if a concept already has an entry (e.g. the Barnett formula, used on both the SNP and Plaid Cymru pages), reuse its existing slug rather than adding a second entry with the same explanation.
- Don't duplicate the Glossary: if a term is already defined in `GLOSSARY_TERMS`, leave it as plain text on party pages instead of adding a `REFERENCE_TERMS` entry for it - each concept should be explained in exactly one place on the site.
- Neutrality standard: same bar as the rest of the site - write a short, factual, dictionary-style explanation of what the thing is and does. No framing it as good or bad, no party attribution beyond plain fact. Fact-check the explanation against a neutral, reliable source before publishing, same as manifesto content itself - and where a pledge's real-world status has since changed (enacted, cancelled, scrapped, superseded), note that too, since a lot of these 2024 manifesto pledges are now historical.

## Rules

- Commit after completing a coherent unit of work (feature, fix, or refactor). Each commit should represent a stable, working state with a clear message describing the change.
- Always show proposed changes before applying them
- Never delete files without asking first
- Keep replies short and avoid jargon
- Always explain in plain, clear English
- A task counts as done ONLY if it runs without errors and to the standard set by the user

## Troubleshooting

If the app doesn't start, check for syntax errors first:

```
py -m py_compile app.py
```

A clean run means no syntax errors.
