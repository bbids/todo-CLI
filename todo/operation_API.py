import logging
import os

# getch allows us to read a character
from getch import getch

from todo.args_parser import parse_arguments
from todo.operation import Operation
from todo.config import Config

class Operation_API:

    def __init__(self):
        self.args = parse_arguments()

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
            case "update":
                self.update()
            case "interact":
                self.interact()
            case "reset_ids":
                self.reset_ids()
            case "config":
                Config.check_todo_existence()
                self.config()
            case _:
                logging.debug("???")

    def add(self):
        logging.info(f"Adding '{self.args.task}'")
        prio = 5 if self.args.prio is None else self.args.prio
        Operation.add_task(self.args.task, prio)

    def read(self):
        Operation.display_tasks()

    def remove(self):
        try:
            Operation.remove_task(int(self.args.taskID))
        except ValueError:
            logging.error("invalid literal for taskID, an integer type")

    def create(self):
        Operation.create_todo_file()

    def update(self):
        id = int(self.args.taskID)
        new_content = None if self.args.cont is None else self.args.cont
        new_priority = None if self.args.prio is None else int(self.args.prio)
        Operation.update_task(id, new_content, new_priority)

    def reset_ids(self):
        Operation.reset_ids()

    def interact(self):
        i = 0
        os.system("clear")
        Operation.display_tasks_interactive(i)
        while True:
            ch = getch()

            match ch:
                case "w":
                    os.system("clear")
                    i += 1
                    i = Operation.display_tasks_interactive(i)
                case "s":
                    os.system("clear")
                    i -= 1 
                    i = Operation.display_tasks_interactive(i)
                case "c":
                    os.system("clear")
                    print("cleared :P")
                case "d":
                    Operation.remove_task_interactive(i)
                    os.system("clear")
                    i = Operation.display_tasks_interactive(i)
                case _:
                    break

    def config(self):
        Config.run()