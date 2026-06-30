# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the project

```
python score_calculator.py
```

No dependencies beyond the Python standard library. No build or install step required.

## Architecture

This is a learning/practice repository tracking the iterative development of a CLI score calculator. The files represent a progression of versions:

| File | Description |
|------|-------------|
| `score_calculator_v1.py` | Baseline: collects scores, computes average, no error handling |
| `score_calculator_v2.py` | Adds `try/except` for invalid input |
| `score_calculator FINAL.py` | Adds `.strip()` for whitespace tolerance |
| `score_calculator_v4.py` | Adds range validation (0–100), empty-input guard, live feedback per entry |
| `score_calculator.py` | Current canonical version: includes all of the above plus min/max, pass/fail count, and letter grade (A/B/C/D/F based on average, pass threshold ≥ 40) |

`README.md` and `README.txt` (identical content) document this version history.

All versions are flat scripts with no functions or modules — logic runs at the top level in a `while True` input loop followed by a results block.

## Rules

- Always show proposed changes before applying them
- Never delete files without asking first
- Keep all secret keys server side — never in browser/client code
- Keep replies short and avoid jargon
- Always explain in plain, clear English
- A task counts as done ONLY if it runs without errors and to the standard set by the user

## Troubleshooting

If the app doesn't start, check for syntax errors first:

```
python -m py_compile score_calculator.py
```

A clean run means no syntax errors.
