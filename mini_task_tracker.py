"""Mini Task Tracker - AI Engineering Week 1, Day 2.

A menu-based task manager that stores tasks in tasks.json
and reloads them when the program is run again.
"""

import json

TASKS_FILE = "tasks.json"

# Each task is stored as {"title": "...", "done": False}
tasks = []


def load_tasks():
    """Load tasks from tasks.json; return an empty list if missing or broken."""
    try:
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        # First run: no file yet, so start with an empty list
        return []
    except json.JSONDecodeError:
        print("Warning: tasks.json is corrupted. Starting with an empty list.")
        return []


def save_tasks():
    """Save the current task list to tasks.json."""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def add_task():
    """Ask for a title and store the new task as Pending."""
    title = input("Task title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return
    tasks.append({"title": title, "done": False})
    save_tasks()
    print("Task added.")


def view_tasks():
    """Show a numbered list of tasks with Pending or Done status."""
    if not tasks:
        print("No tasks yet.")
        return
    for number, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Pending"
        print(f"{number}. {task['title']} [{status}]")


def get_task_index():
    """Ask for a task number; return its list index, or None if invalid."""
    if not tasks:
        print("No tasks available.")
        return None
    try:
        number = int(input("Task number: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None
    if number < 1 or number > len(tasks):
        print(f"Invalid task number. Choose between 1 and {len(tasks)}.")
        return None
    return number - 1


def complete_task():
    """Mark the selected task as done."""
    index = get_task_index()
    if index is None:
        return
    tasks[index]["done"] = True
    save_tasks()
    print("Task completed.")


def delete_task():
    """Remove the selected task."""
    index = get_task_index()
    if index is None:
        return
    removed = tasks.pop(index)
    save_tasks()
    print(f"Task deleted: {removed['title']}")


def main():
    global tasks
    tasks = load_tasks()

    # Keep showing the menu until the user chooses Exit
    while True:
        print("\n--- TASK TRACKER ---")
        print("1. Add  2. View  3. Complete  4. Delete  5. Exit")
        choice = input("Choice: ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
