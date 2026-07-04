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
