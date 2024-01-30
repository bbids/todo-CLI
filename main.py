#!/usr/bin/python3

from getpass import getuser
import os
import sys
import logging
import argparse

def create_todo_file(todo_file_path = None):
    """Create a hidden todo file for storage purposes."""
    if todo_file_path is None:
        # todo_file_path = os.path.join("/home", getuser(), ".todo_data")
        # use temp directory for now
        todo_file_path = os.path.join("/home", getuser(), "temp", ".todo_data")
    
    todo_dir = os.path.dirname(todo_file_path)
    if not os.path.exists(todo_dir):
        logging.error(f"File path '{todo_file_path}' is not valid.")
        sys.exit()

    logging.info(f"Creating todo_data at {todo_file_path}")

    with open(todo_file_path, "w") as f:
        f.write("Hello, World!\n")

    logging.info(f"File successfuly created.")


def parse_arguments():
    parser = argparse.ArgumentParser()

    subparser = parser.add_subparsers(dest="operation",help="Available To-Do file operations")

    parser_create = subparser.add_parser("create", help="create new To-Do.")
    parser_create.add_argument("-p", "--path", help=f"Optional path for the todo file. Default is: /home/{getuser()}/")

    subparser.add_parser("read", help="read To-Do tasks")

    parser_add_task = subparser.add_parser("add", help="add task to To-Do")
    parser_add_task.add_argument("task", help="A quoted message to add to To-Do")

    parser_remove_task = subparser.add_parser("remove", help="remove task from To-Do")
    parser_remove_task.add_argument("taskID", help="A task ID, available in operation read")

    args = parser.parse_args()
    
    return args

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    if len(sys.argv) == 1:
        print("-h for help")

    args = parse_arguments()

    match args.operation:
        case "create":
            logging.debug("create was used")
        case "remove":
            logging.debug("remove was used")
        case "add":
            logging.debug("add was used")
            logging.info(f"Adding '{args.task}'")
        case "read":
            logging.debug("read was used")
        case _:
            logging.debug("???")