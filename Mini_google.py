class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_as_completed(self, task):
        if task in self.tasks:
            print(f"Task '{task}' marked as completed.")
            self.tasks.remove(task)
        else:
            print(f"Task '{task}' not found.")

    def view_tasks(self):
        print("\nTo-Do List:")
        for task in self.tasks:
            print(f"- {task}")


def main_todo_list():
    todo_list = ToDoList()

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. View Tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter task to mark as completed: ")
            todo_list.mark_as_completed(task)
        elif choice == '3':
            todo_list.view_tasks()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_todo_list()

