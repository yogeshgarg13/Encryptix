class TodoList:
  def __init__(self):
    self.tasks = []

  def add_task(self, task):
    self.tasks.append(task)

  def view_tasks(self):
    print("To-Do List")
    print("-----------")
    for i, task in enumerate(self.tasks, start=1):
      print(f"{i}. {task}")

  def update_task(self, task_index, new_task):
    if 0 <= task_index < len(self.tasks):
      self.tasks[task_index] = new_task

  def delete_task(self, task_index):
    if 0 <= task_index < len(self.tasks):
      del self.tasks[task_index]

def main():
  todo_list = TodoList()

  while True:
    print("To-Do List App")
    print("--------------")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = int(input("Enter your choice (1/2/3/4/5): "))

    if choice == 1:
      task = input("Enter the task: ")
      todo_list.add_task(task)

    elif choice == 2:
      todo_list.view_tasks()

    elif choice == 3:
      task_index = int(input("Enter the index of the task to update: ")) - 1
      if 0 <= task_index < len(todo_list.tasks):
        new_task = input("Enter the new task: ")
        todo_list.update_task(task_index, new_task)

    elif choice == 4:
      task_index = int(input("Enter the index of the task to delete: ")) - 1
      if 0 <= task_index < len(todo_list.tasks):
        todo_list.delete_task(task_index)

    elif choice == 5:
      break

    else:
      print("Invalid choice!")

if __name__ == "__main__":
  main()
