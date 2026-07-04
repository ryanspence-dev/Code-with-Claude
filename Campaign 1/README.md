Score Calculator
================

A simple command-line tool for entering test scores and getting a summary.

## Running it

```
python score_calculator.py
```

## What it does

Prompts you to enter scores one at a time (0-100). Type "done" when finished.

Once you're done entering scores, it prints:
- Every score you entered
- Total number of scores
- Highest and lowest score
- Average score
- Letter grade (A/B/C/D/F, based on the average)
- Pass/fail count (pass threshold: score >= 40)

Invalid input (non-numbers, empty entries, or scores outside 0-100) is
rejected with a message, and you're prompted to try again - it won't crash.

## Development history

Earlier draft versions are kept in `old_versions/` for reference, showing
the tool's progression from a basic average calculator to the current
version:

1. `score_calculator_v1.py` - basic average calculator, crashes on bad input
2. `score_calculator_v2.py` - adds error handling for bad input
3. `score_calculator FINAL.py` - adds `.strip()` to tolerate stray whitespace
4. `score_calculator_v4.py` - adds range validation, empty-input guard, and
   live per-entry feedback

`score_calculator.py` (this project's current version) builds on all of the
above, adding min/max, pass/fail counts, and letter grading.
