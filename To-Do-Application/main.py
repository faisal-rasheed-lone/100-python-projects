import json

# Define the Task class to represent individual tasks
class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def edit_task(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.title} ({self.due_date}) - {status}"

# Define the TaskList class to manage a list of tasks
class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Task List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def edit_task(self, task_index, title, description, due_date):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].edit_task(title, description, due_date)
            print("Task updated successfully.")
        else:
            print("Invalid task number.")

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f"Task '{removed_task.title}' removed.")
        else:
            print("Invalid task number.")

    def save_tasks_to_file(self, filename):
        with open(filename, 'w') as file:
            task_list_data = [{'title': task.title,
                               'description': task.description,
                               'due_date': task.due_date,
                               'completed': task.completed}
                              for task in self.tasks]
            json.dump(task_list_data, file)

    def load_tasks_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                task_list_data = json.load(file)
                self.tasks = [Task(task_data['title'],
                                   task_data['description'],
                                   task_data['due_date'])
                              for task_data in task_list_data]
            print("Tasks loaded from file.")
        except FileNotFoundError:
            print("No tasks found in the file.")
        except json.JSONDecodeError:
            print("Error decoding JSON data from file.")

# Main Application
if __name__ == "__main__":
    my_task_list = TaskList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4. Edit Task")
        print("5. Remove Task")
        print("6. Save Tasks to File")
        print("7. Load Tasks from File")
        print("8. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6/7/8): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date: ")
            task = Task(title, description, due_date)
            my_task_list.add_task(task)
            print("Task added successfully.")
        elif choice == "2":
            my_task_list.list_tasks()
        elif choice == "3":
            task_index = int(input("Enter the task number to mark as completed: ")) - 1
            my_task_list.tasks[task_index].mark_as_completed()
            print("Task marked as completed.")
        elif choice == "4":
            task_index = int(input("Enter the task number to edit: ")) - 1
            title = input("Enter new task title: ")
            description = input("Enter new task description: ")
            due_date = input("Enter new due date: ")
            my_task_list.edit_task(task_index, title, description, due_date)
        elif choice == "5":
            task_index = int(input("Enter the task number to remove: ")) - 1
            my_task_list.remove_task(task_index)
        elif choice == "6":
            filename = input("Enter the filename to save tasks: ")
            my_task_list.save_tasks_to_file(filename)
            print("Tasks saved to file.")
        elif choice == "7":
            filename = input("Enter the filename to load tasks from: ")
            my_task_list.load_tasks_from_file(filename)
        elif choice == "8":
            print("Exiting the To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
