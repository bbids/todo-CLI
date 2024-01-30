import os
import sys
import logging
import json

from utility import read_json_file
from config import config_rewrite_current_todo
from config import config_get_current_todo

from constants import TodoKeys
from constants import TaskKeys
from constants import FileConstants

def create_todo_file(todo_file_path = None):
    """Create a hidden todo file for non-volatile storage purposes, configure the config to use this new file."""
    # Although we have custom todo file paths, this is likely to be deprecated.
    # It future update it will be encouraged that the user specifies the working directory of the new todo file beforehand.
    #if todo_file_path is None:
    todo_file_path = os.path.join(os.getcwd(), FileConstants.TODO)
    #else:
    #    # make sure the directory is valid
    #    todo_dir = os.path.dirname(todo_file_path)
    #    if not os.path.exists(todo_dir):
    #        logging.error(f"File path '{todo_file_path}' is not valid.")
    #        sys.exit()

    logging.info(f"creating todo_data at {todo_file_path}")
    config_rewrite_current_todo(todo_file_path)
    logging.info(f"config.json: change current To-Do to {todo_file_path}")


    with open(todo_file_path, "w") as f:
        data = {
            TodoKeys.KEY_TASKS : []
        }
        json.dump(data, f, indent=4)

    logging.info(f"File successfuly created.")

def add_task(content = "", priority = 0):
    """Add a task to JSON-formatted file """
    todo_file_path = config_get_current_todo()
    data = read_json_file(todo_file_path)
    tasks = data[TodoKeys.KEY_TASKS]

    # to be changed with addition of remove
    id = (int(tasks[-1][TaskKeys.KEY_ID]) + 1) if len(tasks) > 0 else 0

    # task format as specified by the documentation
    new_task = {
        "ID": id,
        "Priority": priority,
        "Content": content,
        "DueDate": None,
        "Category": None,
    }
    tasks.append(new_task)

    with open(todo_file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def display_tasks():
    """Display the tasks in a pretty way."""
    todo_file_path = config_get_current_todo()
    data = read_json_file(todo_file_path)
    
    # Not so pretty right now, but this can come later
    for task in data[TodoKeys.KEY_TASKS]:
        print(task)

def remove_single_task(taskID):
    """Remove the task with given ID of int type"""
    todo_file_path = config_get_current_todo()
    data = read_json_file(todo_file_path)
    tasks = data[TodoKeys.KEY_TASKS]

    # ID's are not changed, this is a design decision, although it might change in the future
    data[TodoKeys.KEY_TASKS] = [item for item in tasks if item[TaskKeys.KEY_ID] != taskID]

    len_before = len(tasks)
    len_after = len(data[TodoKeys.KEY_TASKS])
    if len_after < len_before:
        logging.info(f"Task with ID:{taskID} succesfuly deleted")
        with open(todo_file_path, "w", encoding="utf-8") as f:
            json.dump(data, f)
    else:
        logging.error(f"Task with ID:{taskID} not found.")

if __name__ == "__main__":
    remove_single_task(1)