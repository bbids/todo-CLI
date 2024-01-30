import logging
import sys
import json

from constants import TodoKeys

def read_json_file(file_path):
    """Read json file and return data in dictionary form"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        logging.error("Trouble decoding the json file.\nExiting ...")
        sys.exit()
    except FileNotFoundError:
        logging.error("File not found.\nExiting ...")
        sys.exit()
    except TypeError:
        logging.error("config.json: Current-ToDo not specified correctly.\nExiting ...")
        sys.exit()

    return data   

def get_new_task(id, priority, content, due_date, category):
    """Return task as specified by the documentation """
    return {
            "ID": id,
            "Priority": priority,
            "Content": content,
            "DueDate": due_date,
            "Category": category,
        }

def get_config_template():
    """Return .config.json template as specified by the documentation"""
    return {
            TodoKeys.KEY_TASKS : []
        }