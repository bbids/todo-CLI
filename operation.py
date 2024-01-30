import os
import sys
import logging
import json

from utility import read_json_file
from utility import get_new_task
from utility import get_config_template
from config import Config

from constants import TodoKeys
from constants import TaskKeys
from constants import FileConstants

class Operation:
    """Namespace for available operations"""

    def create_todo_file():
        """Create a hidden todo file for non-volatile storage purposes, configure the config to use this new file."""
        todo_file_path = os.path.join(os.getcwd(), FileConstants.TODO)
        logging.info(f"creating todo_data at {todo_file_path}")
        Config.set_todo_file(todo_file_path)
        logging.info(f"config.json: changed todo file location to {todo_file_path}")


        with open(todo_file_path, "w") as f:
            data = get_config_template()
            json.dump(data, f, indent=4)

        logging.info(f"File successfuly created.")

    def add_task(content = "", priority = 0):
        """Add a task to JSON-formatted file """
        todo_file_path = Config.get_todo_file_path()
        data = read_json_file(todo_file_path)
        tasks = data[TodoKeys.KEY_TASKS]

        # to be changed with addition of remove
        id = (int(tasks[-1][TaskKeys.KEY_ID]) + 1) if len(tasks) > 0 else 0

        # task format as specified by the documentation
        new_task = get_new_task(id, priority, content, None, None) 
        tasks.append(new_task)

        with open(todo_file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def display_tasks():
        """Display the tasks in a pretty way."""
        todo_file_path = Config.get_todo_file_path()
        data = read_json_file(todo_file_path)

        # Not so pretty right now, but this can come later
        for task in data[TodoKeys.KEY_TASKS]:
            print(task)

    def remove_task(taskID):
        """Remove the task with given ID of int type"""
        todo_file_path = Config.get_todo_file_path()
        data = read_json_file(todo_file_path)
        tasks = data[TodoKeys.KEY_TASKS]

        # ID's are not changed, this is a design decision, although it might change in the future
        data[TodoKeys.KEY_TASKS] = [item for item in tasks if item[TaskKeys.KEY_ID] != taskID]

        len_before = len(tasks)
        len_after = len(data[TodoKeys.KEY_TASKS])
        if len_after < len_before:
            logging.info(f"Task with ID:{taskID} succesfuly deleted")
            with open(todo_file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
        else:
            logging.error(f"Task with ID:{taskID} not found.")

    def reset_ids():
        """Reset the task IDs"""
        todo_file_path = Config.get_todo_file_path()
        data = read_json_file(todo_file_path)

        id = 0
        for item in data[TodoKeys.KEY_TASKS]:
            item[TaskKeys.KEY_ID] = id
            id += 1
        
        with open(todo_file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

if __name__ == "__main__":
    Operation.remove_single_task(1)