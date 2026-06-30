import json
import os

TASKS_FILE = "tasks.json"


def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


tasks = load_tasks()

print("=" * 40)
print("       TODO LIST")
print("=" * 40)

while True:
    print("\n1) Add task")
    print("2) View tasks")
    print("3) Remove task")
    print("4) Mark task complete")
    print("5) Exit")
    choice = input("> Choose an option: ").strip()

    if choice == "1":
        text = input("Enter task: ").strip()
        if text == "":
            print("  ! Task cannot be empty.")
            continue
        tasks.append({"text": text, "done": False})
        save_tasks(tasks)
        print(f"  + Added: {text}")

    elif choice == "2":
        print("-" * 40)
        if not tasks:
            print("  No tasks yet.")
        for i, task in enumerate(tasks, start=1):
            mark = "x" if task["done"] else " "
            print(f"  {i}. [{mark}] {task['text']}")
        print("-" * 40)

    elif choice == "3":
        raw = input("Enter task number to remove: ").strip()
        try:
            index = int(raw)
        except ValueError:
            print("  ! Please enter a valid number.")
            continue
        if index < 1 or index > len(tasks):
            print("  ! No task with that number.")
            continue
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"  - Removed: {removed['text']}")

    elif choice == "4":
        raw = input("Enter task number to mark complete: ").strip()
        try:
            index = int(raw)
        except ValueError:
            print("  ! Please enter a valid number.")
            continue
        if index < 1 or index > len(tasks):
            print("  ! No task with that number.")
            continue
        tasks[index - 1]["done"] = True
        save_tasks(tasks)
        print(f"  + Marked complete: {tasks[index - 1]['text']}")

    elif choice == "5":
        break

    else:
        print("  ! Invalid option. Please choose 1-5.")

print("\nGoodbye!")
