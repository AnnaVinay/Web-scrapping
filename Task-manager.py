import os
import json
from datetime import datetime

class TaskManager:
    def __init__(self, file_path='tasks.json'):
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                return json.load(file)
        return []

    def save_tasks(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.tasks, file, indent=2)

    def add_task(self, title, description):
        task = {
            'title': title,
            'description': description,
            'completed': False,
            'timestamp': datetime.now().isoformat()
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f'Task "{title}" added successfully.')

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return

        for index, task in enumerate(self.tasks, start=1):
            status = "Completed" if task['completed'] else "Not Completed"
            print(f"{index}. {task['title']} - {status}")

    def mark_completed(self, task_index):
        try:
            task = self.tasks[task_index - 1]
            task['completed'] = True
            self.save_tasks()
            print(f'Task "{task["title"]}" marked as completed.')
        except IndexError:
            print("Invalid task index. Please try again.")

# Example usage
if __name__ == "__main__":
    task_manager = TaskManager()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task_manager.add_task(title, description)
        elif choice == '2':
            task_manager.view_tasks()
        elif choice == '3':
            task_manager.view_tasks()
            index = int(input("Enter the task index to mark as completed: "))
            task_manager.mark_completed(index)
        elif choice == '4':
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
