import json
import os
from datetime import datetime


# File to store tasks
tasks_file = 'tasks.json'


# Task class to handle task properties
class Task:
    def __init__(self, description, due_date=None, priority=None, completed=False):
        self.description = description
        self.completed = completed
        self.due_date = due_date
        self.priority = priority


    def to_dict(self):
        return {
            "description": self.description,
            "due_date": self.due_date,
            "priority": self.priority,
            "completed": self.completed
        }
    

    @staticmethod
    def from_dict(task_dict):
        return Task(
            description=task_dict["description"],
            due_date=task_dict.get("due_date"),
            priority=task_dict.get("priority"),
            completed=task_dict.get("completed", False)
        )
    

# TO-DO-LIST class to manage the list of tasks
class ToDoList:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    
    def add_task(self, description, due_date=None, priority=None):
        task = Task(description, due_date, priority)
        self.tasks.append(task)
        self.save_tasks()

    
    def vew_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for i, task in enumerate(self.tasks, 1):
                status = "Completed" if task.completed else "Pending"
                print(f"{i}. {task.description} - Due: {task.due_date} - Priority: {task.priority} - Status: {status}")

    def mark_task_as_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            self.save_tasks()


    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_tasks()


    def save_tasks(self):
        with open(tasks_file, "w") as file:
            tasks_dict = [task.to_dict() for task in self.tasks]
            json.dump(tasks_dict, file, indent=4)


    def load_tasks(self):
        if os.path.exists(tasks_file):
            with open(tasks_file, "r") as file:
                tasks_dict = json.load(file)
                self.tasks = [Task.from_dict(task_dict) for task_dict in tasks_dict]


def main():
    todo_list = ToDoList()

    while True:
        print("\nTO-DO LIST MENU")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ") or None
            priority = input("Enter priority (High, Medium, Low): ") or None
            todo_list.add_task(description, due_date, priority)
        elif choice == "2":
            todo_list.vew_tasks()
        elif choice == "3":
            index = int(input("Enter task index to mark as completed: "))
            todo_list.mark_task_as_completed(index - 1)
        elif choice == "4":
            index = int(input("Enter task index to delete: "))
            todo_list.delete_task(index - 1)
        elif choice == "5":
            print("Exiting...\nGOODBYE")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
