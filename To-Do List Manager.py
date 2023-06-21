tasks = []

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added.")

def view_tasks():
    if tasks:
        print("Task:")
        for index, task in enumerate(tasks):
            print(f"{index+1}. {task}")

    else:
        print("No tasks found.")

def remove_task():
    view_tasks()
    if tasks:
        index = int(input("Enter the task number to remove: "))-1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print(f"Removed tass: {removed_task}")
        else:
            print("Invalid task number.")
    else:
        print("No tasks found.")

while True:
    print("\nMenu:")
    print("1. Add a task")
    print("2. View task")
    print("3. Remove a task")
    print("4. Exit")

    choice = input ("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again. ")