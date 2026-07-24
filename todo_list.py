class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True


tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        description = input("Enter task description: ")
        tasks.append(Task(description))
        print("Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                status = "✓ Completed" if task.completed else "✗ Pending"
                print(f"{i}. {task.description} - {status}")

    elif choice == "3":
        if not tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                status = "✓ Completed" if task.completed else "✗ Pending"
                print(f"{i}. {task.description} - {status}")

            try:
                task_num = int(input("Enter task number to mark as completed: "))
                if 1 <= task_num <= len(tasks):
                    tasks[task_num - 1].mark_completed()
                    print("Task marked as completed!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        print("Thank you for using the To-Do List App!")
        break

    else:
        print("Invalid choice. Please try again.")