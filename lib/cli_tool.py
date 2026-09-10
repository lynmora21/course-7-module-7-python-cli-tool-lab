# cli_tool.py

import argparse

from .models import Task, User


# In-memory storage for users
users = {}


def get_or_create_user(username):
    """Return an existing user or create a new one."""
    if username not in users:
        users[username] = User(username)

    return users[username]


def add_task(args):
    """Add a new task for a user."""
    user = get_or_create_user(args.user)

    # Prevent empty task titles
    if not args.title.strip():
        print("❌ Task title cannot be empty.")
        return

    # Prevent duplicate tasks
    for task in user.tasks:
        if task.title.lower() == args.title.lower():
            print(f"❌ Task '{args.title}' already exists for {args.user}.")
            return

    task = Task(args.title)
    user.add_task(task)


def list_tasks(args):
    """List all tasks for a user."""
    user = users.get(args.user)

    if user is None:
        print(f"❌ User '{args.user}' not found.")
        return

    user.list_tasks()


def complete_task(args):
    """Mark a user's task as completed."""
    user = users.get(args.user)

    if user is None:
        print(f"❌ User '{args.user}' not found.")
        return

    for task in user.tasks:
        if task.title.lower() == args.title.lower():
            task.complete()
            return

    print(f"❌ Task '{args.title}' not found for {args.user}.")


def main():
    """Set up the command-line interface."""
    parser = argparse.ArgumentParser(
        description="Task Manager CLI - Manage your tasks from the terminal."
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )

    # Add task command
    add_parser = subparsers.add_parser(
        "add-task",
        help="Add a new task for a user."
    )
    add_parser.add_argument(
        "user",
        help="Name of the user."
    )
    add_parser.add_argument(
        "title",
        help="Title of the task."
    )
    add_parser.set_defaults(func=add_task)

    # List tasks command
    list_parser = subparsers.add_parser(
        "list-tasks",
        help="List all tasks for a user."
    )
    list_parser.add_argument(
        "user",
        help="Name of the user."
    )
    list_parser.set_defaults(func=list_tasks)

    # Complete task command
    complete_parser = subparsers.add_parser(
        "complete-task",
        help="Mark a task as completed."
    )
    complete_parser.add_argument(
        "user",
        help="Name of the user."
    )
    complete_parser.add_argument(
        "title",
        help="Title of the task to complete."
    )
    complete_parser.set_defaults(func=complete_task)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
