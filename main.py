#!/usr/bin/python3
import sys
import logging

from args_parser import parse_arguments

from config import config_exists
from config import config_setup

from operation_functions import create_todo_file
from operation_functions import add_task
from operation_functions import display_tasks


def main():
    logging.basicConfig(level=logging.DEBUG)

    # Absolutely necessary to have a config file
    if not config_exists():
        config_path = config_setup()
        logging.info(f"Config file not found. Creating a config file at {config_path}")

    # if args not specified, should really have a nice "Written by bbids @github"
    if len(sys.argv) == 1:
        print("-h for help")
        sys.exit()

    # parse the commands
    args = parse_arguments()

    # pythonic switch
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

if __name__ == "__main__":
    main()

    # init, create the task in the current directory
    # move, choose the new path for some todo
    # show, show the available todo files
    # config, show the config file
    # update
    # optional: verbose, set logging level
        
    # if not specified the script looks at the current folder if .todo_file is present