import os
import pickle
from datetime import datetime

class Task:
    def __init__(self, title, description, due_date=None):
        self.title = title
        self.description = description
        self.completed = False
        self.creation_date = datetime.now()
        self.due_date = due_date

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def list_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            status = "Completed" if task.completed else "Not Completed"
            print(f"{i}. {task.title} - {task.description} - Due: {task.due_date} - {status}")

    def mark_completed(self, task):
        task.completed = True

    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.tasks, file)

    def load_from_file(self, filename):
        if os.path.exists(filename):
            with open(filename, 'rb') as file:
                self.tasks = pickle.load(file)

def main():
    todo_list = ToDoList()

    filename = "todo_list.pkl"
    todo_list.load_from_file(filename)

    while True:
        print("\n==== To-Do List ====")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("5. Save and Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (optional, format: YYYY-MM-DD): ")
            
            if due_date:
                due_date = datetime.strptime(due_date, "%Y-%m-%d")

            new_task = Task(title, description, due_date)
            todo_list.add_task(new_task)
            print("Task added successfully!")

        elif choice == "2":
            todo_list.list_tasks()

        elif choice == "3":
            todo_list.list_tasks()
            task_index = int(input("Enter the task number to mark as completed: ")) - 1
            selected_task = todo_list.tasks[task_index]
            todo_list.mark_completed(selected_task)
            print("Task marked as completed!")

        elif choice == "4":
            todo_list.list_tasks()
            task_index = int(input("Enter the task number to remove: ")) - 1
            selected_task = todo_list.tasks[task_index]
            todo_list.remove_task(selected_task)
            print("Task removed successfully!")

        elif choice == "5":
            todo_list.save_to_file(filename)
            print("To-Do List saved. Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
]