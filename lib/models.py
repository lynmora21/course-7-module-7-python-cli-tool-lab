class Task:
    """Represents a task belonging to a user."""

    def __init__(self, title):
        self.title = title
        self.completed = False

    def complete(self):
        """Mark the task as completed."""
        if self.completed:
            print(f"ℹ️ Task '{self.title}' is already completed.")
        else:
            self.completed = True
            print(f"✅ Task '{self.title}' completed.")

    def __str__(self):
        status = "✅" if self.completed else "⬜"
        return f"{status} {self.title}"


class User:
    """Represents a user who can have multiple tasks."""

    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        """Add a task to the user's task list."""
        self.tasks.append(task)
        print(f"📌 Task '{task.title}' added to {self.name}.")

    def list_tasks(self):
        """Display all tasks belonging to the user."""
        if not self.tasks:
            print(f"ℹ️ {self.name} has no tasks.")
            return

        print(f"\nTasks for {self.name}:")
        for task in self.tasks:
            print(f"  {task}")
