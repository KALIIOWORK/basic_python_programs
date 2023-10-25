todos = {}

def add_task(task, todos):
    todos[task] = {'completed': False}

def mark_completed(task, todos):
    if task in todos:
        todos[task]['completed'] = True
    else:
        print("Task not found")

def remove_task(task, todos):
    if task in todos:
        del todos[task]
    else:
        print("Task not found")

def list_tasks(todos):
    print("To-Do List: ")
    i = 1
    for task, info in todos.items():
        status = '✓' if info['completed'] else ' '
        print(f"{i} [{status}] {task}")
        i += 1

def program():
    while True:

        print("\nMenu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. View List")
        print("0. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(task, todos)
        elif choice == "2":
            task = input("Enter the task to remove: ")
            remove_task(task, todos)
        elif choice == "3":
            task = input("Enter the task to mark as completed: ")
            mark_completed(task, todos)
        elif choice == "4":
            list_tasks(todos)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")
            
program()