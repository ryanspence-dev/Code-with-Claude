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
    choice = input("> Choose an option: ")

    if choice == "1":
        text = input("Enter task: ")
        tasks.append({"text": text, "done": False})
        save_tasks(tasks)
        print(f"  + Added: {text}")

    elif choice == "2":
        print("-" * 40)
        for i, task in enumerate(tasks, start=1):
            mark = "x" if task["done"] else " "
            print(f"  {i}. [{mark}] {task['text']}")
        print("-" * 40)

    elif choice == "3":
        index = int(input("Enter task number to remove: "))
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"  - Removed: {removed['text']}")

    elif choice == "4":
        index = int(input("Enter task number to mark complete: "))
        tasks[index - 1]["done"] = True
        save_tasks(tasks)
        print(f"  + Marked complete: {tasks[index - 1]['text']}")

    elif choice == "5":
        break

print("\nGoodbye!")
