import sys

# Initialize the task list
tasks = []

def print_welcome_message():
    """Display the welcome message."""
    print("Welcome to the To-Do List App!")

def print_menu():
    """Display the menu options."""
    print("\nMenu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

def add_task():
    """Add a new task to the list."""
    try:
        task = input("Enter the task description: ").strip()
        if task:
            tasks.append(task)
            print("Task added successfully.")
        else:
            print("Task description cannot be empty.")
    except Exception as e:
        print(f"An error occurred while adding the task: {e}")

def view_tasks():
    """Display all tasks in the list."""
    if tasks:
        print("\nYour tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks available.")

def mark_task_complete():
    """Mark a task as complete by adding 'X'."""
    try:
        view_tasks()
        task_index = int(input("Enter the task number to mark as complete: ").strip())
        if 1 <= task_index <= len(tasks):
            tasks[task_index - 1] += " [X]"
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred while marking the task as complete: {e}")

def delete_task():
    """Delete a task from the list."""
    try:
        view_tasks()
        task_index = int(input("Enter the task number to delete: ").strip())
        if 1 <= task_index <= len(tasks):
            tasks.pop(task_index - 1)
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred while deleting the task: {e}")

def quit_application():
    """Quit the application."""
    print("Thank you for using the To-Do List App. Goodbye!")
    sys.exit()

def main():
    """Main function to run the To-Do List Application."""
    print_welcome_message()
    while True:
        print_menu()
        try:
            choice = int(input("Select an option: ").strip())
            if choice == 1:
                add_task()
            elif choice == 2:
                view_tasks()
            elif choice == 3:
                mark_task_complete()
            elif choice == 4:
                delete_task()
            elif choice == 5:
                quit_application()
            else:
                print("Invalid option. Please select a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
