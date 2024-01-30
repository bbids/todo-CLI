#!/usr/bin/python3

from getpass import getuser
import os
import sys
import logging

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


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    if len(sys.argv) == 1:
        print("Usage: ...")
    else:
        create_todo_file()            