#!/usr/bin/python3
import sys
import logging

from args_parser import parse_arguments
from operation_functions import create_todo_file
from operation_functions import add_task
from operation_functions import display_tasks


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    if len(sys.argv) == 1:
        print("-h for help")

    args = parse_arguments()

    match args.operation:
        case "create":
            logging.debug("create was used")
            create_todo_file()
        case "remove":
            logging.debug("remove was used")
        case "add":
            logging.debug("add was used")
            logging.info(f"Adding '{args.task}'")
            add_task(args.task, 5)
        case "read":
            logging.debug("read was used")
            display_tasks()
        case _:
            logging.debug("???")


        # init, create the task in the current directory
        # move, choose the new path for some todo
        # show, show the available todo files
        # config, show the config file
        # update
        # optional: verbose, set logging level
            
        # if not specified the script looks at the current folder if .todo_file is present