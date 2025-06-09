tasks = []

def display_tasks():
    if len(tasks) == 0:
        print("No tasks to display.")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added!")

def delete_task():
    display_tasks()
    if len(tasks) > 0:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            print(f"Task '{deleted_task}' deleted!")
        else:
            print("Invalid task number!")

while True:
    print("\nOptions:")
    print("1. display Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        display_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
