import os
import sys
import logging
import json

from utility import get_data
from constants import TODO_FILE

def create_todo_file(todo_file_path = None):
    """Create a hidden todo file for non-volatile storage purposes."""
    if todo_file_path is None:
        todo_file_path = os.path.join(os.getcwd(), TODO_FILE)
    else:
        # make sure the directory is valid
        todo_dir = os.path.dirname(todo_file_path)
        if not os.path.exists(todo_dir):
            logging.error(f"File path '{todo_file_path}' is not valid.")
            sys.exit()

    logging.info(f"Creating todo_data at {todo_file_path}")

    with open(todo_file_path, "w") as f:
        f.write("{\n    \"tasks\": []\n}")

    logging.info(f"File successfuly created.")

def add_task(content = "", priority = 0, path = None):
    """Add a task to JSON-formatted file """
    if path is None:
        path = os.getcwd()
    
    file_name = os.path.join(path, TODO_FILE)

    data = get_data(file_name)
    tasks = data["tasks"]

    id = (int(tasks[-1]["ID"]) + 1) if len(tasks) > 0 else 0
    new_task = {
        "ID": id,
        "Priority": priority,
        "Content": content,
        "DueDate": None,
        "Category": None,
    }
    tasks.append(new_task)

    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def display_tasks(path = None):
    """Display the tasks in a pretty way."""
    if path is None:
        path = os.getcwd()

    file_name = os.path.join(path, TODO_FILE)

    data = get_data(file_name)
    
    for task in data["tasks"]:
        print(task)