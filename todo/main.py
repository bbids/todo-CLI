import sys
import logging

from todo.config import Config
from todo.operation_API import Operation_API

def main():
    logging.basicConfig(level=logging.INFO)

    # Absolutely necessary to have a config file
    if not Config.exists():
        config_file_path = Config.create()
        logging.info(f"Config file not found. Creating a config file at {config_file_path}")

    # if args not specified, should really have a nice "Written by bbids @github"
    if len(sys.argv) == 1:
        print("-h for help")
        sys.exit()

    operator = Operation_API()
    operator.execute()

if __name__ == "__main__":
    main()

    # consider termcolor for pretty output

    # init, create the task in the current directory
    # move, choose the new path for some todo
    # show, show the available todo files
    # config, show the config file
    # update
    # optional: verbose, set logging level
        
    # if not specified the script looks at the current folder if .todo_file is present