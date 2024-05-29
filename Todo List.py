import cmd

class ToDoList(cmd.Cmd):
  intro = "Welcome to your To-Do List!"
  prompt = "(To-Do) >> "

  def do_add(self, arg):
    """Add a new task."""
    self.tasks.append(arg)
    print(f"Task '{arg}' added!")

  def do_list(self, arg):
    """List all tasks."""
    if not self.tasks:
      print("No tasks found.")
    else:
      for i, task in enumerate(self.tasks):
        print(f"{i+1}. {task}")

  def do_done(self, arg):
    """Mark a task as completed."""
    try:
      index = int(arg) - 1
      if self.tasks[index]:
        del self.tasks[index]
        print(f"Task '{arg}' marked as completed!")
      else:
        print(f"Task '{arg}' not found.")
    except IndexError:
      print("Invalid task number.")

  def do_exit(self, arg):
    """Exit the application."""
    print("Exiting...")
    exit()

  def emptyline(self):
    """Handle empty line input."""
    pass

if __name__ == "__main__":
  # Load tasks from a file (optional)
  tasks = []
  # ...

  # Start the command-line interface
  ToDoList().cmdloop()
