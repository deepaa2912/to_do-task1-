#Description: Develop a command-line to-do list application that allows users to mana
#Features:
#1. Task Management: Allow users to add, remove, and mark tasks as completed.
#2. Task Priority: Implement a priority system for tasks (e.g., high, medium, low).
#3. Due Dates: Enable users to set due dates for tasks.
#4. List View: Display tasks in a list with their details.
#5. Data Persistence: Store tasks in a file/database for persistence across sessions.
#Tech Stack:
#Python
#File handling or a simple database library


import json
from datetime import datetime

TASKS_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            view_tasks(tasks)
        elif choice == "5":
            save_tasks(tasks)
            break
        else:
            print("Invalid choice. Please try again.")

def add_task(tasks):
    title = input("Enter task title: ")
    priority = input("Enter task priority (high, medium, low): ").lower()
    due_date = input("Enter due date (YYYY-MM-DD): ")
    
    task = {
        "title": title,
        "priority": priority,
        "due_date": due_date,
        "completed": False
    }
    
    tasks.append(task)
    print("Task added successfully!")

def remove_task(tasks):
    view_tasks(tasks)
    task_index = int(input("Enter the index of the task to remove: "))
    
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(f"Task '{removed_task['title']}' removed successfully!")
    else:
        print("Invalid index. Please try again.")

def mark_task_completed(tasks):
    view_tasks(tasks)
    task_index = int(input("Enter the index of the task to mark as completed: "))
    
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print(f"Task '{tasks[task_index]['title']}' marked as completed!")
    else:
        print("Invalid index. Please try again.")

def view_tasks(tasks):
    print("\nTasks:")
    for idx, task in enumerate(tasks):
        status = "Completed" if task["completed"] else "Not Completed"
        print(f"{idx}. {task['title']} - Priority: {task['priority']} - Due Date: {task['due_date']} - Status: {status}")

if __name__ == "__main__":
    main()
