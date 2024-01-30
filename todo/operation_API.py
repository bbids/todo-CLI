import logging

from todo.args_parser import parse_arguments
from todo.operation import Operation


class Operation_API:

    def __init__(self, testingArgs = None):
        if testingArgs is None:
            self.args = parse_arguments()
        else:
            # parsing is done in the test module, with additional content added
            # manually to simulate running in CLI
            self.args = testingArgs

    def execute(self):
        # pythonic switch
        logging.debug(f"{self.args.operation} was used")
        match self.args.operation:
            case "create":
                self.create()
            case "remove":
                self.remove()
            case "add":
                self.add()
            case "read":
                self.read()
            case "reset_ids":
                self.reset_ids()
            case _:
                # parser should catch it already,
                # this is really intended for tests, beside nice to have default
                logging.error("Unknown command.")

    def add(self):
        logging.info(f"Adding '{self.args.task}'")
        Operation.add_task(self.args.task, 5)

    def read(self):
        Operation.display_tasks()

    def remove(self):
        try:
            Operation.remove_task(int(self.args.taskID))
        except ValueError:
            logging.error("invalid literal for taskID, an integer type")

    def create(self):
        Operation.create_todo_file()

    def reset_ids(self):
        Operation.reset_ids()

    