__version__ = "2.2.0"

import os
from enum import Enum
from task_manager import TaskManager
from task_manager import Choice

FILE_NAME="tasks_file.txt"

manager = TaskManager()

CHOICE = Choice

class Menu(Enum):
        EXIT="0"
        ADD="1"
        LIST_ALL="2"
        LIST_COMPLETED="3"
        LIST_UNCOMPLETED="4"
        SEARCH_BY_KEYWORD="5"
        MARK="6"
        EDITE="7"
        DELETE="8"
        SAVE="9"
        LOAD="10"
        MENU="m"


def menu():
    print("[1] . Add task")
    print("[2] . List all tasks")
    print("[3] . List completed tasks")
    print("[4] . List uncompleted tasks")
    print("[5] . Search task by keyword")
    print("[6] . Mark task as done")
    print("[7] . Edite task name")
    print("[8] . Delete task")
    print("[9] . Save")
    print("[10]. Load")
    print("[0] . Exit")

menu()
while True:
    print()
    print("[m] Menu")
    choice = input(">")
    
    match choice:
        case Menu.MENU.value:
            menu()
        case Menu.EXIT.value:
                if not manager.UP_TO_DATE:
                    exit_choice="3"
                    print("Warning: Unsaved changes!")
                    print("1. Save")
                    print("2. Discard")
                    print("3. Cancel")
                    exit_choice = input(">")
                    if exit_choice == "1":
                        manager.save_tasks(FILE_NAME)
                        print("✓ Data synchronized to disk.")
                        print("Exiting...")
                        break
                    elif exit_choice == "2":
                        print("Changes discarded.")
                        print("Exiting...")
                        break
                    else:
                        print("✗ Failed to Exit.")
                else:
                    break

        case Menu.ADD.value:
            task_name = input("Enter task name: ").strip()
            if not task_name:
                print("Empty task name not allowed!")
                continue
            
            priority = input("choose task priority (1-3): ")
            if not ("1" <= priority <= "3"):
                print("Invalid priority!")
                continue

            priority = int(priority)
            if manager.add_task(task_name, priority):
                print("Task added successfully.")
            else:
                print("Task already exist!")

        case Menu.LIST_ALL.value:
            if manager.tasks:
                print(f"\n--- ({len(manager.tasks)}) Task ---")
                
                for task_name, info in manager.get_tasks(CHOICE.ALL.value):
                    status = "✓ Completed" if info["done"] else "✗ Pending"
                    print(f"[{status}] {task_name}")
            else:
                print("No taskes yet!")

        case Menu.LIST_COMPLETED.value:
            if manager.tasks:
                completed_tasks = manager.get_tasks(CHOICE.COMPLETED.value)

                if not completed_tasks:
                    print("No task has been completed yet!")
                    continue

                print(f"--- ✓ Completed tasks ({len(completed_tasks)}) ---")
                for task_name, _ in completed_tasks:
                    print(task_name)

            else:
                print("No taskes yet!")

        case Menu.LIST_UNCOMPLETED.value:
            if manager.tasks:
                uncompleted_tasks = manager.get_tasks(CHOICE.UNCOMPLETED.value)

                if not uncompleted_tasks:
                    print("All tasks has been completed!")
                    continue

                print(f"--- ✗ Pending tasks ({len(uncompleted_tasks)}) ---")
                for task_name, _ in uncompleted_tasks:
                    print(task_name)

            else:
                print("No taskes yet!")

        case Menu.SEARCH_BY_KEYWORD.value:
            keyword=input("Enter a keyword: ").strip()

            if not keyword:
                print("Error: Empty keyword is not allowed!")
                continue

            tasks = manager.get_tasks_by_keyword(keyword)

            if not tasks:
                print(f"No tasks found matching: '{keyword}'")

            print(f"\n--- Search Results ({len(tasks)}) ---")
            for task_name, info in tasks:
                status = "✓ Completed" if info["done"] else "✗ Pending"
                print(f"[{status}] {task_name}")

        case Menu.MARK.value:
            task_name = str(input("Enter task name: ")).strip()

            if manager.edit_task_status(task_name, True):
                print("Task marked as ✓ DONE")
            else:
                print("Task does not exist")

        case Menu.EDITE.value:
            old_name=input("Enter task name: ").strip()
            new_name=input("Enter a new name: ").strip()

            if not old_name or not new_name:
                print("Error: Task names cannot be empty!")
                continue

            if manager.edit_task_name(old_name, new_name):
               print(f"Success: '{old_name}' renamed to '{new_name}'.")
            else:
                print("Error: Could not rename. Either the task doesn't exist or the name is taken.")

        case Menu.DELETE.value:
            task_name=input("Enter task name: ").strip()

            task_data = manager.tasks.get(task_name)
            if not task_data:
                print("Error: Task does not exist!")
                continue

            should_delete = True
            if not task_data["done"]:
                print(f"Warning: Task '{task_name}' is still [✗ Pending]!")
                choice = input("Are you sure you want to delete? (y/n): ")
                if choice != "y":
                    should_delete = False

            if should_delete:
                if manager.delete_task(task_name):
                    print("Task deleted successfully.")
                else:
                    print("Error: Task could not be deleted.")
            else:
                print("Delete operation canceled.")

        case Menu.SAVE.value:
                
                if not manager.tasks:
                    confirm = input(f"Tasks list empty. Save anyway to clear file? (y/n): ").lower()
                    if confirm != 'y':
                        print("✗ Failed to save data.")
                        continue
                
                if manager.save_tasks(FILE_NAME):
                    print("✓ Data synchronized to disk.")
                else:
                    print("✗ Failed to save data.")

        case Menu.LOAD.value:

            if manager.tasks:
                print("Warning: unsaved data detected!")
                confirm = input("Are you sure you want to load? (y/n): ")
                if confirm != "y":
                    print("✗ Failed to load data.")
                    continue

            if manager.load_tasks(FILE_NAME):
                print("✓ Data loaded successfully.")
            else:
                print("✗ Failed to load data.")
                print(f"Error: '{FILE_NAME}' file does not exist.")

        case _:
            print("Error: Invalid choice!")

print()
