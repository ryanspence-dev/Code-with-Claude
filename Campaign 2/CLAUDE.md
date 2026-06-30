# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the project

```
python todo.py
```

No dependencies beyond the Python standard library. No build or install step required.

## Architecture

A single-file CLI to-do list app (`todo.py`). Unlike Campaign 1, this project does not keep separate version files — its build-up is recorded in git history instead:

1. Basic add/view/remove (in-memory only)
2. Mark tasks complete
3. JSON persistence (`tasks.json`, load/save helper functions)
4. Input validation and error handling (empty input, invalid menu choice, out-of-range task numbers)

The script is flat with two small helper functions (`load_tasks`, `save_tasks`) followed by a top-level `while True` menu loop — no classes.

`tasks.json` is created at runtime and is gitignored; it should never be committed.

## Rules

- Always show proposed changes before applying them
- Never delete files without asking first
- Keep replies short and avoid jargon
- Always explain in plain, clear English
- A task counts as done ONLY if it runs without errors and to the standard set by the user

## Troubleshooting

If the app doesn't start, check for syntax errors first:

```
python -m py_compile todo.py
```

A clean run means no syntax errors.
