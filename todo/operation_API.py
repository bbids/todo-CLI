import logging
import os

# getch allows us to read a character
# from getch import getch

from todo.args_parser import parse_arguments
# from todo.constants import Colors
import todo.database as database

class Operation_API:

    def __init__(self, testingArgs = None):
        if testingArgs is None:
            self.args = parse_arguments()
        else:
            # for testing purposes
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
            case "update":
                self.update()
            case "interact":
                self.interact()
            case "reset_ids":
                self.reset_ids()
            case "set":
                self.set()
            case "get":
                self.get()
            case _:
                # argsparser should catch it, this is for tests
                logging.error("Unknown command")

    def add(self):
        prio = "not specified" if self.args.prio is None else self.args.prio
        database.add_task(self.args.task, prio)

    def read(self):
        database.show_tasks()

    def remove(self):
        database.remove_task(self.args.taskID)

    def update(self):
        id = self.args.taskID
        new_content = None if self.args.cont is None else self.args.cont
        new_priority = None if self.args.prio is None else self.args.prio
        database.update_task(id, new_content, new_priority)
    
"""
    def remove(self):
        try:
            Operation.remove_task(int(self.args.taskID))
        except ValueError:
            logging.error("invalid literal for taskID, an integer type")

    def create(self):
        if os.path.isfile(os.path.join(os.getcwd(), FileConstants.TODO)):
            while True:
                ans = input(f"The {Colors.RED}todo file{Colors.DEFAULT} is already present in the current directory. " 
                            "Do you want to override?\nY/N: ")
                match ans.lower():
                    case 'y':
                        Operation.create_todo_file()
                        break
                    case 'n':
                        logging.info("Skipped todo file creation.")
                        break
                    case _:
                        continue
        else:
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

    def set(self):
        path = self.args.todoDir

        match path:
            case ".":
                path = os.getcwd()
                Config.set_todo_file(os.path.join(path, FileConstants.TODO))
            case _:
                if os.path.isdir(path):
                    Config.set_todo_file(os.path.join(path, FileConstants.TODO))
                else:
                    logging.error(f"{path} is not a a valid directory")

    def get(self):
        logging.info("Printing the currently focused todo file:")
        print(Config.get_todo_file_path())
"""