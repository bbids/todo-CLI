import logging

from .args_parser import parse_arguments
from . import operations as operation
from . import database as database


class Operation_API:
    def __init__(self, testingArgs=None):
        #if testingArgs is None:
        self.args = parse_arguments()
        #else:
            # for testing purposes
        #    self.args = testingArgs

    def execute(self):
        # pythonic switch
        logging.debug(f"{self.args.operation} was used")
        match self.args.operation:
            # case "create":
            #     self.create()
            case "remove":
                self.remove()
            case "add":
                self.add()
            case "read":
                self.read()
            case "update":
                self.update()
            # case "interact":
            #     self.interact()
            # case "reset_ids":
            #     self.reset_ids()
            # case "set":
            #     self.set()
            # case "get":
            #     self.get()
            # case _:
                # argsparser should catch it, this is for tests
            #    logging.error("Unknown command")

    def add(self):
        prio = "not specified" if self.args.prio is None else int(self.args.prio)
        database.add_task(self.args.task, prio)

    def read(self):
        tasks = database.show_tasks()
        operation.display_tasks(tasks)

    def remove(self):
        database.remove_task(self.args.taskID)

    def update(self):
        id = self.args.taskID
        new_content = None if self.args.cont is None else self.args.cont
        new_priority = None if self.args.prio is None else int(self.args.prio)
        database.update_task(id, new_content, new_priority)
