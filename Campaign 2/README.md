# ToDo List (CLI)

A simple command-line to-do list app written in Python, with no dependencies beyond the standard library.

## Running

```
python todo.py
```

## Features

- Add, view, and remove tasks
- Mark tasks as complete
- Tasks persist between runs in `tasks.json` (created automatically, not tracked by git)
- Input validation: empty tasks, invalid menu choices, and out-of-range task numbers are all caught with a friendly error message

## Usage

On launch you'll see a menu:

```
1) Add task
2) View tasks
3) Remove task
4) Mark task complete
5) Exit
```

Pick a number and follow the prompts.
