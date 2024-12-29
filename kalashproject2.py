class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = {"description": description, "completed": False}
        self.tasks.append(task)

    def view_tasks(self):
        if not self.tasks:
            print("No tasks to display.")
        else:
            for i, task in enumerate(self.tasks, 1):
                status = "Completed" if task["completed"] else "Not Completed"
                print(f"{i}. {task['description']} - {status}")

    def mark_task_completed(self, task_number):
        try:
            task = self.tasks[task_number - 1]
            task["completed"] = True
            print(f"Task '{task['description']}' marked as completed.")
        except IndexError:
            print("Invalid task number.")

    def delete_task(self, task_number):
        try:
            task = self.tasks.pop(task_number - 1)
            print(f"Task '{task['description']}' deleted successfully.")
        except IndexError:
            print("Invalid task number.")

def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            description = input("Enter the task description: ")
            task_manager.add_task(description)
            print("Task added successfully.")

        elif choice == "2":
            task_manager.view_tasks()

        elif choice == "3":
            task_manager.view_tasks()
            task_number = int(input("Enter task number to mark as completed: "))
            task_manager.mark_task_completed(task_number)

        elif choice == "4":
            task_manager.view_tasks()
            task_number = int(input("Enter task number to delete: "))
            task_manager.delete_task(task_number)

        elif choice == "5":
            print("Exiting task manager...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
