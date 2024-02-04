import sys
import logging
import os

from .operation_API import Operation_API
from . import database as database

def main():
    logging.basicConfig(level=logging.INFO)

    if not os.path.exists("todo.db"):
        database.create_table()

    # if args not specified, should really have a nice "Written by bbids @github"
    if len(sys.argv) == 1:
        print("-h for help")
        sys.exit()

    operator = Operation_API()
    operator.execute()

if __name__ == "__main__":
    main()